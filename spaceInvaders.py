import pygame, sys, os, random, time
from pygame.locals import *

class Screen:
    def __init__(self, width=640, height=480):
        self.pygame = pygame

        self.pygame.init()
        self.pygame.mouse.set_visible(False)
        self.pygame.display.set_caption('Space invaders v0.1')
        window = pygame.display.set_mode((width, height))
        myFont = self.pygame.font.SysFont("ubuntu", 20)
        self.screen = self.pygame.display.get_surface()
    
    def input(self):
        for event in self.pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)
                if event.key == K_LEFT:
                    pass
                if event.key == K_RIGHT:
                    pass
                if event.key == K_SPACE:
                    pass
                if event.key == K_a:
                    pass
                else:
                    print event

    def fill(self, color):
        self.screen.fill(color)
    
    def flip(self):
        self.pygame.display.flip()
    
    def fillSurface(self, color, surface):
        self.pygame.display.get_surface().fill(color, surface)

    def draw(self, mouseX, mouseY):
        return self.pygame.draw.rect(self.screen,(255,255,255),[[mouseX,mouseY],[50, mouseY+10]], 1)

    def makeTick(self):
            self.pygame.time.Clock().tick()

class Game:
    def __init__(self, screen):
        self.screen = screen

    def startGame(self):
        while True:
            self.screen.input()
            self.screen.fill((0,0,0))
            desk = self.screen.draw(100,100)
            self.screen.fillSurface(Color("red"), desk)

            self.screen.flip()

            time.sleep(0.007)
            self.screen.makeTick()

if __name__ == "__main__":
    screen = Screen()
    game = Game(screen)
    game.startGame()
