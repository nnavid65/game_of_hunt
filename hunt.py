import time


class Hunt:

    Symbol = 'o'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1 # cell per 2 seconds
        self.vision = 5 # cells can be seen
        self.timer = 1  # for production 
    
    def move(self, hunter, dx, dy):
        # try to move away nearest hunter
        pass

    def see_hunters(self, hunters):
        pass


    def reproduce(self):
        pass

