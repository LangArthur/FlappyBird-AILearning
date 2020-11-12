#!/usr/bin/python3

class GameObject():

    def __init__(self, x, y, displayable):
        self.x = x
        self.y = y
        self.displayable = displayable

    def draw(self, window):
        pass