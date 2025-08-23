import time

import numpy as np

import hunter


class Hunt:

    Symbol = '🐑'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1 # cell per 2 seconds
        self.vision = 2 # cells can be seen
        self.age = 0
        self.energy = 10
        self.produce = 5
        self.timer = 1  # for production

    def move(self, hunters, width, height, grid):
        # move away if see hunter
        closest_hunter = self.see_hunters(hunters)
        if closest_hunter:
            dx = self.x - closest_hunter.x
            dy = self.y - closest_hunter.y
            step_x = int(np.sign(dx) * self.speed)
            step_y = int(np.sign(dy) * self.speed)
            new_x = (self.x + step_x) % width
            new_y = (self.y + step_y) % height
            if grid[new_y][new_x] in ('.'):
                self.x = new_x
                self.y = new_y
        # move randomly
        #else:
            #self.x = (self.x + np.random.choice([-self.speed, 0, self.speed])) % width
            #self.y = (self.y + np.random.choice([-self.speed, 0, self.speed])) % height

        else:
            dx = np.random.choice([-self.speed, 0, self.speed])
            dy = np.random.choice([-self.speed, 0, self.speed])
            new_x = (self.x + dx) % width
            new_y = (self.y + dy) % height
            if grid[new_y][new_x] in ('.'):
                self.x = new_x
                self.y = new_y


    def see_hunters(self, hunters):
        visible_hunters = [
            hunter for hunter in hunters
            if (hunter.x - self.x) ** 2 + (hunter.y - self.y) ** 2 <= self.vision ** 2
        ]
        if not visible_hunters:
            return None
        return min(visible_hunters, key=lambda hunter: (hunter.x - self.x) ** 2 + (hunter.y - self.y) ** 2)

    def reproduce(self):
        # age increase in each step
        self.age += 1
        if self.age > self.produce:
            # reproduce
            self.age = 0
            return True
        return False

    def hunt_died(self):
        # age increase in each step
        self.age += 1
        if self.age > self.energy:
            # die
            return True
        return False
