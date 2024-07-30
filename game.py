import pygame
from cutWiresModule import cutWiresModule
from colors import *
from driver import *
from Timer import *

def stage2(screen,timer):
    running = True
    placa = Placa()
    pin_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 8)

    module = cutWiresModule(screen)
    for i in range(1,6):
        for j in range(0,2):
            module.add_pin((pin_pos.x*(2*j+1),pin_pos.y*(i*1.3)))

    module.add_wire(0,3, GREEN)
    module.add_wire(2,5, RED)
    module.add_wire(4,7, BLUE)
    module.add_wire(6,9, BLACK)
    module.add_wire(8,1, YELLOW)
    while running:
        if not timer.update_time():
            return False
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray")
        module.draw()
        # desenha um pino para o fio
        if placa.read_button(0):
            module.cut_wire(color= RED)
        if placa.read_button(1):
            module.cut_wire(color= BLUE)
            return False
        if placa.read_button(2):
            module.cut_wire(color= BLACK)
        if placa.read_button(3):
            module.cut_wire(color= GREEN)
            return False
        
        cut_right = 0
        for wire in module.wires:
            if wire["color"] == BLACK and wire["cut"]:
                cut_right +=1
            if wire["color"] == RED and wire["cut"]:
                cut_right +=1
        if cut_right > 0:
            return True


        pygame.display.flip()
