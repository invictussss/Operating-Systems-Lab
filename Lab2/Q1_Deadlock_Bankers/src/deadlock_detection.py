def detect_deadlock(allocation, request, available):
    processes = len(allocation)
    resources = len(available)

    work = available.copy()
    finish = [False] * processes

    for i in range(processes):
        if sum(allocation[i]) == 0:
            finish[i] = True

    while True:
        found = False

        for i in range(processes):
            if not finish[i]:
                possible = all(
                    request[i][j] <= work[j]
                    for j in range(resources)
                )

                if possible:
                    for j in range(resources):
                        work[j] += allocation[i][j]

                    finish[i] = True
                    found = True

        if not found:
            break

    deadlocked = [
        i for i in range(processes) if not finish[i]
    ]

    return deadlocked


def main():
    allocation = [
        [1, 0],
        [0, 1]
    ]

    request = [
        [0, 1],
        [1, 0]
    ]

    available = [0, 0]

    print("DEADLOCK DETECTION")

    print("\nAllocation Matrix:", allocation)
    print("Request Matrix:", request)
    print("Available Resources:", available)

    deadlocked = detect_deadlock(
        allocation, request, available
    )

    if deadlocked:
        print("\nDeadlock detected!")
        print("Deadlocked Processes:", deadlocked)

        print("\n--- Recovery Started ---")

        victim = deadlocked[-1]

        print(f"Terminating P{victim} to recover resources.")

        for j in range(len(available)):
            available[j] += allocation[victim][j]
            allocation[victim][j] = 0
            request[victim][j] = 0

        print("Updated Available Resources:", available)

        remaining = detect_deadlock(
            allocation, request, available
        )

        if not remaining:
            print("\nDeadlock successfully recovered!")
            print("All remaining processes can proceed.")
        else:
            print("\nDeadlock still exists:", remaining)

    else:
        print("\nNo deadlock detected.")


if __name__ == "__main__":
    main()
