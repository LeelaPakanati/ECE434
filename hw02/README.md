# HW 02

fourLED.py runs the four buttons with four leds using interupts. Pins can be seen in the two arrays used for btn_pins and led_pins


togglegpio.sh is the modified shell script for toggling gpio

togglegpio.py is the modified python script for toggling gpio

togglegpio.c is the modified c program for toggling gpio: it is modified to take in gpio number, either 1 arg for onOfftime or a 2 args for onTime and offTime; it also handles C-c exitting properly with the signal handler


etch_a_sketch.py is the python script for running etch-a-sketch with two input args: xdim and ydim

the pinouts for etch_a_sketch are also available in the top of of the code

