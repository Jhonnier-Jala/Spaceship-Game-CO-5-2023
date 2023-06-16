import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_PLAYER_TYPE

class BulletSpaceship(Bullet):
    WIDTH = 10
    HEIGHT = 25
    SPEED = 20
    def __init__(self, center):
        self.image = BULLET
        self.type = BULLET_PLAYER_TYPE
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center, self.type)

    def update(self, enemy):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0:
            enemy.is_alive = False
        super().update(enemy)
        if not self.is_alive:
            enemy.is_destroyed = True
