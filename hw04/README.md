# HW04

## Memory Map
| AM335X      | Memory Map     |
|-------------|----------------|
| 0x4000_0000 | Boot ROM       |
| 0x402F_0400 | SRAM Internal  |
| 0x4740_1000 | USB0           |
| 0x8000_0000 | EMIF0 SDRAM    |
| 0x44E0_7000 | GPIO0          |
| 0x44E0_9000 | UART0          |
| 0x44E0_B000 | I2C0           |
| 0x44E0_D000 | ADC            |
| 0x4802_2000 | UART1          |
| 0x4802_4000 | UART2          |
| 0x4802_A000 | I2C1           |
| 0x4804_C000 | GPIO1          |
| 0x4819_C000 | I2C2           |
| 0x481A_6000 | UART3          |
| 0x481A_8000 | UART4          |
| 0x481A_A000 | UART5          |
| 0x481A_C000 | GPIO2          |
| 0x481A_E000 | GPIO3          |
| 0x4830_E000 | LCD Controller |

## MMAP

### gpioLED:

usage

`./gpioLED`

toggles leds USR2, USR3 by buttons on pins GPIO0_26 and GPIO1_12


### toggleGPIO:

usage

`./toggleGPIO`

toggles pin P9_4 as fast as possible



### Speed of toggling:

The method has a lot less over head than the python or C library or the bash scripts we tested learler. It is able to toggle the LED w/ only a .6ms delay and can acheive a 20ms period at its fastest
