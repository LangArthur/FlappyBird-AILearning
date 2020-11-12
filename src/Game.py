#!/usr/bin/python3

import pygame

from src.Ground import Ground

SCREEN_COLOR = 0,0,0

class Game():
    def __init__(self, x, y):
        pygame.init()
        self.winSize = (x, y)
        self.window = pygame.display.set_mode(self.winSize)
        self.isRunning = True
        self.gameObject = []
        self.initGameObject()

    def initGameObject(self):
        self.gameObject.append(Ground(0, 550))

    def run(self):
        while self.isRunning:
            self.draw()
            self.manageEvent()

    def manageEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

    def draw(self):
        self.window.fill(SCREEN_COLOR)
        for go in self.gameObject:
            go.draw(self.window)
        pygame.display.flip()
