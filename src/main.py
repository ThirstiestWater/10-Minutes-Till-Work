import pygame, math, sys
from pygame.locals import *
import data.utils
from data.entities.player import Player
from random import randint

def normalize_vector(vector: list) -> list:
    try:
        return [vector[0] / math.sqrt(vector[0]**2 + vector[1]**2), vector[1] / math.sqrt(vector[0]**2 + vector[1]**2)]
    except:
        return [0, 0]


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
        self.world_w, self.world_h = 1400, 700
        self.screen = pygame.display.set_mode((self.world_w, self.world_h))
        pygame.display.set_caption("Project")
        self.background = (15, 15, 30)

    def run(self):
        #Run Game
        Running = True
        while Running:
            seconds_timer = 0
            seconds_tracker = 0
            playing = True
            movement = [0,0]
            player = Player(self)
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
                                player.hit(1)
                            case pygame.K_a:
                                movement[0] -= 1
                            case pygame.K_d:
                                movement[0] += 1
                            case pygame.K_w:
                                movement[1] -= 1
                            case pygame.K_s:
                                movement[1] += 1
                        # After a change in movement occurs, change player's direction
                        player.direction_change(normalize_vector(movement))
                        
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
                        player.direction_change(normalize_vector(movement))

                player.update()
                player.render()
            

                # if seconds_tracker % (self.FPS//2) == 0:
                #     f"Half a second has passed"

                # if seconds_tracker == self.FPS:
                #     seconds_tracker = 0
                #     seconds_timer += 1
                # seconds_tracker += 1

                # Draws a rectange for reference
                pygame.draw.rect(self.screen, (255, 255, 255), (10, 10, 10, 10))

                pygame.display.update()
                self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit()

Game().run()