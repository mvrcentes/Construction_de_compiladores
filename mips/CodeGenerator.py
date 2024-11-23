from mips.RegisterAllocator import RegisterAllocator

class CodeGenerator:
    def __init__(self, tac_file_path):
        self.tac_file_path = tac_file_path
        self.register_allocator = RegisterAllocator()
        self.mips_code = []
        self.actual_function = None
        self.data_words = []

    def read_tac_file(self):
        """Reads TAC code from a file and returns it as a list of instructions."""
        with open(self.tac_file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def generate_mips_code(self):
        """Generates MIPS code from the TAC code."""
        tac_code = self.read_tac_file()

        self.mips_code.append(".text") # Start of text segment
        self.mips_code.append(".globl main") # Declare main as a global function

        for line in tac_code:
            parts = line.split()
            # print(parts)
            # print("\n")

            if not parts:
                continue

            if parts[0] == "_main:":
                self.mips_code.append("main:")
                self.actual_function = "_main"
                continue

            if parts[0] == "data":
                self.data_words.append(parts[1])
                continue

            if parts[0] == "BeginFunc":
                #self.mips_code.append("addi $sp, $sp, -32  # Adjust stack pointer")
                continue

            if parts[0] == "EndFunc":
                if self.actual_function == "_main":
                    self.mips_code.append("li $v0, 10  # Exit system call")
                    self.mips_code.append("syscall")
                else:
                    self.mips_code.append("jr $ra  # Return from function")
                    self.mips_code.append("")
                continue

            if parts[0] == "return":
                reg = self.register_allocator.get_register(parts[1])
                self.mips_code.append(f"move $v0, {reg}  # Return value")
                self.mips_code.append("jr $ra  # Return")
                continue

            if parts[0] == "ifFalse":
                condition_reg = self.register_allocator.get_register(parts[1])
                label = parts[-1]
                self.mips_code.append(f"beq {condition_reg}, $zero, {label}  # Branch if false")
                continue

            if parts[0] == "if":            
                condition_reg = self.register_allocator.get_register(parts[1])
                label = parts[-1]
                self.mips_code.append(f"bne {condition_reg}, $zero, {label}  # Branch if true")
                continue

            if parts[0] == "goto":
                label = parts[1]
                self.mips_code.append(f"b {label}  # Unconditional jump")
                continue

            if parts[0].endswith(":"):
                label = parts[0][:-1]
                self.mips_code.append(f"{label}:")
                continue

            if parts[0] == "PushParam":
                reg = self.register_allocator.get_register(parts[1])
                self.mips_code.append(f"sw {reg}, 0($sp)  # Push parameter")
                self.mips_code.append("addi $sp, $sp, -4")
                continue

            if parts[0] == "LCall":
                function_name = parts[1]
                if function_name == "print":
                    self.mips_code.append(self.register_allocator.generate_print_instruction(parts[2]))
                else:
                    self.mips_code.append(f"jal {function_name}  # Call function")
                    result_reg = self.register_allocator.get_register(parts[-1])
                    self.mips_code.append(f"move {result_reg}, $v0  # Store return value")
                continue

            if parts[0] == "PopParams":
                self.mips_code.append(f"addi $sp, $sp, {parts[1]}  # Pop parameters")
                continue

            # Handle assignment operations (e.g., x = 10 or x = y)
            if "=" in parts and len(parts) == 4:
                dest = parts[0]
                src = parts[2]

                self.mips_code.append(self.register_allocator.generate_copy_instruction(dest, src))

                continue

            # Handle arithmetic and logic operations (e.g., _t0 = n <= 1)
            if "=" in parts and len(parts) == 6:
                dest = parts[0]
                op1 = parts[2]
                operator = parts[3]
                op2 = parts[4]

                if operator == "+":
                    self.mips_code.append(self.register_allocator.generate_instruction("add", dest, op1, op2))
                elif operator == "-":
                    self.mips_code.append(self.register_allocator.generate_instruction("sub", dest, op1, op2))
                elif operator == "*":
                    self.mips_code.append(self.register_allocator.generate_instruction("mul", dest, op1, op2))
                elif operator == "/":
                    self.mips_code.append(self.register_allocator.generate_instruction("div", dest, op1, op2))
                elif operator == "<=":
                    self.mips_code.append(self.register_allocator.generate_instruction("sle", dest, op1, op2))
                elif operator == ">=":
                    self.mips_code.append(self.register_allocator.generate_instruction("sge", dest, op1, op2))
                elif operator == "<":
                    self.mips_code.append(self.register_allocator.generate_instruction("slt", dest, op1, op2))
                elif operator == ">":
                    self.mips_code.append(self.register_allocator.generate_instruction("sgt", dest, op1, op2))
                elif operator == "==":
                    self.mips_code.append(self.register_allocator.generate_instruction("seq", dest, op1, op2))
                # Add more operators as needed
                continue
        
        data_segment = ".data\n"
        for word in self.data_words:
            data_segment += f"{word}: .word 0\n"

        self.mips_code.append("\n#----------------data section-------------------")
        self.mips_code.append(data_segment)

        return self.mips_code

    def write_mips_to_file(self, output_path):
        """Writes the generated MIPS code to a file."""
        with open(output_path, 'w') as file:
            for line in self.mips_code:
                file.write(line + "\n")
