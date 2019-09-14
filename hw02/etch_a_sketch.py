#!/usr/bin/env python3
import argparse
import curses
import Adafruit_BBIO.GPIO as GPIO

UP_PIN = ""
DOWN_PIN = ""
LEFT_PIN = ""
RIGHT_PIN = ""
CLEAR_PIN = ""

GPIO.setup(UP_PIN, GPIO.IN)
GPIO.setup(DOWN_PIN, GPIO.IN)
GPIO.setup(LEFT_PIN, GPIO.IN)
GPIO.setup(RIGHT_PIN, GPIO.IN)
GPIO.setup(CLEAR_PIN, GPIO.IN)

def setup_stage(args, stdscr):
    stdscr.addstr(0,0, "Welcome to Etch-A-Sketch | Contols:\n\tW-A-S-D to move cursor\n\tr to clear the screen\n\tq to quit\n\t")
    intro_len = 4
    
    x_axis = "  "
    for i in range(args.x_dim):
        x_axis = x_axis + " " + str(i)
    stdscr.addstr(intro_len+1, 0, x_axis, curses.A_BOLD)
    
    for i in range(args.y_dim):
        stdscr.addstr(intro_len+2+i, 0, str(i)+':', curses.A_BOLD) 


def main(stdscr):
    parser = argparse.ArgumentParser(description='Etch A Stetch configuration parser')
    parser.add_argument('x_dim', type=int, help='The x dimension of the Etch-A-Sketch')
    parser.add_argument('y_dim', type=int, help='The y dimension of the Etch-A-Sketch')
    args = parser.parse_args()

    curses.curs_set(0)

    setup_stage(args, stdscr)
    (currx, curry) = (0,0)
    (xpos, ypos) = map_coords(currx, curry)
    stdscr.addstr(xpos, ypos, 'X', curses.A_BLINK) 
    stdscr.refresh()


    while True:
        if GPIO.input(CLEAR_PIN):
            stdscr.clear()
            setup_stage(args, stdscr)
            (currx, curry) = (0,0)
            (xpos, ypos) = map_coords(currx, curry)
            stdscr.addstr(xpos, ypos, 'X', curses.A_BLINK) 
            stdscr.refresh()

        if GPIO.input(DOWN_PIN):
            stdscr.addstr(xpos, ypos, 'X')
            if curry != args.y_dim - 1:
                curry += 1
            (xpos, ypos) = map_coords(currx, curry)
            stdscr.addstr(xpos, ypos, 'X', curses.A_BLINK) 
            stdscr.refresh()
        if GPIO.input(RIGHT_PIN):
            stdscr.addstr(xpos, ypos, 'X')
            if currx != args.x_dim - 1:
                currx += 1
            (xpos, ypos) = map_coords(currx, curry)
            stdscr.addstr(xpos, ypos, 'X', curses.A_BLINK) 
            stdscr.refresh()
        if GPIO.input(UP_PIN):
            stdscr.addstr(xpos, ypos, 'X')
            if curry != 0:
                curry -= 1
            (xpos, ypos) = map_coords(currx, curry)
            stdscr.addstr(xpos, ypos, 'X', curses.A_BLINK) 
            stdscr.refresh()
        if GPIO.input(LEFT_PIN):
            stdscr.addstr(xpos, ypos, 'X')
            if currx != 0:
                currx -= 1
            (xpos, ypos) = map_coords(currx, curry)
            stdscr.addstr(xpos, ypos, 'X', curses.A_BLINK) 
            stdscr.refresh()

def map_coords(x, y, intro_len=4):
    real_x = intro_len + 2 + y
    real_y = 3 + 2 * x
    return (real_x, real_y)

curses.wrapper(main)
