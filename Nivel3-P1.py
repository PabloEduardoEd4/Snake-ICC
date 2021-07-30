
import pygame
from pygame.locals import *
import time
import random

from config import *
from entities import *

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
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Joaquin M")

        pygame.mixer.init()
        self.musica_fondo()

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
        self.bloque = bloques(self.surface)


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
        if not (0 <= self.snake.x[0] <= 960 and 0 <= self.snake.y[0] <= 500):
            self.musica_juego('crash')
            raise "Toco Pared"

        print(self.snake.y[0])

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

    

    def run(self):
        self.surface = pygame.display.set_mode((1000, 520))
        self.snake = Snake(self.surface)
        self.snake.dibujar_snake()
        self.manzana = Manzana(self.surface)
        self.manzana.dibujar_manzana()
        self.bloque = bloques(self.surface)
        self.bloque.dibujar_pared()

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
    game.run()