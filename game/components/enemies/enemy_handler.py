import random
from game.components.enemies.ship import Ship
from game.components.enemies.ship_white_lvl2 import ShipWhite
from game.components.enemies.ship_ovni import ShipOvni

class EnemyHandler:
    SHIP_TYPES = [Ship, ShipWhite, ShipOvni]

    def __init__(self):
        self.enemies = []
        self.timer = 0
        self.delay = 100
    
    def update(self, bullet_handler):
        # self.timer += 1
        self.add_enemy()
        # if self.timer >= self.delay:
        #     # self.enemies.append(Ship())
        #     self.timer = 0
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        ship_type = random.choice(self.SHIP_TYPES)
        enemy = ship_type()
        if len(self.enemies) < 2:
            self.enemies.append(enemy)
            
    def remove_enemy(self,enemy):
        self.enemies.remove(enemy)