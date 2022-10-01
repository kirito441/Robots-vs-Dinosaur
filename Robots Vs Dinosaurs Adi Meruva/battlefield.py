from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon


class Battlefield:
    def __init__(self):
        self.dino = Dinosaur("Big Dawg Eren Jaeger", 40)
        self.robo = Robot("Little Bro Armin Arlert")
        
        pass
    
    def run_game(self):
        #runs functions in order
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    
    def display_welcome(self):
        print("On this beautiful day we witness the great battle of " + self.dino.name + " the dinosaur and " + self.robo.name + "the robot!")
        pass

    def battle_phase(self):
    
       

        while (self.robo.health > 0) and (self.dino.health > 0):
            
                self.robo.attack(self.dino)
                print(self.dino.name + " attacked " + self.robo.name + " for " + str(self.dino.atkpwr) + " damage!") 
                print(self.robo.name + "'s health is " + str(self.robo.health))
                
                if (self.dino.health < 0):
                    self.dino.health = 0
                
            
            
                self.dino.attack(self.robo)
                print(self.robo.name + " attacked " + self.dino.name + " with " + self.robo.weapon.name + " for " + str(self.robo.weapon.atkpwr) +" damage!")
                print(self.dino.name + "'s health is " + str(self.dino.health)) 
                if (self.robo.health < 0):
                    self.robo.health =0
                
                
        
    
    def display_winner(self):
        #if robot health > dino
        #if dino health >robot
        if (self.robo.health > self.dino.health) :
            print( self.dino.name + " has been defeated! " + self.robo.name + "is the winner!")
        else:
            print( self.robo.name + " has been defeated! " + self.dino.name + "is the winner!")