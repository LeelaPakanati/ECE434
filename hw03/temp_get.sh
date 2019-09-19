#!/bin/bash

config-pin -i P9_21
config-pin -i P9_22
config-pin P9_21 i2c
config-pin P9_22 i2c

temp0=$(i2cget -y 2 0x48 00)
temp0f=$(($temp * 9 / 5 +32))
temp1=$(i2cget -y 2 0x49 00)
temp1f=$(($temp * 9 / 5 +32))

echo "Sensor0: " $temp0f " | Sensor1: " $temp1f
