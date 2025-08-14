import time

import numpy as np


class Hunt:

    Symbol = 'o'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1 # cell per 2 seconds
        self.vision = 5 # cells can be seen
        self.timer = 1  # for production

    def move(self, hunters, width, height):
        # move randomly
        self.x = (self.x + np.random.choice([-1, 0, 1])) % width
        self.y = (self.y + np.random.choice([-1, 0, 1])) % height

    def see_hunters(self, hunters):
        pass


    def reproduce(self):
        pass



