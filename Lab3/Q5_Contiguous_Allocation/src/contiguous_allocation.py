def first_fit(blocks, process_size):
    for i in range(len(blocks)):
        if blocks[i] >= process_size:
            blocks[i] -= process_size
            return i
    return -1


def best_fit(blocks, process_size):
    best_index = -1

    for i in range(len(blocks)):
        if blocks[i] >= process_size:
            if best_index == -1 or blocks[i] < blocks[best_index]:
                best_index = i

    if best_index != -1:
        blocks[best_index] -= process_size

    return best_index


def worst_fit(blocks, process_size):
    worst_index = -1

    for i in range(len(blocks)):
        if blocks[i] >= process_size:
            if worst_index == -1 or blocks[i] > blocks[worst_index]:
                worst_index = i

    if worst_index != -1:
        blocks[worst_index] -= process_size

    return worst_index


def display_blocks(blocks):
    print("Remaining Memory Blocks:", blocks)


def memory_allocation():
    print("\n========== CONTIGUOUS MEMORY ALLOCATION ==========")

    n = int(input("Enter number of memory blocks: "))

    if n <= 0:
        print("Invalid number of blocks!")
        return

    blocks = list(map(int, input("Enter block sizes: ").split()))

    if len(blocks) != n or any(x <= 0 for x in blocks):
        print("Invalid memory block sizes!")
        return

    processes = int(input("Enter number of processes: "))

    if processes <= 0:
        print("Invalid number of processes!")
        return

    sizes = list(map(int, input("Enter process sizes: ").split()))

    if len(sizes) != processes or any(x <= 0 for x in sizes):
        print("Invalid process sizes!")
        return

    for name, algorithm in [
        ("FIRST FIT", first_fit),
        ("BEST FIT", best_fit),
        ("WORST FIT", worst_fit)
    ]:
        print(f"\n----- {name} ALLOCATION -----")

        available = blocks.copy()

        for i, size in enumerate(sizes):
            index = algorithm(available, size)

            if index != -1:
                print(f"Process P{i + 1} ({size} KB) allocated to Block {index + 1}")
            else:
                print(f"Process P{i + 1} ({size} KB) could not be allocated")

        display_blocks(available)


def swapping():
    print("\n========== SWAPPING SIMULATION ==========")

    memory_size = int(input("Enter total memory size (KB): "))
    process_size = int(input("Enter process size (KB): "))

    if memory_size <= 0 or process_size <= 0:
        print("Invalid memory or process size!")
        return

    if process_size > memory_size:
        print("Process is larger than available memory!")
        return

    print("\nProcess loaded into main memory.")
    print("Memory Used:", process_size, "KB")
    print("Free Memory:", memory_size - process_size, "KB")

    print("\nSwapping process out to secondary storage...")
    print("Process moved to secondary storage successfully.")

    print("\nSwapping process back into main memory...")
    print("Process restored successfully.")


def address_translation():
    print("\n========== ADDRESS TRANSLATION ==========")

    base = int(input("Enter base address: "))
    limit = int(input("Enter segment limit: "))
    logical_address = int(input("Enter logical address (offset): "))

    if base < 0 or limit <= 0:
        print("Invalid base address or segment limit!")
        return

    print("\nBase Address:", base)
    print("Segment Limit:", limit)
    print("Logical Address:", logical_address)

    if logical_address < 0 or logical_address >= limit:
        print("ERROR: Invalid logical address. Segment limit exceeded!")
        return

    physical_address = base + logical_address

    print("Physical Address = Base Address + Logical Address")
    print("Physical Address =", base, "+", logical_address)
    print("Physical Address:", physical_address)


def main():
    print("=" * 60)
    print(" CONTIGUOUS ALLOCATION, SWAPPING AND ADDRESS TRANSLATION")
    print("=" * 60)

    memory_allocation()
    swapping()
    address_translation()

    print("\nCONTIGUOUS ALLOCATION SIMULATION COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
