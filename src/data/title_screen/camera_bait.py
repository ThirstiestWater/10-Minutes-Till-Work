class Rat():
    def __init__(self, pos):
        self.pos = pos
        self.speed = 1
        self.direction = [1, 0]

    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed