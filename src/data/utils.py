import pygame, math
from pygame.locals import *

TILEWIDTH = 50

def normalize_vector(vector: list) -> list:
    try:
        return [vector[0] / math.sqrt(vector[0]**2 + vector[1]**2), vector[1] / math.sqrt(vector[0]**2 + vector[1]**2)]
    except:
        return [0, 0]

class Camera():
    def __init__(self, target):
        self.pos = target.pos
        self.original_pos = self.pos[::]
        self.offset = [0, 0]
        self.speed = 1.5

    def get_offset(self):
        return self.offset
    
    def get_pos(self):
        return self.pos
    
    def update(self):
        self.offset[0] = self.original_pos[0] - self.pos[0]
        self.offset[1] = self.original_pos[1] - self.pos[1]

class Tile():
    def __init__(self, game, pos, width = TILEWIDTH):
        self.pos = pos
        self.width = width
        self.game = game
        self.color = (game.background[0] + 10, game.background[1] + 10, game.background[2] + 10)

    def move(self, new_pos):
        self.pos = new_pos

    def get_pos(self):
        return self.pos

    def render(self):
        pygame.draw.rect(self.game.screen, self.color, (self.pos[0] + self.game.camera.get_offset()[0], self.pos[1] + self.game.camera.get_offset()[1], self.width, self.width))

class Map():
    def __init__(self, game):
        self.game = game
        self.tiles = []
        for i in range(0, self.game.world_w // TILEWIDTH + 2, 2):
            for j in range(0, self.game.world_h // TILEWIDTH + 1, 2):
                self.tiles.append(Tile(self.game, [i * TILEWIDTH, j * TILEWIDTH]))
        for i in range(1, self.game.world_w // TILEWIDTH + 2, 2):
            for j in range(1, self.game.world_h // TILEWIDTH + 2, 2):
                self.tiles.append(Tile(self.game, [i * TILEWIDTH, j * TILEWIDTH]))

    def update(self):
        camera_offset = self.game.camera.get_offset()
        for tile in self.tiles:
            tile_pos = tile.get_pos()
            if tile_pos[0] + camera_offset[0] >= self.game.world_w + TILEWIDTH:
                tile.move([tile_pos[0] - self.game.world_w - TILEWIDTH * 2, tile_pos[1]])
            elif tile_pos[0] + camera_offset[0] <= -1 * TILEWIDTH:
                tile.move([tile_pos[0] + self.game.world_w + TILEWIDTH * 2, tile_pos[1]])
            if tile_pos[1] + camera_offset[1] >= self.game.world_h + TILEWIDTH:
                tile.move([tile_pos[0], tile_pos[1] - self.game.world_h - TILEWIDTH * 2])
            elif tile_pos[1] + camera_offset[1] <= -1 * TILEWIDTH:
                tile.move([tile_pos[0], tile_pos[1] + self.game.world_h + TILEWIDTH * 2])

    def render(self):
        for tile in self.tiles:
            tile.render()