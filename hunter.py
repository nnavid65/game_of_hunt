
import numpy as np


class Hunter:
    Symbol = '+'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2  # cell per 2 seconds
        self.vision = 3  # cells can be seen
        self.energy = 5 # after 5 seconds is disapear


    def move(self, hunts, width, height):
        self.x = (self.x + np.random.choice([-1, 0, 1])) % width
        self.y = (self.y + np.random.choice([-1, 0, 1])) % height
    

    def see_hunt(self, hunts):
        pass


    def reproduce(self):
        pass
