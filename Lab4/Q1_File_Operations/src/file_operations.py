import os
import stat
import shutil
from datetime import datetime


def display_metadata(file_path):
    print("\n========== FILE METADATA ==========")

    try:
        info = os.stat(file_path)

        print("File Name:", os.path.basename(file_path))
        print("File Size:", info.st_size, "bytes")
        print("Permissions:", stat.filemode(info.st_mode))
        print("Created:", datetime.fromtimestamp(info.st_ctime))
        print("Last Modified:", datetime.fromtimestamp(info.st_mtime))
        print("Last Accessed:", datetime.fromtimestamp(info.st_atime))

    except OSError as error:
        print("Metadata Error:", error)


def main():
    print("=" * 55)
    print("       FILE OPERATIONS AND SEQUENTIAL ACCESS")
    print("=" * 55)

    test_directory = "test_directory"

    try:
        os.makedirs(test_directory, exist_ok=True)
        print("\nTest directory created:", test_directory)

        original_file = os.path.join(test_directory, "student_records.txt")
        renamed_file = os.path.join(test_directory, "final_records.txt")

        print("\n1. Creating and opening file for writing")

        records = [
            "101,Vikash,CSE\n",
            "102,Ankush,CSE\n",
            "103,Rahul,AIML\n"
        ]

        with open(original_file, "w") as file:
            for record in records:
                file.write(record)

        print("Records written successfully.")

        print("\n2. Closing and reopening the file")

        print("\n3. Reading records sequentially")

        with open(original_file, "r") as file:
            for line_number, record in enumerate(file, start=1):
                print(f"Record {line_number}: {record.strip()}")

        print("\n4. Appending a new record")

        with open(original_file, "a") as file:
            file.write("104,Aman,CSE\n")

        print("New record appended successfully.")

        print("\n5. Reading updated file")

        with open(original_file, "r") as file:
            for line_number, record in enumerate(file, start=1):
                print(f"Record {line_number}: {record.strip()}")

        print("\n6. Renaming the file")

        os.rename(original_file, renamed_file)
        print("File renamed successfully.")

        print("\n7. Listing directory contents")

        print("Files:", os.listdir(test_directory))

        display_metadata(renamed_file)

        print("\n8. Preserving required evidence")

        evidence_file = os.path.join(
            "output", "preserved_records.txt"
        )

        shutil.copy2(renamed_file, evidence_file)

        print("Evidence preserved at:", evidence_file)

        print("\n9. Deleting the test file")

        os.remove(renamed_file)
        print("Test file deleted successfully.")

        print("\n10. Verifying deletion")

        if not os.path.exists(renamed_file):
            print("Verification successful: Test file no longer exists.")

        print("\n11. Testing error handling")

        try:
            with open(renamed_file, "r") as file:
                file.read()

        except FileNotFoundError:
            print("Handled Error: File does not exist.")

        try:
            os.remove(renamed_file)

        except FileNotFoundError:
            print("Handled Error: Cannot delete a missing file.")

        print("\nRemaining directory contents:", os.listdir(test_directory))

        print("\nFILE OPERATIONS SIMULATION COMPLETED SUCCESSFULLY.")

    except OSError as error:
        print("File System Error:", error)


if __name__ == "__main__":
    main()
