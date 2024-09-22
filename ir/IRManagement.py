class IRManager:
    def __init__(self):
        self.label_counter = 0
        self.temp_counter = 0
        self.code = []
        self.free_temps = [] # Stack of free temporary variables
        self.expr_cache = {} # Cache of expressions

    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emit(self, code_line):
        self.code.append(code_line)

    def get_code(self):
        return "".join(self.code)

    def get_new_temp(self):
        if self.free_temps:
            return self.free_temps.pop()
        
        temp = f"_t{self.temp_counter}"
        self.temp_counter += 1

        return temp

    def create_temp(self, expr_str):
        # Check if this expression has been computed before
        if expr_str in self.expr_cache:
            return self.expr_cache[expr_str]
        else:
            # Emit TAC for the operation and generate a new temp
            temp = self.get_new_temp()

            self.emit(f"\t{temp} = {expr_str};\n")
            
            # Store the result in the cache
            self.expr_cache[expr_str] = temp
            return temp


    def free_temp(self, temp):
        self.free_temps.append(temp)