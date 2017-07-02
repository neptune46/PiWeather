#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

SHCP1 = 29
STCP1 = 31
DS1   = 32

SHCP2 = 33
STCP2 = 35
DS2   = 37

SHCP3 = 36
STCP3 = 38
DS3   = 40

class LED8:
    
    def __init__(self, ds, shcp, stcp):
        self.__pin_ds = ds
        self.__pin_shcp = shcp
        self.__pin_stcp = stcp
        
        #GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.__pin_ds, GPIO.OUT)
        GPIO.setup(self.__pin_shcp, GPIO.OUT)
        GPIO.setup(self.__pin_stcp, GPIO.OUT)
        GPIO.output(self.__pin_shcp, False)
        GPIO.output(self.__pin_stcp, False)


    def __del__(self):
        self.setByte(0x00)
        
    def delay_ms(self):
        time.sleep(0.001)
        
    def setOneBit(self, bit):
        GPIO.output(self.__pin_ds, bit)
        GPIO.output(self.__pin_shcp, False)
        GPIO.output(self.__pin_shcp, True)

        
    def setByte(self, data):
        print "======== %d ========" % data
        for i in range(8):
            bit = data & 0x01
            self.setOneBit(bit)
            data >>= 1
        GPIO.output(self.__pin_stcp, True)
        GPIO.output(self.__pin_stcp, False)


def test():
    GPIO.setmode(GPIO.BOARD)
    led1 = LED8(DS1, SHCP1, STCP1)
    led2 = LED8(DS2, SHCP2, STCP2)
    led3 = LED8(DS3, SHCP3, STCP3)
    for i in range(0, 130):
        led1.setByte(i)
        led2.setByte(i)
        led3.setByte(i)
        time.sleep(0.1)
        
if __name__ == "__main__": 
    try:
        test()
    except KeyboardInterrupt: 
        print "key board interrupt!"
    
    print "cleanup GPIO"
    GPIO.cleanup()
    print "exit..."