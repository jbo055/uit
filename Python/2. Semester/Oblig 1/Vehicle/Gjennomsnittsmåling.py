import os
import pickle
from datetime import datetime

def file_to_dict(filename):
    vehicle_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 2:
                    regnr, timestamp = parts
                    vehicle_data[regnr] = timestamp
    except FileNotFoundError:
        print(f"File {filename} could not be found.")
    return vehicle_data

class SpeedTicket:
    def __init__(self, timestamp, speed, speed_limit):
        self.timestamp = timestamp
        self.speed = speed
        self.speed_limit = speed_limit

    def __str__(self):
        return f"Timestamp: {self.timestamp}, Speed: {self.speed:.2f}, Speed Limit: {self.speed_limit:.2f}"
    
class Vehicle:
    def __init__(self, regnr, make, model, model_year, mileage, price):
        self.regnr = regnr
        self.make = make
        self.model = model
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.speed_tickets = []
        
    
    
    def add_speed_ticket(self, ticket):
        if not any(t.timestamp == ticket.timestamp for t in self.speed_tickets):
            self.speed_tickets.append(ticket)
        else:
            print(f"Ticket for {self.regnr} already exists!")

    def __str__(self):
        base_info = (f"Regnr: {self.regnr}, Make: {self.make}, Model: {self.model}, "
                     f"Model Year: {self.model_year}, Mileage: {self.mileage}, Price: {self.price}")
        
        # Tickets should be printed last
        tickets_str = "\n".join(str(ticket) for ticket in self.speed_tickets)
        if tickets_str:
            return f"{base_info}\nTickets:\n{tickets_str}"
        return base_info
    
class Car(Vehicle):
    def __init__(self, regnr, make, model, model_year, mileage, price, doors):
        super().__init__(regnr, make, model, model_year, mileage, price)
        self.doors = doors
        
    def __str__(self):
        base_info = (f"Regnr: {self.regnr}, Make: {self.make}, Model: {self.model}, "
                     f"Model Year: {self.model_year}, Mileage: {self.mileage}, "
                     f"Price: {self.price}, Doors: {self.doors}")
        tickets_str = "\n".join(str(ticket) for ticket in self.speed_tickets)
        return f"{base_info}\nTickets:\n{tickets_str}" if tickets_str else base_info
    
class Truck(Vehicle):
    def __init__(self, regnr, make, model, model_year, mileage, price, wheel_drive):
        super().__init__(regnr, make, model, model_year, mileage, price)
        self.wheel_drive = wheel_drive
        
    def __str__(self):
        base_info = (f"Regnr: {self.regnr}, Make: {self.make}, Model: {self.model}, "
                     f"Model Year: {self.model_year}, Mileage: {self.mileage}, "
                     f"Price: {self.price}, Drive Type: {self.wheel_drive}")
        tickets_str = "\n".join(str(ticket) for ticket in self.speed_tickets)
        return f"{base_info}\nTickets:\n{tickets_str}" if tickets_str else base_info
    
class SUV(Vehicle):
    def __init__(self, regnr, make, model, model_year, mileage, price, passenger_capacity):
        super().__init__(regnr, make, model, model_year, mileage, price)
        self.passenger_capacity = passenger_capacity
        
    def __str__(self):
        base_info = (f"Regnr: {self.regnr}, Make: {self.make}, Model: {self.model}, "
                     f"Model Year: {self.model_year}, Mileage: {self.mileage}, "
                     f"Price: {self.price}, Passenger Capacity: {self.passenger_capacity}")
        tickets_str = "\n".join(str(ticket) for ticket in self.speed_tickets)
        return f"{base_info}\nTickets:\n{tickets_str}" if tickets_str else base_info
    
def calculate_speed(time_a, time_b, distance):
    timeformat = "%Y-%d-%m %H:%M:%S"
    time_a = datetime.strptime(time_a, timeformat)
    time_b = datetime.strptime(time_b, timeformat)
    time_diff_hours = (time_b - time_a).total_seconds() / 3600
    
    if time_diff_hours > 0:
        speed = distance / time_diff_hours
        return speed
    return 0

def find_speeders(dict_a, dict_b, speed_limit, distance, vehicles_dict):
    tolerance_limit = speed_limit * 1.05

    for regnr, time_a in dict_a.items():
        if regnr in dict_b:
            time_b = dict_b[regnr]
            speed = calculate_speed(time_a, time_b, distance)
            
            if speed > tolerance_limit:
                ticket = SpeedTicket(time_b, speed, speed_limit)
                
                if regnr in vehicles_dict:
                    vehicles_dict[regnr].add_speed_ticket(ticket)
                else:
                    new_vehicle = Vehicle(regnr, "Unknown", "Unknown", 0, 0, 0)
                    new_vehicle.add_speed_ticket(ticket)
                    vehicles_dict[regnr] = new_vehicle
    for ticket in vehicles_dict.values():
        print(ticket)

FILENAME = "vehicles.dat"

def load_vehicles():
    try:
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
    except (EOFError, FileNotFoundError):
        return {}
    

def save_vehicles(vehicles_dict):
    with open(FILENAME, "wb") as file:
        pickle.dump(vehicles_dict, file)

vehicles_dict = load_vehicles()

def menu():
    print(f"{'='*10} Menu {'='*10}\n\n1. New Car\n2. New Truck\n3. New SUV\n4. Find vehicles by make\n5. Show all vehicles\n6. Check speeding tickets.\n7. Quit\n")

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

def is_regnr_unique(regnr, vehicles_dict):
    return regnr not in vehicles_dict

def add_new_vehicle(vehicle_type):
    make = input("Please enter make of the vehicle: ").strip()
    model = input("Please enter model of the vehicle: ").strip()
    model_year = input_valid_int("Please enter year of the make: ")
    mileage = input_valid_float("Please enter mileage of the vehicle: ")
    price = input_valid_float("Please enter price of the vehicle: ")

    while True:
        regnr = input("Please enter registration number of the vehicle: ").strip()
        if is_regnr_unique(regnr, vehicles_dict):
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

    vehicles_dict[vehicle.regnr] = vehicle
    print("Vehicle added successfully!")

def find_vehicles_by_make():
    if not vehicles_dict:
        print("No vehicles in inventory.")
        return
    
    make = input("Name of vehicle: ").strip()
    
    found = [vehicle for vehicle in vehicles_dict.values() if vehicle.make.lower() == make.lower()]
    if found:
        for vehicle in found:
            print(vehicle)
    else:
        print("No vehicles found for that make.")

def show_all_vehicles():
    if not vehicles_dict:
        print("No vehicles in inventory.")
        return
    print("The following vehicles are in inventory: ")
    for vehicle in vehicles_dict.values():
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
            find_speeders(file_to_dict("box_a.txt"), file_to_dict("box_b.txt"), 60, 5, vehicles_dict)
        elif choice == 7:
            save_vehicles(vehicles_dict)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()   

