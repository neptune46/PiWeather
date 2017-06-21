import RPi.GPIO as GPIO
import time

CLK = 11
DIO = 12

class TM1637:
    __clk = 0
    __dio = 0
    __brightness = 4
    __point_on = False
    __display_data = ['8', '8', '8', '8']
    
    def __init__(self, clk, dio, brightness=4):
        self.__clk = clk
        self.__dio = dio
        self.__brightness = brightness

        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.__clk, GPIO.OUT)
        GPIO.setup(self.__dio, GPIO.OUT)

    def delay_ms(self):
        time.sleep(0.001)
    
    def i2c_start(self):
        GPIO.output(self.__clk, GPIO.HIGH)
        GPIO.output(self.__dio, GPIO.HIGH)
        self.delay_ms()
        GPIO.output(self.__dio, GPIO.LOW)
        self.delay_ms()
    
    def i2c_stop(self):
        GPIO.output(self.__clk, GPIO.LOW)
        self.delay_ms()
        GPIO.output(self.__dio, GPIO.LOW)
        self.delay_ms()
        GPIO.output(self.__clk, GPIO.HIGH)
        self.delay_ms()
        GPIO.output(self.__dio, GPIO.HIGH)
        self.delay_ms()

    def i2c_ack(self):
        GPIO.output(self.__clk, GPIO.LOW)
        self.delay_ms()
    
        # set data pin as input
        GPIO.setup(self.__dio, GPIO.IN)
        self.delay_ms()
    
        count = 10
        
        # read ack signal
        while GPIO.input(self.__dio) and count:
            self.delay_ms()
            print count
            count = count - 1
        
        GPIO.output(self.__clk, GPIO.HIGH)
        self.delay_ms()
        GPIO.output(self.__clk, GPIO.LOW)
        self.delay_ms()
        
        # set data pin as output
        GPIO.setup(self.__dio, GPIO.OUT)
        self.delay_ms()
    
    def i2c_write_byte(self, data):
        for i in range(8):
            GPIO.output(self.__clk, GPIO.LOW)
            self.delay_ms()
            if data & 0x01:
                GPIO.output(self.__dio, GPIO.HIGH)
            else:
                GPIO.output(self.__dio, GPIO.LOW)
            self.delay_ms()
            data >>= 1
            GPIO.output(self.__clk, GPIO.HIGH)
            self.delay_ms()
            
    def led8_display(self, value):
        # write command1 - set address mode
        self.i2c_start()
        self.i2c_write_byte(0x40) # 0x40 - auto address ; 0x44 - fixed address
        self.i2c_ack()
        self.i2c_stop()
        
        # write command2 - set start address
        self.i2c_start()
        self.i2c_write_byte(0xc0) # address range: 0xc0 ~ 0xc6
        self.i2c_ack()
        
        # write command data
        for i in range(4):
            self.i2c_write_byte(value)
            self.i2c_ack()
        self.i2c_stop()
        
        # write command 3 - control brightness 
        self.i2c_start()
        self.i2c_write_byte(0x88) # set maxium brightness
        self.i2c_ack()
        time.sleep(1)
        self.i2c_stop()

def main():
    led8 = TM1637(CLK, DIO)
    led8.led8_display(0x7f)
    print "press any key to exit...wait for 2 seconds"
    #r = raw_input()
    time.sleep(1)
    
    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
        #GPIO.cleanup()
        
    print "exit..."
    GPIO.cleanup()
