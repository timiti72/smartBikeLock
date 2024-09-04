import time

#timer_type:
#	True/1 for "time";
#	False/0 for "time_elapsed"

start_time = 0
start_time_elapsed = 0

def timer_start(timer_type = True):
    global start_time, start_time_elapsed
    if timer_type:
        start_time = time.ticks_ms()
    else:
        start_time_elapsed = time.ticks_ms()

def timer_check(timer_type = True):
    global start_time, start_time_elapsed
    if timer_type:
        if start_time == 0:
            return 0
        return time.ticks_ms() - start_time
    else:
        if start_time_elapsed == 0:
            return 0
        return time.ticks_ms() - start_time_elapsed

def timer_reset(timer_type = True):
    global start_time, start_time_elapsed
    if timer_type:
        start_time = 0
    else:
        start_time_elapsed = 0
    
def timer_elapsed(n):
    counting = True
    timer_start(False)
    while counting:
        if(timer_check(False)>=n):
            counting = False
    return counting
