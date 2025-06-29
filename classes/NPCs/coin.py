import pyxel
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

    @property
    def v_y(self):
        return self.__v_y

    # Here we initialize the values that ar true or False
    def __initialize_booleans(self):
        self.__dead = False
        self.__coin_in_air = False
        self.__stopping = False
        self.first = True
        self.second = True
        self.third = True
        self.fourth = True

    # Here we initialize the values for the forces x and y acting on mario

    # This is the method that detects every button pressed and stores information to give it to other methods

    # This is the method that changes mario's position every frame
    def __update_position(self):
        # Update the position of the turtle, wrapping around the screen if necessary
        if self.x > c.screen_width and self.y > 150:
            self.x = c.screen_width -10
            self.y = 10
            self.__v_x = -self.__v_x
        elif self.x < 0 and self.y > 150:
            self.x = 10
            self.y = 10
            self.__v_x = -self.__v_x
        elif self.x > c.screen_width:
            self.x = 0
        elif self.x < 0:
            self.x = c.screen_width
        else:
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

    def __collide_player(self, player, coins: list):
        if self.__is_colliding(player):
            self.__dead = True

    def __collide_enemies(self, enemies: list):
        for enemy in enemies:
            if self.__is_colliding(enemy):
                # Adjust position and direction when colliding with enemies
                if self.x < enemy.x:
                    self.x = enemy.x - self.width
                    self.__v_x = -self.__v_x
                else:
                    self.x = enemy.x + enemy.width
                    self.__v_x = -self.__v_x

    def __collide_blocks(self, blocks: list, ):
        for block in blocks:

            if self.__is_colliding(block):  # check for collision

                self.__coin_in_air = False
                self.y = block.y - self.height
                self.__v_y = 0

    def __collide_coins(self, coins: list):
        for coin in coins:
            if coin is not self and self.__is_colliding(coin):
                # Adjust position and direction when colliding with enemies
                if self.x < coin.x:
                    self.x = coin.x - self.width

                    self.__looking_right = True
                else:
                    self.x = coin.x + coin.width

                    self.__looking_right = False

                self.__v_x = -self.__v_x
                self.__looking_right = not self.__looking_right

    def __gravity_push(self):

        if self.y < pyxel.height:
            self.__v_y += c.gravity

    # This is the method that, following the input we give him when we press a button,
    # changes the model of mario every x frames
    def __update_animations(self):
        coin_frames = [c.s_coin_1, c.s_coin_2, c.s_coin_3, c.s_coin_4, c.s_coin_5]
        frame_index = int((pyxel.frame_count / (c.fps / 30)) % len(coin_frames))
        self.sprite = coin_frames[frame_index]

    # This is the method that groups every method that mario needs to update,
    # this makes it easier to plug it on the board
    def update_status(self, blocks: list, enemies, coins, player):
        self.__update_animations()
        self.__update_position()
        self.__gravity_push()
        self.__collide_blocks(blocks)
        self.__collide_enemies(enemies)
        self.__collide_coins(coins)
        self.__collide_player(player, coins)
