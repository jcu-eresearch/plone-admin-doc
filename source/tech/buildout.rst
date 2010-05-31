Buildout
========

About
-----

Buildout is an advanced deployment system that is typically used for deploying Python applications.  In the instance, buildout is used to deploy the Plone CMS, being built upon a Zope environment. Buildout leverages existing Python tools like `ez_setup.py`_ and `setuptools`_ to create complex reproducible installs of complex systems.  Essentially, this means that a small set of configuration files are stored in a code repository (for example, `Subversion` or `git`) and these can be checked-out and built on almost any computing environment.  There are some reservations about making a statement like `our software can run on any computer`, but any mainstream set of computing hardware (Intel or AMD-based), with a reasonably mainstream OS (Windows, Mac, Linux) should be able to run buildout.

Why?
----

We use buildout for a variety of reasons:

 * It is the prescribed method to install and set up Plone/Zope environments
 * It makes life easier as package dependencies can be automatically installed
 * Configuration files are light-weight, easily understood and quick to modify
 * The system is entirely extensible, with hundreds of recipes (add-ons) being available
 * Buildouts integrate well with source-code repositories for branching and merging for custom configurations
 * It's *miles* better than having to manually install software or build anything from source!

Quick primer
------------

Buildout utilises one or more :file:`{x}.cfg` configuration files.  These start with a `[buildout]` directive and then continue on to define what Python packages it should download and where from, how to build certain aspects of your system, and essentially wiring things together.  Buildout can be used to build non-Python applications too, as buildout can run arbitrary, system-level commands.  At a general overview, think of buildout as being similar to a Makefile, except that it's much more intelligent when it comes to your Python applications and Python egg packages.

Best practices
--------------

Don't worry if you don't understand everything that's written here, it'll become clear soon enough.  Here are some best practices for using Buildout: 

 * Create buildouts and customisations in a test environemnt first and test thoroughly to avoid any problems when putting them into production.

     * This is occassionally troublesome if your desktop environment is a different distribution to the one being run on your production environment.  For example, there are slightly different system-level packages needed for Ubuntu/Debian compared to Red Hat/CentOS.
     * However, using a Python virtual-env (Virtual Environment) will typically resolve any issues.  See the section about :doc:`virtualenv <virtualenv>`

 * Make any changes to buildouts on your local machine (through commands like ``git commit`` and ``git push``) and then pull them onto the production VM (``git pull``).  These commands may be different if you happen to be using subversion or another version control system.

     * This ensures that all changes are backed up to git in case of failures.

 * Try and manage your environment through buildout, as much as humanly possible.

     * This reduces the manual changes that are required elsewhere and allows for the buildout to be moved to other servers, locations, or other operating systems with ease.
     * If adding products to buildouts, attempt to find or use eggified products, when possible.  These days, most products are available in egg form.  If they're not, then in all liklihood, you either can't use them or you shouldn't be using them since they'll be well out of date.

 *  *Use a local server to serve products and python packages, where possible.*  At the time of writing, the best manner in which to do this is to set up a `collective.eggproxy`_ server, and point the buildout at this.  Any requests for Python eggs go through the proxy, which caches them accordingly.  Processing times are significantly reduced for subsequent buildouts.

     * This will save your internet quota, and increase the speed at which you can run and re-run the buildout process.
     * It also means that package donloads are *automatic*, so you shouldn't need to do anything after starting the server.  Coincidentally, the `collective.eggproxy`_ setup should be carried out with a buildout as well.  Read the fine manual to see how eggproxy works.

More information
----------------

See the `Buildout`_ website.

.. seealso::

   `ez_setup.py <http://peak.telecommunity.com/dist/ez_setup.py>`_
       Script for setting up easy_install
   `Setuptools <http://pypi.python.org/pypi/setuptools>`_
       The setuptools homepage
   `collective.eggproxy <http://pypi.python.org/pypi/collective.eggproxy>`_
       A proxy server used to maintain an intelligent mirror of PyPI packages.
   `Buildout <http://www.buildout.org>`_
       Home page of the Buildout project 
