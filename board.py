import pyxel
from classes import mario
from classes.blocks.pipes import Pipes
from classes.blocks.floor import Floor
from classes.blocks.ground import Ground


class Board:

    def __init__(self, w: int, h: int):

        self.width = w
        self.height = h
        # For mario here we name an object called player
        self.player = mario.Mario(int(w/2), 170)
        pyxel.init(self.width, self.height)
        pyxel.load("assets/sprites.pyxres")
        self.initialize_pipes()
        self.initialize_floor()
        self.initialize_ground()


        pyxel.run(self.update, self.draw)

    def initialize_pipes(self):
        self.pipes = [
            Pipes(0, 20, "left", "no_straight"),
            Pipes(368, 20, "right", "no_straight"),
            Pipes(0, 175, "left", "straight"),
            Pipes(358, 175, "right", "straight")
        ]

    def initialize_floor(self):
        self.floor = self.create_floor(0, 55, 25)
        self.floor2 = self.create_floor(225, 55, 25)
        self.floor3 = self.create_floor(120, 100, 23)
        self.floor4 = self.create_floor(0, 110, 6)
        self.floor5 = self.create_floor(358, 110, 6)
        self.floor6 = self.create_floor(0, 150, 23)
        self.floor7 = self.create_floor(239, 150, 23)

    def create_floor(self, x, y, count):
        floors = []
        for i in range(count):
            floors.append(Floor(x, y))
            x += 7
        return floors
    def initialize_ground(self):
        self.ground = self.create_ground(0, 204,  25)
    def create_ground(self, x, y, count):
        grounds = []
        for i in range(count):
            grounds.append(Ground(x,y))
            x += 16
        return grounds

    def update(self):
        # For mario we only need to call the update method, this will do all the things for mario
        self.player.update_status()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # For mario we then draw his position and his firs sprite
        pyxel.blt(self.player.x, self.player.y, *self.player.sprite)

        for tuberia in self.pipes:
            pyxel.blt(tuberia.x, tuberia.y, *tuberia.sprite)

        for floors in self.floor + self.floor2 + self.floor3 + self.floor4 + self.floor5 + self.floor6 + self.floor7:
            pyxel.blt(floors.x, floors.y, *floors.sprite)

        for grounds in self.ground:
            pyxel.blt(grounds.x, grounds.y, *grounds.sprite)
