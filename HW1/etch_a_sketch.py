#!/usr/bin/env python3
import argparse
import curses

def main():
    parser = argparse.ArgumentParser(description='Etch A Sketch configuration parser')
    parser.add_argument('x_dim', type=int, help='The x dimension of the Etch-A-Sketch')
    parser.add_argument('y_dim', type=int, help='The x dimension of the Etch-A-Sketch')
    args = parser.parse_args()

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    stdscr.addstr(0,0, "Welcom to Etch-A-Sketch | Contols:\n\tW-A-S-D to move cursor\n\tSpacebar to toggle draw\n\tr to clear the screen\n\tq to quit\n\t")
    intro_len = 5
    
    x_axis = "  "
    for i in range(args.x_dim):
        x_axis = x_axis + " " + str(i)
    stdscr.addstr(intro_len+1, 0, x_axis, curses.A_BOLD)
    
    for i in range(args.y_dim):
        stdscr.addstr(intro_len+2+i, 0, str(i)+':', curses.A_BOLD) 

    origin = map_coords(0,0)
    stdscr.addstr(origin[0], origin[1], 'X', curses.A_BLINK) 
    curpos = (0,0)
    stdscr.refresh()
    
    draw_mode = False
    while True:
        c = stdscr.getkey()
        if c == 'q':
            break

    curses.nocbreak()
    curses.echo()
    curses.endwin()

def map_coords(x, y, introlen=5):
    real_x = 3 + 2 * x
    real_y = introlen+ 2 + 2 * y
    return (real_x, real_y)

if __name__ == '__main__':
    main()
