import pygame
from vector import Vector

X = 0
Y = 1

class Swixel:


    def __init__(self, window, x, y, size, flock, color=(255, 255, 255)):
        self.window = window
        self.x = x
        self.y = y
        self.vector = Vector(1, 1)  # movement direction
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.color = color

    # swixel is drawn as a simple rectangle of colour
    def draw(self):
        self.update()
        self.window.fill(self.color, self.rect)

    # update position
    def update(self):
        self.x += self.vector.x
        self.y += self.vector.y

        # collision with boundaries
        boundary = self.window.get_rect()
        if (self.x < boundary.left) or (self.x > boundary.right):
            self.vector.x = -self.vector.x
        if (self.y < boundary.top) or (self.y > boundary.bottom):
            self.vector.y = -self.vector.y

        # separation from neighbours

        # get a list of the n nearest neighbours


        # draw rectangle
        self.rect.update(self.x, self.y, self.size, self.size)

    def separation(boid, flock, desiredSeparation):
        steer = Vector(0, 0)
        count = 0
        for each otherBoid in flock
            distance = distance(boid.position, otherBoid.position)
            if distance > 0 and distance < desiredSeparation
                diff = boid.position - otherBoid.position
                diff = normalize(diff)
                diff = diff / distance // Weight
                by
                distance
                steer = steer + diff
                count = count + 1
        if count > 0
            steer = steer / count
        return steer

    def home_to(self, pos):
        self.home = pos

