import machine

def light_sleep(button_pin_num, sleep_time):
    button_pin = machine.Pin(button_pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN)
    
    def wake_up_callback(pin):
        print("Woke up from light sleep")
        
    button_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=wake_up_callback)

    print("Going to light sleep. Press the button to wake up...")
    
    if time_until_deep_sleep == -1:
        machine.lightsleep()
    else:
        machine.lightsleep(sleep_time)
    
    print("Woke up from light sleep")
    

