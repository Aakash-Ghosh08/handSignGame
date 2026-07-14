import math
import pygame
from constants import HEIGHT, WIDTH

class fireball:
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
    def type(self):
        return "fireball"
    def radius(self):
        return 10
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), 10)
        
class lightening:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    def move(self):
        self.x += self.direction[0] * 15
        self.y += self.direction[1] * 15
        if(self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT):
            return False
        return True
    def type(self):
        return "lightening"
    def radius(self):
        return 30
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), (int(self.x), int(self.y)), 30)