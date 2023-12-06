class Tuberias:

    def __init__(self, x: int, y: int, side: str, type: str):

        self.x = x
        self.y = y
        self.side = side
        self.type = type
        self.sprite = Tuberias.sprite(self)

    def sprite(self):
        if self.type == ("no_straight"):
            if self.side == "right":
                sprite = (0, 0, 176, 31, 28)
            else:
                sprite = (0, 80, 176, 31, 28)
        else:
            if self.side == "right":
                sprite = (0, 32, 188, 42, 17)
            else:
                sprite = (0, 37, 188, 42, 17)
        return sprite