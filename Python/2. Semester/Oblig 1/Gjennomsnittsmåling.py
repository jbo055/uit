from datetime import datetime
from Vehicle import Vehicle, Car, Truck, SUV

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
