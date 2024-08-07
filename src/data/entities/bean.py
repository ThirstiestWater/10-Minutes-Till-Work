import pygame

class Bean():
    
    MAX_HEALTH = 5
    
    def __init__(self, game, position):
        self.game = game
        
        #size of character
        self.size = game.world_w * 0.02
        self.pos = position

    def render(self):
        
        if self.collision(self.game.player):
            if self.game.player.health_percentage < self.MAX_HEALTH - 0.2:
                self.game.player.health_percentage = 1
            else:
                self.game.player.health_percentage += 0.2
            
        
    
    def collision(self, other) -> bool:
        x_distance_sqr = (self.pos[0] - other.pos[0])**2
        y_distance_sqr = (self.pos[1] - other.pos[1])**2
        combined_radius = (self.size + other.size) ** 2
        
        
        return x_distance_sqr + y_distance_sqr <= combined_radius
            