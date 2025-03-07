import os
import pickle
from datetime import datetime

vehicles_dict = {}

class Vehicle:
    def __init__(self, reg_number, make, model, model_year, mileage, price):
        self.reg_number = reg_number
        self.make = make
        self.model = model
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.speed_tickets = []

    def add_speed_ticket(self, ticket):
        if ticket.timestamp not in [t.timestamp for t in self.speed_tickets]:
            self.speed_tickets.append(ticket)

    def show_tickets(self):
        for ticket in self.speed_tickets:
            print(ticket)
    
    def __str__(self):
        return f"Reg Number: {self.reg_number}, Make: {self.make}, Model: {self.model}, Model Year: {self.model_year}, Mileage: {self.mileage}, Price: {self.price}"

class Car(Vehicle):
    def __init__(self, reg_number, make, model, model_year, mileage, price, doors):
        super().__init__(reg_number, make, model, model_year, mileage, price)
        self.doors = doors

    def __str__(self):
        return super().__str__() + f", Doors: {self.doors}"    

class Truck(Vehicle):
    def __init__(self, reg_number, make, model, model_year, mileage, price, drive_type):
        super().__init__(reg_number, make, model, model_year, mileage, price)
        self.drive_type = drive_type

    def __str__(self):
        return super().__str__() + f", Drive Type: {self.drive_type}"

class SUV(Vehicle):
    def __init__(self, reg_number, make, model, model_year, mileage, price, passenger_capacity):
        super().__init__(reg_number, make, model, model_year, mileage, price)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return super().__str__() + f", Passenger Capacity: {self.passenger_capacity}"
    
def load_vehicles():
    if os.path.exists("vehicles.dat"):
        with open("vehicles.dat", "rb") as file:
            return pickle.load(file)
    return {}

def save_vehicles(vehicles_dict):
    with open("vehicles.dat", "wb") as file:
        pickle.dump(vehicles_dict, file)

def check_speed_violations():
    for regnr, vehicle in vehicles_dict.items():
        if vehicle.speed_tickets:
            print(f"Registration Number: {regnr}")
            vehicle.show_tickets()

def display_menu():
    print("""
        MENU
1) New car
2) New truck
3) New SUV
4) Find vehicles by make
5) Show all vehicles
6) Show tickets
7) Quit
    """)

def add_vehicle(vehicle_type, vehicles_dict):
    reg_number = input("Please enter registration number: ")
    make = input("Please enter make of the vehicle: ")
    model = input("Please enter model of the vehicle: ")
    model_year = int(input("Please enter year of the make: "))
    mileage = int(input("Please enter mileage of the vehicle: "))
    price = float(input("Please enter the price of the vehicle: "))

    if vehicle_type == "Car":
        doors = int(input("Please enter number of doors: "))
        vehicle = Car(reg_number, make, model, model_year, mileage, price, doors)
    elif vehicle_type == "Truck":
        drive_type = input("Please enter drive type (F/B/4): ")
        vehicle = Truck(reg_number, make, model, model_year, mileage, price, drive_type)
    elif vehicle_type == "SUV":
        passenger_capacity = int(input("Please enter passenger capacity: "))
        vehicle = SUV(reg_number, make, model, model_year, mileage, price, passenger_capacity)

    vehicles_dict[reg_number] = vehicle
    print("Vehicle added successfully!")


def find_vehicle_by_make(vehicles_dict):
    make = input("Enter the make of the vehicle: ")
    found = [v for v in vehicles_dict.values() if v.make.lower() == make.lower()]
    if found:
        for vehicle in found:
            print(vehicle)
    else:
        print("No vehicles found for that make.")


def show_all_vehicles(vehicles_dict):
    if vehicles_dict:
        print("The following vehicles are in inventory:")
        for vehicle in vehicles_dict.values():
            print(vehicle)
    else:
        print("No vehicles in inventory.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def file_to_dict(filename):
    vehicle_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                regnr = parts[0]
                timestamp = " ".join(parts[1:]) # samler dato og tid til en streng
                vehicle_data[regnr] = datetime.strptime(timestamp, "%Y-%d-%m %H:%M:%S")
    except FileNotFoundError:
        print("File not found.")
    return vehicle_data

class SpeedTicket:
    def __init__(self, timestamp, speed, speed_limit):
        self.timestamp = timestamp
        self.speed = speed
        self.speed_limit = speed_limit

    def __str__(self):
        return f"Timestamp: {self.timestamp}, Speed: {self.speed}, Speed Limit: {self.speed_limit}"
    
def find_speeders(dict_a, dict_b, speed_limit, distance):
    for regnr in dict_a:
        if regnr in dict_b:
            time_a = dict_a[regnr]
            time_b = dict_b[regnr]
            time_diff = (time_b - time_a).total_seconds() / 3600 # tiden i timer
            speed = distance / time_diff # hastigheten i km/t

            if speed > speed_limit * 1.05:
                ticket = SpeedTicket(time_b, speed, speed_limit)
                vehicles_dict[regnr].add_speed_ticket(ticket)


def main():
    dict_a = file_to_dict("box_a.txt")
    dict_b = file_to_dict("box_b.txt")
    vehicles_dict = load_vehicles()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_vehicle("Car", vehicles_dict)
            elif choice == 2:
                add_vehicle("Truck", vehicles_dict)
            elif choice == 3:
                add_vehicle("SUV", vehicles_dict)
            elif choice == 4:
                find_vehicle_by_make(vehicles_dict)
            elif choice == 5:
                show_all_vehicles(vehicles_dict)
            elif choice == 6:
                check_speed_violations()
            elif choice == 7:
                save_vehicles(vehicles_dict)
                print("Exiting the program...")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()