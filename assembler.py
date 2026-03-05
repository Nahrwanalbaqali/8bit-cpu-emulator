from cpu import SimpleCPU


# 1. THE ASSEMBLER FUNCTION
def assemble(code_lines):
    # This dictionary maps our human-readable words to the CPU's hex codes
    opcodes = {
        "LOAD_A": 0x01,
        "PRINT_A": 0x03,
        "LOAD_B": 0x04,
        "ADD_A_B": 0x05,
        "STORE_A": 0x06,
        "JUMP": 0x07,
        "HALT": 0xFF
    }

    machine_code = []

    for line in code_lines:
        parts = line.strip().split()
        if not parts:
            continue

        instruction = parts[0]

        # Add the opcode
        machine_code.append(opcodes[instruction])

        # If there is a number after the command (like the '5' in 'LOAD_A 5'), add it too
        if len(parts) > 1:
            argument = int(parts[1])
            machine_code.append(argument)

    return machine_code


# 2. WRITE YOUR ASSEMBLY PROGRAM
# This program loads 10 and 20, adds them, prints 30, and stops.
# --- WRITING A LOOPING PROGRAM ---
# We want to count up by 5s forever (5, 10, 15, 20...)

my_program_text = [
    "LOAD_B 5",   # Address 0 & 1: Put 5 into Register B
    "ADD_A_B",    # Address 2: Add B into A (A starts at 0, so 0+5=5)
    "PRINT_A",    # Address 3: Print the new value of A
    "JUMP 2"      # Address 4 & 5: Go back to Memory Address 2 (the ADD instruction)
]

# 3. TRANSLATE AND RUN
print("Compiling program...")
compiled_hex = assemble(my_program_text)
print(f"Machine Code generated: {[hex(b) for b in compiled_hex]}")

my_cpu = SimpleCPU()
my_cpu.load_program(compiled_hex)
my_cpu.run()