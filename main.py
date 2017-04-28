#!/usr/bin/env python3
from ev3dev import ev3
from ev3dev import core
import time
import sys
import reset

us = core.UltrasonicSensor('in1')
rm = ev3.LargeMotor('outA')
lm = ev3.LargeMotor('outB')



try:
    while True:

        print("forward!")

        rm.run_forever(speed_sp=200)
        lm.run_forever(speed_sp=200)

        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
        while us.distance_centimeters > 10:
            time.sleep(0.2)

        time.sleep(1)

        print("backwards!")

        rm.run_forever(speed_sp=-200)
        lm.run_forever(speed_sp=-200)

        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)
        while us.distance_centimeters < 30:
           time.sleep(0.2)
         
        time.sleep(1)
        reset.reset_walled()
        print("again!")

except:
    reset.reset_walled()

    print("Aww shit")
    print(sys.exc_info())


