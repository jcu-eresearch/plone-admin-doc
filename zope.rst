Zope
====

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Zope is a python web application server.


.. include:: zope-req.rst

Install
-------

Instructions under this section will install Zope under the directory ``/opt/zope``

Running as the **zope** user (as configured in the ``buildout.cfg`` file).  

Clone the current version of the Zope buildout::

   $ cd /opt
   $ git clone git://code.arcs.org.au/plone-deployments/zope-buildout.git zope
   $ cd zope

Install `zc.buildout`_ using the bootstrap script::

   $ python2.4 bootstrap.py

Execute the buildout to install and configure Zope and the Zope Instance.

::

   $ bin/buildout


The script for running the server is located at::

   /opt/zope/etc/init.d/zope

Symlink it into place for ease of use by other administrators ``ln -s /opt/zope/etc/init.d/zope /etc/init.d/zope``



The Zope instances control scripts are all located in the bin directory. 
Running the following command will run as the effective user zope.

::

  $ bin/instance start

.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
