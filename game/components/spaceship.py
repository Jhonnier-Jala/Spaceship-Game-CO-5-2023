import pygame
from game.utils.constants import DEFAULT_TYPE, SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SHOOTING_TIME = 20
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0

    def update(self, user_input,bullet_handler):
        self.shooting_time += 1
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - (self.rect.width // 2)
            
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0 - (self.rect.width // 2)

    def move_up(self):
        if self.rect.y > (SCREEN_HEIGHT // 2) - 40:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < (SCREEN_WIDTH // 2) - 60:
            self.rect.y += 10

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(DEFAULT_TYPE, self.rect.center)

    