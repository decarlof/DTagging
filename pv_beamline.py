# -*- coding: utf-8 -*-
"""
Transmission X-ray Microscope process variables grouped by component

"""

from epics import PV

# User Status
user_name = PV('32idcTXM:UserName')
user_affiliation = PV('32idcTXM:UserInstitution')
user_badge = PV('32idcTXM:UserBadge')
user_email = PV('32idcTXM:UserEmail')
proposal_number = PV('32idcTXM:ProposalNumber')
proposal_title = PV('32idcTXM:ProposalTitle')
user_info_update_time= PV('32idcTXM:UserInfoUpdate')
file_name = PV('32idcPG3:HDF1:FileName')
file_path = PV('32idcPG3:HDF1:FilePath_RBV')

