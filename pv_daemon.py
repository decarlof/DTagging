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
import epics_pv_32ID as pv

def pv_daemon():
    # set the experiment date 
    now = datetime.datetime.today().replace(tzinfo=pytz.timezone('US/Central'))

    # set iso format time
    pv.timeISO.put(now.isoformat())

    # get PI information
    pi_name, pi_institution, pi_badge, pi_email = sch.find_pi_info(now)
    pv.pi_name.put(pi_name)
    pv.pi_institution.put(pi_institution)
    pv.pi_badge.put(pi_badge)
    pv.pi_email.put(pi_email)

    # get experiment information
    proposal_id, proposal_title = sch.find_experiment_info(now)
    pv.proposal_id.put(proposal_id)
    pv.proposal_title.put(proposal_title)

try:
    while True:
        pv_daemon()
        time.sleep(60)
except (KeyboardInterrupt, SystemExit):
    pass    
