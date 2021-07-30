#Intento 3

import pygame
from pygame.locals import *
import time
import random

from config import *
from entities import *

if __name__ == '__main__':
    game = Game()
    game.load()
    game.run()