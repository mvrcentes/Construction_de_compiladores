from structures.Symbols.SymbolsClasses import Symbol
from structures.Types.TypesClasses import Type

class SymbolsTable:
    def __init__(self):
        # The hash map to store symbols, where the key is the symbol's name
        self.table = {}

    def define(self, symbol: Symbol):
        """Define a new symbol in the table."""
        if symbol.name in self.table:
            raise KeyError(f"Symbol {symbol.name} is already defined.")
        self.table[symbol.name] = symbol

    def lookup(self, name: str):
        """Look up a symbol by name."""
        return self.table.get(name)

    def assign(self, name: str, value: any, type: Type):
        """Assign a value to an already defined symbol."""
        symbol = self.lookup(name)
        if symbol is None:
            raise KeyError(f"Symbol {name} is not defined.")
        
        # Assign value and type
        symbol.value = value
        symbol.type  = type

    def exists(self, name: str) -> bool:
        """Check if a symbol exists in the table."""
        return name in self.table
    
    def print_table(self):
        """Prints the symbol table in a legible format."""
        if not self.table:
            print("Symbol table is empty.")
            return
        
        print("Symbol Table:")
        print(f"{'Name':<15} {'Info':<15}")
        print("-" * 45)
        for name, symbol in self.table.items():
            symbol_info = str(symbol)
            print(f"{name:<15} {symbol_info:<15}")

    def __repr__(self):
        return str(self.table)
