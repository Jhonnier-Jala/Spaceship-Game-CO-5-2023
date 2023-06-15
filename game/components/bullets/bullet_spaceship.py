import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletSpaceship(Bullet):
    WIDTH = 5
    HEIGHT = 15
    SPEED = 20
    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, enemy):
        self.rect.y -= self.SPEED
        if self.rect.colliderect(enemy.rect):
            enemy.is_alive = False

