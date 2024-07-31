
import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
class Bar:
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color
        self.path = "assets/UI Pixels/"+self.color+"/ScrollBars/Sprite-0006.png"
        self.assets = {}

        self.spacing_between_bars = (SCREEN_WIDTH-10)*0.0588
        self.load_assets()
        self.bar_background = pygame.Surface(self.assets["bar"].get_size(), pygame.SRCALPHA)
        self.bar_background.blit(self.assets["bar"], (0,0), (0, 0, 16, 48))
        self.bar_fill = pygame.Surface(self.assets["bar"].get_size(), pygame.SRCALPHA)
        self.bar_fill.blit(self.assets["bar"], (0,0), (16, 30, 10, 15))
        self.bar_switch =  pygame.Surface(self.assets["bar"].get_size(), pygame.SRCALPHA)
        self.bar_switch.blit(self.assets["bar"], (0,0), (32, 30, 30, 15))

    def draw(self):
        self.barX = 5
        self.barY = SCREEN_WIDTH*0.3
        self.bar_background = pygame.transform.scale(self.bar_background, (int(SCREEN_WIDTH*0.2), int(SCREEN_HEIGHT*0.2)))
        self.bar_fill = pygame.transform.scale(self.bar_fill, (int(SCREEN_WIDTH*0.2), int(SCREEN_HEIGHT*0.2)))
        self.bar_switch = pygame.transform.scale(self.bar_switch, (int(SCREEN_WIDTH*0.2), int(SCREEN_HEIGHT*0.2)))
        self.spacing = (self.bar_background.get_height() - 5*(self.bar_background.get_height()) / 48)//10
    def next(self):
        self.barX += self.spacing_between_bars
    def blit(self):
        self.screen.blit(self.bar_background, (self.barX, self.barY))
    def load_image(self):
        return pygame.image.load(self.path)
    def load_assets(self):
        self.assets = {}
        self.assets["bar"] = self.load_image()
        return self.assets
    def fill_bar(self,percent):
        initial_y = self.barY + self.bar_background.get_height()*0.7
        for _ in range(0, percent//10):
            self.screen.blit(self.bar_fill, (self.barX, initial_y))
            initial_y -= self.spacing

        self.screen.blit(self.bar_switch, (self.barX, initial_y+ self.spacing))
    
    