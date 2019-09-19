#!/usr/bin/env python3
import curses
import Adafruit_BBIO.GPIO as GPIO
import smbus
from time import sleep
from math import pow

UP_PIN = "P8_10"
DOWN_PIN = "P8_8"
LEFT_PIN = "P8_12"
RIGHT_PIN = "P8_6"
CLEAR_PIN = "P8_4"

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

x_dim = 8
y_dim = 8

bus.write_i2c_block_data(matrix, 0, matrix_data)
(currx, curry) = (7,0)
matrix_data[curry*2] |= pow(2, currx)

def write_data():
    bus.write_i2c_block_data(matrix, 0, matrix_data)

write_data()

def clear(ch):
    matrix_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    write_data()

def move_up(ch):
    if curry != 0:
        matrix_data[curry*2] ^= pow(2, currx)   #turn off current cursor
        matrix_data[curry*2+1] |= pow(2, currx)  #turn on red at curr pos
        curry += 1
        matrix_data[curry*2] |= pow(2, currx) #turn on cursor at new current
        bus.write_i2c_block_data(matrix, 0, matrix_data)
    write_data()

def move_down(ch):
    if curry != y_dim - 1:
        matrix_data[curry*2] ^= pow(2, currx)   #turn off current cursor
        matrix_data[curry*2+1] |= pow(2, currx)  #turn on red at curr pos
        curry -= 1
        matrix_data[curry*2] |= pow(2, currx) #turn on cursor at new current
        bus.write_i2c_block_data(matrix, 0, matrix_data)
    write_data()

def move_left(ch):
    if currx != 0:
        matrix_data[curry*2] ^= pow(2, currx)   #turn off current cursor
        matrix_data[curry*2+1] |= pow(2, currx)  #turn on red at curr pos
        currx -= 1
        matrix_data[curry*2] |= pow(2, currx) #turn on cursor at new current
        bus.write_i2c_block_data(matrix, 0, matrix_data)
    write_data()

def move_right(ch):
   if currx != x_dim - 1:
        matrix_data[curry*2] ^= pow(2, currx)   #turn off current cursor
        matrix_data[curry*2+1] |= pow(2, currx)  #turn on red at curr pos
        currx += 1
        matrix_data[curry*2] |= pow(2, currx) #turn on cursor at new current
        bus.write_i2c_block_data(matrix, 0, matrix_data)
    write_data()

GPIO.add_event_detect(UP_PIN, GPIO.RISING, callback=move_up)
GPIO.add_event_detect(DOWN_PIN, GPIO.RISING, callback=move_down)
GPIO.add_event_detect(LEFT_PIN, GPIO.RISING, callback=move_left)
GPIO.add_event_detect(RIGHT_PIN, GPIO.RISING, callback=move_right)
GPIO.add_event_detect(CLEAR_PIN, GPIO.RISING, callback=clear)

while True:
    pass
