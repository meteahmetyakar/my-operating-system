# 📌 CPU & OS & Cooperative Multithreading Simulator

A Python-based simulator of a custom CPU and cooperative multithreading OS with syscall-driven scheduling.

---

## 📖 Introduction

This project implements a full-stack simulation of a simple operating system on the CPU in Python. Key components:
- **Loader** (`loader.py`): loads `.asm` into memory
- **Memory** (`memory.py`): sparse dict with base/limit protection
- **CPU** (`cpu.py`): fetch-decode-execute and syscalls
- **OS Assembly** (`os.asm`): kernel, scheduler, and thread routines
- **Simulator** (`simulator.py`): CLI with debug modes

---

## 🏗️ Architecture

- **Project Architecture**
<img src="https://github.com/meteahmetyakar/my-operating-system/blob/main/images/system-architecture.png"/>

1. **Simulator** invokes **Loader** with an `.asm` file.  
2. **Loader** parses data & instruction sections via `utils.py`.  
3. **Loader** populates **Memory** and sets registers/segments.  
4. **Simulator** runs **CPU** cycles: executes instructions, handles syscalls, and interfaces with **OS**.  

---

- **CPU Instruction Set**
<img src="https://github.com/meteahmetyakar/my-operating-system/blob/main/images/instruction-set.png"/>

- **Memory Layout**
<img src="https://github.com/meteahmetyakar/my-operating-system/blob/main/images/memory-layout.png"/>

- **Thread Table Structure**
<img src="https://github.com/meteahmetyakar/my-operating-system/blob/main/images/thread-table.png"/>


---

## 🛠️ Installation

```bash
git clone https://github.com/meteahmetyakar/my-operating-system.git
cd my-operating-system
```

---

## ▶️ Usage

```bash
# Normal execution
python simulator.py os.asm

# With debug (-D 0–3)
python simulator.py -D 2 os.asm
```

**Debug modes**:  
- 0: full run  
- 1: dump memory after each instruction  
- 2: step-and-pause per instruction  
- 3: dump thread table on syscalls/context switches  

---

## 🗄️ File Overview

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `loader.py`        | Parses assembly and initializes memory       |
| `memory.py`        | Implements segments, base/limit checks       |
| `cpu.py`           | CPU ISA: SET, ADD, JIF, PUSH/POP, SYSCALL    |
| `utils.py`         | Assembly parsing helpers                     |
| `simulator.py`     | CLI entry, debug-mode orchestration          |
| `os.asm`           | Kernel: scheduler, syscalls, thread code     |

---

## 🔢 Registers & Segments

- **Registers (0–3)**: PC, SP, SYSCALL_RESULT, INSTR_COUNT  
- **Segments (4–9)**: instr_base/limit, stack_base/limit, data_base/limit  
- **Thread/Mode (10–11)**: THREAD_ID, MODE (0=kernel,1=user)  
- **Temp/Halt (12–13)**: saved_PC, halted_count  

---

## 🗂️ Thread Table (200–419)

Each 20-word slot stores:
`thread_id`, `instr_count`, `exec_count`, `state` (0=ready,1=blocked,2=running),  
`PC`, `SP`, instr bounds, stack bounds, data bounds, `mode`, `will_schedule`,  
`blocked_remain`, reserved…  

---

## 📜 OS Assembly (`os.asm`)

- **Init**: set kernel mode, clear counters, init thread table  
- **Scheduler**: round-robin over threads, skip blocked/halted  
- **Syscalls**:  
  - `PRN`: print & block 100 instr  
  - `YIELD`: reschedule  
  - `HLT`: mark halted  
- **Threads**:  
  - 1: print 1..N  
  - 2: linear search  
  - 3: bubble-like sort  
  - 4–10: immediate `HLT`  

---

## 🤖 Scheduling & Syscalls

- Cooperative multitasking: threads call `YIELD` or `HLT`.  
- Blocked threads resume when `INSTR_COUNT` ≥ `blocked_remain`.  

---

## ✅ Conclusion

This simulator provides hands-on experience with CPU internals, memory protection, and cooperative thread scheduling, all implemented in Python.

