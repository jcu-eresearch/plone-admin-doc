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

Setting Emergency User
----------------------

Within the ``buildout.cfg`` file the are sections that describe the configuration of the services. The sections titled **instanceN** uses the `plone.recipe.zope2instance`_ recipe to describe the Zope instances that host the applications. To set the emergency user and password for one of these instances use the **user** property.

::

   [instance]
   user = admin:secret

Setting Effective User
----------------------

Within the ``buildout.cfg`` file the are sections that describe the configuration of the services. The sections titled **instanceN** uses the `plone.recipe.zope2instance`_ recipe to describe the Zope instances that host the applications. To set the effective user that the service will run as use the **effective-user** property.

::

   [instance]
   effective-user = zope


.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`plone.recipe.zope2instance`: http://pypi.python.org/pypi/plone.recipe.zope2instance
