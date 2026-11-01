from dataclasses import dataclass
from collections import deque
import threading
import os
import time


@dataclass
class Process:
    name: str
    arrival: int
    burst: int
    remaining: int = 0
    completion: int = 0
    turnaround: int = 0
    waiting: int = 0

    def __post_init__(self):
        self.remaining = self.burst


def round_robin(processes, quantum):
    jobs = sorted(processes, key=lambda p: (p.arrival, p.name))
    queue = deque()

    time_now = 0
    index = 0
    completed = []

    while index < len(jobs) or queue:

        if not queue:
            time_now = max(time_now, jobs[index].arrival)

        while index < len(jobs) and jobs[index].arrival <= time_now:
            queue.append(jobs[index])
            index += 1

        current = queue.popleft()

        run = min(quantum, current.remaining)
        current.remaining -= run
        time_now += run

        while index < len(jobs) and jobs[index].arrival <= time_now:
            queue.append(jobs[index])
            index += 1

        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time_now
            completed.append(current)

    for p in completed:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst

    return completed


def show_metrics(processes):
    print("\n" + "=" * 60)
    print("ROUND ROBIN PROCESS METRICS")
    print("=" * 60)

    print("Process\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        print(
            f"{p.name}\t{p.arrival}\t{p.burst}\t"
            f"{p.completion}\t{p.turnaround}\t{p.waiting}"
        )

    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    avg_wt = sum(p.waiting for p in processes) / len(processes)

    print(f"\nAverage Turnaround Time : {avg_tat:.2f}")
    print(f"Average Waiting Time    : {avg_wt:.2f}")


def worker(name, lock):
    with lock:
        print(f"Thread {name} started")

    time.sleep(0.2)

    with lock:
        print(f"Thread {name} completed")


def thread_demo():
    print("\n" + "=" * 60)
    print("THREAD DEMONSTRATION")
    print("=" * 60)

    lock = threading.Lock()

    t1 = threading.Thread(target=worker, args=("A", lock))
    t2 = threading.Thread(target=worker, args=("B", lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both threads have finished.")


def ipc_demo():
    print("\n" + "=" * 60)
    print("PIPE IPC DEMONSTRATION")
    print("=" * 60)

    read_end, write_end = os.pipe()

    message = b"Message sent through pipe"

    os.write(write_end, message)
    os.close(write_end)

    received = os.read(read_end, 100).decode()
    os.close(read_end)

    print("Sender : Parent process")
    print("Receiver: Child-side reader")
    print("Data received:", received)


process_data = [
    Process("P1", 0, 7),
    Process("P2", 2, 4),
    Process("P3", 4, 1),
    Process("P4", 5, 4)
]

result = round_robin(process_data, 2)

show_metrics(result)
thread_demo()
ipc_demo()

print("\nAll demonstrations completed successfully.")
from dataclasses import dataclass
from collections import deque
import threading
import os
import time


@dataclass
class Process:
    name: str
    arrival: int
    burst: int
    remaining: int = 0
    completion: int = 0
    turnaround: int = 0
    waiting: int = 0

    def __post_init__(self):
        self.remaining = self.burst


def round_robin(processes, quantum):
    jobs = sorted(processes, key=lambda p: (p.arrival, p.name))
    queue = deque()

    time_now = 0
    index = 0
    completed = []

    while index < len(jobs) or queue:

        if not queue:
            time_now = max(time_now, jobs[index].arrival)

        while index < len(jobs) and jobs[index].arrival <= time_now:
            queue.append(jobs[index])
            index += 1

        current = queue.popleft()

        run = min(quantum, current.remaining)
        current.remaining -= run
        time_now += run

        while index < len(jobs) and jobs[index].arrival <= time_now:
            queue.append(jobs[index])
            index += 1

        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time_now
            completed.append(current)

    for p in completed:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst

    return completed


def show_metrics(processes):
    print("\n" + "=" * 60)
    print("ROUND ROBIN PROCESS METRICS")
    print("=" * 60)

    print("Process\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        print(
            f"{p.name}\t{p.arrival}\t{p.burst}\t"
            f"{p.completion}\t{p.turnaround}\t{p.waiting}"
        )

    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    avg_wt = sum(p.waiting for p in processes) / len(processes)

    print(f"\nAverage Turnaround Time : {avg_tat:.2f}")
    print(f"Average Waiting Time    : {avg_wt:.2f}")


def worker(name, lock):
    with lock:
        print(f"Thread {name} started")

    time.sleep(0.2)

    with lock:
        print(f"Thread {name} completed")


def thread_demo():
    print("\n" + "=" * 60)
    print("THREAD DEMONSTRATION")
    print("=" * 60)

    lock = threading.Lock()

    t1 = threading.Thread(target=worker, args=("A", lock))
    t2 = threading.Thread(target=worker, args=("B", lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both threads have finished.")


def ipc_demo():
    print("\n" + "=" * 60)
    print("PIPE IPC DEMONSTRATION")
    print("=" * 60)

    read_end, write_end = os.pipe()

    message = b"Message sent through pipe"

    os.write(write_end, message)
    os.close(write_end)

    received = os.read(read_end, 100).decode()
    os.close(read_end)

    print("Sender : Parent process")
    print("Receiver: Child-side reader")
    print("Data received:", received)


process_data = [
    Process("P1", 0, 7),
    Process("P2", 2, 4),
    Process("P3", 4, 1),
    Process("P4", 5, 4)
]

result = round_robin(process_data, 2)

show_metrics(result)
thread_demo()
ipc_demo()

print("\nAll demonstrations completed successfully.")
