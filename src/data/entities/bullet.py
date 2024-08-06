import pygame


class Bullet():
    
    def __init__(self, game):
        self.game = game
        
        #size of character
        self.size = game.world_w * 0.02
        self.pos = [game.player.pos[0], game.player.pos[1]]
        
        self.direction = [game.mouse_pos]
        self.speed = 5
        
    def render(self):
        bullet_color = (255, 255, 255)
        pygame.draw.circle(self.game.screen, bullet_color, self.pos, self.size)
        
        
        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        
        