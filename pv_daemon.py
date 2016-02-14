#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module generating user and proposal info PVs
"""

import pytz
import datetime
import time
import sys

# set ~/scheduling.ini to match your configuration
import dmagic.scheduling as sch
import pv_32ID as pv

def pv_daemon():
    # set the experiment date 
    now = datetime.datetime.today().replace(tzinfo=pytz.timezone('US/Central'))
    print now
    # set iso format time
    pv.time_iso.put(now.isoformat())

    # get PI information
    user_name, user_institution, user_badge, user_email = sch.find_pi_info(now)
    pv.user_name.put(user_name)
    pv.user_affiliation.put(user_institution)
    pv.user_email.put(user_email)
    pv.user_badge.put(user_badge)

    # get experiment information
    proposal_number, proposal_title = sch.find_experiment_info(now)
    pv.proposal_number.put(proposal_number)
    pv.proposal_title.put(proposal_title)

try:
    while True:
	pv_daemon()
        time.sleep(3600)
except (KeyboardInterrupt, SystemExit):
    pass    
