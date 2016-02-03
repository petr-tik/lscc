#! usr/bin/env python
import unittest

class easy(unittest.TestCase):
    pass

class Rover(object):
    def __init__(self, position, direction):
        self.position = (0,0)
        self.direction = "N"


class testRover(unittest.TestCase):
    def setUp(self):
        self.rover = Rover((0,0), "N")

    def test_dir(self):        
        self.direction = self.rover.direction
        self.assertEqual(self.direction, "N")

    def test_pos(self):
        self.position = self.rover.position
        self.assertEqual(self.position, (0,0))

if __name__ == '__main__':
    unittest.main()

