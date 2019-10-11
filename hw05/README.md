# HW05

## Make  
### Part A  
1. target = app.o  
2. Dependency = app.c  
3. Command = compiler and assemble but do not link  

Makefile made from excercise in ./make/  

## Installing kernel Source  
I installed the kernel 4.14 using the tutorial

## Cross Compile

output on host  
Hello, World! Main is executing at 0x55a07d8d86aa  
This address (0x7ffca7e38980) is in our stack frame  
This address (0x55a07dad9018) is in our bss section  
This address (0x55a07dad9010) is in our data section  


output on bone  
Hello, World! Main is executing at 0x44a5ad  
This address (0xbec25b78) is in our stack frame  
This address (0x45b010) is in our bss section  
This lddress (0x45b008) is in our data section  

## Kernel Modules  
File Structure:


### part 1:  

```bash
make  
sudo insmod hello.ko  
sudo rmmod hello.ko  
dmesg -H | tail-2  
```
