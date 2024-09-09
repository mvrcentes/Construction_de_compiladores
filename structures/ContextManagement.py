from structures.Symbols.SymbolsTable import SymbolsTable
from structures.Symbols.SymbolsClasses import Symbol
from structures.Types.TypesClasses import Type

class Context:
    def __init__(self, name: str, parent:'Context'=None):
        self.name = name
        self.symbol_table = SymbolsTable()
        self.parent = parent
        self.class_symbol = None

    def define(self, symbol: Symbol):
        self.symbol_table.define(symbol)

    def lookup(self, name: str):
        return self.symbol_table.lookup(name)

    def assign(self, name: str, value: any, type: Type):
        self.symbol_table.assign(name, value, type)

    def replace(self, name: str, symbol: Symbol):
        self.symbol_table.replace(name, symbol)

    def exists(self, name: str):
        return self.symbol_table.exists(name)
    
    def print_symbol_table(self):
        self.symbol_table.print_table(self.name)

    def set_context_class(self, class_symbol):
        self.class_symbol = class_symbol

    def get_context_class(self):
        return self.class_symbol

    def __repr__(self):
        return f"Context(name={self.name}, symbols={self.symbol_table})"

class ContextManager:
    def __init__(self):
        self.contexts = {}
        self.global_context = self.create_context("Main.global")
        self.current_context = self.global_context

    def create_context(self, name: str, parent: 'Context'=None):
        """Create a new context with an optional parent context."""
        context = Context(name, parent)
        self.contexts[name] = context
        return context

    def enter_context(self, name: str):
        """Enter a context by name."""
        self.current_context = self.contexts.get(name)
        if not self.current_context:
            raise KeyError(f"Context {name} does not exist.")
        return self.current_context

    def exit_context(self):
        """Exit the current context and return to the parent context."""
        if self.current_context and self.current_context.parent:
            self.current_context = self.current_context.parent
        else:
            self.current_context = self.global_context

    def lookup(self, name: str):
        """Look up a symbol by name in the current context and its parents."""
        context = self.current_context
        while context:
            symbol = context.lookup(name)
            if symbol:
                return symbol, context.name
            context = context.parent


    def define(self, symbol: Symbol):
        """Define a new symbol in the current context."""
        if self.current_context:
            self.current_context.define(symbol)
        else:
            raise RuntimeError("No active context to define symbol.")

    def assign(self, name: str, value: any, type: Type):
        """Assign a value to an already defined symbol in a context."""
        context = self.exists(name)
        context.assign(name, value, type)

    def replace(self, name: str, symbol: Symbol, context_name: str):
        """Replace a symbol in the current context."""
        if self.contexts[context_name]:
            self.contexts[context_name].replace(name, symbol)
        else:
            raise KeyError(f"Context {context_name} does not exist.")
        
    def exists(self, name: str):
        """Check if a symbol exists in the current context or its parents."""
        if self.current_context:
            context = self.current_context
            while context:
                if context.lookup(name):
                    return context
                context = context.parent
            return None
        else:
            raise RuntimeError("No active context to check symbol existence.")

    def capture_context(self, name: str):
        """Capture the current context for closure purposes."""
        if name in self.contexts:
            context = self.contexts[name]
            context.parent = self.current_context
        else:
            raise KeyError(f"Context {name} does not exist.")
        
    def check_recursive_context(self, name: str):
        """Check if a context is recursive."""
        context = self.current_context
        while context:
            if context.name == name:
                return True
            context = context.parent
        return False
    
    def get_context_name(self):
        """Get the name of the current context."""
        return self.current_context.name

    def __repr__(self):
        return f"ContextManager(current_context={self.current_context}, contexts={self.contexts})"
