
class Mario:
    """ This class stores all the information needed for our plane.
    It is very likely more attributes will be needed, here we show the
    basic ones"""
    def __init__(self, x: int, y: int, ):
        """ This method creates the Plane object
        @param x the starting x of Plane
        @param y the starting y of Plane
       """
        self.x = x
        self.y = y
        self.idle_sprite = (0, 0, 0, 16, 24)  # when mario is still
