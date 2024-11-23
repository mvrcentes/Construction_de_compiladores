class Type:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size  # Size of the type in bytes

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, size={self.size})"


class VoidType(Type):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VoidType, cls).__new__(cls)
            cls._instance.name = "void"
            cls._instance.size = 0  # Void has no size
        return cls._instance

    def __init__(self):
        super().__init__("void", 0)


class AnyType(Type):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnyType, cls).__new__(cls)
            cls._instance.name = "any"
            cls._instance.size = -1  # Size unknown or dynamic
        return cls._instance

    def __init__(self):
        super().__init__("any", -1)


class NilType(Type):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NilType, cls).__new__(cls)
            cls._instance.name = "nil"
            cls._instance.size = 0  # Nil has no size
        return cls._instance

    def __init__(self):
        super().__init__("nil", 0)


class Primitive(Type):
    _instances = {}

    def __new__(cls, name, size):
        if name not in cls._instances:
            instance = super(Primitive, cls).__new__(cls)
            cls._instances[name] = instance
        return cls._instances[name]

    def __init__(self, name, size):
        super().__init__(name, size)


class IntType(Primitive):
    def __init__(self):
        super().__init__("int", 4)  # Typically 4 bytes

    def __new__(cls):
        return super(IntType, cls).__new__(cls, "int", 4)


class DoubleType(Primitive):
    def __init__(self):
        super().__init__("double", 8)  # Typically 8 bytes

    def __new__(cls):
        return super(DoubleType, cls).__new__(cls, "double", 8)


class BoolType(Primitive):
    def __init__(self):
        super().__init__("bool", 1)  # Typically 1 byte

    def __new__(cls):
        return super(BoolType, cls).__new__(cls, "bool", 1)


class StringType(Primitive):
    def __init__(self):
        super().__init__("string", -1)  # Dynamic size, depends on content

    def __new__(cls):
        return super(StringType, cls).__new__(cls, "string", -1)


class Reference(Type):
    def __init__(self, name, reference_type=None, size=8):
        super().__init__(name, size)  # Reference size, typically 8 bytes (64-bit systems)
        self.reference_type = reference_type

    def __str__(self):
        return f"{self.name}[{self.reference_type}]" if self.reference_type else self.name


class ArrayType(Reference):
    def __init__(self, name, reference_type, element_count):
        element_size = reference_type.size if reference_type else 0
        total_size = element_size * element_count
        super().__init__(name, reference_type, total_size)

    def __str__(self):
        return f"{self.name}[{self.reference_type}]" if self.reference_type else self.name


class ClassType(Type):
    def __init__(self, name, size=0):
        super().__init__(name, size)