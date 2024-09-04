import machine
from timer import *

transistor_pin = machine.Pin(21, machine.Pin.OUT)

def activate_solenoid():
    transistor_pin.on()

def deactivate_solenoid():
    transistor_pin.off()

