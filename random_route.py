from random import randint
class RandomRoute:
    randomnum = randint(1,9)
    def __init__(self,color,number):
        self.color = color 
        self.number = number 
        self.text = None
        if self.number <  RandomRoute.randomnum:
            self.text = f"{self.number} is too low, try again!"
        elif self.number > RandomRoute.randomnum:
            self.text = f"{self.number} is too high, try again!"
        else:
            self.text = f"{self.number}: found it!"
