from Screen import *
from Game import *
from SpaceShip import *

if __name__ == "__main__":
    screen = Screen()
    spaceShip = SpaceShip()
    game = Game(screen, spaceShip)
    game.startGame()
