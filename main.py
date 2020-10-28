#!/usr/bin/python3

import sys, pygame

def main():

    pygame.init()

    size = width, height = 320, 240
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("ressources/bird1.png")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
    return 0

if __name__ == "__main__":
    main()