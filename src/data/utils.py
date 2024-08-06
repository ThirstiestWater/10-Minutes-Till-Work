import pygame, math
from pygame.locals import *

def normalize_vector(vector: list) -> list:
    try:
        return [vector[0] / math.sqrt(vector[0]**2 + vector[1]**2), vector[1] / math.sqrt(vector[0]**2 + vector[1]**2)]
    except:
        return [0, 0]

class Camera():
    def __init__(self, game):
        self.pos = [game.world_w//2, game.world_h//2]
        self.original_pos = self.pos[::]
        self.offset = [0, 0]
        self.speed = 1.5

    def get_offset(self):
        return self.offset
    
    def get_pos(self):
        return self.pos
    
    def follow(self, target_pos):
        if (target_pos[0] - self.pos[0])**2 + (target_pos[1] - self.pos[1])**2 < self.speed**2:
            self.pos = target_pos[::]
        else:
            direction = [target_pos[0] - self.pos[0], target_pos[1] - self.pos[1]]
            self.pos[0] += direction[0] * self.speed
            self.pos[1] += direction[1] * self.speed
        
        self.offset[0] = self.original_pos[0] - self.pos[0]
        self.offset[1] = self.original_pos[1] - self.pos[1]