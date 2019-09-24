#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
import os

os.system("config-pin P9_21 i2c") 
os.system("config-pin P9_22 i2c") 
bus = smbus.SMBus(2)
address = 0x48
alert_pin = 'P9_12'
bus.write_byte_data(address, 3, 28)
bus.write_byte_data(address, 2, 27)
bus.write_byte_data(address, 1, 4)

def read_temp(ch):
    print("Alert Triggered")
    while GPIO.input(alert_pin):
        temp = bus.read_byte_data(address, 0)
        print(str(temp) + "C\r", end="")
        time.sleep(0.25)
    print("\r\nAlert Restored")

GPIO.setup(alert_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(alert_pin, GPIO.RISING, callback=read_temp)

while True:
#    print(GPIO.input(alert_pin), ":", bus.read_byte_data(address,0))
    pass
