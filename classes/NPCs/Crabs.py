import constants as c

class Crab:
    def __init__(self, x: int, y: int, ) -> None:
        # Here we initialize all the methods and properties we will be having for mario
        self.x = x
        self.y = y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__sprite = c.s_crab_standing

class GreenCrab:
    def __init__(self, x: int, y: int, ) -> None:
        # Here we initialize all the methods and properties we will be having for mario
        self.x = x
        self.y = y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__sprite = c.s_greencrab_standing

class BlueCrab:
    def __init__(self, x: int, y: int, ) -> None:
        # Here we initialize all the methods and properties we will be having for mario
        self.x = x
        self.y = y
        self.width = c.NPCS_width
        self.height = c.NPCs_height
        self.__sprite = c.s_bluecrab_standing