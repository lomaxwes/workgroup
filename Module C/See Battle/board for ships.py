class Board:
        def __init__(self, size=6):
            self.size = size
            self.field = [["`"]*size for i in range(size)]


        def __str__(self):
            vis = ""
            vis += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
            for i, row in enumerate(self.field):
                vis += f"\n{i+1} | " + " | ".join(row) + " |"
            return vis

a = Board()
print(a)
