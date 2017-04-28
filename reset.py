#!/usr/bin/env python3
from ev3dev import ev3

rm = ev3.LargeMotor('outA')
lm = ev3.LargeMotor('outB')

def reset_walled():
    rm.stop(stop_action='brake')
    lm.stop(stop_action='brake')

    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

if __name__ == "__main__":
    reset_walled()