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
   $ python2.4 `which virtualenv` zope2-python

.. include:: zope-req.rst


Buildout
--------

::
   
   $ git clone git://code.arcs.org.au/plone-deployments/zope-buildout.git
   $ . ./zope2-python/bin/activate
   (zope2-python)$ cd zope-buildout
   (zope2-python)$ python bootstrap.py
   (zope2-python)$ ./bin/buildout



