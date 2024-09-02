from structures.Types.TypesClasses import *

class Symbol:
    def __init__(self, name: str, type: Type):
        self.name = name
        self.type = type

    def __repr__(self):
        return f"Symbol (type={self.type})"