import pygame
from game.components.bullets.bullet_handler import BulletHandler
#from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components import text_util

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemi_handler.update(self.bullet_handler)
        self.bullet_handler.update(self.player)
        if not self.player.is_alive:
            pygame.time.delay(500)
            self.playing = False

    def draw(self):
        self.draw_background()
        self.player.draw(self.screen)
        self.enemi_handler.draw(self.screen)
        self.bullet_handler.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        text, text_rect = text_util.get_message("Press any key to Start", 30, WHITE_COLOR)
        self.screen.blit(text, text_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()