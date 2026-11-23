# Operating Systems Lab

A collection of practical implementations and experiments covering important concepts of Operating Systems. This repository contains solutions for Lab 1, Lab 2, Lab 3, and Lab 4, implemented using Python and C.

## 👨‍💻 Author

- **Name:** Vikash Kumar
- **Roll Number:** 2401730185
- **Course:** B.Tech CSE (AI & ML)
- **University:** K.R. Mangalam University, Sohna, Gurugram

## 📚 Repository Overview

| Lab | Main Topics | Questions |
|---|---|---:|
| Lab 1 | System Calls, CPU Scheduling, Threads and IPC | 4 |
| Lab 2 | Deadlocks, Threads, Race Conditions and Synchronization | 4 |
| Lab 3 | Device Management, Memory Management and Disk Scheduling | 5 |
| Lab 4 | File Operations, File Allocation, Directories and Free-Space Management | 4 |

---

# 📁 Complete Repository Structure

```text
Operating-Systems-Lab/
│
├── .gitignore
│
├── Lab1/
│   ├── Q1_System_Calls/
│   │   └── src/
│   │       ├── child_record.txt
│   │       ├── system_calls
│   │       └── system_calls.c
│   │
│   ├── Q2_FCFS_SJF/
│   │   └── src/
│   │       └── scheduling.py
│   │
│   ├── Q3_Priority_Round_Robin/
│   │   └── src/
│   │       └── priority_rr.py
│   │
│   └── Q4_Metrics_Threads_IPC/
│       └── src/
│           └── metrics_threads_ipc.py
│
├── Lab2/
│   ├── Q1_Deadlock_Bankers/
│   │   ├── output/
│   │   │   └── controlled_deadlock_output.txt
│   │   └── src/
│   │       ├── banker.py
│   │       ├── controlled_deadlock
│   │       ├── controlled_deadlock.c
│   │       └── deadlock_detection.py
│   │
│   ├── Q2_Thread_Creation/
│   │   ├── output/
│   │   │   └── thread_comparison_output.txt
│   │   └── src/
│   │       └── thread_comparison.py
│   │
│   ├── Q3_Race_Condition/
│   │   ├── output/
│   │   │   └── race_condition_output.txt
│   │   └── src/
│   │       ├── race_condition
│   │       ├── race_condition.c
│   │       └── race_condition.y
│   │
│   └── Q4_Classical_Synchronization/
│       ├── output/
│       │   ├── dining_philosophers_output.txt
│       │   ├── producer_consumer_output.txt
│       │   └── readers_writers_output.txt
│       └── src/
│           ├── dining_philosophers
│           ├── dining_philosophers.c
│           ├── producer_consumer
│           ├── producer_consumer.c
│           ├── readers_writers
│           └── readers_writers.c
│
├── Lab3/
│   ├── Q1_Device_Management/
│   │   ├── output/
│   │   │   └── device_management_output.txt
│   │   └── src/
│   │       └── device_management.py
│   │
│   ├── Q2_Paging_Segmentation/
│   │   ├── output/
│   │   │   └── paging_segmentation_output.txt
│   │   └── src/
│   │       └── paging_segmentation.py
│   │
│   ├── Q3_Demand_Paging/
│   │   ├── output/
│   │   │   └── demand_paging_output.txt
│   │   └── src/
│   │       └── demand_paging.py
│   │
│   ├── Q4_Disk_Scheduling/
│   │   ├── output/
│   │   │   └── disk_scheduling_output.txt
│   │   └── src/
│   │       └── disk_scheduling.py
│   │
│   └── Q5_Contiguous_Allocation/
│       ├── output/
│       │   └── contiguous_allocation_output.txt
│       └── src/
│           └── contiguous_allocation.py
│
├── Lab4/
│   ├── Q1_File_Operations/
│   │   ├── output/
│   │   │   ├── file_operations_output.txt
│   │   │   └── preserved_records.txt
│   │   └── src/
│   │       └── file_operations.py
│   │
│   ├── Q2_File_Allocation/
│   │   ├── output/
│   │   │   └── file_allocation_output.txt
│   │   └── src/
│   │       └── file_allocation.py
│   │
│   ├── Q3_Directory_Structures/
│   │   ├── output/
│   │   │   └── access_directory_output.txt
│   │   └── src/
│   │       └── access_directory.py
│   │
│   └── Q4_Free_Space_Access_Control/
│       ├── output/
│       │   └── free_space_management_output.txt
│       └── src/
│           └── free_space_management.py
│
├── README.md
├── requirements.txt
├── terminal_commands.txt
└── ubuntu_terminal_session.txt
```

---

# 🧪 Lab 1: Process Management and CPU Scheduling

Lab 1 covers process management, system calls, CPU scheduling algorithms, threads, and inter-process communication.

### Q1: System Calls
**File:** `Lab1/Q1_System_Calls/src/system_calls.c`

Topics covered:
- File operations using system calls.
- Process creation using `fork()`.
- Program execution using `execlp()`.
- Process synchronization using `wait()`.
- File handling using `open()`, `read()`, and `write()`.

### Q2: FCFS and SJF Scheduling
**File:** `Lab1/Q2_FCFS_SJF/src/scheduling.py`

Topics covered:
- First Come First Serve (FCFS).
- Shortest Job First (SJF).
- Waiting time.
- Turnaround time.
- CPU scheduling calculations.

### Q3: Priority and Round Robin Scheduling
**File:** `Lab1/Q3_Priority_Round_Robin/src/priority_rr.py`

Topics covered:
- Priority Scheduling.
- Round Robin Scheduling.
- Time Quantum.
- Waiting time and turnaround time.

### Q4: Scheduling Metrics, Threads and IPC
**File:** `Lab1/Q4_Metrics_Threads_IPC/src/metrics_threads_ipc.py`

Topics covered:
- Round Robin scheduling metrics.
- Thread creation and execution.
- Inter-Process Communication (IPC).
- Pipe-based communication.

---

# 🔒 Lab 2: Process Synchronization and Deadlocks

Lab 2 focuses on deadlock handling, multithreading, race conditions, and classical synchronization problems.

### Q1: Deadlock Detection and Banker's Algorithm
**Files:**
- `Lab2/Q1_Deadlock_Bankers/src/banker.py`
- `Lab2/Q1_Deadlock_Bankers/src/deadlock_detection.py`
- `Lab2/Q1_Deadlock_Bankers/src/controlled_deadlock.c`

Topics covered:
- Deadlock concepts.
- Deadlock detection.
- Banker's Algorithm.
- Safe and unsafe states.
- Controlled deadlock demonstration.

### Q2: Thread Creation and Performance
**File:** `Lab2/Q2_Thread_Creation/src/thread_comparison.py`

Topics covered:
- Thread creation.
- Thread execution.
- Multithreading.
- Performance comparison.

### Q3: Race Condition
**Files:**
- `Lab2/Q3_Race_Condition/src/race_condition.c`
- `Lab2/Q3_Race_Condition/src/race_condition.y`

Topics covered:
- Race conditions.
- Shared resources.
- Concurrent execution.
- Synchronization using mutex mechanisms.

### Q4: Classical Synchronization Problems
**C programs:**
- `producer_consumer.c`
- `readers_writers.c`
- `dining_philosophers.c`

Topics covered:
- Producer-Consumer Problem.
- Readers-Writers Problem.
- Dining Philosophers Problem.
- Process synchronization.
- Mutual exclusion and shared resources.

---

# 💾 Lab 3: Memory Management and Disk Management

Lab 3 covers device management, memory allocation, paging, segmentation, demand paging, and disk scheduling.

### Q1: Device Management
**File:** `Lab3/Q1_Device_Management/src/device_management.py`

Topics covered:
- Device management concepts.
- Device allocation and management.
- Input/output device handling.

### Q2: Paging and Segmentation
**File:** `Lab3/Q2_Paging_Segmentation/src/paging_segmentation.py`

Topics covered:
- Paging.
- Segmentation.
- Logical and physical memory concepts.
- Address translation.

### Q3: Demand Paging
**File:** `Lab3/Q3_Demand_Paging/src/demand_paging.py`

Topics covered:
- Demand paging.
- Page faults.
- Page replacement concepts.
- Memory management.

### Q4: Disk Scheduling
**File:** `Lab3/Q4_Disk_Scheduling/src/disk_scheduling.py`

Topics covered:
- Disk scheduling algorithms.
- Disk head movement.
- Seek time calculations.
- Disk access management.

### Q5: Contiguous Allocation
**File:** `Lab3/Q5_Contiguous_Allocation/src/contiguous_allocation.py`

Topics covered:
- Contiguous memory allocation.
- Memory block allocation.
- Memory management techniques.

---

# 📂 Lab 4: File-System Interface and Implementation

Lab 4 focuses on file handling, file allocation techniques, directory structures, and free-space management.

### Q1: File Operations and Sequential Access
**File:** `Lab4/Q1_File_Operations/src/file_operations.py`

Topics covered:
- Creating and opening files.
- Reading and writing records.
- Sequential file access.
- Appending records.
- Renaming and listing files.
- File metadata.
- File deletion and error handling.

### Q2: File Allocation Methods
**File:** `Lab4/Q2_File_Allocation/src/file_allocation.py`

Topics covered:
- Contiguous Allocation.
- Linked Allocation.
- Indexed Allocation.
- Comparison of file allocation techniques.

### Q3: Directory Structures and File Access
**File:** `Lab4/Q3_Directory_Structures/src/access_directory.py`

Topics covered:
- Direct Access.
- Indexed Access.
- Single-Level Directory.
- Two-Level Directory.
- Tree-Structured Directory.

### Q4: Free-Space Management and Access Control
**File:** `Lab4/Q4_Free_Space_Access_Control/src/free_space_management.py`

Topics covered:
- Bitmap-based free-space management.
- File deletion.
- Block release and reuse.
- Read, Write, and Execute permissions.
- File access control.

---

# 🛠️ Technologies Used

- **Python 3:** Algorithm implementation and simulations.
- **C:** System calls, process management, and synchronization.
- **GCC:** C program compilation.
- **Ubuntu Linux / WSL:** Development and execution environment.
- **Git and GitHub:** Version control and project hosting.
- **VS Code:** Code editing and development.

# ⚙️ Requirements

- Ubuntu Linux or Windows Subsystem for Linux (WSL).
- Python 3.
- GCC compiler.
- Git.
- VS Code (optional).

Install the basic development tools on Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip build-essential git
```

Install Python dependencies, if required:

```bash
pip3 install -r requirements.txt
```

# 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/invictussss/Operating-Systems-Lab.git
```

### 2. Open the Project

```bash
cd Operating-Systems-Lab
code .
```

### 3. Run a Python Program

Example:

```bash
python3 Lab1/Q2_FCFS_SJF/src/scheduling.py
```

Another example:

```bash
python3 Lab3/Q4_Disk_Scheduling/src/disk_scheduling.py
```

### 4. Compile and Run a C Program

Example:

```bash
cd Lab1/Q1_System_Calls/src
gcc system_calls.c -o system_calls
./system_calls
```

For C programs that use POSIX threads, compile with the `-pthread` option where required.

# 📄 Output Files

The repository contains saved output files for the practical implementations.

Output files are stored in the respective `output/` directories wherever included in the repository.

These files provide execution evidence and help verify the program results.

# 🎯 Learning Outcomes

Through these practical assignments, the repository demonstrates:

- Understanding of operating system fundamentals.
- Implementation of CPU scheduling algorithms.
- Understanding of process and thread management.
- Deadlock detection and avoidance.
- Process synchronization and race-condition handling.
- Memory management and disk scheduling.
- File-system operations and allocation techniques.
- Practical programming using Python and C in Linux.

# 🔗 GitHub Repository

**Repository:** https://github.com/invictussss/Operating-Systems-Lab

---

**Operating Systems Lab | B.Tech CSE (AI & ML)**

**K.R. Mangalam University, Sohna, Gurugram**
