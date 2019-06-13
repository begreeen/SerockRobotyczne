#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *
from comm import *

import time

light_sensor = ColorSensor(INPUT_4)
number = 0

# adres IP komputera, port komunikacyjny - taki sam ustawiony na komputerze
comm = Communication('192.168.8.100', 6340)

while True:
    light_value = light_sensor.reflected_light_intensity
    number = number + 1

    comm.send(light_value, 'swiatlo-1')
    comm.send(number, 'number-1')
    
    time.sleep(1)
