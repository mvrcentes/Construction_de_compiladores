from structures.Types.TypesClasses import *

class Symbol:
    def __init__(self, name: str, type: Type):
        self.name = name
        self.type = type

    def __repr__(self):
        return f"Symbol (type={self.type})"

class Constant(Symbol):
    def __init__(self, name: str, ctx: any, type: Type, value: any):
        if value is None or type is None:
            raise ValueError("A constant must have an initial type and value")
        super().__init__(name, ctx, type)
        self.value = value

    def __repr__(self):
        return f"Constant (type={self.type}, value={self.value})"
    
class Variable(Symbol):
    def __init__(self, name: str, type: Type = NilType(), value: any = None):
        super().__init__(name, type)
        self.value = value

    # Set type
    def set_type(self, type: Type):
        self.type = type

    # Set new value
    def set_value(self, value: any):
        self.value = value

    def __repr__(self):
        return f"Variable (type={self.type}, value={self.value})"

class Parameter(Symbol):
    def __init__(self, name: str, ctx:any, type: Type = NilType(), value: any = None):
        super().__init__(name, ctx, type)
        self.value = value

    # Set type
    def set_type(self, type: Type):
        self.type = type

    # Set value
    def set_value(self, value: any):
        self.value = value

    def __repr__(self):
        return f"Parameter (type={self.type}, value={self.value})"

class Function(Symbol):
    def __init__(self, name: str, ctx: any, return_type: Type = NilType(), parameters: list = None):
        super().__init__(name, ctx, return_type)
        self.parameters = parameters if parameters is not None else []

    def add_parameter(self, parameter: Parameter):
        self.parameters.append(parameter)

    # Set the return type of the function until it is known
    def set_return_type(self, return_type: Type):
        self.type = return_type