from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple

from StaticError import Type as StaticErrorType
from AST import Type

class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, param)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function: List[FuncDecl] =  [
            FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putInt", [ParamDecl("i", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl("i", IntType())], VoidType(), Block([])),
            FuncDecl("getFloat", [], FloatType(), Block([])),
            FuncDecl("putFloat", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            FuncDecl("putFloatLn", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putBool", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            FuncDecl("putBoolLn", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl("s", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl("s", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [], VoidType(), Block([]))
        ]
        self.function_current: FuncDecl = None
    
    def check(self):
        self.visit(self.ast, None)

    def printEnv(self,env):
        for idx in range(len(env)):
            print("=", idx)
            for x in env[idx]:
                print(x)
                
    def visitProgram(self, ast: Program,c : None):
        def assignMethod(ast: MethodDecl, c: StructType) -> MethodDecl:
            # c is struct AST
            if c is None:
                raise Undeclared(Type, ast.recType.name)
            
            res = self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name)
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)
            
            # res = self.lookup(ast.fun.name, c.elements, lambda x: x[0])
            # if not res is None:
            #     raise Redeclared(Field(), ast.fun.name)
            

            c.methods.append(ast)

            return ast
        
        list_name = ["getInt", "putInt", "putIntLn", "getFloat", "putFloat", "putFloatLn", "getBool", "putBool", "putBoolLn", "getString", "putString", "putStringLn", "putLn"]
        for item in ast.decl:
            if isinstance(item, VarDecl):
                if item.varName in list_name:
                    raise Redeclared(Variable(), item.varName)
                list_name.append(item.varName)
            elif isinstance(item, ConstDecl):
                if item.conName in list_name:
                    raise Redeclared(Constant(), item.conName)
                list_name.append(item.conName)
            elif isinstance(item, FuncDecl):
                if item.name in list_name:
                    raise Redeclared(Function(), item.name)
                list_name.append(item.name)
            elif isinstance(item, Type):
                print("Type::", item.name)
                if item.name in list_name:
                    raise Redeclared(StaticErrorType(), item.name)
                list_name.append(item.name)

                
          
        # list Type AST
        self.list_type = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc, ast.decl, [])
        
        
        # list function AST
        self.list_function = self.list_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))
        

       
        
        list(map(
            lambda item: assignMethod(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)), 
             list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))

        print("list_type", self.list_type)
    
        o = [[
                Symbol("getInt", FuntionType()),
                Symbol("putInt", FuntionType()),
                Symbol("putIntLn", FuntionType()),
                Symbol("getFloat", FuntionType()),
                Symbol("putFloat", FuntionType()),
                Symbol("putFloatLn", FuntionType()),
                Symbol("getBool", FuntionType()),
                Symbol("putBool", FuntionType()),
                Symbol("putBoolLn", FuntionType()),
                Symbol("getString", FuntionType()),
                Symbol("putString", FuntionType()),
                Symbol("putStringLn", FuntionType()),
                Symbol("putLn", FuntionType()),
            ]]

        for decl in ast.decl:
            if isinstance(decl, Decl): 
                print("Decl::", decl)
                #self.printEnv(o)
                result = self.visit(decl, o)
                if isinstance(result, Symbol):
                    print("=>Symbol::", result)
                    o[0].append(result)
                    
                
    def avaluateast(self, ast: AST, c: List[List[Symbol]]) -> int:  
        if type(ast) == IntLiteral:
            return ast.value
        if type(ast) == Id:
            res = None
            for env in c:
                res = self.lookup(ast.name, env, lambda x: x.name)
                if not res is None:
                    break
            if res is None:
                raise Undeclared(Identifier(), ast.name)
            return res.value
        if type(ast) == BinaryOp:
            LHS = self.avaluateast(ast.left, c)
            RHS = self.avaluateast(ast.right, c)
            if ast.op == '+':
                return LHS + RHS
            if ast.op == '-':
                return LHS - RHS
            if ast.op == '*':
                return LHS * RHS
            if ast.op == '/':
                if RHS == 0:
                    raise TypeMismatch(ast)
                return round(LHS / RHS)
            if ast.op == '%':
                if RHS == 0:
                    raise TypeMismatch(ast)
                return LHS % RHS
        if type(ast) == UnaryOp:
            if ast.op == '-':
                return -self.avaluateast(ast.body, c)
        return 0
    
    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) -> StructType:
        res = self.lookup(ast.name, self.list_type, lambda x: x.name)
        
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)
        self.list_type = [ast] + self.list_type
        
        def visitElements(element: Tuple[str,Type], c: List[Tuple[str,Type]]) -> Tuple[str,Type]:
            res = self.lookup(element[0], c, lambda x: x[0])
            if not res is None:
                raise Redeclared(Field(), element[0])
            return element
            

        ast.elements = reduce(lambda acc,ele: [visitElements(ele,acc)] + acc , ast.elements , [])
        return ast

    def visitPrototype(self, ast: Prototype, c: List[Prototype]) -> Prototype:
        # TODO: Implement
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        
        return ast
        

    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) -> InterfaceType:
        res = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if not res is None:
            raise Redeclared(StaticErrorType(), ast.name)  
        
        self.list_type = [ast] + self.list_type

        
        ast.methods = reduce(lambda acc,ele: [self.visit(ele,acc)] + acc , ast.methods , [])
        return ast
    
    def visitFuncDecl(self, ast: FuncDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        
        self.function_current = ast
        
        env = [[]] + c
        for param in ast.params:
            p = self.visit(param, env)
            env[0].append(p)
            print("Symbol::Param::", p)
            
        # Visit body
        self.visit(ast.body, env)
        
        return Symbol(ast.name, FuntionType(), None)

    def visitParamDecl(self, ast: ParamDecl, c: list[Symbol]) -> Symbol:
        print("visitParamDecl::", ast)
        res = self.lookup(ast.parName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        
        return Symbol(ast.parName, ast.parType , None)
    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) -> None:
        self.function_current = ast.fun
        
        # res = self.lookup(ast.fun.name, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Method(), ast.fun.name)
        
        env = [[]] + [[Symbol(ast.receiver, ast.recType, None)]] + c
        for param in ast.fun.params:
            res = self.lookup(param.parName, env[0], lambda x: x.name)
            if not res is None:
                raise Redeclared(Parameter(), param.parName)
            env[0].append(self.visit(param, env))
        
        self.visit(Block( ast.fun.body.member), env)
        
    def compareInterfaceStruct(self, interface: InterfaceType, struct: StructType) -> bool:
        print("CompareInterfaceStruct::", interface, struct)
       
        
        if len(interface.methods) > len(struct.methods):
            return False
        
        for idx in range(len(interface.methods)):
            prototype = interface.methods[idx]
            method = struct.methods[idx]
            
            if prototype.name != method.fun.name:
                return False
            
            if not self.checkType(prototype.retType, method.fun.retType, []):
                return False
            
            if len(prototype.params) != len(method.fun.params):
                return False
            
            for i in range(len(prototype.params)):
                if not self.checkType(prototype.params[i], method.fun.params[i].parType, []):
                    return False
                
            return True
        
                
    def checkType(self, lhs: Type, rhs: Type, valid_types: List[Tuple[Type, Type]], c=[[]], isAssign=True) -> bool:
        
        
        if type(lhs) == Id:
            lhs = self.lookup(lhs.name, self.list_type, lambda x: x.name)
        
        if type(rhs) == Id:
            rhs = self.lookup(rhs.name, self.list_type, lambda x: x.name)
            
        print("Typelhs", lhs)
        print("Typerhs", rhs)
        
        if type(lhs) == ArrayType and type(rhs) == ArrayType:
            lhs = self.visit(lhs, c)
            rhs = self.visit(rhs, c)
            print("+Typelhs", lhs)
            print("+Typerhs", rhs)
            if isAssign:
                if not self.checkType(lhs.eleType, rhs.eleType, [(FloatType, IntType)], c, False):
                    return False
            else:
                if not self.checkType(lhs.eleType, rhs.eleType, []):
                    return False
            if len(lhs.dimens) != len(rhs.dimens):
                return False
            for i in range(len(lhs.dimens)):
                if self.avaluateast(lhs.dimens[i],c) != self.avaluateast(rhs.dimens[i],c):
                    return False
            return True
        
        if type(lhs) == StructType and type(rhs) == StructType:
            return lhs.name == rhs.name  or rhs.name == ''
        
        if type(lhs) == InterfaceType and type(rhs) == InterfaceType:
            return lhs.name == rhs.name  or rhs.name == ''
        
        if type(lhs) == InterfaceType and type(rhs) == StructType:
            if rhs.name =='': return True
            if isAssign:
                return self.compareInterfaceStruct(lhs, rhs) 
            return False
            
        if type(lhs) == type(rhs):
            return True
        
        for valid_type in valid_types:
            if isinstance(lhs, valid_type[0]) and isinstance(rhs, valid_type[1]):
                return True
        
        return False
        
    def visitVarDecl(self, ast: VarDecl, c : List[List[Symbol]],) -> Symbol:
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        
        lhs_type = ast.varType
        if isinstance(lhs_type, ArrayType):
            lhs_type = self.visit(lhs_type, c)
        
        if isinstance(lhs_type, Id):
            lhs_type = self.lookup(lhs_type.name, self.list_type, lambda x: x.name)
        
        rhs_type = self.visit(ast.varInit, c) if ast.varInit else None
        rhs_value = self.avaluateast(ast.varInit, c) if ast.varInit else 0

        if rhs_type is None:
            print("varInit", ast.varInit)
            if isinstance(ast.varInit, MethCall) or isinstance(ast.varInit, FuncCall):
                raise TypeMismatch(ast.varInit)
            return Symbol(ast.varName, lhs_type, rhs_value)
        elif lhs_type is None:
            return Symbol(ast.varName, rhs_type, rhs_value)
       
        elif self.checkType(lhs_type, rhs_type, [(FloatType, IntType)], c):
            return Symbol(ast.varName, lhs_type, rhs_value)
        
            
        raise TypeMismatch(ast)

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)
        
        lhs_type = ast.conType
        if isinstance(lhs_type, Id):
            lhs_type = self.lookup(lhs_type.name, self.list_type, lambda x: x.name)
            
        rhs_type = self.visit(ast.iniExpr, c) if ast.iniExpr else None
        
        rhs_value = self.avaluateast(ast.iniExpr, c) if ast.iniExpr else 0
        
        if rhs_type is None:
            #???
            if isinstance(ast.iniExpr, MethCall) or isinstance(ast.iniExpr, FuncCall):
                raise TypeMismatch(ast.iniExpr)
            
            
            return Symbol(ast.conName, lhs_type, rhs_value)

        elif lhs_type is None:
            return Symbol(ast.conName, rhs_type, rhs_value)
        elif self.checkType(lhs_type, rhs_type, [(FloatType, IntType)], c):

            return Symbol(ast.conName, lhs_type, rhs_value)
        
        raise TypeMismatch(ast)
        

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        # reduce(
        #     lambda acc, ele: [
        #         ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
        #     ] + acc[1:], 
        #     ast.member, 
        #     [[]] + c
        # )
        env = [[]] + c
        for ele in ast.member:
            print("ele::", ele)
            if isinstance(ele, FuncCall):
                print("visitFuncCall::checkVoid", ele)
                res = self.lookup(ele.funName, self.list_function, lambda x: x.name)
                if res is None:
                    raise Undeclared(Function(), ele.funName)
                #print("res", res)
                if not isinstance(res.retType, VoidType):
                    print("visitFuncCall::retType::NeedVoid", res.retType)
                    raise TypeMismatch(ele)
            if isinstance(ele, MethCall):
                type_receiver = self.visit(ele.receiver, env)
                res = None  
                if isinstance(type_receiver, StructType):
                    res = self.lookup(ele.metName, type_receiver.methods, lambda x: x.fun.name) # return  MethodDecl
                    print("res", res)
                    if res is None:
                        raise Undeclared(Method(), ele.metName)
                    
                    if not isinstance(res.fun.retType, VoidType):
                        print("visitMethCall::retType::NeedVoid", res.fun.retType)
                        raise TypeMismatch(ele)
                elif isinstance(type_receiver, InterfaceType):
                    res = self.lookup(ele.metName, type_receiver.methods, lambda x: x.name) # return Prototype
                    if res is None:
                        raise Undeclared(Method(), ele.metName)
                    
                    if not isinstance(res.retType, VoidType):
                        print("visitMethCall::retType::NeedVoid", res.retType)
                        raise TypeMismatch(ele)
                else:
                    raise TypeMismatch(ele)
            
            result = self.visit(ele, env)
            if isinstance(result, Symbol):
                env[0].append(result)
                print("=>Symbol::", result)

    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]) -> None:
        type_cond = self.visit(ast.cond, c)
        if not isinstance(type_cond, BoolType):
            raise TypeMismatch(ast)
         
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None: 
    
    
        # env = [[]] + c
        # for ele in ast.member:
        #     print("ele::", ele)
        #     result = self.visit(ele, env)
        #     if isinstance(result, Symbol):
        #         env[0].append(result)
    
        env = [[]] + c
        print("=>Symbol::",self.visit(ast.init, env))
        env[0].append(self.visit(ast.init, env))    
            
        type_cond = self.visit(ast.cond, env)
        if not isinstance(type_cond, BoolType):
            raise TypeMismatch(ast) 
        
        print("ast.upda", ast.upda)
        upda = self.visit(ast.upda, env)
        if isinstance(upda, Symbol):
            env[0].append(upda)
            print("=>Symbol::", upda)
        
        for ele in ast.loop.member:
            print("ele::", ele)
            result = self.visit(ele, env)
            if isinstance(result, Symbol):
                env[0].append(result)
                print("=>Symbol::", result)

        

      
    
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None: 
        
        self.visit(Block([VarDecl(ast.idx.name, IntType(), None), VarDecl(ast.value.name, None, None)] + ast.loop.member), c)
    
    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        
        res = None
       
        for env in c:
            res = self.lookup(ast.name, env, lambda x: x.name)
            if not res is None:
                break

        if res is None:
            raise Undeclared(Identifier(), ast.name)
                    
        #Symbol(v,Id(TIEN)) for struct
        #Symbol(a,IntType) 
        current_type = None
        if isinstance(res.mtype, Id):
            current_type = self.lookup(res.mtype.name, self.list_type, lambda x: x.name)
            #return AST
       
        if res and not isinstance(res.mtype, FuntionType):
            print("visitId::type::", res.mtype if not isinstance(res.mtype, Id) else current_type)
            return res.mtype if not isinstance(res.mtype, Id) else current_type
        raise Undeclared(Identifier(), ast.name)


    def checkArgsParams(self, args: List[Expr], params: List[ParamDecl],o) -> None:
        # name: str
        # params: List[ParamDecl]
        # retType: Type # VoidType if there is no return type
        # body: Block
        if len(args) != len(params):
            return False
        for i in range(len(args)):
            print("args", args[i])
            argType = self.visit(args[i], o)
            
            parType = params[i]
            if isinstance(params[i], ParamDecl):
                parType =  params[i].parType
            print("argType::", argType)
            print("parType::", parType)
            if not self.checkType( parType,argType, [], o, False):
                return False
        return True
        
        
    
    def visitFuncCall(self, ast: FuncCall, c: List[List[Symbol]]) -> Type:
        print("visitFuncCall::", ast)
        # funName:str
        # args:List[Expr] # [] if there is no arg 
        res = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        print("function::", res)
           
        if not res:
            raise Undeclared(Function(), ast.funName)
        
      
        print("CheckArgsParams::", ast.args, res.params)
        if not self.checkArgsParams(ast.args, res.params, c):
            raise TypeMismatch(ast)
        
        #print("OK")
        
        return res.retType if not isinstance(res.retType, VoidType) else None

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver = self.visit(ast.receiver, c)
        print("FieldAccess::", ast)
        print("type_receiver", type_receiver)
        res = None
        
        if not isinstance(type_receiver, StructType):
            raise TypeMismatch(ast)
        
        if isinstance(type_receiver, StructType):
            res = self.lookup(ast.field, type_receiver.elements, lambda x: x[0])
        if res is None:
            raise Undeclared(Field(), ast.field)
        
        
        if isinstance(res[1], Id):
            return self.lookup(res[1].name, self.list_type, lambda x: x.name)
        return res[1]
        
    

    def visitMethCall(self, ast: MethCall, c: List[List[Symbol]]) -> Type:
        print("visitMethCall::", ast)
        type_receiver = self.visit(ast.receiver, c)
        res = None  
        if isinstance(type_receiver, StructType):
            res = self.lookup(ast.metName, type_receiver.methods, lambda x: x.fun.name) # return  MethodDecl
            #print("res", res)
            if res is None:
                raise Undeclared(Method(), ast.metName)
            
            if not self.checkArgsParams(ast.args, res.fun.params, c):
                raise TypeMismatch(ast)
            
            print("res.fun.retType", res.fun.retType)
           
            return res.fun.retType if not isinstance(res.fun.retType, VoidType) else None
        
        elif isinstance(type_receiver, InterfaceType):
            res = self.lookup(ast.metName, type_receiver.methods, lambda x: x.name) # return Prototype
            if res is None:
                raise Undeclared(Method(), ast.metName)
            
            if not self.checkArgsParams(ast.args, res.params, c):
                raise TypeMismatch(ast)
            return res.retType if not isinstance(res.retType, Id) else self.lookup(res.retType.name, self.list_type, lambda x: x.name)
        
        
        raise TypeMismatch(ast)
        
        
        
        


    def visitIntType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitFloatType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitBoolType(self, ast, c: List[List[Symbol]])-> Type: return ast
    def visitStringType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitVoidType(self, ast, c: List[List[Symbol]]) -> Type: return ast
    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        #list(map(lambda item: # TODO: Implement, ast.dimens))]
    #    dimens:List[Expr]
    #   eleType:Type
        print("visitArrayType::", ast)
        dimens  = []
        for dimen in ast.dimens:
            if not isinstance(self.visit(dimen, c), IntType):
                raise TypeMismatch(ast)
            dimens.append(IntLiteral(int(self.avaluateast(dimen, c))))
        return ArrayType(dimens, ast.eleType)
    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> None:
        
        RHS_type = self.visit(ast.rhs, c)
        
        if isinstance(ast.lhs, Id):
            res = self.lookup(ast.lhs.name, c[0], lambda x: x.name)
            if res is None:
                return Symbol(ast.lhs.name, RHS_type, None)         
        
        
        LHS_type = self.visit(ast.lhs, c)
        
        
        if not self.checkType(LHS_type, RHS_type, [(FloatType, IntType)]):
            raise TypeMismatch(ast)
        
    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None: 
        # expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt # None if there is no else
        
        expr_type = self.visit(ast.expr, c)
        if not isinstance(expr_type, BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.thenStmt.member), c)
        if ast.elseStmt:
            if isinstance(ast.elseStmt, If):
                self.visit(ast.elseStmt, c)
            else: self.visit(Block(ast.elseStmt.member), c)
        
        # if # TODO: Implement:
        #     raise TypeMismatch(ast)
        # self.visit(Block(ast.thenStmt.member), c)
        # if ast.elseStmt:
        #     # TODO: Implement
        

    def visitContinue(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitBreak(self, ast, c: List[List[Symbol]]) -> None: return None
    def visitReturn(self, ast:Return, c: List[List[Symbol]]) -> None: 
        print("visitReturn::", ast)
        return_type = None
        function_return_type = self.function_current.retType

        if isinstance(function_return_type, VoidType):
            if ast.expr:
                self.visit(ast.expr, c)
                if isinstance(ast.expr, FuncCall) or isinstance(ast.expr, MethCall):
                    raise TypeMismatch(ast.expr)
                raise TypeMismatch(ast)
            return None
        else: 
            if not ast.expr:
                raise TypeMismatch(ast)    
            return_type = self.visit(ast.expr, c)
                
            if self.checkType(function_return_type, return_type, [], [[]], False):
                return None
            
            raise TypeMismatch(ast)
        
        
        
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        LHS_type = self.visit(ast.left, c)
        RHS_type = self.visit(ast.right, c)
        
        if ast.op in ['+']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if type(LHS_type) == StringType:
                    return StringType()
                elif type(LHS_type) == FloatType:
                    return FloatType()
                elif type(RHS_type) == FloatType:
                    return FloatType()
                elif type(LHS_type) == IntType:
                    return IntType()
        if ast.op in ['-', '*', '/']:
            if self.checkType(LHS_type, RHS_type, [(IntType, FloatType), (FloatType, IntType)]):
                if type(LHS_type) == FloatType:
                    return FloatType()
                elif type(RHS_type) == FloatType:
                    return FloatType()
                elif type(LHS_type) == IntType:
                    return IntType()
        if ast.op in ['%']:
            if self.checkType(LHS_type, RHS_type, []):
                if type(LHS_type) == IntType:
                    return IntType()
        
        if ast.op in ['==', '!=', '>', '<', '>=', '<=']:
            if self.checkType(LHS_type, RHS_type,[ ]):
                if type(LHS_type) == IntType or type(LHS_type) == FloatType or type(LHS_type) == StringType:
                    return BoolType()
        
        if ast.op in ['&&', '||']:
            if self.checkType(LHS_type, RHS_type, []):
                if type(LHS_type) == BoolType:
                    return BoolType()
        
        
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        #op:str, body:Expr
        unary_type = self.visit(ast.body, c)
        if ast.op == '-':
            if type(unary_type) == IntType:
                return IntType()
            elif type(unary_type) == FloatType:
                return FloatType()
        if ast.op == '!':
            if type(unary_type) == BoolType:
                return BoolType()
        raise TypeMismatch(ast)
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        # arr:Expr
        # idx:List[Expr]
        print("VisitArrayCell::", ast)
        array_type = self.visit(ast.arr, c)  #dimens:List[Expr] eleType:Type: ArrayType(IntType,[IntLiteral(2),IntLiteral(3)])
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)
       
        if len(array_type.dimens) < len(ast.idx):
            raise TypeMismatch(ast)
        
        for i in range(len(ast.idx)):
            if not self.checkType(IntType(), self.visit(ast.idx[i], c), []):
                raise TypeMismatch(ast)
                
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
        
        
       
        # if not all(map(lambda item: self.checkType(self.visit(item, c), # TODO: Implement), ast.idx)):
        #     raise TypeMismatch(ast)
        # if len(array_type.dimens) == len(ast.idx):
        #     return # TODO: Implement
        # elif len(array_type.dimens) > len(ast.idx):
        #     return # TODO: Implement
        # raise TypeMismatch(ast)
        pass

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) -> Type: return IntType()
    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) -> Type: return FloatType()
    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) -> Type: return BoolType()
    def visitStringLiteral(self, ast, c: List[List[Symbol]]) -> Type: return StringType()
    
    def checkArray(self, dimens: List[Expr], value: NestedList, eleType: Type, c: List[List[Symbol]]):
        print("checkArray::")

        if len(dimens) == 0:
            return self.checkType(eleType, self.visit(value, c), [(FloatType, IntType)])
        
        print("dimens::", dimens)
        print("value::", value)
        
        
        
        if dimens[0] != len(value):
            return False
        for val in value:
            if not self.checkArray(dimens[1:], val, eleType, c):
                return False
        return True
            
        
        
    
    def visitArrayLiteral(self, ast:ArrayLiteral , c: List[List[Symbol]]) -> Type:  
        # dimens:List[Expr]
        # eleType: Type
        # value: NestedList
        print("ArrayLiteral::", ast)

        # dimen_type = []
        
        # for dimen in ast.dimens:
        #     if not isinstance(self.visit(dimen, c), IntType):
        #         raise TypeMismatch(ast)
        #     dimen_type.append(dimen)
        
        # print("dimen_type", dimen_type)
        
        # eleType = ast.eleType
        # for value in ast.value:
        #     if not self.checkType(eleType, self.visit(value, c), [(FloatType, IntType)]):
        #         raise TypeMismatch(ast)
        
        
        
        # return ArrayType(dimen_type, eleType)
        
        dimen_type = []
        # Check type of dimension
        for dimen in ast.dimens:
            if not isinstance(self.visit(dimen, c), IntType):
                raise TypeMismatch(ast)
            dimen_type.append(self.avaluateast(dimen,c))

        if not self.checkArray(dimen_type,  ast.value, ast.eleType, c):
            raise TypeMismatch(ast)
        
        return ArrayType(ast.dimens, ast.eleType)
        
        
    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]) -> Type: 
        # StructLiteral
        # name:str
        # elements: List[Tuple[str,Expr]] # [] if there is no elements
        
        # StructType
        # name: str
        # elements:List[Tuple[str,Type]]
        # methods:List[MethodDecl]
        
        print("visitStructLiteral::", ast)
        res = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if res is None:
            raise Undeclared(Type(), ast.name)

        print("StructType::", res)
        
        for ele in ast.elements:
            eleType = self.lookup(ele[0], res.elements, lambda x: x[0])[1]
            if eleType is None:
                raise Undeclared(Field(), ele[0])
            exprType = self.visit(ele[1], c)
           
            
            if not self.checkType(eleType, exprType, [(FloatType, IntType)]):
                raise TypeMismatch(ast)
        return res
            
        
        
        
    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type: return StructType("",[], [])