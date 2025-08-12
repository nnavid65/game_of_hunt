

class Utils:
    def __init__(self, width, height):
        self.width = width
        self.height = height  
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]  

    def draw(self):
        #for row in range(self.height):
         #   for col in range(self.width):
          #      print('.' if self.grid[row][col] else '_', end=' ')
           # print()

        for row in self.grid:
            print(' '.join(row))