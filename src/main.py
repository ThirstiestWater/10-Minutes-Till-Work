import pygame, math
import data.entities
import data.utils
from pygame.locals import *
from random import randint

#Initialize Game
pygame.init()

#Set up Clock
FPS = 60
clock = pygame.time.Clock()

#Set up Joysticks
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

#Set up Display
world_w, world_h = 1400, 700
screen = pygame.display.set_mode((world_w, world_h))
pygame.display.set_caption("Project")
background = (15, 15, 30)
margins = 10

#Run Game
Running = True
while Running:
    seconds_timer = 0
    seconds_tracker = 0
    playing = True
    #Run main scene
    while playing:
        screen.fill(background)
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

        if seconds_tracker % (FPS//2) == 0:
             f"Half a second has passed"

        if seconds_tracker == FPS:
            seconds_tracker = 0
            seconds_timer += 1
        seconds_tracker += 1

        pygame.display.update()
        clock.tick(FPS)

pygame.quit()