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