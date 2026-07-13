import pygame
from attack import fireball, lightening
from constants import WIDTH, HEIGHT
import helperMethods

class player:
    def __init__(self, x, y, color, name="Player"):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = color
        self.name = name
        self.speed = 5
        self.shield = False
        self.attacks = []
        self.cooldown = 0
        self.health = 100
        self.isDead = False
        self.handSigns = []

    def move(self, direction):
        self.x += direction[0] * self.speed
        self.y += direction[1] * self.speed
        if(self.x < 0):
            self.x = 0
        elif(self.x > WIDTH):
            self.x = WIDTH
        if(self.y < 0):
            self.y = 0
        elif(self.y > HEIGHT):
            self.y = HEIGHT
        
    def update(self, other):
        for attack in self.attacks:
            if not attack.move():
                self.attacks.remove(attack)
                
        self.cooldown = max(0, self.cooldown - 1)
        
        self.checkCollision(other)
        
        if(self.health <= 0):
            self.color = (255, 0, 0)
            self.isDead = True
            
        if(len(self.handSigns) > 5):
            self.handSigns.pop(0)            
        
    def activate_shield(self):
        self.shield = True
    
    def deactivate_shield(self):
        self.shield = False
        
    def attack(self, direction):
        if self.cooldown == 0:
            self.cooldown = 20
            if helperMethods.has_sequence(self.handSigns, ["fist", "open"]):
                helperMethods.delete_sequence(self.handSigns, ["fist", "open"])
                self.attacks.append(lightening(self.x, self.y, direction))
            else:
                self.attacks.append(fireball(self.x, self.y, direction))
            
    def damage(self, amount):
        if not self.shield:
            self.health -= amount
            if self.health < 0:
                self.health = 0
            
    def checkCollision(self, other):
        for attack in other.attacks:
            if ((self.x - attack.x) ** 2 + (self.y - attack.y) ** 2) ** 0.5 < self.radius + attack.radius():
                if attack.type() == "fireball":
                    self.damage(10)
                elif attack.type() == "lightening":
                    self.damage(50)
                other.attacks.remove(attack)
                
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def draw(self, surface):
        #draw self
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        
        #draw shield if shield
        if(self.shield):
            pygame.draw.circle(surface, (0, 0, 255), (self.x, self.y), self.radius + 5, 2)
        
        #draw attacks
        for attack in self.attacks:
            attack.draw(surface)
            
        #draw health bar
        pygame.draw.rect(surface, (255, 0, 0), (self.x - 20, self.y - 30, 40, 5))
        pygame.draw.rect(surface, (0, 255, 0), (self.x - 20, self.y - 30, 40 * (self.health / 100), 5))
        
        #draw name tag
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        name_tag = font.render(self.name, True, (0, 0, 0))
        surface.blit(name_tag, (self.x - name_tag.get_width() // 2, self.y - 50))
