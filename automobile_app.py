# Super class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")   # stores "car" in Vehicle class
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\nVehicle Information")
        print("-------------------")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


# User input
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter roof type (solid or sun roof): ")

# Create object
car = Automobile(year, make, model, doors, roof)

# Display output
car.display_info()