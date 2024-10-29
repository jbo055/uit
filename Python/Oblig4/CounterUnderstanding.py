class Counter:
    total_count = 0
    def __init__(self, name):
        self.name = name
        self.instance_count = 0
        Counter.total_count += 1
    def increment(self):
        local_count = 0
        self.instance_count += 1
        local_count += 1
        print(f"{self.name}: instance_count = {self.instance_count}, local_count = {local_count}")
# Opprett noen objekter av klassen Counter
counter1 = Counter("Counter1")
counter2 = Counter("Counter2")
# Kall metoden increment flere ganger for hvert objekt
counter1.increment()
counter1.increment()
counter2.increment()
# Vis total antall objekter opprettet
print(f"Total number of Counter objects created: {Counter.total_count}")
# Vis instansvariabelen for hvert objekt
print(f"{counter1.name} instance_count: {counter1.instance_count}")
print(f"{counter2.name} instance_count: {counter2.instance_count}")