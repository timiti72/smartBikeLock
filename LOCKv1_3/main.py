import machine
import time

import detection.lora_code
import timer
import detection.solenoid
import detection.button
import detection.detect_wire
import sensors.sensors
import misc.file
import detection.ble_simple_peripheral
detection.solenoid.deactivate_solenoid()

STATE_UNLOCK = "bike lock unlocked"
STATE_ALARM = "alarm triggered"
STATE_IDLE = "idle"
STATE_RIDE_ON = "ride on"
STATE_RIDE_OFF = "ride off"
STATE_COMM_ON = "communication on"
STATE_COMM_OFF = "communication off"
RIDE_FILE = "sensors/ride.txt"

LORA_TIMER = 0
LORA_SENDER_TIME = 750
LORA_RECEIVER_TIME = 1_500
READ_TIME = 5_000
last_sensor_read_time = 0
time_stamp_mark = 0
toggle_alarm = False

misc.file.create_file(RIDE_FILE)
misc.file.clear_file(RIDE_FILE)

CURRENT_STATE = STATE_IDLE
DATA_STATE = True
LPM_STATE = True
time_stamp_flag = False

lora = detection.lora_code.initialize_lora()
detection.lora_code.configure_lora(lora)
detection.lora_code.set_receive_callback(lora)

timer.timer_elapsed(2_000)

while True:
    
    if CURRENT_STATE == STATE_ALARM:
        if toggle_alarm == False:
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, "ALARM_START")
            detection.lora_code.toggle_receiver_mode(lora)
            toggle_alarm = True
            
        if detection.lora_code.received_message == "ALARM_STOP":
            detection.lora_code.received_message = "NONE"
        
        if detection.detect_wire.check_wire_connection() == True:
            print("Wire OK")
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, "ALARM_STOP")
            print("ALARM_STOP")
            CURRENT_STATE = STATE_IDLE
            toggle_alarm = False
    
    if CURRENT_STATE == STATE_IDLE:
        detection.lora_code.toggle_receiver_mode(lora)
        
        if detection.detect_wire.check_wire_connection() == False:
            print("Wire NOT OK")
            CURRENT_STATE = STATE_ALARM
        
        elif detection.lora_code.received_message == "STATE_RIDE_ON":
            time_stamp_init = time.ticks_ms()
            CURRENT_STATE = STATE_RIDE_ON
            detection.lora_code.received_message = "NONE"
            
        elif detection.lora_code.received_message == "STATE_SOLENOID":
            activation_window = time.ticks_ms()
            print("Solenoid activation")
            while time.ticks_ms() - activation_window < 10_000:
                if detection.button.is_button_pressed() == True:
                    detection.solenoid.activate_solenoid()
                
            detection.solenoid.deactivate_solenoid()
            
            while not detection.detect_wire.check_wire_connection():
                continue
            timer.timer_elapsed(100)
            detection.lora_code.toggle_sender_mode(lora, "WIRE_ON")
            print("wire OK - continue")
            CURRENT_STATE = STATE_IDLE
                
            detection.lora_code.received_message = "NONE"

    if CURRENT_STATE == STATE_RIDE_ON:
        detection.lora_code.toggle_receiver_mode(lora)
        
        time_stamp = time.ticks_ms() - time_stamp_init
        
        if time_stamp % READ_TIME == 0:
            sensor_readings = sensors.sensors.read_sensors(time_stamp)
            
            misc.file.write_to_file(RIDE_FILE,str(sensor_readings[0])+","+str(sensor_readings[1])+","+str(sensor_readings[2])+","+str(sensor_readings[3])+","+str(sensor_readings[4])+","+str(sensor_readings[5])+","+str(sensor_readings[6])+","+str(sensor_readings[7])+","+str(sensor_readings[8])+"\n")
            
            CURRENT_STATE = STATE_RIDE_ON
            
        if detection.lora_code.received_message == "STATE_RIDE_OFF":
            CURRENT_STATE = STATE_RIDE_OFF
            detection.lora_code.received_message = "NONE"
            
    if CURRENT_STATE == STATE_RIDE_OFF:
        detection.ble_simple_peripheral.demo()
        CURRENT_STATE = STATE_IDLE
            
            
            
            
            
            
            
