from player import *
from animator import *
from tile import *
from board import *
import pygame
import os

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('/', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    clock = pygame.time.Clock()
    path = os.path.dirname(os.path.realpath(__file__)) + '/..'

    direction = '-'
    board = Board()
    tiles = board.getTiles("level1.txt");
    #board object can be created here, and the parameter for the __init__ can be the level file at [path + '/levels/level1.txt']
    #it can have check() to check if jumps are possible
    #update() to edit tiles after a jump
    #and getPlayerInitPos() so we can put the players in the right position initially. 
        #Maybe this can be an array like this [[9,6],[12,11]]

    p1 = Player(path + '/animation/character1/', 9, 6)
    p2 = Player(path + '/animation/character2/', 12, 11)

    #Maybe this animation objects can be somehow part of the board? Think about later
    anims = [	
    	Animator(path + '/animation/coin/', 9, 3),
    	Animator(path + '/animation/dice2/', 3, 12),
    	Animator(path + '/animation/dice1/', 14, 4),
    	Animator(path + '/animation/pin2/', 12, 9)
    ]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if pygame.key.get_pressed()[pygame.K_w]:
            direction = 'up'
        elif pygame.key.get_pressed()[pygame.K_a]:
            direction = 'left'
        elif pygame.key.get_pressed()[pygame.K_s]:
            direction = 'down'
        elif pygame.key.get_pressed()[pygame.K_d]:
            direction = 'right'
        else:
        	direction = 'idle'

        screen.fill((255, 255, 255))
        screen.blit(get_image(path + '/animation/bg_2.png'), (0, 0))
        screen.blit(get_image(path + '/animation/label.png'), (0, 560))

        for i in range(len(tiles)):
            screen.blit(get_image(path + tiles[i].path), tiles[i].getRealXY())
       
        p1.update(direction, screen) #add board parameter to check if jump is possible
        p2.update(direction, screen)

        for i in range(len(anims)):
        	anims[i].update(screen)

        
        pygame.display.flip()
        clock.tick(60)

main()