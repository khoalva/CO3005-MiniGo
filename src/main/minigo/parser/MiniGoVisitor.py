# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inBlockStatement.
    def visitInBlockStatement(self, ctx:MiniGoParser.InBlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:MiniGoParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MiniGoParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:MiniGoParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:MiniGoParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniGoParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#recType.
    def visitRecType(self, ctx:MiniGoParser.RecTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MiniGoParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MiniGoParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_op.
    def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forClause.
    def visitForClause(self, ctx:MiniGoParser.ForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initStmt.
    def visitInitStmt(self, ctx:MiniGoParser.InitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#postStmt.
    def visitPostStmt(self, ctx:MiniGoParser.PostStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalarAssignment.
    def visitScalarAssignment(self, ctx:MiniGoParser.ScalarAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rangeClause.
    def visitRangeClause(self, ctx:MiniGoParser.RangeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionParts.
    def visitExpressionParts(self, ctx:MiniGoParser.ExpressionPartsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionPart.
    def visitExpressionPart(self, ctx:MiniGoParser.ExpressionPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logicalExpr.
    def visitLogicalExpr(self, ctx:MiniGoParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#higherLogicalExpr.
    def visitHigherLogicalExpr(self, ctx:MiniGoParser.HigherLogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MiniGoParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniGoParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniGoParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#selector.
    def visitSelector(self, ctx:MiniGoParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arguments.
    def visitArguments(self, ctx:MiniGoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index.
    def visitIndex(self, ctx:MiniGoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicLit.
    def visitBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayLit.
    def visitArrayLit(self, ctx:MiniGoParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayValue.
    def visitArrayValue(self, ctx:MiniGoParser.ArrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayElems.
    def visitArrayElems(self, ctx:MiniGoParser.ArrayElemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structvalue.
    def visitStructvalue(self, ctx:MiniGoParser.StructvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldValue.
    def visitFieldValue(self, ctx:MiniGoParser.FieldValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDeclarations.
    def visitFieldDeclarations(self, ctx:MiniGoParser.FieldDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:MiniGoParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceElem.
    def visitInterfaceElem(self, ctx:MiniGoParser.InterfaceElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodElem.
    def visitMethodElem(self, ctx:MiniGoParser.MethodElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter_type.
    def visitParameter_type(self, ctx:MiniGoParser.Parameter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rel_op.
    def visitRel_op(self, ctx:MiniGoParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_op.
    def visitAdd_op(self, ctx:MiniGoParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_op.
    def visitMul_op(self, ctx:MiniGoParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unary_op.
    def visitUnary_op(self, ctx:MiniGoParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#getIntCall.
    def visitGetIntCall(self, ctx:MiniGoParser.GetIntCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putIntCall.
    def visitPutIntCall(self, ctx:MiniGoParser.PutIntCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putIntLnCall.
    def visitPutIntLnCall(self, ctx:MiniGoParser.PutIntLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#getFloatCall.
    def visitGetFloatCall(self, ctx:MiniGoParser.GetFloatCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putFloatCall.
    def visitPutFloatCall(self, ctx:MiniGoParser.PutFloatCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putFloatLnCall.
    def visitPutFloatLnCall(self, ctx:MiniGoParser.PutFloatLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#getBoolCall.
    def visitGetBoolCall(self, ctx:MiniGoParser.GetBoolCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putBoolCall.
    def visitPutBoolCall(self, ctx:MiniGoParser.PutBoolCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putBoolLnCall.
    def visitPutBoolLnCall(self, ctx:MiniGoParser.PutBoolLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#getStringCall.
    def visitGetStringCall(self, ctx:MiniGoParser.GetStringCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putStringCall.
    def visitPutStringCall(self, ctx:MiniGoParser.PutStringCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putStringLnCall.
    def visitPutStringLnCall(self, ctx:MiniGoParser.PutStringLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#putLnCall.
    def visitPutLnCall(self, ctx:MiniGoParser.PutLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGoParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expressionList.
    def visitExpressionList(self, ctx:MiniGoParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inBlockStatementList.
    def visitInBlockStatementList(self, ctx:MiniGoParser.InBlockStatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declarationList.
    def visitDeclarationList(self, ctx:MiniGoParser.DeclarationListContext):
        return self.visitChildren(ctx)



del MiniGoParser