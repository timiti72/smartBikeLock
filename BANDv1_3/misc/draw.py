

def draw_temp(offset_x, offset_y, oled):
    #layer 1
    oled.hline(offset_x+1, offset_y, 1, 1)
    oled.hline(offset_x+3, offset_y, 2, 1)
    #layer 2
    oled.hline(offset_x+1, offset_y+1, 1, 1)
    oled.hline(offset_x+3, offset_y+1, 1, 1)
    #layer 3
    oled.hline(offset_x+1, offset_y+2, 1, 1)
    oled.hline(offset_x+3, offset_y+2, 2, 1)
    #layer 4
    oled.hline(offset_x+1, offset_y+3, 1, 1)
    oled.hline(offset_x+3, offset_y+3, 1, 1)
    #layer 5
    oled.hline(offset_x+1, offset_y+4, 1, 1)
    oled.hline(offset_x+3, offset_y+4, 1, 1)
    #layer 6
    oled.hline(offset_x, offset_y+5, 2, 1)
    oled.hline(offset_x+3, offset_y+5, 2, 1)
    #layer 7
    oled.hline(offset_x, offset_y+6, 1, 1)
    oled.hline(offset_x+4, offset_y+6, 1, 1)
    #layer 8
    oled.hline(offset_x+1, offset_y+7, 3, 1)
    oled.show()

def draw_border(oled):
    #border horizontal
    oled.hline(0, 21, 128, 1)
    oled.hline(0, 63, 128, 1)
    #border vertical
    oled.vline(0, 21, 63, 1)
    oled.vline(127, 21, 63, 1)
    oled.show()

def draw_lock(offset_x, offset_y, oled, color, frame):
    
    frame%=7
    
    oled.fill_rect(offset_x, offset_y+15, 19, 15, 1)
    #key hole
    oled.vline(offset_x+7, offset_y+19, 2, 0)
    oled.vline(offset_x+8, offset_y+18, 4, 0)
    oled.vline(offset_x+9, offset_y+18, 8, 0)
    oled.vline(offset_x+10, offset_y+18, 4, 0)
    oled.vline(offset_x+11, offset_y+19, 2, 0)
    #lock arm frame 1
    if frame == 1:
        oled.vline(offset_x+2, offset_y+10, 5, color)
        oled.vline(offset_x+3, offset_y+8, 7, color)
        oled.vline(offset_x+4, offset_y+6, 4, color)
        
        oled.hline(offset_x+5, offset_y+6, 9, color)
        oled.hline(offset_x+5, offset_y+7, 9, color)
        
        oled.vline(offset_x+14, offset_y+6, 4, color)
        oled.vline(offset_x+15, offset_y+8, 7, color)
        oled.vline(offset_x+16, offset_y+10, 5, color)
    #lock arm frame 2 
    if frame == 2:
        oled.vline(offset_x+2, offset_y+8, 7, color)
        oled.vline(offset_x+3, offset_y+6, 9, color)
        oled.vline(offset_x+4, offset_y+4, 4, color)
        
        oled.hline(offset_x+5, offset_y+4, 9, color)
        oled.hline(offset_x+5, offset_y+5, 9, color)
        
        oled.vline(offset_x+14, offset_y+4, 4, color)
        oled.vline(offset_x+15, offset_y+6, 7, color)
        oled.vline(offset_x+16, offset_y+8, 5, color)
    #lock arm frame 3    
    if frame == 3:
        oled.vline(offset_x+2, offset_y+6, 9, color)
        oled.vline(offset_x+3, offset_y+4, 11, color)
        oled.vline(offset_x+4, offset_y+2, 4, color)
        
        oled.hline(offset_x+5, offset_y+2, 9, color)
        oled.hline(offset_x+5, offset_y+3, 9, color)
        
        oled.vline(offset_x+14, offset_y+2, 4, color)
        oled.vline(offset_x+15, offset_y+4, 7, color)
        oled.vline(offset_x+16, offset_y+6, 5, color)
    #lock arm frame 4    
    if frame == 4:
        oled.vline(offset_x+2, offset_y+4, 11, color)
        oled.vline(offset_x+3, offset_y+2, 13, color)
        oled.vline(offset_x+4, offset_y, 4, color)
        
        oled.hline(offset_x+5, offset_y, 9, color)
        oled.hline(offset_x+5, offset_y+1, 9, color)
        
        oled.vline(offset_x+14, offset_y, 4, color)
        oled.vline(offset_x+15, offset_y+2, 7, color)
        oled.vline(offset_x+16, offset_y+4, 5, color)
    #lock arm frame 5    
    if frame == 5:
        oled.vline(offset_x+2, offset_y+4, 11, color)
        oled.vline(offset_x+3, offset_y+2, 13, color)
        oled.vline(offset_x+4, offset_y, 4, color)
        
        oled.hline(offset_x+5, offset_y, 9, color)
        oled.hline(offset_x+5, offset_y+1, 9, color)
        
        oled.vline(offset_x+14, offset_y, 4, color)
        oled.vline(offset_x+15, offset_y+2, 7, color)
        oled.vline(offset_x+16, offset_y+4, 5, color)
        
        oled.pixel(offset_x+11, offset_y+8, color)
        oled.pixel(offset_x+20, offset_y+8, color)
        oled.pixel(offset_x+12, offset_y+9, color)
        oled.pixel(offset_x+19, offset_y+9, color)
        oled.pixel(offset_x+13, offset_y+10, color)
        oled.pixel(offset_x+18, offset_y+10, color)
        oled.pixel(offset_x+18, offset_y+14, color)
        oled.pixel(offset_x+18, offset_y+14, color)
        oled.pixel(offset_x+19, offset_y+15, color)
        oled.pixel(offset_x+20, offset_y+16, color)
        
        oled.hline(offset_x+11, offset_y+12, 3, color)
        oled.hline(offset_x+18, offset_y+12, 3, color)
        
        
    #lock arm frame 6    
    if frame == 6:
        oled.vline(offset_x+2, offset_y+10, 5, color)
        oled.vline(offset_x+3, offset_y+8, 7, color)
        oled.vline(offset_x+4, offset_y+6, 4, color)
        
        oled.hline(offset_x+5, offset_y+6, 9, color)
        oled.hline(offset_x+5, offset_y+7, 9, color)
        
        oled.vline(offset_x+14, offset_y+6, 4, color)
        oled.vline(offset_x+15, offset_y+8, 7, color)
        oled.vline(offset_x+16, offset_y+10, 5, color)
        
        oled.pixel(offset_x+11, offset_y+8, color)
        oled.pixel(offset_x+20, offset_y+8, color)
        oled.pixel(offset_x+12, offset_y+9, color)
        oled.pixel(offset_x+19, offset_y+9, color)
        oled.pixel(offset_x+13, offset_y+10, color)
        oled.pixel(offset_x+18, offset_y+10, color)
        oled.pixel(offset_x+18, offset_y+14, color)
        oled.pixel(offset_x+18, offset_y+14, color)
        oled.pixel(offset_x+19, offset_y+15, color)
        oled.pixel(offset_x+20, offset_y+16, color)
        
        oled.hline(offset_x+11, offset_y+12, 3, color)
        oled.hline(offset_x+18, offset_y+12, 3, color)
    
    oled.show()

def draw_wave(wave_no, offset_x, offset_y, oled, inverted, color):
    wave_no %= 8
    if inverted:
        inverted_x = 2
    else:
        inverted_x = inverted_y = 0
        
    if wave_no == 1:
        #WAVE 1
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+5, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+4, 1, color)
        #column 3
        oled.vline(offset_x+2-inverted_x*2, offset_y+2, 2, color)
        oled.show()
    elif wave_no == 2:
        #WAVE 2
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+7, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+6, 1, color)
        #column 3
        oled.vline(offset_x+2-2*inverted_x, offset_y+2, 4, color)
        oled.show()
    elif wave_no == 3:
        #WAVE 3
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+9, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+8, 1, color)
        #column 3
        oled.vline(offset_x+2-2*inverted_x, offset_y+2, 6, color)
        oled.show()
    elif wave_no == 4:
        #WAVE 4
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+11, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+10, 1, color)
        #column 3
        oled.vline(offset_x+2-inverted_x*2, offset_y+2, 8, color)
        oled.show()
    elif wave_no == 5:
        #WAVE 5
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+13, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+12, 1, color)
        #column 3
        oled.vline(offset_x+2-inverted_x*2, offset_y+2, 3, color)
        oled.vline(offset_x+2-inverted_x*2, offset_y+9, 3, color)
        #column 4
        oled.vline(offset_x+3-inverted_x*3, offset_y+4, 6, color)
        oled.show()
    elif wave_no == 6:
        #WAVE 6
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+15, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+14, 1, color)
        #column 3
        oled.vline(offset_x+2-inverted_x*2, offset_y+2, 2, color)
        oled.vline(offset_x+2-inverted_x*2, offset_y+12, 2, color)
        #column 4
        oled.vline(offset_x+3-inverted_x*3, offset_y+4, 2, color)
        oled.vline(offset_x+3-inverted_x*3, offset_y+10, 2, color)
        #column 5
        oled.vline(offset_x+4-inverted_x*4, offset_y+5, 6, color)
        oled.show()
    elif wave_no == 7:
        #WAVE 7
        #column 1
        oled.vline(offset_x, offset_y, 1, color)
        oled.vline(offset_x, offset_y+16, 1, color)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, color)
        oled.vline(offset_x+1-inverted_x, offset_y+15, 1, color)
        #column 3
        oled.vline(offset_x+2-inverted_x*2, offset_y+2, 3, color)
        oled.vline(offset_x+2-inverted_x*2, offset_y+12, 3, color)
        #column 4
        oled.vline(offset_x+3-inverted_x*3, offset_y+4, 3, color)
        oled.vline(offset_x+3-inverted_x*3, offset_y+10, 3, color)
        #column 5
        oled.vline(offset_x+4-inverted_x*4, offset_y+6, 5, color)
        oled.show()
    elif wave_no == 8:
        #WAVE 8
        #column 1
        oled.vline(offset_x, offset_y, 1, 1)
        oled.vline(offset_x, offset_y+19, 1, 1)
        #column 2
        oled.vline(offset_x+1-inverted_x, offset_y+1, 1, 1)
        oled.vline(offset_x+1-inverted_x, offset_y+18, 1, 1)
        #column 3
        oled.vline(offset_x+2-inverted_x*2, offset_y+2, 3, 1)
        oled.vline(offset_x+2-inverted_x*2, offset_y+15, 3, 1)
        #column 4
        oled.vline(offset_x+3-inverted_x*3, offset_y+4, 3, 1)
        oled.vline(offset_x+3-inverted_x*3, offset_y+13, 3, 1)
        #column 5
        oled.vline(offset_x+4-inverted_x*4, offset_y+z, 8, 1)
        oled.show()
        
def draw_danger(offset_x, offset_y, oled):
    #column  1
    oled.vline(offset_x, offset_y, 11, 1)
    oled.vline(offset_x, offset_y+20, 3, 1)
    #column  2
    oled.vline(offset_x+1, offset_y, 15, 1)
    oled.vline(offset_x+1, offset_y+19, 5, 1)
    #column  3
    oled.vline(offset_x+2, offset_y, 16, 1)
    oled.vline(offset_x+2, offset_y+19, 5, 1)
    #column  4
    oled.vline(offset_x+3, offset_y, 15, 1)
    oled.vline(offset_x+3, offset_y+19, 5, 1)
    #column  5
    oled.vline(offset_x+4, offset_y, 11, 1)
    oled.vline(offset_x+4, offset_y+20, 3, 1)
    oled.show()

def draw_time(offset_x, offset_y, oled):
    #layer 1
    oled.hline(offset_x+1, offset_y, 5, 1)
    #layer 2
    oled.hline(offset_x, offset_y+1, 2, 1)
    oled.hline(offset_x+3, offset_y+1, 1, 1)
    oled.hline(offset_x+5, offset_y+1, 2, 1)
    #layer 3+4+5
    oled.hline(offset_x, offset_y+2, 1, 1)
    oled.hline(offset_x+3, offset_y+2, 1, 1)
    oled.hline(offset_x+6, offset_y+2, 1, 1)
    oled.hline(offset_x, offset_y+3, 1, 1)
    oled.hline(offset_x+3, offset_y+3, 1, 1)
    oled.hline(offset_x+6, offset_y+3, 1, 1)
    oled.hline(offset_x, offset_y+4, 1, 1)
    oled.hline(offset_x+4, offset_y+4, 1, 1)
    oled.hline(offset_x+6, offset_y+4, 1, 1)
    #layer 6
    oled.hline(offset_x, offset_y+5, 2, 1)
    oled.hline(offset_x+5, offset_y+5, 2, 1)
    #layer 7
    oled.hline(offset_x+1, offset_y+6, 5, 1)
    oled.show()

def draw_heart(offset_x, offset_y, oled):
    #layer 1
    oled.pixel(14, 26, 1)
    oled.pixel(15, 26, 1)
    oled.pixel(16, 26, 1)
    oled.pixel(20, 26, 1)
    oled.pixel(21, 26, 1)
    oled.pixel(22, 26, 1)
    #;ayer 2
    oled.pixel(13, 27, 1)
    oled.pixel(14, 27, 1)
    oled.pixel(15, 27, 1)
    oled.pixel(16, 27, 1)
    oled.pixel(17, 27, 1)
    oled.pixel(19, 27, 1)
    oled.pixel(20, 27, 1)
    oled.pixel(21, 27, 1)
    oled.pixel(22, 27, 1)
    oled.pixel(23, 27, 1)
    #layer 3
    oled.hline(13, 28, 11, 1)
    #layer 4
    oled.hline(14, 29, 9, 1)
    #layer 5
    oled.hline(15, 30, 7, 1)
    #layer 6
    oled.hline(16, 31, 5, 1)
    #layer 7
    oled.hline(17, 32, 3, 1)
    #layer 8
    oled.hline(18, 33, 1, 1)
    oled.show()
    
def draw_circle(offset_x, offset_y, oled):
    #layer 1
    oled.pixel(offset_x+1, 48, 1)
    oled.pixel(offset_x+2, 48, 1)
    #layer 2
    oled.pixel(offset_x, 49, 1)
    oled.pixel(offset_x+3, 49, 1)
    #layer 3
    oled.pixel(offset_x, 50, 1)
    oled.pixel(offset_x+3, 50, 1)
    #layer 4
    oled.pixel(offset_x+1, 51, 1)
    oled.pixel(offset_x+2, 51, 1)
    oled.show()      


