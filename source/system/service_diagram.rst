
.. index::
    single: service
    single: diagram

.. _service-diagram:

Service Diagram
---------------

An example system layout might be the following:

.. image:: ../resources/service-diagram.pdf
   :width: 300pt

In this diagram, the typical port allocations are detailed beneath the relevant service name.  Also, please note that this is just a general overview of the system and doesn't being to take into account aspects like where these services should physically reside or similar points.  In this example, the services could live all on one virtual machine, or could be spread across five or more physical computers.

Keep in mind that not all services may be in use for any given installation of Plone.  If your site is smaller, or doesn't need multiple Zope instances connecting to your backend storage, then you may not be using Zeo.  Similarly, if your site is not being cache-accelerated, then you may not being using Varnish.
