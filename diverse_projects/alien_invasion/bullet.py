import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_info["color"]
        self.rect = pygame.Rect(0, 0, self.settings.bullet_info["width"],
                                self.settings.bullet_info["height"])
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    #calling the sprite.Group update method calls the Bullet::
    # update method for each bullet instance in the Group
    def update(self):
        self.y -= self.settings.bullet_info["speed"]
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

