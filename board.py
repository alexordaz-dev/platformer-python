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
        self.tuberias = [Tuberias(0, 30, "left", "no_straight"),
                      Tuberias(270, 30, "right", "no_straight"),
                      Tuberias(0, 168, "left", "straight"),
                      Tuberias(260, 168, "right", "straight")]
        floor1 = []
        x = 0
        for i in range(17):
            floor1.append(Floor(x,63))
            x += 7
        self.floor = floor1

        floor2 = []
        x = 181
        for i in range(17):
            floor2.append(Floor(x,63))
            x += 7
        self.floor2 = floor2
        # Running the game
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
        for floor_tile in self.floor + self.floor2:
            pyxel.blt(floor_tile.x, floor_tile.y, *floor_tile.sprite)