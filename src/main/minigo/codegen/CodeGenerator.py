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

    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<clinit>", VoidType())  # Sửa lỗi đánh máy từ <cinit> thành <clinit>
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        
        # Tạo danh sách các VarDecl có varInit và là static
        static_var_decls = list(filter(lambda x: isinstance(x, VarDecl) and x.varInit is not None or isinstance(x, ConstDecl) and x.iniExpr is not None, ast.decl))
        
        # Tạo Block chứa các VarDecl và xử lý
        for decl in static_var_decls:
            if isinstance(decl, VarDecl):
                env['isLeft'] = False
                env['stmt'] = False
                code, exprType = self.visit(decl.varInit, env)
                env['isLeft'] = False
                env['stmt'] = True
                self.emit.printout(code)
                if type(decl.varType) is FloatType and type(exprType) is IntType:
                    self.emit.printout(self.emit.emitI2F(frame))
                _type = decl.varType
                
                if decl.varType is None:
                    _type = exprType
                if type(_type) is Id:
                    _type = ClassType(_type.name)
                self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{decl.varName}", _type, frame))
                
            elif isinstance(decl, ConstDecl):
                env['isLeft'] = False
                env['stmt'] = False
                code, conType = self.visit(decl.iniExpr, env)
                env['isLeft'] = False
                env['stmt'] = True
                self.emit.printout(code)
                self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{decl.conName}", conType, frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def _emitObjectInit(self, emit, className):
        frame = Frame("<init>", VoidType())  
        emit.printout(emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        emit.printout(emit.emitVAR(frame.getNewIndex(), "this", ClassType(className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        emit.printout(emit.emitLABEL(frame.getStartLabel(), frame))
        emit.printout(emit.emitREADVAR("this", ClassType(className), 0, frame))  
        emit.printout(emit.emitINVOKESPECIAL(frame))  
    
        
        emit.printout(emit.emitLABEL(frame.getEndLabel(), frame))
        emit.printout(emit.emitRETURN(VoidType(), frame))  
        emit.printout(emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def acceptMethodDecl(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.recType.name, o['env'][-1]),None)
        sym.methods.append(ast)
        return o
    def visitProgram(self, ast, c):
        env ={}
        env['env'] = [c]
        env['isLeft'] = False
        env['stmt'] = True
    
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for x in ast.decl:
            if type(x) is StructType:
                env['env'][0].append(x)
        for x in ast.decl:
            if type(x) is MethodDecl:
                self.acceptMethodDecl(x, env)
        env['method'] = False
        env = reduce(lambda a,x: self.visit(x,a) if type(x) is not MethodDecl else a, ast.decl, env)
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        self.emit.printout(self.emit.emitEPILOG())
        return env
    

    def declareVar(self, name, _type, o):
        """
        Khai báo biến trong môi trường hiện tại.
        name: Tên biến
        _type: Kiểu biến
        o: Môi trường (list of scopes)
        """
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(name, _type, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, name, _type, frame.getStartLabel(), frame.getEndLabel(), frame))
        return o, index

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
        if env['method']:
            self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,False, frame))
        else:
            self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        if env['method']:
            frame.getNewIndex()
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
    def visitParamDecl(self, ast, o):
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return o
    
    def visitVarDecl(self, ast, o):

        if 'frame' not in o: # global var
            temp_frame = Frame("temp", VoidType())
            env = o.copy()
            env['frame'] = temp_frame
            _type = ast.varType
            _, varType = self.visit(ast.varInit, env)
            if ast.varType is None:
                _type = varType
            if type(_type) is Id:
                _type = ClassType(_type.name)
            o['env'][0].append(Symbol(ast.varName, _type, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, _type, True, True, None))
        else:
            frame = o['frame']
            varType = ast.varType
            if ast.varInit:
                o['stmt'] = False
                codegen, _type = self.visit(ast.varInit, o)
                o['stmt'] = True
                self.emit.printout(codegen)
                if varType is None:
                    varType = _type
            else:
                if type(ast.varType) is FloatType:
                    self.emit.printout(self.emit.emitPUSHFCONST(0.0, frame))
                elif type(ast.varType) is IntType:
                    self.emit.printout(self.emit.emitPUSHICONST(0, frame))
                elif type(ast.varType) is BoolType:
                    self.emit.printout(self.emit.emitPUSHICONST(0, frame))

            if type(varType) is Id and ast.varInit:
                varType = ClassType(varType.name)
                self.emit.printout(self.emit.emitNEW(varType, frame))
                # self.emit.printout(self.emit.emitDUP(frame))
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame, f"{varType.name}/<init>", MType([], VoidType())))
            elif type(varType) is Id and not ast.varInit:
                varType = ClassType(varType.name)
                self.emit.printout(self.emit.emitNEW(varType, frame))
                self.emit.printout(self.emit.emitDUP(frame))
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame, f"{varType.name}/<init>", MType([], VoidType())))
            o, index = self.declareVar(ast.varName, varType, o)
            
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index,  frame))
        return o
    
    def visitConstDecl(self, ast, o):

        if 'frame' not in o:
            temp_frame = Frame("temp", VoidType())
            env = o.copy()
            env['frame'] = temp_frame
            _, conType = self.visit(ast.iniExpr, env)
            o['env'][0].append(Symbol(ast.conName, conType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, conType, True, True, None))
        else:
            frame = o['frame']

            o['stmt'] = False
            codegen, varType = self.visit(ast.iniExpr, o)
            o['stmt'] = True
            if type(varType) is Id:
                varType = ClassType(varType.name)
                self.emit.printout(self.emit.emitNEW(varType, frame))
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame, f"{varType.name}/<init>", MType([], VoidType())))

            self.emit.printout(codegen)
            o, index = self.declareVar(ast.conName, varType, o)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, varType, index,  frame))
        return o


    def visitFuncCall(self, ast, o):
        if o['stmt']:
            sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
            env = o.copy()
            env['isLeft'] = False
            env['stmt'] = False
            [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
            env['stmt'] = True
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o
        else:
            codegen = ''
            sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
            env = o.copy()
            env['isLeft'] = False
            env['stmt'] = False
            [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
            if sym.value.isStatic:
                codegen += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])
            else:
                codegen += self.emit.emitINVOKEVIRTUAL(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])
            return codegen, sym.mtype.rettype
    
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
                return self.emit.emitPUTSTATIC(f"{self.className}/{ast.name}", sym.mtype, o['frame']), sym.mtype
            else:
                return self.emit.emitGETSTATIC(f"{self.className}/{ast.name}", sym.mtype, o['frame']), sym.mtype
        
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
        return codegen, ArrayType(ast.dimens, ast.eleType)
  
    def visitArrayCell(self, ast, o):
        if o['isLeft']:

            o['isLeft'] = False
            codegen, arrType = self.visit(ast.arr, o)
            o['isLeft'] = True
            # Xác định kiểu trả về
            remaining_dims = len(arrType.dimens) - len(ast.idx)
            if remaining_dims == 0:
                for i in range(len(arrType.dimens)-1):
                    codegen += self.visit(ast.idx[i], o)[0]
                    codegen += self.emit.emitALOAD(ArrayType(arrType.dimens, arrType.eleType), o['frame'])
                codegen += self.visit(ast.idx[-1], o)[0]
                # Truy cập đến phần tử cuối cùng
                return codegen, arrType
            # else:
            #     for i in range(len(arrType.dimens) - remaining_dims):
            #         codegen += self.visit(ast.idx[i], o)[0]
            #         codegen += self.emit.emitALOAD(ArrayType(arrType.dimens, arrType.eleType), o['frame'])

            #     # Trả về mảng với số chiều còn lại
            #     new_dimens = arrType.dimens[len(ast.idx):]
            #     return codegen, ArrayType(new_dimens, arrType.eleType)


        else:
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
            # else:
            #     for i in range(len(arrType.dimens) - remaining_dims):
            #         codegen += self.visit(ast.idx[i], o)[0]
            #         codegen += self.emit.emitALOAD(ArrayType(arrType.dimens, arrType.eleType), o['frame'])

            #     # Trả về mảng với số chiều còn lại
            #     new_dimens = arrType.dimens[len(ast.idx):]
            #     return codegen, ArrayType(new_dimens, arrType.eleType)
        
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

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        o['stmt'] = False
        condCode, _ = self.visit(ast.cond, o)
        o['stmt'] = True
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

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

        self.visit(ast.init, o)
        
        forLabel = frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(forLabel, frame))
        o['stmt'] = False
        code, _ = self.visit(ast.cond, o)
        o['stmt'] = True
        self.emit.printout(code)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.visit(ast.upda, o)
        self.emit.printout(self.emit.emitGOTO(forLabel, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        o['frame'].exitLoop()
        return o
    
    # def visitForEach(self, ast: ForEach, c: List[List[Symbol]]):
    #     """
    #     Kiểm tra vòng lặp for ... range trong MiniGo.
    #     ast: ForEach(idx: Id, value: Id, arr: Expr, loop: Block)
    #     c: Environment (list of scopes)
    #     """


    
    def visitReturn(self, ast, o):
        o['stmt'] = False
        code, typ = self.visit(ast.expr, o)
        o['stmt'] = True
        self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(typ, o['frame']))
        return o
    
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o
    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o
    
    def visitStructType(self, ast, o):
        env = o.copy()
        emit = Emitter(self.path + "/" + ast.name + ".j")
        tempEmit = self.emit
        self.emit = emit
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))
        
        for x in ast.elements:
            if type(x[1]) is Id:
                eleType = ClassType(x[1].name)
            else:
                eleType = x[1]
            self.emit.printout(self.emit.emitATTRIBUTE(x[0],eleType,False,False, None))
        temp = self.className
        self.className = ast.name
        self.emitObjectInit()
        env['method'] = True
        for x in ast.methods:
            self.visit(x,env)
        env['method'] = False
        emit.emitEPILOG()
        self.className = temp
        self.emit = tempEmit

        return o
    
    def visitFieldAccess(self, ast, o):
        if o['isLeft']:
            if type(ast.receiver) is Id:
                sym = next(filter(lambda x: x.name == ast.receiver.name, [j for i in o['env'] for j in i]),None)
                struct_sym = next(filter(lambda x: x.name == sym.mtype.name, o['env'][-1]),None)
                ele = next(filter(lambda x: x[0] == ast.field, struct_sym.elements),None)
                if ele is None:
                    _type = None
                else:
                    _type = ele[1]
                    if type(_type) is Id:
                        _type = ClassType(_type.name)
                return self.emit.emitPUTFIELD(f"{struct_sym.name}/{ast.field}",_type,o['frame'])
            else:
                o['isLeft'] = False
                code, recType = self.visit(ast.receiver, o)
                o['isLeft'] = True

                ele = next(filter(lambda x: x[0] == ast.field, recType.elements),None)
                if ele is None:
                    _type = None
                else:
                    _type = ele[1]
                    if type(_type) is Id:
                        _type = ClassType(_type.name)
                return self.emit.emitPUTFIELD(f"{recType.name}/{ast.field}",_type,o['frame'])
        else:
            codegen = ''
            _type = None
            if type(ast.receiver) is Id:
                sym = next(filter(lambda x: x.name == ast.receiver.name, [j for i in o['env'] for j in i]),None)
                struct_sym = next(filter(lambda x: x.name == sym.mtype.name, o['env'][-1]),None)
                ele = next(filter(lambda x: x[0] == ast.field, struct_sym.elements),None)
                if ele is None:
                    _type = None
                else:
                    _type = ele[1]
                    if type(_type) is Id:
                        _type = ClassType(_type.name)
                codegen += self.visit(ast.receiver, o)[0]
                codegen += self.emit.emitGETFIELD(f"{struct_sym.name}/{ast.field}",_type,o['frame'])
            else:
                code, recType = self.visit(ast.receiver, o)
                codegen += code
                ele = next(filter(lambda x: x[0] == ast.field, recType.elements),None)
                if ele is None:
                    _type = None
                else:
                    _type = ele[1]
                    if type(_type) is Id:
                        _type = ClassType(_type.name)
                
                codegen += self.emit.emitGETFIELD(f"{recType.name}/{ast.field}",_type,o['frame'])
            if type(_type) is ClassType:
                _type = next(filter(lambda x: x.name == _type.name, o['env'][-1]),None)
            return codegen, _type

    def visitAssign(self, ast, o):
        """
            lhs: LHS
            rhs: Expr
        """
       
        o['stmt'] = False
        codeR, typeRight = self.visit(ast.rhs, o)
        o['stmt'] = True
        if type(ast.lhs) is Id:
            sym = next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]),None)
            if sym is None:
                o, index = self.declareVar(ast.lhs.name, typeRight, o)
            o['isLeft'] = True
            codeL, typeLeft = self.visit(ast.lhs, o)
            o['isLeft'] = False
            self.emit.printout(codeR + codeL)
        elif type(ast.lhs) is FieldAccess:
            self.emit.printout(self.visit(ast.lhs.receiver, o)[0])
            o['isLeft'] = True
            codeL = self.visit(ast.lhs, o)
            o['isLeft'] = False
            self.emit.printout(codeR + codeL)
        elif type(ast.lhs) is ArrayCell:
            o['isLeft'] = True
            codegen, arrType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            self.emit.printout(codegen)
            codeR,eleType = self.visit(ast.rhs, o)
            self.emit.printout(codeR)
            self.emit.printout(self.emit.emitASTORE(eleType, o['frame']))
        else:
            o['isLeft'] = True
            codeL, typeLeft = self.visit(ast.lhs, o)
            o['isLeft'] = False
            self.emit.printout(codeL)
            self.emit.printout(codeR)
            self.emit.emitASTORE(typeLeft, o['frame'])
        return o
    
    def visitStructLiteral(self, ast, o):
        codegen = ''
        codegen += self.emit.emitNEW(ClassType(ast.name), o['frame'])
        codegen += self.emit.emitDUP(o['frame'])
        codegen += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>", MType([], VoidType()))
        for ele in ast.elements:
            codegen += self.emit.emitDUP(o['frame'])
            o['stmt'] = False
            codeR, typeRight = self.visit(ele[1], o)
            o['stmt'] = True
            codegen += codeR
            codegen += self.emit.emitPUTFIELD(f"{ast.name}/{ele[0]}", typeRight, o['frame'])
        return codegen, ClassType(ast.name)
    
    def visitMethodDecl(self, ast, o):

        env = o.copy()
        env['frame'] = Frame("Method", ast.recType)
        env['frame'].enterScope(True)
        env['env'] = [[]] + env['env']
        _type = ast.recType
        if type(_type) is Id:
            _type = ClassType(_type.name)
        index = env['frame'].getNewIndex()
        env['env'][0].append(Symbol(ast.receiver, _type, Index(index)))
       
        self.visit(ast.fun, env)
        env['frame'].exitScope()
        return o

    def visitMethCall(self, ast, o):
        if o['stmt']:
            
            return o
        else:
            codegen = ''
            _type = None
            if type(ast.receiver) is Id:
                sym_var = next(filter(lambda x: x.name == ast.receiver.name, [j for i in o['env'] for j in i]),None)
                sym_struct = next(filter(lambda x: x.name == sym_var.mtype.name, o['env'][-1]),None)
                method = next(filter(lambda x: x.fun.name == ast.metName, sym_struct.methods),None)
                env = o.copy()
                env['isLeft'] = False
                env['stmt'] = False
                args = []
                for x in ast.args:
                    code, arg_type = self.visit(x, env)
                    args.append(arg_type)
                    codegen += code

                env['stmt'] = True
                _type = method.fun.retType
                codegen += self.visit(ast.receiver, o)[0]
                codegen += self.emit.emitINVOKEVIRTUAL(f"{sym_struct.name}/{ast.metName}",MType(args,_type), o['frame'])
            else:
                codegen += self.visit(ast.receiver, o)[0]
                env = o.copy()
                env['isLeft'] = False
                env['stmt'] = False
                [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
                env['stmt'] = True
                codegen += self.emit.emitINVOKEVIRTUAL(f"{ast.obj.name}/{ast.method.name}",None, o['frame'])
            return codegen, _type