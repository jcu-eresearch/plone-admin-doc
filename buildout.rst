Buildout
========

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Buildout is an advanced deployment systems that is mostly used to deploy and test Zope environments. Buildout leverages  existing Python tools like `ez_setup.py`_ and `setuptools`_ to create complex reproducible installs of complex systems.

Deploying
---------

When deploying the first step is to bootstrap the environment with the required python libraries and create directories [#f1]_ that will be used for the deployment.

:: 

   $ git clone git://code.arcs.org.au/plone-deployments/zope-buildout.git 
   Initialized empty Git repository in /home/russell/zope-buildout/.git/
   remote: Counting objects: 297, done.
   remote: Compressing objects: 100% (140/140), done.
   remote: Total 297 (delta 170), reused 258 (delta 150)
   Receiving objects: 100% (297/297), 49.74 KiB, done.
   Resolving deltas: 100% (170/170), done.
   $ cd zope-buildout/
   $ python bootstrap.py 
   Creating directory '/home/russell/tmp/zope-buildout/bin'.
   Creating directory '/home/russell/tmp/zope-buildout/parts'.
   Creating directory '/home/russell/tmp/zope-buildout/eggs'.
   Creating directory '/home/russell/tmp/zope-buildout/develop-eggs'.
   Generated script '/home/russell/tmp/zope-buildout/bin/buildout'.
   $ 

Once the bootstrapping is complete, you can execute the `bin/buildout` script which will configure the environment based on the configuration stored in `buildout.cfg`

Recipes
-------

Buildout uses recipes to install an configure the software. By default buildout can only install python eggs but using recipes as extension points allows bulidtout to install complex applications like `nginx`_ [#f2]_, `apache`_ [#f3]_ and `varnish`_ [#f4]_ and other useful software.




Regenerating Scripts
--------------------

To save time, you can run buildout in "offline" (-o) and non-updating (-N)
mode, which will prevent it from downloading things and checking for new
versions online::


 $ bin/buildout -No


Upgrading Software
------------------

Running buildout without any options causes it to check for new versions of software and regenerate based on changes made to the configuration files.

::

 $ bin/buildout


.. seealso::

   Project `Buildout <http://www.buildout.org/>`_
      The Buildout homepage
   PyPI `zc.buildout`_
      The Buildout PyPI entry


.. rubric:: Footnotes

.. [#f1] Standard buildout `directory layout <http://www.buildout.org/docs/dirstruct.html>`_
.. [#f2] `Nginx Recipe <http://pypi.python.org/pypi/gocept.nginx>`_
.. [#f3] `Apache Recipe <http://pypi.python.org/pypi/plone.recipe.apache/0.3.1>`_
.. [#f4] `Varnish Recipe <http://pypi.python.org/pypi/plone.recipe.varnish>`_


.. _`ez_setup.py`: http://peak.telecommunity.com/dist/ez_setup.py
.. _`bootstrap.py`: http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py
.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`setuptools`: http://peak.telecommunity.com/DevCenter/setuptools
.. _`apache`: http://www.apache.org
.. _`nginx`: http://wiki.nginx.org
.. _`varnish`: http://varnish.projects.linpro.no


