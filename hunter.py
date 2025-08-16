
import numpy as np


class Hunter:
    Symbol = '+'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5  # cell per 2 seconds
        self.vision = 5  # cells can be seen
        self.energy = 7  # after 5 seconds is disapear
        self.age = 0  # for reproduction


    def move(self, hunts, width, height, grid):
        # move towards hunt if see hunt
        closest_hunt = self.see_hunt(hunts)
        if closest_hunt:
              # stepwise to avoid overshoot
            dx = int(np.sign(closest_hunt.x - self.x))
            dy = int(np.sign(closest_hunt.y - self.y))
            new_x = (self.x + dx) % width
            new_y = (self.y + dy) % height
            if grid[new_y][new_x] in ('.', 'o'):
                self.x, self.y = new_x, new_y
        else:
            #for _ in range(self.speed):
            # random walk should be 1-cell steps, not speed-sized jumps
            dx = np.random.choice([-1, 0, 1])
            dy = np.random.choice([-1, 0, 1])
            new_x = (self.x + dx) % width
            new_y = (self.y + dy) % height
            if grid[new_y][new_x] in ('.', 'o'):
                self.x, self.y = new_x, new_y


    def see_hunt(self, hunts):
        visible_hunts = [
            hunt for hunt in hunts
            if (hunt.x - self.x) ** 2 + (hunt.y - self.y) ** 2 <= self.vision ** 2
        ]
        if not visible_hunts:
            return None
        return min(visible_hunts, key=lambda hunt: (hunt.x - self.x) ** 2 + (hunt.y - self.y) ** 2)

    def reproduce(self):
        # age increase in each step
        self.age += 1
        if self.age > self.energy:
            self.age = 0
            return True
        return False
    
