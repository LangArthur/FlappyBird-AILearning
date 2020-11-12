#!/usr/bin/python3

# implementing a gameObject
class GameObject():

    # constructor
    # param x: the window of the game
    def __init__(self, x, y, displayable):
        self.x = x
        self.y = y
        self.displayable = displayable

    # draw the gameObject
    # param window: the window of the game
    def draw(self, window):
        pass

    # update the gameObject
    def update(self):
        pass