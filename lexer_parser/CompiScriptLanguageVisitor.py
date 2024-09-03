# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompiScriptLanguageParser import CompiScriptLanguageParser
else:
    from CompiScriptLanguageParser import CompiScriptLanguageParser

# This class defines a complete generic visitor for a parse tree produced by CompiScriptLanguageParser.

class CompiScriptLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CompiScriptLanguageParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:CompiScriptLanguageParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CompiScriptLanguageParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#statementDeclaration.
    def visitStatementDeclaration(self, ctx:CompiScriptLanguageParser.StatementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CompiScriptLanguageParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStatement.
    def visitForStatement(self, ctx:CompiScriptLanguageParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:CompiScriptLanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:CompiScriptLanguageParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStatement.
    def visitReturnStatement(self, ctx:CompiScriptLanguageParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:CompiScriptLanguageParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#blockStatement.
    def visitBlockStatement(self, ctx:CompiScriptLanguageParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedAssigment.
    def visitNestedAssigment(self, ctx:CompiScriptLanguageParser.NestedAssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logicOrAssigment.
    def visitLogicOrAssigment(self, ctx:CompiScriptLanguageParser.LogicOrAssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def visitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def visitLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#equality.
    def visitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#factor.
    def visitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedUnary.
    def visitNestedUnary(self, ctx:CompiScriptLanguageParser.NestedUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#callUnary.
    def visitCallUnary(self, ctx:CompiScriptLanguageParser.CallUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#true.
    def visitTrue(self, ctx:CompiScriptLanguageParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#false.
    def visitFalse(self, ctx:CompiScriptLanguageParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#nil.
    def visitNil(self, ctx:CompiScriptLanguageParser.NilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#this.
    def visitThis(self, ctx:CompiScriptLanguageParser.ThisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#number.
    def visitNumber(self, ctx:CompiScriptLanguageParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#string.
    def visitString(self, ctx:CompiScriptLanguageParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#id.
    def visitId(self, ctx:CompiScriptLanguageParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedExpression.
    def visitNestedExpression(self, ctx:CompiScriptLanguageParser.NestedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#super.
    def visitSuper(self, ctx:CompiScriptLanguageParser.SuperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)



del CompiScriptLanguageParser