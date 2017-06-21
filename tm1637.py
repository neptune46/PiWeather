import RPi.GPIO as GPIO
import time

"""
      A
     ---
  F |   | B
     -G-
  E |   | C
     ---
      D

"""

digital_coding = {
    '0': 0x3f,
    '1': 0x06,
    '2': 0x5b,
    '3': 0x4f,
    '4': 0x66,
    '5': 0x6d,
    '6': 0x7d,
    '7': 0x07,
    '8': 0x7f,
    '9': 0x6f,
    'A': 0x77,
    'a': 0x77,
    'B': 0x7c,
    'b': 0x7c,
    'C': 0x39,
    'c': 0x39,
    'D': 0x5e,
    'd': 0x5e,
    'E': 0x79,
    'e': 0x79,
    'F': 0x71,
    'f': 0x71,
    '-': 0x40
}

class TM1637:
    __clk = 0
    __dio = 0
    __brightness = 4

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

        # read ack signal
        count = 10
        while GPIO.input(self.__dio) and count:
            self.delay_ms()
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
            
    def display_digit(self, value):
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
            code = digital_coding[value[i]]
            self.i2c_write_byte(code)
            self.i2c_ack()
        self.i2c_stop()
        
        # write command 3 - control brightness 
        self.i2c_start()
        self.i2c_write_byte(0x88) # set maxium brightness
        self.i2c_ack()
        time.sleep(1)
        self.i2c_stop()



