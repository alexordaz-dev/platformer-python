import constants as c

class Pow1:

    def __init__(self, x: int, y: int, width):
        self.x = x
        self.y = y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__sprite = c.s_pow_1
        self.collision_count = 0  # Contador de colisiones

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, new_sprite: list):
        self.__sprite = new_sprite
    def update_status(self, player):
        if self.__is_colliding(player):
            self.collision_count += 1
            self.__update_sprite()

    def __is_colliding(self, player):
        return (
            self.x < player.x + player.width and
            self.x + self.width > player.x and
            self.y < player.y + player.height and
            self.y + self.height > player.y
        )

    def __update_sprite(self):
        if self.collision_count == 1:
            self.__sprite = c.s_pow_2
        elif self.collision_count == 2:
            self.__sprite = c.s_pow_3
        elif self.collision_count == 3:
            # El sprite desaparece (puedes definir un sprite de desaparición o simplemente establecer None)
            self.__sprite = (0,0,0,0,0,)
