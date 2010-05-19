Quickstart
==========

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Introduction
------------

Clean basic plone install using virtualenv and buildout.

Environment Setup
-----------------

::

   $ easy_install virtualenv

If your system doesn't have easy_install packaged :ref:`install easyinstall <faq-easyinstall>`.

::

   $ cd /opt
   $ python2.4 `which virtualenv` virt-zope2


.. include:: tech/zope/prereq.rst


Buildout
--------

::
   
   $ git clone git://code.arcs.org.au/plone-deployments/zope-buildout.git
   $ . ./virt-zope2/bin/activate

Once you have sourced the ``activate`` file, you should notice your prompt change to include **(virt-zope)**::

   (virt-zope)$ cd zope-buildout

   (virt-zope)$ python bootstrap.py
   Creating directory '/opt/zope-buildout/bin'.
   Creating directory '/opt/zope-buildout/parts'.
   Creating directory '/opt/zope-buildout/eggs'.
   Creating directory '/opt/zope-buildout/develop-eggs'.
   Generated script '/opt/zope-buildout/bin/buildout'.
   (virt-zope)$ ./bin/buildout



