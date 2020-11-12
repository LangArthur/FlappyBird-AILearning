#!/usr/bin/python3
import pygame
from src.GameObject import GameObject

class Pipe(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y, True)
        self.pipe_image = pygame.image.load("ressources/pipe.png")

    def draw(self, window):
        window.blit(self.pipe_image, (self.x, self.y))
