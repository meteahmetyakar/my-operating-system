#utils.py
# Instruction representation using NamedTuple from built-in typing module
from typing import NamedTuple, List, Union

class Instruction(NamedTuple):
    opcode: str
    operands: List[Union[int, str]]

    def __str__(self) -> str:
        operands_str = ', '.join(str(op) for op in self.operands)
        return f"{self.opcode} {operands_str}"

def parse_instruction_line(line: str) -> Instruction:
    """
    Parses a single line of GTU-C312 assembly (without the line number) into an Instruction.
    - Removes comments starting with '#'
    - Splits the remaining content into opcode and operands
    - Converts numeric operand strings to int, leaves others as str
    """
    # Remove comments and strip whitespace
    line = line.split('#')[0].strip()
    if not line:
        raise ValueError("Empty or comment-only line cannot be parsed.")

    parts = line.split()
    opcode = parts[0].upper()  # Normalize opcode to uppercase
    operands: List[Union[int, str]] = []

    for op in parts[1:]:
        try:
            operands.append(int(op))
        except ValueError:
            operands.append(op)

    return Instruction(opcode, operands)
