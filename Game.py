import pygame, sys, os, random, time
from pygame.locals import *
from pygame.math import *

from Screen import *

class Game:
    def __init__(self, screen):
        self.screen = screen

    def handleInput(self):
        for event in self.screen.getInput():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)
                else:
                    return event.key


    def startGame(self):
        while True:
            self.handleInput()
            self.screen.fill((0,0,0))
            desk = self.screen.draw(100,100)
            self.screen.fillSurface(Color("red"), desk)

            self.screen.flip()

            time.sleep(0.007)
            self.screen.makeTick()
