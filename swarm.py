import swixel
from random import randint

class Swarm:


    def __init__(self, window, centre_x, centre_y, size, color=(255, 255, 255)):
        STARTING_SIZE = 5  # intial size of swixels
        self.size = size  # number of swixels in the swarm
        self.swixels = []
        for i in range(size):
            x = centre_x + randint(-300, 300)
            y = centre_y + randint(-300, 300)
            self.swixels.append(swixel.Swixel(window, x, y, STARTING_SIZE, color))

    def draw(self):
        self.update()
        for s in self.swixels:
            s.draw()

    # update position
    def update(self):
        pass

    # return a list of neighbouring swixels
    # TODO for now, just return the whole swarm
    def neighbours(self):
        return self.swixels


