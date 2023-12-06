import pyxel
from classes.blocks.tuberias import Tuberias
from classes.blocks.floor import Floor

class Board:

    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        # Initializing the object
        self.width = w
        self.height = h
        # This block initializes pyxel
        # The first thing to do is to create the screen, see API for
        # more parameters
        pyxel.init(self.width, self.height,)
        # Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
        pyxel.load("assets/sprites.pyxres")

        # this creates the position of something in  the screen
        # example: self.mario = Mario(int(self.width / 2), 200)
        self.tuberias = [Tuberias(0, 20, "left", "no_straight"),
                      Tuberias(270, 20, "right", "no_straight"),
                      Tuberias(0, 175, "left", "straight"),
                      Tuberias(260, 175, "right", "straight")]
        floor1 = []
        x = 0
        for i in range(18):
            floor1.append(Floor(x,55))
            x += 7
        self.floor = floor1

        floor2 = []
        x = 174
        for i in range(18):
            floor2.append(Floor(x,55))
            x += 7
        self.floor2 = floor2

        floor3 = []
        x = 94
        for i in range(16):
            floor3.append(Floor(x,100))
            x += 7
        self.floor3 = floor3

        floor4 = []
        x = 0
        for i in range(6):
            floor4.append(Floor(x,108))
            x += 7
        self.floor4 = floor4

        floor5 = []
        x = 258
        for i in range(6):
            floor5.append(Floor(x, 108))
            x += 7
        self.floor5 = floor5

        floor6 = []
        x = 0
        for i in range(16):
            floor6.append(Floor(x, 150))
            x += 7
        self.floor6 = floor6

        floor7 = []
        x = 188
        for i in range(16):
            floor7.append(Floor(x, 150))
            x += 7
        self.floor7 = floor7
        pyxel.run(self.update, self.draw)


    def update(self):
        """ This is executed each frame, here invocations to the update
        methods of all objects must be included"""

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        """ This is executed also each frame, here you should just draw
        things """
        pyxel.cls(0)

        for tuberia in self.tuberias:
            pyxel.blt(tuberia.x, tuberia.y, *tuberia.sprite)

            # Draw floor
        for floor_tile in self.floor + self.floor2 + self.floor3 + self.floor4 + self.floor5 + self.floor6 + self.floor7:
            pyxel.blt(floor_tile.x, floor_tile.y, *floor_tile.sprite)