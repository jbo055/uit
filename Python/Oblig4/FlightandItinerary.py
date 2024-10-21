from datetime import datetime

class Flight:
    def __init__(self, flight_number: str, departure_time: datetime, arrival_time: datetime):
        # Initialize the flight details
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
    
    def get_flight_time(self) -> float:
        """Calculate the flight time in minutes."""
        # Calculate the difference between arrival and departure times
        flight_duration = self.arrival_time - self.departure_time
        # Convert the flight duration to minutes
        return flight_duration.total_seconds() / 60

class Itinerary:
    def __init__(self, flights: list):
        # Initialize the list of flights
        self.flights = flights
    
    def get_total_flight_time(self) -> float:
        """Calculate the total flight time of all flights in minutes."""
        total_flight_time = 0
        # Sum the flight times of all flights
        for flight in self.flights:
            total_flight_time += flight.get_flight_time()
        return total_flight_time
    
    def get_total_travel_time(self) -> float:
        """Calculate the total travel time from the first departure to the last arrival."""
        if len(self.flights) == 0:
            return 0
        
        # The travel starts with the departure of the first flight
        first_departure = self.flights[0].departure_time
        # The travel ends with the arrival of the last flight
        last_arrival = self.flights[-1].arrival_time
        
        # Calculate the total travel time
        total_travel_time = last_arrival - first_departure
        # Convert the total travel time to minutes
        return total_travel_time.total_seconds() / 60

def main():

    flights = []

    flights.append(Flight("US230",

        datetime(2014, 4, 5, 5, 5, 0),

        datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",

        datetime(2014, 4, 5, 6, 55, 0),

        datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",

        datetime(2014, 4, 5, 9, 35, 0),

        datetime(2014, 4, 5, 12, 55, 0)))

   

    itinerary = Itinerary(flights)

    print(itinerary.get_total_travel_time())

    print(itinerary.get_total_flight_time())

main()