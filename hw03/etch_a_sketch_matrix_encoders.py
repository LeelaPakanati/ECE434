#!/usr/bin/env python3
import curses
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2b
import smbus
from time import sleep
from math import pow
import os

os.system("config-pin P9_21 i2c") 
os.system("config-pin P9_22 i2c") 
os.system("config-pin P8_41 qep") 
os.system("config-pin P8_42 qep") 
os.system("config-pin P8_33 qep") 
os.system("config-pin P8_35 qep") 
matrix = 0x70
bus = smbus.SMBus(2)
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)
matrix_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
temp_address = 0x48

yEncoder = RotaryEncoder(eQEP1)
yEncoder.setAbsolute()
yEncoder.enable()
xEncoder = RotaryEncoder(eQEP2b)
xEncoder.setAbsolute()
xEncoder.enable()


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
    if curry != 0:
        update('y', -1)

def move_down(ch):
    global y_dim
    global currx
    global curry
    global matrix_data
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

curr_ency = yEncoder.position
curr_encx = xEncoder.position
while True:
    temp = bus.read_byte_data(temp_address, 0)
    if(temp>26):
        clear(0)
    if yEncoder.position > curr_ency:
        move_up(0)
    elif yEncoder.position < curr_ency:
        move_down(0)
    if xEncoder.position > curr_encx:
        move_right(0)
    elif xEncoder.position < curr_encx:
        move_left(0)
    curr_ency = yEncoder.position
    curr_encx = xEncoder.position
    
