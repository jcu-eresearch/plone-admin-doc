Zeo
===

Zeo is a service that separates the data store out of the Zope service.  Essentially, Zeo is the service that operates the backend :abbr:`ZODB (Zope Object Database)`. This means we can take advantage of mass storage and allow better scalability, rather than just having the database being tied to one instance of Zope (or Plone).

Prerequisites
-------------

Zeo has the same prerequisites as Zope 2 does.  

.. include:: zope/prereq.rst

Install
-------

Instructions under this section will install Zeo under the directory::

  /srv/zeo

Running as the **zope** user (as configured in the ``buildout.cfg`` file). 

Clone the current version of the Zope buildout::

   cd /opt
   git clone git://code.arcs.org.au/plone-deployments/zeo-buildout.git zeo
   cd zeo

You may need to check out a certain branch of the repository to make sure that you've got the right configuration for the instance you're deploying.  Certain instances may have specific requirements (for example, eggs or scripts) which individual branches provide.

Install a virtualenv inside the buildout::

   virtualenv -p /usr/bin/python2.4 .
   source ./bin/activate

Install `zc.buildout`_ using the bootstrap script::

   python bootstrap.py

Execute the buildout to install and configure Zope and the Zope Instance.

::

   bin/buildout

Local Zeo Operation
-------------------

The Zeo instance control scripts are all located in the ``./bin/`` directory within a given buildout folder.  Running the relevant command will control the service and do so as the effective-user *zope*. 

::

   $ bin/zeo-arcs start
   . . daemon process started, pid=22281
   $ bin/zeo-arcs status
   program running; pid=22281

   $ bin/zeo-arcs stop
   . . daemon process stopped
   $ bin/zeo-arcs status
   daemon manager not running

Global Operation
-----------------

The server-wide script for running Zeo instances is located at::

  /etc/init.d/zeo

Running this script with the ``start`` argrument will start the server, just like it did with the local instances described above.  Conversely, the ``stop`` argument will stop the service from operating.  You can check whether the server is running with the argument ``status``.

