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
        self.move_N = self.rover.move("N")
        self.assertEqual(self.move_N, self.rover.y)    
        
    def test_move_W(self):
 #       self.move_W = self.rover.move("W")
 #       self.assertEqual(self.move_W, self.rover.x)    
        pass
    def test_move_E(self):
        #self.move_E = self.rover.move("E")
        #self.assertEqual(self.move_E, self.rover.x)    
        pass



if __name__ == '__main__':
    unittest.main()



