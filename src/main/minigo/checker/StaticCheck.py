"""
 * @author 2211605
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Dict, Any, Union, Optional, Tuple

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

# def traverse_env(env, name):
#     print(name, end=": ")
#     out = "["
#     for i in env:
#         out += "["
#         for j in i:
#             out += str(j) + ", "
#         if len(i) > 0:
#             out = out[:-2]
#         out += "],"
#     out = out[:-1] + "]"
#     print(out)
    

class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.buildin_functions = [
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
            Symbol("putFloat", MType([FloatType()], VoidType())),
            Symbol("putFloatLn", MType([FloatType()], VoidType())),
            Symbol("getBool", MType([], BoolType())),
            Symbol("putBool", MType([BoolType()], VoidType())),
            Symbol("putBoolLn", MType([BoolType()], VoidType())),
            Symbol("getString", MType([], StringType())),
            Symbol("putString", MType([StringType()], VoidType())),
            Symbol("putStringLn", MType([StringType()], VoidType())),
            Symbol("putLn", MType([], VoidType()))
        ]
        self.functions = self.buildin_functions.copy()
        self.types = []
        self.env = [[]]
        self.current_function = None
        self.is_statement_context = False  # Cờ để phân biệt statement/expression
        self.first_phase = True
        self.allow_cast = [(IntType, FloatType), (FloatType, IntType), (InterfaceType, StructType)]

    def check(self):
        return self.visit(self.ast,self.env)
    def _lookup_symbol(self, name: str, env: List[List[Symbol]]):
        """Tra cứu symbol trong môi trường scope."""
        for scope in env:
            symbol = self.lookup(name, scope, lambda x: x.name)
            if symbol:
                return symbol
        return None

    def methodDeclPhase1(self, ast, c):
        # print("methodDeclPhase1", c)
        sym = self.lookup(ast.recType.name, self.types, lambda x: x.name)
        if sym is None or not (isinstance(sym, StructType) or isinstance(sym, InterfaceType)):
            raise Undeclared(Type(), str(ast.recType))
        
        if isinstance(sym, StructType):
            # check redeclare method trong struct
            methods = []
            for i in sym.methods:
                param_types = [param.parType for param in i.fun.params]
                func_type = MType(param_types, i.fun.retType)
                methods.append(Symbol(i.fun.name, func_type))
            for i in sym.elements:
                if i[0] == ast.fun.name:
                    raise Redeclared(Method(), ast.fun.name)
            # Kiểm tra Redeclared cho tên method trong scope của struct
            if self.lookup(ast.fun.name, methods, lambda x: x.name):
                raise Redeclared(Method(), ast.fun.name)
            sym.methods.insert(0, ast)
        elif isinstance(sym, InterfaceType):
            # check redeclare prototype trong interface
            methods = []
            for i in sym.methods:
                param_types = [param.parType for param in i.params]
                func_type = MType(param_types, i.retType)
                methods.append(Symbol(i.name, func_type))
                
            # Kiểm tra Redeclared cho tên method trong scope của struct
            if self.lookup(ast.fun.name, methods, lambda x: x.name):
                raise Redeclared(Method(), ast.fun.name)
            prototype = Prototype(ast.fun.name, ast.fun.params, ast.fun.returnType)
            sym.methods.insert(0, prototype)
        

    def visitProgram(self,ast, c):
        # print("visitProgram", c)
        for decl in ast.decl:
            if isinstance(decl,FuncDecl):
                if self.lookup(decl.name, self.functions, lambda x: x.name):
                    raise Redeclared(Function(), decl.name)
                param_types = [param.parType for param in decl.params]
                func_type = MType(param_types, decl.retType)
                self.functions.insert(0, Symbol(decl.name, func_type))
            elif isinstance(decl, AST.Type):
                self.types.insert(0, self.visit(decl, c))
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                self.methodDeclPhase1(decl, c)
        # print("Types", self.types)
        self.first_phase = False
        for decl in ast.decl:        
            if isinstance(decl, MethodDecl):
                self.visit(decl, c)
            else:
                c[0].insert(0, self.visit(decl, c))
            
        return c
    def is_compatible_type(self, target: Type, source: Type, allowed_casts, env=[[]], allow_cast=True) -> bool:
        """
        Kiểm tra tính tương thích giữa hai kiểu.
        - target: Kiểu mục tiêu (LHS)
        - source: Kiểu nguồn (RHS)
        - allowed_casts: Các cặp kiểu cho phép ép (e.g., [(FloatType, IntType)])
        - env: Môi trường scope, dùng để tính kích thước mảng
        - allow_cast: Cho phép ép kiểu trong assignment
        """
        # Resolve Id sang kiểu thực tế
        
        target = self._resolve_id(target)
        source = self._resolve_id(source)
      
        # Kiểm tra cùng kiểu
        if type(target) is type(source):
            if isinstance(target, ArrayType):
                
                return self._compare_array_types(target, source, allowed_casts, env, allow_cast)
            if isinstance(target, StructType):
                return target.name == source.name or source.name == ''
            if isinstance(target, InterfaceType):
                return target.name == source.name or source.name == ''
            return True
        retVal = True if (isinstance(target, StructType) or isinstance(target, InterfaceType)) and isinstance(source, StructType) and source.name == '' else False
        # Kiểm tra ép kiểu hợp lệ nếu allow_cast=True
        return allow_cast and any(isinstance(target, cast[0]) and isinstance(source, cast[1]) 
                                 for cast in allowed_casts) or retVal

    def _resolve_id(self, type_obj: Type) -> Type:
        """Resolve Id thành kiểu thực tế từ self.list_type."""
        if isinstance(type_obj, Id):
            resolved = self.lookup(type_obj.name, self.types, lambda x: x.name)
            return resolved if resolved else type_obj
        return type_obj
    
   
    def evaluate_ast(self, ast: Expr, env: List[List[Symbol]]) -> int:
        """Tính giá trị số nguyên của một biểu thức AST trong kiểm tra ngữ nghĩa."""
        
        if isinstance(ast, IntLiteral):
            return int(ast.value)
        
        elif isinstance(ast, Id):
            symbol = self._lookup_symbol(ast.name, env)
            if symbol is None:
                raise Undeclared(Identifier(), ast.name)
            symbol_value = int(self.evaluate_ast(symbol.value, env))
            
            if not isinstance(symbol_value, int):  # Giá trị phải là số nguyên
                raise TypeMismatch(ast)
            return symbol_value
        
        elif isinstance(ast, BinaryOp):
            left_val = int(self.evaluate_ast(ast.left, env))
            right_val = int(self.evaluate_ast(ast.right, env))
            op = ast.op
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                if right_val == 0:
                    raise TypeMismatch(ast)  # Chia cho 0
                return left_val // right_val
            elif op == '%':
                if right_val == 0:
                    raise TypeMismatch(ast)  # Modulo cho 0
                return left_val % right_val
            else:
                raise TypeMismatch(ast)  # Toán tử không hỗ trợ
        elif isinstance(ast, UnaryOp):
            operand_val = int(self.evaluate_ast(ast.body, env))
            op = ast.op
            if op == '-':
                return -operand_val
            elif op == '!':
                return 1 - operand_val
            else:
                raise TypeMismatch(ast)
        else:
            raise TypeMismatch(ast)  # Biểu thức không hỗ trợ

    def _compare_array_types(self, target: ArrayType, source: ArrayType, allowed_casts: List[Tuple[Type, Type]], env, allow_cast) -> bool:
        """So sánh hai ArrayType về số chiều, kiểu và giá trị."""
        
        # Kiểm tra số chiều
        if len(target.dimens) != len(source.dimens):
            return False
        # Kiểm tra kiểu của mỗi chiều (phải là IntType)
        for t_dim in target.dimens:
            if not isinstance(self.visit(t_dim, env), IntType):
                return False
        for s_dim in source.dimens:
            if not isinstance(self.visit(s_dim, env), IntType):
                return False
     
        # Kiểm tra giá trị của mỗi chiều
        for t_dim, s_dim in zip(target.dimens, source.dimens):
            if self.evaluate_ast(t_dim, env) != self.evaluate_ast(s_dim, env):
                return False

        # So sánh kiểu phần tử
        return self.is_compatible_type(target.eleType, source.eleType, [(FloatType, IntType)], env, allow_cast)

    def does_struct_implement_interface(self, interface: InterfaceType, struct: StructType) -> bool:
        """
        Kiểm tra xem struct có triển khai đầy đủ interface không.
        - interface: InterfaceType với danh sách prototype
        - struct: StructType với danh sách method
        """
        if len(interface.methods) > len(struct.methods):
            return False

        for proto in interface.methods:
            method = self.lookup(proto.name, struct.methods, lambda x: x.fun.name)
            if not method or not self._is_method_compatible(proto, method.fun):
                return False
        return True

    def _is_method_compatible(self, proto: Prototype, method: FuncDecl) -> bool:
        """Kiểm tra prototype và method có signature khớp nhau không."""
        if not self.is_compatible_type(proto.retType, method.retType, [], allow_cast=False):
            return False
        if len(proto.params) != len(method.params):
            return False
        return all(self.is_compatible_type(proto_param, method_param.parType, [], allow_cast=False)
                   for proto_param, method_param in zip(proto.params, method.params))
    def _validate_assignment(self, lhs_type: Type, rhs_type: Type, ast: Assign, env: List[List[Symbol]]) -> None:
        """Kiểm tra tính hợp lệ của gán dựa trên kiểu."""

        if isinstance(lhs_type, ArrayType):
            if not isinstance(rhs_type, ArrayType):
                raise TypeMismatch(ast)

            if not self.is_compatible_type(lhs_type, rhs_type, self.allow_cast, env):
                raise TypeMismatch(ast)
        elif isinstance(lhs_type, InterfaceType):
            if isinstance(rhs_type, StructType):
                if rhs_type.name == '': return True
                if not self.does_struct_implement_interface(lhs_type, rhs_type):
                    raise TypeMismatch(ast)
            elif not self.is_compatible_type(lhs_type, rhs_type, []):
                raise TypeMismatch(ast)
        elif isinstance(lhs_type, StructType):
            if not self.is_compatible_type(lhs_type, rhs_type, []):
                raise TypeMismatch(ast)
        elif not self.is_compatible_type(lhs_type, rhs_type, [(FloatType, IntType)]):
            raise TypeMismatch(ast)
        
    def visitVarDecl(self, ast, c):
        """
            varName : str
            varType : Type # None if there is no type
            varInit : Expr # None if there is no initialization
        """
        # traverse_env(c, "visitVarDecl")

        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        res2 = self.lookup(ast.varName, self.buildin_functions, lambda x: x.name)
        if not res is None or not res2 is None:
            raise Redeclared(Variable(), ast.varName)
        LHS_type = ast.varType
        if isinstance(LHS_type, Id):
            LHS_type = self.lookup(LHS_type.name, self.types, lambda x: x.name)
            if LHS_type is None:
                raise Undeclared(Type(), ast.varType.name)
        if isinstance(LHS_type, ArrayType):
            self.visit(LHS_type, c)
        if isinstance(LHS_type, StructType):
            if self.lookup(LHS_type.name, self.types, lambda x: x.name) is None:
                raise Undeclared(Type(), ast.varType.name)
        if isinstance(LHS_type, InterfaceType):
            if self.lookup(LHS_type.name, self.types, lambda x: x.name) is None:
                raise Undeclared(Type(), ast.varType.name)
 
        if ast.varInit is not None:
            self.is_statement_context = False
            RHS_type = self.visit(ast.varInit, c)
            self.is_statement_context = True
            
            if ast.varType is None:
                LHS_type = RHS_type
            else:
                LHS_type = ast.varType
            
            if isinstance(LHS_type, Id):                
                LHS_type = self.lookup(LHS_type.name, self.types, lambda x: x.name)               
                if LHS_type is None:
                    raise TypeMismatch(ast)

            if isinstance(RHS_type, Id):               
                RHS_type = self.lookup(RHS_type.name, self.types, lambda x: x.name)
                if RHS_type is None:
                    raise TypeMismatch(ast)
            
            self._validate_assignment(LHS_type, RHS_type, ast, c)
        
        return Symbol(ast.varName, LHS_type, ast.varInit if ast.varInit else None)
        
    def visitConstDecl(self, ast, c):
        # traverse_env(c, "visitConstDecl")
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        res2 = self.lookup(ast.conName, self.buildin_functions, lambda x: x.name)
        if not res is None or not res2 is None:
            raise Redeclared(Constant(), ast.conName) 
        self.is_statement_context = False
        initType = self.visit(ast.iniExpr, c)
        self.is_statement_context = True
        if ast.conType is None:
            ast.conType = initType
        if not type(ast.conType) is type(initType):
            raise TypeMismatch(ast)
        return Symbol(ast.conName, ast.conType, ast.iniExpr)
    
    def visitFuncDecl(self,ast, c):
        # traverse_env(c, "visitFuncDecl")
        param_types = [param.parType for param in ast.params]
        func_type = MType(param_types, ast.retType)
        if self.current_function is None:
            res = self.lookup(ast.name, c[0], lambda x: x.name)
            res2 = self.lookup(ast.name, self.buildin_functions, lambda x: x.name)
            if not res is None or not res2 is None:
                raise Redeclared(Function(), ast.name)     
            c[0].insert(0, Symbol(ast.name, func_type, None))

        params = []
        for param in ast.params:
            if self.lookup(param.parName, params, lambda x: x.name):
                raise Redeclared(Parameter(), param.parName)  # Chỉ kiểm tra trong tham số
            params.insert(0, Symbol(param.parName, param.parType))
        
        temp = self.current_function
        self.current_function = func_type
        self.visit(ast.body, [[]] + [params] + c)  # Truyền cả local và global scope
        self.current_function = temp
        return Symbol(ast.name, func_type)

    def visitMethodDecl(self, ast, c):
        # traverse_env(c, "visitMethodDecl")
        sym = self.lookup(ast.recType.name, self.types, lambda x: x.name)

        if sym is None or not (isinstance(sym, StructType) or isinstance(sym, InterfaceType)):
            raise Undeclared(Type(), str(ast.recType))
        
        receiver_scope = []
        if isinstance(sym, StructType):
            # Scope của struct (fields + methods)
            methods = []
            for i in sym.methods:
                param_types = [param.parType for param in i.fun.params]
                func_type = MType(param_types, i.fun.retType)
                methods.append(Symbol(i.fun.name, func_type))
            receiver_scope = [Symbol(i[0], i[1], None) for i in sym.elements] + methods

        elif isinstance(sym, InterfaceType):
            # Scope của interface (methods)
            receiver_scope = [Symbol(i.name, MType(i.params, i.retType)) for i in sym.methods]

        method_scope = [[]] + [[Symbol(ast.receiver, sym, None)]] + [receiver_scope] + c
        # traverse_env(method_scope, "visitMethodScope")
        temp = self.current_function
        self.current_function = ast
        self.visit(ast.fun, method_scope)
        self.current_function = temp
        

    def visitPrototype(self, ast, c):
        # traverse_env(c, "visitPrototype")
        if self.lookup(ast.name, c[0], lambda x: x.name):
            raise Redeclared(Prototype(), ast.name)
        
        param_types = [param.parType for param in ast.params]
        func_type = MType(param_types, ast.returnType)
        c[0].insert(0, Symbol(ast.name, func_type))
        
        return Symbol(ast.name, func_type)

    def visitIntType(self, ast, c):
        return IntType()
    
    def visitFloatType(self, ast, c):
        return FloatType()
    
    def visitBoolType(self, ast, c):
        return BoolType()
    
    def visitStringType(self, ast, c):
        return StringType()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    def visitArrayType(self, ast, c):
        """
        ast: ArrayType(dimens: List[Expr], eleType: Type)
        c: Environment (list of scopes)
        Trả về ArrayType nếu hợp lệ, ném lỗi nếu không.
        """
        # traverse_env(c, "visitArrayType")  # Debug scope (nếu cần)

        # Bước 1: Kiểm tra eleType
        if ast.eleType is None:
            raise Undeclared(Type(), "None")
        ele_type = self._resolve_type(ast.eleType, c)
        if isinstance(ele_type, VoidType):
            raise TypeMismatch(ast)  # eleType không được là VoidType

        # Bước 2: Kiểm tra dimens
        if ast.dimens is None or not ast.dimens:
            raise TypeMismatch(ast)  # dimens không được None hoặc rỗng
        for dim_expr in ast.dimens:
            dim_type = self.visit(dim_expr, c)
            if not isinstance(dim_type, IntType):
                raise TypeMismatch(ast)  # Kích thước phải là IntType

        # Bước 3: Trả về ArrayType
        return ArrayType(dimens=ast.dimens, eleType=ele_type)

    # Hàm phụ trợ
    def _resolve_type(self, type_obj: Type, env) -> Type:
        """Giải quyết kiểu, xử lý trường hợp Id hoặc Type trực tiếp."""
        if isinstance(type_obj, Id):
            resolved = self.lookup(type_obj.name, self.types, lambda x: x.name)
            if resolved is None:
                raise Undeclared(Type(), type_obj.name)
            return resolved
        return type_obj
    
    def visitStructType(self, ast, c):
        
        if self.first_phase:
            # Kiểm tra Redeclared cho tên struct
            if self.lookup(ast.name, self.types, lambda x: x.name):
                raise Redeclared(Type(), ast.name)
        else:
            # Kiểm tra Redeclared cho tên struct
            if self.lookup(ast.name, self.buildin_functions, lambda x: x.name):
                raise Redeclared(Type(), ast.name)
            if self.lookup(ast.name, c[0], lambda x: x.name):
                raise Redeclared(Type(), ast.name)    
        # Kiểm tra các field trong struct
        field_scope = []
        for field in ast.elements:
            if self.lookup(field[0], field_scope, lambda x: x[0]):
                raise Redeclared(Field(), field[0])
            field_scope.insert(0, field)    
        return ast

    def visitInterfaceType(self, ast, c):

        if self.first_phase:
            # Kiểm tra Redeclared cho tên interface
            if self.lookup(ast.name, self.types, lambda x: x.name):
                raise Redeclared(Type(), ast.name)
        else:
            # Kiểm tra Redeclared cho tên interface
            if self.lookup(ast.name, self.buildin_functions, lambda x: x.name):
                raise Redeclared(Type(), ast.name)
            if self.lookup(ast.name, c[0], lambda x: x.name):
                raise Redeclared(Type(), ast.name)
        
        interface_scope = []
        # Kiểm tra các phương thức trong interface
        for method in ast.methods:

            if self.lookup(method.name, interface_scope, lambda x: x.name):
                raise Redeclared(Prototype(), method.name)
            
            interface_scope.insert(0, method)
        
        return ast
    
    def visitBlock(self, ast, c):
        self.is_statement_context = True
        for member in ast.member:
            if isinstance(member, Decl):
                c[0].insert(0, self.visit(member, c))
            else:
                self.visit(member, c)
        self.is_statement_context = False
 
    def visitAssign(self, ast, c):
        """Kiểm tra câu lệnh gán trong MiniGo.
        ast: Assign(lhs: Expr, rhs: Expr, is_extended_op: bool)
        c: Environment (list of scopes)
        """
        # traverse_env(c, "visitAssign")  # Debug scope
        # print("ast", ast)
        # Bước 1: Kiểm tra RHS trước để xác định loại gán
        rhs_type, is_extended_op = self._analyze_rhs(ast.rhs, ast.lhs, c)

        # Bước 2: Xử lý LHS
        if isinstance(ast.lhs, Id):
            lhs_symbol = self._lookup_symbol(ast.lhs.name, c)

            # print("lhs_symbol", lhs_symbol)
            if not is_extended_op:  # Toán tử :=
                if lhs_symbol is None or isinstance(lhs_symbol.mtype, MType):  # Chưa khai báo -> khai báo mới
                    if isinstance(rhs_type, VoidType):
                        raise TypeMismatch(ast)
                    # if not self._is_scalar_type(rhs_type):
                    #     raise TypeMismatch(ast)
                    c[0].insert(0, Symbol(ast.lhs.name, rhs_type, None))
                    return  # Kết thúc vì khai báo mới
                else:  # Đã khai báo -> gán giá trị
                    lhs_type = lhs_symbol.mtype
            else:  # Toán tử =, +=, -=, v.v.
                if lhs_symbol is None:
                    raise Undeclared(Identifier(), ast.lhs.name)
                if isinstance(lhs_symbol.mtype, MType):
                    raise Redeclared(Variable(), ast.lhs.name)
                if not self._is_scalar_type(lhs_symbol.mtype):
                    raise TypeMismatch(ast)
                lhs_type = lhs_symbol.mtype

        elif isinstance(ast.lhs, ArrayCell):
            lhs_type = self.visit(ast.lhs, c)  # Lấy kiểu phần tử từ ArrayCell
            arr_symbol = self._lookup_symbol(ast.lhs.arr.name, c) if isinstance(ast.lhs.arr, Id) else None
            if arr_symbol is None and isinstance(ast.lhs.arr, Id):
                raise Undeclared(Identifier(), ast.lhs.arr.name)
            arr_type = arr_symbol.mtype if arr_symbol else self.visit(ast.lhs.arr, c)
            if not isinstance(arr_type, ArrayType):
                raise TypeMismatch(ast)
            if isinstance(lhs_type, ArrayType):  # LHS phải là phần tử, không phải mảng
                raise TypeMismatch(ast)

        elif isinstance(ast.lhs, FieldAccess):
            lhs_type = self.visit(ast.lhs, c)  # Lấy kiểu của trường
            obj_symbol = self._lookup_symbol(ast.lhs.receiver.name, c) if isinstance(ast.lhs.receiver, Id) else None
            if obj_symbol is None and isinstance(ast.lhs.receiver, Id):
                raise Undeclared(Identifier(), ast.lhs.obj.name)
            obj_type = obj_symbol.mtype if obj_symbol else self.visit(ast.lhs.receiver, c)
            if not isinstance(obj_type, StructType):
                raise TypeMismatch(ast)
            if lhs_type is None:
                raise Undeclared(Field(), ast.lhs.field.name)

        else:
            raise TypeMismatch(ast)

        # Bước 3: Kiểm tra và cập nhật gán
        if isinstance(lhs_type, VoidType):
            raise TypeMismatch(ast)
        if not self.is_compatible_type(lhs_type, rhs_type, [(FloatType, IntType), (InterfaceType, StructType)], c, allow_cast=True):
            raise TypeMismatch(ast)
        # Cập nhật giá trị (nếu cần, chỉ cho Id)
        if isinstance(ast.lhs, Id) and lhs_symbol:
            lhs_symbol.value = ast.rhs  # Lưu biểu thức RHS thay vì rhs_type
            
    def _analyze_rhs(self, rhs: Expr, lhs: Expr, env: List[List[Symbol]]) -> Tuple[Type, bool]:
        """Phân tích RHS để xác định loại gán và trả về kiểu."""
        if isinstance(rhs, BinaryOp):
            if isinstance(rhs.left, Id) and rhs.left.name == (lhs.name if isinstance(lhs, Id) else None):
                op = rhs.op
                if op in ['+', '-', '*', '/', '%']:
                    rhs_type = self.visitBinaryOp(rhs, env)
                    return rhs_type, True  # Là +=, -=, v.v.
        self.is_statement_context = False
        rhs_type = self.visit(rhs, env)
        self.is_statement_context = True
        return rhs_type, False  # Là = hoặc :=
    
    def _is_scalar_type(self, type_obj: Type) -> bool:
        """Kiểm tra xem kiểu có phải scalar không."""
        return isinstance(type_obj, (IntType, FloatType, BoolType, StringType))
   
    def visitIf(self, ast, c):
        # traverse_env(c, "visitIf")
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.thenStmt, [[]] + c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, [[]] + c)
    
    def visitForBasic(self, ast, c):
        """
            cond:Expr
            loop:Block
        """
        
        if not isinstance(self.visit(ast.cond, c), BoolType):
            raise TypeMismatch(ast)
        scope = [[]] + c
        self.visit(ast.loop, scope)
 
    def visitForStep(self, ast, c):
        
        """
            init:Stmt
            cond:Expr
            upda:Assign
            loop:Block
        """
        # traverse_env(c, "visitForStep")
        scope = [[]] + c
        if isinstance(ast.init, Decl):
            scope[0].insert(0, self.visit(ast.init, scope))
        elif isinstance(ast.init, Assign):
            self.visit(ast.init, scope)
        
        if not isinstance(self.visit(ast.cond, scope), BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.upda, scope)
        self.visit(ast.loop, scope)
        
    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]):
        """
        Kiểm tra vòng lặp for ... range trong MiniGo.
        ast: ForEach(idx: Id, value: Id, arr: Expr, loop: Block)
        c: Environment (list of scopes)
        """
        # Tăng scope để debug (nếu có traverse_env)

        # Kiểm tra arr
        arr_type = None
        if isinstance(ast.arr, Id):
            res = self._lookup_symbol(ast.arr.name, c)
            if res is None:
                raise Undeclared(Identifier(), ast.arr.name)
            arr_type = res.mtype
        else:
            arr_type = self.visit(ast.arr, c)  # Nếu arr là biểu thức (khác Id)

        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)
        
        # Xử lý idx (index)
        if ast.idx.name != "_":  # Không phải blank identifier
            res = self._lookup_symbol(ast.idx.name, c)
            if res is None:
                raise Undeclared(Identifier(), ast.idx.name)
            if not isinstance(res.mtype, IntType):
                raise TypeMismatch(ast)

        # Xử lý value
        value_type = self._get_value_type(arr_type)
        if ast.value.name != "_":  # Không phải blank identifier
            res = self._lookup_symbol(ast.value.name, c) 
            if res is None:
                raise Undeclared(Identifier(), ast.value.name)
            else:
                if not self.is_compatible_type(res.mtype, value_type, [], c, False):
                    raise TypeMismatch(ast)
     
        # Kiểm tra thân vòng lặp
        self.visit(ast.loop, [[]] + c)


    def _get_value_type(self, arr_type: ArrayType) -> Type:
        """Tính kiểu của value dựa trên dimens và eleType."""
        if len(arr_type.dimens) == 1:
            return arr_type.eleType  # Mảng 1 chiều -> value là eleType
        else:
            # Loại bỏ chiều ngoài cùng, giữ các chiều còn lại
            return ArrayType(dimens=arr_type.dimens[1:], eleType=arr_type.eleType)
        
    def visitContinue(self, ast, c):        
        pass
    
    def visitBreak(self, ast, c):
        pass
    
    def visitReturn(self, ast, c):
        # traverse_env(c, "visitReturn")
    
        if ast.expr is not None:
            self.is_statement_context = False
            
            if not self.is_compatible_type(self.current_function.rettype, self.visit(ast.expr, c), [], c, False):
                raise TypeMismatch(ast)
            self.is_statement_context = True
        else:
            if not type(VoidType()) is type(self.current_function.rettype):
                raise TypeMismatch(ast)

    def visitBinaryOp(self, ast, c):
        # traverse_env(c, "visitBinaryOp")
        
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        
        result = None
        if ast.op in ['+']:
            if type(left) is StringType and type(right) is StringType:
                result = StringType()
            elif type(left) is IntType and type(right) is IntType:
                result = IntType()
            elif type(left) is FloatType and type(right) is FloatType \
                or type(left) is IntType and type(right) is FloatType \
                or type(left) is FloatType and type(right) is IntType:
                result = FloatType()
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['-','*','/']:
            if type(left) is IntType and type(right) is IntType:
                result = IntType()
            elif type(left) is FloatType and type(right) is FloatType \
                or type(left) is IntType and type(right) is FloatType \
                or type(left) is FloatType and type(right) is IntType:
                result = FloatType()
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['%']:
            if type(left) is IntType and type(right) is IntType:
                result = IntType()
            else:
                raise TypeMismatch(ast)
        elif ast.op in ['<','<=','>','>=','==','!=']:
            if not type(left) is type(right):
                raise TypeMismatch(ast)
            if not type(left) in [IntType, FloatType, StringType]:
                raise TypeMismatch(ast)
            result = BoolType()
        elif ast.op in ['&&','||', '!']:
            if not type(left) is type(right):
                raise TypeMismatch(ast)
            if not type(left) is BoolType:
                raise TypeMismatch(ast)
            result = BoolType()
        # print("result", result)
        return result
    
    def visitUnaryOp(self, ast, c):
        
        body = self.visit(ast.body, c)
        
        if ast.op in ['-']:
            if not type(body) in [IntType, FloatType]:
                raise TypeMismatch(ast)
            return body
        elif ast.op in ['!']:
            if not type(body) is BoolType:
                raise TypeMismatch(ast)
            return BoolType()
    
    def visitFuncCall(self, ast, c):
        """
            funName:str
            args:List[Expr] # [] if there is no arg 
        """
        # traverse_env(c, "visitFuncCall")
        # func_sym = self.lookup(ast.funName, self.functions, lambda x: x.name)
        func_sym = self._lookup_symbol(ast.funName, c)
        if func_sym is None:
            func_sym = self.lookup(ast.funName, self.functions, lambda x: x.name)
    
        if func_sym is None:
            raise Undeclared(Function(), ast.funName)

        if not isinstance(func_sym.mtype, MType):
            raise Undeclared(Function(), ast.funName)
        
        if len(ast.args) != len(func_sym.mtype.partype):
            raise TypeMismatch(ast)
        
        for arg, param in zip(ast.args, func_sym.mtype.partype):
            temp = self.is_statement_context
            self.is_statement_context = False
            arg_type = self.visit(arg, c)
            self.is_statement_context = temp
            
            param_type = self.lookup(param.name, self.types, lambda x: x.name) if isinstance(param, Id) else param
            if isinstance(arg_type, StructType) and arg_type.name == '':
                continue
            if not self.is_compatible_type(param_type, arg_type, [], c, False):
                raise TypeMismatch(ast)
        
        ret_type = func_sym.mtype.rettype
        if self.is_statement_context:
            if not isinstance(ret_type, VoidType):
                raise TypeMismatch(ast)
        else:  # Trong expression
            if isinstance(ret_type, VoidType):
                raise TypeMismatch(ast)
        return func_sym.mtype.rettype

    def visitMethCall(self, ast, c):
        # traverse_env(c, "visitMethCall")

        res = self._lookup_symbol(ast.receiver.name, c)

        if res is None:
            raise Undeclared(Identifier(), ast.receiver.name)
        if not isinstance(res.mtype, StructType) and not isinstance(res.mtype, InterfaceType):
            raise TypeMismatch(ast)
        res_type = res.mtype
        ret_type = None
        if isinstance(res_type, StructType):
            for method in res_type.methods:
                if ast.metName == method.fun.name:
                    if len(ast.args) != len(method.fun.params):
                        raise TypeMismatch(ast)
                    for arg, param in zip(ast.args, method.fun.params):
                        if not self.is_compatible_type(self.visit(arg, c), param.parType, [], c):
                            raise TypeMismatch(ast)
                    ret_type = method.fun.retType
        elif isinstance(res_type, InterfaceType):
            for method in res_type.methods:
                if ast.metName == method.name:
                    # print("method", method)
                    if len(ast.args) != len(method.params):
                        raise TypeMismatch(ast)
                    for arg, param in zip(ast.args, method.params):
                        if not self.is_compatible_type(self.visit(arg, c), param, [], c):
                            raise TypeMismatch(ast)
                    ret_type = method.retType
        else:
            raise Undeclared(Method(), ast.metName)
        
        if ret_type is None:
            raise Undeclared(Method(), ast.metName)
        
        if self.is_statement_context:
            if not isinstance(ret_type, VoidType):
                raise TypeMismatch(ast)
        else:  # Trong expression
            if isinstance(ret_type, VoidType):
                raise TypeMismatch(ast)
        
        return ret_type

    def visitId(self,ast,c):
        
        res = self._lookup_symbol(ast.name, c)
        
        if res is None or not isinstance(res, Symbol) or isinstance(res.mtype, MType):
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        """
        Kiểm tra truy cập phần tử mảng trong MiniGo.
        ast: ArrayCell(arr: Expr, idx: List[Expr])
        c: Environment (list of scopes)
        """
        # Debug scope (giả định traverse_env có sẵn)
        # traverse_env(c, "visitArrayCell")

        # Kiểm tra arr
        arr_type = self.visit(ast.arr, c)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)

        # Kiểm tra số lượng chỉ số
        if len(ast.idx) > len(arr_type.dimens):
            raise TypeMismatch(ast)

        # Kiểm tra kiểu của từng chỉ số
        for idx_expr in ast.idx:
            idx_type = self.visit(idx_expr, c)
            if not isinstance(idx_type, IntType):
                raise TypeMismatch(ast)

        # Xác định kiểu trả về
        remaining_dims = len(arr_type.dimens) - len(ast.idx)
        if remaining_dims == 0:
            # Truy cập đến phần tử cuối cùng
            return arr_type.eleType
        else:
            # Trả về mảng với số chiều còn lại
            new_dimens = arr_type.dimens[len(ast.idx):]
            return ArrayType(new_dimens, arr_type.eleType)
    
    def visitFieldAccess(self, ast, c):
        """
            receiver:Expr
            field:str
        """
        # traverse_env(c, "visitFieldAccess")

        # Bước 1: Lấy kiểu của receiver
        receiver_type = self.visit(ast.receiver, c)
        if isinstance(receiver_type, Id):
            receiver_type = self.lookup(receiver_type.name, self.types, lambda x: x.name)
            if receiver_type is None:
                raise Undeclared(Type(), str(ast.receiver))
        # Bước 2: Kiểm tra receiver có phải StructType không
        if not isinstance(receiver_type, StructType):
            raise TypeMismatch(ast)

        # Bước 3: Tìm trường trong StructType
        field = self.lookup(ast.field, receiver_type.elements, lambda x: x[0])
        if field is None:
            raise Undeclared(Field(), ast.field)
        return field[1]
    
    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        """
        ast: ArrayLiteral(dimens: List[Expr], eleType: Type, value: NestedList)
        c: Environment (list of scopes)
        Trả về ArrayType nếu hợp lệ, ném lỗi nếu không.
        """
        # traverse_env(c, "visitArrayLiteral")  # Debug scope (nếu cần)

        # Bước 1: Kiểm tra dimens
        if not ast.dimens:
            raise TypeMismatch(ast)  # ArrayLiteral phải có ít nhất 1 chiều
        for dim_expr in ast.dimens:
            dim_type = self.visit(dim_expr, c)
            if not isinstance(dim_type, IntType):
                raise TypeMismatch(ast)  # Kích thước phải là IntType

        # Bước 2: Kiểm tra value khớp với dimens và eleType
        expected_dims = len(ast.dimens)
        actual_dims = self._get_nested_depth(ast.value)
        if expected_dims != actual_dims:
            raise TypeMismatch(ast)  # Số chiều không khớp

        # Bước 3: Kiểm tra kiểu của các phần tử trong value
        flat_elements = self._flatten_nested_list(ast.value)
        for elem in flat_elements:
            elem_type = self.visit(elem, c) if isinstance(elem, Expr) else self._infer_primlit_type(elem, ast)
            if not self.is_compatible_type(ast.eleType, elem_type, [(FloatType, IntType), (InterfaceType, StructType)], c, allow_cast=True):
                raise TypeMismatch(ast)  # Kiểu phần tử không khớp với eleType

        # Bước 4: Trả về ArrayType
        return ArrayType(dimens=ast.dimens, eleType=ast.eleType)

    # Hàm phụ trợ
    def _get_nested_depth(self, nested_list: NestedList) -> int:
        """Tính độ sâu của NestedList."""
        if not isinstance(nested_list, list):
            return 0
        if not nested_list:  # Danh sách rỗng
            return 1
        return 1 + self._get_nested_depth(nested_list[0])

    def _flatten_nested_list(self, nested_list: NestedList) -> List:
        """Làm phẳng NestedList thành danh sách các phần tử cơ bản."""
        flat = []
        if isinstance(nested_list, list):
            for item in nested_list:
                flat.extend(self._flatten_nested_list(item))
        else:
            flat.append(nested_list)
        return flat

    def _infer_primlit_type(self, primlit, ast) -> Type:
        """Suy ra kiểu từ PrimLit."""
        if isinstance(primlit, int):
            return IntType()
        elif isinstance(primlit, float):
            return FloatType()
        elif isinstance(primlit, bool):
            return BoolType()
        elif isinstance(primlit, str):
            return StringType()
        raise TypeMismatch(ast)  # PrimLit không hợp lệ

    def visitStructLiteral(self, ast, c):
        """
        ast: StructLiteral(name: str, elements: List[Tuple[str, Expr]])
        c: Environment (list of scopes)
        Trả về StructType nếu hợp lệ, ném lỗi nếu không.
        """
        # traverse_env(c, "visitStructLiteral")  # Debug scope (nếu cần)

        # Bước 1: Kiểm tra StructType tồn tại
        struct_type = self.lookup(ast.name, self.types, lambda x: x.name)
        if struct_type is None:
            raise Undeclared(Type(), ast.name)
        if not isinstance(struct_type, StructType):
            raise TypeMismatch(ast)

        # Bước 2: Kiểm tra elements của StructLiteral
        defined_fields = {field[0]: field[1] for field in struct_type.elements}  # Từ StructType
        provided_fields = {field_name: expr for field_name, expr in ast.elements}  # Từ StructLiteral

        # Kiểm tra từng trường được cung cấp
        for field_name, expr in ast.elements:
            if field_name not in defined_fields:
                raise Undeclared(Field(), field_name)  # Trường không tồn tại trong struct
            expected_type = defined_fields[field_name]
            actual_type = self.visit(expr, c)
            if not self.is_compatible_type(expected_type, actual_type, [], c, allow_cast=False):
                raise TypeMismatch(ast)  # Kiểu của expr không khớp với kiểu trường

        # Kiểm tra xem có thiếu trường bắt buộc nào không (tùy MiniGo, có thể bỏ qua)
        # for field_name in defined_fields:
        #     if field_name not in provided_fields:
        #         raise TypeMismatch(ast)  # Thiếu trường bắt buộc

        # Bước 3: Trả về StructType
        return struct_type

    def visitNilLiteral(self, ast, c):
        return StructType("",[], [])