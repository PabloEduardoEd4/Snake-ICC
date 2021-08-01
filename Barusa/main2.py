import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Manzana:
    def __init__(self, dibujar):
        self.dibujar = dibujar
        self.manzana = pygame.image.load("Recursos/manzana255.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.dibujar.blit(self.manzana, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, dibujar):
        self.dibujar = dibujar
        self.serpiente = pygame.image.load("Recursos/cabeza255.png").convert()
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

    def caminar(self):

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

        self.draw()

    def draw(self):
        for i in range(self.largo):
            self.dibujar.blit(self.serpiente, (self.x[i], self.y[i]))

        pygame.display.flip()

    def incrementar_largo(self):
        self.largo += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Joaquin Mendoza")

        pygame.mixer.init()
        self.musica_fondo()

        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Manzana(self.surface)
        self.apple.draw()

    def musica_fondo(self):
        pygame.mixer.music.load('Recursos/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)



    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Manzana(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def fondo_juego(self):
        bg = pygame.image.load("Recursos/Fondo.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.fondo_juego()
        self.snake.caminar()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Comer Manzana
        for i in range(self.snake.largo):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.play_sound("ding")
                self.snake.incrementar_largo()
                self.apple.move()

        # Se toca
        for i in range(3, self.snake.largo):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Se toco la cola"

        # Toca pared
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound('crash')
            raise "Toco Pared"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.largo}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def show_game_over(self):
        self.fondo_juego()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over! Tu score es {self.snake.largo}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Para jugar otra vez presiona Enter. Para salir presiona ESC!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
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

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.run()