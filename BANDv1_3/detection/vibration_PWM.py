import machine
from timer import*
"""
PWM control of the vibration motor:
-if intensity_step = 100 then the time_interval determines
the length of a vibration at 100%
-if the intensity_step is 100 the minimum time_interval should be 130
to achieve 100% vibration intensity
"""
vib_pin = machine.Pin(16, machine.Pin.OUT)
vibrate = machine.PWM(vib_pin)

vibrate.freq(1000)

def set_vib_intensity(vib_intensity_percentage):
    vib_intensity = int(vib_intensity_percentage/100*1023)
    vibrate.duty_u16(vib_intensity*64)
    
set_vib_intensity(0)

def pulse_vibration(time_interval, intensity_step):

    for i in range(0, 101, intensity_step):
        set_vib_intensity(i)
        timer_elapsed(time_interval)
        
    for i in range(100, -1, intensity_step*-1):
        set_vib_intensity(i)
        timer_elapsed(time_interval)
