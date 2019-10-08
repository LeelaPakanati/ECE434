#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

int keepgoing = 1;    // Set to 0 when ctrl-c is pressed
void signal_handler(int sig);
void signal_handler(int sig)
{
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    unsigned int gpio_dir;
    
    unsigned int GPIO_60 = (1<<7);

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }

    gpio_dir = *gpio_oe_addr;
    gpio_dir &= ~GPIO_60;
    *gpio_oe_addr = gpio_dir;

    printf("Start blinking gpio1_7: P9_4\n");
    while(keepgoing) {
        *gpio_setdataout_addr = GPIO_60;
        usleep(500);
        *gpio_cleardataout_addr = GPIO_60;
        usleep(500);
    }

    munmap((void *)gpio_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
