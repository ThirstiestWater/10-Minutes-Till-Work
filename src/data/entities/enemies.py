import pygame

class Enemies():
    
    MAX_HEALTH = 5
    
    def __init__(self, game, pos):
        self.health = self.MAX_HEALTH
        self.health_percentage = 1
        self.damage = 1
        
        #size of character
        self.size = game.world_w * 0.03
        self.pos = pos
        
        self.game = game
        self.direction = [0, 0]
        self.speed = 3
    
    def render(self):
        ice_color = (254,250,224)
        
        real_pos = [self.pos[0] + self.game.camera.get_offset()[0], self.pos[1] + self.game.camera.get_offset()[1]]
        
        #take updated ice size
        pygame.draw.circle(self.game.screen, ice_color, real_pos, self.size * 0.9 * self.health_percentage)
        
        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed 
        self.pos[1] += self.direction[1] * self.speed
    
        #hit player if collision
        if self.collision(self.game.player):
            self.game.player.hit(self.damage)
            self.game.enemies.remove(self)
        
        i = 0
        while i < len(self.game.bullets):
            bullet = self.game.bullets[i]
            if self.collision(bullet):
                self.health -= bullet.damage
                self.game.bullets.remove(bullet)
            i += 1

        if self.health <= 0:
            self.game.enemies.remove(self)
    
    def follow_player(self):
        distance_from_player_x = self.game.player.pos[0] - self.pos[0]
        distance_from_player_y = self.game.player.pos[1] - self.pos[1]
        
        xy = [distance_from_player_x, distance_from_player_y]
        
        self.direction = self.game.normalize_vector(xy)
        
    
    def collision(self, other) -> bool:
        
        x_distance_sqr = (self.pos[0] - other.pos[0])**2
        y_distance_sqr = (self.pos[1] - other.pos[1])**2
        combined_radius = (self.size + other.size) ** 2
        
        
        return x_distance_sqr + y_distance_sqr <= combined_radius
    
    def push(self, target, magnitude):
        direction = self.game.normalize_vector(target)
        self.pos[0] += direction[0] * magnitude
        self.pos[1] += direction[1] * magnitude
        
        