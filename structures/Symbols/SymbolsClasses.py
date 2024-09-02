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
    
    def __repr__(self):
        params_str = ", ".join(str(param) for param in self.parameters)
        return f"Function (return_type={self.type}, parameters=[{params_str}])"

class Field(Symbol):
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
        return f"Field (type={self.type}, value={self.value})"

class Method(Function):
    def __init__(self, name: str, ctx: any, return_type: Type = NilType(), parameters: list = None, is_static: bool = False):
        super().__init__(name, ctx, return_type, parameters)
        self.is_static = is_static

    def __repr__(self):
        params_str = ", ".join(str(param) for param in self.parameters)
        return f"Method (return_type={self.type}, is_static={self.is_static}, parameters=[{params_str}])"
    
class ClassSymbol(Symbol):
    def __init__(self, name: str, ctx: any, classType: Type, superclass: 'ClassSymbol' = None, methods: list = None):
        super().__init__(name, ctx, classType)
        self.superclass = superclass
        self.fields = []
        self.methods = methods if methods is not None else []

    def add_method(self, method: Method):
        self.methods.append(method)

    def lookup_method(self, method_name: str):
        # First look in the current class's methods
        for method in self.methods:
            if method.name == method_name:
                return method
        # If not found, look in the superclass
        if self.superclass:
            return self.superclass.lookup_method(method_name)
        return None
    
    def __repr__(self):
        methods_str = ", ".join(str(method) for method in self.methods)
        superclass_str = f" extends {self.superclass.name}" if self.superclass else ""
        return f"ClassSymbol ({self.name}{superclass_str}, methods=[{methods_str}])"

