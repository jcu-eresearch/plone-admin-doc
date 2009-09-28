Standard Operating Environment
==============================

.. sectionauthor:: Russell Sim <russell.sim@arcs.org.au>

Service Operation
-----------------

Starting/Stopping and Restarting should all happen using the systems buitin services implementation.

::

   $ /etc/init.d/zope
   Usage: /etc/init.d/zope {start|stop|restart|reload|status}

   $ /etc/init.d/zeo
   Usage: /etc/init.d/zeo {start|stop|restart|reload|status}


Effective Users
---------------

In the case of development machines the services should be running as the branch name from git. Production services run as the user ``zope``.


Directory Layout
----------------

+------------------+---------------------------------+
| Directory        | Purpose                         |
+==================+=================================+
| ``/opt``         | Used to store software installs |
+------------------+---------------------------------+
| ``/srv``         | Used to store data              |
+------------------+---------------------------------+
| ``/var/log/``    | Log file Directory              |
+------------------+---------------------------------+
| ``/etc/init.d/`` | Service control scripts         |
+------------------+---------------------------------+

