VirtualEnv
==========

Our Plone environments utilise the Python programming language.  Due to the number of different Python package (commonly known as `eggs`) dependencies that our system requires, it is easiest to install these in an isolated environment.  By doing so, we can ensure that our install doesn't affect other Python applications (or other Plone installations!) that might be on our physical or virtual machine.  The technology we use of this is called `virtualenv`_, and it creates a distinct separation between the system Python path and a local, virtualenv.  As a useful side note, having a virtualenv present also means that you can install packages on a shared host, when you might not have access to install into the system-wide Python path.

Installing
----------

The easiest, most universal manner of installing virtualenv on a system is to utilise `setuptools`_, and specifically, the `easy_install` command.  Also, depending on your OS, you might be able to install a pre-compiled binary package (for example an .rpm or a .deb) of virtualenv.  This latter installation method locks you into your distribution's specific version, and in the case of OSes like Ubuntu 10.04, may introduce undesired patches that affect your work.

All distributions
~~~~~~~~~~~~~~~~~

::

   # wget http://pypi.python.org/packages/2.4/s/setuptools/setuptools-0.6c11-py2.4.egg
   # sh setuptools-0.6c11-py2.4.egg
   # rm setuptools-0.6c11-py2.4.egg
   # easy_install -U virtualenv

**Note:** Keep in mind that you will need to download the relevant setuptools egg for your Python version.  Also, you need to use the relevant *easy_install* command for your required Python version.  For example, this may be *easy_install-2.4* for Plone 3, or *easy_install-2.6* for Plone 4 or later. 

Debian/Ubuntu
~~~~~~~~~~~~~

::

   # apt-get install python-virtualenv

Using a virtual environment
---------------------------

New environment
~~~~~~~~~~~~~~~

Building a new environment is simple.  You just run the `virtualenv`_ command, and your virtual environment is automagically created.

::

   $ virtualenv virt-python
   $ source virt-python/bin/activate
   (virt-python)$ which python
   /home/russell/virt-python/bin/python

Using the `source` command activates the virtualenv, causing the default Python interpreter to become a local copy, which gets created in `virt-python/bin/`.  Any Python-centric commands run whilst the virtualenv is *activated* will use this interpreter. In particular, eggs installed within this virtualenv will only be available locally here.

Upgrading an existing folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converting any existing folder (such as a pre-existing buildout) to virtualenv is straightforward.

::
   $ cd ~/virt-python
   $ virtualenv . 
   $ source ./bin/activate
   (virt-python)$ which python
   /home/russell/virt-python/bin/python

Deactivating
~~~~~~~~~~~~

Once you're finished, or want to work outside your virtualenv again, deactivate the virtualenv when done::

   (virtual-python)$ deactivate
   $ which python
   /usr/bin/python 

Tips
~~~~

* You can make virtualenv use *any* Python interpreter on your system with the `-p PYTHON_EXE` flag when first running the command.  For example, if we wanted to use Python2.4 specifically, then we would create a virtualenv thusly: `virtualenv -p /usr/bin/python2.4`
* Virtualenv can be told to ignore all system-level packages with the `--no-site-packages` flag.  This is useful if you're already using something at site (system) level and want to use something older in a virtualenv.

.. seealso::

   `Virtualenv <http://pypi.python.org/pypi/virtualenv>`_
      The Virtualenv homepage
   `Setuptools <http://pypi.python.org/pypi/setuptools>`_
      The setuptools homepage

