
from antlr4 import *

from lexer_parser.CompiScriptLanguageVisitor import CompiScriptLanguageVisitor
from lexer_parser.CompiScriptLanguageParser import CompiScriptLanguageParser

from structures.Types.TypesClasses import *
from structures.Types.TypesTable import TypesTable

from structures.Symbols.SymbolsClasses import *
from structures.ContextManagement import *

from ir.IRManagement import IRManager

class TacGenerator(CompiScriptLanguageVisitor):
    def __init__(self, context_manager: ContextManager):
        super().__init__()  # Python 3 style super call
        self.ir_manager = IRManager()
        self.context_manager = context_manager
        
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        """
        Visit the program node and emit TAC for the operations.
        """
        self.context_manager.enter_context("Main.global")  # Start in global context
        self.visitChildren(ctx)
        self.context_manager.exit_context()  # Exit global context
        
        # Return self.code_generator.get_code()
        print(self.ir_manager.get_code())

        # Write the TAC to a file
        with open("output.tac", "w") as tac_file:
            tac_file.write(self.ir_manager.get_code())

    # Visit a parse tree produced by CompiScriptLanguageParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CompiScriptLanguageParser.ClassDeclarationContext):
        """
        Visit the class declaration
        """
        return self.visit(ctx.classDecl())

    # Visit a parse tree produced by CompiScriptLanguageParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:CompiScriptLanguageParser.FunctionDeclarationContext):
        """
        Visit the function declaration node and emit TAC for the operations.
        """
        self.visit(ctx.funDecl())


    # Visit a parse tree produced by CompiScriptLanguageParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CompiScriptLanguageParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#statementDeclaration.
    def visitStatementDeclaration(self, ctx:CompiScriptLanguageParser.StatementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        """
        Visit the class declaration for the class node and emit TAC for the operations.
        """
        main_context = self.context_manager.get_context_name()

        class_name = ctx.IDENTIFIER(0).getText()
        superclass = None

        if ctx.IDENTIFIER(1):
            superclass_name = ctx.IDENTIFIER(1).getText()
            self.context_manager.enter_context(f"Class.{superclass_name}")

        self.context_manager.enter_context(f"Class.{class_name}")  # Enter a new context for the class

        # Visit the methos in the class
        for func in ctx.function():
            self.visit(func)
        
        self.context_manager.exit_context()  # Exit the context for the class

        if superclass:
            self.context_manager.enter_context(main_context) # Return to the main context


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx: CompiScriptLanguageParser.VarDeclContext):
        """
        Visit the variable declaration node and emit TAC for the operations.
        """
        
        # Check if this variable is an array declaration
        if ctx.arrayAccess():  # This checks for array access
            var_name = ctx.arrayAccess().IDENTIFIER().getText()
            array_size = int(ctx.arrayAccess().NUMBER().getText())  # Get the array size
            self.ir_manager.emit(f"\t{var_name} = alloc {array_size * 4}\n")  # Emit TAC for array allocation (4 bytes per element assumed)
        else:
            var_name = ctx.IDENTIFIER().getText()

            if self.context_manager.get_context_name()== "Main.global" or self.context_manager.get_context_name().split(".")[1] == "main":
                self.ir_manager.emit(f"\tdata {var_name}\n")

            # Handle regular variable declaration and assignment
            if ctx.expression():
                value = self.visit(ctx.expression())  # Visit and evaluate the expression on the right-hand side
                self.ir_manager.emit(f"\t{var_name} = {value} ;\n")  # Emit TAC for the assignment
        
        return var_name

    # Visit a parse tree produced by CompiScriptLanguageParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CompiScriptLanguageParser.ExpressionStatementContext):
        """
        Visit the expression statement node and emit TAC for the operations.
        """
        return self.visit(ctx.exprStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#forStatement.
    def visitForStatement(self, ctx:CompiScriptLanguageParser.ForStatementContext):
        """
        Visit the 'for' statement node and emit TAC for the operations.
        """
        self.visit(ctx.forStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:CompiScriptLanguageParser.IfStatementContext):
        """
        Visit the 'if' statement node and emit TAC for the operations.
        """
        return self.visit(ctx.ifStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:CompiScriptLanguageParser.PrintStatementContext):
        """
        Visit the 'print' statement node and emit TAC for the operations.
        """
        return self.visit(ctx.printStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStatement.
    def visitReturnStatement(self, ctx:CompiScriptLanguageParser.ReturnStatementContext):
        """
        Visit the 'return' statement node and emit TAC for the operations.
        """
        return self.visit(ctx.returnStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:CompiScriptLanguageParser.WhileStatementContext):
        """
        Visit the 'while' statement node and emit TAC for the operations.
        """
        return self.visit(ctx.whileStmt())


    # Visit a parse tree produced by CompiScriptLanguageParser#blockStatement.
    def visitBlockStatement(self, ctx:CompiScriptLanguageParser.BlockStatementContext):
        """
        Visit the block statement node and emit TAC for the operations.
        """
        self.context_manager.enter_context(f"Block.{id(ctx)}")  # Enter a new context for the block
        self.visit(ctx.block())  # Visit the block

        self.context_manager.exit_context()  # Exit the context for the block


    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        """
        Visit the 'for' statement node and emit TAC for the operations.
        """

        if ctx.varDecl():
            self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            self.visit(ctx.exprStmt())

        # Late enter of the context for the 'for' statement
        self.context_manager.enter_context(f"For.{id(ctx)}")  # Enter a new context for the 'for' statement

        start_label = self.ir_manager.new_label()
        body_label = self.ir_manager.new_label()
        next_label = self.ir_manager.new_label()

        self.context_manager.define(LabelSymbol("Label.start", VoidType(), start_label))
        self.context_manager.define(LabelSymbol("Label.body", VoidType(), body_label))
        self.context_manager.define(LabelSymbol("Label.end", VoidType(), next_label))

        # Emit the start label
        self.ir_manager.emit(f"\n\t{start_label}:\n")

        if ctx.expression(0):
            self.visit(ctx.expression(0))  # Visit the condition

        # Emit the code for the 'body' part
        self.ir_manager.emit(f"\n\t{body_label}:\n")
        self.visit(ctx.statement())

        # Early exit of the context for the 'For' statement
        self.context_manager.exit_context()

        # Emit the increment, if it exists
        if ctx.expression(1):
            self.visit(ctx.expression(1))  # Visit the increment

        # Emit goto to the start label
        self.ir_manager.emit(f"\tgoto {start_label}\n")

        # Emit the next label
        self.ir_manager.emit(f"\n\t{next_label}:\n")


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx: CompiScriptLanguageParser.IfStmtContext):
        """
        Visit the 'if' statement node and emit TAC for the operations.
        """
        self.context_manager.enter_context(f"If.{id(ctx)}")  # Enter a new context for the 'if' statement

        true_label = self.ir_manager.new_label()
        next_label = self.ir_manager.new_label()

        self.context_manager.define(LabelSymbol("Label.true", VoidType(), true_label))
        self.context_manager.define(LabelSymbol(f"Label.end", VoidType(), next_label))

        if ctx.statement(1):
            false_label = self.ir_manager.new_label()
            self.context_manager.define(LabelSymbol("Label.false", VoidType(), false_label))

        # Evaluate the boolean condition, passing the true/false labels for short-circuiting
        self.visit(ctx.expression())

        # Emit the code for the 'then' part
        self.ir_manager.emit(f"\n\t{true_label}:\n")
        self.visit(ctx.statement(0))  # Visit the 'then' branch

        # Emit the code for the 'else' part, if it exists
        if ctx.statement(1):
            self.ir_manager.emit(f"\tgoto {next_label}\n")
            self.ir_manager.emit(f"\n\t{false_label}:\n")
            self.visit(ctx.statement(1))  # Visit the 'else' branch

        # Emit the next label
        self.ir_manager.emit(f"\n\t{next_label}:\n")

        # Exit the context for the 'if' statement
        self.context_manager.exit_context()


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        """
        Visit the 'print' statement node and emit TAC for the operations.
        """
        arg = self.visit(ctx.expression())  # Visit the expression
        self.ir_manager.emit(f"\tLCall print {arg} ;\n")

        return None


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        """
        Visit the 'return' statement node and emit TAC for the operations.
        """
        if ctx.expression():
            return_value = self.visit(ctx.expression())  # Visit the return value

            # Emit TAC for the return statement
            self.ir_manager.emit(f"\treturn {return_value}\n")

    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        """
        Visit the 'while' statement node and emit TAC for the operations.
        """
        self.context_manager.enter_context(f"While.{id(ctx)}")  # Enter a new context for the 'if' statement

        start_label = self.ir_manager.new_label()
        body_label = self.ir_manager.new_label()
        next_label = self.ir_manager.new_label()

        self.context_manager.define(LabelSymbol("Label.start", VoidType(), start_label))
        self.context_manager.define(LabelSymbol("Label.body", VoidType(), body_label))
        self.context_manager.define(LabelSymbol(f"Label.end", VoidType(), next_label))

        # Emit the start label
        self.ir_manager.emit(f"\n\t{start_label}:\n")

        self.visit(ctx.expression())  # Visit the condition

        # Emit the code for the 'body' part
        self.ir_manager.emit(f"\n\t{body_label}:\n")
        self.visit(ctx.statement())

        # Emit goto to the start label
        self.ir_manager.emit(f"\tgoto {start_label}\n")

        # Emit the next label
        self.ir_manager.emit(f"\n\t{next_label}:\n")

        # Exit the context for the 'while' statement
        self.context_manager.exit_context()

    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        """
        Visit the block node and emit TAC for the operations.
        """
        for declaration in ctx.declaration():
            self.visit(declaration)


    # Visit a parse tree produced by CompiScriptLanguageParser#assignmentExp.
    def visitAssignmentExp(self, ctx:CompiScriptLanguageParser.AssignmentExpContext):
        """
        Visit the assignment node and emit TAC for the operations.
        """
        return self.visit(ctx.assignment())


    # Visit a parse tree produced by CompiScriptLanguageParser#funAnonExp.
    def visitFunAnonExp(self, ctx:CompiScriptLanguageParser.FunAnonExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#funAnon.
    def visitFunAnon(self, ctx:CompiScriptLanguageParser.FunAnonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedAssignment.
    def visitNestedAssignment(self, ctx:CompiScriptLanguageParser.NestedAssignmentContext):
        """
        Visit the assignment node and emit TAC for the operations.
        """
        if ctx.call():
            # Handling method calls and member accesses
            value = self.visit(ctx.call())

            if value == "this":
                field_name = ctx.IDENTIFIER().getText()
                value = self.visit(ctx.assignment())

                parameters = list(self.context_manager.get_symbol_table().items())

                for i in range(len(parameters)):
                    temp_size = self.ir_manager.create_temp("4") # Size of

                    # Check if the field exists in the parameters
                    if parameters[i][0] == field_name and parameters[i][1].__class__ == Parameter:

                        # Compute the offset for the index
                        temp_index = self.ir_manager.create_temp(str(i))

                        temp_offset = self.ir_manager.create_temp(f"{temp_index} * {temp_size}")  # Offset = index * 4

                        # Calculate the address of arr[index]
                        tem_pointer = self.ir_manager.create_temp(f"this + {temp_offset}")  # Pointer to arr[index]
                        temp_address = self.ir_manager.create_temp(f"*({tem_pointer})") # Dereference the pointer

                        # Emit TAC for assignment
                        temp_value = self.ir_manager.create_temp(value)
                        self.ir_manager.emit(f"\t{temp_address} = {temp_value} ;\n")
        else:
            var_name = ctx.IDENTIFIER().getText()
            value = self.visit(ctx.assignment())  # Visit the assignment on the right-hand side

            # Emit TAC for assignment
            self.ir_manager.emit(f"\t{var_name} = {value} ;\n")
            return var_name


    # Visit a parse tree produced by CompiScriptLanguageParser#logicOrAssignment.
    def visitLogicOrAssignment(self, ctx:CompiScriptLanguageParser.LogicOrAssignmentContext):
        """
        Visit the 'or' assignment node and emit TAC for the operations.
        """
        return self.visit(ctx.logic_or())


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def visitLogic_or(self, ctx: CompiScriptLanguageParser.Logic_orContext):
        """
        Generalized short-circuiting for logical 'or' expressions.
        Works in both control-flow contexts and non-control-flow contexts.
        """
        context_name = self.context_manager.get_context_name().split(".")[0]

        # Evaluate the left operand
        left = self.visit(ctx.logic_and(0))

        # Check if the context is an 'if' statement and there are more than one 'or' operands
        if context_name == "If":
            # Retrieve the true and false labels from the context
            true_label = self.context_manager.label_lookup("Label.true").value
            false_label = self.context_manager.label_lookup("Label.false")

            # If false_label is None, set it to the end label
            false_label = false_label.value if false_label is not None else self.context_manager.label_lookup("Label.end").value
            
            if len(ctx.logic_and()) > 1:
                # Emit short-circuit check for the left operand
                self.ir_manager.emit(f"\n\tif {left} goto {true_label}\n")
            else:
                # Emit short-circuit check for the left operand
                self.ir_manager.emit(f"\n\tifFalse {left} goto {false_label}\n")
        elif context_name == "While" or context_name == "For":
            # Retrieve the start and next labels from the context
            body_label = self.context_manager.label_lookup("Label.body").value
            next_label = self.context_manager.label_lookup(f"Label.end").value

            if len(ctx.logic_and()) > 1:
                # Emit short-circuit check for the left operand
                self.ir_manager.emit(f"\n\tif {left} goto {body_label}\n")
            else:
                # Emit short-circuit check for the left operand
                self.ir_manager.emit(f"\n\tifFalse {left} goto {next_label}\n")

        # Evaluate the right operand if the left is false
        for i in range(1, len(ctx.logic_and())):
            right = self.visit(ctx.logic_and(i))

            operator = ctx.getChild(2 * i - 1).getText()
            # Form the expression string
            expr_str = f"{left} {operator} {right}"
            left = self.ir_manager.create_temp(expr_str)

            self.ir_manager.emit(f"\n\tif {right} goto {true_label}\n")

            # Check if this is the last operand
            if (i+1)==len(ctx.logic_and()):
                if context_name == "If":
                    false_label = self.context_manager.label_lookup("Label.false")

                    # If false_label is None, set it to the end label
                    false_label = false_label.value if false_label is not None else self.context_manager.label_lookup("Label.end").value

                    # If all conditions are false, go to the false label
                    self.ir_manager.emit(f"\tgoto {false_label}")
                elif context_name == "While" or context_name == "For":
                    next_label = self.context_manager.label_lookup(f"Label.end").value

                    # If all conditions are false, go to the next label
                    self.ir_manager.emit(f"\tgoto {next_label}")

        return left


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def visitLogic_and(self, ctx: CompiScriptLanguageParser.Logic_andContext):
        """
        Generalized short-circuiting for logical 'and' expressions.
        Works in both control-flow contexts and non-control-flow contexts.
        """
        context_name = self.context_manager.get_context_name().split(".")[0]

        # Evaluate the left operand
        left = self.visit(ctx.equality(0))

        # Check if the context is an 'if' statement and there are more than one 'and' operands
        if context_name == "If" and len(ctx.equality()) > 1:
            # Retrieve the true and false labels from the context
            false_label = self.context_manager.label_lookup("Label.false")

            # If false_label is None, set it to the end label
            false_label = false_label.value if false_label is not None else self.context_manager.label_lookup("Label.end").value

            # Emit short-circuit check for the left operand
            self.ir_manager.emit(f"\n\tifFalse {left} goto {false_label}\n")

        elif (context_name == "While" or context_name == "For") and len(ctx.equality()) > 1:
            # Retrieve the start and next labels from the context
            next_label = self.context_manager.label_lookup(f"Label.end").value

            # Emit short-circuit check for the left operand
            self.ir_manager.emit(f"\n\tifFalse {left} goto {next_label}\n")

        # Evaluate the right operand if the left is true
        for i in range(1, len(ctx.equality())):
            right = self.visit(ctx.equality(i))

            operator = ctx.getChild(2 * i - 1).getText()
            # Form the expression string
            expr_str = f"{left} {operator} {right}"
            left = self.ir_manager.create_temp(expr_str)

            if context_name == "If":
                self.ir_manager.emit(f"\n\tifFalse {right} goto {false_label}\n")

        return left


    # Visit a parse tree produced by CompiScriptLanguageParser#equality.
    def visitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        """
        Visit the equality node and emit TAC for the operations.
        """
        left = self.visit(ctx.comparison(0))

        for i in range(1, len(ctx.comparison())):
            right = self.visit(ctx.comparison(i))

            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            # Form the expression string
            expr_str = f"{left} {operator} {right}"

            left = self.ir_manager.create_temp(expr_str)

        return left


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        """
        Visit the comparison node and emit TAC for the operations.
        """
        left = self.visit(ctx.term(0))

        for i in range(1, len(ctx.term())):
            right = self.visit(ctx.term(i))

            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            # Form the expression string
            expr_str = f"{left} {operator} {right}"

            left = self.ir_manager.create_temp(expr_str)

        return left


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        """
        Visit the term node and emit TAC for the operations.
        """
        left = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            right = self.visit(ctx.factor(i))

            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            # Form the expression string
            expr_str = f"{left} {operator} {right}"

            left = self.ir_manager.create_temp(expr_str)

        return left


    # Visit a parse tree produced by CompiScriptLanguageParser#factor.
    def visitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        """
        Visit the factor node and emit TAC for the operations.
        """
        left = self.visit(ctx.unary(0))

        for i in range(1, len(ctx.unary())):
            right = self.visit(ctx.unary(i))

            # Retrieve the operator directly from the children nodes between terms
            operator = ctx.getChild(2 * i - 1).getText()

            # Form the expression string
            expr_str = f"{left} {operator} {right}"

            left = self.ir_manager.create_temp(expr_str)

        return left


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedUnary.
    def visitNestedUnary(self, ctx:CompiScriptLanguageParser.NestedUnaryContext):
        """
        Visit the unary node and emit TAC for the operations.
        """
        operator = ctx.getChild(0).getText()
        value = self.visit(ctx.unary())

        # Form the expression string
        expr_str = f"{operator} {value}"

        return self.ir_manager.create_temp(expr_str)


    # Visit a parse tree produced by CompiScriptLanguageParser#callUnary.
    def visitCallUnary(self, ctx:CompiScriptLanguageParser.CallUnaryContext):
        """
        Visit the unary node and emit TAC for the operations.
        """
        return self.visit(ctx.call())


    # Visit a parse tree produced by CompiScriptLanguageParser#primaryCall.
    def visitPrimaryCall(self, ctx:CompiScriptLanguageParser.PrimaryCallContext):
        
        # Evaluate the primary value
        primary_value = self.visit(ctx.primary())

        i=1
        while i < len(list(ctx.getChildren())):
            # Check if this is a function call ( '(' arguments? ')' )
            if ctx.getChild(i).getText() == '(':
                func_name = primary_value
                
                # Evaluate the arguments
                arguments = self.visit(ctx.getChild(i+1)) if ctx.arguments() else []
                i = i + 3 if ctx.arguments() else i + 2 # Skip the arguments and the closing parenthesis

                # Emit temporary variables for the arguments
                arg_temps = []
                for arg in arguments:
                    temp = self.ir_manager.get_new_temp()
                    arg_temps.append(temp)
                    self.ir_manager.emit(f"\t{temp} = {arg} ;\n")

                # Emit the push parameters
                for arg_temp in arg_temps:
                    self.ir_manager.emit(f"\tPushParam {arg_temp} ;\n")

                # Emit the function call
                temp = self.ir_manager.get_new_temp()

                # Check if the function is the 'main' function
                if func_name != "main":
                    self.ir_manager.emit(f"\t{temp} = LCall _{func_name} ;\n")
                else:
                    self.ir_manager.emit(f"{temp} = LCall _main ;\n")

                if ctx.arguments():
                    self.ir_manager.emit(f"\tPopParams {len(arguments)*4} ;\n")

                primary_value = temp
                
            # Check if this is a member access ( '.' IDENTIFIER )
            elif ctx.getChild(i).getText() == '.':
                member_name = ctx.getChild(i + 1).getText() # Get the member name

                if primary_value == "this":
                    parameters = list(self.context_manager.get_symbol_table().items())
                    
                    for i in range(len(parameters)):
                        temp_size = self.ir_manager.create_temp("4") # Size of

                        # Check if the field exists in the parameters
                        if parameters[i][0] == member_name and parameters[i][1].__class__ == Parameter:

                            # Compute the offset for the index
                            temp_index = self.ir_manager.create_temp(str(i))

                            temp_offset = self.ir_manager.create_temp(f"{temp_index} * {temp_size}")  # Offset = index * 4

                            # Calculate the address of arr[index]
                            tem_pointer = self.ir_manager.create_temp(f"this + {temp_offset}")  # Pointer to arr[index]
                            temp_address = self.ir_manager.create_temp(f"*({tem_pointer})") # Dereference the pointer

                            primary_value = temp_address

                            break
                        
                    i = i + 2
        
        return primary_value

    # Visit a parse tree produced by CompiScriptLanguageParser#funAnonCall.
    def visitFunAnonCall(self, ctx:CompiScriptLanguageParser.FunAnonCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#true.
    def visitTrue(self, ctx:CompiScriptLanguageParser.TrueContext):
        """
        Visit the true node and emit TAC for the operations.
        """
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#false.
    def visitFalse(self, ctx:CompiScriptLanguageParser.FalseContext):
        """
        Visit the false node and emit TAC for the operations.
        """
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#nil.
    def visitNil(self, ctx:CompiScriptLanguageParser.NilContext):
        """
        Visit the nil node and emit TAC for the operations.
        """
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#this.
    def visitThis(self, ctx:CompiScriptLanguageParser.ThisContext):
        """
        Visit the 'this' node and emit TAC for the operations.
        """
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#number.
    def visitNumber(self, ctx:CompiScriptLanguageParser.NumberContext):
        """
        Visit the number node and emit TAC for the operations.
        """
        return ctx.NUMBER().getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#string.
    def visitString(self, ctx:CompiScriptLanguageParser.StringContext):
        """
        Visit the string node and emit TAC for the operations.
        """
        return ctx.STRING().getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#id.
    def visitId(self, ctx:CompiScriptLanguageParser.IdContext):
        """
        Visit the identifier node and emit TAC for the operations.
        """
        return ctx.IDENTIFIER().getText()


    # Visit a parse tree produced by CompiScriptLanguageParser#nestedExpression.
    def visitNestedExpression(self, ctx:CompiScriptLanguageParser.NestedExpressionContext):
        """
        Visit the expression node and emit TAC for the operations.
        """
        return self.visit(ctx.expression())


    # Visit a parse tree produced by CompiScriptLanguageParser#super.
    def visitSuper(self, ctx:CompiScriptLanguageParser.SuperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#newInstance.
    def visitNewInstance(self, ctx:CompiScriptLanguageParser.NewInstanceContext):
        """
        Visit the new instance node and emit TAC for the operations.
        """
        return self.visit(ctx.newExpression())


    # Visit a parse tree produced by CompiScriptLanguageParser#newExpression.
    def visitNewExpression(self, ctx:CompiScriptLanguageParser.NewExpressionContext):
        """
        Visit the new expression node and emit TAC for the operations.
        """
        # Main context
        main_context = self.context_manager.get_context_name()
        
        class_name = ctx.IDENTIFIER().getText() # Retrieve the class name

        self.context_manager.enter_context(f"Class.{class_name}") # Enter the class context
        self.context_manager.enter_context(f"Instance.{class_name}.{id(ctx)}") # Enter the instance context

        # Capture the context for the 'init' method
        self.context_manager.capture_context_for(f"Method.{class_name}.init")
        self.context_manager.enter_context(f"Method.{class_name}.init")
        
        # Evaluate the arguments
        arguments = [*self.visit(ctx.arguments())] if ctx.arguments() else []
        arguments.insert(0, f"alloc {len(arguments)*4}")  # Allocate space for the arguments

        primary_value = self.ir_manager.get_new_temp()

        # Emit temporary variables for the arguments
        arg_temps = []
        for arg in arguments:
            temp = primary_value if arg == f"alloc {len(arguments[1:])*4}" else self.ir_manager.get_new_temp()
            arg_temps.append(temp)
            self.ir_manager.emit(f"\t{temp} = {arg} ;\n")

        # Emit the push parameters
        for arg_temp in arg_temps:
            self.ir_manager.emit(f"\tPushParam {arg_temp} ;\n")

        # Emit the function call
        temp = self.ir_manager.get_new_temp()

        # Check if the function is the 'main' function
        self.ir_manager.emit(f"\t{temp} = LCall _{class_name}.init ;\n")

        if ctx.arguments():
            self.ir_manager.emit(f"\tPopParams {len(arguments)*4} ;\n")

        self.context_manager.exit_context()  # Exit the context for the 'init' method
        self.context_manager.enter_context(main_context)  # Return to the main context

        return primary_value


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        """
        Visit the function node and emit TAC for the operations.
        """
        # Retrieve the function name
        func_name = ctx.IDENTIFIER().getText()

        # Check if the function is a method and set the function name accordingly
        prefix, name = self.context_manager.get_context_name().split('.')
        if prefix == "Class":
            func_name = f"{name}.{func_name}"

        # Create a label for the function entry
        function_label = f"_{func_name}"
        self.ir_manager.emit(f"{function_label}:\n")
        self.ir_manager.emit(f"\tBeginFunc ;\n")

        # Enter a new context for the function
        context_name = f"Method.{func_name}" if prefix == "Class" else f"Function.{func_name}"
        self.context_manager.capture_context_for(context_name)
        self.context_manager.enter_context(context_name)

        parameters = []

        i = 0
        # Handle parameters
        for key, value in self.context_manager.get_symbol_table().items():
            if value.__class__ == Parameter:
                parameters.append((i, key))
                i += 1

        for i, param_name in parameters:
            # Assign each parameter a temporary variable
            self.ir_manager.emit(f"\t{param_name} = param{i} ;\n")
                

        # Visit the function body (block)
        self.visit(ctx.block())

        # Exit the function context
        self.context_manager.exit_context()

        self.ir_manager.emit(f"\tEndFunc ;\n")


    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        """
        Visit the arguments node and emit TAC for the operations.
        """
        arguments = []
        for i in range(len(ctx.expression())):
            arguments.append(self.visit(ctx.expression(i)))

        return arguments
    
    # Visit a parse tree produced by CompiScriptLanguageParser#newArray.
    def visitNewArray(self, ctx:CompiScriptLanguageParser.NewArrayContext):
        """
        Visit the new array node and emit TAC for the operations.
        """
        return self.visit(ctx.array())
    
    # Visit a parse tree produced by CompiScriptLanguageParser#array.
    def visitArray(self, ctx:CompiScriptLanguageParser.ArrayContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by CompiScriptLanguageParser#arrayAssignment.
    def visitArrayAssignment(self, ctx: CompiScriptLanguageParser.ArrayAssignmentContext):
        """
        Visit the array assignment node and emit TAC for the operations.
        """
        temp_address = self.visit(ctx.arrayAccess())  # Address of arr[index]
        value = self.visit(ctx.expression())    # Value to be assigned (arr[index] = value)

        temp_value = self.ir_manager.create_temp(value)
        self.ir_manager.emit(f"\t{temp_address} = {temp_value} ;\n")
    
    # Visit a parse tree produced by CompiScriptLanguageParser#arrayAccess.
    def visitArrayAccess(self, ctx: CompiScriptLanguageParser.ArrayAccessContext):
        """
        Visit the array access node and emit TAC for the operations.
        """
        array_name = ctx.IDENTIFIER().getText()   # Array name
        index = int(ctx.NUMBER().getText())      # Index expression (arr[index])

        # Compute the offset for the index
        temp_index = self.ir_manager.create_temp(str(index))  # Index
        temp_size = self.ir_manager.create_temp("4")  # Size of each element in the array
        
        temp_offset = self.ir_manager.create_temp(f"{temp_index} * {temp_size}")  # Offset = index * 4

        # Calculate the address of arr[index]
        tem_pointer = self.ir_manager.create_temp(f"{array_name} + {temp_offset}")  # Pointer to arr[index]
        temp_address = self.ir_manager.create_temp(f"*({tem_pointer})") # Dereference the pointer

        return temp_address
    
    # Visit a parse tree produced by CompiScriptLanguageParser#primaryArrayAccess.
    def visitPrimaryArrayAccess(self, ctx:CompiScriptLanguageParser.PrimaryArrayAccessContext):
        """
        Visit the primary array access node and emit TAC for the operations.
        """
        return self.visit(ctx.arrayAccess())