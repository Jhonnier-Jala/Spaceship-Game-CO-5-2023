import pygame
import random
from game.components.power.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD

class PowerHandled:
    def __init__(self):
        self.powers = []
        self.when_appears = random.randint(3000, 7000)
        self.duration = random.randint(3000, 5000)

    def generate_power(self):
        power = Shield()
        self.powers.append(power)
        self.when_appears += random.randint(3000, 7000)

    def update(self,player):
        current_time = pygame.time.get_ticks()
        if len(self.powers) == 0 and current_time >= self.when_appears:
            self.generate_power()
        for power in self.powers:
            power.update()
            if player.rect.colliderect(power.rect):
                power.start_time = pygame.time.get_ticks()
                player.has_power = True
                player.power_time = power.start_time + (self.duration * 1000)
                player.set_power_image(SPACESHIP_SHIELD)


    def draw(self, screen):
        for power in self.powers:
            power.draw(screen)