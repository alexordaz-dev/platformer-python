
import constants as c
class mario():
    def __init__(self,coord: int)->None:
        self.coord = coord
        self.__sprite = c.s_mario_standing
        self.__ancho = c.mario_width
        self.__alto = c.mario_height

        self.__score = 0
        self.__money = 0
        self.__lifes= 3

