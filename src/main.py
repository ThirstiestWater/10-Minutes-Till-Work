import pygame, math, sys
from pygame.locals import *
from data.utils import *
from data.entities.player import Player
from data.entities.bullet import Bullet
from data.entities.enemies import Enemies
from data.entities.bean import Bean
from data.title_screen.text import Text
from random import randint

class Game():
    def __init__(self):
        #Initialize Game
        pygame.init()

        #Set up Clock
        self.FPS = 60
        self.clock = pygame.time.Clock()

        #Set up Joysticks
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        #Set up Display
        self.world_w, self.world_h = 1000, 500
        self.screen = pygame.display.set_mode((self.world_w, self.world_h))
        pygame.display.set_caption("Project")
        self.background = (127, 85, 57)


    def run(self):
        #Run Game
        Running = True
        while Running:

            self.title_screen = True
            self.playing = True

            line1 = Text(self, "10 Minutes", (255, 255, 255), "Candara", 96, [self.world_w//5, self.world_h//8], 30)
            line2 = Text(self, "Till Work", (255, 255, 255), "Candara", 96, [self.world_w//5 * 2, self.world_h//8 + self.world_h//6], 30)

            while self.title_screen:
                self.screen.fill(self.background)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        Running = False
                        self.title_screen = False
                        self.playing = False
                    if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                        self.title_screen = False
                
                line1.update()
                line2.update()
                line1.render()
                line2.render()

                pygame.display.update()
                self.clock.tick(self.FPS)

            
            attack_speed = 0.1
            shooting_timer = attack_speed * self.FPS
            clicking = False

            enemy_spawn_rate = 2
            enemy_timer = enemy_spawn_rate * self.FPS
            
            bean_spawn_rate = 15
            bean_timer = bean_spawn_rate * self.FPS

            movement = [0,0]
            # Initialize all entities
            self.player = Player(self)
            self.camera = Camera(target=self.player)
            self.tile_map = Map(self)

            self.enemies = []
            self.enemy_removal_list = []
            
            self.beans = []
            self.beans_removal_list = []

            self.bullets = []
        
            #Run main scene
            while self.playing:
                self.screen.fill(self.background)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            Running = False
                            self.playing = False
                    if event.type == pygame.KEYDOWN:
                        match event.key: # Switch Case for the Keys that are pressed
                            case pygame.K_SPACE:
                                self.player.hit(1)
                            case pygame.K_a:
                                movement[0] -= 1
                            case pygame.K_d:
                                movement[0] += 1
                            case pygame.K_w:
                                movement[1] -= 1
                            case pygame.K_s:
                                movement[1] += 1
                        # After a change in movement occurs, change player's direction
                        self.player.direction_change(self.normalize_vector(movement))
                        
                    if event.type == pygame.KEYUP:
                        match event.key:
                            case pygame.K_a:
                                movement[0] += 1
                            case pygame.K_d:
                                movement[0] -= 1
                            case pygame.K_w:
                                movement[1] += 1
                            case pygame.K_s:
                                movement[1] -= 1
                        # After a change in movement occurs, change player's direction
                        self.player.direction_change(self.normalize_vector(movement))

                    if event.type == MOUSEBUTTONDOWN:
                        clicking = True
                    if event.type == MOUSEBUTTONUP:
                        clicking = False

                self.mouse_pos = [pygame.mouse.get_pos()[0] - self.camera.get_offset()[0], pygame.mouse.get_pos()[1] - self.camera.get_offset()[1]]

                if clicking and shooting_timer >= attack_speed * self.FPS:
                    shooting_timer = 0
                    self.bullets.append(Bullet(self))
                shooting_timer += 1

                if enemy_timer >= enemy_spawn_rate * self.FPS:
                    enemy_timer = 0
                    self.spawn_enemies()
                enemy_timer += 1
                
                if bean_timer >= bean_spawn_rate * self.FPS:
                    bean_timer = 0
                    self.spawn_beans()
                bean_timer += 1

                self.player.update()
                self.camera.update()
                self.tile_map.update()
                
                self.tile_map.render()                
                self.player.render()

                for enemy in self.enemies:
                    enemy.follow_player()
                    enemy.update()
                    enemy.render()
                    for other in self.enemies:
                        if not enemy is other:
                            if enemy.collision(other):
                                push_dir = [other.pos[0] - enemy.pos[0], other.pos[1] - enemy.pos[1]]
                                other.push(push_dir, 1)
                                enemy.push([push_dir[0] * -1, push_dir[1] * -1], 1)

                for enemy in self.enemy_removal_list:
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                        
                for bean in self.beans:
                    bean.update()
                    bean.render()
                
                for bean in self.beans_removal_list:
                    if bean in self.beans:
                        self.beans.remove(bean)

                i = 0
                while i < len(self.bullets):
                    bullet = self.bullets[i]
                    bullet.update()
                    bullet.render()
                    i += 1

                pygame.display.update()
                self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit()

    def spawn_enemies(self):
        for i in range(5):
            x_sign = -1 if randint(0,1) else 1
            y_sign = -1 if randint(0,1) else 1
            position = [self.player.pos[0] + randint(self.world_h//2, self.world_h) * x_sign, self.player.pos[1] + randint(self.world_h//2, self.world_h) * y_sign]
            self.enemies.append(Enemies(self, position))
            
    def spawn_beans(self):
        for i in range(3):
            x_sign = -1 if randint(0,1) else 1
            y_sign = -1 if randint(0,1) else 1
            position = [self.player.pos[0] + randint(self.world_h//2, self.world_h) * x_sign, self.player.pos[1] + randint(self.world_h//2, self.world_h) * y_sign]
            self.beans.append(Bean(self, position))
            

    def normalize_vector(self, vector: list) -> list:
        try:
            return [vector[0] / math.sqrt(vector[0]**2 + vector[1]**2), vector[1] / math.sqrt(vector[0]**2 + vector[1]**2)]
        except:
            return [0, 0]

Game().run()