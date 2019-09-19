#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

def read_temp(ch):
    while GPIO.input(alert_pin):
        temp = bus.read_byte_data(address, 0)
        print(str(temp) + "C", end="/r")
        time.sleep(0.25)

bus = smbus.SMBus(2)
address = 0x48
alert_pin = 'P9_12'
bus.write_byte_data(address, 3, 27)
bus.write_byte_data(address, 2, 26)
GPIO.setup(alert_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(alert_pin, GPIO.RISING, callback=read_temp)

while
    pass
