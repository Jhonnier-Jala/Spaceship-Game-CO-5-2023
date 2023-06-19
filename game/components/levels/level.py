import pygame
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.helps.ally_ship import AllyShip
from game.components import text_utils 
from game.utils.constants import WHITE_COLOR


class Level:
    def __init__(self, enemy_count, ally_count):
        self.enemy_handler = EnemyHandler()
        self.ally_ship = AllyShip()
        self.enemy_count = enemy_count
        self.ally_count = ally_count
        self.level_time = 0

    def update(self, bullet_handler):
        self.enemy_handler.update(bullet_handler)
        self.ally_ship.update(bullet_handler)

    def draw(self, screen):
        self.enemy_handler.draw(screen)
        self.ally_ship.draw(screen)

    def is_level_completed(self):
        return self.enemy_handler.number_enemy_destroyed >= self.enemy_count

    def reset(self):
        self.enemy_handler.reset()
        self.ally_ship.reset()


