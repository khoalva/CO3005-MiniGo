
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
class ASTGeneration(MiniGoVisitor):
# Visit a parse tree produced by MiniGoParser#program.
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        decls = self.visit(ctx.declarationList())
        return Program(decls)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):

        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#inBlockStatement.
    def visitInBlockStatement(self, ctx:MiniGoParser.InBlockStatementContext):

        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):

        return self.visit(ctx.getChild(0))

        # Visit a parse tree produced by MiniGoParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:MiniGoParser.DeclarationStatementContext):

        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MiniGoParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MiniGoParser.VariableDeclarationContext):
        # Get variable name
        varName = ctx.IDENTIFIER().getText()
        
        if ctx.types():
            varType = self.visit(ctx.types())
            return VarDecl(varName, varType, self.visit(ctx.expression())) if ctx.expression() else VarDecl(varName, varType, None)
        else:
            return VarDecl(varName, None, self.visit(ctx.expression()))


    # Visit a parse tree produced by MiniGoParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:MiniGoParser.ConstantDeclarationContext):
        
        # Get constant name
        name = ctx.IDENTIFIER().getText()
        
        # Get type if specified
        constType = None
            
        # Get initializer
        init = self.visit(ctx.expression())
        
        return ConstDecl(name, constType, init)


    # Visit a parse tree produced by MiniGoParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:MiniGoParser.TypeDeclarationContext):

        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by MiniGoParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniGoParser.MethodDeclarationContext):
        
        reciever = self.visit(ctx.receiver())
        recType = self.visit(ctx.recType())

        name = ctx.IDENTIFIER().getText()
        if ctx.parameter_type():
            params = self.visit(ctx.parameter_type())
        else:  
            params = []

        if ctx.types():
            returnType = self.visit(ctx.types())
        else:
            returnType = VoidType()
        
        body = self.visit(ctx.block())

        fun = FuncDecl(name, params, returnType, body)
        return MethodDecl(reciever, recType, fun)

        # Visit a parse tree produced by MiniGoParser#reciever.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return ctx.IDENTIFIER().getText()

    # Visit a parse tree produced by MiniGoParser#recType.
    def visitRecType(self, ctx:MiniGoParser.RecTypeContext):
        return Id(ctx.IDENTIFIER().getText())

    # Visit a parse tree produced by MiniGoParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MiniGoParser.FunctionDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        if ctx.parameter_type():
            params = self.visit(ctx.parameter_type())
        else:
            params = []
        
        if ctx.types():
            returnType = self.visit(ctx.types())
        else:
            returnType = VoidType()
        
        body = self.visit(ctx.block())
        
        return FuncDecl(name, params, returnType, body)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return Block(self.visit(ctx.inBlockStatementList()))


    # Visit a parse tree produced by MiniGoParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MiniGoParser.AssignmentStatementContext):

        lhs = self.visit(ctx.lhs())
        op = self.visit(ctx.assign_op())

        if op == '+=': 
            rhs = BinaryOp('+', lhs, self.visit(ctx.expression()))
        elif op == '-=':
            rhs = BinaryOp('-', lhs, self.visit(ctx.expression()))
        elif op == '*=':
            rhs = BinaryOp('*', lhs, self.visit(ctx.expression()))
        elif op == '/=':
            rhs = BinaryOp('/', lhs, self.visit(ctx.expression()))
        elif op == '%=':
            rhs = BinaryOp('%', lhs, self.visit(ctx.expression()))
        else:
            rhs = self.visit(ctx.expression())

        return Assign(lhs, rhs)
    
    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        cond = self.visit(ctx.condition())
        thenStmt = self.visit(ctx.block(0))
        if ctx.block(1):
            elseStmt = self.visit(ctx.block(1))
        elif ctx.ifStatement():
            elseStmt = self.visit(ctx.ifStatement())
        else:
            elseStmt = None

        return If(cond, thenStmt, elseStmt)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        
        if ctx.condition():
            cond = self.visit(ctx.condition())
            block = self.visit(ctx.block())
            return ForBasic(cond, block)
        elif ctx.forClause():
            init, cond, post = self.visit(ctx.forClause())
            block = self.visit(ctx.block())
            return ForStep(init, cond, post, block)
        elif ctx.rangeClause():
            idx, value, expr = self.visit(ctx.rangeClause())
            block = self.visit(ctx.block())
            return ForEach(idx, value, expr, block)


    # Visit a parse tree produced by MiniGoParser#forClause.
    def visitForClause(self, ctx:MiniGoParser.ForClauseContext):
        
            init = self.visit(ctx.initStmt())
            cond = self.visit(ctx.condition())
            post = self.visit(ctx.postStmt())

            return init, cond, post


    # Visit a parse tree produced by MiniGoParser#initStmt.
    def visitInitStmt(self, ctx:MiniGoParser.InitStmtContext):
        
        if ctx.scalarAssignment():
            return self.visit(ctx.scalarAssignment())
        elif ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())


    # Visit a parse tree produced by MiniGoParser#postStmt.
    def visitPostStmt(self, ctx:MiniGoParser.PostStmtContext):
        return self.visit(ctx.scalarAssignment())


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visit(ctx.expression())

    def visitScalarAssignment(self, ctx:MiniGoParser.ScalarAssignmentContext):
        lhs = ctx.IDENTIFIER().getText()
        asign_op = ctx.assign_op().getText()
        if asign_op == '+=':
            rhs = BinaryOp('+', Id(lhs), self.visit(ctx.expression()))
        elif asign_op == '-=':
            rhs = BinaryOp('-', Id(lhs), self.visit(ctx.expression()))
        elif asign_op == '*=':
            rhs = BinaryOp('*', Id(lhs), self.visit(ctx.expression()))
        elif asign_op == '/=':
            rhs = BinaryOp('/', Id(lhs), self.visit(ctx.expression()))
        elif asign_op == '%=':
            rhs = BinaryOp('%', Id(lhs), self.visit(ctx.expression()))
        else:
            rhs = self.visit(ctx.expression())
        return Assign(Id(lhs), rhs)

    # Visit a parse tree produced by MiniGoParser#rangeClause.
    def visitRangeClause(self, ctx:MiniGoParser.RangeClauseContext):
        idx = Id(ctx.IDENTIFIER(0).getText())
        value = Id(ctx.IDENTIFIER(1).getText())
        expr = self.visit(ctx.expression())
        return idx, value, expr


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return(None)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        if ctx.builtInFunctionCall():
            return self.visit(ctx.builtInFunctionCall())
        
        # Get initial identifier
        name = ctx.IDENTIFIER().getText()
        base = Id(name)
        
        # Visit all expression parts
        parts = self.visit(ctx.expressionParts())
        
        # Start with the base identifier and build up the AST
        current = base
        
        for part in parts:
            if part['type'] == 'arguments':
                # If we have a method call receiver ready
                if isinstance(current, FieldAccess):
                    # Create method call from the field access
                    current = MethCall(
                        receiver=current.receiver,
                        metName=current.field,
                        args=part['arguments'] if 'arguments' in part else []
                    )
                else:
                    # Regular function call
                    current = FuncCall(
                        funName=current.name if isinstance(current, Id) else None,
                        args=part['arguments'] if 'arguments' in part else []
                    )
                    
            elif part['type'] == 'selector':
                # Field access
                current = FieldAccess(
                    receiver=current,
                    field=part['identifier']
                )
                
            elif part['type'] == 'index':
                # If we already have an array cell, add to its indices
                if isinstance(current, ArrayCell):
                    current.idx.append(part['expression'])
                else:
                    # Create new array cell
                    current = ArrayCell(
                        arr=current,
                        idx=[part['expression']]
                    )
        
        return current
                    
            

    # Visit a parse tree produced by MiniGoParser#expressionParts.
    def visitExpressionParts(self, ctx:MiniGoParser.ExpressionPartsContext):
        if ctx.expressionParts():
            return [self.visit(ctx.expressionPart())] + self.visit(ctx.expressionParts())
        else:
            return [self.visit(ctx.expressionPart())]

    # Visit a parse tree produced by MiniGoParser#expressionPart.
    def visitExpressionPart(self, ctx:MiniGoParser.ExpressionPartContext):
        if ctx.arguments():
            return self.visit(ctx.arguments())
        elif ctx.index():
            return self.visit(ctx.index())
        elif ctx.selector():
            return self.visit(ctx.selector())


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visit(ctx.logicalExpr())


    # Visit a parse tree produced by MiniGoParser#logicalExpr.
    def visitLogicalExpr(self, ctx:MiniGoParser.LogicalExprContext):
        
        if ctx.OR():
            return BinaryOp(
                op=ctx.OR().getText(),
                left=self.visit(ctx.logicalExpr()),
                right=self.visit(ctx.higherLogicalExpr())
            )
        else:
            return self.visit(ctx.higherLogicalExpr())


    # Visit a parse tree produced by MiniGoParser#higherLogicalExpr.
    def visitHigherLogicalExpr(self, ctx:MiniGoParser.HigherLogicalExprContext):
        
        if ctx.AND():
            return BinaryOp(
                op=ctx.AND().getText(),
                left=self.visit(ctx.higherLogicalExpr()),
                right=self.visit(ctx.relationalExpr())
            )
        else:
            return self.visit(ctx.relationalExpr())


    # Visit a parse tree produced by MiniGoParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MiniGoParser.RelationalExprContext):
        if ctx.rel_op():
            return BinaryOp(
                op=self.visit(ctx.rel_op()),
                left=self.visit(ctx.relationalExpr()),
                right=self.visit(ctx.additiveExpr())
            )
        else:
            return self.visit(ctx.additiveExpr())


    # Visit a parse tree produced by MiniGoParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniGoParser.AdditiveExprContext):
        if ctx.add_op():
            return BinaryOp(
                op=self.visit(ctx.add_op()),
                left=self.visit(ctx.additiveExpr()),
                right=self.visit(ctx.multiplicativeExpr())
            )
        else:
            return self.visit(ctx.multiplicativeExpr())


    # Visit a parse tree produced by MiniGoParser#multiplicative_expr.
    def visitMultiplicativeExpr(self, ctx:MiniGoParser.MultiplicativeExprContext):
        if ctx.mul_op():
            return BinaryOp(
                op=self.visit(ctx.mul_op()),
                left=self.visit(ctx.multiplicativeExpr()),
                right=self.visit(ctx.unaryExpr())
            )
        else:
            return self.visit(ctx.unaryExpr())


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        if ctx.unary_op():
            return UnaryOp(
                op=self.visit(ctx.unary_op()),
                body=self.visit(ctx.unaryExpr())
            )
        else:
            return self.visit(ctx.primaryExpr())


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        if ctx.operand():
            return self.visit(ctx.operand())
        else:
            base = self.visit(ctx.primaryExpr())
            if ctx.arguments():
                args = self.visit(ctx.arguments())
                
                if isinstance(base, Id):
                    return FuncCall(funName=base.name, args=args['arguments'])
                elif isinstance(base, FieldAccess):
                    return MethCall(receiver=base.receiver, metName=base.field, args=args['arguments'])
            elif ctx.index():
                idx = self.visit(ctx.index())
                if isinstance(base, ArrayCell):
                    base.idx.append(idx['expression'])
                    return base
                else:
                    return ArrayCell(arr=base, idx=[idx['expression']])
            elif ctx.selector():
                field = self.visit(ctx.selector())
                return FieldAccess(receiver=base, field=field['identifier'])
        


    # Visit a parse tree produced by MiniGoParser#selector.
    def visitSelector(self, ctx:MiniGoParser.SelectorContext):
        return {'type': 'selector', 'identifier': ctx.IDENTIFIER().getText()}


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        exprs = self.visit(ctx.expressionList()) if ctx.expressionList() else []
        return {'type': 'arguments', 'arguments': exprs}


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return {'type': 'index', 'expression': self.visit(ctx.expression())}


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.basicLit():
            return self.visit(ctx.basicLit())
        elif ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.structLit():
            return self.visit(ctx.structLit())
        elif ctx.expression():
            return self.visit(ctx.expression())


    # Visit a parse tree produced by MiniGoParser#basicLit.
    def visitBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.BOOL_LIT():
            return BooleanLiteral(ctx.BOOL_LIT().getText() == 'true')
        elif ctx.NIL_LIT():
            return NilLiteral()


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        arrayType = self.visit(ctx.arrayType())
        elems = self.visit(ctx.arrayValue())
        return ArrayLiteral(arrayType.dimens, arrayType.eleType, elems)


    # Visit a parse tree produced by MiniGoParser#arrayValue.
    def visitArrayValue(self, ctx:MiniGoParser.ArrayValueContext):
        return self.visit(ctx.arrayElems())


    # Visit a parse tree produced by MiniGoParser#arrayElems.
    def visitArrayElems(self, ctx:MiniGoParser.ArrayElemsContext):
        if ctx.arrayElems():
            if ctx.basicLit():
                return [self.visit(ctx.basicLit())] + self.visit(ctx.arrayElems())
            elif ctx.IDENTIFIER():
                return [Id(ctx.IDENTIFIER().getText())] + self.visit(ctx.arrayElems())
            elif ctx.arrayValue():
                return [self.visit(ctx.arrayValue())] + self.visit(ctx.arrayElems())
            elif ctx.structLit():
                return [self.visit(ctx.structLit())] + self.visit(ctx.arrayElems())
        else:
            if ctx.basicLit():
                return [self.visit(ctx.basicLit())]
            elif ctx.IDENTIFIER():
                return [Id(ctx.IDENTIFIER().getText())]
            elif ctx.arrayValue():
                return [self.visit(ctx.arrayValue())]
            elif ctx.structLit():
                return [self.visit(ctx.structLit())]


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        name = ctx.IDENTIFIER().getText()
        fields = self.visit(ctx.structvalue())
        return StructLiteral(name, fields)


    # Visit a parse tree produced by MiniGoParser#structvalue.
    def visitStructvalue(self, ctx:MiniGoParser.StructvalueContext):
        return self.visit(ctx.fieldValue()) if ctx.fieldValue() else []


    # Visit a parse tree produced by MiniGoParser#fieldValue.
    def visitFieldValue(self, ctx:MiniGoParser.FieldValueContext):
        return [(ctx.IDENTIFIER().getText(), self.visit(ctx.expression()))] + self.visit(ctx.fieldValue()) \
            if ctx.fieldValue() else [(ctx.IDENTIFIER().getText(), self.visit(ctx.expression()))]

    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        types = self.visit(ctx.types())
        if isinstance(types, ArrayType):
            if ctx.INT_LIT():
                return ArrayType([IntLiteral(ctx.INT_LIT().getText())] + types.dimens, types.eleType)
            elif ctx.IDENTIFIER():
                return ArrayType([Id(ctx.IDENTIFIER().getText())] + types.dimens, types.eleType)
        else:
            if ctx.INT_LIT():
                return ArrayType([IntLiteral(ctx.INT_LIT().getText())], types)
            elif ctx.IDENTIFIER():
                return ArrayType([Id(ctx.IDENTIFIER().getText())], types)

    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        name = ctx.IDENTIFIER().getText()
        elements = self.visit(ctx.fieldDeclarations())
        return StructType(name, elements, [])


    # Visit a parse tree produced by MiniGoParser#field_method_declaration.
    def visitFieldDeclarations(self, ctx:MiniGoParser.FieldDeclarationsContext):
        if ctx.fieldDeclarations():
            return self.visit(ctx.fieldDeclaration()) + self.visit(ctx.fieldDeclarations())
        else:
            return self.visit(ctx.fieldDeclaration())

    # Visit a parse tree produced by MiniGoParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:MiniGoParser.FieldDeclarationContext):
        elements = self.visit(ctx.identifierList())
        eleType = self.visit(ctx.types())
        return [(ele, eleType) for ele in elements]


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        name = ctx.IDENTIFIER().getText()
        methods = self.visit(ctx.interfaceElem())
        return InterfaceType(name, methods)


    # Visit a parse tree produced by MiniGoParser#interfaceElem.
    def visitInterfaceElem(self, ctx:MiniGoParser.InterfaceElemContext):
        if ctx.interfaceElem():
            return [self.visit(ctx.methodElem())] + self.visit(ctx.interfaceElem())
        else:
            return [self.visit(ctx.methodElem())]

    # Visit a parse tree produced by MiniGoParser#methodElem.
    def visitMethodElem(self, ctx:MiniGoParser.MethodElemContext):
        name = ctx.IDENTIFIER().getText()
        typeList = [param_type.parType for param_type in self.visit(ctx.parameter_type()) if isinstance(param_type, ParamDecl)] if ctx.parameter_type() else []
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        return Prototype(name, typeList, retType)


    # Visit a parse tree produced by MiniGoParser#parameter_type.
    def visitParameter_type(self, ctx:MiniGoParser.Parameter_typeContext):
        types = self.visit(ctx.types())
        ids = self.visit(ctx.identifierList())
        result = [ParamDecl(id, types) for id in ids]
        return result + self.visit(ctx.parameter_type()) if ctx.parameter_type() else result

    # Visit a parse tree produced by MiniGoParser#rel_op.
    def visitRel_op(self, ctx:MiniGoParser.Rel_opContext):
        return ctx.getText()


    # Visit a parse tree produced by MiniGoParser#add_op.
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#mul_op.
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#unary_op.
    def visitUnary_op(self, ctx:MiniGoParser.Unary_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        
        base = self.visit(ctx.lhs())
        
        if ctx.selector():
            field = self.visit(ctx.selector())
            return FieldAccess(receiver=base, field=field['identifier'])
        elif ctx.index():
            idx = self.visit(ctx.index())
            if isinstance(base, Id) or isinstance(base, FieldAccess):
                return ArrayCell(arr=base, idx=[idx['expression']])
            elif isinstance(base, ArrayCell):
                base.idx.append(idx['expression'])
                return base


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()


    # Visit a parse tree produced by MiniGoParser#getIntCall.
    def visitGetIntCall(self, ctx:MiniGoParser.GetIntCallContext):
        return FuncCall(funName='getInt', args=[])


    # Visit a parse tree produced by MiniGoParser#putIntCall.
    def visitPutIntCall(self, ctx:MiniGoParser.PutIntCallContext):
        return FuncCall(funName='putInt', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#putIntLnCall.
    def visitPutIntLnCall(self, ctx:MiniGoParser.PutIntLnCallContext):
        return FuncCall(funName='putIntLn', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#getFloatCall.
    def visitGetFloatCall(self, ctx:MiniGoParser.GetFloatCallContext):
        return FuncCall(funName='getFloat', args=[])


    # Visit a parse tree produced by MiniGoParser#putFloatCall.
    def visitPutFloatCall(self, ctx:MiniGoParser.PutFloatCallContext):
        return FuncCall(funName='putFloat', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#putFloatLnCall.
    def visitPutFloatLnCall(self, ctx:MiniGoParser.PutFloatLnCallContext):
        return FuncCall(funName='putFloatLn', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#getBoolCall.
    def visitGetBoolCall(self, ctx:MiniGoParser.GetBoolCallContext):
        return FuncCall(funName='getBool', args=[])


    # Visit a parse tree produced by MiniGoParser#putBoolCall.
    def visitPutBoolCall(self, ctx:MiniGoParser.PutBoolCallContext):
        return FuncCall(funName='putBool', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#putBoolLnCall.
    def visitPutBoolLnCall(self, ctx:MiniGoParser.PutBoolLnCallContext):
        return FuncCall(funName='putBoolLn', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#getStringCall.
    def visitGetStringCall(self, ctx:MiniGoParser.GetStringCallContext):
        return FuncCall(funName='getString', args=[])


    # Visit a parse tree produced by MiniGoParser#putStringCall.
    def visitPutStringCall(self, ctx:MiniGoParser.PutStringCallContext):
        return FuncCall(funName='putString', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#putStringLnCall.
    def visitPutStringLnCall(self, ctx:MiniGoParser.PutStringLnCallContext):
        return FuncCall(funName='putStringLn', args=[self.visit(ctx.expression())])


    # Visit a parse tree produced by MiniGoParser#putLnCall.
    def visitPutLnCall(self, ctx:MiniGoParser.PutLnCallContext):
        return FuncCall(funName='putLn', args=[])


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.identifierList()) if ctx.identifierList() else [ctx.IDENTIFIER().getText()]


    # Visit a parse tree produced by MiniGoParser#expersionList.
    def visitExpressionList(self, ctx:MiniGoParser.ExpressionListContext):
        return [self.visit(ctx.expression())] + self.visit(ctx.expressionList()) if ctx.expressionList() else [self.visit(ctx.expression())]


    # Visit a parse tree produced by MiniGoParser#inBlockStatementList.
    def visitInBlockStatementList(self, ctx:MiniGoParser.InBlockStatementListContext):
        if ctx.inBlockStatementList():
            if ctx.statement():
                return [self.visit(ctx.statement())] + self.visit(ctx.inBlockStatementList())
            elif ctx.inBlockStatement():
                return [self.visit(ctx.inBlockStatement())] + self.visit(ctx.inBlockStatementList())
        else:
            if ctx.statement():
                return [self.visit(ctx.statement())]
            elif ctx.inBlockStatement():
                return [self.visit(ctx.inBlockStatement())]


    # Visit a parse tree produced by MiniGoParser#declarationList.
    def visitDeclarationList(self, ctx:MiniGoParser.DeclarationListContext):
        return [self.visit(ctx.declaration())] + self.visit(ctx.declarationList()) if ctx.declarationList() else [self.visit(ctx.declaration())]
