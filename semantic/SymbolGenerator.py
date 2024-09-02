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
