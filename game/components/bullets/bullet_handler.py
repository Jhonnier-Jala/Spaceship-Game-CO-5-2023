from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.utils.constants import BULLET_ENEMY_TYPE, SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy

class BulletHandler:
    def __init__(self):
        self.bullets = []
    
    def update(self, player):
        for bullet in self.bullets:
            bullet.update(player)
            if bullet.rect.top >= SCREEN_HEIGHT:
                self.bullets.remove(bullet)
                # print(len(self.bullets))

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == DEFAULT_TYPE:
            self.bullets.append(BulletSpaceship(center))

    def remove_bullet(self,bullet):
        self.bullets.remove(bullet)