import pygame
import random
import math

class Player():
    
    MAX_HEALTH = 5
    
    def __init__(self, game):
        self.health = self.MAX_HEALTH
        self.health_percentage = 1
        
        #size of character
        self.size = game.world_w * 0.30
        self.pos = [game.world_w//2, game.world_h//2]
        
        self.game = game
        self.direction = [0, 0]
        self.speed = 1
        
        
    def render(self):
        cup_color = (254,250,224)
        pygame.draw.circle(self.game.screen, cup_color, (self.pos), self.size)
        coffee_color = (221,161,94)
        
        #take updated coffee size
        pygame.draw.circle(self.game.screen, coffee_color, (self.pos), self.size * 0.9 * self.health_percentage)
    
    
    def update(self):
        
        #update pos based off of direction looking and speed of movement
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        
        #decrement coffee size based off of health percentage
        if self.health_percentage > (self.health / self.MAX_HEALTH):
            self.health_percentage -= 0.01
    
    def direction_change(self, new_direction):
        self.direction = new_direction
        
    