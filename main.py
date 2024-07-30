import pygame
import random
import numpy as np
from driver import *
from Bar import *
from Timer import *
IMAGE_PATH = 'assets/UI Pixels/Blue/ScrollBars/Sprite-0006.png'
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
ON = True
OFF = False
placa = Placa()

def main(screen,timer):
    bar_blue = Bar(screen,"Blue")
    bar_red = Bar(screen,"Red")

    run = True
    target = [random.choice([ON,OFF]) for i in range(17)]
    link = np.random.permutation([i for i in range(17)])

    

    while run:
        if not timer.update_time():
            return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bar_blue.draw()
        bar_red.draw()

        swiches_status = [placa.read_switche(i) for i in range(18)]
        
            
        for i in range(17):
            bar_blue.blit()
            bar_red.blit()
            if swiches_status[link[i]]:
                if target[i]:
                    bar_blue.fill_bar(100)
                else:
                    bar_red.fill_bar(100)
            else:
                if target[i]:
                    bar_red.fill_bar(0)
                else:
                    bar_blue.fill_bar(0)
        
            bar_blue.next()
            bar_red.next()
        if swiches_status[17]:
            run = False
        pygame.display.update()
    for i in range(17):
        if swiches_status[link[i]] != target[i]:
            return False
    return True