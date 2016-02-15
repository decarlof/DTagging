import time
import pytz
import datetime
import epics

import pv_32ID as pv

def pv_daemon():
    now = datetime.datetime.today()
    central = pytz.timezone('US/Central')

    local_time = central.localize(now)
    local_time_iso = local_time.isoformat()
    print local_time_iso

    pv.time_iso.put(local_time_iso)

try:
    while True:
	pv_daemon()
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    pass    
