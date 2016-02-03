#! usr/bin/env python
import unittest

class easy(unittest.TestCase):
    pass

class Rover(object):
    def __init__(self, position, direction):
        self.position = (0,0)
        self.direction = "N"


class testRover(unittest.TestCase):
    def test_dir(self):
        rover = Rover((0,0), "N")        
        self.direction = rover.direction
        self.assertEqual(self.direction, "N")


if __name__ == '__main__':
    unittest.main()

