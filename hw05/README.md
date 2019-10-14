# HW05

## Make  
### Part A  
1. target = app.o  
2. Dependency = app.c  
3. Command = compiler and assemble but do not link  

Makefile made from excercise in ./make/  

## Installing kernel Source  
I installed the kernel 4.19 using the tutorial

## Cross Compile

output on host  
```bash
Hello, World! Main is executing at 0x55a07d8d86aa  
This address (0x7ffca7e38980) is in our stack frame  
This address (0x55a07dad9018) is in our bss section  
This address (0x55a07dad9010) is in our data section  
```

output on bone  
```bash
Hello, World! Main is executing at 0x44a5ad  
This address (0xbec25b78) is in our stack frame  
This address (0x45b010) is in our bss section  
This lddress (0x45b008) is in our data section  
```

## Kernel Modules  
File Structure:
```
.
├── part1
│   ├── hello.c
│   └── Makefile
├── part2
│   ├── 99-ebbchar.rules
│   ├── ebbchar.c
│   ├── Makefile
│   └── testebbchar.c
└── part3
    ├── gpio_test.c
    └── Makefile
```

### part 1:  
Passing parameters to the kernel module will print w/ the inputs  
This is the Minimal Device Driver  
```bash
make  
sudo insmod hello.ko  
sudo rmmod hello.ko  
dmesg -H | tail-2  
```

### part 2:  
This will take input from the user for module configuration  
This is the aCharacterDevice  
```bash
make
sudo insmod ebbchar.ko
dmesg -H | tail -5
./test
dmesg -H | tail -10
```

### part 3:  
These commands will show that the module is working  
This is the KernelGPIO  
```bash
make
sudo insmod gpio_test.ko
tail -f /var/log/kern.log
```

## Prof. Yoder's comments

Looks good. 

Grade:  10/10