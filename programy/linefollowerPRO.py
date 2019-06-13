#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.led import *
from ev3dev2.sound import *
import time
import sys
import select

# tworzymy obiekt czujnika swiatla - tutaj podlaczony do wejscia 4
sensors = [ColorSensor(INPUT_1), ColorSensor(INPUT_2), ColorSensor(INPUT_3), ColorSensor(INPUT_4)]

motor_tank = MoveTank(OUTPUT_A, OUTPUT_D)

last_error = 0
suma = 0

speed = 25
Kp = 0.2
Ki = 0
Kd = 0

while True:
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        try:
            s = line.split()
            if s[0] == 's':
                speed = float(s[1])
            if s[0] == 'p':
                Kp = float(s[1])
            if s[0] == 'i':
                Ki = float(s[1])
            if s[0] == 'd':
                Kd = float(s[1])
            if s[0] == 'q':
                motor_tank.off()
                break
        except:
            pass
        print("AAAAAAAAAAAAAA", line)
        

    light_values = [i.reflected_light_intensity for i in sensors]
    maxi = max(light_values)
    mini = min(light_values)

    if maxi == 0 or mini == maxi:
        motor_tank.off()
        print("ZERO!!!")
        continue
    
    normed = [i - mini for i in light_values]
    maxi = max(normed)
    if maxi == 0:
        print(light_values, in_sight, normed, end=' ')
    normed = [1 - i/maxi for i in normed]


    in_sight_threshold = 0.5
    in_sight = [i < in_sight_threshold for i in normed]

    normed = [i/sum(normed) for i in normed]
    
    print(light_values, in_sight, normed, end=' ')

    position = normed[0] * (-100) + normed[1] * (-50) + normed[2] * (50) + normed[3] * (100)

    print(position)
    # if sum([int(i) for i in in_sight]) == 1:
    #     if in_sight[0]:
    #         position =

    

    


    error = position

    

    suma = 0.99*suma + error
    diff = error - last_error
    
    turn = Kp * error + Ki * suma + Kd * diff 

    motor_tank.on(speed + turn, speed - turn)

    time.sleep(0.01)
    last_error = error
