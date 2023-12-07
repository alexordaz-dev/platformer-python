import pyxel
import constants as c


class Mario:
    def __init__(self, x: int, y: int,) -> None:
        # Here we initialize all the methods and properties we will be having for mario
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
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, new):
        self.__dead = new

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, new_lives):
        self.__lives = new_lives

    @property
    def looking_right(self):
        return self.__looking_right
    @property
    def

    @property
    def v_y(self):
        return self.__v_y

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, new_sprite: list):
        self.__sprite = new_sprite

    # Here we initialize the values that ar true or False
    def __initialize_booleans(self):
        self.__looking_right = True
        self.__walking = False
        self.__dead = False

    # Here we initialize the values for the forces x and y acting on mario
    def __initialize_forces(self):
        self.__v_x = 0
        self.__v_y = 0

    def die(self):
        self.lives -= 1
        self.dead = True

        # This is the method that detects every button pressed and stores information to give it to other methods
    def __detect_buttons(self):
        if pyxel.btn(pyxel.KEY_D):
            self.__v_x = min(self.__v_x + c.normal_v, c.max_v_x)
            self.__looking_right = True
            self.__walking = True
        elif not pyxel.btn(pyxel.KEY_A) and self.__looking_right:
            self.__v_x = max(self.__v_x - c.friction, 0)
            self.__walking = False
        if pyxel.btn(pyxel.KEY_A):
            self.__v_x = max(self.__v_x - c.normal_v, -c.max_v_x)
            self.__looking_right = False
            self.__walking = True
        elif not pyxel.btn(pyxel.KEY_D) and not self.__looking_right:
            self.__v_x = max(-self.__v_x - c.friction, 0)
            self.__walking = False
        if pyxel.btn(pyxel.KEY_A):
            self.__v_x = max(self.__v_x - c.normal_v, -c.max_v_x)
            self.__looking_right = False
            self.__walking = True
        elif not pyxel.btn(pyxel.KEY_D) and not self.__looking_right:
            self.__v_x = min(self.__v_x + c.friction, 0)
            self.__walking = False
        if pyxel.btn(pyxel.KEY_SPACE):
            self.mario_is_in_air = True
            self.__v_y = -c.jump_force

    # This is the method that changes mario's position every frame
    def __update_position(self):  # changes the player position
        self.x += self.__v_x
        self.y += self.__v_y

    def __gravity_push(self):

        if self.y < pyxel.height:
            self.__v_y += c.gravity
        else:
            self.die()

    # This is the method that, following the input we give him when we press a button,
    # changes the model of mario every x frames
    def __update_animations(self):
        if self.looking_right:
            if self.__walking:
                if self.sprite != c.s_mario_walking_r1 and pyxel.frame_count % (c.fps/30) == 0:
                    self.sprite = c.s_mario_walking_r1
                elif self.sprite != c.s_mario_walking_r2 and pyxel.frame_count % (c.fps/30) == 0:
                    self.sprite = c.s_mario_walking_r2
                elif self.sprite != c.s_mario_walking_r3 and pyxel.frame_count % (c.fps/30) == 0:
                    self.sprite = c.s_mario_walking_r3
            elif not self.__walking:
                self.sprite = c.s_mario_standing
        else:
            if self.__walking:
                if self.sprite != c.s_mario_walking_l1 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_mario_walking_l1
                elif self.sprite != c.s_mario_walking_l2 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_mario_walking_l2
                elif self.sprite != c.s_mario_walking_l3 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_mario_walking_l3
            elif not self.__walking:
                self.sprite = c.s_mario_standing_l

    # This is the method that groups every method that mario needs to update,
    # this makes it easier to plug it on the board
    def update_status(self):
        self.__update_animations()
        self.__update_position()
        self.__detect_buttons()
        self.__gravity_push()
