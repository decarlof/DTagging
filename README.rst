========
DTagging
========


.. warning:: If your python installation is in a location different from #!/usr/bin/env python please edit the first line of the bin/dmagic file to match yours.


`DTagging <https://github.com/decarlof/DTagging>`_  is used at the Advanced Photon Source Imaging Group
to generate EPICS Process Variables (PVs)for storing the information associated with the current user including:

* User Name
* User Institution
* User Badge
* User e-mail
* General User Proposal (GUP) number 
* Proposal Title


.. image:: epics/medm_screen.png
  :width: 400
  :alt: medm screen


The current user information is obtained from the APS scheduluing system running at a predefined beamline.
This information can be easely stored in all hdf files collected using `area detector <http://cars9.uchicago.edu/software/epics/areaDetector.html>`_
see `DXFile <http://dxfile.readthedocs.io/en/latest/source/demo/doc.areadetector.html>`_ for more details.

Pre-requisites
--------------

* Install `PyEpics <http://cars9.uchicago.edu/software/python/pyepics3/index.html>`_::

    pip install pyepics

edit your .cshrc to set PYEPICS_LIBCA:

Example: setenv PYEPICS_LIBCA /APSshare/epics/extensions-base/3.14.12.2-ext1/lib/linux-x86_64/libca.so

* Install DMagic from `source <http://dmagic.readthedocs.io/en/latest/source/install.html#installing-from-source>`_ 

To access the `APS scheduling system <https://schedule.aps.anl.gov/>`__ you need 
to create in your home directory the DMagic configuration file 
`scheduling.ini <https://github.com/decarlof/DMagic/blob/master/config/scheduling.ini>`__.

Using DTagging
--------------

* Clone the `DTagging <https://github.com/decarlof/DTagging>`_ project from its `GitHub <https://github.com>`_ repository::

    git clone https://github.com/decarlof/DTagging.git DTagging
    cd DTagging

* Load in your EPICS ioc the DTagging/epics/experimentInfo.db file. Example::
    
    dbLoadRecords("$(TOP)/32idcTXMApp/Db/experimentInfo.db", "P=32idcTXM:")

* Add a link to your main MEDM screen to load the DTagging/epics/experimentInfo.adl file.

* Customize the DTagging/pv_beamline.py file to match the PV names in use at your beamline then run::

    python pv_update.py
    

pv_user.py reads the current user information from the scheduling system and update the user information PVs.
You can verify the result by accessing the user info medm screen or by running::

    python pv_print.py
    
    
Features
--------

* Generate PVs containing the current experiment/user information
