import timer
import sensors.move_sensor
import sensors.temp_humid
import math

def calculate_roll(accel_y, accel_z):
    roll = math.atan2(accel_y, accel_z)
    roll_degrees = math.degrees(roll)
    return roll_degrees

def calculate_pitch(accel_x, accel_z):
    pitch = math.atan2(accel_x, accel_z)
    pitch_degrees = math.degrees(pitch)
    return pitch_degrees

def truncate(number, decimals=1):
    factor = 10.0 ** decimals
    return int(int(number * factor) / factor)


def read_sensors(time_stamp):
    
    data_read = []

    format_time_stamp = truncate(time_stamp / 1000, 1)

    move_sensor_data = sensors.move_sensor.read_values_calibrated(sensors.move_sensor.sensor_calibration(50))
    
    temp_sensor_data = sensors.temp_humid.read_sensor()

    if 'accel' in move_sensor_data:
        roll = calculate_roll(move_sensor_data['accel']['y'], move_sensor_data['accel']['z'])
        pitch = calculate_pitch(move_sensor_data['accel']['x'], move_sensor_data['accel']['z'])
    else:
        roll = 0.0
        pitch = 0.0
    
    #print(type(move_sensor_data['temp']))
    #print(type(pitch))
    
    roll_int = int(float("{:.1f}".format(roll)))
    pitch_int = int(float("{:.1f}".format(pitch)))
    front_accel = move_sensor_data['accel']['y']
    lateral_accel = move_sensor_data['accel']['x']
    
    data_read.append(format_time_stamp)
    data_read.append(temp_sensor_data[0])
    data_read.append(temp_sensor_data[1])
    data_read.append(temp_sensor_data[2])
    data_read.append(temp_sensor_data[3])
    data_read.append(front_accel)
    data_read.append(lateral_accel)
    data_read.append(roll_int)
    data_read.append(pitch_int)
    
    
    return data_read
