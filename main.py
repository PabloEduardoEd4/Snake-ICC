# Snake version 5.0

import pygame
from pygame.locals import *
import time
from random import randint
import json

import highscore_handler

import login
import menu

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode((1000, 500))
    login.register(surface)
    menu.menu(surface)
    '''
    highscore_handler.add('Pablo', 5)
    input()
    print(highscore_handler.get())
    '''