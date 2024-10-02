
from antlr4 import *

from lexer_parser.CompiScriptLanguageVisitor import CompiScriptLanguageVisitor
from lexer_parser.CompiScriptLanguageParser import CompiScriptLanguageParser

from structures.Types.TypesClasses import *
from structures.Types.TypesTable import TypesTable

from structures.Symbols.SymbolsClasses import *
from structures.ContextManagement import *

from structures.ErrorManager import ErrorManager

class SymbolGenerator(CompiScriptLanguageVisitor):
    def __init__(self):
        super().__init__()  # Python 3 style super call
        self.context_manager = ContextManager()
        self.types_table = TypesTable()
        self.error_manager = ErrorManager()

        # Add basic types to the table
        self.types_table.add_type(NilType())
        self.types_table.add_type(IntType())
        self.types_table.add_type(DoubleType())
        self.types_table.add_type(BoolType())
        self.types_table.add_type(StringType())
        self.types_table.add_type(VoidType())
        self.types_table.add_type(AnyType())

        # Flag to handle nested assignments
        self.recursive_assign = False

        self.reserved_keywords = [
            "class", "else", "false", "for", "if", "null", "print", "return", "true", "var", "while"
        ]

    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        """
        Create the global context and visit the children nodes.
        """
        self.context_manager.enter_context("Main.global")  # Start in global context
        self.visitChildren(ctx)
        self.context_manager.exit_context()  # Exit global context

        # Print the symbol table for each context
        for context in self.context_manager.contexts.values():
            context.print_symbol_table()

        return self.context_manager

    # Visit a parse tree produced by CompiScriptLanguageParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CompiScriptLanguageParser.ClassDeclarationContext):
        """
        Handle the declaration of a class.
        """
        return self.visit(ctx.classDecl())


    # Visit a parse tree produced by CompiScriptLanguageParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:CompiScriptLanguageParser.FunctionDeclarationContext):
        """
        Handle the declaration of a function.
        """
        return self.visit(ctx.funDecl())


    # Visit a parse tree produced by CompiScriptLanguageParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CompiScriptLanguageParser.VariableDeclarationContext):
        """
        Handle the declaration of a variable.
        """
        return self.visit(ctx.varDecl())


    # Visit a parse tree produced by CompiScriptLanguageParser#statementDeclaration.
    def visitStatementDeclaration(self, ctx:CompiScriptLanguageParser.StatementDeclarationContext):
        """
        Visit a statement declaration.
        """
        return self.visit(ctx.statement())


    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx: CompiScriptLanguageParser.ClassDeclContext):
        """
        Handle the declaration of a class.
        """
        main_context = self.context_manager.get_context_name()
        
        class_name = ctx.IDENTIFIER(0).getText()
        superclass = None

        # Handle inheritance if specified
        if ctx.IDENTIFIER(1):
            superclass_name = ctx.IDENTIFIER(1).getText()
            superclass, _ = self.context_manager.lookup(superclass_name)
            if superclass.__class__ != ClassSymbol:
                self.error_manager.add_error(f"TypeError: {superclass_name} is not a class.")


        # Create a new class symbol
        self.types_table.add_type(ClassType(class_name))
        class_symbol = ClassSymbol(name=class_name, superclass=superclass)

        # Define the class symbol in the current context
        self.context_manager.define(class_symbol)

        # If the class has a superclass, enter its context
        if superclass:
            self.context_manager.enter_context(f"Class.{superclass_name}")

        # Create a new context for the class
        self.context_manager.create_context(f"Class.{class_name}", parent=self.context_manager.current_context)

        # Enter a new context for this class
        self.context_manager.enter_context(f"Class.{class_name}")

        # Visit all methods in the class
        for func in ctx.function():
            self.visit(func)

        # Exit the class context
        self.context_manager.exit_context()

        # Return to main context (global or block)
        if superclass:
            self.context_manager.enter_context(main_context)

        return None, VoidType()  # Return a placeholder value and type


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        """
        Handle the declaration of a function.
        """
        return self.visit(ctx.function())


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        """
        Handle the declaration of a variable.
        """
        if ctx.arrayAccess():
            # Handling array access
            array_name = ctx.arrayAccess().IDENTIFIER().getText()
            array_index, _ = self.visit(ctx.arrayAccess())

            if array_name in self.reserved_keywords:
                self.error_manager.add_error(f"Array variable name {array_name} is a reserved keyword.")

            symbol = ArraySymbol(name=array_name, size=array_index)

            # Define the symbol in the current context
            self.context_manager.define(symbol)

            if ctx.expression():
                value, type = self.visit(ctx.expression())
                self.context_manager.assign(array_name, value, type)

        else:
            var_name = ctx.IDENTIFIER().getText()

            if var_name in self.reserved_keywords:
                self.error_manager.add_error(f"Variable name {var_name} is a reserved keyword.")
            
            # Create a new variable symbol
            symbol = Variable(name=var_name)

            # Define the symbol in the current context
            self.context_manager.define(symbol)

            # If the variable has an initializer, evaluate the expression and assign it
            if ctx.expression():
                value, type = self.visit(ctx.expression())
                self.context_manager.assign(var_name, value, type)

        return None, VoidType()  # Return a placeholder value and type


    # Visit a parse tree produced by CompiScriptLanguageParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CompiScriptLanguageParser.ExpressionStatementContext):
        """
        Visit an expression statement.
        """
        return self.visit(ctx.exprStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#forStatement.
    def visitForStatement(self, ctx:CompiScriptLanguageParser.ForStatementContext):
        """
        Visit the 'for' statement.
        Handle initialization, condition checking, and iteration updates.
        Ensure that the condition is a boolean expression.
        Visit the loop body.
        """
        return self.visit(ctx.forStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:CompiScriptLanguageParser.IfStatementContext):
        """
        Visit the 'if' statement.
        """
        return self.visit(ctx.ifStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:CompiScriptLanguageParser.PrintStatementContext):
        """
        Visit the 'print' statement.
        """
        return self.visit(ctx.printStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStatement.
    def visitReturnStatement(self, ctx:CompiScriptLanguageParser.ReturnStatementContext):
        """
        Handle return statements within functions.
        Determine the return type dynamically based on the return expression.
        """
        return self.visit(ctx.returnStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:CompiScriptLanguageParser.WhileStatementContext):
        """
        Visit the 'while' statement.
        """
        return self.visit(ctx.whileStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#blockStatement.
    def visitBlockStatement(self, ctx:CompiScriptLanguageParser.BlockStatementContext):
        """
        Visit a block statement.
        Create a new context for the block, visit its children (statements),
        and then exit the context.
        """
        # Create a unique name for the block context
        block_name = f"Block.{id(ctx)}"
        
        # Create a new context with the current context as its parent
        self.context_manager.create_context(block_name, parent=self.context_manager.current_context)
        self.context_manager.enter_context(block_name)
        
        # Visit all the statements inside the block
        value, return_type = self.visit(ctx.block())
        
        # Exit the block context, returning to the parent context
        self.context_manager.exit_context()
        
        return value, return_type


    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        """
        Visit an expression statement.
        Evaluate the expression and return the value and type.
        """
        return self.visit(ctx.expression())


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        """
        Visit the 'for' statement.
        Handle initialization, condition checking, and iteration updates.
        Ensure that the condition is a boolean expression.
        Visit the loop body.
        """
        # Create a unique name for the block context
        for_name = f"For.{id(ctx)}"
        
        # Create a new context with the current context as its parent
        self.context_manager.create_context(for_name, parent=self.context_manager.current_context)
        self.context_manager.enter_context(for_name)

        # Handle the initializer (if any)
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            self.visit(ctx.exprStmt())

        # Evaluate the condition
        if ctx.expression(0): # Condition expression (first one)
            _, condition_type = self.visit(ctx.expression(0))
            if condition_type != BoolType():
                self.error_manager.add_error(f"For loop condition must be of boolean type, got {condition_type.__str__()} instead.")
        
        # Step 3: Visit the loop body (the statement after the parentheses)
        value, type = self.visit(ctx.statement())

        # Step 4: Visit the iteration (second expression, after the second semicolon)
        if ctx.expression(1):  # Update expression (second expression?)
            self.visit(ctx.expression(1))

        # Exit the for context
        self.context_manager.exit_context()

        return value, type  # Return a placeholder value and type


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        """
        Visit the 'if' statement.
        Ensure that the condition is a boolean expression.
        Visit the 'then' branch and the optional 'else' branch.
        """
        # Visit and evaluate the if condition
        _, condition_type = self.visit(ctx.expression())

        # Ensure the condition is of boolean type
        if condition_type != BoolType():
            self.error_manager.add_error(f"If condition must be of boolean type, got {condition_type.__str__()} instead.")

        if_name = f"If.{id(ctx)}"

        # Create a new context with the current context as its parent
        self.context_manager.create_context(if_name, parent=self.context_manager.current_context)
        self.context_manager.enter_context(if_name)

        # Visit the 'then' branch
        value, type = self.visit(ctx.statement(0))

        # Visit the 'else' branch if it exists
        if ctx.statement(1):
            self.visit(ctx.statement(1))
            value, type = "Any", AnyType()  # Placeholder

        # Exit the if context
        self.context_manager.exit_context()

        return value, type  # Return the value and type of the 'then' branch


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        """
        Visit the 'print' statement.
        Evaluate the expression to be printed, ensuring it's valid.
        """
        # Evaluate the expression that is to be printed
        value, type = self.visit(ctx.expression())

        print("Print statement:", value)
        
        return None, VoidType()  # Return a placeholder value and type

    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx: CompiScriptLanguageParser.ReturnStmtContext):
        """
        Handle return statements within functions.
        Determine the return type dynamically based on the return expression.
        """
        
        value, return_type = self.visit(ctx.expression()) if ctx.expression() else (None, VoidType())

        # Traverse the context stack to find the nearest function context
        function_symbol = None
        current_context = self.context_manager.current_context

        while current_context:
            # Look up the symbol associated with the current context
            symbol, _ = self.context_manager.lookup(current_context.name.split('.')[-1])
            if symbol.__class__ == Function:
                function_symbol = symbol
                break
            # Move up to the parent context
            current_context = current_context.parent

        # Check if a function context was found
        if function_symbol:
            # Update the return values of the function
            function_symbol.add_return_value((value, return_type))
        else:
            self.error_manager.add_error("Return statement found outside a function context.")

        return value, return_type

    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        """
        Visit the 'while' statement.
        Ensure that the condition is a boolean expression.
        Visit the loop body to check for semantic correctness.
        """
        # Visit and evaluate the loop condition
        _, condition_type = self.visit(ctx.expression())

        # Ensure the condition is of boolean type
        if condition_type != BoolType():
            self.error_manager.add_error(f"While loop condition must be of boolean type, got {condition_type.__str__()} instead.")

        while_name = f"While.{id(ctx)}"

        # Create a new context with the current context as its parent
        self.context_manager.create_context(while_name, parent=self.context_manager.current_context)
        self.context_manager.enter_context(while_name)

        # Visit the loop body
        value, type = self.visit(ctx.statement())

        # Exit the while context
        self.context_manager.exit_context()

        # In this semantic analysis phase, we don't execute the loop, so we don't loop or check if it will terminate.
        return value, type  # Return a placeholder value and type


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        """
        Visit a block of statements.
        Visit each declaration in the block and collect the return values.
        """
        # Visit each declaration and collect the return values
        for declaration in ctx.declaration():
            self.visit(declaration)

        # Update the current function's return type
        current_function = self.context_manager.get_context_name()
        function_symbol, _ = self.context_manager.lookup(current_function.split('.')[-1])

        if function_symbol.__class__ == Function:
            return_values = function_symbol.get_return_values()

            return_value, return_type = None, VoidType()  # Default return value and type

            # Update the return values of the function
            if len(return_values) > 1:
                # If there are multiple return values, ensure they are all the same type
                types = set([value[1] for value in return_values])
                
                if len(types) > 2 or (len(types) == 2 and AnyType() not in types):
                    self.error_manager.add_error(f"Block has multiple return types: {', '.join([t.__str__() for t in types])}.")
                
                for value in return_values:
                    if value[1] != AnyType():
                        return_value, return_type = "any", value[1]

            elif len(return_values) == 1:
                # If there is only one return value, set the function's return type
                return_value, return_type = return_values[0]

            function_symbol.set_return_type(return_type)
            return return_value, return_type
        else:
            return None, VoidType()  # Return a placeholder value and type


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitAssignmentExp(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        """
        Visit an assignment expression.
        """
        return self.visit(ctx.assignment())


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedAssignment.
    def visitNestedAssignment(self, ctx:CompiScriptLanguageParser.NestedAssignmentContext):
        """
        Handle the assignment of a value to a variable.
        """
        if ctx.call():
            # Handling method calls and member accesses
            value, type = self.visit(ctx.call())

            # Check if a member access is being assigned to
            if value == "this":
                context_name = self.context_manager.get_context_name().split('.')
                if context_name[0] != "Method":
                    self.error_manager.add_error(f"Cannot assign to 'this' outside of a method context.")
                    return None, VoidType()  # Return a placeholder value and type
                
                else:
                    field_name = ctx.IDENTIFIER().getText()

                    self.recursive_assign = True  # Set the recursive flag to handle chained assignments
                    value, type = self.visit(ctx.assignment())

                    # class name and method name
                    class_name = self.context_manager.get_context_name().split('.')[1]
                    method_name = self.context_manager.get_context_name().split('.')[2]
                    self.context_manager.exit_context()  # Exit the method context
                    
                    if context_name[2] == "init":
                        # Define the field in the instance context
                        field = Field(name=field_name, type=type, value=value)
                        self.context_manager.define(field)
                        
                    else:
                        # Assign the value to the field in the instance context
                        self.context_manager.assign(field_name, value, type)
                    
                    self.context_manager.enter_context(f"Method.{class_name}.{method_name}")  # Re-enter the method context

                    self.recursive_assign = False  # Reset the recursive flag

                    if self.recursive_assign:
                        return value, type  # Return the value for chained assignments
                    
            else:
                self.error_manager.add_error(f"Cannot assign to a method call or member access.")

        else:
            # Handling simple variable assignment
            var_name = ctx.IDENTIFIER().getText()
            
            # Ensure the variable exists in the current context
            if not self.context_manager.exists(var_name):
                self.error_manager.add_error(f"Variable {var_name} is not defined.")

            self.recursive_assign = True  # Set the recursive flag to handle chained assignments

            # Evaluate the right-hand side first
            value, type = self.visit(ctx.assignment())
            
            # Assign the value to the current variable
            self.context_manager.assign(var_name, value, type)

            self.recursive_assign = False  # Reset the recursive flag

            if self.recursive_assign:
                return value, type  # Return the value for chained assignments

        return None, VoidType() # Return a placeholder value and type


    # Visit a parse tree produced by CompiScriptLanguageParser#logicOrAssignment.
    def visitLogicOrAssignment(self, ctx:CompiScriptLanguageParser.LogicOrAssignmentContext):
        """
        Handle the assignment of a value to a variable.
        """
        return self.visit(ctx.logic_or())


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def visitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        """
        Visit the 'logic_or' rule.
        Ensures that all operands are boolean and handles 'or' logic.
        """
        left_value, left_type = self.visit(ctx.logic_and(0))

        for i in range(1, len(ctx.logic_and())):
            right_value, right_type = self.visit(ctx.logic_and(i))

            if left_type not in (BoolType(), AnyType()) or right_type not in (BoolType(), AnyType()):
                self.error_manager.add_error(f"Operands of 'or' must be boolean, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
  
            type = BoolType() if left_type == BoolType() and right_type == BoolType() else AnyType()
            left_value, left_type = f"({left_value} {operator} {right_value})", type

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

            if left_type not in (BoolType(), AnyType()) or right_type not in (BoolType(), AnyType()):
                self.error_manager.add_error(f"Operands of 'and' must be boolean, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            type = BoolType() if left_type == BoolType() and right_type == BoolType() else AnyType()
            left_value, left_type = f"({left_value} {operator} {right_value})", type

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
                self.error_manager.add_error(f"Operands of '==' or '!=' must be of the same type, not {left_type.__str__()} and {right_type.__str__()}.")
            
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

            if left_type not in (IntType(), DoubleType(), AnyType()) or right_type not in (IntType(), DoubleType(), AnyType()):
                self.error_manager.add_error(f"Operands of '>', '>=', '<' or '<=' can only be numeric types, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()
  
            left_value, left_type = f"({left_value} {operator} {right_value})", BoolType()

        return left_value, left_type


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        """
        Visit the 'term' rule.
        Ensure that both sides of the term are numeric or strings.
        Return the numeric or string type and a placeholder value.
        """
        left_value, left_type = self.visit(ctx.factor(0))
        
        for i in range(1, len(ctx.factor())):
            right_value, right_type = self.visit(ctx.factor(i))
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            if operator == '+':
                if left_type not in (IntType(), DoubleType(), AnyType()) or right_type not in (IntType(), DoubleType(), AnyType()):
                    if left_type != StringType() and right_type != StringType():
                        self.error_manager.add_error(f"Operands of '+' must be numeric or one of them must be a string, not {left_type.__str__()} and {right_type.__str__()}.")       

            if operator == '-' and (left_type not in (IntType(), DoubleType(), AnyType()) or right_type not in (IntType(), DoubleType(), AnyType())):
                self.error_manager.add_error(f"Operands of '-' must be numeric types, not {left_type.__str__()} and {right_type.__str__()}.")
            
            
            # Check if both operands are strings for concatenation
            if operator == '+' and left_type == StringType() or right_type == StringType():
                # Implementación corregida
                left_value = str(left_value).strip('"') + str(right_value).strip('"')
                left_type = StringType()
            else:
                # Widening the type if necessary
                type = DoubleType() if left_type == DoubleType() or right_type == DoubleType() else IntType()
                type = AnyType() if left_type == AnyType() or right_type == AnyType() else type

                left_value, left_type = f"({left_value} {operator} {right_value})", type
            
        return left_value, left_type
    
    # Visit a parse tree produced by CompiScriptLanguageParser#id.
    def visitId(self, ctx:CompiScriptLanguageParser.IdContext):
        """
        Check if the symbol exists in the current context and return its value and type.
        """
        if not self.context_manager.exists(ctx.IDENTIFIER().getText()):
            self.error_manager.add_error(f"Symbol {ctx.IDENTIFIER().getText()} is not defined.")
        
        symbol, _ = self.context_manager.lookup(ctx.IDENTIFIER().getText())

        # Check if the symbol is a variable
        if symbol.__class__ == Variable or symbol.__class__ == Parameter:
            return symbol.value, symbol.type
        # Check if the symbol is a function
        elif symbol.__class__ == Function:
            return symbol.name, symbol.type

    # Visit a parse tree produced by CompiScriptLanguageParser#factor.
    def visitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        """
        Visit the 'factor' rule.
        Ensure that both sides of the factor are numeric.
        Return the numeric type and a placeholder value.
        """
        left_value, left_type = self.visit(ctx.unary(0))

        for i in range(1, len(ctx.unary())):
            right_value, right_type = self.visit(ctx.unary(i))

            if left_type not in (IntType(), DoubleType(), AnyType()) or right_type not in (IntType(), DoubleType(), AnyType()):
                self.error_manager.add_error(f"Operands of '*', '/' or '%' can only be numeric types, not {left_type.__str__()} and {right_type.__str__()}.")
            
            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            if operator == '/':
                if right_value == 0:
                    self.error_manager.add_error("Division by zero is not allowed")
            
            # Widening the type if necessary
            type = DoubleType() if left_type == DoubleType() or right_type == DoubleType() else IntType()
            type = AnyType() if left_type == AnyType() or right_type == AnyType() else type
                
            left_value, left_type = f"({left_value} {operator} {right_value})", type

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
            if type not in (BoolType(), AnyType()):
                self.error_manager.add_error(f"Unary '!' operator can only be applied to a boolean type, not {type.__str__()}.")
            
            return f"(! {value})", type

        elif ctx.getChild(0).getText() == '-':
            # Negation operation
            value, type = self.visit(ctx.unary())  # Recursively visit the nested unary expression

            # Type checking: ensure the operand is a numeric type
            if type not in (IntType(), DoubleType(), AnyType()):
                self.error_manager.add_error(f"Unary '-' operator can only be applied to numeric types, not {type.__str__()}.")
            
            return f"(- {value})", type


    # Visit a parse tree produced by CompiScriptLanguageParser#callUnary.
    def visitCallUnary(self, ctx:CompiScriptLanguageParser.CallUnaryContext):
        """
        Handle function calls and member accesses.
        """
        return self.visit(ctx.call())


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitPrimaryCall(self, ctx: CompiScriptLanguageParser.CallContext):
        """
        Handle function with id calls, method calls, and member accesses.
        """
        main_context = self.context_manager.get_context_name()

        # Start by visiting the primary expression
        primary_value, primary_type = self.visit(ctx.primary())

        # Handle chained calls or member accesses
        i = 1
        while i < len(list(ctx.getChildren())):
            # Check if this is a function call ( '(' arguments? ')' )
            if ctx.getChild(i).getText() == '(':
                func_name = primary_value
                function_symbol, _ = self.context_manager.lookup(func_name)

                if function_symbol.__class__ != Function:
                    self.error_manager.add_error(f"{func_name} is not a function.")
                    return None, VoidType()

                # Evaluate the arguments
                arguments = self.visit(ctx.getChild(i + 1)) if ctx.arguments() else []
                i = i + 3 if ctx.arguments() else i + 2  # Skip the arguments and the closing parenthesis

                # Check if the number of arguments matches the function's parameters
                if len(arguments) != len(function_symbol.get_parameters()):
                    self.error_manager.add_error(f"Function {func_name} expected {len(function_symbol.get_parameters())} arguments, got {len(arguments)}.")

                # Check for recursive calls
                if self.context_manager.check_recursive_context(f"Function.{func_name}"):
                    # Check if the arguments match the function's parameters
                    for arg, param in zip(arguments, function_symbol.get_parameters()):
                        if arg[1] != param.type:
                            self.error_manager.add_error(f"Recursive function {func_name} expected argument of type {param.type.__str__()}, got {arg[1].__str__()}.")

                    return "any", AnyType()  # Return a placeholder value and type

                # Capture the current context for closure purposes
                self.context_manager.capture_context_for(f"Function.{func_name}")

                # Enter a new context for the function call
                self.context_manager.enter_context(f"Function.{func_name}")

                # Simulate the function execution by assigning arguments to parameters
                for arg, param in zip(arguments, function_symbol.get_parameters()):
                    self.context_manager.assign(param.name, arg[0], arg[1])

                # Visit the function body (block) in this new context
                value, return_type = self.visit(function_symbol.get_block())

                # Exit the function call context
                self.context_manager.exit_context()

                # Update the primary_value and primary_type to reflect the function's return
                primary_value, primary_type = value, return_type

            # Check if this is a member access ( '.' IDENTIFIER )
            elif ctx.getChild(i).getText() == '.':
                member_name = ctx.getChild(i + 1).getText() # Get the member name

                if primary_value.__class__ == Instance:
                    self.context_manager.enter_context(primary_value.name)  # Enter the instance context

                    # Check for attribute (field) access
                    field_symbol = self.context_manager.lookup(member_name)[0]

                    if field_symbol.__class__ == Field:
                        primary_value, primary_type = field_symbol.value, field_symbol.type
                        i = i + 2  # Skip the dot and the member name
                    else:
                        class_name = primary_value.class_symbol.name
                        method_symbol = self.context_manager.lookup(f"{class_name}.{member_name}")[0]
                        if method_symbol.__class__ == Method:
                            # Evaluate the arguments
                            arguments = self.visit(ctx.getChild(i + 3)) if ctx.arguments() else []
                            i = i + 5 if ctx.arguments() else i + 4  # Skip the arguments and the closing parenthesis

                            parameters = method_symbol.get_parameters()[1:] # Skip the 'this' parameter

                            # Check if the number of arguments matches the function's parameters
                            if len(arguments) != len(parameters): 
                                self.error_manager.add_error(f"Method {member_name} expected {len(parameters)} arguments, got {len(arguments)}.")

                            # Check for recursive calls
                            if self.context_manager.check_recursive_context(f"Method.{class_name}.{member_name}"):
                                # Check if the arguments match the function's parameters
                                for arg, param in zip(arguments, parameters):
                                    if arg[1] != param.type:
                                        self.error_manager.add_error(f"Recursive method {member_name} expected argument of type {param.type.__str__()}, got {arg[1].__str__()}.")

                                return "any", AnyType()  # Return a placeholder value and type

                            # Capture the current context for closure purposes
                            self.context_manager.capture_context_for(f"Method.{class_name}.{member_name}")

                            # Enter a new context for the method call
                            self.context_manager.enter_context(f"Method.{class_name}.{member_name}")

                            # Simulate the function execution by assigning arguments to parameters
                            for arg, param in zip(arguments, parameters):
                                self.context_manager.assign(param.name, arg[0], arg[1])

                            # Visit the function body (block) in this new context
                            value, return_type = self.visit(method_symbol.get_block())

                            # Exit the function call context
                            self.context_manager.exit_context()

                            # Update the primary_value and primary_type to reflect the function's return
                            primary_value, primary_type = value, return_type
                        else:
                            self.error_manager.add_error(f"'{member_name}' not found in class {primary_value.class_symbol.name}.")
                            return None, VoidType()
                        
                    self.context_manager.exit_context()  # Exit the instance context
                    self.context_manager.enter_context(main_context)  # Return to the main context
                
                elif primary_value == "this":
                    # Check for attribute (field) access
                    field_symbol = self.context_manager.lookup(member_name)[0]

                    if field_symbol.__class__ == Field:
                        # field value and type
                        primary_value, primary_type = field_symbol.value, field_symbol.type
                        i = i + 2
                    else:
                        self.error_manager.add_error(f"'{member_name}' not found in class {self.context_manager.get_context_name().split('.')[1]}.")
                        return None, VoidType()
                    
                elif primary_value == "super":
                    return None, VoidType()

        return primary_value, primary_type


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
        """
        Return the class type and a placeholder value.
        """
        return ctx.getChild(0).getText(), AnyType()


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



    # Visit a parse tree produced by CompiScriptLanguageParser#nestedExpression.
    def visitNestedExpression(self, ctx:CompiScriptLanguageParser.NestedExpressionContext):
        """
        Visit the nested expression and return the value
        """
        return self.visit(ctx.expression())


    # Visit a parse tree produced by CompiScriptLanguageParser#super.
    def visitSuper(self, ctx:CompiScriptLanguageParser.SuperContext):
        """
        Handle the 'super' keyword.
        """ 
        return ctx.getChild(0).getText(), AnyType()


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        """
        Handle function declaration.
        """
        func_name = ctx.IDENTIFIER().getText()

        # Check if the function is a method and set the function name accordingly
        prefix, name = self.context_manager.get_context_name().split('.')
        if prefix == "Class":
            func_name = f"{name}.{func_name}"
        
        # Create a new function symbol
        # If the function is a method, create a Method symbol; otherwise, create a Function symbol
        function_symbol = Method(name=func_name) if prefix == "Class" else Function(name=func_name)

        # Enter a new context for the function
        context_name = f"Method.{func_name}" if prefix == "Class" else f"Function.{func_name}"
        function_context = self.context_manager.create_context(context_name)
        
        if prefix == "Class":
            class_type = self.types_table.get_type(name)
            this_parameter = Parameter(name="this", type=class_type)
            function_symbol.add_parameter(this_parameter)  # Add the 'this' parameter to the method
            function_context.define(this_parameter)

        # Handle parameters
        if ctx.parameters():
            for i in range(len(ctx.parameters().IDENTIFIER())):
                param_name = ctx.parameters().IDENTIFIER(i).getText()
                parameter_symbol = Parameter(name=param_name)  # Initially, parameter type is NilType
                function_symbol.add_parameter(parameter_symbol)
                function_context.define(parameter_symbol)

        # Set the block of the function
        function_symbol.set_block(ctx.block())
        
        # Add the function to the symbol table in the current context
        self.context_manager.define(function_symbol)
        
        # Verify if the function is a method and add it to the class symbol
        class_symbol, _ = self.context_manager.lookup(name) if prefix == "Class" else (None, None)
        
        # Add the method to the class symbol
        if class_symbol is not None:
            class_symbol.add_method(function_symbol)

        return None, VoidType()


    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        """
        Return the parameters of a function.
        """
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        """
        Handle function arguments.
        """
        arguments = []
        for i in range(len(ctx.expression())):
            arguments.append(self.visit(ctx.expression(i)))

        return arguments
    
    # Visit a parse tree produced by CompiScriptLanguageParser#newInstance.
    def visitNewInstance(self, ctx:CompiScriptLanguageParser.NewInstanceContext):
        """
        Handle the creation of a new instance of a class.
        """
        return self.visit(ctx.newExpression())

    # Visit a parse tree produced by CompiScriptLanguageParser#newExpression.
    def visitNewExpression(self, ctx:CompiScriptLanguageParser.NewExpressionContext):
        """
        Handle the creation of a new instance of a class.
        """
        main_context = self.context_manager.get_context_name()

        class_name = ctx.IDENTIFIER().getText()
        class_symbol, _ = self.context_manager.lookup(class_name)

        if class_symbol.__class__ != ClassSymbol:
            self.error_manager.add_error(f"{class_name} is not a class.")
        
        # Handle constructor (init) if exists
        constructor = class_symbol.lookup_method(f"{class_name}.init")
        
        if constructor:
            class_type = self.types_table.get_type(class_name)
            instance = Instance(f"Instance.{class_name}.{id(ctx)}",class_symbol, class_type)

            self.context_manager.define(instance) # Define the instance in the current context
            self.context_manager.enter_context(f"Class.{class_name}") # Enter the class context

            # Create a new context for instance creation
            self.context_manager.create_context(f"Instance.{class_name}.{id(ctx)}", parent=self.context_manager.current_context)

            # Enter a new context for the instance creation
            self.context_manager.enter_context(f"Instance.{class_name}.{id(ctx)}")

            # Capture the current context for closure purposes
            self.context_manager.capture_context_for(f"Method.{class_name}.init")
            self.context_manager.enter_context(f"Method.{class_name}.init")

            # Evaluate the arguments
            arguments = self.visit(ctx.arguments()) if ctx.arguments() else []

            parameters = constructor.get_parameters()[1:]  # Skip the 'this' parameter

            if len(arguments) != len(parameters):
                self.error_manager.add_error(f"Constructor expected {len(parameters)} arguments, got {len(arguments)}.")

            # Simulate the function execution by assigning arguments to parameters
            for arg, param in zip(arguments, parameters):
                self.context_manager.assign(param.name, arg[0], arg[1])

            # Visit the function body (block) in this new context
            self.visit(constructor.get_block())

            self.context_manager.exit_context()  # Exit the constructor call context
            self.context_manager.enter_context(main_context) # Enter the main context

        else:
            self.error_manager.add_error(f"Class {class_name} does not have a constructor.")

        return instance, class_type
    
    # Visit a parse tree produced by CompiScriptLanguageParser#funAnonExp.
    def visitFunAnonExp(self, ctx: CompiScriptLanguageParser.FunAnonExpContext):
        """
        Handle the declaration of an anonymous function.
        """
        return self.visit(ctx.funAnon())
    
    # Visit a parse tree produced by CompiScriptLanguageParser#funAnonCall
    def visitFunAnonCall(self, ctx:CompiScriptLanguageParser.FunAnonCallContext):
        """
        Handle the call of an anonymous function.
        """
        return self.visit(ctx.funAnon())
    
    # Visit a parse tree produced by CompiScriptLanguageParser#funAnon.
    def visitFunAnon(self, ctx:CompiScriptLanguageParser.FunAnonContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by CompiScriptLanguageParser#newArray.
    def visitNewArray(self, ctx:CompiScriptLanguageParser.NewArrayContext):
        """
        Handle the creation of a new array.
        """
        return self.visit(ctx.array())
    
    # Visit a parse tree produced by CompiScriptLanguageParser#array.
    def visitArray(self, ctx:CompiScriptLanguageParser.ArrayContext):
        """
        Handle the creation of an array.
        """
        # Check if all elements are of the same type
        all_same_type = True
        array_type = None
        values = []

        for i in range(len(ctx.expression())):
            value, type = self.visit(ctx.expression(i))
            values.append(value) # Add the value to the list
            if array_type is None:
                array_type = type
            elif array_type != type:
                all_same_type = False

        if all_same_type:
            return values, ArrayType("Array", array_type)
        else:
            self.error_manager.add_error("Array elements must be of the same type.")

        return None, VoidType() # Return a placeholder value and type
    
    # Visit a parse tree produced by CompiScriptLanguageParser#arrayAssignment.
    def visitArrayAssignment(self, ctx:CompiScriptLanguageParser.ArrayAssignmentContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by CompiScriptLanguageParser#arrayAccess.
    def visitArrayAccess(self, ctx:CompiScriptLanguageParser.ArrayAccessContext):
        """
        Handle the access of an array element or size.
        """
        return int(ctx.NUMBER().getText()), IntType()
    
    # Visit a parse tree produced by CompiScriptLanguageParser#primaryArrayAccess.
    def visitPrimaryArrayAccess(self, ctx:CompiScriptLanguageParser.PrimaryArrayAccessContext):
        return self.visitChildren(ctx)