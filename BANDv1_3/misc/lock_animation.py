from misc.draw import draw_lock
from timer import timer_elapsed
    
def lock_animation(speed, oled, lock):
    unlock_sequence = [1,2,3,4,5]
    lock_sequence = [4,3,2,1,6]
    
    if not lock:
        for i in unlock_sequence:
            draw_lock(53, 27, oled, 1, i)
            timer_elapsed(speed)
            draw_lock(53, 27, oled, 0, i)
        draw_lock(53, 27, oled, 1, 4)
            
    if lock:
        for i in lock_sequence:
            draw_lock(53, 27, oled, 1, i)
            timer_elapsed(speed)
            draw_lock(53, 27, oled, 0, i)
        draw_lock(53, 27, oled, 1, 1)