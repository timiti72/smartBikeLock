from timer import *
from detection.vibration import *
from detection.button import *
import machine

# Constants for touch timings
CLICK_THRESHOLD = 300  # Time in ms for a single click
HOLD_MIN_THRESHOLD = 1000  # Minimum time in ms for a hold
HOLD_MAX_THRESHOLD = 3000  # Maximum time in ms for a hold
MAX_GESTURE_INTERVAL = 500  # Maximum time in ms between gestures

# Touch states
STATE_IDLE = "idle"
STATE_PRESSING = "pressing"
STATE_BUSY = "busy"

# Touch gestures
GESTURE_NONE = "none"
GESTURE_CLICK = "click"
GESTURE_DOUBLE_CLICK = "click+click"
GESTURE_CLICK_HOLD = "click+hold"
STATE_COMM_ON = "communication on"
GESTURE_DOUBLE_CLICK_HOLD = "click+click+hold"
GESTURE_BUTTON_DOUBLE_CLICK_HOLD = "button_click+click+hold"

# States
STATE_IDLE = "idle"
STATE_RIDE_ON = "ride on"
STATE_RIDE_OFF = "ride off"
#CURRENT_STATE  = STATE_IDLE

# Other variables
spam_filter = False
touch_state = STATE_IDLE
touch_gesture = GESTURE_NONE
last_detected_gesture = GESTURE_NONE
click_time = 0

touch_pin = machine.Pin(15, machine.Pin.IN)

def scan_touch(CURRENT_STATE):
    global touch_state, touch_gesture, click_time, last_detected_gesture, spam_filter
    
    if touch_state == STATE_IDLE:
        timer_reset()
        click_time = 0
        touch_gesture = GESTURE_NONE
        if touch_pin.value() == 1:
            timer_start()
            touch_state = STATE_PRESSING
        
    if touch_state == STATE_PRESSING:
        if touch_pin.value() == 0:
            click_time = timer_check()
            timer_reset()
            timer_start()
            if click_time < CLICK_THRESHOLD:
                if touch_gesture == GESTURE_NONE and spam_filter == False:
                    touch_gesture = GESTURE_CLICK
                elif touch_gesture == GESTURE_CLICK and spam_filter == False:
                    touch_gesture = GESTURE_DOUBLE_CLICK
                else:
                    spam_filter = True
                    touch_gesture = GESTURE_NONE
                    
            elif HOLD_MIN_THRESHOLD < click_time < HOLD_MAX_THRESHOLD:
                if touch_gesture == GESTURE_CLICK:
                    touch_gesture = GESTURE_CLICK_HOLD
                elif touch_gesture == GESTURE_DOUBLE_CLICK:
                    touch_gesture = GESTURE_DOUBLE_CLICK_HOLD
                    if is_button_pressed() == True:
                        touch_gesture = GESTURE_BUTTON_DOUBLE_CLICK_HOLD
            elif click_time > HOLD_MAX_THRESHOLD:
                touch_gesture = GESTURE_NONE
                touch_state = STATE_IDLE
            touch_state = STATE_BUSY
        
    if touch_state == STATE_BUSY:
        while timer_check() < MAX_GESTURE_INTERVAL:
            if touch_pin.value() == 1:
                timer_reset()
                touch_state = STATE_PRESSING
                timer_start()
                break 
        if touch_state != STATE_PRESSING:
            last_detected_gesture = touch_gesture
            print(last_detected_gesture)
            
            if touch_gesture == GESTURE_NONE:
                spam_filter = False
                
            elif touch_gesture == GESTURE_CLICK and CURRENT_STATE == STATE_IDLE or CURRENT_STATE == STATE_COMM_ON or CURRENT_STATE == STATE_RIDE_ON:
                vibrate_click()
                
            elif touch_gesture == GESTURE_DOUBLE_CLICK and CURRENT_STATE == STATE_RIDE_ON:
                vibrate_double_click()

            elif touch_gesture == GESTURE_CLICK_HOLD and CURRENT_STATE == STATE_RIDE_ON:
                vibrate_click_hold()

            elif touch_gesture == GESTURE_DOUBLE_CLICK_HOLD and CURRENT_STATE == STATE_IDLE or CURRENT_STATE == STATE_COMM_ON:
                vibrate_double_click_hold()

            elif touch_gesture == GESTURE_BUTTON_DOUBLE_CLICK_HOLD and CURRENT_STATE == STATE_IDLE:
                vibrate_button_double_click_hold()

            touch_state = STATE_IDLE
            touch_gesture = GESTURE_NONE