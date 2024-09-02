# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompiScriptLanguageParser import CompiScriptLanguageParser
else:
    from CompiScriptLanguageParser import CompiScriptLanguageParser

# This class defines a complete listener for a parse tree produced by CompiScriptLanguageParser.
class CompiScriptLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by CompiScriptLanguageParser#program.
    def enterProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#program.
    def exitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#classDeclaration.
    def enterClassDeclaration(self, ctx:CompiScriptLanguageParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#classDeclaration.
    def exitClassDeclaration(self, ctx:CompiScriptLanguageParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:CompiScriptLanguageParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:CompiScriptLanguageParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:CompiScriptLanguageParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:CompiScriptLanguageParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#statementDeclaration.
    def enterStatementDeclaration(self, ctx:CompiScriptLanguageParser.StatementDeclarationContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#statementDeclaration.
    def exitStatementDeclaration(self, ctx:CompiScriptLanguageParser.StatementDeclarationContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#classDecl.
    def enterClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def exitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#funDecl.
    def enterFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def exitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#varDecl.
    def enterVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def exitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CompiScriptLanguageParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CompiScriptLanguageParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#forStatement.
    def enterForStatement(self, ctx:CompiScriptLanguageParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#forStatement.
    def exitForStatement(self, ctx:CompiScriptLanguageParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#ifStatement.
    def enterIfStatement(self, ctx:CompiScriptLanguageParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#ifStatement.
    def exitIfStatement(self, ctx:CompiScriptLanguageParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#printStatement.
    def enterPrintStatement(self, ctx:CompiScriptLanguageParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#printStatement.
    def exitPrintStatement(self, ctx:CompiScriptLanguageParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#returnStatement.
    def enterReturnStatement(self, ctx:CompiScriptLanguageParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#returnStatement.
    def exitReturnStatement(self, ctx:CompiScriptLanguageParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#whileStatement.
    def enterWhileStatement(self, ctx:CompiScriptLanguageParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#whileStatement.
    def exitWhileStatement(self, ctx:CompiScriptLanguageParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#blockStatement.
    def enterBlockStatement(self, ctx:CompiScriptLanguageParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#blockStatement.
    def exitBlockStatement(self, ctx:CompiScriptLanguageParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def enterExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def exitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#forStmt.
    def enterForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def exitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def enterIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def exitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#printStmt.
    def enterPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def exitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def enterReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def exitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def enterWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def exitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#block.
    def enterBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#block.
    def exitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#expression.
    def enterExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#expression.
    def exitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#nestedAssigment.
    def enterNestedAssigment(self, ctx:CompiScriptLanguageParser.NestedAssigmentContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#nestedAssigment.
    def exitNestedAssigment(self, ctx:CompiScriptLanguageParser.NestedAssigmentContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#logicOrAssigment.
    def enterLogicOrAssigment(self, ctx:CompiScriptLanguageParser.LogicOrAssigmentContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#logicOrAssigment.
    def exitLogicOrAssigment(self, ctx:CompiScriptLanguageParser.LogicOrAssigmentContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#logic_or.
    def enterLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def exitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#logic_and.
    def enterLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def exitLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#equality.
    def enterEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#equality.
    def exitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#comparison.
    def enterComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#comparison.
    def exitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#term.
    def enterTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#term.
    def exitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#factor.
    def enterFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#factor.
    def exitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#nestedUnary.
    def enterNestedUnary(self, ctx:CompiScriptLanguageParser.NestedUnaryContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#nestedUnary.
    def exitNestedUnary(self, ctx:CompiScriptLanguageParser.NestedUnaryContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#callUnary.
    def enterCallUnary(self, ctx:CompiScriptLanguageParser.CallUnaryContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#callUnary.
    def exitCallUnary(self, ctx:CompiScriptLanguageParser.CallUnaryContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#call.
    def enterCall(self, ctx:CompiScriptLanguageParser.CallContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#call.
    def exitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#true.
    def enterTrue(self, ctx:CompiScriptLanguageParser.TrueContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#true.
    def exitTrue(self, ctx:CompiScriptLanguageParser.TrueContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#false.
    def enterFalse(self, ctx:CompiScriptLanguageParser.FalseContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#false.
    def exitFalse(self, ctx:CompiScriptLanguageParser.FalseContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#nil.
    def enterNil(self, ctx:CompiScriptLanguageParser.NilContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#nil.
    def exitNil(self, ctx:CompiScriptLanguageParser.NilContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#this.
    def enterThis(self, ctx:CompiScriptLanguageParser.ThisContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#this.
    def exitThis(self, ctx:CompiScriptLanguageParser.ThisContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#number.
    def enterNumber(self, ctx:CompiScriptLanguageParser.NumberContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#number.
    def exitNumber(self, ctx:CompiScriptLanguageParser.NumberContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#string.
    def enterString(self, ctx:CompiScriptLanguageParser.StringContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#string.
    def exitString(self, ctx:CompiScriptLanguageParser.StringContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#id.
    def enterId(self, ctx:CompiScriptLanguageParser.IdContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#id.
    def exitId(self, ctx:CompiScriptLanguageParser.IdContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#nestedExpression.
    def enterNestedExpression(self, ctx:CompiScriptLanguageParser.NestedExpressionContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#nestedExpression.
    def exitNestedExpression(self, ctx:CompiScriptLanguageParser.NestedExpressionContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#super.
    def enterSuper(self, ctx:CompiScriptLanguageParser.SuperContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#super.
    def exitSuper(self, ctx:CompiScriptLanguageParser.SuperContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#function.
    def enterFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#function.
    def exitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#parameters.
    def enterParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#parameters.
    def exitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#arguments.
    def enterArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#arguments.
    def exitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        pass



del CompiScriptLanguageParser