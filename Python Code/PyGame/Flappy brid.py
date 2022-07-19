import sys
import time
import random
import pygame
from pygame.locals import *


class Brid():
    def __init__(self, screen):
        self.brid = pygame.image.load('img/hero1.png')
        self.screen = screen
        # self.pipe = pygame.image.load('img/')
        self.fall = 10
        self.rise = 40
        self.x = 70
        self.y = 300

    def control(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_SPACE]:
            self.y -= self.rise

    def down(self):
        if self.y <= 700:
            self.y += self.fall
        if self.y >= 10:
            self.control()
        else:
            self.y = self.y

    def display(self):
        self.screen.blit(self.brid, (self.x, self.y))


class GameBackground:
    def __init__(self, screen):
        pygame.init()
        self.background1 = pygame.image.load('img/background.png')
        self.background2 = pygame.image.load('img/background.png')
        self.screen = screen
        self.x1 = 0
        self.x2 = 480

    def move(self):
        self.x1 -= 2
        self.x2 -= 2
        if self.x1 <= -480:
            self.x1 = 0
        if self.x2 <= 0:
            self.x2 = 480

    def draw(self):
        self.screen.blit(self.background1, (self.x1, 0))
        self.screen.blit(self.background2, (self.x2, 0))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 852))
        pygame.display.set_caption('Flappy Brid')
        self.bk = GameBackground(self.screen)
        self.brid = Brid(self.screen)

    def game_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.game_quit()
            self.bk.move()
            self.bk.draw()
            self.brid.down()
            self.brid.display()
            pygame.display.update()
            time.sleep(0.03)


if __name__ == '__main__':
    game = Game()
    game.run()
