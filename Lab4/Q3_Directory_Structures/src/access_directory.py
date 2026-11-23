# Q3: Direct Access, Indexed Access and Directory Structures

def direct_access():
    print("\n--- DIRECT ACCESS ---")

    records = {
        0: "101,Vikash,AIML",
        1: "102,Viraj,CSE",
        2: "103,Chirag,AIML",
        3: "104,Mayank,CSE",
        4: "105,Akshita,AIML"
    }

    print("Available Records:")
    for block, record in records.items():
        print(f"Block {block}: {record}")

    try:
        block = int(input("\nEnter block number to access (0-4): "))

        if block in records:
            print("Record Found:", records[block])
        else:
            print("Invalid block number.")

    except ValueError:
        print("Please enter a valid integer.")


def indexed_access():
    print("\n--- INDEXED ACCESS ---")

    disk = {
        10: "101,Vikash,AIML",
        20: "102,Viraj,CSE",
        30: "103,Chirag,AIML",
        40: "104,Mayank,CSE",
        50: "105,Akshita,AIML"
    }

    index_table = {
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50
    }

    print("Index Table:")
    for index, block in index_table.items():
        print(f"Index {index} -> Disk Block {block}")

    try:
        index = int(input("\nEnter index to access (1-5): "))

        if index in index_table:
            block = index_table[index]
            print("Disk Block:", block)
            print("Record Found:", disk[block])
        else:
            print("Invalid index.")

    except ValueError:
        print("Please enter a valid integer.")


def directory_structures():
    print("\n--- DIRECTORY STRUCTURES ---")

    # 1. Single-Level Directory
    single_level = [
        "Vikash.txt",
        "Viraj.txt",
        "Chirag.txt",
        "Mayank.txt",
        "Akshita.txt"
    ]

    print("\n1. Single-Level Directory:")
    print("Root/")

    for file in single_level:
        print("  " + file)

    # 2. Two-Level Directory
    two_level = {
        "Vikash": ["notes.txt", "program.py"],
        "Viraj": ["report.pdf", "data.csv"],
        "Chirag": ["main.py", "project.txt"],
        "Mayank": ["assignment.docx", "output.txt"],
        "Akshita": ["records.txt", "image.png"]
    }

    print("\n2. Two-Level Directory:")

    for user, files in two_level.items():
        print(user + "/")

        for file in files:
            print("  " + file)

    # 3. Tree-Structured Directory
    tree = {
        "Students": {
            "Vikash": ["notes.txt", "program.py"],
            "Viraj": ["report.pdf"],
            "Chirag": ["project.txt"],
            "Mayank": ["assignment.docx"],
            "Akshita": ["records.txt"]
        },
        "Common": {
            "Shared": ["timetable.pdf", "notice.txt"]
        }
    }

    print("\n3. Tree-Structured Directory:")
    print("Root/")

    for folder, subfolders in tree.items():
        print("  " + folder + "/")

        for subfolder, files in subfolders.items():
            print("    " + subfolder + "/")

            for file in files:
                print("      " + file)


def main():
    print("=" * 60)
    print("   FILE ACCESS AND DIRECTORY STRUCTURES SIMULATION")
    print("=" * 60)

    direct_access()
    indexed_access()
    directory_structures()

    print("\n" + "=" * 60)
    print("   SIMULATION COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
