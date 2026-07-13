import math
import pygame
from constants import HEIGHT, WIDTH

class attack:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    def move(self):
        self.x += self.direction[0] * 10
        self.y += self.direction[1] * 10
        if(self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT):
            return False
        return True
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), 10)