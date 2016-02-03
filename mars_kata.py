#! usr/bin/env python
import unittest

class easy(unittest.TestCase):
    pass

class Rover(object):
    def __init__(self, position, direction):
        self.position = (0,0)
        self.direction = "N"


class testRover(unittest.TestCase):
    def __init__(self):
        self.direction = Rover.direction()
        self.assertEqual(self.direction, "N")


if __name__ == '__main__':
    unittest.main()

