#!/usr/bin/python3

import sys, pygame

from src.Ground import Ground

def main():

    pygame.init()

    gameObjects = [Ground(1, 400, True)]

    size = 320, 240
    black = 0, 0, 0

    window = pygame.display.set_mode(size)


    ground = Ground(...)


    bird = pygame.image.load("ressources/bird1.png")
    birdrect = bird.get_rect()

    isRunning = True

    while isRunning:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        pygame.display.flip()
    return 0

if __name__ == "__main__":
    main()