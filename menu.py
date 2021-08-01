import pygame
from pygame.locals import *

import highscore_handler

def menu(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('arial', 30)
    line1 = font.render(f"JUGAR", True, (250, 255, 255))
    line2 = font.render(f"HIGHSCORES", True, (250, 255, 255))
    line3 = font.render(f"SALIR", True, (255, 255, 255))

    button_1 = pygame.Rect(250,50,500,100)
    button_2 = pygame.Rect(250,160,500,100)
    button_3 = pygame.Rect(250,270,500,100)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_1.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        res = plyrs(surface) 
                        if res != None:
                            return res
            if button_2.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return highscores(surface)
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        exit()
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (255,0,0), button_1)
        pygame.draw.rect(surface, (255,0,0), button_2)
        pygame.draw.rect(surface, (255,0,0), button_3)

        surface.blit(line1, (400, 90))
        surface.blit(line2, (400, 190))
        surface.blit(line3, (400, 290))
        pygame.display.update()
    
def plyrs(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('arial', 30)
    line1 = font.render(f"1 Player", True, (250, 255, 255))
    line2 = font.render(f"2 Player", True, (250, 255, 255))
    line3 = font.render(f"SALIR", True, (255, 255, 255))

    button_1 = pygame.Rect(250,50,500,100)
    button_2 = pygame.Rect(250,160,500,100)
    button_3 = pygame.Rect(250,270,500,100)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_1.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return 1
            if button_2.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return 2
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return menu(surface)
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (255,0,0), button_1)
        pygame.draw.rect(surface, (255,0,0), button_2)
        pygame.draw.rect(surface, (255,0,0), button_3)
        surface.blit(line1, (400, 90))
        surface.blit(line2, (400, 190))
        surface.blit(line3, (400, 290))
        pygame.display.update()

def highscores(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('arial', 30)
    line1 = font.render(f"Highscores", True, (250, 255, 255))
    highscores = highscore_handler.get()
    highscores = [f'{x} : {highscores[x]}'for x in highscores.keys()]
    line2 = [font.render(x, True, (250, 255, 255)) for x in highscores][:5]
    line3 = font.render(f"Salir", True, (255, 255, 255))

    #button_1 = pygame.Rect(250,50,500,100)
    #button_2 = pygame.Rect(250,160,500,100)
    button_3 = pygame.Rect(250,270,500,100)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return menu(surface)
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (255,0,0), button_3)
        surface.blit(line1 , (400, 25))
        down = 0
        for x in line2:
            surface.blit(x, (400, 90+down))
            down += 27
        surface.blit(line3, (400, 290))
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode((1000, 500))
    print(menu(surface))