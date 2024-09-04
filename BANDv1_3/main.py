#import machine
import time

import system.light_sleep
import detection.touch
import detection.lora_code
import detection.display
import timer
import detection.vibration
import detection.ble_simple_central
import detection.ble_simple_peripheral
import sensors.sensors
import misc.file
import misc.file_merging

from detection.battery import get_battery_voltage, FULLY_DISCHARGED_VOLTAGE, FULLY_CHARGED_VOLTAGE

"""
    ArmBand states:

idle - all sensors are off except for LoRa ,which is in receiver mode, and the button&touch (this state is also used while charging the device)
rideOn - triggered by it's gesture, unlocks LPM/HPM gesture recognition; all sensors are active
rideOff - a signaling that the ride is ended right after which, the state becomes IDLE
commOn - activates while there is a bluetooth connection between the device and the Smartphone; used for sending ride data
commOff - a signaling state in which the data stored on the device is deleted; shortly after the state becomes IDLE

    Gesture functionality (gesture detection only in: idle, rideOn, rideOff):
    
DOUBLE_CLICK_HOLD: starts ride (if ride is not started and in idle state)
CLICK_HOLD: stops ride (if ride is started)
CLICK_CLICK: (while ride is on) if in LPM goes to HPM and vice versa
CLICK: shows info on the display
BUTTON_CLICK + DOUBLE_CLICK_HOLD: sends signal to unlock the bike lock

    At 0.5 seconds interval, the storage lasts for approximately **15.4 hours**.
    At 2 seconds interval, the storage lasts for approximately **61.7 hours** (or about 2.6 days).
    At 5 seconds interval, the storage lasts for approximately **154.3 hours** (or about 6.4 days).

"""
STATE_SOLENOID_OPEN = "solenoid is open"
STATE_SOLENOID_CLOSE = "solenoid is closed"
STATE_ALARM = "alarm_triggered"
STATE_IDLE = "idle"
STATE_RIDE_ON = "ride on"
STATE_RIDE_OFF = "ride off"
STATE_COMM_ON = "communication on"
STATE_COMM_OFF = "communication off"
STATE_COMM_CANCELLED = "file transfer cancelled"
STATE_COMM_FAILED = "file transfer failed"
STATE_COMM_DONE = "file transfer done"
RIDE_FILE = "sensors/ride.txt"
CFG_FILE = "detection/cfg.txt"
RIDE_RECEIVED_FILE = "sensors/ride_rec.txt"

#SLEEP_TIME = 0
#LIGHT_SLEEP_TIME = 300_000 # enters light sleep after 5 minutes of inactivity
LORA_TIMER = 0
LORA_SENDER_TIME = 750
LORA_RECEIVER_TIME = 1_500
READ_TIME_LPM = 10_000
READ_TIME_HPM = 5_000
last_sensor_read_time = 0
time_stamp_mark = 0
alarm_vibration = 0
alarm_vibration_interval = 500
screen_time_stop = 10_000
screen_time_start = 0
solenoid_time = 0
solenoid_time_interval = 10_000
display_flag = False

CURRENT_STATE = STATE_IDLE
DATA_STATE = True
LPM_STATE = True
time_stamp_flag = False

if not misc.file.file_exists(CFG_FILE):
    misc.file.create_file(CFG_FILE)
    
if not misc.file.file_exists(RIDE_FILE):
    misc.file.create_file(RIDE_FILE)
misc.file.clear_file(RIDE_FILE)

lora = detection.lora_code.initialize_lora()
detection.lora_code.configure_lora(lora)
detection.lora_code.set_receive_callback(lora)

detection.display.start_screen()

print("woke up")

while True:
    
    detection.touch.scan_touch(CURRENT_STATE)
 
    if CURRENT_STATE == STATE_ALARM:
        
        if (alarm_vibration - time.ticks_ms()) % alarm_vibration_interval == 0:
            detection.vibration.vibrate_click()
            detection.display.powerOn()
            detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 1)
            
        detection.vibration.vibrate_off()
        
        if detection.touch.last_detected_gesture == detection.touch.GESTURE_CLICK:
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
            detection.lora_code.toggle_sender_mode(lora, "ALARM_STOP")
            print("ALARM_STOP")
            detection.lora_code.toggle_receiver_mode(lora)
            detection.lora_code.received_message = "NONE"
            CURRENT_STATE = STATE_IDLE
            
        if detection.lora_code.received_message == "ALARM_STOP":
            CURRENT_STATE = STATE_IDLE
            
    if CURRENT_STATE == STATE_IDLE:
        detection.lora_code.toggle_receiver_mode(lora)
        detection.vibration.vibrate_off()
        
        """
        if time.ticks_ms() - SLEEP_TIME >= 20000:

            detection.display.end_screen()
            timer_sleep(1000)
            
            #system.light_sleep.light_sleep(17, 5000)
            machine.lightsleep(5000)

            detection.display.end_screen()
            timer_sleep(1000)
            SLEEP_TIME = 0
         """   
        
        if detection.lora_code.received_message == "ALARM_START":
            alarm_vibration = time.ticks_ms()
            CURRENT_STATE = STATE_ALARM
            detection.lora_code.received_message = "NONE"
        
        if not display_flag:
            detection.display.powerOn()
            SLEEP_TIME = 0
            detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 1)
            screen_time_start = time.ticks_ms()
            display_flag = True
            
        if time.ticks_ms() - screen_time_start >= screen_time_stop:
            detection.display.show_info(False, CURRENT_STATE, None, None, None, 1, 1)
            SLEEP_TIME = time.ticks_ms()
            screen_time_start = 0
            detection.display.powerOff()
        
        if detection.touch.last_detected_gesture == detection.touch.GESTURE_CLICK:
            SLEEP_TIME = 0
            detection.display.powerOn()
            if screen_time_start == 0:
                detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 1)
            screen_time_start = time.ticks_ms()
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
        
        elif detection.touch.last_detected_gesture == detection.touch.GESTURE_DOUBLE_CLICK_HOLD:
            display_flag = False
            print("new state")
            CURRENT_STATE = STATE_RIDE_ON
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, "STATE_RIDE_ON")
            print("State: rideOn, LPM mode (default)")
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
            
        elif detection.touch.last_detected_gesture == detection.touch.GESTURE_BUTTON_DOUBLE_CLICK_HOLD:
            solenoid_time = time.ticks_ms()
            CURRENT_STATE = STATE_IDLE
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, "STATE_SOLENOID")
            
            detection.display.powerOn()
            if screen_time_start == 0:
                detection.display.show_info(True, STATE_SOLENOID_OPEN, None, None, None, 1, 1)
            else:
                detection.display.show_info(True, STATE_SOLENOID_OPEN, None, None, None, 1, 0)
            
            print("State: idle + solenoid activation enabled")
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
            timer.timer_elapsed(100)
            detection.lora_code.toggle_receiver_mode(lora)
            
            while detection.lora_code.received_message != "WIRE_ON":
                if time.ticks_ms() - solenoid_time >= solenoid_time_interval:
                    break
                continue
            print("wire connected - continue")
            detection.display.powerOn()
            detection.display.show_info(True, STATE_SOLENOID_CLOSE, None, None, None, 1, 0)
            detection.lora_code.received_message = "NONE"
            detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 0)
            screen_time_start = time.ticks_ms()
        
        else:
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
    
    if CURRENT_STATE == STATE_RIDE_ON:
        
        if not display_flag:
            sensors_readings = sensors.sensors.init_sensors(-1)
            detection.display.powerOn()
            if screen_time_start == 0:
                detection.display.show_info(True, CURRENT_STATE, str(sensors_readings[2]), int(sensors_readings[0]), str(sensors_readings[1]), 1, 1)
            else:
                detection.display.show_info(True, CURRENT_STATE, str(sensors_readings[2]), int(sensors_readings[0]), str(sensors_readings[1]), 1, 0)
            screen_time_start = time.ticks_ms()
            display_flag = True
            
        if time.ticks_ms() - screen_time_start >= screen_time_stop:
            detection.display.show_info(False, CURRENT_STATE, str(sensors_readings[2]), int(sensors_readings[0]), str(sensors_readings[1]), 1, 1)
            screen_time_start = 0
            detection.display.powerOff()
            
        if detection.touch.last_detected_gesture == detection.touch.GESTURE_CLICK:
            detection.display.powerOn()
            if screen_time_start == 0:
                detection.display.show_info(True, CURRENT_STATE, str(sensors_readings[2]), int(sensors_readings[0]), str(sensors_readings[1]), 0, 1)
            screen_time_start = time.ticks_ms()
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
        
        if detection.touch.last_detected_gesture == detection.touch.GESTURE_CLICK_HOLD:
            CURRENT_STATE = STATE_RIDE_OFF
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, "STATE_RIDE_OFF")
            print("State: rideOff")
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
            
        elif detection.touch.last_detected_gesture == detection.touch.GESTURE_DOUBLE_CLICK:
            LPM_STATE = not LPM_STATE
            mode = "LPM" if LPM_STATE else "HPM"
            print(f"State: ride on, {mode} mode")
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
            
        elif detection.touch.last_detected_gesture == detection.touch.GESTURE_NONE:
            current_time = time.ticks_ms()
            if LPM_STATE and current_time - last_sensor_read_time >= READ_TIME_LPM:
                
                if time_stamp_flag == False:
                    time_stamp_mark = current_time
                    time_stamp_flag = True
                sensors_readings = sensors.sensors.read_sensors(current_time - time_stamp_mark)
                misc.file.write_to_file(RIDE_FILE, str(sensors_readings[0])+ ","+ str(sensors_readings[1])+ ","+ str(sensors_readings[2]))
                misc.file.write_to_file(RIDE_FILE, "\n")
                last_sensor_read_time = current_time
                
            elif not LPM_STATE and current_time - last_sensor_read_time >= READ_TIME_HPM:
                sensors_readings = sensors.sensors.read_sensors(current_time - time_stamp_mark)
                misc.file.write_to_file(RIDE_FILE, str(sensors_readings[0])+ ","+ str(sensors_readings[1])+ ","+ str(sensors_readings[2]))
                misc.file.write_to_file(RIDE_FILE, "\n")
                last_sensor_read_time = current_time
        else:
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
    
    if CURRENT_STATE == STATE_RIDE_OFF:
        
        detection.display.powerOn()
        if screen_time_start == 0:
            detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 1)
        else:
            detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 0)
        detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
        last_sensor_read_time = 0
        time_stamp_flag = False
        display_flag = False
        CURRENT_STATE = STATE_COMM_ON
        
    
    if CURRENT_STATE == STATE_COMM_ON:

        if not display_flag:
            detection.display.powerOn()
            detection.display.show_info(True, CURRENT_STATE, None, None, None, 1, 0)
            screen_time_start = time.ticks_ms()
            display_flag = True
            
        if time.ticks_ms() - screen_time_start >= screen_time_stop:
            detection.display.show_info(False, CURRENT_STATE, None, None, None, 1, 1)
            screen_time_start = 0
            detection.display.powerOff()
        
        if detection.touch.last_detected_gesture == detection.touch.GESTURE_CLICK:
            detection.display.powerOn()
            if screen_time_start == 0:
                detection.display.show_info(True, CURRENT_STATE, None, None, None, 0, 1)
            screen_time_start = time.ticks_ms()
            
        elif detection.touch.last_detected_gesture == detection.touch.GESTURE_CLICK_HOLD:
            display_flag = False
            CURRENT_STATE = STATE_IDLE
            detection.touch.last_detected_gesture = detection.touch.GESTURE_NONE
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, STATE_COMM_OFF)
            detection.display.powerOn()
            if screen_time_start == 0:
                detection.display.show_info(True, STATE_COMM_CANCELLED, None, None, None, 1, 1)
            else:
                detection.display.show_info(True, STATE_COMM_CANCELLED, None, None, None, 1, 0)
            print("File transfer canceled")
        timer.timer_elapsed(3000)
        detection.ble_simple_central.demo()
        CURRENT_STATE = STATE_COMM_OFF
            
    if CURRENT_STATE == STATE_COMM_OFF:
        misc.file_merging.merge_files_by_timestamp('sensors/received_data.txt', 'sensors/ride.txt')
        detection.ble_simple_peripheral.demo()
        CURRENT_STATE = STATE_IDLE
        
    if misc.file.read_file(CFG_FILE) != CURRENT_STATE:
        misc.file.clear_file(CFG_FILE)
        misc.file.write_to_file(CFG_FILE, CURRENT_STATE)