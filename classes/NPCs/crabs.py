import pyxel
import constants as c


class Crab:
    def __init__(self, x: int, y: int, __v_x: int, __v_y: int) -> None:
        self.x = x
        self.y = y
        self.__v_x = __v_x
        self.__v_y = __v_y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__initialize_booleans()
        self.__initialize_sprint()

    @property
    def v_x(self):
        return self.__v_x

    @property
    def looking_right(self):
        return self.__looking_right

    @property
    def v_y(self):
        return self.__v_y

    def __initialize_booleans(self):
        self.__turning_right = False
        self.__turning_left = False
        self.__turning_frames = 0

        if self.__v_x > 0:
            self.__looking_right = True
        elif self.__v_x < 0:
            self.__looking_right = False

    def __initialize_sprint(self):
        if self.__looking_right:
            self.sprite = c.s_crab_walking_r1
        else:
            self.sprite = c.s_crab_walking_l1

    def __update_position(self):
        if self.x > c.screen_width:
            self.x = 0
        elif self.x < 0:
            self.x = c.screen_width
        else:
            self.x += self.__v_x
            self.y += self.__v_y

    def __is_colliding(self, entity):
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
                # Ajustar posición en el eje X
                if self.x < enemy.x:
                    self.x = enemy.x - self.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = True
                else:
                    self.x = enemy.x + enemy.width
                    self.__turning_frames = c.turning_animation_frames
                    self.__looking_right = False

                # Establecer la dirección del cangrejo según la dirección del enemigo
                self.__v_x = -self.__v_x
                self.__looking_right = not self.__looking_right

    def __collide_player(self, player):
        if self.__is_colliding(player):
            if self.x < player.x:
                self.x = player.x - self.width
                self.__turning_frames = c.turning_animation_frames
                self.__looking_right = False
            else:
                self.x = player.x + player.width
                self.__turning_frames = c.turning_animation_frames
                self.__looking_right = True

    def __collide_blocks(self, blocks: list):
        for block in blocks:
            if self.__is_colliding(block):  # check for collision
                self.y = block.y - self.height
                self.__v_y = 0

    def __gravity_push(self):
        if self.y < pyxel.height:
            self.__v_y += c.gravity

    def __update_animations(self):

        if self.__turning_frames > 0:
            turning_frames = [c.s_crab_turning_r1, c.s_crab_turning_r2] if self.__looking_right else [
                c.s_crab_turning_l1, c.s_crab_turning_l2]
            frame_index = int(((c.turning_animation_frames - self.__turning_frames) / c.turning_animation_frames) * len(
                turning_frames))
            self.sprite = turning_frames[frame_index]
            self.__v_x = 0
            self.__turning_frames -= 1
        else:
            self.__v_x = 2
            walking_frames = [c.s_crab_walking_r1, c.s_crab_walking_r2, c.s_crab_walking_r3]
            if not self.__looking_right:
                self.__v_x = -2
                walking_frames = [c.s_crab_walking_l1, c.s_crab_walking_l2, c.s_crab_walking_l3]
            frame_index = int((pyxel.frame_count / (c.fps / 30)) % len(walking_frames))
            self.sprite = walking_frames[frame_index]

    def update_status(self, blocks: list, enemies, player):
        self.__update_animations()
        self.__update_position()
        self.__gravity_push()
        self.__collide_blocks(blocks, )
        self.__collide_enemies(enemies)
        self.__collide_player(player)
