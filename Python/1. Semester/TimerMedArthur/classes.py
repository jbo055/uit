class Car:
    plate = "000000"
    hp = 0
    name = "Cecilie"
    brand = "Toyota"
    weight = 0

car1 = Car()
car2 = Car()
car1.name = "Max"
print(car1.name, car2.name)

class Human:
    def __init__(self, name, hp = 0):
        self.name = name
        self.hp = hp

    def print_data(self):
        print(self.name)
        print(self.color)

    def fight():
        print("fighting")

class SuperHuman(Human):
    def __init__(self, name = "Ola Normann", special_ability = "flying", weapon = "rifle"):
        super().__init__(name, hp= 100) 
        self.weapon = weapon
        self.special_ability = special_ability

class GameCharacter:
    def __init__(self, name = "Max", weapon = "Bazooka", special_ability = "flying"):
        self.name = name
        self.weapon = weapon
        self.special_ability = special_ability

# this is a function (not a method)
def print_stats(GameCharacter):
    print(GameCharacter.name) # I cannot reach attributes in my class without self prefix - functions are always locally visible

# def fight():
# h1 = Human("Arthur", "AT1234", "red")

g1 = GameCharacter()

g2 = GameCharacter("Arthur", "Sword", "Teleportation")
print_stats(g1)

s1 = SuperHuman("Arthur", "Flying")
s2 = SuperHuman()
print(s1.name, s1.special_ability, s1.weapon, s1.hp)
