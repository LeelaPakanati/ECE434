#!/usr/bin/env python3
import curses
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1
import smbus
from time import sleep
from math import pow

RIGHT_PIN = "P8_14"
UP_PIN = "P8_12"
LEFT_PIN = "P8_16"
CLEAR_PIN = "P8_10"
DOWN_PIN = "P8_18"

matrix = 0x70
bus = smbus.SMBus(2)
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)
matrix_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

GPIO.setup(UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(CLEAR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

myEncoder = RotaryEncoder(eQEP1)
myEncoder.setAbsolute()
myEncoder.enable()

x_dim = 8
y_dim = 8

bus.write_i2c_block_data(matrix, 0, matrix_data)
currx = 0
curry = 7
matrix_data[curry*2] |= int(pow(2, currx))

def update(xory, dir):
    global currx
    global curry
    global matrix_data
    matrix_data[curry*2] &= ~int(pow(2, currx))   #turn off current cursor
    matrix_data[curry*2+1] |= int(pow(2, currx))  #turn on red at curr pos
    if xory == 'x':
        currx += dir
    elif xory == 'y':
        curry += dir
    matrix_data[curry*2+1] &= ~int(pow(2, currx))   #turn off old turnt
    matrix_data[curry*2] |= int(pow(2, currx)) #turn on cursor at new current
    write_data()

def write_data():
    global matrix
    global matrix_data
    bus.write_i2c_block_data(matrix, 0, matrix_data)

write_data()

def clear(ch):
    global currx
    global curry
    global matrix_data
    matrix_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    currx = 0
    curry = 7
    matrix_data[curry*2] |= int(pow(2, currx))
    write_data()

def move_up(ch):
    global currx
    global curry
    global matrix_data
    print('yeet\n\n\n\n\n\n\n\n\n\n')
    if curry != 0:
        update('y', -1)

def move_down(ch):
    global y_dim
    global currx
    global curry
    global matrix_data
    print('yeet\n\n\n\n\n\n\n\n\n\n')
    if curry != y_dim - 1:
        update('y', 1)

def move_left(ch):
    global currx
    global curry
    global matrix_data
    if currx != 0:
        update('x', -1)

def move_right(ch):
    global x_dim
    global currx
    global curry
    global matrix_data
    if currx != x_dim - 1:
        update('x', 1)

GPIO.add_event_detect(UP_PIN, GPIO.RISING, callback=move_up, bouncetime=3)
GPIO.add_event_detect(DOWN_PIN, GPIO.RISING, callback=move_down, bouncetime=3)
GPIO.add_event_detect(LEFT_PIN, GPIO.RISING, callback=move_left, bouncetime=3)
GPIO.add_event_detect(RIGHT_PIN, GPIO.RISING, callback=move_right, bouncetime=3)
GPIO.add_event_detect(CLEAR_PIN, GPIO.RISING, callback=clear, bouncetime=3)

while True:
    print(currx, " : ", curry)
    sleep(.1)
