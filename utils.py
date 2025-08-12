

class Utils:
    def __init__(self, width, height):
        self.width = width
        self.height = height  
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]  

    def draw(self):
        print("\n" + "-" * (self.width + 2))
        for row in self.grid:
            print("|" + "".join(row) + "|")
        print("-" * (self.width + 2))
