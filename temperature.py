import tm1637
import time
import RPi.GPIO as GPIO

CLK1 = 11
DIO1 = 12

CLK2 = 13
DIO2 = 15

CLK3 = 16
DIO3 = 18


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
        
def test(ssd):
    
    tempDisp = TempDisplay(ssd)

    tempDisp.setTemp(21, 30)
    time.sleep(1)

    tempDisp.setTemp(17, 29)
    time.sleep(1)

    tempDisp.setTemp(-5, -2)
    time.sleep(1)

    tempDisp.setTemp(0, 1)
    time.sleep(1)

    tempDisp.setTemp(-1, 8)
    time.sleep(1)

    tempDisp.setTemp(-10, 8)
    time.sleep(1)

    tempDisp.setTemp(-8, 9)
    time.sleep(1)

    tempDisp.setTemp(-18, 120)
    time.sleep(1)
    
if __name__ == "__main__": 
    try:
        ssd1 = tm1637.TM1637(CLK1, DIO1)
        test(ssd1)
        ssd2 = tm1637.TM1637(CLK2, DIO2)
        test(ssd2)
        ssd3 = tm1637.TM1637(CLK3, DIO3)
        test(ssd3)
    except KeyboardInterrupt: 
        print "key board interrupt!"

    print "exit..."