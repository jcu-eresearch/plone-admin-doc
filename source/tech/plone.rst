
Plone
=====

Plone an open-source :abbr:`CMS` and is built using the `Python <http://python.org>` programming language.  It runs upon the Zope application layer.  Plone the core application this set of documentation focuses on.  Despite this fact, most of the documentation actually focusses on the surrounding frameworks or dependencies that we have on our Plone systems.  The good news about this is that the core of Plone itself is battle-tested by the large community it has.

About Plone
-----------

See the :doc:`Introduction <intro>` to this documentation for more information about what Plone is and what it can do.

Set Up Procedure
----------------

#) Set up standard environment (see :doc:`SOE <../system/soe>`)
#) Install Virtualenv (see :doc:`Virtualenv <virtualenv>`)
#) Read up on what Buildout is (see :doc:`Buildout <buildout>`)
#) Set up Zeo database service (using buildout; see :doc:`Zeo <zeo>`)
#) Set up Zope instance (using buildout; see :doc:`Zope <zope/index>`).  The given buildout configuration installs the Plone CMS at the same time.

Creating a Plone site
---------------------

#) Start Zope using the instance script ``bin/instance fg``, to start the service in the forground
#) Look in the console output for what the server address is.  It will likely be something like ``localhost:8080``.  
#) Open this URL in your browser.  You should be greeted with the 'Zope Quickstart' page if you're using Plone 3, or a Plone installation page if Plone 4.

   #) If Plone 4, follow the instructions.
   #) If Plone 3, append ``manage`` to the end of the URL.  You should be prompted for your username and password.  Enter them now.
   #) Click onto the large drop-down menu next to the 'Add' button, and locate 'Plone site' in this listing.  Click it.
   #) Enter the relevant details (site ID, title, and so forth).  Everything but the actual site ID can be changed later, so take care with this property.
   #) You should notice a lot of messages flying past in the console output; your Plone site will be installed shortly.
   #) When done, you can now go to visit your new site.  If you chose the ID ``foo`` for your site, then the address will be something like `http://localhost:8080/foo`.  
   #) Start configuring away!

This address for your site isn't permanent by any means.  You can do any of the following:

 * Put a domain name against this site
 * Virtual-host the site behind another web server
 * Use the :abbr:`VHM (Virtual Host Monster)` with a special address to make the site work with any existing URL structure.  See `How VHM Works <http://plone.org/documentation/kb/plone-apache/vhm>` for more details.

Customise a Plone site
----------------------

Finally...
----------

Consider theming with :doc:`Deliverance <deliverance>`.
