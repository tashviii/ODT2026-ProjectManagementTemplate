from machine import Pin
import time

switch = Pin(22,Pin.IN,Pin.PULL_UP)

while True:
    if (switch.value()==0):
        print ("yay")
    