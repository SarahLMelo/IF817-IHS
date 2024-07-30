import pygame
import math
import random
from colors import *


class cutWiresModule:
    def __init__(self,surface):
        self.surface = surface
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()
        self.pin_size =  (self.surface_width/30,self.surface_width/30)
        self.wires_blend = math.floor(self.pin_size[1]/3)
        self.pins = []
        self.wires = []

    # adiciona um pin e retorna o seu id
    def add_pin(self,position):
        self.pins.append((position[0] - self.pin_size[0]/2,position[1] - self.pin_size[1]/2))
        return (len(self.pins) - 1)
    
    # adiciona um fio ligando dois pinos 
    # pin1 e pin2 são ids dos pinos
    def add_wire(self,pin1,pin2,color):
        if pin1 < len(self.pins) and pin2 < len(self.pins):
            used_pins = [wire['link'] for wire in self.wires]
            used_pins = list(zip(*used_pins))
            if used_pins:
                used_pins = used_pins[0] + used_pins[1]
            if pin1 not in used_pins and pin2 not in used_pins:
                self.wires.append({'cut': False, 'link': (pin1,pin2), 'color': color})
                return True
        return False
    def cut_wire(self,index = None,color = None):
        if not color:
            self.wires[index]['cut'] = True
        else: 
            for wire in self.wires:
                if wire['color'] == color:
                    wire['cut'] = True


    #desenha o esquema do Modulo
    def draw(self):
        for pin_position in self.pins:
            self.draw_pin(pin_position, self.pin_size)
        for wire_status in self.wires:
            wire = wire_status['link']
            wire_start = (self.pins[wire[0]][0] + self.pin_size[0]/2,self.pins[wire[0]][1]+ self.pin_size[0]/2)
            wire_end = (self.pins[wire[1]][0]+ self.pin_size[0]/2,self.pins[wire[1]][1]+ self.pin_size[0]/2)
            wire_color = wire_status['color']
            if not wire_status['cut']:
                self.draw_wire(wire_start, wire_end,color= wire_color,blend=self.wires_blend)
            else:
                add_tuple = lambda t1, t2:  tuple(map(lambda x,y: x+y,t1,t2))
                dw = wire_end[0] - wire_start[0]
                dh = wire_end[1] - wire_start[1]
                self.draw_wire(wire_start, add_tuple(wire_end,(-dw*0.58,-dh*0.58)),color= wire_color,blend=self.wires_blend)
                self.draw_wire(add_tuple(wire_start,(dw*0.5,dh*0.5)), wire_end,color= wire_color,blend=self.wires_blend)


    def draw_pin(self,position,size = (30,30),padding = 5,border_radio = 0):

        # desenha retângulo externo com uma borda passante de tamanho "padding"
        position_out = (position[0]-padding,position[1]-padding)
        size_out = (size[0] + 2*padding,size[1] + 2*padding)
        rect_out = pygame.Rect(position_out,size_out)
        pygame.draw.rect(self.surface,GRAY,rect_out,width=0,border_radius=border_radio)

        # desenha retângulo interno em posição e tamanho estabelecido
        rect_inner = pygame.Rect(position,size)
        pygame.draw.rect(self.surface, BLACK,rect_inner,width=0,border_radius=border_radio)

    def draw_wire(self,start,end,color = RED,blend = 10):
        start = (start[0],start[1])
        end = (end[0],end[1])
        pygame.draw.line(self.surface,color,start,end, blend)