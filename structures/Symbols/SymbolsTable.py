from structures.Symbols.SymbolsClasses import Symbol
from structures.Types.TypesClasses import Type

import textwrap

# SymbolsTable
# This class represents a symbol table. It contains a hash map to store symbols.
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
        symbol.set_value(value)
        symbol.set_type(type)

    def replace(self, name: str, symbol: Symbol):
        """Replace a symbol in the table."""
        if name not in self.table:
            raise KeyError(f"Symbol {name} is not defined.")
        self.table[name] = symbol

    def exists(self, name: str) -> bool:
        """Check if a symbol exists in the table."""
        return name in self.table
    
    import textwrap

    def print_table(self, context_name: str):
        """Prints the symbol table in a formatted table-like style with cells and wraps large values."""
        
        # Print table header
        print(f"--> Symbol Table for {context_name}:")
        if not self.table:
            print("Symbol table is empty.")
            print("\n")
            return
        
        # Define column widths
        name_width = 20
        info_width = 50
        total_width = name_width + info_width + 5

        # Print table headers with borders
        print("+" + "-" * (name_width + 2) + "+" + "-" * (info_width + 2) + "+")
        print(f"| {'Name':<{name_width}} | {'Info':<{info_width}} |")
        print("+" + "-" * (name_width + 2) + "+" + "-" * (info_width + 2) + "+")

        # Print each row of the symbol table
        for name, symbol in self.table.items():
            symbol_info = str(symbol)

            # Wrap the symbol info to fit within the defined width
            wrapped_info = textwrap.wrap(symbol_info, info_width)

            # Print the first line (name + first part of info)
            print(f"| {name:<{name_width}} | {wrapped_info[0]:<{info_width}} |")

            # Print the rest of the wrapped lines (only info column)
            for line in wrapped_info[1:]:
                print(f"| {'':<{name_width}} | {line:<{info_width}} |")

            print(f"| {"":<{name_width}} | {"":<{info_width}} |")
            
        # Print bottom border
        print("+" + "-" * (name_width + 2) + "+" + "-" * (info_width + 2) + "+")
        print("\n")


        def __repr__(self):
            return str(self.table)
