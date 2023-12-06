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
        # We draw something putting blt taking the values from the  object
        # Parameters are x, y, and a tuple containing the image bank,
        # the starting x and y and the size which we initialize before with
        # the self. ...
        pyxel.blt(self.tuberias[0].x, self.tuberias[0].y, *self.tuberias[0].sprite)
        pyxel.blt(self.tuberias[1].x, self.tuberias[1].y, *self.tuberias[1].sprite)
        pyxel.blt(self.tuberias[2].x, self.tuberias[2].y, *self.tuberias[2].sprite)
        pyxel.blt(self.tuberias[3].x, self.tuberias[3].y, *self.tuberias[3].sprite)

        pyxel.blt(self.floor[0].x, self.floor[0].y, *self.floor[0].sprite)
        pyxel.blt(self.floor[1].x, self.floor[1].y, *self.floor[1].sprite)
        pyxel.blt(self.floor[2].x, self.floor[2].y, *self.floor[2].sprite)
        pyxel.blt(self.floor[3].x, self.floor[3].y, *self.floor[3].sprite)
        pyxel.blt(self.floor[4].x, self.floor[4].y, *self.floor[4].sprite)
        pyxel.blt(self.floor[5].x, self.floor[5].y, *self.floor[5].sprite)
        pyxel.blt(self.floor[6].x, self.floor[6].y, *self.floor[6].sprite)
        pyxel.blt(self.floor[7].x, self.floor[7].y, *self.floor[7].sprite)
        pyxel.blt(self.floor[8].x, self.floor[8].y, *self.floor[8].sprite)
        pyxel.blt(self.floor[9].x, self.floor[9].y, *self.floor[9].sprite)
        pyxel.blt(self.floor[10].x, self.floor[10].y, *self.floor[10].sprite)
        pyxel.blt(self.floor[11].x, self.floor[11].y, *self.floor[11].sprite)
        pyxel.blt(self.floor[12].x, self.floor[12].y, *self.floor[12].sprite)
        pyxel.blt(self.floor[13].x, self.floor[13].y, *self.floor[13].sprite)
        pyxel.blt(self.floor[14].x, self.floor[14].y, *self.floor[14].sprite)
        pyxel.blt(self.floor[15].x, self.floor[15].y, *self.floor[15].sprite)
        pyxel.blt(self.floor[16].x, self.floor[16].y, *self.floor[16].sprite)
        pyxel.blt(self.floor2[0].x, self.floor2[0].y, *self.floor2[0].sprite)
        pyxel.blt(self.floor2[1].x, self.floor2[1].y, *self.floor2[1].sprite)
        pyxel.blt(self.floor2[2].x, self.floor2[2].y, *self.floor2[2].sprite)
        pyxel.blt(self.floor2[3].x, self.floor2[3].y, *self.floor2[3].sprite)
        pyxel.blt(self.floor2[4].x, self.floor2[4].y, *self.floor2[4].sprite)
        pyxel.blt(self.floor2[5].x, self.floor2[5].y, *self.floor2[5].sprite)
        pyxel.blt(self.floor2[6].x, self.floor2[6].y, *self.floor2[6].sprite)
        pyxel.blt(self.floor2[7].x, self.floor2[7].y, *self.floor2[7].sprite)
        pyxel.blt(self.floor2[8].x, self.floor2[8].y, *self.floor2[8].sprite)
        pyxel.blt(self.floor2[9].x, self.floor2[9].y, *self.floor2[9].sprite)
        pyxel.blt(self.floor2[10].x, self.floor2[10].y, *self.floor2[10].sprite)
        pyxel.blt(self.floor2[11].x, self.floor2[11].y, *self.floor2[11].sprite)
        pyxel.blt(self.floor2[12].x, self.floor2[12].y, *self.floor2[12].sprite)
        pyxel.blt(self.floor2[13].x, self.floor2[13].y, *self.floor2[13].sprite)
        pyxel.blt(self.floor2[14].x, self.floor2[14].y, *self.floor2[14].sprite)
        pyxel.blt(self.floor2[15].x, self.floor2[15].y, *self.floor2[15].sprite)
        pyxel.blt(self.floor2[16].x, self.floor2[16].y, *self.floor2[16].sprite)