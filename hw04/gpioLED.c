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
    volatile void *gpio0_addr;
    volatile unsigned int *gpio0_datain;
    volatile unsigned int *gpio0_oe_addr;
    volatile unsigned int *gpio0_setdataout_addr;
    volatile unsigned int *gpio0_cleardataout_addr;
    volatile void *gpio1_addr;
    volatile unsigned int *gpio1_datain;
    volatile unsigned int *gpio1_oe_addr;
    volatile unsigned int *gpio1_setdataout_addr;
    volatile unsigned int *gpio1_cleardataout_addr;
    unsigned int gpio0_dir;
    unsigned int gpio1_dir;

    int fd = open("/dev/mem", O_RDWR);

    gpio0_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);
    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio0_oe_addr           = gpio0_addr + GPIO_OE;
    gpio1_oe_addr           = gpio1_addr + GPIO_OE;

    printf("%d", gpio0_addr);
    printf("%d", gpio1_addr);

    if(gpio0_addr == MAP_FAILED) {
        printf("Unable to map GPIO_0\n");
        exit(1);
    }
    if(gpio1_addr == MAP_FAILED) {
        printf("Unable to map GPIO_1\n");
        exit(1);
    }

    gpio0_datain            = gpio0_addr + GPIO_DATAIN;
    gpio0_oe_addr           = gpio0_addr + GPIO_OE;
    gpio0_setdataout_addr   = gpio0_addr + GPIO_SETDATAOUT;
    gpio0_cleardataout_addr = gpio0_addr + GPIO_CLEARDATAOUT;

    gpio1_datain            = gpio1_addr + GPIO_DATAIN;
    gpio1_oe_addr           = gpio1_addr + GPIO_OE;
    gpio1_setdataout_addr   = gpio1_addr + GPIO_SETDATAOUT;
    gpio1_cleardataout_addr = gpio1_addr + GPIO_CLEARDATAOUT;

    gpio0_dir = *gpio0_oe_addr;
    gpio1_dir = *gpio1_oe_addr;
    gpio0_dir &= ~(USR0|USR1|USR2|USR3);
    gpio0_dir |= BTN0; 
    gpio1_dir |= BTN1; 
    *gpio0_oe_addr = gpio0_dir;
    *gpio1_oe_addr = gpio1_dir;
 
    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    while(keepgoing){
        if(*gpio0_datain & BTN0){
            *gpio0_setdataout_addr   |= USR0;
        } else{
            *gpio0_cleardataout_addr  &= ~USR0;
        }
        if(*gpio1_datain & BTN1){
            *gpio1_setdataout_addr   |= USR0;
        } else{
            *gpio1_cleardataout_addr  &= ~USR0;
        }
    }
    munmap((void *)gpio0_addr, GPIO1_SIZE);
    munmap((void *)gpio1_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
