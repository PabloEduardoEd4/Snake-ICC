# Snake version 5.0

import pygame
from pygame.locals import *

import highscore_handler
from config import *
from levels import *

import login
import menu
from classgame import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    name = login.register(surface)
    print(name)
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
    if plys == 1:
        points = [20,35,40,45]
        curscore = 0
        for x in range(len(P1)):
            game = P1Game(walls = P1[x], maxscore = points[x],surface = surface)
            notlost, score = game.run()
            curscore += score
            if not notlost:
                break
        highscore_handler.add(game_name, curscore)
    '''
    highscore_handler.add('Pablo', 5)
    input()
    print(highscore_handler.get())
    '''