import machine
from timer import *
# voltage at ADC pin = 2.54V
# voltage after the divider circuit = 2.69
# voltage drop across the transistor 2.69 - 2.54 = 0.15 V

R1 = 5_060 # 5kOhm resistance
R2 = 9_950 # 10kOhm resistance
V_DROP = 0.03 # voltage drop of transistor
FULLY_CHARGED_VOLTAGE = 4.10
FULLY_DISCHARGED_VOLTAGE = 3.4
BATTERY_CAPACITY = 1_500 # mAh
IDLE_CONSUMPTION = 247 # mAh
RIDE_ON_CONSUMPTION = 358 # mAh

adc_pin = machine.ADC(2)
transistor_pin = machine.Pin(22, machine.Pin.OUT)

def get_battery_voltage():
    transistor_pin.value(1)
    timer_elapsed(1000)
    
    adc_value = adc_pin.read_u16()
    #print("adc_value: ", adc_value)
    
    transistor_pin.value(0)
    
    adc_voltage = adc_value * (3.3 / 65535)
    #transforming the read value back in Volts
    
    battery_voltage = (adc_voltage + 0.11) * ((R1 + R2) / R2) + V_DROP
    #calculate the battery voltage based on the voltage divider formula
    
    return battery_voltage
    
def get_battery_percentage(voltage):
    #print(voltage)
    if voltage > FULLY_CHARGED_VOLTAGE:
        return 100
    if voltage < FULLY_DISCHARGED_VOLTAGE:
        return 0
    return (voltage - FULLY_DISCHARGED_VOLTAGE) / (FULLY_CHARGED_VOLTAGE - FULLY_DISCHARGED_VOLTAGE) * 100
    

def calculate_running_time(battery_percentage, battery_capacity_mAh, average_current_consumption_mA):
    # Calculate estimated running time in hours
    running_time_hours = (battery_percentage / 100.0) * (battery_capacity_mAh / average_current_consumption_mA)
    return running_time_hours