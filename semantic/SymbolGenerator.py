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

    # Visit a parse tree produced by CompiScriptLanguageParser#nestedAssigment.
    def visitNestedAssigment(self, ctx:CompiScriptLanguageParser.NestedAssigmentContext):
        """
        Handle the assignment of a value to a variable.
        """
        if ctx.call():
            # If the `call` is present, visit the `call` to process it
            print("Assignment contains a call.")
            self.visit(ctx.call())
        else:

            # Handling simple variable assignment
            var_name = ctx.IDENTIFIER().getText()
            
            # Ensure the variable exists or create it
            if not self.context_manager.exists(var_name):
                raise NameError(f"Variable {var_name} is not defined.")

            # Evaluate the right-hand side first
            value, type = self.visit(ctx.assignment())
            # Assign the value to the current variable
            self.context_manager.assign(var_name, value, type)

        return value, type # Return the value for chained assignments


    # Visit a parse tree produced by CompiScriptLanguageParser#logicOrAssigment.
    def visitLogicOrAssigment(self, ctx:CompiScriptLanguageParser.LogicOrAssigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def visitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        """
        Visit the 'logic_or' rule.
        Ensures that all operands are boolean and handles 'or' logic.
        """
        left_value, left_type = self.visit(ctx.logic_and(0))

        for i in range(1, len(ctx.logic_and())):
            right_value, right_type = self.visit(ctx.logic_and(i))

            if left_type != BoolType() or right_type != BoolType():
                raise TypeError(f"Operands of 'or' must be boolean, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
  
            left_value, left_type = f"({left_value} {operator} {right_value})", BoolType()

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def visitLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        """
        Visit the 'logic_and' rule.
        Ensures that all operands are boolean and handles 'and' logic.
        """
        left_value, left_type = self.visit(ctx.equality(0))

        for i in range(1, len(ctx.equality())):
            right_value, right_type = self.visit(ctx.equality(i))

            if left_type != BoolType() or right_type != BoolType():
                raise TypeError(f"Operands of 'and' must be boolean, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
  
            left_value, left_type = f"({left_value} {operator} {right_value})", BoolType()

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#equality.
    def visitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        """
        Visit the 'equality' rule.
        Ensures that both sides of the equality are of the same type and handles '==' and '!=' operations.
        Return the boolean type and a placeholder value.
        """
        left_value, left_type = self.visit(ctx.comparison(0))

        for i in range(1, len(ctx.comparison())):
            right_value, right_type = self.visit(ctx.comparison(i))

            if left_type != right_type:
                raise TypeError(f"Operands of '==' or '!=' must be of the same type, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
  
            left_value, left_type = f"({left_value} {operator} {right_value})", BoolType()

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        """
        Visit the 'comparison' rule.
        Ensure that both sides of the comparison are numeric.
        Return the boolean type and a placeholder value.
        """
        left_value, left_type = self.visit(ctx.term(0))

        for i in range(1, len(ctx.term())):
            right_value, right_type = self.visit(ctx.term(i))

            if left_type not in (IntType(), DoubleType()) or right_type not in (IntType(), DoubleType()):
                raise TypeError(f"Operands of '>', '>=', '<' or '<=' can only be numeric types, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
  
            left_value, left_type = f"({left_value} {operator} {right_value})", BoolType()

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        """
        Visit the 'term' rule.
        Ensure that both sides of the term are numeric.
        Return the numeric type and a placeholder value.
        """
        left_value, left_type = self.visit(ctx.factor(0))
        j = 1 # Placeholder for the operator index
        for i in range(1, len(ctx.factor())):
            right_value, right_type = self.visit(ctx.factor(i))

            if left_type not in (IntType(), DoubleType()) or right_type not in (IntType(), DoubleType()):
                raise TypeError(f"Operands of '+' or '-' can only be numeric types, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
            
            # Widening the type if necessary
            type = DoubleType() if left_type == DoubleType() or right_type == DoubleType() else IntType()
                
            left_value, left_type = f"({left_value} {operator} {right_value})", type
            # update the operator index
            j += 2

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#factor.
    def visitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        """
        Visit the 'factor' rule.
        Ensure that both sides of the factor are numeric.
        Return the numeric type and a placeholder value.
        """
        left_value, left_type = self.visit(ctx.unary(0))
        j = 1 # Placeholder for the operator index
        for i in range(1, len(ctx.unary())):
            right_value, right_type = self.visit(ctx.unary(i))

            if left_type not in (IntType(), DoubleType()) or right_type not in (IntType(), DoubleType()):
                raise TypeError(f"Operands of '*', '/' or '%' can only be numeric types, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            if operator == '/':
                if right_value == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
            
            # Widening the type if necessary
            type = DoubleType() if left_type == DoubleType() or right_type == DoubleType() else IntType()
                
            left_value, left_type = f"({left_value} {operator} {right_value})", type
            
            # update the operator index
            j += 2

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedUnary.
    def visitNestedUnary(self, ctx:CompiScriptLanguageParser.NestedUnaryContext):
        """
        Visit the 'unary' rule.
        Ensures that the operand type is correct for the unary operation.
        Handles logical NOT and arithmetic negation.
        """

        # Check which operator is used
        if ctx.getChild(0).getText() == '!':
            # Logical NOT operation
            value, type = self.visit(ctx.unary())  # Recursively visit the nested unary expression

            # Type checking: ensure the operand is a boolean
            if type != BoolType():
                raise TypeError(f"Unary '!' operator can only be applied to a boolean type, not {type.__str__()}.")
            
            return f"(! {value})", type

        elif ctx.getChild(0).getText() == '-':
            # Negation operation
            value, type = self.visit(ctx.unary())  # Recursively visit the nested unary expression

            # Type checking: ensure the operand is a numeric type
            if type not in (IntType(), DoubleType()):
                raise TypeError(f"Unary '-' operator can only be applied to numeric types, not {type.__str__()}.")
            
            return f"(- {value})", type


    # Visit a parse tree produced by CompiScriptLanguageParser#callUnary.
    def visitCallUnary(self, ctx:CompiScriptLanguageParser.CallUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#true.
    def visitTrue(self, ctx:CompiScriptLanguageParser.TrueContext):
        """
        Return the bool type and a placeholder value.
        """
        return ctx.getChild(0).getText(), BoolType()


    # Visit a parse tree produced by CompiScriptLanguageParser#false.
    def visitFalse(self, ctx:CompiScriptLanguageParser.FalseContext):
        """
        Return the bool type and a placeholder value.
        """
        return ctx.getChild(0).getText(), BoolType()


    # Visit a parse tree produced by CompiScriptLanguageParser#nil.
    def visitNil(self, ctx:CompiScriptLanguageParser.NilContext):
        """
        Return the nil type and a placeholder value.
        """
        return ctx.getChild(0).getText(), NilType()


    # Visit a parse tree produced by CompiScriptLanguageParser#this.
    def visitThis(self, ctx:CompiScriptLanguageParser.ThisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#number.
    def visitNumber(self, ctx:CompiScriptLanguageParser.NumberContext):
        """
        Return the Double or Int type and a placeholder value.
        """
        if '.' in ctx.NUMBER().getText():
            return ctx.NUMBER().getText(), DoubleType()
        
        return ctx.NUMBER().getText(), IntType()

    # Visit a parse tree produced by CompiScriptLanguageParser#string.
    def visitString(self, ctx:CompiScriptLanguageParser.StringContext):
        """
        Return the String type and a placeholder value.
        """
        return ctx.STRING().getText(), StringType()


    # Visit a parse tree produced by CompiScriptLanguageParser#id.
    def visitId(self, ctx:CompiScriptLanguageParser.IdContext):
        """
        Check if the symbol exists in the current context and return its value and type.
        """
        if self.context_manager.exists(ctx.IDENTIFIER().getText()):
            symbol = self.context_manager.lookup(ctx.IDENTIFIER().getText())
        else:
            raise NameError(f"Symbol {ctx.IDENTIFIER().getText()} is not defined.")

        # Define the symbol in the current context
        if isinstance(symbol, Variable):
            return symbol.value, symbol.type


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedExpression.
    def visitNestedExpression(self, ctx:CompiScriptLanguageParser.NestedExpressionContext):
        """
        Visit the nested expression and return the value
        """
        return self.visit(ctx.expression())


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