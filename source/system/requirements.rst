.. index::
    single: CMS
    single: Requirements

System requirements
===================

The following are are a suggested set of system requirements for operating one or more instances of the Plone :term:`CMS`. 

Hardware
--------

Minimum
^^^^^^^

 * Dual-core CPU (or similar)
 * 2 GB RAM
 * 5 GB HDD space for OS, 5 GB for Plone and database
 * 1 shared, public IP address (for at least HTTP hosting)
 * Linux-based OS (Centos/RHEL or Ubuntu/Debian; no preference/host dependent)
 * SSH access, ability to communicate with administrator for package installs
 * Open ports required:

    * *External:* 22 (SSH), 80 (HTTP)
    * *Internal/localhost:* 6081 (Varnish), 8080 (Zope/Plone), 8081 (Zeo)

Recommended
^^^^^^^^^^^

 * 2+ Dual-core CPU (or similar)
 * 2+ GB RAM
 * 5+ GB HDD space for OS, 20+ GB for Plone and database
 * 1 dedicated, public IP address (for HTTP hosting and SSL/HTTPS hosting)
 * Linux-based OS (Centos/RHEL or Ubuntu/Debian; no preference/host dependent)
 * SSH access, root or sudo access for package installs on the system
 * Open ports required:

    * *External:* 22 (SSH), 80 (HTTP), 443 (HTTPS)
    * *Internal/localhost:* 6081 (Varnish), 8000 (Deliverance), 8080 (Zope/Plone), 8081 (Zeo)

Notes on Operating Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^

Keep in mind that whilst other operating systems and architectures can run Plone/Zope/Python, the recommended enviornment is always a Linux-based environment.  Typically, Linux-based OSes are free to install, packages are readily available for software dependencies, and generally, other Plone developers use the same type of environment.  You are able to run Plone on platforms like Microsoft Windows and Apple Mac OS X and it will likely work well, but, put simply, some of what we do (for example, patches for optimal use) will not run.


Networking
----------

As with any given web-based service, your system requires direct access to the Internet or your organisation's Intranet, if that's the given use case.  The relevant firewalls, networking, and associated configuration will be different depending on the organisation hosting the service and where the physical hardware is located.  If you have any questions regarding networking-related issues, you should contact your relevant systems administrator.  Otherwise, contact your IT helpdesk and they should be able to point you in the right direction.

As an overview, however, your system or systems should be running:

 * A front-end webserver, such as Apache or nginx
 * Plone/Zope as the main application layer
 * Optionally, Zeo as the backend database (not always required on smaller sites)

You may also have some of the following:

 * Deliverance (or collective.xdv present) to theme the Plone site using a static theme and a transformation
   ruleset.
 * Varnish, a caching web accelerator, which aims to reduce the number of requests of the backend Plone as 
   possible by serving static content (images, pages, files) where possible.
 * Haproxy, or similar, as a load-balancing technology, for sites where multiple backends of Zope/Zeo are 
   required.

Notes on networking
^^^^^^^^^^^^^^^^^^^

As with any web-based service, your clients will need to be able to connect to the sites that you are operating.  This involves ensuring that network connectivity is working end-to-end.  In the case of an Intranet site, then your local network may well be set up already to facilitate the connection from your users' desktop computers.  Depending on your network, however, you may need to get your system administrator to open certain firewall ports.

In the case of an Internet site, you will need to ensure that you have at least a single externally-visible IP address and that the relevant ports required are going to be forward through your organisation's firewall.  In the most comlete example, you should have ports 80 and 443 forwarded through to your host machine for HTTP and HTTPS (SSL) access respectively.  If your site is to use HTTPS, then you require a dedicated public IP address and you should also seek a :abbr:`CA (Certificate Authority)`-signed certificate for use for the given domain.

Service Diagram
---------------

An example system layout might be the following:

.. image:: ../resources/service-diagram.pdf
   :width: 300pt

In this diagram, the typical port allocations are detailed beneath the relevant service name.  Also, please note that this is just a general overview of the system and doesn't being to take into account aspects like where these services should physically reside or similar points.  In this example, the services could live all on one virtual machine, or could be spread across five or more physical computers.
