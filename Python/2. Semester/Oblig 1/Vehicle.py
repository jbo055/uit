import os
import pickle

class Vehicle:
    def __init__(self, regnr, merke, modell, modellår, kmstand, pris):
        self.regnr = regnr
        self.merke = merke
        self.modell = modell
        self.modellår = modellår
        self.kmstand = kmstand
        self.pris = pris
    
    def __str__(self):
        return f"Regnr: {self._regnr}, Merke: {self._merke}, Modell: {self._modell}, Modellår: {self._modellår}, Kmstand: {self._kmstand}, Pris: {self._pris}"

    
class Car(Vehicle):
    def __init__(self, regnr, merke, modell, modellår, kmstand, pris, dører):
        super().__init__(regnr, merke, modell, modellår, kmstand, pris)
        self.dører = dører

    def __str__(self):
        return super().__str__() + f", Dører: {self._dører}"    

class Truck(Vehicle):
    def __init__(self, regnr, merke, modell, modellår, kmstand, pris, hjuldrift):
        super().__init__(regnr, merke, modell, modellår, kmstand, pris)
        self._hjuldrift = hjuldrift

    def __str__(self):
        return super().__str__() + f", Hjuldrift: {self._hjuldrift}"


class SUV:
    def __init__(self, regnr, merke, modell, modellår, kmstand, pris, passasjer_kapasitet):
        super().__init__(regnr, merke, modell, modellår, kmstand, pris)
        self.passasjer_kapasitet = passasjer_kapasitet

    def __str__(self):
        return super().__str__() + f", Passasjerkapasitet: {self.passasjer_kapasitet}"
    
def load_vehicles():
    if os.path.exists("vehicles.dat"):
        with open("vehicles.dat", "rb") as file:
            return pickle.load(file)
    return []

def save_vehicles(vehicles_list):
    with open("vehicles.dat", "wb") as file:
        pickle.dump(vehicles_list, file)

def display_menu():
    print("""
        MENU
1) New car
2) New truck
3) New SUV
4) Find vehicles by make
5) Show all vehicles
6) Quit
    """)

# Funksjon for å legge til kjøretøy
def add_vehicle(vehicle_type, vehicles_list):
    regnr = input("Please enter registration number: ")
    merke = input("Please enter make of the vehicle: ")
    modell = input("Please enter model of the vehicle: ")
    modellår = int(input("Please enter year of the make: "))
    kilometerstand = int(input("Please enter mileage of the vehicle: "))
    pris = float(input("Please enter the price of the vehicle: "))

    if vehicle_type == "Car":
        antall_dorer = int(input("Please enter number of doors: "))
        vehicle = Car(regnr, merke, modell, modellår, kilometerstand, pris, antall_dorer)
    elif vehicle_type == "Truck":
        hjuldrift = input("Please enter drive type (F/B/4): ")
        vehicle = Truck(regnr, merke, modell, modellår, kilometerstand, pris, hjuldrift)
    elif vehicle_type == "SUV":
        passasjer_kapasitet = int(input("Please enter passenger capacity: "))
        vehicle = SUV(regnr, merke, modell, modellår, kilometerstand, pris, passasjer_kapasitet)
    
    vehicles_list.append(vehicle)
    print("Vehicle added successfully!")

# Funksjon for å finne kjøretøy etter merke
def find_vehicle_by_make(vehicles_list):
    merke = input("Enter the make of the vehicle: ")
    found = [v for v in vehicles_list if v.merke.lower() == merke.lower()]
    if found:
        for vehicle in found:
            print(vehicle)
    else:
        print("No vehicles found for that make.")

# Funksjon for å vise alle kjøretøy
def show_all_vehicles(vehicles_list):
    if vehicles_list:
        print("The following vehicles are in inventory:")
        for vehicle in vehicles_list:
            print(vehicle)
    else:
        print("No vehicles in inventory.")

# Hovedprogrammet
def main():
    vehicles_list = load_vehicles()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_vehicle("Car", vehicles_list)
            elif choice == 2:
                add_vehicle("Truck", vehicles_list)
            elif choice == 3:
                add_vehicle("SUV", vehicles_list)
            elif choice == 4:
                find_vehicle_by_make(vehicles_list)
            elif choice == 5:
                show_all_vehicles(vehicles_list)
            elif choice == 6:
                save_vehicles(vehicles_list)
                print("Exiting the program...")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()