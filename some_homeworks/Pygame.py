import sys
import pygame


def run_script():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(print(event.key))


run_script()