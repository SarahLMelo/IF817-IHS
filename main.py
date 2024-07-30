import pygame
import random
import numpy as np
from driver import *

IMAGE_PATH = 'assets/UI Pixels/Blue/ScrollBars/Sprite-0006.png'
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
ON = 1
OFF = 0
placa = Placa()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def load_image(image_path):
    return pygame.image.load(image_path)

def load_assets():
    assets = {}
    assets["bar"] = load_image(IMAGE_PATH)
    return assets

def fill_bar(percent, bar, bar_switch, initial_x, initial_y, spacing):
    for _ in range(0, percent//10):
        screen.blit(bar, (initial_x, initial_y))
        initial_y -= spacing

    screen.blit(bar_switch, (initial_x, initial_y + spacing))

def main():
    spacing_between_bars = (SCREEN_WIDTH-10)*0.0588

    assets = load_assets()
    screen.fill((50, 58, 69))
    bar_background = pygame.Surface(assets["bar"].get_size(), pygame.SRCALPHA)
    bar_background.blit(assets["bar"], (0,0), (0, 0, 16, 48))
    bar_fill = pygame.Surface(assets["bar"].get_size(), pygame.SRCALPHA)
    bar_fill.blit(assets["bar"], (0,0), (16, 30, 10, 15))
    bar_switch =  pygame.Surface(assets["bar"].get_size(), pygame.SRCALPHA)
    bar_switch.blit(assets["bar"], (0,0), (32, 30, 30, 15))

    run = True
    target = [random.choice([ON,OFF]) for i in range(17)]
    link = np.random.permutation([i for i in range(17)])

    

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        barX = 5
        barY = SCREEN_WIDTH*0.3
        bar_background = pygame.transform.scale(bar_background, (int(SCREEN_WIDTH*0.2), int(SCREEN_HEIGHT*0.2)))
        bar_fill = pygame.transform.scale(bar_fill, (int(SCREEN_WIDTH*0.2), int(SCREEN_HEIGHT*0.2)))
        bar_switch = pygame.transform.scale(bar_switch, (int(SCREEN_WIDTH*0.2), int(SCREEN_HEIGHT*0.2)))
        spacing = (bar_background.get_height() - 5*(bar_background.get_height()) / 48)//10

        swiches_status = [placa.read_switche(i) for i in range(17)]
        for i in range(17):
            screen.blit(bar_background, (barX, barY))
            if swiches_status[link[i]]:
                fill_bar(100, bar_fill, bar_switch, barX, barY + bar_background.get_height()*0.7, spacing)
            else:
                fill_bar(0, bar_fill, bar_switch, barX, barY + bar_background.get_height()*0.7, spacing)
            barX += spacing_between_bars
        pygame.display.update()

    pygame.quit()