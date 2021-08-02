import pygame
from pygame.locals import *

from Nivel1_P1 import Game as n1
from Nivel2_P1 import Game as n2
from Nivel3_P1 import Game as n3
from Nivel4_P1 import Game as n4

from config import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    game = n1(surface)
    game.run()
    print(1)
    game = n2(surface)
    game.run()
    print(2)
    game = n3(surface)
    game.run()
    print(3)
    game = n4(surface)
    game.run()
    print(4)