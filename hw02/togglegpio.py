#!/usr/bin/env python3
import argparse
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

parser = argparse.ArgumentParser(description='Toggle GPIO')
parser.add_argument('pin') 
parser.add_argument('period', type=float)
args = parser.parse_args()

print(args.pin)
GPIO.setup(args.pin, GPIO.OUT)

while True:
     GPIO.output(args.pin, GPIO.HIGH)
     sleep(args.period/2)
     GPIO.output(args.pin, GPIO.LOW)
     sleep(args.period/2)
