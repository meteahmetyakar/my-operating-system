# simulator.py

import sys
from loader import load_program
from cpu import CPU
from memory import MemoryAccessError

def print_memory(mem, stream):
    """Print full memory dump to the given stream."""
    for line in mem.dump_memory().splitlines():
        print(line, file=stream)

def print_thread_table(mem, stream):
    """Print only the thread-table entries (200..200+11*20) to the given stream."""
    print("=== Thread Table ===", file=stream)
    for i in range(11):  # 0 = OS, 1..10 = threads
        base = 200 + i*20
        fields = {
            "threadID":       mem.data_segment.get(base+0, 0),
            "instr_count":    mem.data_segment.get(base+1, 0),
            "exec_count":     mem.data_segment.get(base+2, 0),
            "state":          mem.data_segment.get(base+3, 0),
            "PC":             mem.data_segment.get(base+4, 0),
            "SP":             mem.data_segment.get(base+5, 0),
            "instr_base":     mem.data_segment.get(base+6, 0),
            "instr_limit":    mem.data_segment.get(base+7, 0),
            "stack_base":     mem.data_segment.get(base+8, 0),
            "stack_limit":    mem.data_segment.get(base+9, 0),
            "data_base":      mem.data_segment.get(base+10,0),
            "data_limit":     mem.data_segment.get(base+11,0),
            "mode":           mem.data_segment.get(base+12,0),
            "will_schedule":  mem.data_segment.get(base+13,0),
            "blocked_remain": mem.data_segment.get(base+14,0),
        }
        print(f"Entry {i} @ {base}: {fields}", file=stream)
    print("====================", file=stream)

def main():
    if len(sys.argv) != 4 or sys.argv[2] != "-D":
        print("Usage: python simulator.py <program_filename.asm> -D <mode>")
        print("Modes:")
        print(" 0 : run, dump memory AFTER halt")
        print(" 1 : dump memory AFTER each instruction")
        print(" 2 : dump memory AFTER each instruction, pause for Enter")
        print(" 3 : dump thread table AFTER each syscall or context switch")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        mem = load_program(filename)
    except Exception as e:
        print(f"Error loading '{filename}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        debug = int(sys.argv[3])
    except ValueError:
        print("Debug mode must be an integer 0–3", file=sys.stderr)
        sys.exit(1)

    cpu = CPU(mem)

    print(f"=== Running '{filename}' (debug={debug}) ===")
    try:
        if debug == 0:
            cpu.run()
            print_memory(mem, sys.stderr)

        elif debug == 1:
            while not cpu.halted:
                instr = cpu.fetch()
                cpu.execute(instr)
                print(instr)
                print_memory(mem, sys.stderr)

        elif debug == 2:
            while not cpu.halted:
                instr = cpu.fetch()
                cpu.execute(instr)
                print(instr)
                print_memory(mem, sys.stderr)
                input("Press Enter to continue...")

        elif debug == 3:
            while not cpu.halted:
                instr = cpu.fetch()
                cpu.execute(instr)
                if instr.opcode in ("SYSCALL", "USER"):
                    print(instr)
                    print_thread_table(mem, sys.stderr)

        else:
            print(f"Unknown debug mode: {debug}", file=sys.stderr)
            sys.exit(1)

    except MemoryAccessError as e:
        print(f"\nSimulation halted due to memory error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"\nSimulation halted due to unexpected error: {e}", file=sys.stderr)

    if debug in (1, 2, 3):
        print("\n=== Final Memory Dump ===", file=sys.stderr)
        print_memory(mem, sys.stderr)

if __name__ == "__main__":
    main()
