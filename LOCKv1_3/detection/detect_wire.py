import machine
import timer

input_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
output_pin = machine.Pin(26, machine.Pin.OUT)

def check_wire_connection():
    output_pin.value(1)  # Set output pin high
    timer.timer_elapsed(10)
    connection_status = input_pin.value()  # Read input pin value
    output_pin.value(0)  # Set output pin low to reset the state
    return connection_status == 1
