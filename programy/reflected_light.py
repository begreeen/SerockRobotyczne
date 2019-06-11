#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *

import time

# tworzymy obiekt czujnika swiatla - tutaj podlaczony do wejscia 4
light_sensor = ColorSensor(INPUT_4)

# nieskonczona petla while
while True:
    # odczytaj wartosc i zapisz do zmiennej light_value
    light_value = light_sensor.reflected_light_intensity

    # wyswietl na teminalu zmienna light value
    print(light_value)

    # poczekaj 2 sekundy pomiedz odczytami
    time.sleep(2)

