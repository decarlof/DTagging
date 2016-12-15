========
DTagging
========

`DTagging <https://github.com/decarlof/DTagging>`_  is used at the Advanced Photon Source Imaging Group
to generate EPICS Process Variables (PVs)for storing the information associated with the current user including:

* User Name
* User Institution
* User Badge
* User e-mail
* General User Proposal (GUP) number 
* Proposal Title

The current user information is obtained from the APS scheduluing system running at a predefined beamline.
This information can be easely stored in all hdf files collected using `area detector <http://cars9.uchicago.edu/software/epics/areaDetector.html>`_
see `DXFile <http://dxfile.readthedocs.io/en/latest/source/demo/doc.areadetector.html>`_ for more details.

Pre-requisites
--------------

* Load in your EPICS ioc the ExperimentInfo `db <https://github.com/decarlof/DTagging/tree/master/epics>`_ file:
    * Example: dbLoadRecords("$(TOP)/32idcTXMApp/Db/experimentInfo.db", "P=32idcTXM:")

* Add a link to your main MEDM screen to load the ExperimentInfo `medm <https://github.com/decarlof/DTagging/tree/master/epics>`_ file.

* Install `PyEpics <http://cars9.uchicago.edu/software/python/pyepics3/index.html>`_
    * pip install pyepics
    * edit your .cshrc to set PYEPICS_LIBCA. Example: setenv PYEPICS_LIBCA /APSshare/epics/extensions-base/3.14.12.2-ext1/lib/linux-x86_64/libca.so
    
* Install `DMagic <http://dmagic.readthedocs.io/>`_
    * item 3 
    * item 4
   

Features--------* Generate PVs containing the current experiment/user information
