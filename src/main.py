import pygame, math, sys
from pygame.locals import *
import data.entities
import data.utils
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
            #Run main scene
            while playing:
                self.screen.fill(self.background)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            Running = False
                            playing = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print("'a' pressed")
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            print("'a' pressed")

                if seconds_tracker % (self.FPS//2) == 0:
                    f"Half a second has passed"

                if seconds_tracker == self.FPS:
                    seconds_tracker = 0
                    seconds_timer += 1
                seconds_tracker += 1

                pygame.display.update()
                self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit()

Game().run()