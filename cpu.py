class SimpleCPU:
    def __init__(self):
        # SIMULATING HARDWARE
        self.memory = [0] * 256  # 256 bytes of RAM
        self.pc = 0  # Program Counter (points to current instruction)
        self.reg_a = 0  # Register A (General purpose storage)
        self.running = True

    def load_program(self, program):
        # Flash the "ROM" into our RAM
        for i, byte in enumerate(program):
            self.memory[i] = byte

    def run(self):
        print("--- CPU Booting ---")
        while self.running:
            # 1. FETCH
            instruction = self.memory[self.pc]
            self.pc += 1  # Move to the next byte

            # 2 & 3. DECODE AND EXECUTE
            self.execute(instruction)
        print("--- CPU Halted ---")

    def execute(self, instruction):
        # DEFINING THE INSTRUCTION SET (OPCODES)

        # 0x01: LOAD_A (Load the next byte into Register A)
        if instruction == 0x01:
            self.reg_a = self.memory[self.pc]
            self.pc += 1

        # 0x02: ADD_A (Add the next byte to Register A)
        elif instruction == 0x02:
            self.reg_a += self.memory[self.pc]
            self.pc += 1

        # 0x03: PRINT_A (Output the value of Register A to the screen)
        elif instruction == 0x03:
            print(f"OUTPUT: {self.reg_a}")

        # 0xFF: HALT (Stop the CPU)
        elif instruction == 0xFF:
            self.running = False

        else:
            print(f"CRASH! Unknown Opcode: {hex(instruction)} at Memory Address {self.pc - 1}")
            self.running = False


# --- WRITING OUR FIRST "ASSEMBLY" PROGRAM ---
# We write the program using raw bytes (Machine Code)
# Program logic: Load 5 into A, Add 10 to A, Print A, Stop.
rom_program = [
    0x01, 0x05,  # LOAD_A 5
    0x02, 0x0A,  # ADD_A 10 (0x0A is 10 in hexadecimal)
    0x03,  # PRINT_A (Should output 15)
    0xFF  # HALT
]

# --- POWERING ON THE CPU ---
my_cpu = SimpleCPU()
my_cpu.load_program(rom_program)
my_cpu.run()


class SimpleCPU:
    def __init__(self):
        self.memory = [0] * 256  # 256 bytes of RAM
        self.pc = 0  # Program Counter
        self.reg_a = 0  # Register A
        self.reg_b = 0  # Register B
        self.running = True

    def load_program(self, program):
        for i, byte in enumerate(program):
            self.memory[i] = byte

    def run(self):
        print("--- CPU Booting ---")
        while self.running:
            instruction = self.memory[self.pc]
            self.pc += 1
            self.execute(instruction)
        print("--- CPU Halted ---")

    def execute(self, instruction):
        # 0x01: LOAD_A [value]
        if instruction == 0x01:
            self.reg_a = self.memory[self.pc]
            self.pc += 1

        # 0x04: LOAD_B [value]
        elif instruction == 0x04:
            self.reg_b = self.memory[self.pc]
            self.pc += 1

        # 0x05: ADD_A_B (Adds B into A)
        elif instruction == 0x05:
            self.reg_a += self.reg_b

        # 0x06: STORE_A [address] (Saves A into RAM)
        elif instruction == 0x06:
            address = self.memory[self.pc]
            self.memory[address] = self.reg_a
            self.pc += 1

        # 0x07: JUMP [address] (Changes the Program Counter to create loops)
        elif instruction == 0x07:
            address = self.memory[self.pc]
            self.pc = address

        # 0x03: PRINT_A
        elif instruction == 0x03:
            print(f"OUTPUT: {self.reg_a}")

        # 0xFF: HALT
        elif instruction == 0xFF:
            self.running = False

        else:
            print(f"CRASH! Unknown Opcode: {hex(instruction)}")
            self.running = False