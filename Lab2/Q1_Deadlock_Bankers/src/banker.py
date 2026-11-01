def calculate_need(maximum, allocation):
    need = []

    for i in range(len(maximum)):
        row = []

        for j in range(len(maximum[i])):
            row.append(maximum[i][j] - allocation[i][j])

        need.append(row)

    return need


def display_matrix(title, matrix):
    print("\n" + title)

    for i, row in enumerate(matrix):
        print(f"P{i}: {row}")


def safety_algorithm(allocation, need, available):
    n = len(allocation)
    m = len(available)

    work = available.copy()
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                possible = True

                for j in range(m):
                    if need[i][j] > work[j]:
                        possible = False
                        break

                if possible:
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            break

    if len(safe_sequence) == n:
        print("\nSystem is in a SAFE state.")
        print("Safe Sequence:", end=" ")

        for p in safe_sequence:
            print(f"P{p}", end=" ")

        print()
    else:
        print("\nSystem is in an UNSAFE state.")
        print("No safe sequence exists.")


def main():
    print("BANKER'S ALGORITHM")

    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resource types: "))

    allocation = []
    maximum = []

    print("\nEnter Allocation Matrix:")

    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))
        allocation.append(row)

    print("\nEnter Maximum Matrix:")

    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))
        maximum.append(row)

    available = list(
        map(int, input("\nEnter Available Resources: ").split())
    )

    need = calculate_need(maximum, allocation)

    display_matrix("Allocation Matrix:", allocation)
    display_matrix("Maximum Matrix:", maximum)
    display_matrix("Need Matrix:", need)

    print("\nAvailable Resources:", available)

    safety_algorithm(allocation, need, available)


if __name__ == "__main__":
    main()
