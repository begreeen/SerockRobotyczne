#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *

import time

# wyświetl tekst na terminalu
print("Zaczynamy zabawe!")

# silniki podłączone do wyjścia A oraz B
motor_tank = MoveTank(OUTPUT_A, OUTPUT_B)

# wlacz silnik A na moc 50%, silnik B na 50%
motor_tank.on(50, 50)

time.sleep(2)

# wylacz silniki
motor_tank.off()

print("Koniec programu!")