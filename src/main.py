import pygame, math, sys
from pygame.locals import *
from data.utils import *
from data.entities.player import Player
from data.entities.bullet import Bullet
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
            
            attack_speed = 1
            shooting_timer = attack_speed * self.FPS
            clicking = False

            playing = True
            movement = [0,0]
            # Initialize all entities
            self.player = Player(self)
            self.camera = Camera(target=self.player)
            self.tile_map = Map(self)

            self.enemies = []

            self.bullets = []
        
            #Run main scene
            while playing:
                self.screen.fill(self.background)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            Running = False
                            playing = False
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

                if clicking and shooting_timer == attack_speed * self.FPS:
                    shooting_timer = 0
                    self.bullets.append(Bullet(self))

                self.player.update()
                self.camera.update()
                self.tile_map.update()
                
                self.tile_map.render()                
                self.player.render()

                i = 0
                while i < len(self.enemies):
                    enemy = self.enemies[i]
                    enemy.update()
                    enemy.render()
                    i += 1

                i = 0
                while i < len(self.bullets):
                    bullet = self.bullets[i]
                    bullet.update()
                    bullet.render()
                    i += 1

                # if seconds_tracker % (self.FPS//2) == 0:
                #     f"Half a second has passed"

                # if seconds_tracker == self.FPS:
                #     seconds_tracker = 0
                #     seconds_timer += 1
                # seconds_tracker += 1

                pygame.display.update()
                self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit()
    
    def normalize_vector(self, vector: list) -> list:
        try:
            return [vector[0] / math.sqrt(vector[0]**2 + vector[1]**2), vector[1] / math.sqrt(vector[0]**2 + vector[1]**2)]
        except:
            return [0, 0]

Game().run()