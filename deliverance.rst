Deliverance
===========

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Install
-------

The easiest way to get started with deliverance is using virtual env

::

   $ virtualenv deliverance
   $ cd deliverance
   $ . ./bin/activate
   $ mkdir src
   $ cd src
   $ svn co http://codespeak.net/svn/z3/deliverance/trunk/ deliverance
   $ cd deliverance
   $ python setup.py devlop
   $ cd ../..

If you have PasteScript installed you should now be able to run::

   $ paster create --list-templates
   Available templates:
     archetype:                 A Plone project that uses Archetypes
     basic_namespace:           A project with a namespace package
     basic_package:             A basic setuptools-enabled package
     deliverance:               Basic template for a deliverance-proxy setup
     deliverance_plone:         Plone-specific template for deliverance-proxy
   $ paster create -t deliverance_plone dplone
   .....
   $ cd dplone
   $ deliverance-proxy etc/deliverance.xml

