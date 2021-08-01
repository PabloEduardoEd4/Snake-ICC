import pygame
from pygame.locals import *
import time
import random

T=40
class Manzana:
    def  __init__(self,dibujo):
        self.dibujo = dibujo
        self.manzana = pygame.image.load("Recursos/manzana255.png").convert()
        self.x =120
        self.y =120

    def dibujar(self):
        self.dibujo.blit(self.manzana,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*T
        self.y = random.randint(1,19)*T

class Snake:
    def __init__(self,dibujo):
        self.dibujo = dibujo
        self.cuerpo = pygame.image.load("Recursos/cabeza255.png").convert()
        self.largo = 1
        self.cuerpox = [T]
        self.cuerpoy = [T]
        self.direccion = "abajo"

    def dibujar(self):
        for x in range(self.largo):
            self.dibujo.blit(self.cuerpo,(self.cuerpox[x],self.cuerpoy[x]))
        pygame.display.flip()

    def tamano(self):
        self.largo += 1
        self.x.append(-1)
        self.y.append(-1)

    def mover_derecha(self):
        self.direccion = "derecha"
    def mover_izquierda(self):
        self.direccion = "izquierda"
    def mover_arriba(self):
        self.direccion = "arriba"
    def mover_abajo(self):
        self.direccion = "abajo"

    def caminar(self):
        
        for x in range(self.largo-1,0,-1):
            self.cuerpoy[x] = self.cuerpoy[x-1]
            self.cuerpox[x] = self.cuerpox[x-1]

        if self.direccion == "arriba":
            self.cuerpoy[0] -= T
        if self.direccion == "abajo":
            self.cuerpoy[0] += T
        if self.direccion == "derecha":
            self.cuerpox[0] -= T
        if self.direccion == "izquierda":
            self.cuerpox[0] += T

        self.dibujar()


class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.musica_fondo()
        self.surface = pygame.display.set_mode((1000,800))
        self.snake = Snake(self.surface)
        self.snake.dibujar()
        self.manzana = Manzana(self.surface)
        self.manzana.dibujar()
    
    def musica_fondo(self):
        pygame.mixer.music.load('Recursos/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def efecto_sonidos(self, sonido):
        if sonido == "golpe":
            sound = pygame.mixer.Sound("Recursos/crash.mp3")
        elif sonido == 'nom':
            sound = pygame.mixer.Sound("Recursos/ding.mp3")
        pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = Snake(self.surface)
        self.manzana = Manzana(self.surface)

    def comer(self, x1, x2, y1, y2):
        if x1 >= x2 and x1 < x2 + T:
            if y1 >= y2 and y1 < y2 + T:
                return True
        return False

    def Fondo(self):
        fondo = pygame.image.load("Recursos/Fondo.jpg")
        self.surface.blit(fondo, (0,0))

    def Puntaje(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.largo}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def Perder(self):
        self.Fondo()
        font = pygame.font.SysFont('arial', 30)
        linea1 = font.render(f"Game over! Tu score es {self.snake.largo}", True, (255, 255, 255))
        self.surface.blit(linea1, (200, 300))
        linea2 = font.render("Para jugar otra vez presiona Enter. Para salir presiona ESC!", True, (255, 255, 255))
        self.surface.blit(linea2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def correrJuego(self):
        self.Fondo()
        self.snake.caminar()
        self.manzana.dibujar()
        self.Puntaje()
        pygame.display.flip()

        #come mansana
        for x in range(self.snake.largo):
            if self.comer(self.snake.cuerpox[x], self.snake.cuerpoy[x], self.manzana.x, self.manzana.y):
                self.efecto_sonidos("nom")
                self.snake.tamano()
                self.manzana.move()

        # Se toca
        for x in range(3, self.snake.largo):
            if self.comer(self.snake.cuerpox[0], self.snake.cuerpoy[0], self.snake.cuerpox[x], self.snake.cuerpoy[x]):
                self.efecto_sonidos('golpe')

        # toca borde
        if not (0 <= self.snake.cuerpox[0] <= 1000 and 0 <= self.snake.cuerpoy[0] <= 800):
            self.efecto_sonidos('golpe')


    def run (self):
        juego = True
        pausa = False

        while juego:
            for event in pygame.event.get():
                if event.type  ==  KEYDOWN:
                    if event.key == K_ESCAPE:
                        juego = False
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

                elif event.type== QUIT:
                    juego = False
            try:

                if not pausa:
                    self.play()

            except Exception as e:
                self.Perder()
                pausa = True
                self.reset()

            time.sleep(.1)


if __name__ == '__main__':
    juego = Juego()
    juego.run()


            