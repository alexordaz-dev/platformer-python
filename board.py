import pyxel
from classes import mario
from classes.blocks.pipes import Pipes
from classes.blocks.floor import Floor
from classes.blocks.ground import Ground
from classes.blocks.pow import Pow1
from classes.NPCs.turtles import Turtle
from classes.NPCs.crabs import Crab
from classes.NPCs.coin import Coin
import constants


class Board:

    def __init__(self, ):
        self.__blocks = None
        self.width = int(constants.screen_width)
        self.height = int(constants.screen_height)
        # For mario here we name an object called player
        self.player = mario.Mario(int(self.width / 2), 170)
        self.coin = [Coin(90, 10, 3, 3), Coin(300, 10, -2, 2)]
        pyxel.init(self.width, self.height)
        pyxel.load("assets/sprites.pyxres")
        self.initialize_pipes()
        self.initialize_floor()
        self.generate_blocks()
        self.create_ground()
        self.generate_enemies()
        pyxel.run(self.update, self.draw)



    def initialize_pipes(self):
        self.__pipes = [
            Pipes(0, 20, "left", "no_straight"),
            Pipes(368, 20, "right", "no_straight"),
            Pipes(0, 175, "left", "straight"),
            Pipes(358, 175, "right", "straight")
        ]

    def initialize_floor(self):
        self.floor = self.create_floor(0, 55, 25)
        self.floor2 = self.create_floor(225, 55, 25)
        self.floor3 = self.create_floor(120, 100, 23)
        self.floor4 = self.create_floor(0, 110, 6)
        self.floor5 = self.create_floor(358, 110, 6)
        self.floor6 = self.create_floor(0, 150, 23)
        self.floor7 = self.create_floor(239, 150, 23)

    def create_floor(self, x, y, count):
        floors = []
        for i in range(count):
            floors.append(Floor(x, y, 1))
            x += 7
        return floors

    def generate_enemies(self):
        self.__enemies = [
            Turtle(10, 10, 2, 2),
            Turtle(360, 10, -2, 2),
            Crab(40, 70, 2, 2),
            Crab(360, 70, -2, 2)
        ]

    def generate_blocks(self):
        self.__blocks = [
            Floor(0, 150, 160),
            Floor(239, 150, 160),
            Floor(225, 55, 170),
            Floor(120, 100, 155),
            Floor(0, 110, 54),
            Floor(358, 110, 60),
            Floor(0, 55, 170),
            Pow1(192, 150, 16)
        ]

    def create_ground(self):
        x = 0
        for i in range(25):
            self.__blocks.append(Ground(x, constants.ground_height))
            x += 16

    def update(self):
        # For mario we only need to call the update method, this will do all the things for mario
        for enemy in self.__enemies:
            enemy.update_status(self.__blocks, self.__enemies, )
        for coin in self.coin:
            coin.update_status(self.__blocks,self.__enemies)
        self.player.update_status(self.__blocks, self.player)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # For mario we then draw his position and his firs sprite
        pyxel.blt(self.player.x, self.player.y, *self.player.sprite)

        for enemy in self.__enemies:
            pyxel.blt(enemy.x, enemy.y, *enemy.sprite)

        for coin in self.coin:
            pyxel.blt(coin.x, coin.y, *coin.sprite)

        for pipe in self.__pipes:
            pyxel.blt(pipe.x, pipe.y, *pipe.sprite)

        for floors in self.floor + self.floor2 + self.floor3 + self.floor4 + self.floor5 + self.floor6 + self.floor7:
            pyxel.blt(floors.x, floors.y, *floors.sprite)

        for grounds in self.__blocks:
            pyxel.blt(grounds.x, grounds.y, *grounds.sprite)
