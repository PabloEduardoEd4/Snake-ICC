import pygame
from pygame.locals import *
import time
from random import randint
import json

def register(surface):
    surface.fill((0,0,0))
    name = ''
    font = pygame.font.SysFont('arial',30)
    line1 = font.render(f"Type Name", True, (250, 255, 255))
    surface.blit(line1 , (400, 25))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return name if name != '' else 'Anon' + str(randint(1,1010101010))
                else:
                    name += event.unicode
        name_obj = font.render(name, True, (255, 255, 255))
        
        surface.blit(name_obj , (0, 250))
        pygame.display.update()
    

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode((1000, 500))
    print(register(surface))