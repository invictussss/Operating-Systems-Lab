from collections import deque


class Device:
    def __init__(self, name, device_type, shared=False):
        self.name = name
        self.device_type = device_type
        self.shared = shared
        self.status = "Available"
        self.owner = None


class FiniteBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = deque()

    def insert(self, item):
        if len(self.items) >= self.capacity:
            print("Buffer is FULL. Cannot insert:", item)
            return False

        self.items.append(item)
        print("Inserted into buffer:", item)
        return True

    def remove(self):
        if not self.items:
            print("Buffer is EMPTY. Nothing to remove.")
            return None

        item = self.items.popleft()
        print("Removed from buffer:", item)
        return item

    def display(self):
        print(f"Buffer: {list(self.items)}")
        print(f"Buffer usage: {len(self.items)}/{self.capacity}")


class DeviceManager:
    def __init__(self):
        self.devices = {
            "Printer": Device("Printer", "Output", shared=False),
            "Scanner": Device("Scanner", "Input", shared=False),
            "Disk": Device("Disk", "Storage", shared=True)
        }

        self.shared_queue = deque()
        self.buffer = FiniteBuffer(3)

    def display_state(self):
        print("\n----- CURRENT DEVICE STATE -----")

        for device in self.devices.values():
            print(
                f"{device.name} | Type: {device.device_type} | "
                f"Status: {device.status} | Owner: {device.owner}"
            )

        print("Shared Request Queue:", list(self.shared_queue))
        self.buffer.display()
        print("--------------------------------")

    def request_device(self, process, device_name):
        if device_name not in self.devices:
            print("Invalid device request:", device_name)
            return

        device = self.devices[device_name]

        print(f"\n{process} requests {device_name}")

        if device.shared:
            self.shared_queue.append((process, device_name))
            print("Request added to shared-device FIFO queue.")
            self.process_shared_queue()

        elif device.status == "Available":
            device.status = "Assigned"
            device.owner = process
            print(f"{device_name} allocated to {process}.")

        else:
            print(
                f"Request REJECTED. {device_name} is already "
                f"assigned to {device.owner}."
            )

        self.display_state()

    def process_shared_queue(self):
        while self.shared_queue:
            process, device_name = self.shared_queue[0]
            device = self.devices[device_name]

            if device.status == "Available":
                self.shared_queue.popleft()
                device.status = "Assigned"
                device.owner = process

                print(
                    f"Shared device {device_name} assigned to {process}."
                )
            else:
                print(
                    f"{process} is waiting for {device_name}."
                )
                break

    def complete_request(self, process, device_name):
        print(f"\n{process} completes request for {device_name}")

        if device_name not in self.devices:
            print("Invalid device.")
            return

        device = self.devices[device_name]

        if device.owner != process:
            print("Completion rejected: Process does not own this device.")
            return

        device.status = "Available"
        device.owner = None

        print(f"{device_name} released successfully.")

        if device.shared:
            self.process_shared_queue()

        self.display_state()

    def virtual_device_demo(self):
        print("\n----- VIRTUAL DEVICE SIMULATION -----")
        print("Virtual Printer acts as a software abstraction.")
        print("Multiple processes can submit print requests")
        print("without directly controlling the physical printer.")
        print("The operating system manages these requests")
        print("through a common interface and device queue.")
        print("------------------------------------")


def main():
    print("=" * 55)
    print("       DEVICE MANAGEMENT SIMULATION")
    print("=" * 55)

    manager = DeviceManager()

    manager.display_state()

    # Dedicated device allocation
    manager.request_device("P1", "Printer")

    # Reject another request while printer is busy
    manager.request_device("P2", "Printer")

    # Dedicated scanner allocation
    manager.request_device("P3", "Scanner")

    # Shared device FIFO queue
    manager.request_device("P1", "Disk")
    manager.request_device("P2", "Disk")
    manager.request_device("P3", "Disk")

    # Virtual device abstraction
    manager.virtual_device_demo()

    # Finite buffer demonstration
    print("\n----- FINITE BUFFER DEMONSTRATION -----")

    manager.buffer.insert("Data-1")
    manager.display_state()

    manager.buffer.insert("Data-2")
    manager.display_state()

    manager.buffer.insert("Data-3")
    manager.display_state()

    # Buffer full condition
    manager.buffer.insert("Data-4")
    manager.display_state()

    # Buffer removal
    manager.buffer.remove()
    manager.display_state()

    # Buffer empty condition
    manager.buffer.remove()
    manager.buffer.remove()
    manager.buffer.remove()
    manager.display_state()

    # Complete dedicated requests
    manager.complete_request("P1", "Printer")
    manager.complete_request("P3", "Scanner")

    # Complete shared-device requests in FIFO order
    manager.complete_request("P1", "Disk")
    manager.complete_request("P2", "Disk")
    manager.complete_request("P3", "Disk")

    print("\n----- CPU AND DEVICE INDEPENDENCE -----")
    print("The CPU can execute other processes while an I/O")
    print("device performs its assigned operation.")
    print("After I/O completion, the device can notify the")
    print("CPU through an interrupt.")
    print("This allows CPU and device operations to overlap.")

    print("\nDEVICE MANAGEMENT SIMULATION COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
