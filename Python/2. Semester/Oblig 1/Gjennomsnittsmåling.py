import datetime
import os
import pickle

# Skriv hjelpefunksjonen file_to_dict() som har en parameter filename. Denne funksjonen skal 
# lese inn en tekstfil filename fra en fotoboks, som inneholder bilnummer, dato og tid for 
# hver passering. Funksjonen skal returnere en dictionary med bilnummer som nøkkel og tidspunkt 
# som verdi for nøkkelen.
# Eksempel på kjøring av funksjon på fila box_a.txt som vist i figuren: (viser kun 3 første poster)

def file_to_dict(filename):
    with open(filename, "r") as file:
        



class SpeedTicket:
    def __init__(self, time_stamp, speed, speed_limit):
        self.time_stamp = time_stamp
        self.speed = speed
        self.speed_limit = speed_limit

