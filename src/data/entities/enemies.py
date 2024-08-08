import pygame, math

class Enemies():
    
    MAX_HEALTH = 5
    
    def __init__(self, game, pos):
        self.health = self.MAX_HEALTH
        self.damage = 1
        
        #size of character
        self.size = game.world_w * 0.02
        self.pos = pos
        
        self.game = game
        self.direction = [0, 0]
        self.speed = 3
    
    def render(self):
        ice_color = (254,250,224)
        outline = (50,130,253)
        
        real_pos = [self.pos[0] + self.game.camera.get_offset()[0], self.pos[1] + self.game.camera.get_offset()[1]]
        offset = self.game.camera.get_offset()
        norm = [self.direction[1], self.direction[0]]
        
        #take updated ice size
        distance_to_corner = math.sqrt(2 * (self.size ** 2))
        points = [[], [], [], []]
        try:
            theta = math.atan(self.direction[1]/self.direction[0])
        except:
            theta = 0
        angles = [theta, theta + math.pi/2, theta + math.pi, theta + 3*math.pi/2]
        points[0] = [(self.pos[0] + offset[0]) + (self.direction[0]*math.cos(angles[0]) - self.direction[1]*math.sin(angles[0]))*distance_to_corner, \
                     (self.pos[1] + offset[1]) + (self.direction[0]*math.sin(angles[0]) + self.direction[1]*math.cos(angles[0]))*distance_to_corner]
        points[1] = [(self.pos[0] + offset[0]) + (self.direction[0]*math.cos(angles[1]) - self.direction[1]*math.sin(angles[1]))*distance_to_corner, \
                     (self.pos[1] + offset[1]) + (self.direction[0]*math.sin(angles[1]) + self.direction[1]*math.cos(angles[1]))*distance_to_corner]
        points[2] = [(self.pos[0] + offset[0]) + (self.direction[0]*math.cos(angles[2]) - self.direction[1]*math.sin(angles[2]))*distance_to_corner, \
                     (self.pos[1] + offset[1]) + (self.direction[0]*math.sin(angles[2]) + self.direction[1]*math.cos(angles[2]))*distance_to_corner]
        points[3] = [(self.pos[0] + offset[0]) + (self.direction[0]*math.cos(angles[3]) - self.direction[1]*math.sin(angles[3]))*distance_to_corner, \
                     (self.pos[1] + offset[1]) + (self.direction[0]*math.sin(angles[3]) + self.direction[1]*math.cos(angles[3]))*distance_to_corner]
        pygame.draw.polygon(self.game.screen, ice_color, points)
        pygame.draw.polygon(self.game.screen, outline, points, 3)

        # Eyes (Functioning)
        pygame.draw.circle(self.game.screen, (0, 0, 0), [real_pos[0] + self.direction[0] * self.size * 4/10 - norm[0] * self.size*1/3, real_pos[1] + self.direction[1] * self.size*4/10 + norm[1] * self.size*1/3], self.size//6)
        pygame.draw.circle(self.game.screen, (0, 0, 0), [real_pos[0] + self.direction[0] * self.size * 4/10 + norm[0] * self.size*1/3, real_pos[1] + self.direction[1] * self.size*4/10 - norm[1] * self.size*1/3], self.size//6)
  

        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed 
        self.pos[1] += self.direction[1] * self.speed
    
        #hit player if collision
        if self.collision(self.game.player):
            self.game.player.hit(self.damage)
            self.game.enemy_removal_list.append(self)
        
        i = 0
        while i < len(self.game.bullets):
            bullet = self.game.bullets[i]
            if self.collision(bullet):
                self.health -= bullet.damage
                self.game.bullets.remove(bullet)
            i += 1

        if self.health <= 0:
            self.game.enemy_removal_list.append(self)
    
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
        
        