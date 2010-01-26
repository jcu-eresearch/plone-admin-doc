Zope
====

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Zope is a python web application server.


Prerequisites
-------------

.. include:: prereq.rst


Install
-------

Instructions under this section will install Zope under the directory ``/opt/zope``

Running as the **zope** user (as configured in the ``buildout.cfg`` file).  

Clone the current version of the Zope buildout::

   cd /opt
   git clone git://code.arcs.org.au/plone-deployments/zope-buildout.git zope
   cd zope

Install a virtualenv inside the buildout::

   virtualenv -p /usr/bin/python2.4 .
   source ./bin/activate

Install `zc.buildout`_ using the bootstrap script::

   python bootstrap.py

Execute the buildout to install and configure Zope and the Zope Instance.

::

   bin/buildout


Zope Service Control
--------------------

.. include:: service.rst


Intergrating with Operating System
----------------------------------

.. include:: intergration.rst


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
