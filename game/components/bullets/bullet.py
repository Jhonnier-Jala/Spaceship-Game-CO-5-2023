


class Bullet:
    def __init__(self, image,center, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_alive = True

    def update(self, nave):
        if self.rect.colliderect(nave.rect):
            nave.is_alive = False
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)