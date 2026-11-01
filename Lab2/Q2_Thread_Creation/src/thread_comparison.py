import threading
import time
import os


def calculate_square(numbers):
    total = 0

    for num in numbers:
        total += num * num

    return total


def single_thread_demo(numbers):
    print("\n--- Single Thread Execution ---")

    start = time.perf_counter()

    result = calculate_square(numbers)

    end = time.perf_counter()

    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Process ID:", os.getpid())
    print("Result:", result)

    return end - start


def worker(numbers, results, index):
    print(
        f"{threading.current_thread().name} "
        f"started | ID: {threading.get_ident()}"
    )

    results[index] = calculate_square(numbers)

    print(f"{threading.current_thread().name} completed")


def multi_thread_demo(numbers):
    print("\n--- Multiple Thread Execution ---")

    mid = len(numbers) // 2

    first_half = numbers[:mid]
    second_half = numbers[mid:]

    results = [0, 0]

    t1 = threading.Thread(
        target=worker,
        args=(first_half, results, 0),
        name="Worker-1"
    )

    t2 = threading.Thread(
        target=worker,
        args=(second_half, results, 1),
        name="Worker-2"
    )

    start = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print("Combined Result:", sum(results))

    return end - start


def main():
    numbers = list(range(1, 500001))

    print("THREAD CREATION AND PERFORMANCE")
    print("Total Numbers:", len(numbers))

    single_time = single_thread_demo(numbers)
    multi_time = multi_thread_demo(numbers)

    print("\n--- Performance Comparison ---")

    print(f"Single Thread Time: {single_time:.6f} seconds")
    print(f"Multiple Thread Time: {multi_time:.6f} seconds")

    print("\nBoth executions completed successfully.")


if __name__ == "__main__":
    main()
