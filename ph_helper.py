# this module will be imported in the into your flowgraph
#
# Drive an external serial port, uses its RTS and DTR lines to
#  control the phase switch.
#
import serial
import math
import time
sport = None
port_state = -1
def update_state(state,device):
    global port_state
    global sport
    if (sport == None):
        try:
            sport = serial.Serial(port=device,baudrate=1200,rtscts=False,
                dsrdtr=False)
        except:
            sport = None
            pass
    if (sport != None and port_state != state):
        sport.write("%1d" % state)
        port_state = state
        sport.rts = state
        sport.dtr = 0 if state != 0 else 1
        return (state)
    
    return (None)
        
def update_data(value):
    ltp = time.gmtime()
    datestr = "fringe-%04d%02d%02d" % (ltp.tm_year, ltp.tm_mon, ltp.tm_mday)
    fname = datestr+".csv"
    fp = open(fname, "a")
    tmstr = "%02d:%02d:%02d" % (ltp.tm_hour, ltp.tm_min, ltp.tm_sec)
    fp.write(tmstr+",")
    fp.write("%.9f\n" % value)
    fp.close()
    return 1

    
def getalpha(corner, srate):
    alpha = math.e ** (-2.0*(corner/srate))
    alpha = 1.0 - alpha
    return alpha


    
