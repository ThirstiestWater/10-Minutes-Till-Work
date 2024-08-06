import pygame

class Player():
    
    MAX_HEALTH = 5
    
    def __init__(self, game):
        self.health = self.MAX_HEALTH
        self.health_percentage = 1
        
        #size of character
        self.size = game.world_w * 0.02
        self.pos = [game.world_w//2, game.world_h//2]
        
        self.game = game
        self.direction = [0, 0]
        self.speed = 5

        self.facing = [1,0]
        
    def render(self):
        real_pos = [self.pos[0] + self.game.camera.get_offset()[0], self.pos[1] + self.game.camera.get_offset()[1]]

        #Coffee Cup
        cup_color = (254,250,224)
        pygame.draw.circle(self.game.screen, cup_color, real_pos, self.size)
        #Handle
        
        #take updated coffee size
        coffee_color = (221,161,94)
        pygame.draw.circle(self.game.screen, coffee_color, real_pos, self.size * 0.9 * self.health_percentage)

        #Eyes
        norm = [self.facing[1], self.facing[0]]
        pygame.draw.circle(self.game.screen, (0, 0, 0), [real_pos[0] + self.facing[0] * self.size * 4/10 - norm[0] * self.size*1/3, real_pos[1] + self.facing[1] * self.size*4/10 + norm[1] * self.size*1/3], self.size//6)
        pygame.draw.circle(self.game.screen, (0, 0, 0), [real_pos[0] + self.facing[0] * self.size * 4/10 + norm[0] * self.size*1/3, real_pos[1] + self.facing[1] * self.size*4/10 - norm[1] * self.size*1/3], self.size//6)
    
    
    def update(self):
        self.facing[0] = self.pos[0] - self.game.mouse_pos[0]
        self.facing[1] = self.pos[1] - self.game.mouse_pos[1]
        self.facing = self.game.normalize_vector(self.facing)
        
        #update pos based off of direction looking and speed of movement
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        
        #decrement coffee size based off of health percentage
        if self.health_percentage > (self.health / self.MAX_HEALTH):
            self.health_percentage -= 0.01
    
    def direction_change(self, new_direction):
        self.direction = new_direction
        
    def hit(self, damage):
        self.health -= damage
        
    #collision    
    def collision(self, other):
        
        x_distance_sqr = (self.pos[0] - other.pos[0])**2
        y_distance_sqr = (self.pos[1] - other.pos[1])**2
        combined_radius = (self.size + other.size) ** 2
        
        
        return True if x_distance_sqr + y_distance_sqr <= combined_radius else False

        
    