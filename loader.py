# loader.py

import re
from typing import Tuple, List
from utils import Instruction, parse_instruction_line
from memory import Memory, MemoryAccessError, Mode

def load_program(filename: str) -> Memory:
    """
    Reads a GTU-C312 program file with sections:
      Begin Data Section
        <addr> <value> [#comment]
        ...
      End Data Section
      Begin Instruction Section
        <addr> <OPCODE> [operands...] [#comment]
        ...
      End Instruction Section

    Populates a Memory object:
      - data_segment with (addr -> value)
      - instruction_segment with (addr -> Instruction)
      - registers:
         PC (0), SP (1), SYSTEM_CALL_RESULT (2) default 0 if not set in data
         INSTR_COUNT (3) = 0
         INSTRUCTION_BASE (4) = min instruction addr
         INSTRUCTION_LIMIT (5) = max instruction addr
         STACK_BASE (6) = data_limit + 1
         STACK_LIMIT (7) = memory.size - 1
         DATA_BASE (8) = min data addr (≥0)
         DATA_LIMIT (9) = max data addr
         THREAD_ID (10) = 0
         MODE (11) = Mode.KERNEL.value
    """
    mem = Memory()
    # Track data/instruction addresses
    data_addrs = []
    instr_addrs = []

    in_data = False
    in_instr = False

    with open(filename, 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            # Skip empty lines
            if not line:
                continue
            # Section markers
            if re.match(r"^\s*Begin Data Section", line, re.IGNORECASE):
                in_data = True
                continue
            if re.match(r"^\s*End Data Section", line, re.IGNORECASE):
                in_data = False
                continue
            if re.match(r"^\s*Begin Instruction Section", line, re.IGNORECASE):
                in_instr = True
                continue
            if re.match(r"^\s*End Instruction Section", line, re.IGNORECASE):
                in_instr = False
                continue

            if in_data:
                # Remove comment
                parts = line.split('#', 1)[0].strip().split()
                if len(parts) < 2:
                    continue
                addr = int(parts[0])
                value = int(parts[1])
                mem.data_segment[addr] = value
                data_addrs.append(addr)

            elif in_instr:
                # Each instruction line: "<addr> <rest>"
                # Split off comment, then parse
                code_part = line.split('#', 1)[0].strip()
                tokens = code_part.split()
                if len(tokens) < 2:
                    continue
                addr = int(tokens[0])
                instr_text = " ".join(tokens[1:])
                instr = parse_instruction_line(instr_text)
                mem.instruction_segment[addr] = instr
                instr_addrs.append(addr)

    # Set register defaults if not present
    # Ensure PC (0) and SP (1) exist in data_segment; default to 0
    if 0 not in mem.data_segment:
        mem.data_segment[0] = 0
    if 1 not in mem.data_segment:
        mem.data_segment[1] = 0
    # SYSTEM_CALL_RESULT (2) and INSTR_COUNT (3) default 0
    mem.data_segment.setdefault(2, 0)
    mem.data_segment.setdefault(3, 0)

    return mem