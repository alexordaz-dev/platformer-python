import pyxel
import constants as c


class Bicho:
    def __init__(self, x: int, y: int, __v_x: int, __v_y: int) -> None:
        self.x = x
        self.y = y
        self.__v_x = __v_x
        self.__v_y = __v_y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__initialize_booleans()
        self.sprite = c.s_bicho_1
        self.__rebound_frames = 4
        self.__turned = False
        self.__time_since_last_punch = 0
        self.__dead = False

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
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, new):
        self.__dead = new

    def set_dead(self):
        if self.__dead:
            self.__dead = True

    def should_be_removed(self):
        return self.__dead
    def __initialize_booleans(self):
        # Initialize boolean flags for turning and looking direction
        self.__turning_right = False
        self.__turning_left = False
        self.__turning_frames = 0
        self.__punched = False

        # Determine initial looking direction based on velocity
        if self.__v_x > 0:
            self.__looking_right = True
        elif self.__v_x < 0:
            self.__looking_right = False

    def jump(self):
        if self.__v_y == 0:
            self.__v_y = -c.bicho_jump

    def __update_position(self):
        # Update the position of the turtle, wrapping around the screen if necessary
        if self.x > c.screen_width and self.y > 150:
            self.x = c.screen_width - 10
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
        # Check for collision with another entity based on bounding boxes
        if (
                abs(entity.x - self.x) < entity.width
                and entity.x - self.width < self.x
                and abs(entity.y - self.y) < self.height
        ):  # check for collision
            return True
        else:
            return False

    def __collide_enemies(self, enemies: list):
        for enemy in enemies:
            if enemy is not self and self.__is_colliding(enemy):
                # Adjust position and direction when colliding with enemies
                if self.x < enemy.x:
                    self.x = enemy.x - self.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = True
                else:
                    self.x = enemy.x + enemy.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = False

                # Reverse the turtle's direction and update looking direction
                self.__v_x = -self.__v_x
                self.__looking_right = not self.__looking_right

    def __collide_coins(self, coins: list):
        for coin in coins:
            if self.__is_colliding(coin):
                # Adjust position and direction when colliding with enemies
                if self.x < coin.x:
                    self.x = coin.x - self.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = True
                else:
                    self.x = coin.x + coin.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = False

    def __collide_player(self, player):
        if self.__is_colliding(player):
            if not self.__turned:
                player.dead = True
                # Adjust position and direction when colliding with the player
                if self.x < player.x:
                    self.x = player.x - self.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = False
                else:
                    self.x = player.x + player.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = True
            if self.__turned:
                self.set_dead()

    def __collide_blocks(self, blocks: list):
        for block in blocks:
            if self.__is_colliding(block):  # check for collision
                # Adjust position and stop vertical movement when colliding with blocks
                self.y = block.y - self.height
                self.__v_y = 0
                if not self.__turned: self.jump()

    def __gravity_push(self):
        # Apply gravity force to the turtle if it is not at the bottom of the screen
        if self.y < pyxel.height:
            self.__v_y += c.gravity

    def __turn_upside(self, player):
        if abs((player.y - player.height) - (self.y + self.height)) < 1 and abs(player.x - self.x) < 14:
            if self.__time_since_last_punch == 0 or self.__time_since_last_punch > 20:
                self.__punched = True
                self.__time_since_last_punch = 1

    def __update_animations(self,player):
        if self.__turned and self.__is_colliding(player):
            self.__dead = True  # Set turtle as dead when the death animation is complete
        if self.__turning_frames > 0:
            # Animate turning with appropriate sprite frames
            turning_frames = [c.s_bicho_1, c.s_bicho_1] if self.__looking_right else [
                c.s_bicho_1, c.s_bicho_1]
            frame_index = int(((c.turning_animation_frames - self.__turning_frames) / c.turning_animation_frames) * len(
                turning_frames))
            self.sprite = turning_frames[frame_index]
            self.__v_x = 0
            self.__turning_frames -= 1
        elif self.__punched and self.__rebound_frames > 0:
            self.__v_x = 0
            self.__v_y = -2.5
            self.sprite = c.s_bichoupsidedown_1
            self.__rebound_frames -= 1
        elif self.__punched and self.__rebound_frames == 0:
            self.__punched = False
            self.__time_since_last_punch = 0
            if self.__turned:
                self.__turned = False
                self.__v_y = -3
            else:
                self.__turned = True
        elif self.__turned:
            self.__v_x = 0
            self.sprite = c.s_bichoupsidedown_2
        else:
            # Animate walking with appropriate sprite frames
            self.__v_x = c.npc_v
            walking_frames = [c.s_bicho_1, c.s_bicho_2, c.s_bicho_3]
            if not self.__looking_right:
                self.__v_x = -c.npc_v
                walking_frames = [c.s_bicho_1, c.s_bicho_2, c.s_bicho_3]
            frame_index = int((pyxel.frame_count / (c.fps / 30)) % len(walking_frames))
            self.sprite = walking_frames[frame_index]
            self.__punched = False
            self.__turned = False
            self.__time_since_last_punch = 0
            self.__rebound_frames = 4

    def update_status(self, blocks: list, enemies, player, coins):
        # Update turtle status by calling individual methods
        self.__update_animations(player)
        self.__update_position()
        self.__gravity_push()
        self.__collide_blocks(blocks, )
        self.__collide_enemies(enemies)
        self.__collide_player(player)
        self.__collide_coins(coins)
        self.__turn_upside(player)
        self.should_be_removed()
