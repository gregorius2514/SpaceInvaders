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
                else:
                    return event.key

    def startGame(self):
        moveRight = False
        moveLeft = False
        moveUp = False
        moveDown = False
        stop = True

        while True:
            key = self.handleInput()
            if key == K_RIGHT:
                moveRight = True
                moveLeft = False
            elif key == K_LEFT:
                moveLeft = True
                moveRight = False
            elif key == K_UP:
                moveUp = True
                moveDown = False
            elif key == K_DOWN:
                moveDown = True
                moveUp = False
            elif key == K_SPACE:
                stop = not stop
                moveDown = False
                moveUp = False
                moveLeft = False
                moveRight = False

            if not stop:
                if moveRight:
                    self.spaceShip.moveToRight()
                if moveLeft:
                    self.spaceShip.moveToLeft()
                if moveUp:
                    self.spaceShip.moveToUp()
                if moveDown:
                    self.spaceShip.moveToDown()

            self.screen.fill((0,0,0))
            desk = self.screen.draw(self.spaceShip.shipPosition.x,
                    self.spaceShip.shipPosition.y)
            self.screen.fillSurface(Color("red"), desk)

            self.screen.flip()

            time.sleep(0.007)
            self.screen.makeTick()
