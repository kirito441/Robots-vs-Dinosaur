class Dinosaur:
    def __init__(self,name,attack_power):
        
        self.name = name
        self.health = 400
        self.atkpwr = attack_power
        pass

    def attack(self, robot):
        robot.health -= self.atkpwr
        pass