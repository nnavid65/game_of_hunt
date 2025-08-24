import time

import numpy as np

import hunt
import utils
from hunt import Hunt
from hunter import Hunter


class Game:
    def __init__(self):
        self.width = 60
        self.height = 35
        self.hunts = []
        self.hunters = []
        self.drawer = utils.Utils(self.width, self.height)


    def add_hunts(self):
        total_cells = self.width * self.height
        num_hunts = int(total_cells * 0.03)  # 10% of the cells
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

    def add_new_hunts(self, parent):
        # add new hunt in empty space
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (dx == 0 and dy == 0):
                    continue
                nx = (parent.x + dx) % self.width
                ny = (parent.y + dy) % self.height
                if self.drawer.grid[ny][nx] == ' ':
                    self.hunts.append(Hunt(nx, ny))
                    return

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



    def hunter_catch_hunts(self):
        eaten_indices = set()
        eaten_cells = set()

        for hunter in self.hunters:
            for i, h in enumerate(self.hunts):
                key = (h.x, h.y)
                if key in eaten_cells:
                    continue  # prey here already eaten this tick
                if hunter.x == h.x and hunter.y == h.y:
                    eaten_indices.add(i)
                    eaten_cells.add(key)
                    hunter.ate = True
                    self.add_new_hunter_near(hunter)
                    break  # one prey per hunter

        if eaten_indices:
            self.hunts = [h for i, h in enumerate(self.hunts) if i not in eaten_indices]




    def add_new_hunter_near(self, parent_hunter):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (parent_hunter.x + dx) % self.width
                ny = (parent_hunter.y + dy) % self.height
                if self.drawer.grid[ny][nx] in (' ', Hunt.Symbol):
                    self.hunters.append(Hunter(nx, ny))
                    return




    def setup(self):
        # Add hunts and hunters
        self.add_hunts()
        self.add_hunters()
        self.drawer.clear_grid()
        self.place_hunts_in_grid()
        self.place_hunters_in_grid()
        # draw a grid
        self.drawer.draw()



    def main(self):
        self.setup()
        tick = 0
        while True:
            tick += 1
            # clear grid before placing
            self.drawer.clear_grid()

            # place hunts
            self.place_hunts_in_grid()

            # place hunters
            self.place_hunters_in_grid()

            for hunter in self.hunters:
                hunter.ate = False

            # move hunts
            for hunt in self.hunts:
                hunt.move(self.hunters, self.width, self.height, self.drawer.grid)

            # clear grid
            self.drawer.clear_grid()

            # place hunts
            self.place_hunts_in_grid()

            # place hunters
            self.place_hunters_in_grid()

            # move hunters
            for hunter in self.hunters:
                hunter.move(self.hunts, self.width, self.height, self.drawer.grid)

            # hunter catch hunts
            self.hunter_catch_hunts()

            # refresh the grid so reproduction sees real empties
            self.drawer.clear_grid()
            self.place_hunts_in_grid()
            self.place_hunters_in_grid()



            # hunt produce and death
            surviving_hunts = []
            for hunt in self.hunts:
                if hunt.age + 1 > hunt.energy:
                    # hunt died
                    continue
                if hunt.reproduce():
                    # produce hunt
                    self.add_new_hunts(hunt)
                surviving_hunts.append(hunt)
            self.hunts = surviving_hunts

            # hunt reproduction
            #for hunt in list(self.hunts):
                #if hunt.reproduce():
                    # produce hunt
                 #   self.add_new_hunts(hunt)

            # energy update hunter
            for hunter in self.hunters:
                if getattr(hunter, "ate", False):
                    hunter.energy = 10
                    hunter.ate = False
                else:
                    hunter.energy -= 1

            # remove dead hunters
            self.hunters = [hunter for hunter in self.hunters if hunter.energy > 0]

            # clear grid
            self.drawer.clear_grid()

            # add hunt  
            self.place_hunts_in_grid()


            # add hunters
            self.place_hunters_in_grid()


            #if tick % 4 == 0:  # draw every 4th tick
            print(f"Hunts: {len(self.hunts)} | Hunters: {len(self.hunters)}")
            print("game of hunt")
            self.drawer.draw()

            if len(self.hunts) == 0 or len(self.hunters) == 0:
                print("Game Over")
                break

            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.main()
