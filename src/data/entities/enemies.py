import pygame
from utils import normalize_vector as nv


class Enemies():
    
    MAX_HEALTH = 4
    
    def __init__(self, game):
        self.health = self.MAX_HEALTH
        self.health_percentage = 1
        
        #size of character
        self.size = game.world_w * 0.04
        self.pos = [game.world_w//2, game.world_h//2]
        
        self.game = game
        self.direction = [0, 0]
        self.speed = 4
    
    def render(self):
        ice_color = (254,250,224)
        
        real_pos = [self.pos[0] + self.game.camera.get_offset()[0], self.pos[1] + self.game.camera.get_offset()[1]]
        
        
        #take updated ice size
        pygame.draw.circle(self.game.screen, ice_color, (real_pos), self.size * 0.9 * self.health_percentage)
        
        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed 
        self.pos[1] += self.direction[1] * self.speed
    
        #decrement coffee size based off of health percentage
        if self.health_percentage > (self.health / self.MAX_HEALTH):
            self.health_percentage -= 0.01
    
    
    def follow_player(self):
        distance_from_player_x = self.pos[0] - self.game.player.pos[0]
        
        distance_from_player_y = self.pos[1] - self.game.player.pos[1]
        
        xy = [distance_from_player_x, distance_from_player_y]
        
        self.direction = nv(xy)
        