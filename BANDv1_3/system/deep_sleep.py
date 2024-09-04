import machine

def deep_sleep_with_button(button_pin_num):

    button_pin = machine.Pin(button_pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN)
    
    button_pin.irq(trigger=machine.Pin.IRQ_RISING, wake=machine.DEEPSLEEP)
    
    print("Going to deep sleep. Press the button to wake up...")
    
    machine.deepsleep()
