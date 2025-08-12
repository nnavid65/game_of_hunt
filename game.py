import numpy as np

import utils
from hunt import Hunt
from hunter import Hunter


class Game:
    def __init__(self):
        self.width = 50
        self.height = 30
        
        self.hunts = []
        self.add_hunt()

        self.hunters = []
        self.add_hunter()

    def add_hunt(self):
        total_cell = self.width * self.height
        num_hunts = int(total_cell * 0.1)
        positions = set()

        while len(positions) < num_hunts:
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            positions.add((x, y))

        for (x, y) in positions:
            self.hunts.append(Hunt(x, y))


    def add_hunter(self):
        total_cell = self.width * self.height
        num_hunters = int(total_cell * 0.1)
        positions = set()

        while len(positions) < num_hunters:
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            positions.add((x, y))

        for (x, y) in positions:
            self.hunters.append(Hunter(x, y))

    def main(self):
        drawer = utils.Utils(self.width, self.height)


        for hunt in self.hunts:
            drawer.grid[hunt.y][hunt.x] = Hunt.Symbol  # Place '+'

        for hunter in self.hunters:
            drawer.grid[hunter.y][hunter.x] = Hunter.Symbol  # Place 'H'

        drawer.draw()


if __name__ == "__main__":
    game = Game()
    game.main()
