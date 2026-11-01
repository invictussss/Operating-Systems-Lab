from dataclasses import dataclass


@dataclass
class Process:
    name: str
    arrival: int
    burst: int
    completion: int = 0
    turnaround: int = 0
    waiting: int = 0


def calculate_times(processes):
    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst


def fcfs(processes):
    order = sorted(processes, key=lambda p: (p.arrival, p.name))
    time = 0

    for p in order:
        if time < p.arrival:
            time = p.arrival

        time += p.burst
        p.completion = time

    calculate_times(order)
    return order


def sjf(processes):
    pending = processes.copy()
    completed = []
    time = 0

    while pending:
        ready = [p for p in pending if p.arrival <= time]

        if not ready:
            time = min(p.arrival for p in pending)
            continue

        current = min(
            ready,
            key=lambda p: (p.burst, p.arrival, p.name)
        )

        time += current.burst
        current.completion = time

        completed.append(current)
        pending.remove(current)

    calculate_times(completed)
    return completed


def show_result(title, processes):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)

    print("Process\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        print(
            f"{p.name}\t{p.arrival}\t{p.burst}\t"
            f"{p.completion}\t{p.turnaround}\t{p.waiting}"
        )

    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    avg_wt = sum(p.waiting for p in processes) / len(processes)

    print(f"\nAverage TAT = {avg_tat:.2f}")
    print(f"Average WT  = {avg_wt:.2f}")


data = [
    Process("P1", 0, 7),
    Process("P2", 2, 4),
    Process("P3", 4, 1),
    Process("P4", 5, 4)
]

fcfs_result = fcfs([
    Process(p.name, p.arrival, p.burst) for p in data
])

sjf_result = sjf([
    Process(p.name, p.arrival, p.burst) for p in data
])

show_result("FCFS Scheduling", fcfs_result)
show_result("SJF Scheduling", sjf_result)
