#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *

import time

# tworzymy obiekt czujnika swiatla - tutaj podlaczony do wejscia 4
light_sensor = ColorSensor(INPUT_4)

# silniki podłączone do wyjścia A oraz B
motor_tank = MoveTank(OUTPUT_A, OUTPUT_B)


# nieskonczona petla while
while True:
    # odczytaj wartosc i zapisz do zmiennej light_value
    light_value = light_sensor.reflected_light_intensity

    # jeden silnik w jedną strone - drugi w druga strone!
    motor_tank.on(light_value, -light_value)

    # poczekaj 0.5 sekundy pomiedzy odczytami
    time.sleep(0.5)
