#!/usr/bin/python3
import pygame

from src.GameObject import GameObject

class Ground(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, True)
        self.ground_image = pygame.image.load("ressources/base.png")

    def draw(self, window):
        window.blit(self.ground_image, (self.x, self.y))

