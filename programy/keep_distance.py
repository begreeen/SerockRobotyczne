#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *
from comm import *

import time

P = 10

distance_sensor = UltrasonicSensor(INPUT_2)
motors = MoveTank(OUTPUT_A, OUTPUT_D)

comm = Communication('192.168.43.247', 6340)

setpoint = 30

while True:
    distance = distance_sensor.distance_centimeters
    error = distance - setpoint

    power = P * error

    if power > 100:
        power = 100
    if power < -100:
        power = -100

    motors.on(power, power)

    comm.send(error, 'error')
    comm.send(power, 'power')

    #time.sleep(0.001)

