import math
import pygame

class BoomerangMonkey(Tower): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 300
        self.price = None
        self.damage = None
        self.img = pygame.image.load("images/tower_images/dartm.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (60, 60))
        self.reload_tick = [0, 20]  # number of frames to wait before shooting again
        self.is_reloading = False
        self.width = self.img.get_width()
        self.height = self.img.get_height()