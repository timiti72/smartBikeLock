import random
import time

def mode_animation(length, speed, row_no, line_no, oled):
    animation_length = time.ticks_ms()
    rows = []
    
    for _ in range(row_no):
        lines = []
        while len(lines) < line_no:
            line_length = random.randint(20, 40)
            line_poz_y = random.randint(23, 62)
            if all(abs(line_poz_y - l[1]) >= 2 for l in lines):  # Ensure y distance is at least 2 pixels
                line_speed = random.randint(1, 5)  # Random speed for each line
                lines.append([0, line_poz_y, line_length, line_speed])
        rows.append(lines)

    max_x = oled.width
    all_off_screen = False
    
    while not all_off_screen:
        oled.fill(0)  # Clear the screen
        
        all_off_screen = True  # Assume all lines will be off-screen unless proven otherwise
        
        for row in rows:
            for line in row:
                line_poz_x, line_poz_y, line_length, line_speed = line
                current_x = line_poz_x + line_speed
                if current_x < max_x:
                    oled.hline(current_x, line_poz_y, line_length, 1)
                    line[0] = current_x  # Update the position of the line
                    all_off_screen = False  # There is still at least one line on the screen
                else:
                    line[0] = max_x + 1  # Ensure the line stays off-screen
        
        oled.show()
        time.sleep(speed / 1000)
        
        if time.ticks_ms() - animation_length > length and all_off_screen:
            break
