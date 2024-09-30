from structures.Types.TypesClasses import Type

class TypesTable:
    def __init__(self):
        # Hash map to store types, where the key is the type name
        self.table = {}

    def add_type(self, type_obj: Type):
        """Add a new type to the table."""
        if type_obj.name in self.table:
            raise KeyError(f"Type {type_obj.name} is already defined.")
        self.table[type_obj.name] = type_obj

    def get_type(self, name: str) -> Type:
        """Retrieve a type by name."""
        if name not in self.table:
            raise KeyError(f"Type {name} is not defined.")
        return self.table[name]

    def exists(self, name: str) -> bool:
        """Check if a type exists in the table."""
        return name in self.table

    def __repr__(self):
        return str(self.table)
