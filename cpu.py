# cpu.py

from typing import List, Union, NamedTuple
from memory import Memory, MemoryAccessError
from utils import Instruction

class CPU:
    def __init__(
        self,
        memory: Memory,
    ):
        self.memory = memory
        self.halted = False
        self.instr_count = 0

    def get_pc(self) -> int:
        return self.memory.registers.PC()

    def set_pc(self, value: int) -> None:
        self.memory.write_data(0, value)

    def get_sp(self) -> int:
        return self.memory.registers.SP()

    def set_sp(self, value: int) -> None:
        self.memory.write_data(1, value)


    def fetch(self) -> Instruction:
        return self.memory.read_instruction(self.get_pc())

    def execute(self, instr: Instruction) -> bool:
        opcode = instr.opcode
        ops = instr.operands

        if opcode == "SET":
            self.set_pc(self.get_pc() + 1)
            B = int(ops[0]); A = int(ops[1])
            self.memory.write_data(A, B)

        elif opcode == "CPY":
            self.set_pc(self.get_pc() + 1)
            A1 = int(ops[0]); A2 = int(ops[1])
            val = self.memory.read_data(A1)
            self.memory.write_data(A2, val)


        elif opcode == "CPYI":
            self.set_pc(self.get_pc() + 1)
            A1 = int(ops[0]); A2 = int(ops[1])
            addr = self.memory.read_data(A1)
            val = self.memory.read_data(addr)
            self.memory.write_data(A2, val)

        elif opcode == "CPYI2":
            self.set_pc(self.get_pc() + 1)
            A1 = int(ops[0]); A2 = int(ops[1])
            addr = self.memory.read_data(A1)
            val = self.memory.read_data(A2)
            self.memory.write_data(addr, val)

        elif opcode == "ADD":
            self.set_pc(self.get_pc() + 1)
            A = int(ops[0]); B = int(ops[1])
            old = self.memory.read_data(A)
            self.memory.write_data(A, old + B)

        elif opcode == "ADDI":
            self.set_pc(self.get_pc() + 1)
            A1 = int(ops[0]); A2 = int(ops[1])
            v1 = self.memory.read_data(A1)
            indirect_addr = self.memory.read_data(A2)
            v2 = self.memory.read_data(indirect_addr)
            self.memory.write_data(A1, v1 + v2)


        elif opcode == "SUBI":
            self.set_pc(self.get_pc() + 1)
            A1 = int(ops[0]); A2 = int(ops[1])
            v1 = self.memory.read_data(A1)
            indirect_addr = self.memory.read_data(A2)
            v2 = self.memory.read_data(indirect_addr)
            self.memory.write_data(A2, v1 - v2)

        elif opcode == "CALL":
                # CALL C: push return address, jump to C
                C = int(ops[0])
                ret_addr = self.get_pc() + 1
                self.set_sp(self.get_sp() - 1)
                self.memory.write_data(self.get_sp(), ret_addr)
                self.set_pc(C)

        elif opcode == "RET":
            # RET: pop return address into PC
            ret_addr = self.memory.read_data(self.get_sp())
            self.set_sp(self.get_sp() + 1)
            self.set_pc(ret_addr)

        elif opcode == "JIF":
            A = int(ops[0]); C = int(ops[1])
            if self.memory.read_data(A) <= 0:
                self.set_pc(C)
            else:
                self.set_pc(self.get_pc() + 1)

        elif opcode == "PUSH":
            self.set_pc(self.get_pc() + 1)
            A = int(ops[0])
            self.set_sp(self.get_sp() - 1)
            self.memory.write_data(self.get_sp(), A)

        elif opcode == "POP":
            self.set_pc(self.get_pc() + 1)
            A = int(ops[0])
            addr = self.memory.read_data(self.get_sp())
            self.memory.write_data(A, addr)
            self.set_sp(self.get_sp() + 1)

        elif opcode == "SYSCALL":
            call_type = ops[0]
            self.memory.data_segment[11] = 0 #switch kernel mode
            PC = self.get_pc()
            self.memory.write_data(12, PC + 1)
            if call_type == "PRN":
                A = ops[1]
                val = self.memory.read_data(A)
                print(val)
                self.set_pc(900)

            elif call_type == "YIELD":
                self.set_pc(700)

            elif call_type == "HLT":
                self.set_pc(800)

            else:
                raise ValueError(f"Unknown SYSCALL type: {call_type}")


        elif opcode == "HLT":
            self.halted = True
            return False
        
        elif opcode == "USER":
            A = int(ops[0])
            addr = self.memory.read_data(A)
            pc_addr = self.memory.read_data(addr)
            self.set_pc(pc_addr)
            self.memory.data_segment[11] = 1 #switch user mode


        else:
            raise ValueError(f"Unknown opcode: {opcode}")

        # Update instruction count
        self.instr_count += 1
        for i in range(0, 11):
            thread_table_entry_base = 200 + i * 20
            num_of_instr_count_table_idx = thread_table_entry_base + 1
            self.memory.data_segment[num_of_instr_count_table_idx] = self.instr_count
            
        self.memory.write_data(3, self.instr_count)

        thread_table_entry_base = 200 + self.memory.registers.THREAD_ID() * 20
        num_of_execution_count_table_idx = thread_table_entry_base + 2
        self.memory.data_segment[num_of_execution_count_table_idx] += 1

        return True

    def run(self) -> None:
        while not self.halted:
            instr = self.fetch()
            _ = self.execute(instr)