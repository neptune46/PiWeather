import tm1637
import time
import RPi.GPIO as GPIO

CLK = 11
DIO = 12

# 4 digits Seven-Segment-Display for Mininum/Maximum temperature (-9~99)

class TempDisplay:
    __temp_min = 0
    __temp_max = 0
    
    def __init__(self, ssd):
        self.__ssd = ssd
        
    def setTemp(self, min, max):
        self.__temp_min = min
        self.__temp_max = max
        
    def show(self):
        self.__ssd.display_digit(['0', '1', '2', '3'])
        
def test():
    ssd = tm1637.TM1637(CLK, DIO)
    temp = TempDisplay(ssd)
    temp.setTemp(21, 30)
    temp.show()
    
if __name__ == "__main__": 
    try:
        test()
    except KeyboardInterrupt: 
        print "key board interrupt!"

    print "exit..."