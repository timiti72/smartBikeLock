import machine
import onewire
import ds18x20

temp_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(14)))

def read_temps():
    roms = temp_sensor.scan()
    if len(roms) == 0:
        print("No DS18B20 sensor found.")
        
    else:
        temp_sensor.convert_temp()
        for rom in roms:
            temperature = temp_sensor.read_temp(rom)
        return temperature
