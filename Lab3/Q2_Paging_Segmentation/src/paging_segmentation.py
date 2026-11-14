def paging():
    print("\n========== PAGING ==========")

    page_size = int(input("Enter page size: "))

    if page_size <= 0:
        print("Invalid page size!")
        return

    n = int(input("Enter number of page table entries: "))

    if n <= 0:
        print("Invalid number of entries!")
        return

    page_table = []

    print("\nEnter frame number for each page.")
    print("Enter -1 for an unmapped page.")

    for i in range(n):
        frame = int(input(f"Page {i} frame number: "))
        page_table.append(frame)

    logical_address = int(input("\nEnter logical address: "))

    if logical_address < 0:
        print("Invalid logical address!")
        return

    page_number = logical_address // page_size
    offset = logical_address % page_size

    print("\n----- PAGING CALCULATIONS -----")
    print("Logical Address:", logical_address)
    print("Page Size:", page_size)
    print("Page Number =", logical_address, "//", page_size, "=", page_number)
    print("Offset =", logical_address, "%", page_size, "=", offset)

    if page_number >= len(page_table):
        print("ERROR: Invalid page number. Page does not exist.")
        return

    frame_number = page_table[page_number]

    if frame_number < 0:
        print("ERROR: Page is unmapped. Address translation rejected.")
        return

    physical_address = frame_number * page_size + offset

    print("Page Table Entry: Valid")
    print("Frame Number:", frame_number)
    print("Physical Address = Frame Number * Page Size + Offset")
    print("Physical Address =", frame_number, "*", page_size, "+", offset)
    print("Physical Address:", physical_address)


def segmentation():
    print("\n========== SEGMENTATION ==========")

    n = int(input("Enter number of segments: "))

    if n <= 0:
        print("Invalid number of segments!")
        return

    segments = []

    for i in range(n):
        print(f"\nSegment {i}:")
        base = int(input("Enter base address: "))
        limit = int(input("Enter segment limit: "))

        segments.append((base, limit))

    segment_number = int(input("\nEnter segment number: "))
    offset = int(input("Enter offset: "))

    print("\n----- SEGMENTATION CALCULATIONS -----")
    print("Segment Number:", segment_number)
    print("Offset:", offset)

    if segment_number < 0 or segment_number >= len(segments):
        print("ERROR: Invalid segment reference.")
        return

    base, limit = segments[segment_number]

    print("Base Address:", base)
    print("Segment Limit:", limit)

    if offset < 0 or offset >= limit:
        print("ERROR: Invalid offset. Segment limit exceeded.")
        return

    physical_address = base + offset

    print("Segment Reference: Valid")
    print("Physical Address = Base Address + Offset")
    print("Physical Address =", base, "+", offset)
    print("Physical Address:", physical_address)


def main():
    print("=" * 50)
    print("       PAGING AND SEGMENTATION SIMULATION")
    print("=" * 50)

    paging()
    segmentation()

    print("\nSIMULATION COMPLETED.")


if __name__ == "__main__":
    main()
