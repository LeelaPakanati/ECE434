#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

btn_pins = ["P9_11", "P9_13", "P9_21", "P9_17"]
led_pins = ["P9_12", "P9_14", "P9_16", "P9_18"]

def setLED(btn_pin):
    print("Toggling on led : ", str(btn_pins.index(btn_pin)))
    GPIO.output(led_pins[btn_pins.index(btn_pin)], GPIO.input(btn_pin))

for i in led_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

for i in range(len(btn_pins)): 
    GPIO.setup(btn_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(btn_pins[i], GPIO.BOTH, callback=setLED)
        
while(True):
    pass

