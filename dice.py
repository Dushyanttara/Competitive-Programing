#Dushyant Tara(21-06-2020): This program helps us understand use of random module
"""A class for a throw dice
"""
from random import randint    

class Die():
    """A simple attempt to create a dice.
    """
    def __init__(self,sides = 6):
        """A simple attempt to make a die

        Args:
            sides (int, optional): Sides of the dice. Defaults to 6.
        """            
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and no. of sides.
        """
        self.output = randint(1,self.sides)
        print(self.output)


ludo_die = Die(6)

turn = 0
for turn in range(10):
    ludo_die.roll_die()
    turn += 1

ten_die = Die(10)
twenty_die = Die(20)
turn = 0
for turn in range(10):
    ten_die.roll_die()
    twenty_die.roll_die()
    turn += 1