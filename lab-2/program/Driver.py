import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):

    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.result = None

    def visitProg(self, ctx):
        for child in ctx.stat():
            self.visit(child)

    def visitPrintExpr(self, ctx):
        # Impresion de resultado expresion
        print(f"Result: {self.visit(ctx.expr())}")

    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value

        #Impresion de asignacion
        print(f"Assign: {name} = {value}")

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()

        if operator == '+':
            return left + right
        else:
            return left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()

        if operator == '*':
            return left * right
        else:
            return int(left / right)

    def visitInt(self, ctx):
        return int(ctx.INT().getText())
    
    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.variables:
            return self.variables[name]
        else:
            raise ValueError(f"Variable '{name}' no definida.")
        
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitComp(self, ctx):
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
        
    def visitIf(self,ctx):
        condition = self.visit(ctx.expr())
        if condition:
            for child in ctx.stat()[:len(ctx.stat()) - len(ctx.ELSE()) - 1 if ctx.ELSE() else len(ctx.stat())]:
                self.visit(stat)
        elif ctx.ELSE() is not None:
            for stat in ctx.stat()[len(ctx.stat()) - len(ctx.ELSE()):]:
                self.visit(stat)

    
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!
    
    visitor = EvalVisitor()
    visitor.visit(tree)

    if visitor.result is not None:
        print(f"Result: {visitor.result}")

if __name__ == '__main__':
    main(sys.argv)
