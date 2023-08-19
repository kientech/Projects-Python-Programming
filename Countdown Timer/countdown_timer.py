# Coding With Kien

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    print('Time is up!')

countdown(60)  # countdown for 60 seconds
