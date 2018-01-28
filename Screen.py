import pygame, sys, os, random, time
from pygame.locals import *
from pygame.math import *

class Screen:
    def __init__(self, width=640, height=480):
        self.pygame = pygame

        self.pygame.init()
        self.pygame.mouse.set_visible(False)
        self.pygame.display.set_caption('Space invaders v0.1')
        window = pygame.display.set_mode((width, height))
        myFont = self.pygame.font.SysFont("ubuntu", 20)
        self.screen = self.pygame.display.get_surface()
    
    def getInput(self):
        return self.pygame.event.get()

    def getPressedKeys(self):
        return self.pygame.key.get_pressed()

    def fill(self, color):
        self.screen.fill(color)
    
    def flip(self):
        self.pygame.display.flip()
    
    def fillSurface(self, color, surface):
        self.pygame.display.get_surface().fill(color, surface)

    def draw(self, positionX, positionY, color=(255,255,255), dimW=20, dimH=20):
        return self.pygame.draw.rect(self.screen, color, [[positionX,
            positionY],[dimW, dimH]], 1)

    def makeTick(self):
            self.pygame.time.Clock().tick()

    def getMousePosition(self):
        return self.pygame.mouse.get_pos()

