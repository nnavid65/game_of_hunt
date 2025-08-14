import time

import numpy as np

import hunt
import utils
from hunt import Hunt
from hunter import Hunter


class Game:
    def __init__(self):
        self.width = 50
        self.height = 30
        self.hunts = []
        self.hunters = []
        self.drawer = utils.Utils(self.width, self.height)


    def add_hunts(self):
        total_cells = self.width * self.height
        num_hunts = int(total_cells * 0.05)  # 10% of the cells
        positions = set()

        while len(positions) < num_hunts:
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            positions.add((x, y))

        for x, y in positions:
            self.hunts.append(Hunt(x, y))

    def place_hunts_in_grid(self):
        for hunt in self.hunts:
            self.drawer.grid[hunt.y][hunt.x] = Hunt.Symbol

    def add_hunters(self):
        total_cells = self.width * self.height
        num_hunters = int(total_cells * 0.01)  # 10% of the cells
        positions = set()

        while len(positions) < num_hunters:
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            positions.add((x, y))

        for x, y in positions:
            self.hunters.append(Hunter(x, y))


    def place_hunters_in_grid(self):
        for hunter in self.hunters:
            self.drawer.grid[hunter.y][hunter.x] = Hunter.Symbol

    def setup(self):
        # draw a grid
        self.drawer.draw()

        # add hunts to the grid
        self.add_hunts()
        self.place_hunts_in_grid()

        # move hunts
        for hunt in self.hunts:
            hunt.move(self.hunters, self.width, self.height)

        self.add_hunters()
        self.place_hunters_in_grid()

        # move hunters
        for hunter in self.hunters:
            hunter.move(self.hunters, self.width, self.height)

        self.drawer.draw()

    def main(self):
        self.setup()
        while True:
            # clear grid before placing
            self.drawer.clear_grid()

            # move hunts
            for hunt in self.hunts:
                hunt.move(self.hunters, self.width, self.height)

            # place hunts
            self.place_hunts_in_grid()


            # move hunters
            for hunter in self.hunters:
                hunter.move(self.hunters, self.width, self.height)

            # place hunters
            self.place_hunters_in_grid()

            # draw updated grid
            self.drawer.draw()
            time.sleep(2)


if __name__ == "__main__":
    game = Game()
    game.main()
