class MileMachine:
    def __init__(self):
        self.ways = {"A": {"glare": (0, "B")},
                     "B": {"show": (1, "C"),
                           "glare": (3, "E"), "bend": (2, "F")},
                     "C": {"bend": (4, "D")},
                     "D": {"glare": (5, "E")},
                     "E": {"show": (6, "F")},
                     "F": {"glare": (7, "F"), "show": (8, "A")}}
        self.current = "A"

    def move(self, method):
        number = self.ways[self.current][method][0]
        self.current = self.ways[self.current][method][1]
        return number

    def glare(self):
        return self.move("glare")

    def show(self):
        return self.move("show")

    def bend(self):
        return self.move("bend")


def main():
    return MileMachine()
