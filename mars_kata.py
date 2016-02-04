#! usr/bin/env python
"""
from london software craftsmanship group meetup on python katas
"""

import unittest

class Rover(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

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



class testRover(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(0, 0, "N")
        
    def test_dir(self):        
        direction = self.rover.direction
        self.assertEqual(direction, "N")

    def test_pos(self):
        x = self.rover.x
        self.assertEqual(x, 0)
        
    def test_move(self):
        if self.rover.direction == "N":
            before = self.rover.y
            self.rover.move()
            after = self.rover.y
            self.assertEqual(before + 1, after)      
        """elif self.rover.direction == "S":
            self.y -= 1
            return self.y
        elif self.rover.direction == "W":
            self.x -= 1
            return self.x
        elif self.rover.direction == "E":
            self.x += 1
            return self.x
"""
#        move_W = self.rover.move()
 #       self.assertEqual(move_W, self.rover.x)    
   


    def test_rotate(self):
        # successfully tested ability of the rover to rotate around its own axis

        dir1 = self.rover.direction        
        for x in xrange(4):
            self.rover.rotate("L")
        dir2 = self.rover.direction    
        self.assertEqual(dir1, dir2)



if __name__ == '__main__':
    unittest.main()



