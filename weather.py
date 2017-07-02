import temperature
import condition
import time
import RPi.GPIO as GPIO

CODE_SUNNY = 0
CODE_CLOUDY = 1
CODE_PARTLY_CLOUDY = 2
CODE_OVERCAST = 3
CODE_SHOWER_RAIN = 4
CODE_LIGHT_RAIN = 5
CODE_MODERATE_RAIN = 6
CODE_HEAVY_RAIN = 7

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
    day1 = [CODE_SUNNY, 22, 32]
    day2 = [CODE_OVERCAST, 18, 27]
    day3 = [CODE_SHOWER_RAIN, 19, 24]
    data = [day1, day2, day3]
    wth.update(data)
    time.sleep(5)

    wth.clear()

    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
    
    print "cleanup GPIO in exit..."
    GPIO.cleanup()
    print "exit..."
