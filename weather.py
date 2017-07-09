#!/usr/bin/env python
# encoding: utf-8

import temperature
import condition
import hefengapi
import time
import RPi.GPIO as GPIO

class Weather:
    __weatherCondi = [0, 0, 0]
    __airTemp = [0, 0, 0]

    def __init__(self):
        for i in range(3):
            self.__weatherCondi[i] = condition.Condition(i)
            self.__airTemp[i] = temperature.TempDisplay(i)

    def update(self, data):
        for i in range(3):
            self.__weatherCondi[i].display(data[i][0])
            self.__airTemp[i].setTemp(data[i][1], data[i][2])
    
    def clear(self):
        for i in range(3):
            self.__weatherCondi[i].clear()
            self.__airTemp[i].clear()

def main():
    print "start..."
    wth = Weather()
    data = hefengapi.getWeather()
    wth.update(data)
    time.sleep(20)
    wth.clear()

    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
    
    print "cleanup GPIO in exit..."
    GPIO.cleanup()
    print "exit..."
