import machine
import system.deep_sleep

def light_sleep(button_pin_num, time_until_deep_sleep):
    button_pin = machine.Pin(button_pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN)
    
    def wake_up_callback(pin):
        print("Woke up from light sleep")
        
    button_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=wake_up_callback)

    print("Going to light sleep. Press the button to wake up...")
    
    if time_until_deep_sleep == -1:
        machine.lightsleep()
    else:
        machine.lightsleep(time_until_deep_sleep)
    
    print("Woke up from light sleep - going to deep sleep")
    
    system.deep_sleep.deep_sleep_with_button(button_pin_num)
