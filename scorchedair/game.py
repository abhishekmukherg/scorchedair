import pygame
from pygame.locals import *

class Game(object):
    def __init__(self):
        """Game init"""
        self.screen = pygame.display.set_mode((700,700))
        pygame.display.set_caption('Scorched Air')
        
    def update(self):
        """Updates the game"""
        pass
    
    def render(self):
        """Draws the game to the screen"""
        #Fill with black
        self.screen.fill((0,0,0))
    
    def over(self):
        """Returns true if game is over, false otherwise"""
        return False