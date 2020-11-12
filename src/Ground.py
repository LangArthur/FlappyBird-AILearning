#!/usr/bin/python3

from src.GameObject import GameObject

class Ground(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, True)

    def draw(self, window):
        pass
