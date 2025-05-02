'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None

    def init(self):
        mem = [Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putLn",MType([],VoidType()),CName("io",True)),
                Symbol("getInt",MType([],IntType()),CName("io",True)),
                Symbol("getFloat",MType([],FloatType()),CName("io",True)),
                Symbol("getBool",MType([],BoolType()),CName("io",True)),
                Symbol("getString",MType([],StringType()),CName("io",True)),]
        return mem

    def gen(self, ast, dir_):
        print(ast)
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self, ast, c):
        env ={}
        env['env'] = [c]
        env['isLeft'] = False
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        self.emitObjectInit()
        self.emit.printout(self.emit.emitEPILOG())
        return env


    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    def visitVarDecl(self, ast, o):

        if 'frame' not in o: # global var
            o['env'][0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if ast.varInit:
                codegen = self.visit(ast.varInit, o)[0]
                self.emit.printout(codegen)
            else:
                if type(ast.varType) is FloatType:
                    self.emit.printout(self.emit.emitPUSHFCONST(0.0, frame))
                elif type(ast.varType) is IntType:
                    self.emit.printout(self.emit.emitPUSHICONST(0, frame))
                elif type(ast.varType) is BoolType:
                    self.emit.printout(self.emit.emitPUSHICONST(0, frame))
                else:
                    self.emit.printout(self.emit.emitPUSHNULL(frame))
    
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index,  frame))
        return o
    
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        env = o.copy()
        env['isLeft'] = False
        [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
        return o
    
    def visitBlock(self, ast, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if type(sym.value) is Index:
            if o['isLeft']:
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:
                return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:         
            if o['isLeft']:
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, 0, o['frame']), sym.mtype
            else:
                return self.emit.emitREADVAR(ast.name, sym.mtype, 0, o['frame']), sym.mtype
        
    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o['frame']), FloatType()
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()
    def visitBooleanLiteral(self, ast, o):
        if ast.value:
            return self.emit.emitPUSHICONST(1, o['frame']), BoolType()
        else:
            return self.emit.emitPUSHICONST(0, o['frame']), BoolType()
    
    def reduceNestedList(self, lst, arrTyp, eleTyp, o):
        # lst: list of literals
        # o: environment
        # ..., arrayref -> arrayref
        codegen = ''
        if isinstance(lst[0], list):
            codegen += self.emit.emitPUSHICONST(len(lst), o['frame'])
            codegen += self.emit.emitNEWARRAY(arrTyp, o['frame'])
            for i in range(len(lst)):
                codegen += self.emit.emitDUP(o['frame'])
                codegen += self.emit.emitPUSHICONST(i, o['frame'])
                codegen += self.reduceNestedList(lst[i], arrTyp, eleTyp, o)[0]
                codegen += self.emit.emitASTORE(arrTyp, o['frame'])
            return codegen, lst[0]
        else:
            return self.reduceList(lst, eleTyp, o)
    def reduceList(self, lst, eleTyp, o):
        # lst: list of literals
        # o: environment
        # ..., arrayref -> arrayref
        codegen = ''
        codegen += self.emit.emitPUSHICONST(len(lst), o['frame'])
        codegen += self.emit.emitNEWARRAY(eleTyp, o['frame'])
        for i in range(len(lst)):
            codegen += self.emit.emitDUP(o['frame'])
            codegen += self.emit.emitPUSHICONST(i, o['frame'])
            codegen += self.visit(lst[i], o)[0]
            codegen += self.emit.emitASTORE(eleTyp, o['frame'])
        return codegen, eleTyp


    def visitArrayLiteral(self, ast, o):
        codegen = ''
        
        if len(ast.dimens) == 1:
            codegen += self.reduceList(ast.value, ast.eleType, o)[0]
        else:
            codegen += self.reduceNestedList(ast.value, ArrayType(dimens=ast.dimens, eleType=ast.eleType), ast.eleType, o)[0]
        return codegen, ast.eleType
  
    def visitArrayCell(self, ast, o):
        codegen, arrType = self.visit(ast.arr, o)

        # Xác định kiểu trả về
        remaining_dims = len(arrType.dimens) - len(ast.idx)
        if remaining_dims == 0:
            for i in range(len(arrType.dimens)-1):
                codegen += self.visit(ast.idx[i], o)[0]
                codegen += self.emit.emitALOAD(ArrayType(arrType.dimens, arrType.eleType), o['frame'])
            codegen += self.visit(ast.idx[-1], o)[0]
            codegen += self.emit.emitALOAD(arrType.eleType, o['frame'])
            # Truy cập đến phần tử cuối cùng
            return codegen, arrType.eleType
        else:
            for i in range(len(arrType.dimens) - remaining_dims):
                codegen += self.visit(ast.idx[i], o)[0]
                codegen += self.emit.emitALOAD(ArrayType(arrType.dimens, arrType.eleType), o['frame'])

            # Trả về mảng với số chiều còn lại
            new_dimens = arrType.dimens[len(ast.idx):]
            return codegen, ArrayType(new_dimens, arrType.eleType)
        
    def visitStructLiteral(self, ast, o):
        pass
    def visitBinaryOp(self, ast, o):
        codegen = ''
        result = None
        if ast.op in ['+']:
            codeL, left = self.visit(ast.left, o)
            codeR, right = self.visit(ast.right, o)
            if type(left) is StringType and type(right) is StringType:
                codegen += codeL
                codegen += codeR
                result = StringType()
                codegen += self.emit.emitINVOKEVIRTUAL("java.lang.String/concat", MType([StringType()], StringType()), o['frame'])
            elif type(left) is IntType and type(right) is IntType:
                codegen += codeL
                codegen += codeR
                result = IntType()
                codegen += self.emit.emitADDOP('+',IntType(),o['frame'])
            elif type(left) is FloatType and type(right) is FloatType:
                codegen += codeL
                codegen += codeR
                result = FloatType()
                codegen += self.emit.emitADDOP('+',FloatType(),o['frame'])
            elif type(left) is IntType and type(right) is FloatType:
                codegen += codeL
                codegen += self.emit.emitI2F(o['frame'])
                codegen += codeR
                result = FloatType()
                codegen += self.emit.emitADDOP('+',FloatType(),o['frame'])
            elif type(left) is FloatType and type(right) is IntType:
                result = FloatType()
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitI2F(o['frame'])
                codegen += self.emit.emitADDOP('+',FloatType(),o['frame'])

        elif ast.op in ['-','*','/']:
            codeL, left = self.visit(ast.left, o)
            codeR, right = self.visit(ast.right, o)
            if type(left) is IntType and type(right) is IntType:
                result = IntType()
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitADDOP('-',result,o['frame']) if ast.op == '-' else self.emit.emitMULOP('*',result,o['frame']) if ast.op == '*' else self.emit.emitMULOP('/',result,o['frame'])

            elif type(left) is FloatType and type(right) is FloatType:
                result = FloatType()
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitADDOP('-',result,o['frame']) if ast.op == '-' else self.emit.emitMULOP('*',result,o['frame']) if ast.op == '*' else self.emit.emitMULOP('/',result,o['frame'])
            elif type(left) is IntType and type(right) is FloatType:
                result = FloatType()
                codegen += codeL
                codegen += self.emit.emitI2F(o['frame'])
                codegen += codeR
                codegen += self.emit.emitADDOP('-',result,o['frame']) if ast.op == '-' else self.emit.emitMULOP('*',result,o['frame']) if ast.op == '*' else self.emit.emitMULOP('/',result,o['frame'])
            elif type(left) is FloatType and type(right) is IntType:
                result = FloatType()
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitI2F(o['frame'])
                codegen += self.emit.emitADDOP('-',result,o['frame']) if ast.op == '-' else self.emit.emitMULOP('*',result,o['frame']) if ast.op == '*' else self.emit.emitMULOP('/',result,o['frame'])

        elif ast.op in ['%']:
            codeL, left = self.visit(ast.left, o)
            codeR, right = self.visit(ast.right, o)
            if type(left) is IntType and type(right) is IntType:
                codegen += codeL
                codegen += codeR
                result = IntType()
                codegen += self.emit.emitMOD(o['frame'])
        elif ast.op in ['<','<=','>','>=','==','!=']:
            codeL, left = self.visit(ast.left, o)
            codeR, right = self.visit(ast.right, o)
            result = BoolType()
            if type(left) is IntType and type(right) is IntType:
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitREOP(ast.op, IntType(), o['frame'])
            elif type(left) is FloatType and type(right) is FloatType:
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitREOP(ast.op, FloatType(), o['frame'])
            elif type(left) is IntType and type(right) is FloatType:
                codegen += codeL
                codegen += self.emit.emitI2F(o['frame'])
                codegen += codeR
                codegen += self.emit.emitREOP(ast.op, FloatType(), o['frame'])
            elif type(left) is FloatType and type(right) is IntType:
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitI2F(o['frame'])
                codegen += self.emit.emitREOP(ast.op, FloatType(), o['frame'])
            elif type(left) is StringType and type(right) is StringType:
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitREOP(ast.op, FloatType(), o['frame'])
            elif type(left) is BoolType and type(right) is BoolType:
                codegen += codeL
                codegen += codeR
                codegen += self.emit.emitREOP(ast.op, FloatType(), o['frame'])
        elif ast.op in ['&&','||']:
            codeL, _ = self.visit(ast.left, o)
            codegen += codeL
            result = BoolType()
            if ast.op == '&&':
                label1 = o['frame'].getNewLabel()
                label2 = o['frame'].getNewLabel()
                codegen += self.emit.emitIFFALSE(label1, o['frame'])
                codegen += self.visit(ast.right, o)[0]
                codegen += self.emit.emitIFFALSE(label1, o['frame'])
                codegen += self.emit.emitPUSHICONST(1, o['frame'])
                codegen += self.emit.emitGOTO(label2, o['frame'])
                codegen += self.emit.emitLABEL(label1, o['frame'])
                codegen += self.emit.emitPUSHICONST(0, o['frame'])
                codegen += self.emit.emitLABEL(label2, o['frame'])
            elif ast.op == '||':
                label1 = o['frame'].getNewLabel()
                label2 = o['frame'].getNewLabel()
                codegen += self.emit.emitIFTRUE(label1, o['frame'])
                codegen += self.visit(ast.right, o)[0]
                codegen += self.emit.emitIFTRUE(label1, o['frame'])
                codegen += self.emit.emitPUSHICONST(0, o['frame'])
                codegen += self.emit.emitGOTO(label2, o['frame'])
                codegen += self.emit.emitLABEL(label1, o['frame'])
                codegen += self.emit.emitPUSHICONST(1, o['frame'])
                codegen += self.emit.emitLABEL(label2, o['frame'])

        return codegen, result
    def visitUnaryOp(self, ast, o):
        codegen, body = self.visit(ast.body, o)
        
        if ast.op in ['-']:
            codegen += self.emit.emitNEGOP(body, o['frame'])
            return codegen, body
        elif ast.op in ['!']:
            codegen += self.emit.emitNOT(body, o['frame'])
            return codegen, BoolType()
            
    def visitIf(self, ast, o):

        label1 = o['frame'].getNewLabel()
        label2 = o['frame'].getNewLabel()
        codeL, left = self.visit(ast.expr, o)
        self.emit.printout(codeL)
        self.emit.printout(self.emit.emitIFFALSE(label1, o['frame']))
        self.visit(ast.thenStmt, o)
        if ast.elseStmt:
            self.emit.printout(self.emit.emitGOTO(label2, o['frame']))
            self.emit.printout(self.emit.emitLABEL(label1, o['frame']))
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(label2, o['frame']))
        else:
            self.emit.printout(self.emit.emitLABEL(label1, o['frame']))
        return o
    
    def visitForBasic(self, ast, o):
        """
            cond:Expr
            loop:Block
        """
        o['frame'].enterLoop()
        frame = o['frame']
        breakLabel = frame.getNewLabel()
        continueLabel = frame.getNewLabel()
        
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        condCode, _ = self.visit(ast.cond, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))

        o['frame'].exitLoop()

        return o
    def visitForStep(self, ast, o):
        """
            init:Stmt
            cond:Expr
            upda:Assign
            loop:Block
        """
        o['frame'].enterLoop()
        frame = o['frame']
        breakLabel = frame.getNewLabel()
        continueLabel = frame.getNewLabel()
        self.visit(ast.init, o)
        
        forLabel = frame.getNewLabel()
        code, _ = self.visit(ast.cond, o)
        self.emit.printout(code)
        self.emit.printout(self.emit.emitLABEL(forLabel, frame))
        



        o['frame'].exitLoop()
    # def visitForEach(self, ast: ForEach, c: List[List[Symbol]]):
    #     """
    #     Kiểm tra vòng lặp for ... range trong MiniGo.
    #     ast: ForEach(idx: Id, value: Id, arr: Expr, loop: Block)
    #     c: Environment (list of scopes)
    #     """


    def visitAssign(self, ast, o):
        """
            lhs: LHS
            rhs: Expr
        """
        o['isLeft'] = True
        codeL, typeLeft = self.visit(ast.lhs, o)
        o['isLeft'] = False
        codeR, typeRight = self.visit(ast.rhs, o)
        if type(ast.lhs) is Id:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.lhs.name, typeRight, Index(index)))
            self.emit.printout(codeR + codeL)
        else:
            self.emit.printout(codeL)
            self.emit.printout(codeR)
            self.emit.emitASTORE(typeLeft, o['frame'])
        return o
        
        


    
