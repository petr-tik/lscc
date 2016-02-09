#!usr/bin/env python

import unittest
import random as rnd
from mars_kata import Rover

print "\n\n\n\n..........................."
print "Starting tests"
print "...........................\n\n\n\n"

class testRover(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(0, 0, "N", -5, 5, 5)
        
    def test_dir(self):        
        direction = self.rover.direction
        self.assertIn(direction, ["N", "S", "E", "W"])

    def test_pos(self):
        self.assertTrue(self.rover.min_val <= self.rover.y <= self.rover.max_val)
        self.assertTrue(self.rover.min_val <= self.rover.x <= self.rover.max_val)
        
    def test_move(self):
        before_x = self.rover.x
        before_y = self.rover.y
        self.rover.move()
        after_x = self.rover.x
        after_y = self.rover.y
            
        if self.rover.direction == "N":
            self.assertEqual(before_y + 1, after_y)      

        elif self.rover.direction == "S":
            self.assertEqual(before_y - 1, after_y)      
        
        elif self.rover.direction == "E":
            self.asserEqual(before_x + 1, after_x) 

        elif self.rover.direction == "W":
            self.assertEqual(before_x - 1, after_x)      

        else:
            raise "Error"        
 

    def test_rotate(self):
        # successfully tested ability of the rover to rotate around its own axis

        dir1 = self.rover.direction        
        for x in xrange(4):
            self.rover.rotate("L")
        dir2 = self.rover.direction    
        self.assertEqual(dir1, dir2)

    def test_read(self):
        before_y = self.rover.y
        self.rover.read("LLM")
        self.assertEqual(before_y - 1, self.rover.y)
        self.assertEqual(self.rover.direction, "S")      

    def test_num_obstacles(self):
        self.assertLessEqual(len(self.rover.obstacles), self.rover.num_obstacles)
        

if __name__ == '__main__':
    unittest.main(verbosity=10)