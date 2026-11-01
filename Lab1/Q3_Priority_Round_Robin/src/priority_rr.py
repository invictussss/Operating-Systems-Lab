from dataclasses import dataclass
from collections import deque


@dataclass
class Process:
    name: str
    arrival: int
    burst: int
    priority: int
    remaining: int = 0
    completion: int = 0
    turnaround: int = 0
    waiting: int = 0

    def __post_init__(self):
        self.remaining = self.burst


def calculate_times(processes):
    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst


def priority_scheduling(processes):
    pending = processes.copy()
    result = []
    time = 0

    while pending:
        ready = [p for p in pending if p.arrival <= time]

        if not ready:
            time = min(p.arrival for p in pending)
            continue

        current = min(
            ready,
            key=lambda p: (p.priority, p.arrival, p.name)
        )

        time += current.burst
        current.completion = time

        result.append(current)
        pending.remove(current)

    calculate_times(result)
    return result


def round_robin(processes, quantum):
    jobs = sorted(processes, key=lambda p: (p.arrival, p.name))
    queue = deque()

    time = 0
    index = 0
    finished = []

    while index < len(jobs) or queue:

        if not queue:
            time = max(time, jobs[index].arrival)

        while index < len(jobs) and jobs[index].arrival <= time:
            queue.append(jobs[index])
            index += 1

        current = queue.popleft()

        run_time = min(quantum, current.remaining)
        current.remaining -= run_time
        time += run_time

        while index < len(jobs) and jobs[index].arrival <= time:
            queue.append(jobs[index])
            index += 1

        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time
            finished.append(current)

    calculate_times(finished)
    return finished


def display(title, processes):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print("Process\tAT\tBT\tP\tCT\tTAT\tWT")

    for p in processes:
        print(
            f"{p.name}\t{p.arrival}\t{p.burst}\t{p.priority}\t"
            f"{p.completion}\t{p.turnaround}\t{p.waiting}"
        )

    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    avg_wt = sum(p.waiting for p in processes) / len(processes)

    print(f"\nAverage TAT = {avg_tat:.2f}")
    print(f"Average WT  = {avg_wt:.2f}")


data = [
    Process("P1", 0, 7, 2),
    Process("P2", 2, 4, 1),
    Process("P3", 4, 1, 3),
    Process("P4", 5, 4, 2)
]

priority_result = priority_scheduling([
    Process(p.name, p.arrival, p.burst, p.priority)
    for p in data
])

rr_result = round_robin([
    Process(p.name, p.arrival, p.burst, p.priority)
    for p in data
], 2)

display("Priority Scheduling", priority_result)
display("Round Robin (Quantum = 2)", rr_result)
