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
import random


class Board:

    def __init__(self):
        self.__lives = 3
        self.__game_over = False
        self.__time_since_last_coin = 0
        self.__time_since_last_enemy = 0
        self.__blocks = None
        self.width = int(constants.screen_width)
        self.height = int(constants.screen_height)
        self.player = Mario(int(self.width / 2), 170)
        pyxel.init(self.width, self.height)
        pyxel.load("assets/sprites.pyxres")
        self.initialize_pipes()
        self.initialize_floor()
        self.__current_level = 1  # Initialize __current_level before calling generate_blocks
        self.generate_blocks(self.__current_level)
        self.create_ground()
        self.generate_enemies()
        self.generate_coins()
        pyxel.run(self.update, self.draw)
        self.__time_since_last_enemy = 0

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
        self.__floor = [
            self.create_floor(0, 55, 25),
            self.create_floor(225, 55, 25),
            self.create_floor(120, 100, 23),
            self.create_floor(0, 110, 6),
            self.create_floor(358, 110, 6),
            self.create_floor(0, 150, 23),
            self.create_floor(239, 150, 23),
        ]

    def create_floor(self, x, y, count):
        floors = []
        for i in range(count):
            floors.append(Floor(x, y))
            x += 7
        return floors

    def generate_coins(self):
        self.__coins = []

    def generate_enemies(self):
        self.__enemies = [
            Turtle(120, 10, 2, 2),
            Turtle(360, 10, -2, 2),
            Crab(40, 70, 2, 2),
            Crab(360, 70, -2, 2),
            Bicho(150, 10, 2, 2),
            Bicho(300, 10, 2, 2)
        ]
        if self.current_level == 1:
            self.__enemies = []

    def generate_blocks(self, current_level):
        self.__blocks = [
            Pow1(192, 150, 16)
        ]
        for floor_list in self.__floor:
            self.__blocks.extend(floor_list)

    def create_ground(self):
        x = 0
        for i in range(25):
            self.__blocks.append(Ground(x, constants.ground_height))
            x += 16

    def reset(self, level):
        self.__current_level = level
        self.initialize_pipes()
        self.initialize_floor()
        self.generate_blocks(self.__current_level)
        self.create_ground()
        self.generate_enemies()

    def handle_player_death(self):
        self.__lives -= 1

        if self.__lives > 0:
            self.player = Mario(int(constants.screen_width / 2), 170)
            if self.__lives == 2:
                pyxel.blt(20, 10, *(0, 200, 56, 11, 9))
            elif self.__lives == 1:
                pyxel.blt(35, 10, *(0, 200, 56, 11, 9))
        else:
            quit()

    def update(self):
        if not self.player.should_be_removed():
            self.player.update_status(self.__blocks, self.__enemies)
            self.update_enemies_and_coins()
        else:
            self.handle_player_death()

    def update_enemies_and_coins(self):
        if self.__time_since_last_enemy >= 100 and len(self.__enemies) < 30:
            last_enemy = self.__enemies[-1] if self.__enemies else None
            new_enemy_x = 0 if not last_enemy or last_enemy.x == 400 else 400
            new_enemy_speed = 2 if not last_enemy or last_enemy.x == 400 else -2
            self.n = random.randint(1, 3)
            if self.n == 1:
                new_enemy = Turtle(new_enemy_x, 18, new_enemy_speed, 2)
            elif self.n == 2:
                new_enemy = Crab(new_enemy_x, 18, new_enemy_speed, 2)
            else:
                new_enemy = Bicho(new_enemy_x, 18, new_enemy_speed, 2)

            self.__enemies.append(new_enemy)
            self.__time_since_last_enemy = 0
        else:
            self.__time_since_last_enemy += 1

        if self.__time_since_last_coin >= 400:
            last_coin = self.__coins[-1] if self.__coins else None
            new_coin_x = 0 if not last_coin or last_coin.x == 116 else 116
            new_coin_speed = 2 if not last_coin or last_coin.x == 116 else -2
            new_coin = Coin(new_coin_x, 18, new_coin_speed, 2)

            self.__coins.append(new_coin)
            self.__time_since_last_coin = 0
        else:
            self.__time_since_last_coin += 1

        for enemy in self.__enemies:
            enemy.update_status(self.__blocks, self.__enemies, self.player, self.__coins)

        self.__enemies = [enemy for enemy in self.__enemies if not enemy.should_be_removed()]

        for coin in self.__coins:
            coin.update_status(self.__blocks, self.__enemies, self.__coins, self.player)

        self.__coins = [coin for coin in self.__coins if not coin.dead]

    def levels(self):
        if all(enemy.dead for enemy in self.__enemies):
            pyxel.cls(0)
            pyxel.text(80, 80, f'Level {self.__current_level + 1}!', 7)
            pyxel.flip()
            self.reset(self.__current_level + 1)

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.x, self.player.y, *self.player.sprite)
        for enemy in self.__enemies:
            pyxel.blt(enemy.x, enemy.y, *enemy.sprite)

        for coin in self.__coins:
            pyxel.blt(coin.x, coin.y, *coin.sprite)

        for pipe in self.__pipes:
            pyxel.blt(pipe.x, pipe.y, *pipe.sprite)

        for ground in self.__blocks:
            pyxel.blt(ground.x, ground.y, *ground.sprite)

        if self.__lives == 3:
            pyxel.blt(20, 10, *(0, 2, 3, 11, 9))
            pyxel.blt(35, 10, *(0, 2, 3, 11, 9))
            pyxel.blt(50, 10, *(0, 2, 3, 11, 9))
        elif self.__lives == 2:
            pyxel.blt(35, 10, *(0, 2, 3, 11, 9))
            pyxel.blt(50, 10, *(0, 2, 3, 11, 9))
        elif self.__lives == 1:
            pyxel.blt(50, 10, *(0, 2, 3, 11, 9))
