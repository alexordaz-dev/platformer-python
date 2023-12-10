import pyxel

import constants
import constants as c


class Turtle:
    def __init__(self, x: int, y: int, ) -> None:
        # Here we initialize all the methods and properties we will be having for mario
        self.x = x
        self.y = y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__sprite = c.s_turtle_standing
        self.__initialize_booleans()
        self.__initialize_forces()

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

    # Here we initialize the values that ar true or False
    def __initialize_booleans(self):
        self.__looking_right = True
        self.__walking = False
        self.__dead = False
        self.__turtle_in_air = False
        self.__stopping = False

    # Here we initialize the values for the forces x and y acting on mario
    def __initialize_forces(self):
        self.__v_x = 2
        self.__v_y = 2

        # This is the method that detects every button pressed and stores information to give it to other methods

    def friction(self):

        if self.__v_x != 0 and not self.__turtle_in_air:
            friction_direction = 1 if self.__v_x > 0 else -1 if self.__v_x < 0 else 0
            self.__v_x = max(abs(self.__v_x) - c.friction, 0) * friction_direction
            self.__stopping = True
            self.__walking = False
        elif self.__v_x != 0 and self.__turtle_in_air:
            friction_direction = 1 if self.__v_x > 0 else -1 if self.__v_x < 0 else 0
            self.__v_x = max(abs(self.__v_x) - c.friction_air, 0) * friction_direction
            self.__stopping = True
            self.__walking = False
        else:
             self.__walking = False
             self.__stopping = False

    # This is the method that changes mario's position every frame
    def __update_position(self):  # changes the player position
        self.x += self.__v_x
        self.y += self.__v_y

    def __is_colliding(self, entity):
        if (abs(entity.x - self.x) < entity.width and entity.x - self.width < self.x and
                abs(entity.y - self.y) < self.height):  # check for collision
            if entity.width == 256 and entity.x + 24 < self.x + self.width:  # check for a cliff
                return False
            else:
                return True
        else:
            return False

    def __collide_blocks(self, blocks: list, player):
        for block in blocks:

            if self.__is_colliding(block):  # check for collision

                self.__turtle_in_air = False
                self.y = block.y - self.height
                self.__v_y = 0


    def __gravity_push(self):

        if self.y < pyxel.height:
            self.__v_y += c.gravity
        else:
            self.die()

    # This is the method that, following the input we give him when we press a button,
    # changes the model of mario every x frames
    def __update_animations(self):
        if self.looking_right:
            if self.__turtle_in_air:
                self.sprite = c.s_turtle_standing
            else:
                if self.sprite != c.s_turtle_walking_r1 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_turtle_walking_r1
                elif self.sprite != c.s_turtle_walking_r2 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_turtle_walking_r2
        else:
            if self.__turtle_in_air:
                self.sprite = c.s_turtle_standing_l
            elif self.__walking:
                if self.sprite != c.s_turtle_walking_l1 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_turtle_walking_l1
                elif self.sprite != c.s_turtle_walking_l2 and pyxel.frame_count % (c.fps / 30) == 0:
                    self.sprite = c.s_turtle_walking_l2

    # This is the method that groups every method that mario needs to update,
    # this makes it easier to plug it on the board
    def update_status(self, blocks: list, turtle):
        self.__update_animations()
        self.__update_position()
        self.__gravity_push()
        self.__collide_blocks(blocks, turtle)




