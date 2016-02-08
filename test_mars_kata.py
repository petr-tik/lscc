#! usr/bin/env python

import unittest
import random as rnd
from mars_kata import Space, Rover

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

        elif self.rover.direction == "S":
            before = self.rover.y
            self.rover.move()
            after = self.rover.y
            self.assertEqual(before - 1, after)      
        
        elif self.rover.direction == "E":
            before = self.rover.y
            self.rover.move()
            after = self.rover.y
            self.asserEqual(before + 1, after) 

        elif self.rover.direction == "W":
            before = self.rover.x
            self.rover.move()
            after = self.rover.x
            self.assertEqual(before - 1, after)      

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

class testSpace(unittest.TestCase):
    def setUp(self):
        self.space = Space(-10, 10, 5)

    def test_num_obstacles(self):
        self.assertEqual(len(self.space.obstacles), self.space.num_obstacles)

    def test_obstacles_within_grid(self):
        pass
        

if __name__ == '__main__':
    unittest.main()