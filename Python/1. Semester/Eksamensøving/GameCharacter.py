# assignment 1: 

# ### Assignment Description:

# Create a Python program with three classes: GameCharacter, Wizard, and Zombie. The GameCharacter class serves as the parent class and includes *private attributes* for 
# the character's name and health points. Both Wizard and Zombie classes inherit from GameCharacter.

# - The Wizard class should include an additional attribute called *magic potion*. Access and modification of this attribute should be handled through *getter and setter 
# methods*.
# - The Zombie class should have an additional attribute called *damage*, implemented using the *@property decorator*.

# The program should also include a *fight function* that enables a simulated battle between Wizards and Zombies. The fight function should:
# - Use *random numbers* to determine attack damage during the battle.
# - Wizards should start with *300 health points*, and Zombies with *100 health points*.
# - Allow the user to define the maximum damage a Zombie can inflict through input in the main function. This value will directly influence the outcome of the fight.

# The main function should enable the user to set up the characters, specify battle parameters, and observe the simulated combat between the two character types.

class GameCharacter:
    def __init__(self, name, health):
        self._name = name
        self._health = health

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health

    
class Wizard(GameCharacter):
    def __init__(self, name, health, magic_potion):
        super().__init__(name, health)
        self.magic_potion = magic_potion

    @property
    def magic_potion(self):
        return self.magic_potion
    
    @magic_potion.setter
    def set_magic_potion(self, value):
        if value < 0:
            print("Amount can not be less than 0")
        else:
            self.magic_potion = value
    
    @magic_potion.getter
    def get_magic_potion(self):
        return self.magic_potion
    
class Zombie(GameCharacter):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    @property
    def damage(self):
        return self.damage
    
    @damage.setter
    def set_damage(self, value):
        if value < 0:
            print("Damage can not be less than 0")




