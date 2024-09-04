import machine

button_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

def is_button_pressed():
    return button_pin.value() == 1