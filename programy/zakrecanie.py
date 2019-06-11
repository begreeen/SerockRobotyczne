#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *

import time

# silniki podłączone do wyjścia A oraz B
motor_tank = MoveTank(OUTPUT_A, OUTPUT_B)

# wyświetl tekst na terminalu
print("Zakrecamy w jedna strone!")

# zakrecamy w jedna strone - jeden silnik na 10%, drugi na 90% mocy
motor_tank.on(10, 90)

# poczekaj 2 sekundy, a nastepnie wylacz silniki
time.sleep(2)
motor_tank.off()


time.sleep(5)

# wyświetl tekst na terminalu
print("Zakrecamy w druga strone!")

# zakrecamy w druga strone - jeden silnik na 90%, drugi na 10% mocy
motor_tank.on(90, 10)
time.sleep(2)
motor_tank.off()

print("Koniec programu!")