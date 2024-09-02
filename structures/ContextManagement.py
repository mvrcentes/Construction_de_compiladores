from structures.Symbols.SymbolsTable import SymbolsTable
from structures.Symbols.SymbolsClasses import Symbol
from structures.Types.TypesClasses import Type

class Context:
    def __init__(self, name: str, parent:'Context'=None):
        self.name = name
        self.symbol_table = SymbolsTable()
        self.parent = parent

    def define(self, symbol: Symbol):
        self.symbol_table.define(symbol)

    def lookup(self, name: str):
        return self.symbol_table.lookup(name)

    def assign(self, name: str, value: any, type: Type):
        self.symbol_table.assign(name, value, type)

    def exists(self, name: str):
        return self.symbol_table.exists(name)

    def __repr__(self):
        return f"Context(name={self.name}, symbols={self.symbol_table})"

class ContextManager:
    def __init__(self):
        self.contexts = {}
        self.global_context = self.create_context("global")
        self.current_context = self.global_context

    def create_context(self, name: str, parent: 'Context'=None):
        context = Context(name, parent)
        self.contexts[name] = context
        return context

    def enter_context(self, name: str):
        self.current_context = self.contexts.get(name)
        if not self.current_context:
            raise KeyError(f"Context {name} does not exist.")
        return self.current_context

    def exit_context(self):
        if self.current_context and self.current_context.parent:
            self.current_context = self.current_context.parent
        else:
            self.current_context = self.global_context

    def lookup(self, name: str):
        context = self.current_context
        while context:
            symbol = context.lookup(name)
            if symbol:
                return symbol
            context = context.parent


    def define(self, symbol: Symbol):
        if self.current_context:
            self.current_context.define(symbol)
        else:
            raise RuntimeError("No active context to define symbol.")

    def assign(self, name: str, value: any, type: Type):
        if self.current_context:
            self.current_context.assign(name, value, type)
        else:
            raise RuntimeError("No active context to assign value.")
        
    def exists(self, name: str):
        context = self.current_context
        while context:
            if context.lookup(name):
                return True
            context = context.parent
        return False

    def capture_context(self, name: str):
        """Capture the current context for closure purposes."""
        context = self.current_context
        while context and context.name != name:
            context = context.parent
        if context:
            return context
        raise KeyError(f"Context {name} not found for closure capture.")

    def __repr__(self):
        return f"ContextManager(current_context={self.current_context}, contexts={self.contexts})"
