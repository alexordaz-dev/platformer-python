class Floor:

    def __init__(self, x: int, y: int, ):

        self.x = x
        self.y = y
        self.__sprite = ()
        self.width = 7
        self.height = 7

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, new_sprite: list):
        self.__sprite = new_sprite

    def __sprite_change(self, level):
        if level == 1 or 2 or 3:
            self.__sprite = (0, 0, 8, 232, 8, 8)
        elif level == 3 or 4 or 5:
            self.__sprite = (0, 0, 8, 232, 8, 8)
        else:
            self.__sprite = (0, 0, 8, 232, 8, 8)

    def update_status(self, level):
        # Update turtle status by calling individual methods
        self.__sprite_change(level)
