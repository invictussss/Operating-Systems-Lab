def fifo_page_replacement(pages, capacity):
    frames = []
    page_faults = 0
    page_hits = 0
    pointer = 0

    print("\n========== FIFO PAGE REPLACEMENT ==========")

    for page in pages:
        if page in frames:
            page_hits += 1
            status = "HIT"
        else:
            page_faults += 1
            status = "PAGE FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % capacity

        print(f"Page: {page} | Frames: {frames} | {status}")

    return page_hits, page_faults


def lru_page_replacement(pages, capacity):
    frames = []
    recent = []
    page_faults = 0
    page_hits = 0

    print("\n========== LRU PAGE REPLACEMENT ==========")

    for page in pages:
        if page in frames:
            page_hits += 1
            recent.remove(page)
            recent.append(page)
            status = "HIT"
        else:
            page_faults += 1
            status = "PAGE FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                least_recent = recent.pop(0)
                frames.remove(least_recent)
                frames.append(page)

            recent.append(page)

        print(f"Page: {page} | Frames: {frames} | {status}")

    return page_hits, page_faults


def optimal_page_replacement(pages, capacity):
    frames = []
    page_faults = 0
    page_hits = 0

    print("\n========== OPTIMAL PAGE REPLACEMENT ==========")

    for i, page in enumerate(pages):
        if page in frames:
            page_hits += 1
            status = "HIT"
        else:
            page_faults += 1
            status = "PAGE FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i + 1:]
                farthest = -1
                replace_page = None

                for frame in frames:
                    if frame not in future:
                        replace_page = frame
                        break

                    next_use = future.index(frame)

                    if next_use > farthest:
                        farthest = next_use
                        replace_page = frame

                frames[frames.index(replace_page)] = page

        print(f"Page: {page} | Frames: {frames} | {status}")

    return page_hits, page_faults


def display_results(name, hits, faults, total):
    print(f"\n----- {name} RESULTS -----")
    print("Total Page References:", total)
    print("Page Hits:", hits)
    print("Page Faults:", faults)
    print("Hit Ratio:", round(hits / total, 2))
    print("Fault Ratio:", round(faults / total, 2))


def main():
    print("=" * 55)
    print("       DEMAND PAGING AND PAGE REPLACEMENT")
    print("=" * 55)

    capacity = int(input("Enter number of frames: "))

    if capacity <= 0:
        print("Invalid frame capacity!")
        return

    n = int(input("Enter number of page references: "))

    if n <= 0:
        print("Invalid number of page references!")
        return

    pages = list(map(int, input("Enter page reference string: ").split()))

    if len(pages) != n:
        print("ERROR: Number of pages does not match the given count!")
        return

    if any(page < 0 for page in pages):
        print("ERROR: Page numbers cannot be negative!")
        return

    print("\nPage Reference String:", pages)
    print("Frame Capacity:", capacity)

    fifo_hits, fifo_faults = fifo_page_replacement(pages, capacity)
    lru_hits, lru_faults = lru_page_replacement(pages, capacity)
    opt_hits, opt_faults = optimal_page_replacement(pages, capacity)

    print("\n========== FINAL COMPARISON ==========")
    display_results("FIFO", fifo_hits, fifo_faults, n)
    display_results("LRU", lru_hits, lru_faults, n)
    display_results("OPTIMAL", opt_hits, opt_faults, n)

    print("\nDEMAND PAGING SIMULATION COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
