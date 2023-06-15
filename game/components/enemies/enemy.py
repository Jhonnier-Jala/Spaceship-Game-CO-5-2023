import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE

class Enemy:
    X_POS_LIST = [i for i in range(50,SCREEN_WIDTH,50)]
    Y_POS = 20
    #SPEED_X = 5
    #SPEED_Y = 1
    LEFT = "left"
    RIGHT = "right"
    MOV_X = [LEFT,RIGHT]
    INTERVAL = 100
    SHOOTING_TIME = 30
    def __init__(self,image,speed_x,speed_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.index = 0
        self.is_alive = True
        self.shooting_time = 0
    
    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def move (self):
        # self.rect.y += self.SPEED_Y
        self.rect.y += self.speed_y
        if self.mov_x == self.LEFT:
            # self.rect.x -= self.SPEED_X
            self.rect.x -= self.speed_x
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0
        else:
            # self.rect.x += self.SPEED_X
            self.rect.x += self.speed_x
            if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0
        if self.index % 2 == 0:
            self.rect.y += self.speed_y
        self.index += 1

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)