from pygame.math import *

class SpaceShip:
    def __init__(self):
        self.acceleraction = Vector2(0, 0)
        self.velocity =  Vector2(0, 0)
        self.shipPosition = Vector2(0,0)


    def _moveShip(self, force):
        self.acceleraction += force
        self.velocity *= 0.1
        self.velocity += self.acceleraction
        self.shipPosition += self.velocity
        self.acceleraction *= 0

    def moveToRight(self):
        self._moveShip(Vector2(1,0))
    
    def moveToLeft(self):
        self._moveShip(Vector2(-1,0))
   
    def moveToUp(self):
        self._moveShip(Vector2(0,-1))
  
    def moveToDown(self):
        self._moveShip(Vector2(0,1))
