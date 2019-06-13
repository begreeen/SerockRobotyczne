#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *

import time

light_sensor = ColorSensor(INPUT_1)
touch_sensor = TouchSensor(INPUT_2)
laser_motor = MediumMotor(OUTPUT_A)
flag_motor = LargeMotor(OUTPUT_B)

THRESHOLD = 40

sound = Sound()



def laser_on():
    print("ENABLING LASER!")
    # sound.speak("Enabling laser!")

    laser_motor.on(10)

    while light_sensor.ambient_light_intensity < THRESHOLD:
        pass
    
    laser_motor.off()

    laser_motor.on_for_degrees(10,50)
        

def laser_off():
    print("DISABLING LASER!")
    # sound.speak("Disabling laser!")

    laser_motor.on(-10)

    while light_sensor.ambient_light_intensity > THRESHOLD:
        pass
    
    laser_motor.off()

    laser_motor.on_for_degrees(-10,50)


def flag_high():
    flag_motor.on_for_degrees(30, -180)

def flag_low():
    flag_motor.on_for_degrees(30, 180)


while True:
    
    touch_sensor.wait_for_bump()
    laser_on()
    flag_high()
    print("Waiting for START!")
    sound.speak("Waiting for start!")
    print(light_sensor.ambient_light_intensity)

    while light_sensor.ambient_light_intensity > THRESHOLD:
        pass

    start_time = time.time()
    print("START!")
    sound.speak("Start!")

    time.sleep(5)

    while light_sensor.ambient_light_intensity > THRESHOLD and not touch_sensor.is_pressed:
        pass
    
    
    elapsed_time = time.time()-start_time
    elapsed_time_message = "Your time: {:.2f} seconds".format(elapsed_time)
    print(elapsed_time_message)
    sound.speak(elapsed_time_message)
    laser_off()

    flag_low()

    # poczekaj 2 sekundy pomiedz odczytami
    #time.sleep(2)
