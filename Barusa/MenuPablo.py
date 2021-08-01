#Version 4.0 de SNAKE

import pygame
from pygame.locals import *
import time
import random
import json

from config import *
from entities import *
import highscore_handler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake v4.0")

        self.surface = pygame.display.set_mode((1000, 500))

        self.players = self.menu()

        pygame.mixer.init()
        self.musica_fondo()

        self.snake = Snake(self.surface)
        self.snake.dibujar_snake()
        self.manzana = Manzana(self.surface)
        self.manzana.dibujar_manzana()

    def musica_fondo(self):
        pygame.mixer.music.load("Recursos/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def musica_juego(self, sonidos):
        if sonidos == "crash":
            sonido = pygame.mixer.Sound("Recursos/crash.mp3")
        elif sonidos == 'ding':
            sonido = pygame.mixer.Sound("Recursos/ding.mp3")
        pygame.mixer.Sound.play(sonido)

    def reset(self):
        self.snake = Snake(self.surface)
        self.manzana = Manzana(self.surface)


    def colision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def fondo_juego(self):
        bg = pygame.image.load("Recursos/fondo2.jpg")
        self.surface.blit(bg, (0,0))

    def jugar(self):
        self.fondo_juego()
        self.snake.mover_snake()
        self.manzana.dibujar_manzana()
        self.score()
        pygame.display.flip()

        # Comer Manzana
        for i in range(self.snake.largo):
            if self.colision(self.snake.x[i], self.snake.y[i], self.manzana.x, self.manzana.y):
                self.musica_juego("ding")
                self.snake.incrementar_largo()
                self.manzana.mover_manzana()

        # Se toca
        for i in range(3, self.snake.largo):
            if self.colision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.musica_juego('crash')
                raise "Se toca"

        # Toca pared
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 500):
            self.musica_juego('crash')
            raise "Toco Pared"

    def score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.largo}",True,(0,0,0))
        self.surface.blit(score,(550,10))

    def perder(self):
        self.fondo_juego()
        self.score = self.snake.largo
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over! Tu score es {self.snake.largo}", True, (236, 255, 0))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Para jugar otra vez presiona Enter. Para salir presiona ESC!", True, (255, 0, 0))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()


    def menu(self):
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
                            return self.plyrs()
                if button_2.collidepoint(mx, my):
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.highscores()
                if button_3.collidepoint(mx, my):
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            exit()
                elif event.type == QUIT:
                    exit()
            pygame.draw.rect(self.surface, (255,0,0), button_1)
            pygame.draw.rect(self.surface, (255,0,0), button_2)
            pygame.draw.rect(self.surface, (255,0,0), button_3)

            self.surface.blit(line1, (400, 90))
            self.surface.blit(line2, (400, 190))
            self.surface.blit(line3, (400, 290))
            pygame.display.update()
    
    def plyrs(self):
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
                            exit()
                elif event.type == QUIT:
                    exit()
            pygame.draw.rect(self.surface, (255,0,0), button_1)
            pygame.draw.rect(self.surface, (255,0,0), button_2)
            self.surface.blit(line1, (400, 90))
            self.surface.blit(line2, (400, 190))
            pygame.display.update()
    
    def highscores(self):
        self.surface = pygame.display.set_mode((1000, 500))
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
                            exit()
                elif event.type == QUIT:
                    exit()
            pygame.draw.rect(self.surface, (255,0,0), button_3)
            self.surface.blit(line1 , (400, 25))
            down = 0
            for x in line2:
                self.surface.blit(x, (400, 90+down))
                down += 27
            self.surface.blit(line3, (400, 290))
            pygame.display.update()

    def game(self):
        running = True
        pausa = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pausa = False

                    if not pausa:
                        if event.key == K_LEFT:
                            self.snake.mover_derecha()

                        if event.key == K_RIGHT:
                            self.snake.mover_izquierda()

                        if event.key == K_UP:
                            self.snake.mover_arriba()

                        if event.key == K_DOWN:
                            self.snake.mover_abajo()

                elif event.type == QUIT:
                    running = False
            try:

                if not pausa:
                    self.jugar()

            except Exception as e:
                self.perder()
                pausa = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.game()

    