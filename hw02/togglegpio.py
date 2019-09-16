#!/usr/bin/env python3
import argparse
import Adafruit_BBGPIO.GPIO as GPIO


def main():
    parser = argparse.ArgumentParser(description='Toggle GPIO')
    parser.add_argument('pin') 
    parser.add_argument('period', type=int)
    args = parser.parse_args()

   GPIO.setup(args.pin, GPIO.OUT)

   toggle = 0
   while True:
        toggle = !toggle
        GPIO.output(args.pin, toggle)
        sleep(args.period/2)
