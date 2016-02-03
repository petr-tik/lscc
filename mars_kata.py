#! usr/bin/env python
import unittest

class Rover(object):
    def __init__(self, x, y, direction):
        self.x = 0
        self.y = 0
        self.direction = "N"

    def move(self):
        if self.direction == "N":
            self.y += 1



class testRover(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(0, 0, "N")

    def test_dir(self):        
        self.direction = self.rover.direction
        self.assertEqual(self.direction, "N")

    def test_pos(self):
        self.x = self.rover.x
        self.assertEqual(self.x, 0)

    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()

