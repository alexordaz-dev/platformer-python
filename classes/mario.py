import pyxel
import constants as c


class Mario:
    def __init__(self, x: int, y: int,) -> None:

        self.x = x
        self.y = y
        self.__sprite = c.s_mario_standing
        self.__initialize_booleans()
        self.__initialize_forces()
        self.__score = 0
        self.__money = 0
        self.__lives = 3

    @property
    def v_x(self):
        return self.__v_x
    @property
    def looking_right(self):
        return self.__looking_right
    @property
    def v_y(self):
        return self.__v_y

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, new_sprite: list):
        self.__sprite = new_sprite

    def __initialize_forces(self):
        self.__v_x = 0
        self.__v_y = 0

    def __initialize_booleans(self):
        self.__looking_right = True
        self.__walking = False

    def __update_position(self):  # changes the player position
        self.x += self.__v_x
        self.y += self.__v_y

    def __update_animations(self):
        if self.looking_right:
            if self.__walking:
                if self.sprite != c.s_mario_walking_r1 and pyxel.frame_count % (c.fps/30) == 0:
                    self.sprite = c.s_mario_walking_r1
                elif self.sprite != c.s_mario_walking_r2 and pyxel.frame_count % (c.fps/30) == 0:
                    self.sprite = c.s_mario_walking_r2
                elif self.sprite != c.s_mario_walking_r3 and pyxel.frame_count % (c.fps/30) == 0:
                    self.sprite = c.s_mario_walking_r3

    def __detect_buttons(self):
        if pyxel.btn(pyxel.KEY_D):
            self.__v_x = min(self.__v_x+c.normal_v, c.max_v_x)
            self.__looking_right = True
            self.__walking = True
        elif not pyxel.btn(pyxel.KEY_A) and self.__looking_right:
            self.__v_x = max(self.__v_x - c.friction, 0)
            self.__walking = False

    def update_status(self, player):
        self.__update_animations()
        self.__update_position()
        self.__detect_buttons()
