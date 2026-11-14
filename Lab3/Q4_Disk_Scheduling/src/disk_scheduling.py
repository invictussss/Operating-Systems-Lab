def calculate_movement(sequence, head):
    movement = 0
    current = head

    for track in sequence:
        movement += abs(track - current)
        current = track

    return movement


def fcfs(requests, head):
    print("\n========== FCFS DISK SCHEDULING ==========")

    sequence = requests.copy()
    movement = calculate_movement(sequence, head)

    print("Head Movement Sequence:", [head] + sequence)
    print("Total Head Movement:", movement)


def sstf(requests, head):
    print("\n========== SSTF DISK SCHEDULING ==========")

    pending = requests.copy()
    sequence = []
    current = head

    while pending:
        nearest = min(pending, key=lambda x: abs(x - current))
        sequence.append(nearest)
        pending.remove(nearest)
        current = nearest

    movement = calculate_movement(sequence, head)

    print("Head Movement Sequence:", [head] + sequence)
    print("Total Head Movement:", movement)


def scan(requests, head, disk_size, direction):
    print("\n========== SCAN DISK SCHEDULING ==========")

    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    if direction == "right":
        sequence = right + [disk_size - 1] + left[::-1]
    else:
        sequence = left[::-1] + [0] + right

    movement = calculate_movement(sequence, head)

    print("Direction:", direction.upper())
    print("Head Movement Sequence:", [head] + sequence)
    print("Total Head Movement:", movement)


def c_scan(requests, head, disk_size, direction):
    print("\n========== C-SCAN DISK SCHEDULING ==========")

    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    if direction == "right":
        sequence = right + [disk_size - 1, 0] + left
    else:
        sequence = left[::-1] + [0, disk_size - 1] + right[::-1]

    movement = calculate_movement(sequence, head)

    print("Direction:", direction.upper())
    print("Head Movement Sequence:", [head] + sequence)
    print("Total Head Movement:", movement)


def swap_space():
    print("\n========== SWAP-SPACE MANAGEMENT ==========")

    total_space = int(input("Enter total swap-space size (MB): "))

    if total_space <= 0:
        print("Invalid swap-space size!")
        return

    used_space = 0

    while True:
        print("\n1. Allocate Swap Space")
        print("2. Release Swap Space")
        print("3. Display Swap-Space Status")
        print("4. Exit Swap-Space Management")

        choice = input("Enter your choice: ")

        if choice == "1":
            size = int(input("Enter process size (MB): "))

            if size <= 0:
                print("Invalid process size!")
            elif used_space + size > total_space:
                print("ERROR: Insufficient swap space!")
            else:
                used_space += size
                print("Swap space allocated successfully.")

        elif choice == "2":
            size = int(input("Enter space to release (MB): "))

            if size <= 0 or size > used_space:
                print("ERROR: Invalid release amount!")
            else:
                used_space -= size
                print("Swap space released successfully.")

        elif choice == "3":
            print("Total Swap Space:", total_space, "MB")
            print("Used Swap Space:", used_space, "MB")
            print("Available Swap Space:", total_space - used_space, "MB")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def main():
    print("=" * 55)
    print("       DISK SCHEDULING AND SWAP-SPACE")
    print("=" * 55)

    disk_size = int(input("Enter total number of disk tracks: "))
    head = int(input("Enter initial head position: "))

    if disk_size <= 0 or head < 0 or head >= disk_size:
        print("Invalid disk size or head position!")
        return

    n = int(input("Enter number of disk requests: "))

    if n <= 0:
        print("Invalid number of requests!")
        return

    requests = list(map(int, input("Enter disk request sequence: ").split()))

    if len(requests) != n or any(x < 0 or x >= disk_size for x in requests):
        print("ERROR: Invalid disk request sequence!")
        return

    direction = input("Enter direction (left/right): ").lower()

    if direction not in ["left", "right"]:
        print("Invalid direction!")
        return

    print("\nDisk Size:", disk_size)
    print("Initial Head Position:", head)
    print("Disk Requests:", requests)

    fcfs(requests, head)
    sstf(requests, head)
    scan(requests, head, disk_size, direction)
    c_scan(requests, head, disk_size, direction)

    swap_space()

    print("\nDISK SCHEDULING SIMULATION COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
