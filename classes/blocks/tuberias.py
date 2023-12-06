class Pipes:

    def __init__(self, x: int, y: int):

        self.x = x
        self.y = y
        self.sprite = Pipes.sprite()

    def sprite(self) -> tuple:
        if self.type == ("complex"):
            if self.side == "right":
                sprite = (0, 0, 176, 31, 28)
            else:
                sprite = (0, 80, 176, 31, 28)
        else:
            if self.side == "right":
                sprite = (0, 32, 188, 42, 17)
            else:
                sprite = (0, 37, 188, 42, 17)

