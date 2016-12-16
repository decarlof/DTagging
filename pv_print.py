# -*- coding: utf-8 -*-
"""
.. module:: add_dataExchange_entries.py
   :platform: Unix
   :synopsis: add Data Exchange entries to an HDF5 file
   :INPUT
      Data Exchange file name 

.. moduleauthor:: David Vine <djvine@gmail.com>, Francesco De Carlo <decarlof@gmail.com>

This module is largely John Hammonds work to which I'll be adding
some scripts as needed.
""" 

import os
import sys
import datetime
import pv_beamline as pv

if __name__ == "__main__":


    # User Status
    print "user_name:", pv.user_name.get()
    print "user_affiliation:", pv.user_affiliation.get()
    print "user_email:", pv.user_email.get()
    print "user_badge:", pv.user_badge.get()
    print "proposal_number:", pv.proposal_number.get()
    print "proposal_title:", pv.proposal_title.get()
    print "user_info_update_time:", pv.user_info_update_time.get()

