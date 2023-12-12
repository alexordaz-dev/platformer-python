import pyxel

import constants as c


class Mario:

    def __init__(self, x: int, y: int, ) -> None:
        # Here we initialize all the methods and properties we will be having for mario
        self.x = x
        self.y = y
        self.width = c.mario_width
        self.height = c.mario_height
        self.__sprite = c.s_mario_standing
        self.__initialize_booleans()
        self.__initialize_forces()
        self.__score = 0
        self.__money = 0
        self.__lives = 3
        self.first = True
        self.__dead = None

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
        self.__mario_in_air = False
        self.__stopping = False
        self.__punch_block = False
        self.__collision_bottom_timer = 60

    # Here we initialize the values for the forces x and y acting on mario
    def __initialize_forces(self):
        self.__v_x = 0
        self.__v_y = 0

    def die(self):
        self.__lives -= 1
        self.dead = True
        if self.__lives == 0:
            quit()

        # This is the method that detects every button pressed and stores information to give it to other methods

    def __detect_buttons(self):
        if pyxel.btn(pyxel.KEY_D):
            self.__v_x = min(self.__v_x + c.normal_v, c.max_v_x)
            self.__looking_right = True
            self.__walking = True
        elif pyxel.btn(pyxel.KEY_A):
            self.__v_x = max(self.__v_x - c.normal_v, -c.max_v_x)
            self.__looking_right = False
            self.__walking = True
        else:
            # if no button pressed, friction applies in both directions
            if self.__v_x != 0 and not self.__mario_in_air:
                friction_direction = 1 if self.__v_x > 0 else -1 if self.__v_x < 0 else 0
                self.__v_x = max(abs(self.__v_x) - c.friction, 0) * friction_direction
                self.__stopping = True
                self.__walking = False
            elif self.__v_x != 0 and self.__mario_in_air:
                friction_direction = 1 if self.__v_x > 0 else -1 if self.__v_x < 0 else 0
                self.__v_x = max(abs(self.__v_x) - c.friction_air, 0) * friction_direction
                self.__stopping = True
                self.__walking = False
            else:
                self.__walking = False
                self.__stopping = False

    # This is the method that changes mario's position every frame
    def __update_position(self):  # changes the player position
        if self.x > c.screen_width:
            self.x = 0
        elif self.x < 0:
            self.x = c.screen_width
        else:
            self.x += self.__v_x
            self.y += self.__v_y

    def __is_colliding(self, entity):
        if (abs(entity.x - self.x) < entity.width and entity.x - self.width < self.x and
                abs(entity.y - self.y) < self.height):  # check for collision

            return True
        else:
            return False
    def __collide_blocks(self, blocks: list, ):
        self.lateral_collision = False

        for block in blocks:
            collision_top = False
            collision_bottom = False

            if self.__is_colliding(block):  # check for collision
                if abs(block.y + block.height - self.y) <= c.collide and not collision_top:
                    collision_bottom = True
                    self.y = block.y + block.height + 3
                    self.__v_y = 1.9

                elif abs(block.y - (self.y + self.height)) <= self.height and not collision_bottom:

                    if pyxel.btn(pyxel.KEY_SPACE):
                        self.__mario_in_air = True

                        self.__v_y = -c.jump_force
                    else:
                        collision_top = True
                        self.__mario_in_air = False
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
            if self.__mario_in_air:
                self.sprite = c.s_mario_jumping_r
            elif self.__walking:
                walking_frames = [c.s_mario_walking_r1, c.s_mario_walking_r2, c.s_mario_walking_r3]
                frame_index = int((pyxel.frame_count / (c.fps / 30)) % len(walking_frames))
                self.sprite = walking_frames[frame_index]
            elif self.__stopping:
                self.sprite = c.s_mario_stop
            else:
                self.sprite = c.s_mario_standing
        else:
            if self.__mario_in_air:
                self.sprite = c.s_mario_jumping_l
            elif self.__walking:
                walking_frames = [c.s_mario_walking_l1, c.s_mario_walking_l2, c.s_mario_walking_l3]
                frame_index = int((pyxel.frame_count / (c.fps / 30)) % len(walking_frames))
                self.sprite = walking_frames[frame_index]
            elif self.__stopping:
                self.sprite = c.s_mario_stop_l
            else:
                self.sprite = c.s_mario_standing_l

    # This is the method that groups every method that mario needs to update,
    # this makes it easier to plug it on the board
    def update_status(self, blocks: list, enemies):
        self.__update_animations()
        self.__update_position()
        self.__detect_buttons()
        self.__gravity_push()
        self.__collide_blocks(blocks)


