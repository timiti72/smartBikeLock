import machine
from timer import *

button_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

def button_pressed_with_timeout(timeout):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < timeout:
        if button_pin.value() == 0:
            return True
        timer_elapsed(10)
    return False

def is_button_pressed():
    return button_pin.value() == 1