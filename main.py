# Snake version 5.0

import pygame
from pygame.locals import *

import highscore_handler
from config import *

import login
import menu

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    name = login.register(surface)
    if name == None:
        exit()
    plys = menu.menu(surface)
    game_name = name
    if plys == 2:
        name1 = login.register(surface, text = "Type Name of P2")
        game_name = f'{name} v {name1}'
        if name1 == None:
            exit()
    with open('pastgames.txt', 'a+') as file:
        file.write(f'{game_name}\n')
    print(name, plys)
    '''
    highscore_handler.add('Pablo', 5)
    input()
    print(highscore_handler.get())
    '''