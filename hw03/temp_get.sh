#!/bin/bash

config-pin -i P9_21
config-pin -i P9_22
config-pin P9_21 i2c
config-pin P9_22 i2c

temp0f=$(($(i2cget -y 2 0x48 00) * 9 / 5 + 32))
temp1f=$(($(i2cget -y 2 0x49 00) * 9 / 5 + 32))

echo "Sensor0: " $temp0f " | Sensor1: " $temp1f
