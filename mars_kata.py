#! usr/bin/env python
"""
from london software craftsmanship group meetup on python katas
"""
from collections import deque
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
        options = deque(["N", "W", "S", "E"])
        if way == "L":
            options.rotate(1)


        elif way == "R":
            options.rotate(-1)

            self.direction = options[0]

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
                    print "N"
                else: self.move()
            else:
                raise "Error"

        return self.x, self.y, self.direction






