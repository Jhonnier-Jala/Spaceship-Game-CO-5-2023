import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_BOT_TYPE

class BulletAllyShip(Bullet):
    WIDTH = 20
    HEIGHT = 30
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, BULLET_BOT_TYPE, center)

    def update(self, enemy):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0:
            self.is_alive = False
        super().update(enemy)
        if not self.is_alive:
            enemy.is_destroyed = True
        


