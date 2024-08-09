import pygame, math

class Text():
    def __init__(self, game, text, color, font, size, pos, speed=40, box = False):
        self.game = game
        self.speed = speed
        text_font = pygame.font.SysFont(font, size, True)
        self.text = text_font.render(text, True, color)
        self.text_box = self.text.get_rect()
        self.original_y = pos[1]
        self.pos = pos
        self.text_box.topleft = (self.pos[0], self.pos[1])

        self.box = box
        if box:
            distance = 20
            self.text_box.centerx = game.world_w//2
            self.box_rect = pygame.font.SysFont(font, size + distance, True).render(text, True, color).get_rect()
            self.box_rect.topleft = (self.pos[0] - distance/2 - 5, self.pos[1] - distance/2 - 5)
            self.box_rect.centerx = (game.world_w//2)
            
        self.color = color

        self.lifespan = 0

    def update(self):
        self.pos[1] = math.sin(math.radians(self.lifespan)) * self.speed + self.original_y
        self.text_box.topleft = (self.pos[0], self.pos[1])
        self.lifespan = (self.lifespan + 1) % 360
        if self.box:
            self.text_box.centerx = self.game.world_w//2
            self.box_rect.center = self.text_box.center

    def render(self):
        self.game.screen.blit(self.text, self.text_box)
        if self.box:
            pygame.draw.rect(self.game.screen, self.color, self.box_rect, 10)