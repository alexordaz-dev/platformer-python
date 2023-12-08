class Pipes:

    def __init__(self, x: int, y: int, side: str, type: str):

        self.x = x
        self.y = y
        self.side = side
        self.type = type
        self.sprite = Pipes.sprite(self)

    def sprite(self):
        if self.type == "no_straight":
            if self.side == "right":
                sprite = (0, 0, 176, 31, 29)
            else:
                sprite = (0, 80, 176, 32, 29)
        else:
            if self.side == "right":
                sprite = (0, 32, 188, 42, 18)
            else:
                sprite = (0, 37, 188, 43, 18)
        return sprite
