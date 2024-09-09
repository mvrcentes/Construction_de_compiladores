class Type:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

class VoidType(Type):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VoidType, cls).__new__(cls)
            cls._instance.name = "void"
        return cls._instance

    def __init__(self):
        super().__init__("void")

class AnyType(Type):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnyType, cls).__new__(cls)
            cls._instance.name = "any"
        return cls._instance

    def __init__(self):
        super().__init__("any")

class NilType(Type):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NilType, cls).__new__(cls)
            cls._instance.name = "nil"
        return cls._instance

    def __init__(self):
        super().__init__("nil")

class Primitive(Type):
    _instances = {}

    def __new__(cls, name):
        if name not in cls._instances:
            instance = super(Primitive, cls).__new__(cls)
            cls._instances[name] = instance
        return cls._instances[name]

    def __init__(self, name):
        super().__init__(name)

class IntType(Primitive):
    def __init__(self):
        super().__init__("int")

    def __new__(cls):
        return super(IntType, cls).__new__(cls, "int")

class DoubleType(Primitive):
    def __init__(self):
        super().__init__("double")

    def __new__(cls):
        return super(DoubleType, cls).__new__(cls, "double")

class BoolType(Primitive):
    def __init__(self):
        super().__init__("bool")

    def __new__(cls):
        return super(BoolType, cls).__new__(cls, "bool")

class StringType(Primitive):
    def __init__(self):
        super().__init__("string")

    def __new__(cls):
        return super(StringType, cls).__new__(cls, "string")

class Reference(Type):
    def __init__(self, name):
        super().__init__(name)

# You can define specific reference types if needed, e.g., for pointers, arrays, etc.

# Class
class ClassType(Type):
    def __init__(self, name):
        super().__init__(name)