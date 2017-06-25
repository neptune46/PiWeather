#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

DS = 33
STCP = 35
SHCP = 37

class LED8:
    
    def __init__(self, ds, shcp, stcp):
        self.__pin_ds = ds
        self.__pin_shcp = shcp
        self.__pin_stcp = stcp
        
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.__pin_ds, GPIO.OUT)
        GPIO.setup(self.__pin_shcp, GPIO.OUT)
        GPIO.setup(self.__pin_stcp, GPIO.OUT)
        GPIO.output(self.__pin_shcp, False)
        GPIO.output(self.__pin_stcp, False)


    def __del__(self):
        self.setByte(0x00)
        print "cleanup GPIO"
        GPIO.cleanup()
        
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
    led = LED8(DS, SHCP, STCP)
    for i in range(0, 32):
        led.setByte(i)
        time.sleep(10)
        
if __name__ == "__main__": 
    try:
        test()
    except KeyboardInterrupt: 
        print "key board interrupt!"

    print "exit..."