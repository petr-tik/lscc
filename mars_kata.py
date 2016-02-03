#! usr/bin/env python
import unittest

class Rover(object):
    def __init__(self, x, y, direction):
        self.x = 0
        self.y = 0
        self.direction = "N"

    def move(self, direction):
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
        self.direction = self.rover.direction
        self.assertEqual(self.direction, "N")

    def test_pos(self):
        self.x = self.rover.x
        self.assertEqual(self.x, 0)

    def test_move(self):
#        self.move_N = self.rover.move("N")
#        self.assertEqual(self.move_N, self.rover.y)    
        pass

if __name__ == '__main__':
    unittest.main()


[n, e, s, w]


