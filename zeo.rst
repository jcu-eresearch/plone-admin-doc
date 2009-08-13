ZEO Configuration
=================

Prerequisites
-------------

You need to install the following packages before running buildout:

Debian-based::


    sudo apt-get install libdb4.4-dev libsasl2-dev libssl-dev libldap python-ldap libldap2-dev libxslt1.1 libxslt1-dev python-libxslt1 python2.4-dev python2.4 python-imaging zlib1g-dev logrotate


Red Hat-based::


    sudo yum install db4 db4-devel cyrus-sasl-ldap cyrus-sasl-devel openssl-devel openldap-devel libxslt libxslt-devel libxslt-python logrotate python-devel


Install
-------

Instructions under this section will install ZEO under the directory::


  /srv/zeo


Running as the '''zope''' user (as configured in the {{{buildout.cfg}}} file).  

The script for running the server is located at::


  /etc/init.d/zeo


Now, you need to run::


 $ python2.4 bootstrap.py


This will install zc.buildout for you.

To install the versions of ZEO run, on RedHat you will require the 
python-devel package.

::

 $ bin/buildout


The ZEO instances control scripts are all located in the bin directory. 
Running the following command will run as the effective user zope.

::

 $ bin/zeo-arcs start


Regenerating Scripts
--------------------

To save time, you can run buildout in "offline" (-o) and non-updating (-N)
mode, which will prevent it from downloading things and checking for new
versions online::


 $ bin/buildout -No


Upgrading Software
------------------

::

 $ bin/buildout

