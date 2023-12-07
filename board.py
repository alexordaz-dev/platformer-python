import pyxel
from classes import mario
from classes.blocks.tuberias import Tuberias
from classes.blocks.floor import Floor


class Board:

    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        # For mario here we name an object called player
        self.player = mario.Mario(int(w/2), 170)
        pyxel.init(self.width, self.height)
        pyxel.load("assets/sprites.pyxres")
        self.initialize_tuberias()
        self.initialize_floor()


        pyxel.run(self.update, self.draw)

    def initialize_tuberias(self):
        self.tuberias = [
            Tuberias(0, 20, "left", "no_straight"),
            Tuberias(270, 20, "right", "no_straight"),
            Tuberias(0, 175, "left", "straight"),
            Tuberias(260, 175, "right", "straight")
        ]

    def initialize_floor(self):
        self.floor = self.create_floor(0, 55, 18)
        self.floor2 = self.create_floor(174, 55, 18)
        self.floor3 = self.create_floor(94, 100, 16)
        self.floor4 = self.create_floor(0, 108, 6)
        self.floor5 = self.create_floor(258, 108, 6)
        self.floor6 = self.create_floor(0, 150, 16)
        self.floor7 = self.create_floor(188, 150, 16)

    def create_floor(self, x, y, count):
        floors = []
        for i in range(count):
            floors.append(Floor(x, y))
            x += 7
        return floors

    def update(self):
        # For mario we only need to call the update method, this will do all the things for mario
        self.player.update_status()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # For mario we then draw his position and his firs sprite
        pyxel.blt(self.player.x, self.player.y, *self.player.sprite)

        for tuberia in self.tuberias:
            pyxel.blt(tuberia.x, tuberia.y, *tuberia.sprite)

        for floors in self.floor + self.floor2 + self.floor3 + self.floor4 + self.floor5 + self.floor6 + self.floor7:
            pyxel.blt(floors.x, floors.y, *floors.sprite)
