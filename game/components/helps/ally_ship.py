import pygame
from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.utils.constants import ALLY_SPACESHIP, SCREEN_WIDTH, BULLET_BOT_TYPE

class AllyShip:
    WIDTH = 40
    HEIGHT = 60
    REGENERATION_TIME = 300  # Tiempo de regeneración en frames
    SPEED = 5
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        self.image = ALLY_SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.shoot_timer = 0
        self.regeneration_timer = 0
        self.is_alive = True
        self.direction = 1

    def update(self, bullet_handler):
        if self.is_alive:
            self.shoot_timer += 1
            if self.shoot_timer >= 10:  # Disparar cada 10 frames
                self.shoot_timer = 0
                bullet_handler.add_bullet(BULLET_BOT_TYPE, self.rect.midtop)
            self.regeneration_timer += 1
            if not self.is_alive and self.regeneration_timer >= self.REGENERATION_TIME:
                self.regeneration_timer = 0
                self.is_alive = True
            self.move()

    def draw(self, screen):
        if self.is_alive:
            screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.SPEED * self.direction
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.direction = -1  # Cambiar dirección al llegar al borde derecho
        elif self.rect.left < 0:
            self.rect.left = 0
            self.direction = 1  # Cambiar dirección al llegar al borde izquierdo

    def reset(self):
        self.shoot_timer = 0
        self.regeneration_timer = 0
        self.is_alive = True
        self.direction = 1
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
