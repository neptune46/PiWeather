import tm1637
import time
import RPi.GPIO as GPIO

# 4 digits Seven-Segment-Display for Mininum/Maximum temperature (-9~99)

class TempDisplay:
    __temp_min = 0
    __temp_max = 0
    
    def __init__(self, ssd):
        self.__ssd = ssd
        
    def setTemp(self, min, max):
        self.__temp_min = min
        self.__temp_max = max
        min_symbol = self.val2sym(self.__temp_min)
        max_symbol = self.val2sym(self.__temp_max)
        self.__ssd.display_digit(min_symbol + max_symbol)

    def val2sym(self, val):
        if val>=0 and val <=99:
            h = val/10
            l = val%10
            return [str(h), str(l)]
        elif val <= -1 and val >= -9 :
            return ['-', str(-val)]
        else:
            return ['-', '-']

    def clear(self):
        self.__ssd.clear()

tempDisp1 = TempDisplay(tm1637.ssd1)
tempDisp2 = TempDisplay(tm1637.ssd2)
tempDisp3 = TempDisplay(tm1637.ssd3)

def test(tempDisp):

    tempDisp.setTemp(21, 30)
    time.sleep(0.1)

    tempDisp.setTemp(17, 29)
    time.sleep(0.1)

    tempDisp.setTemp(-5, -2)
    time.sleep(0.1)

    tempDisp.setTemp(0, 1)
    time.sleep(0.1)

    tempDisp.setTemp(-1, 8)
    time.sleep(0.1)

    tempDisp.setTemp(-10, 8)
    time.sleep(0.1)

    tempDisp.setTemp(-8, 9)
    time.sleep(0.1)

    tempDisp.setTemp(-18, 120)
    time.sleep(0.1)

    tempDisp.clear()
    
if __name__ == "__main__": 
    try:
        GPIO.setmode(GPIO.BOARD)
        test(tempDisp1)
        test(tempDisp2)
        test(tempDisp3)
    except KeyboardInterrupt: 
        print "key board interrupt!"
        print "clean up GPIO..."
        GPIO.cleanup()
    
    print "clean up GPIO..."
    GPIO.cleanup()
    print "exit..."