import pygame
from main import main

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def menu():
    screen.fill((50, 58, 69))

    # Write text
    font = pygame.font.Font(None, 36)
    text = font.render("Press Enter to Start", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(text, textRect)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main()
                run = False

        pygame.display.update()

    pygame.quit()

menu()