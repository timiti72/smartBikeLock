import sensors.pulse
import sensors.temp
import timer

def truncate(number, decimals=1):
    factor = 10.0 ** decimals
    return int(int(number * factor) / factor)


def read_sensors(time_stamp):
    
    data_read = []
    
    if time_stamp == -1:
    
        format_time_stamp = truncate(time_stamp / 1000, 1)
        temperature_int = int(sensors.temp.read_temps())

        data_read.append(0)
        data_read.append(temperature_int)
        data_read.append(0)
    
        return data_read
        
    else: 
        format_time_stamp = truncate(time_stamp / 1000, 1)
    
        time_stamp_int = format_time_stamp
        temperature_int = int(sensors.temp.read_temps())
        pulse_int = sensors.pulse.get_pulse_rate()

        data_read.append(time_stamp_int)
        data_read.append(temperature_int)
        data_read.append(pulse_int)
    
        return data_read

def init_sensors(time_stamp):
    initial_data = []
    
    initial_data = read_sensors(time_stamp)
    
    return initial_data
