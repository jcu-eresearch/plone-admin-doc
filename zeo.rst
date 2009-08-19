Zeo
===

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Zeo is a service that separates the data store out of the Zope service. This means we can take advantage of mass storage and allow better scalability.

.. include:: zope/prereq.rst

Install
-------

Instructions under this section will install Zeo under the directory::


  /srv/zeo


Running as the **zope** user (as configured in the ``buildout.cfg`` file).  

The script for running the server is located at::


  /etc/init.d/zeo


Now, you need to run::


  python2.4 bootstrap.py


This will install zc.buildout for you.

To install the versions of Zeo run, on RedHat you will require the 
python-devel package.

::

   bin/buildout


The Zeo instances control scripts are all located in the bin directory. 
Running the following command will run as the effective user zope.

::

   bin/zeo-arcs start

