import pyxel
import constants as c


class Mario:
    def __init__(self, x: int, y: int,) -> None:

        self.x = x
        self.y = y
        self.__sprite = c.s_mario_standing
        self.__ancho = c.mario_width
        self.__alto = c.mario_height

        self.__score = 0
        self.__money = 0
        self.__lives = 3

    @property
    def v_x(self):
        return self.__v_x

    @property
    def v_y(self):
        return self.__v_y

    def __forces(self):
        self.__v_x = 0
        self.__v_y = 0

    def __update_position(self):  # changes the player position
        self.x += self.__v_x
        self.y += self.__v_y

    def __update_animations(self):
        if self.__looking_right:



    def __buttons(self):
        if pyxel.btn(pyxel.KEY_D):
            self.__v_x = min(self.__v_x+c.normal_v, c.max_v_x)
            self.__looking_right = True
            self._walking = True
        elif not pyxel.btn(pyxel.KEY_A) and self.__looking_right:
            self.__v_x = max(self.__v_x - c.friction, 0)
            self.__walking = False
