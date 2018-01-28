import pygame, sys, os, random, time
from pygame.locals import *
from pygame.math import *

from Screen import *
from SpaceShip import *

class Game:
    def __init__(self, screen, spaceShip):
        self.screen = screen
        # move class SpaceShip to main class and inject it to Game class
        self.spaceShip = spaceShip

    def handleInput(self):
        for event in self.screen.getInput():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)

    def handleSpaceShipMovement(self):
        keys = self.screen.getPressedKeys()

        if keys[pygame.K_RIGHT]:
            self.spaceShip.moveToRight()
        if keys[pygame.K_LEFT]:
            self.spaceShip.moveToLeft()
        if keys[pygame.K_UP]:
            self.spaceShip.moveToUp()
        if keys[pygame.K_DOWN]:
            self.spaceShip.moveToDown()

    def startGame(self):
        while True:
            self.handleInput()
            self.handleSpaceShipMovement()

            self.screen.fill((0,0,0))
            desk = self.screen.draw(self.spaceShip.shipPosition.x,
                    self.spaceShip.shipPosition.y)
            self.screen.fillSurface(Color("red"), desk)

            self.screen.flip()

            time.sleep(0.007)
            self.screen.makeTick()
