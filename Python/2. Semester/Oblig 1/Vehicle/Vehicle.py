import pickle
import os

class Vehicle:
    def __init__(self, regnr, make, model, model_year, mileage, price):
        self.regnr = regnr
        self.make = make
        self.model = model
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        
    def __str__(self):
        return f"Regnr: {self.regnr}, Make: {self.make}, Model: {self.model}, Model Year: {self.model_year}, Mileage: {self.mileage}, Price: {self.price}"
    
class Car(Vehicle):
    def __init__(self, regnr, make, model, model_year, mileage, price, doors):
        super().__init__(regnr, make, model, model_year, mileage, price)
        self.doors = doors
        
    def __str__(self):
        return super().__str__() + f", Doors: {self.doors}"
    
class Truck(Vehicle):
    def __init__(self, regnr, make, model, model_year, mileage, price, wheel_drive):
        super().__init__(regnr, make, model, model_year, mileage, price)
        self.wheel_drive = wheel_drive
        
    def __str__(self):
        return super().__str__() + f", Drive Type: {self.wheel_drive}"
    
class SUV(Vehicle):
    def __init__(self, regnr, make, model, model_year, mileage, price, passenger_capacity):
        super().__init__(regnr, make, model, model_year, mileage, price)
        self.passenger_capacity = passenger_capacity
        
    def __str__(self):
        return super().__str__() + f", Passenger Capacity: {self.passenger_capacity}"

FILENAME = "vehicles.dat"

def load_vehicles():
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as file:
            try:
                return pickle.load(file)
            except EOFError:
                return []
    return []

def save_vehicles(vehicles_list):
    with open(FILENAME, "wb") as file:
        pickle.dump(vehicles_list, file)

vehicles_list = load_vehicles()

def menu():
    print(f"{'='*10} Menu {'='*10}\n\n1. New Car\n2. New Truck\n3. New SUV\n4. Find vehicles by make\n5. Show all vehicles\n6. Quit\n")

def input_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def input_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")
def is_regnr_unique(regnr):
    return not any(vehicle.regnr.lower() == regnr.lower() for vehicle in vehicles_list)

def add_new_vehicle(vehicle_type):
    make = input("Please enter make of the vehicle: ").strip()
    model = input("Please enter model of the vehicle: ").strip()
    model_year = input_valid_int("Please enter year of the make: ")
    mileage = input_valid_float("Please enter mileage of the vehicle: ")
    price = input_valid_float("Please enter price of the vehicle: ")

    while True:
        regnr = input("Please enter registration number of the vehicle: ").strip()
        if is_regnr_unique(regnr):
            break
        print("Registration number already exists. Please enter a unique registration number.")

    if vehicle_type == "Car":
        doors = input_valid_int("Please enter number of doors: ")
        vehicle = Car(regnr, make, model, model_year, mileage, price, doors)
    elif vehicle_type == "Truck":
        wheel_drive = input("Drive Type (2WD/4WD): ").strip()
        vehicle = Truck(regnr, make, model, model_year, mileage, price, wheel_drive)
    elif vehicle_type == "SUV":
        passenger_capacity = input_valid_int("Please enter passenger capacity: ")
        vehicle = SUV(regnr, make, model, model_year, mileage, price, passenger_capacity)

    vehicles_list.append(vehicle)
    save_vehicles()
    print("Vehicle added successfully!")

def find_vehicles_by_make():
    if not vehicles_list:
        print("No vehicles in inventory.")
        return
    
    make = input("Name of vehicle: ").strip()
    found = [vehicle for vehicle in vehicles_list if vehicle.make.lower() == make.lower()]
    
    if found:
        for vehicle in found:
            print(vehicle)
    else:
        print("No vehicles found for that make.")

def show_all_vehicles():
    if not vehicles_list:
        print("No vehicles in inventory.")
    else:
        print("The following vehicles are in inventory: ")
    for vehicle in vehicles_list:
        print(vehicle)

def main():
    while True:
        menu()
        choice = input_valid_int("Please enter your choice: ")

        if choice == 1:
            add_new_vehicle("Car")
        elif choice == 2:
            add_new_vehicle("Truck")
        elif choice == 3:
            add_new_vehicle("SUV")
        elif choice == 4:
            find_vehicles_by_make()
        elif choice == 5:
            show_all_vehicles()
        elif choice == 6:
            save_vehicles()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()   

