#memory.py
from typing import List, Dict, Union
from utils import Instruction
from enum import Enum

class MemoryAccessError(Exception):
    """Special exception to be thrown on memory access errors."""
    pass


class Mode(Enum):
    KERNEL = 0
    USER = 1


class Memory:
    """
    Class that holds data and instruction segments. Controls memory access permission according to the CPU's mode.
    """
    def __init__(self, size: int = 11000):
        self.size = size
        # Dictionaries: sparse storage. Unassigned addresses return a default value of 0. 
        self.instruction_segment: Dict[int, Instruction] = {}
        self.data_segment: Dict[int, int] = {}
        self.registers = self.Registers(self)

    class Registers:
        def __init__(self, memory: 'Memory'):
            self.memory = memory

        def PC(self) -> int:
            return self.memory.data_segment.get(0, 0)

        def SP(self) -> int:
            return self.memory.data_segment.get(1, 0)

        def SYSTEM_CALL_RESULT(self) -> int:
            return self.memory.data_segment.get(2, 0)

        def INSTR_COUNT(self) -> int:
            return self.memory.data_segment.get(3, 0)

        def INSTRUCTION_BASE(self) -> int:
            return self.memory.data_segment.get(4, 0)

        def INSTRUCTION_LIMIT(self) -> int:
            return self.memory.data_segment.get(5, 0)

        def STACK_BASE(self) -> int:
            return self.memory.data_segment.get(6, 0)

        def STACK_LIMIT(self) -> int:
            return self.memory.data_segment.get(7, 0)

        def DATA_BASE(self) -> int:
            return self.memory.data_segment.get(8, 0)

        def DATA_LIMIT(self) -> int:
            return self.memory.data_segment.get(9, 0)

        def THREAD_ID(self) -> int:
            return self.memory.data_segment.get(10, 0)

        def MODE(self) -> int:
            return self.memory.data_segment.get(11, 0)
        
        def TEMP_PC(self) -> int:
            return self.memory.data_segment.get(12, 0)
        
        def HLT_COUNTER(self) -> int:
            return self.memory.data_segment.get(13, 0)

        def REG_BASE(self) -> int:
            return 4
        
        def REG_LIMIT(self) -> int:
            return 20

        #14-20 reserved

    def read_instruction(self, address: int) -> Instruction:
        """
        Reads an instruction from the instruction segment.
        - MemoryAccessError if the address is out of bounds.
        - KeyError if there is no instruction at the address.
        """
        if address < 0 or address >= self.size:
            raise MemoryAccessError(f"Instruction address {address} out of bounds.")
        
        if address not in self.instruction_segment:
            raise KeyError(f"No instruction at address {address}.")
        
        instr_segment_violation = not (self.registers.INSTRUCTION_BASE() <= address <= self.registers.INSTRUCTION_LIMIT())
        is_user_mode = self.registers.MODE() == Mode.USER.value

        if instr_segment_violation and is_user_mode:
            raise MemoryAccessError("Segmentation Fault")

        return self.instruction_segment[address]

    def write_instruction(self, address: int, instr: Instruction) -> None:
        """
        Writes an instruction to the instruction segment.
        - MemoryAccessError if address is out of bounds.
        """
        if address < 0 or address >= self.size:
            raise MemoryAccessError(f"Instruction address {address} out of bounds.")
        self.instruction_segment[address] = instr

    def read_data(self, address: int) -> int:
        """
        Reads value from data segment.
        - MemoryAccessError if address is out of bounds.
        - Throws access violation if USER in CPU mode and address < 1000.
        - Returns 0 for undefined addresses.
        """
        requires_kernel_mode = self.registers.REG_BASE() <= address <= self.registers.REG_LIMIT()
        
        user_accessible_registers = (0 <= address <= 4)
        data_segment_bound = (self.registers.DATA_BASE() <= address <= self.registers.DATA_LIMIT())

        data_segment_violation = not user_accessible_registers and not data_segment_bound

        is_user_mode = self.registers.MODE() == Mode.USER.value

        if requires_kernel_mode and is_user_mode:
            raise MemoryAccessError("Segmentation Fault: Kernel Priviliged Area")

        if data_segment_violation and is_user_mode:
            raise MemoryAccessError("Segmentation Fault: Data Segment Violation")

        return self.data_segment.get(address, 0)

    def write_data(self, address: int, value: int) -> None:
        """
        Writes value to data segment.
        - If address is out of bounds, MemoryAccessError.
        - If USER in CPU mode and address < 1000, throws access violation.
        """
        requires_kernel_mode = self.registers.REG_BASE() <= address <= self.registers.REG_LIMIT()
        
        user_accessible_registers = (0 <= address <= 4)
        data_segment_bound = (self.registers.DATA_BASE() <= address <= self.registers.DATA_LIMIT())
        
        data_segment_violation = not user_accessible_registers and not data_segment_bound

        is_user_mode = self.registers.MODE() == Mode.USER.value

        if requires_kernel_mode and is_user_mode:
            raise MemoryAccessError("Segmentation Fault: Kernel Priviliged Area")

        if data_segment_violation and is_user_mode:
            raise MemoryAccessError("Segmentation Fault: Data Segment Violation")
        

        self.data_segment[address] = value

    def dump_memory(self) -> str:
        """
        Returns both the data segment and the command segment line by line.
        """
        lines: List[str] = []
        lines.append("=== Data Segment ===")
        for addr in sorted(self.data_segment.keys()):
            lines.append(f"{addr}: {self.data_segment[addr]}")
        lines.append("=== Instruction Segment ===")
        for addr in sorted(self.instruction_segment.keys()):
            instr = self.instruction_segment[addr]
            ops_str = " ".join(str(op) for op in instr.operands)
            lines.append(f"{addr}: {instr.opcode} {ops_str}")
        return "\n".join(lines)

    
