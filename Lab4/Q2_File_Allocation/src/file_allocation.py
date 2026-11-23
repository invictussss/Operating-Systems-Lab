# Q2: Contiguous, Linked and Indexed File Allocation

def contiguous_allocation(disk_size, file_size):
    print("\n--- CONTIGUOUS ALLOCATION ---")

    disk = [0] * disk_size
    start = -1

    for i in range(disk_size - file_size + 1):
        if all(disk[j] == 0 for j in range(i, i + file_size)):
            start = i
            break

    if start == -1:
        print("File cannot be allocated contiguously.")
        return

    for i in range(start, start + file_size):
        disk[i] = 1

    print("File allocated successfully.")
    print("Starting Block:", start)
    print("Allocated Blocks:", list(range(start, start + file_size)))
    print("Disk Status:", disk)


def linked_allocation(disk_size, file_size):
    print("\n--- LINKED ALLOCATION ---")

    disk = [0] * disk_size
    free_blocks = [i for i in range(disk_size)]

    if file_size > disk_size:
        print("Not enough free space.")
        return

    allocated = free_blocks[:file_size]

    for block in allocated:
        disk[block] = 1

    print("File allocated successfully.")
    print("Allocated Blocks:", allocated)

    print("Linked List:")
    for i in range(len(allocated)):
        if i < len(allocated) - 1:
            print(allocated[i], "->", end=" ")
        else:
            print(allocated[i], "-> NULL")

    print("Disk Status:", disk)


def indexed_allocation(disk_size, file_size):
    print("\n--- INDEXED ALLOCATION ---")

    disk = [0] * disk_size

    if file_size + 1 > disk_size:
        print("Not enough space for index and data blocks.")
        return

    index_block = 0
    disk[index_block] = 1

    data_blocks = []

    for i in range(1, disk_size):
        if len(data_blocks) == file_size:
            break

        data_blocks.append(i)
        disk[i] = 1

    print("File allocated successfully.")
    print("Index Block:", index_block)
    print("Data Blocks:", data_blocks)
    print("Index Block Contents:", data_blocks)
    print("Disk Status:", disk)


def main():
    print("=" * 55)
    print("       FILE ALLOCATION METHODS SIMULATION")
    print("=" * 55)

    try:
        disk_size = int(input("Enter total number of disk blocks: "))
        file_size = int(input("Enter number of blocks required by file: "))

        if disk_size <= 0 or file_size <= 0:
            print("Please enter positive numbers.")
            return

        if file_size > disk_size:
            print("File size cannot exceed disk size.")
            return

        contiguous_allocation(disk_size, file_size)
        linked_allocation(disk_size, file_size)
        indexed_allocation(disk_size, file_size)

        print("\n" + "=" * 55)
        print("       SIMULATION COMPLETED SUCCESSFULLY")
        print("=" * 55)

    except ValueError:
        print("Invalid input. Please enter integer values.")


if __name__ == "__main__":
    main()
