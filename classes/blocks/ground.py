


import pyxel
class Ground:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (0, 119, 176, 16, 16)
        self.height = pyxel.height/3
        self.width = pyxel.width
