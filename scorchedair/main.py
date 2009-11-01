import pygame, sys
from game import *

pygame.init()

game = Game()
clock = pygame.time.Clock()

#Main game loop
while not game.over():
    #Read pygame events
    for event in pygame.event.get():
        #Handle quit events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    
    #Limit to 60 fps
    clock.tick(60)
    
    #Update the game
    game.update()
    #Render the game
    game.render()
    
    pygame.display.flip()