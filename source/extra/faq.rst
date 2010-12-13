.. _faq:

FAQ
===

How do I...
-----------

.. _faq-easyinstall:
... install easy_install on a system with no packages for it?
   To install setuptools, download the bootstrap module `ez_setup.py <http://peak.telecommunity.com/dist/ez_setup.py>`_ and execute it as follows::
   
       $ python ez_setup.py

Keep in mind that you may need to run the above command with a specific 
Python version (for example, ``python2.4`` or ``python2.6``).  This will 
be entirely dependent on your host system and which version of Plone you 
are using. 

What not to do
--------------

There are a number of problems that can arise during the operation of Plone and Zope. Typically, the :abbr:`SOE (Standard Operating Environment)` that we utilise should reduce the number of potential issues you may encounter.  But, even with that said, Plone/Zope are still software products that may have bugs, no matter how well tested the systems are. The following ideas will constrain any issues that could potentially be caused:

 * Don't install products onto production sites without them having been thoroughly tested first.  This includes checking to see if the products successfully uninstall themselves afterwards and leave the given site    usable.  One such example is that of ZipFileTransport - someone wanted it, and it wasn't well tested first.

 * Don't delete the main webmaster account within the ZMI - this will disable administrator access to the Zope instance.  It's not all doom-and-gloom if you accidentally do it, however, but this will mean you have to go back in and recreate it from the command line.
   
 * Don't change properties, permissions, or otherwise for the webmaster account.  Chances are you'll be working locally on a site, so this applies to the site administrator account too.
           
 * Run pre-flight sanity checks as much as possible before reloading key services, such as httpd on the webserver.  In this specific case, be sure to run ``/etc/init.d/httpd configtest`` or ``service httpd configtest`` (or with ``apache2`` as the service, depending on OS) before reloading.

Buildout and Plone
------------------

There's a lot of little things that can make life simpler when dealing with buildout and Plone. The points listed here might save you a lot of time, because chances are someone's already had your problem.

 * Running the Zope process in the foreground is an excellent way of troubleshooting problems.  If you don't know already (you should!), then you can start your instance with the argument 'fg' instead of the normal 'start' (eg ``./bin/instance1 fg``).  Be sure to restart it normally when you're done, if it's a production system, or otherwise closing your terminal window will kill the foreground process.
   
 * ``ipython`` is quite a handy tool as well for being able to run commands, safely & without (much) fear on a production instance, even if it's still running.  Keep in mind that anything you do in an ipython session isn't saved until you run import transation and transaction.commit().  Otherwise, if you kill your ipython, any variable/changes/etc that you did will disappear (good and bad, depending on circumstance).  Check here for details: http://plone.org/documentation/how-to/setup-ipython-for-zope

     * In conjunction with ``ipython``, ``ipdb`` is an excellent replacement for the standard ``pdb`` debugger for Python code.  Install ``ipdb`` in your buildout and you can simply use it in the same manner as you would ``pdb``, such as ``import ipdb; ipdb.set_trace()`` to get a live, ipython-based debugger anywhere in your code.


