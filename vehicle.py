# +
import math
import random as r

class Vehicle:
    def __init__(self, x_pos, y_pos, angle, speed, noise = 0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.speed = speed
        self.trajectory = [[self.x_pos, self.y_pos]]
        self.noise = noise
    def accelerate(self,acc):
        self.speed +=acc
    
    def move(self):
        theta = self.angle / 180 * math.pi
        self.x_pos += (math.cos(theta) * self.speed + self.noise * (r.random()-0.5))
        self.y_pos += (math.sin(theta) * self.speed + self.noise * (r.random()-0.5))
        self.trajectory.append([self.x_pos, self.y_pos])


# -

import random as r
r.random()
