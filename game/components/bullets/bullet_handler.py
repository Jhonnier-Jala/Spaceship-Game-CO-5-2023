from game.components.helps.lifes import Life
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_BOT_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_spaceship import BulletSpaceship
from game.components.bullets.bullet_ally_ship import BulletAllyShip

class BulletHandler:
    def __init__(self):
        self.bullets = []
        self.live = Life()
    
    def update(self, player, enemies):
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.remove_bullet(bullet)
            else:
                if bullet.type == BULLET_ENEMY_TYPE:
                    bullet.update(player)
                    # self.live.reduce_life()
                elif bullet.type == BULLET_BOT_TYPE:
                    for enemy in enemies:
                        bullet.update(enemy)
                else:
                    for enemy in enemies:
                        bullet.update(enemy)
     
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_BOT_TYPE:
            self.bullets.append(BulletAllyShip(center))
        else:
            self.bullets.append(BulletSpaceship(center))
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
    
    def reset(self):
        self.bullets = []
