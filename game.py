import pygame
from cutWiresModule import cutWiresModule
from colors import *

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
# my_font = pygame.font.SysFont('Comic Sans MS', 30)

# text_surface = my_font.render('Some Text', False, (0, 0, 0))

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
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    module.draw()
    # desenha um pino para o fio
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        module.cut_wire(color= RED)
    if keys[pygame.K_b]:
        module.cut_wire(color= BLUE)
    if keys[pygame.K_x]:
        module.cut_wire(color= BLACK)
    if keys[pygame.K_g]:
        module.cut_wire(color= GREEN)
    if keys[pygame.K_y]:
        module.cut_wire(color= YELLOW)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for5 framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()