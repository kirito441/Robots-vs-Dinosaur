from weapon import Weapon

class Robot:
    def __init__(self,name):
        
        self.name = name
        self.health = 300
        self.weapon = Weapon("Mjolnir", 55)
        pass

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.atkpwr
        
