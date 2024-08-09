import pygame, math

class Text():
    def __init__(self, game, text, color, font, size, pos, speed=40):
        self.game = game
        self.speed = speed
        font = pygame.font.SysFont(font, size, True)
        self.text = font.render(text, True, color)
        self.text_box = self.text.get_rect()
        self.original_y = pos[1]
        self.pos = pos
        self.text_box.topleft = (self.pos[0], self.pos[1])

        self.lifespan = 0

    def update(self):
        self.pos[1] = math.sin(math.radians(self.lifespan)) * self.speed + self.original_y
        self.text_box.topleft = (self.pos[0], self.pos[1])
        self.lifespan = (self.lifespan + 1) % 360

    def render(self):
        self.game.screen.blit(self.text, self.text_box)