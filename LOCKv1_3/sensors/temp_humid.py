import machine
import bme280_float as bme280
from timer import*

i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))

bme = bme280.BME280(i2c=i2c)

def read_sensor():
    read_values = []
    
    read_values.append(bme.values[0])
    read_values.append(bme.values[1])
    read_values.append(bme.values[2])
    read_values.append(bme.altitude)

    return read_values

