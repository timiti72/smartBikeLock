import machine
from timer import*

vibration_pin = machine.Pin(16, machine.Pin.OUT)

def vibrate(n):
    vibration_pin.on()
    timer_elapsed(n)
    vibration_pin.off()

def vibrate_on():
    vibration_pin.on()
    
def vibrate_off():
    vibration_pin.off()
    
def vibrate_click():
    vibrate(200)
    
def vibrate_double_click():
    vibrate(200)
    timer_elapsed(100)
    vibrate(200)
    
def vibrate_click_hold():
    vibrate(200)
    timer_elapsed(100)
    vibrate(500)

def vibrate_double_click_hold():
    vibrate(200)
    timer_elapsed(100)
    vibrate(200)
    timer_elapsed(100)
    vibrate(500)

def vibrate_button_double_click_hold():
    vibrate(500)
    timer_elapsed(100)
    vibrate(500)
    timer_elapsed(100)
    vibrate(500)
    timer_elapsed(100)
    vibrate(500)
