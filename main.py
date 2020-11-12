#!/usr/bin/python3

import sys, pygame

from src.Game import Game

def main():

    game = Game(300, 600)
    game.run()
    # pygame.init()

    # gameObjects = [Ground(1, 400, True)]

    # size = 320, 240
    # black = 0, 0, 0

    # window = pygame.display.set_mode(size)


    # ground = Ground(...)


    # bird = pygame.image.load("ressources/bird1.png")
    # birdrect = bird.get_rect()

    # isRunning = True

    # while isRunning:


    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             isRunning = False

    #     window.fill(black)
    #     window.blit(bird, birdrect)

    #     pygame.display.flip()
    return 0

if __name__ == "__main__":
    main()