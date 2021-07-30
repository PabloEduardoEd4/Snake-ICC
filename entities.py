import pygame
from pygame.locals import *
import time
import random

from config import *

class Manzana:
    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.manzana = pygame.image.load("Recursos/manzana255.png").convert()
        self.x = 120
        self.y = 120

    def dibujar_manzana(self):
        self.Dibujo.blit(self.manzana, (self.x, self.y))
        pygame.display.flip()

    def mover_manzana(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,11)*SIZE

class Snake:
    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.snake = pygame.image.load("Recursos/cabeza255.png").convert()
        self.direccion = 'abajo'

        self.largo = 1
        self.x = [40]
        self.y = [40]

    def mover_derecha(self):
        self.direccion = 'derecha'

    def mover_izquierda(self):
        self.direccion = 'izquierda'

    def mover_arriba(self):
        self.direccion = 'arriba'

    def mover_abajo(self):
        self.direccion = 'abajo'

    def mover_snake(self):
        for i in range(self.largo-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direccion == 'derecha':
            self.x[0] -= SIZE
        if self.direccion == 'izquierda':
            self.x[0] += SIZE
        if self.direccion == 'arriba':
            self.y[0] -= SIZE
        if self.direccion == 'abajo':
            self.y[0] += SIZE

        self.dibujar_snake()

    def dibujar_snake(self):
        for i in range(self.largo):
            self.Dibujo.blit(self.snake, (self.x[i], self.y[i]))

        pygame.display.flip()

    def incrementar_largo(self):
        self.largo += 1
        self.x.append(-1)
        self.y.append(-1)

class bloques:

    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.bloque = pygame.image.load("piedra_2.jpg").convert()
        self.bloque2 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque3 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque4 = pygame.image.load("piedra_2.jpg").convert()

        self.x = 200
        self.y = 200

        self.bloque5 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque6 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque7 = pygame.image.load("piedra_2.jpg").convert()

        self.bloque8 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque9 = pygame.image.load("piedra_2.jpg").convert()

        self.bloque10 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque11 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque12= pygame.image.load("piedra_2.jpg").convert()
        self.bloque13 = pygame.image.load("piedra_2.jpg").convert()

        self.bloque14 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque15 = pygame.image.load("piedra_2.jpg").convert()
        self.bloque16= pygame.image.load("piedra_2.jpg").convert()
        self.bloque17 = pygame.image.load("piedra_2.jpg").convert()



    def dibujar_pared(self):
        self.Dibujo.blit(self.bloque, (self.x, self.y))
        self.Dibujo.blit(self.bloque2, (self.x+40, self.y+40))
        self.Dibujo.blit(self.bloque3, (self.x+80, self.y+80))
        self.Dibujo.blit(self.bloque4, (self.x+120, self.y+120))


        self.Dibujo.blit(self.bloque5, (self.x+200, self.y+120))
        self.Dibujo.blit(self.bloque6, (self.x+240, self.y+160))
        self.Dibujo.blit(self.bloque7, (self.x+280, self.y+200))

        self.Dibujo.blit(self.bloque9, (self.x+380, self.y+280))
        self.Dibujo.blit(self.bloque8, (self.x+420, self.y+280))

        self.Dibujo.blit(self.bloque10, (self.x+400, self.y-160))
        self.Dibujo.blit(self.bloque11, (self.x+440, self.y-160))
        self.Dibujo.blit(self.bloque12, (self.x+480, self.y-160))
        self.Dibujo.blit(self.bloque13, (self.x+520, self.y-160))

        self.Dibujo.blit(self.bloque14, (self.x+560, self.y-160))
        self.Dibujo.blit(self.bloque15, (self.x+560, self.y-140))
        self.Dibujo.blit(self.bloque16, (self.x+560, self.y-120))
        self.Dibujo.blit(self.bloque17, (self.x+560, self.y-100))


        pygame.display.flip()

class Game:
    def __init__(self, menu = True):
        pygame.init()
        pygame.display.set_caption("Snake v5.0")

        self.surface = pygame.display.set_mode(DISPLAY_MODE)

        if menu:
            self.players = self.menu()

        pygame.mixer.init()
        self.musica_fondo()

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

    def musica_fondo(self):
        pygame.mixer.music.load("Recursos/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def musica_juego(self, sonidos):
        if sonidos == "crash":
            sonido = pygame.mixer.Sound("Recursos/crash.mp3")
        elif sonidos == 'ding':
            sonido = pygame.mixer.Sound("Recursos/ding.mp3")
        pygame.mixer.Sound.play(sonido)

    #NOT SAME
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
        self.bloque.dibujar_pared()
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
        if not (0 <= self.snake.x[0] <= DISPLAY_MODE[0] - 40 and 0 <= self.snake.y[0] <= DISPLAY_MODE[1]):
            self.musica_juego('crash')
            raise "Toco Pared"

    def score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.largo}",True,(0,0,0))
        self.surface.blit(score,(550,10))

    def perder(self):
        self.fondo_juego()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over! Tu score es {self.snake.largo}", True, (236, 255, 0))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Para jugar otra vez presiona Enter. Para salir presiona ESC!", True, (255, 0, 0))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def load(self):
        self.surface = pygame.display.set_mode((1000, 520))
        self.snake = Snake(self.surface)
        self.snake.dibujar_snake()
        self.manzana = Manzana(self.surface)
        self.manzana.dibujar_manzana()
        self.bloque = bloques(self.surface)
        self.bloque.dibujar_pared()

    def run(self):
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
