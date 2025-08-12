import utils
from hunt import Hunt
from hunter import Hunter


class Game:
    def __init__(self):
        self.width = 10
        self.height = 10



    def main(self):
        drawer = utils.Utils(self.width, self.height)

        drawer.draw()


if __name__ == "__main__":
    game = Game()
    game.main()
