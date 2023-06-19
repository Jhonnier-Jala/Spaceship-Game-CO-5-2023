import pygame
from game.components.helps.ally_ship import AllyShip
from game.components.levels.level_handler import LevelHandler

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components import text_utils
from game.components.power.power_handled import PowerHandled
from game.components.helps.lifes import Life


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
        self.score = 0
        self.number_death = 0
        self.max_score = 0
        self.power_type = DEFAULT_TYPE
        self.power_time = 0
        self.power_handled = PowerHandled()
        self.ally_ship = AllyShip()
        self.level_handler = LevelHandler()
        self.time_next_level = 0
        self.enemies_nex_level = 3
        self.lives = Life()

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
        if self.playing:
            user_input = pygame.key.get_pressed()
            # if self.level_handler.current_level_index == 0:
            #     self.level_handler.add_level(self.enemies_nex_level)
            # else:
            #     if self.level_handler.is_level_completed():
            #         self.enemies_nex_level += 2
            #         self.level_handler.add_level(self.enemies_nex_level)
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score = self.enemy_handler.number_enemy_destroyed
            self.power_handled.update(self.player)
            self.ally_ship.update(self.bullet_handler)
            # self.level_handler.update(self.bullet_handler)

            if not self.player.is_alive:
                self.lives.reduce_life()
                self.player.is_alive = True
            self.score_player()
            if self.lives.is_game_over():
                pygame.time.delay(300)
                self.playing = False
                self.number_death += 1

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)    
            self.lives.draw(self.screen)   
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_handled.draw(self.screen)
            self.ally_ship.draw(self.screen)
            self.draw_score()
            self.draw_level()
            self.draw_power_time()
            # if self.level_handler.is_level_completed():
            #     self.enemy_handler.increase_level()
            #     self.level_handler.draw()
            
        else:
            self.draw_menu()
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
        if self.number_death == 0:
            text, text_rect = text_utils.get_message('Press any Key to Start', 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press any Key to Restart', 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE_COLOR, height=SCREEN_HEIGHT//2 +50)
            max_score, max_score_rect = text_utils.get_message(f'Your Max score is: {self.max_score}', 30, WHITE_COLOR, height=SCREEN_HEIGHT//2+70)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(max_score, max_score_rect)
        
    def score_player(self):
        self.score = self.enemy_handler.number_enemy_destroyed
        if self.score > self.max_score:
            self.max_score = self.score
    
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'score: {self.score}', 15, WHITE_COLOR, 1000, 40)
        max_score, max_score_rect = text_utils.get_message(f'Max score: {self.max_score}', 15, WHITE_COLOR, 1000, 55)
        self.screen.blit(score, score_rect)
        self.screen.blit(max_score, max_score_rect)

    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time -pygame.time.get_ticks()) /100,2)

            if power_time >= 0:
                text_power, text_power_rect = text_utils.get_message(f'{self.player.power_type.capitalize()} is enable for {power_time}', 15, WHITE_COLOR, 100, 40)
                self.screen.blit(text_power, text_power_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()
    
    def draw_level(self):
        level, level_rect = text_utils.get_message(f'Level: {self.enemy_handler.current_level}', 15, WHITE_COLOR, 1000, 70)
        self.screen.blit(level, level_rect)

        
    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_handled.reset()
        self.lives.reset()
        self.score = 0
