import pyxel
from classes.mario import Mario
from classes.blocks.pipes import Pipes
from classes.blocks.floor import Floor
from classes.blocks.ground import Ground
from classes.blocks.pow import Pow1
from classes.NPCs.turtles import Turtle
from classes.NPCs.crabs import Crab
from classes.NPCs.bicho import Bicho
from classes.NPCs.coin import Coin
import constants


class Board:

    def __init__(self):
        self.__blocks = None
        self.width = int(constants.screen_width)
        self.height = int(constants.screen_height)
        self.player = Mario(int(self.width / 2), 170)
        pyxel.init(self.width, self.height)
        pyxel.load("assets/sprites.pyxres")
        self.initialize_pipes()
        self.initialize_floor()
        self.__current_level = 1  # Inicializa __current_level antes de llamar a generate_blocks
        self.generate_blocks(self.__current_level)
        self.create_ground()
        self.generate_enemies()
        self.generate_coins()
        pyxel.run(self.update, self.draw)

    @property
    def current_level(self):
        return self.__current_level

    @current_level.setter
    def current_level(self, value):
        self.__current_level = value
    def initialize_pipes(self):

        self.__pipes = [
            Pipes(0, 20, "left", "no_straight"),
            Pipes(368, 20, "right", "no_straight"),
            Pipes(0, 175, "left", "straight"),
            Pipes(358, 175, "right", "straight")
        ]

    def initialize_floor(self):
        self.__flor = [
            self.create_floor(0, 55, 25),
            self.create_floor(225, 55, 25),
            self.create_floor(120, 100, 23),
            self.create_floor(0, 110, 6),
            self.create_floor(358, 110, 6),
            self.create_floor(0, 150, 23),
            self.create_floor(239, 150, 23),
        ]

    def create_floor(self, x, y, count,):
        floors = []
        for i in range(count):
            floors.append(Floor(x, y))
            x += 7
        return floors

    def generate_coins(self):
        self.__coins = [Coin(90, 10, 3, 3),
                        Coin(300, 10, -2, 2)
                        ]

    def generate_enemies(self):
<<<<<<< Updated upstream
        self.__enemies = [
            Turtle(120, 10, 2, 2),
            Turtle(360, 10, -2, 2),
            Crab(40, 70, 2, 2),
            Crab(360, 70, -2, 2),
            Bicho(150, 10, 2, 2),
            Bicho(300, 10, 2, 2)
        ]
=======
        if self.current_level == 1:
            self.__enemies = [
                Turtle(120, 10, 2, 2),
                Turtle(360, 10, -2, 2),
                Crab(40, 70, 2, 2),
                Crab(360, 70, -2, 2)
            ]
>>>>>>> Stashed changes

    def generate_blocks(self, current_level):
        self.__blocks = [
            Pow1(192, 150, 16)
        ]

    def create_ground(self):
        x = 0
        for i in range(25):
            self.__blocks.append(Ground(x, constants.ground_height))
            x += 16

    def update(self):
        for floor_list in self.__flor:
            for floor in floor_list:
                floor.update_status(self.__current_level)
        for enemy in self.__enemies:
            enemy.update_status(self.__blocks, self.__enemies, self.player, self.__coins)
        for coin in self.__coins:
            coin.update_status(self.__blocks, self.__enemies, self.__coins, self.player)  # Pass the player object here
        self.player.update_status(self.__blocks, self.__enemies)
        self.levels(self.__current_level)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def levels(self, level):
        if all(enemy.dead for enemy in self.__enemies):
            pyxel.cls(0)
            pyxel.text(80, 80, f'¡Nivel {level + 1}!', 7)
            pyxel.flip()

            self.__current_level += 1
            self.initialize_pipes()
            self.initialize_floor()
            self.generate_blocks(self.__current_level)
            self.create_ground()
            self.generate_enemies()

    def draw(self):
        pyxel.cls(0)
        for enemy in self.__enemies:
            pyxel.blt(enemy.x, enemy.y, *enemy.sprite)

        for coin in self.__coins:
            pyxel.blt(coin.x, coin.y, *coin.sprite)

        for pipe in self.__pipes:
            pyxel.blt(pipe.x, pipe.y, *pipe.sprite)

        for floor_list in self.__flor:
            for floor in floor_list:
                pyxel.blt(floor.x, floor.y, *floor.sprite)

        for grounds in self.__blocks:
            pyxel.blt(grounds.x, grounds.y, *grounds.sprite)


