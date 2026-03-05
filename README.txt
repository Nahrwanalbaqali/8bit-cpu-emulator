Custom 8-Bit CPU Emulator & Assembler
A full-stack low-level system simulation written in Python. This project bridges hardware architecture and software engineering by emulating a von Neumann CPU cycle and providing a custom compiler.

🚀 Features
The Hardware (`cpu.py`):** Simulates RAM (256 bytes), a Program Counter, General Purpose Registers (A & B), and a Fetch-Decode-Execute cycle.
The Software (`assembler.py`):** A custom toolchain that parses human-readable assembly instructions and compiles them into raw machine code (hex).
Instruction Set Architecture (ISA):** Supports Memory Loading, Register Arithmetic, Memory Storing, and Unconditional Branching (JUMP).

🛠️ Quick Start
1. Clone the repository.
2. Open `assembler.py` and modify the `my_program_text` array to write your own assembly code.
3. Run `python assembler.py`. The console will output the compiled machine code and boot the CPU to execute it.
