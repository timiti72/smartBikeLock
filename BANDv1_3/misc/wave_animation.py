from misc.draw import draw_wave
from timer import *

def waves_animation(speed, oled):
    
    x_coord = [67,72,78,85,93,102,112,123]
    x_coord_inverted = [59,54,48,41,33,24,14,3]
    y_coord_initial = 30
    
    for i in range(1,8,1):
      
        draw_wave(i, x_coord[i], y_coord_initial-i+5, oled, 0, 1)
        draw_wave(i, x_coord_inverted[i]+2, y_coord_initial+15-i, oled, 1, 1)
        timer_elapsed(speed)
        if i > 3:
            draw_wave(i-3, x_coord[i-3], y_coord_initial-(i-3)+5, oled, 0, 0)
            draw_wave(i-3, x_coord_inverted[i-3]+2, y_coord_initial+15-(i-3), oled, 1, 0)
    for i in range(5,8,1):  
    # After all waves are drawn, erase the last wave
        draw_wave(i, x_coord[i], y_coord_initial-i+5, oled, 0, 0)
        draw_wave(i, x_coord_inverted[i]+2, y_coord_initial+15-i, oled, 1, 0)
        timer_elapsed(speed)