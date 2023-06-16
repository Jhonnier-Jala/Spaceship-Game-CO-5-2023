import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_4, SCREEN_HEIGHT

class ShipRed(Enemy):
    WIDHT = 60
    HEIGHT = 80
    SPEED_X = [i for i in range(10)]
    SPEED_Y = [i for i in range(5)]

    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        self.speed_x = random.choice(self.SPEED_X)
        self.speed_y = random.choice(self.SPEED_Y)
        super().__init__(self.image, self.speed_x, self.speed_y)
