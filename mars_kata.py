#! usr/bin/env python
"""
from london software craftsmanship group meetup on python katas
"""

import unittest

class Rover(object):
    def __init__(self, x, y, direction):
        self.x = 0
        self.y = 0
        self.direction = "N"

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
            return self.y
        elif self.direction == "S":
            self.y -= 1
            return self.y
        elif self.direction == "W":
            self.x -= 1
            return self.x
        elif self.direction == "E":
            self.x += 1
            return self.x




r = Rover(0,0,"N")
for x in xrange(10):

    print "and now I am facing {}".format(r.direction)
    print "rotating right"
    r.rotate("R")
    print "and now I am facing {}".format(r.direction)
    



class testRover(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(0, 0, "N")
        
    def test_dir(self):        
        self.direction = self.rover.direction
        self.assertEqual(self.direction, "N")

    def test_pos(self):
        self.x = self.rover.x
        self.assertEqual(self.x, 0)

    def test_move_N(self):
        move_N = self.rover.move()
        self.assertEqual(move_N, self.rover.y)    
        
    def test_move_W(self):
#        move_W = self.rover.move()
 #       self.assertEqual(move_W, self.rover.x)    
        pass



    def test_move_E(self):
        #move_E = self.rover.move()
        #self.assertEqual(move_E, self.rover.x)    
        pass

    def test_rotate(self):
        pass



if __name__ == '__main__':
    unittest.main()



