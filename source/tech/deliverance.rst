Diazo (collective.xdv) and Deliverance
======================================

Important note
--------------

Deliverance is no longer being supported as 'the' advanced theming method for Plone.  Diazo (formerly ``collective.xdv``) implements essentially what Deliverance does, but within Zope itself as a post-production hook.  By doing this, we reducing the need to hack options together, get more support from the community, and only need to run a single, seamless sevice.

Any references from this point onwards to Deliverance should essentially apply to Diazo as well.  Diazo works with tiny differences in rule syntax and configurations, but does exactly the same job (and occasionally, a lot more than Deliverance!).

About these tools
-----------------

Deliverance is a middleware application that can theme web applications against a static (X)HTML theme.  The benefit of using Deliverance over traditional theming techniques is that Deliverance is universal and works with any web-based output.  Using a set of transformation rules, Deliverance can move and maniuplate content from a web page or application into areas of a static theme.  

So, for example, you could have a corporate web template or professionally-created page design and apply this to an application like Plone with just a few XML-based rules.  This technique isn't just tied to Plone, however.  You could put Deliverance in front of Joomla, Drupal, Wordpress, RT, or essentially anything else that involves HTML or XHTML!  

Although in its infancy, Deliverance will likely prove to be an essential too in maintaining uniformity of branding across separate applications and web services.

Install
-------

The easiest way to get started with Deliverance is using Virtualenv.  For more information on Virtualenv, see the previously-covered :doc:`Virtualenv documentation <virtualenv>`.

::

   $ virtualenv deliverance
   $ cd deliverance
   $ . ./bin/activate
   $ mkdir src
   $ cd src
   $ svn co http://codespeak.net/svn/z3/deliverance/trunk/ deliverance
   $ cd deliverance
   $ python setup.py develop
   $ cd ../..

Creating a Deliverance configuration
------------------------------------

If you have PasteScript installed you should now be able to run::

   $ paster create --list-templates

To get a list of all the available templates.::

   Available templates:
     archetype:                 A Plone project that uses Archetypes
     basic_namespace:           A project with a namespace package
     basic_package:             A basic setuptools-enabled package
     deliverance:               Basic template for a deliverance-proxy setup
     deliverance_plone:         Plone-specific template for deliverance-proxy

Using paster we can now create a basic Deliverance theme::

   $ paster create -t deliverance_plone dplone
   .....
   $ cd dplone

Operation
---------

Once the templates have been generated we can execute Deliverance with::

   $ deliverance-proxy etc/deliverance.xml

Keep in mind that this command runs in the foreground.  You can use ``Control-Z``, and then ``bg`` to put the command into the background (or else execute the command with an ampersand [&])

This process will become better and more fully daemonised in the future as the Deliverance project becomes more active.

Editing rules
-------------

As mentioned earlier, Deliverance operates with a set of XML-based rules in order to transform content from a page into a theme.  This configuration file is the ``deliverance.xml`` file that was generated earlier.  Due to Deliverance currently existing at version 0.3, the available rules that you can use may change.  hence, you should refer to the `Deliverance documentation` for more information.  Suffice to say that you should be able to ``<append>``, ``<prepend>``, ``<drop>``, ``<replace>`` existing content from your web application and/or your theme.

Working with your theme
-----------------------

Your theme file should be a collection of static files that you can serve out to the world.  One of these files needs to be a HTML or XHTML theme file, and this file should be representative of the design you want for your site.  For example, if we wanted the corporate ARCS design on our pages, then we would obtain the HTML-based theme and use that.  

You can also point your Deliverance instance directly at an web page and use that as the theme.  Keep in mind that if the target site isn't under your total control, its structure may change, breaking your Deliverance configuration.  Because of this, the best practice is to serve the theme manually from a local location to the themed site.  In most cases, this will be the optimal solution anyway.

.. seealso::

   `Deliverance <http://deliverance.openplans.org/>`_
      The Deliverance homepage
   `Deliverance documentation <http://packages.python.org/Deliverance/index.html>`_
      Documentation for the operation and configuration of Deliverance


