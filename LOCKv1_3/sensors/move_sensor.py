from machine import Pin, I2C
from mpu6050 import init_mpu6050, get_mpu6050_data
import timer
 
i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=400000)

init_mpu6050(i2c)
 
def read_values():
    return get_mpu6050_data(i2c)

def sensor_calibration(samples_no):
    
    calibration_values = []

    for i in range (0, samples_no, 1):
        calibration_values.append(read_values())
        timer.timer_elapsed(10)

        # Calculate average values for calibration
    avg_temp = sum([data['temp'] for data in calibration_values]) / samples_no
    avg_accel_x = sum([data['accel']['x'] for data in calibration_values]) / samples_no
    avg_accel_y = sum([data['accel']['y'] for data in calibration_values]) / samples_no
    avg_accel_z = sum([data['accel']['z'] for data in calibration_values]) / samples_no
    avg_gyro_x = sum([data['gyro']['x'] for data in calibration_values]) / samples_no
    avg_gyro_y = sum([data['gyro']['y'] for data in calibration_values]) / samples_no
    avg_gyro_z = sum([data['gyro']['z'] for data in calibration_values]) / samples_no
        
        # Calculate calibration offsets
    calibration_offset = {
        'temp': avg_temp,
        'accel': {
            'x': avg_accel_x,
            'y': avg_accel_y,
            'z': avg_accel_z,
        },
        'gyro': {
            'x': avg_gyro_x,
            'y': avg_gyro_y,
            'z': avg_gyro_z,
        }
    }
    
    return calibration_offset

def read_values_calibrated(calibration_offset):
    
    sensor_data = read_values()  # Read current sensor values
    
    # Subtract calibration offsets from raw sensor data
    calibrated_data = {
        'temp': sensor_data['temp'] - 2.3,
        'accel': {
            'x': sensor_data['accel']['x'] - calibration_offset['accel']['x'],
            'y': sensor_data['accel']['y'] - calibration_offset['accel']['y'],
            'z': sensor_data['accel']['z'] - calibration_offset['accel']['z'],
        },
        'gyro': {
            'x': sensor_data['gyro']['x'] - calibration_offset['gyro']['x'],
            'y': sensor_data['gyro']['y'] - calibration_offset['gyro']['y'],
            'z': sensor_data['gyro']['z'] - calibration_offset['gyro']['z'],
        }
    }
    
    return calibrated_data

    
    