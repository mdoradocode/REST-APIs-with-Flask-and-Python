class Device:
    def __init__(self, name, connectedBy):
        self.name = name
        self.connectedBy = connectedBy
        self.connected = True

    ##The !r calls the repr method which just puts the quotes in automatically, easier than doing it yourself
    def __str__(self):
        return f"Device {self.name!r} ({self.connectedBy})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connectedBy, capacity):
        ##This calls the super (or parent class) class of the child class
        super().__init__(name, connectedBy)
        self.capacity = capacity
        self.remainingPages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remainingPages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            raise TypeError("Device is disconnected at this time, cannot print.")
        print(f"Printing {pages} pages.")
        self.remainingPages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.print(50)
print(printer)
printer.disconnect()
printer.print(30)  # Error
