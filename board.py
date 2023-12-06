import pyxel

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

