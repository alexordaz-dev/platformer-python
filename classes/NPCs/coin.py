import pyxel

import constants
import constants as c


class Coin:
    def __init__(self, x: int, y: int, __v_x: int, __v_y: int, ) -> None:
        # Here we initialize all the methods and properties we will be having for mario
        self.x = x
        self.y = y
        self.__v_x = __v_x
        self.__v_y = __v_y
        self.width = c.coin_width
        self.height = c.NPCs_height
        self.sprite = c.s_coin_1
        self.__initialize_booleans()

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
    def v_y(self):
        return self.__v_y


    # Here we initialize the values that ar true or False
    def __initialize_booleans(self):
        self.__dead = False
        self.__coin_in_air = False
        self.__stopping = False

    # Here we initialize the values for the forces x and y acting on mario


        # This is the method that detects every button pressed and stores information to give it to other methods


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

                self.__coin_in_air = False
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
                if self.sprite != c.s_coin_1 and pyxel.frame_count % (c.fps / 15) == 0:
                    self.sprite = c.s_coin_1
                elif self.sprite != c.s_coin_2 and pyxel.frame_count % (c.fps / 15) == 0:
                    self.sprite = c.s_coin_2
                elif self.sprite != c.s_coin_3 and pyxel.frame_count % (c.fps / 15) == 0:
                    self.sprite = c.s_coin_3
                elif self.sprite != c.s_coin_4 and pyxel.frame_count % (c.fps / 15) == 0:
                    self.sprite = c.s_coin_4
                elif self.sprite != c.s_coin_5 and pyxel.frame_count % (c.fps / 15) == 0:
                    self.sprite = c.s_coin_5
    # This is the method that groups every method that mario needs to update,
    # this makes it easier to plug it on the board
    def update_status(self, blocks: list, coin):
        self.__update_animations()
        self.__update_position()
        self.__gravity_push()
        self.__collide_blocks(blocks, coin)




