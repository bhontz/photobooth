import Adafruit_MPR121.MPR121 as MPR121
import sys, time

def CapTouchHandler(cap, lt, n):
    return_value = -1
    ct = cap.touched()
    pinbit = 0
    for i in range(0, n):
        pinbit = 1 << i
        if ct & pinbit and not lt & pinbit:
            sys.stdout.write("Pin {0} touched.\r".format(i))
            time.sleep(0.5)
            sys.stdout.flush()
            
        if not ct & pinbit and lt & pinbit:
            sys.stdout.write("Pin {0} released.\r".format(i))
            time.sleep(0.5)
            sys.stdout.flush()
            return_value = i
            break
            
    return return_value, ct