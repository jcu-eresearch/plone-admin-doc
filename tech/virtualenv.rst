VirtualEnv
==========

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Virtualenv provides a way of seperating the python path easily away from the system python path. This means you can install eggs without causing conflicts with system installed version.

Installing
----------

The easiest way to install it on most systems is using easy_install

Linux
~~~~~

::

   $ easy_install -U virtualenv

Debian
~~~~~~

::

   $ apt-get install python-virtualenv

Using a virtual environment
---------------------------

Building a new environment is simple.

::

   $ virtualenv virt-python
   $ source virt-python/bin/activate
   (virt-python)$ which python
   /home/russell/virt-python/bin/python

Any commands run within the virtualenv will use this interpreter. Even eggs installed within will only be available to this virtualenv.

Deactivate the virtualenv when done::

   (virtual-python)$ deactivate
   $ which python
   /usr/bin/python 

.. seealso::

   Project `Virtualenv <http://pypi.python.org/pypi/virtualenv>`_
      The Virtualenv homepage

