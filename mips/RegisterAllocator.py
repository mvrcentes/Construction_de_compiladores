class RegisterAllocator:
    def __init__(self):
        # Initialize register descriptor, variable descriptor, memory, and tracking structures
        self.registers_descriptor = {
            '$t0': set(), '$t1': set(), '$t2': set(), '$t3': set(),
            '$t4': set(), '$t5': set(), '$t6': set(), '$t7': set(),
            '$t8': set(), '$t9': set()
        }
        self.variables_descriptor = {}  # Map each variable to a set of locations (registers or memory)
        self.memory = {}                # Store spilled variables in memory
        self.usage_frequency = {}       # Track how often each variable is used
        self.last_access_time = {}      # Track the last access time for each variable
        self.time_counter = 0           # Incremental counter to track the last access time

    def update_usage_tracking(self, variable):
        """Update the usage frequency and last access time for a variable."""
        self.usage_frequency[variable] = self.usage_frequency.get(variable, 0) + 1
        self.last_access_time[variable] = self.time_counter
        self.time_counter += 1

    def spill_and_assign(self, variable):
        # Use a smarter spilling strategy that considers liveness and usage frequency
        least_used_var = None
        least_usage_count = float('inf')
        oldest_access_time = float('inf')
        reg_to_spill = None

        # Find the best candidate for spilling
        for reg, variables in self.registers_descriptor.items():
            if len(variables) > 0:
                for var in variables:
                    usage_count = self.usage_frequency.get(var, 0)
                    access_time = self.last_access_time.get(var, 0)

                    # Prioritize spilling by least usage frequency and oldest access time
                    if usage_count < least_usage_count or (usage_count == least_usage_count and access_time < oldest_access_time):
                        least_used_var = var
                        least_usage_count = usage_count
                        oldest_access_time = access_time
                        reg_to_spill = reg

        if least_used_var:
            print(f"Spilling {least_used_var} from {reg_to_spill} to memory")
            self.memory[least_used_var] = least_used_var
            self.registers_descriptor[reg_to_spill].remove(least_used_var)

            # Update the variables_descriptor to reflect the change
            if least_used_var in self.variables_descriptor:
                self.variables_descriptor[least_used_var].remove(reg_to_spill)
                self.variables_descriptor[least_used_var].add('memory')

            # Assign the new variable to the now-free register
            self.registers_descriptor[reg_to_spill].add(variable)
            self.update_usage_tracking(variable)

            return reg_to_spill

        raise RuntimeError("No registers available and spilling failed")

    def get_register(self, variable):
        # Check if the variable is already in a register
        for reg, variables in self.registers_descriptor.items():
            if variable in variables:
                self.update_usage_tracking(variable)
                return reg

        # Look for a free register
        for reg, variables in self.registers_descriptor.items():
            if len(variables) == 0:
                # Assign the variable to the free register
                self.registers_descriptor[reg].add(variable)
                self.update_usage_tracking(variable)
                return reg

        # If no free register is found, spill and assign
        return self.spill_and_assign(variable)

    def generate_instruction(self, operation, x, y=None, z=None):
        """
        Generate an instruction based on the operation and operands.
        """
        x_reg = self.get_register(x)
        y_reg = self.get_register(y) if y else None
        z_reg = self.get_register(z) if z else None

        if operation == "move":
            return self.generate_copy_instruction(x, y)
        elif operation in ["add", "sub", "mul", "div"]:
            return self.generate_arithmetic_instruction(operation, x, y, z, x_reg, y_reg, z_reg)
        elif operation in ["sle", "seq", "slt", "sge", "sgt"]:
            return self.generate_logic_instruction(operation, x, y, z, x_reg, y_reg, z_reg)
        elif operation == "ld":
            return self.generate_load_instruction(x_reg, x)
        elif operation == "st":
            return self.generate_store_instruction(x_reg, x)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

    def generate_arithmetic_instruction(self, operation, x, y, z, x_reg, y_reg, z_reg):
        """Generates an arithmetic instruction and updates descriptors (Rule 3)."""

        code = ""
        
        # Load the operands into registers if they are not already there
        if y not in self.variables_descriptor or y_reg not in self.variables_descriptor[y]:
            code += self.generate_load_instruction(y_reg, y)

        if z not in self.variables_descriptor or z_reg not in self.variables_descriptor[z]:
            code += self.generate_load_instruction(z_reg, z)

        # Update the descriptors for the result x
        # Rule 3(a): Modify the register descriptor for R_x to contain only x
        self.registers_descriptor[x_reg] = {x}

        # Rule 3(b): Modify the address descriptor for x to include only R_x
        self.variables_descriptor[x] = {x_reg}

        # Rule 3(c): Remove R_x from the address descriptor of any variable other than x
        for var, locations in self.variables_descriptor.items():
            if var != x and x_reg in locations:
                locations.remove(x_reg)

        # Print the generated instruction
        return code + f"{operation} {x_reg}, {y_reg}, {z_reg}" + "\n"
    
    def generate_logic_instruction(self, operation, x, y, z, x_reg, y_reg, z_reg):
        """Generates an arithmetic instruction and updates descriptors (Rule 3)."""

        code = ""
        
        # Load the operands into registers if they are not already there
        if y not in self.variables_descriptor or y_reg not in self.variables_descriptor[y]:
            code += self.generate_load_instruction(y_reg, y)

        if z not in self.variables_descriptor or z_reg not in self.variables_descriptor[z]:
            code += self.generate_load_instruction(z_reg, z)

        # Update the descriptors for the result x
        # Rule 3(a): Modify the register descriptor for R_x to contain only x
        self.registers_descriptor[x_reg] = {x}

        # Rule 3(b): Modify the address descriptor for x to include only R_x
        self.variables_descriptor[x] = {x_reg}

        # Rule 3(c): Remove R_x from the address descriptor of any variable other than x
        for var, locations in self.variables_descriptor.items():
            if var != x and x_reg in locations:
                locations.remove(x_reg)

        # Print the generated instruction
        return code + f"{operation} {x_reg}, {y_reg}, {z_reg}" + "\n"
    
    def is_number(self, s):
        """Checks if the given string is a number (handles integers and floats)."""
        try:
            float(s)  # Attempt to convert to float
            return True
        except ValueError:
            return False 

    def generate_load_instruction(self, reg, x):
        """Generates an LD or LDI instruction and updates descriptors (Rule 1)."""

        # Rule 1(a): Modify the register descriptor for reg to contain only x
        self.registers_descriptor[reg] = {x}

        if x.isdigit() or self.is_number(x):
            return f"li {reg}, {x}" + "\n"
        else:
            # Rule 1(b): Modify the address descriptor for x to add reg
            self.variables_descriptor.setdefault(x, set()).add(reg)

            return f"lw {reg}, {x}" + "\n"
        
    def generate_store_instruction(self, reg, x):
        """Generates an ST instruction and updates descriptors (Rule 2)."""

        # Rule 2: Modify the address descriptor for x to include its memory location
        self.variables_descriptor[x] = {x}

        # Remove x from the register descriptor for reg
        for reg, variables in self.registers_descriptor.items():
            if x in variables:
                self.registers_descriptor[reg].remove(x)

        return f"sw {reg}, {x}" + "\n"

    def generate_copy_instruction(self, x, y):
        """Generates a copy instruction x = y and updates descriptors (Rule 4)."""
        code = ""

        y_reg = self.get_register(y)

        # Load y into a register if it is not already there
        if y not in self.variables_descriptor or y_reg not in self.variables_descriptor[y]:
            code += self.generate_load_instruction(y_reg, y)

        # # Rule 4(a): Add x to the register descriptor for y_reg
        # self.registers_descriptor.setdefault(y_reg, set()).add(x)

        # # Rule 4(b): Modify the address descriptor for x to include only y_reg
        # self.variables_descriptor[x] = {y_reg}

        code += f"move $s0, {y_reg}" + "\n"

        # Remove x from the register descriptor for reg
        for reg, variables in self.registers_descriptor.items():
            if x in variables:
                self.registers_descriptor[reg].remove(x)

        # Modify the address descriptor for x to include only R_x
        self.variables_descriptor[x] = {x}

        # Generate the copy instruction
        return code + f"sw $s0, {x}" + "\n"
    
    def generate_print_instruction(self, x):
        """Generates a print instruction and updates descriptors (Rule 5)."""
        code = ""

        x_reg = self.get_register(x)

        # Load x into a register if it is not already there
        if x not in self.variables_descriptor or x_reg not in self.variables_descriptor[x]:
            code += self.generate_load_instruction(x_reg, x)

        # Rule 5(a): Modify the register descriptor for R_x to contain only x
        self.registers_descriptor[x_reg] = {x}

        # Rule 5(b): Modify the address descriptor for x to include only R_x
        self.variables_descriptor[x] = {x_reg}

        # Rule 5(c): Remove R_x from the address descriptor of any variable other than x
        for var, locations in self.variables_descriptor.items():
            if var != x and x_reg in locations:
                locations.remove(x_reg)

        # Generate the print instruction
        return code + f"li $v0, 1\nmove $a0, {x_reg}\nsyscall" + "\n"

    def __str__(self):
        # Return the current state of registers and memory
        reg_state = ", ".join([f"{reg}: {list(value)}" for reg, value in self.registers_descriptor.items()])
        mem_state = ", ".join([f"{var}" for var in self.memory])
        return f"Registers: {reg_state}\nMemory: {mem_state}"