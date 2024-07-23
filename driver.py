#!/usr/bin/python3

import os, sys
from fcntl import ioctl

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

class Placa:
    def __init__(self):
        self.char_driver = os.open("/dev/mydev", os.O_RDWR)
        self.convert_display_table = [0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x78,0x0,0x10]
        # realiza leitura inicial para p driver ter um bom funcionamento
        self.left_display_status = 0x40404040
        self.right_display_status = 0x40404040
        self.led_status = 0xFFFFFFFF
        ioctl(self.char_driver, RD_PBUTTONS)
        os.read(self.char_driver, 4)

    def convert_num_to_hex(self,num):
        if num < len(self.convert_display_table) and num >= 0:
            return self.convert_display_table[num]
        else:
            print("numero inserido nao pode ser escrito em display")

    def write_display(self,display,num):
        # convert num para hexadecimal
        hex = self.convert_num_to_hex(num)
        # escreve valor no display correspondente
        if display >= 0 and display <=3:
            ioctl(self.char_driver, WR_R_DISPLAY)
        elif display >=4 and display <= 7:
            ioctl(self.char_driver, WR_L_DISPLAY)
            display = (display - 4)

        data = hex << (display*8)
        clear = ~ (0xFF << (display*8))
        self.right_display_status = (self.right_display_status & clear) + data

        os.write(self.char_driver, self.right_display_status.to_bytes(4, 'little'))

    def read_button(self,num):
        if num >= 0 and num <=3 :
            ioctl(self.char_driver, RD_PBUTTONS)
            buttons = os.read(self.char_driver, 1)
            num = 0x1 << num
            if (int.from_bytes(buttons,'little') & num):
                return False
            return True
        else:
            print("button nao existe")

    def read_switche(self,num):
        if num >= 0 and num <=17 :
            ioctl(self.char_driver, RD_SWITCHES)
            buttons = os.read(self.char_driver, 3)
            num = 0x1 << num
            if (int.from_bytes(buttons,'little') & num):
                return True
            return False
        else:
            print("button nao existe")

    def write_led(self,color,acender,num):
        ioctl(self.char_driver, WR_GREEN_LEDS)
        data = 0x1 << num
        if color == 'green':
            data = data << 18

        if acender:
            self.led_status = self.led_status | data
        else:
            self.led_status = self.led_status & (~data)
        os.write(self.char_driver, self.led_status.to_bytes(4, 'little'))

