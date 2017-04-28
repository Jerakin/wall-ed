#!/usr/bin/env python3
from ev3dev import ev3
from ev3dev import core
import time
from enum import Enum
import sys
import reset
import atexit

SPEED = 35

# us = core.UltrasonicSensor('in1')
# rm = ev3.LargeMotor('outA')
# lm = ev3.LargeMotor('outB')
#
# distance = us.distance_centimeters
print()


def get_distance(us):
    try:
        return us.distance_centimeters
    except:
        return 0


def run3():
    us = core.UltrasonicSensor('in1')
    rm = ev3.LargeMotor('outA')
    lm = ev3.LargeMotor('outB')

    set_speed(0, rm, lm)

    rm.run_direct()
    lm.run_direct()

    time.sleep(1)
    start_distance = get_distance(us)
    distance = start_distance

    start_time = time.time()

    set_speed(SPEED, rm, lm)
    while distance > 15:
        distance = get_distance(us)
        print(distance)
        time.sleep(0.05)

    set_speed(0, rm, lm)
    forward_time = time.time() - start_time
    print(forward_time)

    ev3.Sound.speak('Calibrating!').wait()

    set_speed(35, rm)
    set_speed(-35, lm)

    start_time = time.time()
    iterations = 0
    while iterations < 50 or abs(next_distance - distance) > 1:
        next_distance = get_distance(us)
        print(next_distance)
        time.sleep(0.05)
        iterations += 1

    total_time = (time.time() - start_time)
    time.sleep(total_time * 0.03)

    total_time = (time.time() - start_time) * 1.03
    print(total_time)

    set_speed(0, rm, lm)

    ev3.Sound.speak('Calibration done! wubba dubba dub dub!').wait()

    time.sleep(1)

    set_speed(35, rm)
    set_speed(-35, lm)

    turn_time = total_time / 2
    time.sleep(turn_time)
    set_speed(0, rm, lm)

    ev3.Sound.speak('Perfect 180 degree turn motherfucker!').wait()

    set_speed(SPEED, rm, lm)
    time.sleep(forward_time)
    set_speed(0, rm, lm)

    time.sleep(1)

    set_speed(35, rm)
    set_speed(-35, lm)
    time.sleep(turn_time)
    set_speed(0, rm, lm)

    exit()

class Movement(Enum):
    FORWARD = 1
    BACKWARDS = 2


def set_speed(speed=0, *args):
    for m in args:
        m.duty_cycle_sp = speed


def bot_onwards(rm, lm):
    set_speed(-50, rm, lm)
    return Movement.BACKWARDS


def bot_reverse(rm, lm):
    set_speed(50, rm, lm)
    return Movement.FORWARD

def run2():
    print("GO BOT!")
    us = core.UltrasonicSensor('in1')
    rm = ev3.LargeMotor('outA')
    lm = ev3.LargeMotor('outB')
    set_speed(0, rm, lm)

    rm.run_direct()
    lm.run_direct()

    state = bot_onwards(rm, lm)

    while True:
        try:
            distance = us.distance_centimeters
        except:
            distance = 0

        if state == Movement.FORWARD:
            if distance <= 25:
                state = bot_onwards(rm, lm)

        elif state == Movement.BACKWARDS:
            if distance > 50:
                state = bot_reverse(rm, lm)

        print(distance)
        print("again!")
        time.sleep(0.1)


def run():
    us = core.UltrasonicSensor('in1')
    rm = ev3.LargeMotor('outA')
    lm = ev3.LargeMotor('outB')


    rm.duty_cycle_sp = 0
    lm.duty_cycle_sp = 0

    rm.run_direct()
    lm.run_direct()

    while True:
        print("forward!")
        rm.duty_cycle_sp = 50
        lm.duty_cycle_sp = 50

        print("gogogo!")

        #ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        #ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)

        print("gogogo2!")
        while us.distance_centimeters > 25:
            #time.sleep(0.2)
            print(us.distance_centimeters)


        # reset.reset_walled()
        rm.duty_cycle_sp = 0
        lm.duty_cycle_sp = 0
        time.sleep(2)

        #reset.reset_walled()
        print("backwards!")

        #time.sleep(0.1)
        #rm.run_forever(speed_sp=-200)
        #lm.run_forever(speed_sp=-200)
        rm.duty_cycle_sp = -50
        lm.duty_cycle_sp = -50
        # rm.run_direct()
        # lm.run_direct()

        print("gogogo3!")
        #ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
        #   ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)
        print("gogogo4!")
        while us.distance_centimeters < 50:
            print(us.distance_centimeters)

        rm.duty_cycle_sp = 0
        #lm.duty_cycle_sp = 0
        # reset.reset_walled()

        time.sleep(2)
        #reset.reset_walled()
        print("again!")

if __name__ == "__main__":
    atexit.register(reset.reset_walled)
    run3()

