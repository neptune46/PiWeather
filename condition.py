#!/usr/bin/env python
# encoding: utf-8

import led
import time

disp_value = [
    0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01, 0x00
]

class Condition:
    def __init__(self, n):
        self.__index = 8
        self.__valid = True
        if n == 0:
            self.__led = led.led1
        elif n == 1:
            self.__led = led.led2
        elif n == 2:
            self.__led = led.led3
        else:
            print "ERROR: invalid led number! valid range is 0~2"
            self.__valid = False
    
    def __del__(self):
        print "Deconstruct Condition ..."
        
    def display(self, index):
        if self.__valid == True:
            if index < 0 or index > 7:
                self.__index = 8
            else:
                self.__index = index
            value = disp_value[self.__index]
            self.__led.setByte(value)

    def clear(self):
        if self.__valid == True:
            self.__led.clear()

