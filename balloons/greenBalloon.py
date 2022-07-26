from balloons.balloon import Balloon
import pygame


class GreenBalloon(Balloon):
    def __init__(self, x, y, path_index):
        super().__init__(self, x, y, path_index)
        self.img = pygame.image.load(
            "images/balloon_images/greenballoon.png"
        ).convert_alpha()
        img_size = (31, 35)
        self.img = pygame.transform.scale(self.img, img_size)
        self.health = 3
        self.damage = 3
