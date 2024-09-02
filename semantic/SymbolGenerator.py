import sys
import os
from antlr4 import *

from lexer_parser.CompiScriptLanguageVisitor import CompiScriptLanguageVisitor
from lexer_parser.CompiScriptLanguageParser import CompiScriptLanguageParser
from structures.Types.TypesClasses import *
from structures.Types.TypesTable import TypesTable
from structures.Symbols.SymbolsClasses import *
from structures.ContextManagement import *

class SymbolGenerator(CompiScriptLanguageVisitor):
    def __init__(self):
        super().__init__()  # Python 3 style super call
        self.context_manager = ContextManager()
        self.types_table = TypesTable()

        # Add basic types to the table
        self.types_table.add_type(NilType())
        self.types_table.add_type(IntType())
        self.types_table.add_type(DoubleType())
        self.types_table.add_type(BoolType())
        self.types_table.add_type(StringType())

    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        """
        Create the global context and visit the children nodes.
        """
        self.context_manager.enter_context("global")  # Start in global context
        result = self.visitChildren(ctx)
        self.context_manager.exit_context()  # Exit global context

        self.context_manager.current_context.symbol_table.print_table()

        return result
    
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
        """
        Handle the declaration of a variable.
        """
        var_name = ctx.IDENTIFIER().getText()
        
        # Create a new variable symbol
        symbol = Variable(name=var_name)

        # Define the symbol in the current context
        self.context_manager.define(symbol)

        # If the variable has an initializer, evaluate the expression and assign it
        if ctx.expression():
            value, type = self.visit(ctx.expression())
            self.context_manager.assign(var_name, value, type)

        return None


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
