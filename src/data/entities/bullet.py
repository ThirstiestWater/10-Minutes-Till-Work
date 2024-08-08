import pygame


class Bullet():
    
    def __init__(self, game):
        self.game = game
        self.timer = 0
        self.lifespan = 10
        
        #size of character
        self.size = game.world_w * 0.01
        self.pos = game.player.pos[::]
        
        self.direction = game.normalize_vector([game.mouse_pos[0] - self.pos[0], game.mouse_pos[1] - self.pos[1]])
        self.speed = 10
        self.damage = 2
        
    def render(self):
        bullet_color = (255, 255, 255)
        
        real_pos = [self.pos[0] + self.game.camera.get_offset()[0], self.pos[1] + self.game.camera.get_offset()[1]]

        pygame.draw.circle(self.game.screen, bullet_color, real_pos, self.size)
        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        
        self.timer += 1
        if self.timer >= self.lifespan * self.game.FPS:
            self.game.bullets.remove(self)