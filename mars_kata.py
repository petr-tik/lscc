#! usr/bin/env python
"""
from london software craftsmanship group meetup on python katas
"""

import unittest
import random as rnd

        
class Rover(object):
    def __init__(self, x, y, direction, min_val, max_val, num_obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.min_val = min_val
        self.max_val = max_val
        self.num_obstacles = num_obstacles
        self.obstacles = []
        for obs in xrange(self.num_obstacles):
            new = (rnd.randint(min_val, max_val), rnd.randint(min_val, max_val))
            if new not in self.obstacles:
                self.obstacles.append(new)


    def rotate(self, way):
        options = ["N", "W", "S", "E"]
        if way == "L":
            idx_l = (options.index(self.direction) + 1) % 4        
            self.direction = options[idx_l]            

        elif way == "R":
            idx_r = ((options.index(self.direction) - 1) % 4)
            self.direction = options[idx_r]

    def move(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "E":
            self.x += 1

    def read(self, string):
        for x in string:
            if x == "L" or x == "R":
                self.rotate(x)
            elif x == "M":
                if (self.x, self.y) in self.obstacles:
                    return "N"
                else: self.move()
            else:
                raise "Error"

        return self.x, self.y, self.direction





rov = Rover(0,0, "N", -2, 2, 4)
print rov.obstacles
print (rov.x, rov.y, rov.direction)

for x in "MLMRMLMRML":
    print "read %s" % x
    rov.read(x)
    print (rov.x, rov.y, rov.direction)



