from game.components.enemies.ship import Ship

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyer = 0
        self.timer = 0
        self.delay = 100
    
    def update(self, bullet_handler):
        self.timer += 1
        if self.timer >= self.delay:
            self.enemies.append(Ship())
            self.timer = 0
        for enemy in self.enemies:
            enemy.update(bullet_handler)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 2:
            self.enemies.append(Ship())
            
    def remove_enemy(self,enemy):
        self.enemies.remove(enemy)
    
    def reset(self):
        self.enemies = []