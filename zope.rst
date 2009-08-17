Zope
====

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

.. include:: zope-req.rst

Install
-------

Instructions under this section will install Zope under the directory::


  /srv/zope


Running as the **zope** user (as configured in the ``buildout.cfg`` file).  

The script for running the server is located at::


  /etc/init.d/zope


Now, you need to run::


 $ python2.4 bootstrap.py


This will install zc.buildout for you.

To install the versions of Zope run, on RedHat you will require the 
python-devel package.

::

 $ bin/buildout


The Zope instances control scripts are all located in the bin directory. 
Running the following command will run as the effective user zope.

::

 $ bin/zeo-arcs start

