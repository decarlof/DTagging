#!/bin/bash -l
export PYEPICS_LIBCA="/APSshare/epics/extensions-base/3.14.12.2-ext1/lib/linux-x86_64/libca.so"
cd /local/7bmb/conda/DTagging/
/home/beams/7BMB/anaconda3/bin/python pv_update.py
