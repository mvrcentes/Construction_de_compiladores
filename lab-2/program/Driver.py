import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor

class MyVisitor(MiniLangVisitor):

    def __init__(self):
        super(MyVisitor, self).__init__()
        self.variables = {}  # Para almacenar variables asignadas
        self.functions = {}  # Para almacenar funciones definidas por el usuario
        self.res = None

    def visitProg(self, ctx: MiniLangParser.ProgContext):
        for child in ctx.stat():
            self.visit(child)

    def visitPrintExpr(self, ctx: MiniLangParser.PrintExprContext):
        # Impresion de resultado expresion
        print(f"Result: {self.visit(ctx.expr())}")

    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value

        #Impresion de asignacion
        print(f"Assign: {name} = {value}")

    def visitBlank(self, ctx: MiniLangParser.BlankContext):
        pass

    def visitParens(self, ctx: MiniLangParser.ParensContext):
        return self.visit(ctx.expr())

    def visitMulDiv(self, ctx: MiniLangParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()

        if isinstance(left, int) and isinstance(right, int):
            if operator == '*':
                return left * right
            else:
                return int(left / right)
        elif isinstance(left, int) and isinstance(right, str) and operator == '*':
            single = right
            for i in range(left):
                right+=single
            return right
        else:
            raise ValueError("multiply/division: invalid types for operands")

    def visitAddSub(self, ctx: MiniLangParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()

        if isinstance(left, int) and isinstance(right, int):
            if operator == '+':
                return left + right
            else:
                return left - right
        elif isinstance(left, str) and isinstance(right, str) and operator == '+':
            return left + right
        else:
            raise ValueError("addition/subtraction: invalid types for operands")

    def visitComparison(self, ctx: MiniLangParser.ComparisonContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()

        if operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '<=':
            return left <= right
        else:
            return left >= right

    def visitId(self, ctx: MiniLangParser.IdContext):
        name = ctx.ID().getText()
        if name in self.variables:
            return self.variables[name]
        else:
            raise ValueError(f"Variable '{name}' no definida.")
        
    def visitString(self, ctx: MiniLangParser.StringContext):
        return ctx.STRING().getText().strip('"')

    def visitInt(self, ctx: MiniLangParser.IntContext):
        return int(ctx.INT().getText())

    def visitIfStatement(self, ctx: MiniLangParser.IfStatementContext):
        condition = self.visit(ctx.expr())
        if condition:
            for stat in ctx.stat()[:len(ctx.stat()) - 1]:
                self.visit(stat)
        elif ctx.ELSE() is not None:
            for stat in ctx.stat()[len(ctx.stat()) - 1:]:
                res = self.visit(stat)

    def visitWhileStatement(self, ctx: MiniLangParser.WhileStatementContext):
        while self.visit(ctx.expr()):
            for stat in ctx.stat():
                self.visit(stat)

    def visitFuncDef(self, ctx: MiniLangParser.FuncDefContext):
        name = ctx.ID(0).getText()
        params = [param.getText() for param in ctx.ID()[1:]]
        self.functions[name] = (params, ctx.stat())

def main(argv):
    input_file = argv[1]
    with open(input_file, encoding='utf-8') as file:
        input_stream = InputStream(file.read())
    
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog()  # Analizar la entrada utilizando la regla 'prog'

    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)