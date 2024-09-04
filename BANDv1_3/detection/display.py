from machine import I2C, ADC
from sh1106 import SH1106_I2C
from detection.battery import *
from timer import *
from misc.bike_animation import *
from misc.draw import *
from misc.wave_animation import *
from misc.lock_animation import *

STATE_SOLENOID_OPEN = "solenoid is open"
STATE_SOLENOID_CLOSE = "solenoid is closed"
STATE_COMM_CANCELLED = "file transfer cancelled"
STATE_COMM_FAILED = "file transfer failed"
STATE_COMM_DONE = "file transfer done"
STATE_ALARM = "alarm_triggered"
STATE_IDLE = "idle"
STATE_RIDE_ON = "ride on"
STATE_RIDE_OFF = "ride off"
STATE_COMM_ON = "communication on"
STATE_COMM_OFF = "communication off"

WIDTH  = 128
HEIGHT = 64

i2c = machine.I2C(0, scl=machine.Pin(13), sda=machine.Pin(12), freq=400000)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

def screen_reset():
    oled.fill_rect(2, 23, 124, 39, 0)
    oled.show()

def show_battery(state):
    
    battery_percentage = get_battery_percentage(get_battery_voltage())
    battery_indicator = int(battery_percentage/100*128)
    #oled.fill(0)
    
    for i in range(0, battery_indicator, 6):
        oled.fill_rect(0, 5, i, 5, 1)
        oled.show()
        oled.fill(0)
        
    battery_percentage_text = str(int(battery_percentage))
    battery_percentage_text = battery_percentage_text + "%"
    oled.text(battery_percentage_text, 1, 12, 1) 
    oled.fill_rect(0, 5, battery_indicator, 5, 1)
    
    if state == STATE_IDLE:
        estimated_running_time_idle = calculate_running_time(battery_percentage, BATTERY_CAPACITY, IDLE_CONSUMPTION)
        estimated_running_time_idle_txt = f"ERT:{estimated_running_time_idle:.1f}h"
        oled.text(estimated_running_time_idle_txt, 64, 12, 1)
        
    elif state == STATE_RIDE_ON:
        estimated_running_time_ride_on = calculate_running_time(battery_percentage, BATTERY_CAPACITY, RIDE_ON_CONSUMPTION)
        estimated_running_time_ride_on_txt = f"ERT:{estimated_running_time_ride_on:.1f}h"
        oled.text(estimated_running_time_ride_on_txt, 64, 12, 1)
        
def start_screen():
    oled.poweron()
    oled.text("WELCOME :)", 27, 25, 1)
    oled.show()
    timer_elapsed(2000)
    oled.text("WELCOME :)", 27, 25, 0)
    oled.show()
    oled.poweroff()
    
def end_screen():
    oled.poweron()
    oled.text("BYE :(", 37, 25, 1)
    oled.show()
    timer_elapsed(2000)
    oled.text("BYE :(", 37, 25, 0)
    oled.show()
    oled.poweroff()

def powerOff():
    #print("Display Power Off")
    oled.poweroff()
    
def powerOn():
    #print("Display Power On")
    oled.poweron()

def s_to_hhmm(seconds):
    
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return str("{:02}:{:02}".format(hours, minutes))

def show_info(enable, CURRENT_STATE, BPM, ride_time, body_temp, bike_animation, draw_battery):
    
    if enable:
        if draw_battery:
            screen_reset()
            show_battery(CURRENT_STATE)
            draw_border(oled)

        if CURRENT_STATE == STATE_IDLE:
            screen_reset()
            oled.text("X2&hold:RideOn", 8, 27)
            oled.text("Button+X2+hold:", 5, 38)
            oled.text("Unlock bike", 21, 49)
            oled.show()
        
        elif CURRENT_STATE == STATE_RIDE_ON:
            screen_reset()
            if bike_animation:
                oled.text("Ride ON", 37, 50)
                oled.show()
                animate_bike(oled)
                
            oled.vline(0, 21, 63, 1)
            oled.vline(127, 21, 63, 1)
            oled.show()
            oled.text("Ride ON", 37, 50, 0)
            
            oled.show()
            oled.text("Rate: " + str(BPM) + "bpm", 27, 27)
            oled.text("Time: " + str(s_to_hhmm(ride_time)), 27, 38)
            oled.text("Temp: " + str(body_temp) + " C", 27, 49)
            draw_heart(0, 0, oled)
            draw_time(15, 38, oled)
            draw_circle(94, 0, oled)
            draw_temp(16, 49, oled)
        
        elif CURRENT_STATE == STATE_RIDE_OFF:
            screen_reset()
            for i in range(4):
                oled.text("Ride OFF", 28, 38, 1)
                oled.show()
                timer_elapsed(250)
                oled.text("Ride OFF", 28, 38, 0)
                oled.show()
                timer_elapsed(250)
                
        elif CURRENT_STATE == STATE_COMM_ON:
            screen_reset()
            #oled.text("Waiting for", 21, 28, 1)
            oled.text("Sending files", 13, 38, 1)
            #oled.text("connect", 38, 48, 1)
            oled.show()
        
        elif CURRENT_STATE == STATE_COMM_CANCELLED:
            screen_reset()
            oled.text("File", 46, 28, 1)
            oled.text("transfer", 31, 38, 1)
            oled.text("cancelled", 28, 48, 1)
            oled.show()
            timer_elapsed(2_000)
            oled.text("File", 46, 28, 0)
            oled.text("transfer", 31, 38, 0)
            oled.text("cancelled", 28, 48, 0)
            oled.show()
        
        elif CURRENT_STATE == STATE_COMM_FAILED:
            screen_reset()
            oled.text("File", 46, 28, 1)
            oled.text("transfer", 31, 38, 1)
            oled.text("failed", 40, 48, 1)
            oled.show()
            timer_elapsed(2_000)
            oled.text("File", 46, 28, 0)
            oled.text("transfer", 31, 38, 0)
            oled.text("failed", 40, 48, 0)
            oled.show()
            
        elif CURRENT_STATE == STATE_COMM_DONE:
            screen_reset()
            oled.text("File", 46, 28, 1)
            oled.text("transfer", 31, 38, 1)
            oled.text("done", 46, 48, 1)
            oled.show()
            timer_elapsed(2_000)
            oled.text("File", 46, 28, 0)
            oled.text("transfer", 31, 38, 0)
            oled.text("done", 46, 48, 0)
            timer_elapsed(300)
            oled.text("X2&hold:RideOn", 8, 27)
            oled.text("Button+X2+hold:", 5, 38)
            oled.text("Unlock bike", 21, 49)
            oled.show()
        
        elif CURRENT_STATE == STATE_ALARM:
            screen_reset()
            draw_danger(62, 30, oled)
            waves_animation(50, oled)
            draw_border(oled)
            waves_animation(50, oled)
            draw_border(oled)
            waves_animation(50, oled)
            draw_border(oled)
        
        elif CURRENT_STATE == STATE_SOLENOID_OPEN:
            screen_reset()
            lock_animation(400, oled, 0)
            
        elif CURRENT_STATE == STATE_SOLENOID_CLOSE:
            lock_animation(400, oled, 1)
        
    
    oled.show()
    if not enable:
        oled.fill(0)
        oled.show()


   