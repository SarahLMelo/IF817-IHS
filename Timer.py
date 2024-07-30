from driver import *
import pygame
class Timer:
    def __timer__(self):
        self.placa = Placa()
        self.clock = pygame.time.Clock()
        self.time = 120*1000
    def set_time(self):
        resto = self.time
        #calcular os minutos
        minutos = resto // 60000
        #calcular dsegundos
        resto -= minutos*60000
        dsegundos =  resto // 10000

        resto -= dsegundos*10000
        usegundos = resto // 1000

        self.placa.write_display(6,minutos)
        self.placa.write_display(5,dsegundos)
        self.placa.write_display(4,usegundos)
    def update_time(self):
        milli = self.clock.tick()
        self.time -= milli
        if self.time < 0:
            return False
        self.set_time()
        return True
        
        