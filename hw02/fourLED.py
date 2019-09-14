#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

btn_pins = ["", "", "", ""]
led_pins = ["", "", "", ""]

def setLED(event):
    GPIO.output(led_pins[btn_pins.index(event.pin)], even.value) 

for i in btn_pins: 
    GPIO.setup(i, INPUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(i, GPIO.BOTH, callback=setLED)
        
for i in led_pins:
    GPIO.setup(i, OUTPUT)
    GPIO.output(i, LOW)

