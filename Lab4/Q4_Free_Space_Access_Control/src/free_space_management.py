# Q4: Free-Space Management, Deletion and Access Control

class FileSystem:

    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.bitmap = [0] * total_blocks
        self.files = {}

    # Allocate disk blocks
    def allocate_blocks(self, filename, size):
        free_blocks = [
            i for i in range(self.total_blocks)
            if self.bitmap[i] == 0
        ]

        if len(free_blocks) < size:
            print("Not enough free space available.")
            return

        allocated = free_blocks[:size]

        for block in allocated:
            self.bitmap[block] = 1

        self.files[filename] = {
            "blocks": allocated,
            "permissions": {
                "read": True,
                "write": True,
                "execute": False
            }
        }

        print(f"File '{filename}' created successfully.")
        print("Allocated Blocks:", allocated)

    # Display free space using bitmap
    def display_free_space(self):
        print("\n--- FREE-SPACE MANAGEMENT (BITMAP) ---")

        print("Bitmap:", self.bitmap)

        free_blocks = [
            i for i in range(self.total_blocks)
            if self.bitmap[i] == 0
        ]

        print("Free Blocks:", free_blocks)
        print("Total Free Blocks:", len(free_blocks))

    # Delete file and release blocks
    def delete_file(self, filename):
        print("\n--- FILE DELETION ---")

        if filename not in self.files:
            print("File not found.")
            return

        allocated = self.files[filename]["blocks"]

        for block in allocated:
            self.bitmap[block] = 0

        del self.files[filename]

        print(f"File '{filename}' deleted successfully.")
        print("Released Blocks:", allocated)

    # Display file permissions
    def display_permissions(self, filename):
        print("\n--- ACCESS CONTROL ---")

        if filename not in self.files:
            print("File not found.")
            return

        permissions = self.files[filename]["permissions"]

        print("File:", filename)
        print("Read Permission:", permissions["read"])
        print("Write Permission:", permissions["write"])
        print("Execute Permission:", permissions["execute"])

    # Change file permissions
    def change_permissions(self, filename, read, write, execute):
        if filename not in self.files:
            print("File not found.")
            return

        self.files[filename]["permissions"] = {
            "read": read,
            "write": write,
            "execute": execute
        }

        print("Permissions updated successfully.")

    # Check access permission
    def check_access(self, filename, operation):
        print("\nChecking", operation, "permission for", filename)

        if filename not in self.files:
            print("File not found.")
            return

        permissions = self.files[filename]["permissions"]

        if operation in permissions and permissions[operation]:
            print("Access Granted.")
        else:
            print("Access Denied.")


def main():

    print("=" * 60)
    print("   FREE-SPACE MANAGEMENT AND ACCESS CONTROL")
    print("=" * 60)

    try:
        total_blocks = int(input("Enter total disk blocks: "))

        if total_blocks <= 0:
            print("Disk size must be positive.")
            return

        fs = FileSystem(total_blocks)

        # Creating files
        print("\n--- FILE ALLOCATION ---")

        fs.allocate_blocks("Vikash.txt", 2)
        fs.allocate_blocks("Viraj.txt", 2)
        fs.allocate_blocks("Chirag.txt", 2)
        fs.allocate_blocks("Mayank.txt", 1)
        fs.allocate_blocks("Akshita.txt", 1)

        # Display free space
        fs.display_free_space()

        # Access control
        fs.display_permissions("Vikash.txt")

        fs.check_access("Vikash.txt", "read")
        fs.check_access("Vikash.txt", "execute")

        # Change permissions
        print("\n--- MODIFYING PERMISSIONS ---")

        fs.change_permissions(
            "Vikash.txt",
            read=True,
            write=False,
            execute=True
        )

        fs.display_permissions("Vikash.txt")

        fs.check_access("Vikash.txt", "write")
        fs.check_access("Vikash.txt", "execute")

        # Delete a file
        fs.delete_file("Chirag.txt")

        # Display updated free space
        fs.display_free_space()

        print("\n" + "=" * 60)
        print("   SIMULATION COMPLETED SUCCESSFULLY")
        print("=" * 60)

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
