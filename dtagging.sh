#!/bin/bash -l
export PYEPICS_LIBCA="/APSshare/epics/extensions-base/3.14.12.2-ext1/lib/linux-x86_64/libca.so"
cd /local/user2bmb/conda/DTagging/
/local/user2bmb/Software/anaconda/bin/python pv_update.py
