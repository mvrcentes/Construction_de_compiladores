from structures.Types.TypesClasses import *

# Symbol
# This class represents a symbol. It contains a name and a type.
class Symbol:
    def __init__(self, name: str, type: Type):
        self.name = name
        self.type = type

    # Set name
    def set_name(self, name: str):
        self.name = name

    # Get name
    def get_name(self):
        return self.name

    # Set type
    def set_type(self, type: Type):
        self.type = type

    # Get type
    def get_type(self):
        return self.type
        
    def __repr__(self):
        return f"Symbol (type={self.type})"

# Constant
# This class represents a constant symbol. It contains a value.
class Constant(Symbol):
    def __init__(self, name: str, ctx: any, type: Type, value: any):
        if value is None or type is None:
            raise ValueError("A constant must have an initial type and value")
        super().__init__(name, ctx, type)
        self.value = value

    def __repr__(self):
        return f"Constant (type={self.type}, value={self.value})"

# Variable
# This class represents a variable symbol. It contains a value.    
class Variable(Symbol):
    def __init__(self, name: str, type: Type = NilType(), value: any = None):
        super().__init__(name, type)
        self.value = value

    # Set new value
    def set_value(self, value: any):
        self.value = value

    def __repr__(self):
        return f"Variable (type={self.type}, value={self.value})"

# Parameter
# This class represents a parameter symbol. It contains a value.
class Parameter(Symbol):
    def __init__(self, name: str, type: Type = NilType(), value: any = None):
        super().__init__(name, type)
        self.value = value

    # Set value
    def set_value(self, value: any):
        self.value = value

    def __repr__(self):
        return f"Parameter (type={self.type}, value={self.value})"

# Function
# This class represents a function symbol. It contains a return type and parameters.
class Function(Symbol):
    def __init__(self, name: str, return_type: Type = VoidType(), parameters: list = None):
        super().__init__(name, return_type)
        self.parameters = parameters if parameters is not None else []
        self.return_values = [] # List of return values
    
    def set_return_type(self, return_type: Type):
        self.type = return_type

    def set_block(self, block: any):
        self.block = block

    def get_block(self):
        return self.block

    def add_parameter(self, parameter: Parameter):
        self.parameters.append(parameter)

    def get_parameters(self):
        return self.parameters
    
    def add_return_value(self, value: any):
        self.return_values.append(value)

    def get_return_values(self):
        return self.return_values

    def __repr__(self):
        params_str = ", ".join(str(param) for param in self.parameters)
        return f"Function (return_type={self.type}, parameters=[{params_str}])"

# Field
# This class represents a field symbol. It contains a value.    
class Field(Symbol):
    def __init__(self, name: str, type: Type = NilType(), value: any = None):
        super().__init__(name, type)
        self.value = value

    # Set value
    def set_value(self, value: any):
        self.value = value

    # Get value
    def get_value(self):
        return self.value

    def __repr__(self):
        return f"Field (type={self.type}, value={self.value})"

# Method
# This class represents a method symbol. It contains a return type, parameters, and a flag to indicate if it is static.
class Method(Function):
    def __init__(self, name: str, return_type: Type = VoidType(), parameters: list = None):
        super().__init__(name, return_type, parameters)

    def __repr__(self):
        params_str = ", ".join(str(param) for param in self.parameters)
        return f"Method(name={self.name}, return_type={self.type}, parameters=[{params_str}])"

# ClassSymbol
# This class represents a class symbol. It contains fields and methods.    
class ClassSymbol(Symbol):
    def __init__(self, name: str, superclass: 'ClassSymbol' = None):
        super().__init__(name, ClassType(name))
        self.superclass = superclass
        self.methods = {}

    def add_method(self, method: Method):
        if method.name in self.methods:
            raise NameError(f"Method {method.name} already defined in class {self.name}.")
        self.methods[method.name] = method

    def lookup_method(self, name: str):
        if name in self.methods:
            return self.methods[name]
        elif self.superclass:
            return self.superclass.lookup_method(name)
        return None

    def __repr__(self):
        methods_str = ", ".join(str(method) for method in self.methods.values())
        superclass_str = f" extends {self.superclass.name}" if self.superclass else ""
        return f"ClassSymbol({self.name}{superclass_str}, methods=[{methods_str}])"

# Instance
# This class represents an instance of a class symbol.    
class Instance(Variable):
    def __init__(self, name: str, class_symbol: ClassSymbol, type: Type = ClassType):
        super().__init__(name, type)
        self.class_symbol = class_symbol
        self.fields = {}

    def add_field(self, field: Field):
        if field.name in self.fields:
            raise NameError(f"Field {field.name} already defined in instance of class {self.class_symbol.name}.")
        self.fields[field.name] = field

    def __repr__(self):
        return f"Instance(class=[{self.class_symbol.name}])"