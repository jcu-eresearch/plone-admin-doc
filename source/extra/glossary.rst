
.. _glossary:

Glossary
================

.. glossary:: 
    :sorted:

    .. comment:

    This file will be sorted automagically during formatting.
    Graciously borrowed the documentation from the Plone.org site.

    instance
        This is the actual Zope instance program.

    CMS
        Acronymn for 'Content Management System'.  Plone itself is an example of a CMS.

    Workflow
        Workflow is a very powerful way of mimicking business processes — it is also the way security settings are handled in Plone. 

    Acquisition
        Simply put, any Zope object can acquire any object or property from any of its parents. That is, if you have a folder called A, containing two resources (a document called homepage and another folder called B), then an URL pointing at http://.../A/B/homepage would work even though B is empty. This is because Zope starts to look for homepage in B, doesn't find it, and goes back up to A, where it's found. The reality, inevitably, is more complex that this. For the whole story, see the Acquisition chapter in the Zope Book. 

    Archetypes
        Archetypes is a framework designed to facilitate the building of applications for Plone and CMF. Its main purpose is to provide a common method for building content objects, based on schema definitions. Fields can be grouped for editing, making it very simple to create wizard-like forms. Archetypes is able to do all the heavy lifting needed to bootstrap a content type, allowing the developer to focus on other things such as business rules, planning, scaling and designing. It provides features such as auto-generation of editing and presentation views. Archetypes code can be generated from UML using ArchGenXML.

    Catalog 
        The catalog is an internal index of the content inside Plone so that it can be searched. The catalog object is accessible through the ZMI as the portal_catalog object.

    CSS - Cascading Style Sheets

        Cascading Style Sheets is a way to separate content from presentation. Plone uses this extensively, and it is a web standard documented at the W3C web site. If you want to learn CSS, we reccommend the W3Schools CSS Resources and the SitePoint CSS Reference.

    Document 
        A document is a page of content, usually a self-contained piece of text. Documents can be written in several different formats, plain text, HTML or (re)Structured Text. The default home page for a Plone site is one example of a document.

    DTML
        Document Template Markup Language. DTML is a server side templating language earlier used to produce dynamic pieces of content, but is now superceded by ZPT for HTML and XML content. It is still used sparingly for non-XML content like SQL and mail/CSS.

    Expiration Date
        The last day an item should show up in searches, news listings etc. Please note that this doesn't actually remove or disable the item, it merely makes it not show up in searches.

    i18n
        i18n is shorthand for "internationalization" (the letter I, 18 letters, the letter N) - and refers to the process of preparing a program so that it can be used in multiple languages without further altering the source. Plone is fully internationalized.

    KSS - Kinetic Style Sheets
        KSS, Kinetic Style Sheets, is a client side framework for implementing rich user interfaces with AJAX funtionalities. AJAX makes the pages in the browser behave more like an application: instead of loading or reloading a web page, the client can contact the server and recieve information from it, and can change the content or lookout of the currently viewed page without leaving it. KSS enables the building of such interfaces without knowing Javascript.
    
    Kupu
        Kupu is the user-friendly graphical HTML editor component that is bundled with Plone, starting with version 2.1. 

    l10n
        Localization is the actual preparing of data for a particular language. For example Plone is i18n aware and has localization for several languages. The term l10n is formed by the first and last letter of the word and the number of letters in between.

    Layer
        A layer is a set of templates and scripts that get presented to the user. By combining these layers, you create what is referred to as a skin. The order of layers is important, the topmost layers will be examined first when rendering a page. Each layer is an entry in 'portal_skins' -> 'Contents', and is usually a Filesystem Directory View or a Folder.

    LDAP
        Lightweight Directory Access Protocol. An internet protocol which provides a specification for user-directory access by wire, attribute syntax, representation of distinguished names, search filters, an URL format, a schema for user-centric information, authentication methods, and transport layer security. Example: an email client might connect to an LDAP server in order to look up an email address for a person by a person's name.

    Manager
        The Manager Security role is a standard role in Zope. A user with the Manager role has ALL permissions except the Take Ownership permission. Also commonly known as Administrator or root in other systems.

    OpenID
        A distributed identity system. Using a single URI provider an individual is able to login to any web site that accepts OpenID using the URI and a password. Plone implements OpenID as a PAS plug-in.
    
    PAS
        The Pluggable Authentication Service (PAS) is a new framework from Zope Corp. for handling authentication in Zope 2. PAS is a Zope acl_users folder object that uses "plugins" that can implement various authentication interfaces that plug into the PAS framework. Zope 3 also uses a design inspired by PAS. PAS was integrated into Plone at the 2005 San Jose Sprint.

    Request
        Each page view by a client generates a request to Plone. This incoming request is encapsulated in a request object in Zope, usually called REQUEST (or lowercase "request" in the case of ZPT).

    reST (ReStructuredText)
        reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents. reStructuredText is designed for extensibility for specific application domains. The reStructuredText parser is a component of Docutils. reStructuredText is a revision and reinterpretation of the StructuredText and Setext lightweight markup systems.

    Skin
        A collection of template layers, is used as the search path when a page is rendered and the different parts look up template fragments. Skins are defined in the ZMI in portal_skins tool. Used for both presentation and code customizations.

    STX (Structured Text)
        Structured Text (aka. STX) is a simple markup technique that is useful when you don't want to resort to HTML for creating web content. It uses indenting for structure, and other markup for formatting. Has been superceded by reStructuredText, but a lot of people still prefer the old version, as it's easier to learn and more suited to simple documents. More information in the How-to section of plone.org.
    
    Syndication
        Syndication shows you the ten most recently updated objects in a folder in RSS format. This format is designed to be read by other programs.

    Traceback
        A Python "traceback" is a detailed error message generated when an error occurs in executing Python code. Since Plone, running atop Zope, is a Python application, most Plone errors will generate a Python traceback. If you are filing an issue report regarding a Plone or Plone-product error, you should try to include a traceback log entry with the report. To find the traceback, check your event.log log file. Alternatively, use the ZMI to check the error_log object in your Plone folder. A traceback will be included with nearly all error entries. A traceback will look something like this: "Traceback (innermost last): ... AttributeError: adapters" They can be very long. The most useful information is generally at the end.

    TTP
        Actions done TTP are performed "Through the Plone" interface. It is normally a lazy way of telling you that you should not add things from the ZMI, as is the case for adding content, for example.

    TTW
        This is a general term meaning an action should be performed "Through The Web," as opposed to, say, being done programmatically from a Python script. This a method of developing or otherwise customising Plone. Whilst it may be easier to make changes to sites TTW, for any major development efforts or theming, these sets of programming should be applied using a file system product.
    
    UML
        UML (Unified Modeling Language) is a general-purpose modeling language that includes a standardized graphical notation used to create an abstract model of a system, referred to as a UML model. With the use of ArchGenXML, this can be used to generate code for CMF/Plone applications (Products) based on the Archetypes framework. 

    ZMI
        Zope Management Interface Zope has a built in Management Interface that is accessible through the web. Accessing is as simple as adding /manage on to the end of your URL, for example: http://localhost/manage - or visiting Plone Setup and clicking the Zope Management Interface link (Click 'View' to go back to the Plone site). Be careful in there, though - it's the "geek view" of things, and is not straightforward, nor does it protect you from doing stupid things. :)

    ZODB
        ZODB is the Zope Object Database, which is where your content is normally stored when you are using Plone. On the file system, this database is contained in the file "Data.fs", normally located in the "var" directory.
    
    ZPL
        Zope Public License, a BSD-style license that Zope is licensed under.
    
    ZPT - Zope Page Templates
        Zope Page Templates is the templating language that is used to render the Plone pages. It is implemented as an XML namespace, and lives inside the attributes of a tag, making it possible to create templates that look like normal HTML/XML to editors.


    ATCT
        ATContentTypes - the new content types written with Archetypes which replaces the default CMF content types in Plone 2.1 onwards.

    Collective
        The Collective is a community code repository for Plone Products and other add-ons, and is a useful place to find the very latest code for hundreds of add-ons to Plone. Developers of new Plone Products are encouraged to share their code via the Collective so that others can easily find it, use it, and contribute fixes and improvements.

    PLIP
        PLone Improvement Proposal (just like Python's PEPs: Python Enhancement Proposals). These are documents written to structure and organise proposals for the improvement of Plone.

        Motivation, deliverables, risks and a list of people willing to do the work must be included. This document is submitted to the Framework Team, who reviews the proposal and decides if it's suitable to be included in the next Plone release or not.

    ResourceRegistries
        A piece of Plone infrastructure that allows CSS/Javascript declarations to be contained in seperate, logical files before ultimately being appended to the existing Plone CSS/Javascript files on page delivery. Primarily enables Product authors to "register" new CSS/Javascript without needing to touch Plone's templates, but also allows for selective inclusion of CSS/Javascript files and reduces page load by minimizing individual calls to seperate blocks of CSS/Javascript files. Found in the ZMI under "portal_css" and "portal_javascript".

    AGX
        AGX is short for ArchGenXML (see ArchGenXML's glossary entry).

    ArchGenXML
        ArchGenXML is a code-generator for CMF/Plone applications (Products) based on the Archetypes framework. It parses UML models in XMI-Format (.xmi, .zargo, .zuml), created with applications such as ArgoUML, Poseidon or ObjectDomain. A brief tutorial for ArchGenXML is present on the plone.org site.

    BBB - code marker in source code
        When adding (or leaving) a piece of code for backward compatibility, we use a BBB comment marker with a date.
    easy_install
        A command-line tool for automatic discovery and installation of packages into a Python environment. The easy_install script is part of the setuptools package, which uses the Python Package Index as its source for packages.

    METAL
        Macro Expansion Template Attributes Language

    Monkey patch
        A monkey patch is a way to modify the behaviour of Zope or a Product without altering the original code. Useful for fixes that have to live alongside the original code for a while, like security hotfixes, behavioural changes, etc. The term "monkey patch" seems to have originated as follows: First it was "guerilla patch", referring to code that sneakily changes other code at runtime without any rules. In Zope 2, sometimes these patches engage in battle with each other. This term went around Zope Corporation for a while. People heard it as "gorilla patch", though, since the two words sound very much alike, and the word gorilla is heard more often. So, when someone created a guerilla patch very carefully and tried to avoid any battles, they tried to make it sound less forceful by calling it a monkey patch. The term stuck.

    Namespace package
        A feature of setuptools which makes it possible to distribute multiple, separate packages sharing a single top-level namespace. For example, the packages plone.theme and plone.portlets both share the top-level "plone" namespace, but they are distributed as separate eggs. When installed, each egg's source code has its own directory (or possibly a compressed archive of that directory). Namespace packages eliminate the need to distribute one giant plone package, with a top-level plone directory containing all possible children, e.g. plone/theme and plone/portlets. 
    Python egg
        A way to package and distribute Python packages. Each egg contains a setup.py file with metadata (such as the author's name and email address and licensing information), as well as information about dependencies. setuptools, the Python library that powers the egg mechanism, is able to automatically find and download dependencies for eggs that you install. It is even possible for two different eggs to concurrently use different versions of the same dependency. Eggs also support a feature called entry points, a kind of generic plug-in mechanism. Much more detail is available at the PEAK website.

    Python package
        A general term describing a redistributable Python module. At the most basic level, a package is a directory with an __init__.py file and some Python code.

    Python Package Index
        The Python community's index of thousands of downloadable Python packages. It is available as a website to browse, with the ability to search for a particular package. More importantly, setuptools-based packaging tools (most notably, buildout and easy_install) can query this index to download and install eggs automatically. Also known as the Cheese Shop or PyPI.

    Python path
        The order and location of folders in which the Python interpreter will look for modules. It's available in python via sys.path. When Zope is running, this typically includes the global Python modules making up the standard library, the interpreter's site-packages directory, where third party "global" modules and eggs are installed, the Zope software home, and the lib/python directory inside the instance home. It is possible for python scripts to include additional paths in the Python path during runtime. This ability is used by zc.buildout.

    RAD
        Rapid Application Development - A term applied to development tools to refer to any number of features that make programming easier. Archetypes and ArchGenXML are examples of these from the Plone universe.

    Software home
        The directory inside the Zope installation (on the filesystem) that contains all the Python code that makes up the core of the Zope application server. The various Zope packages are distributed here. Also referred to as the $SOFTWARE_HOME environment variable. It varies from one system to the next, depending where you or your packaging system installed Zope. You can find the value of this in the ZMI > Control Panel.

    Sprint
         Based on ideas from the extreme programming (XP) community. A sprint is a three to five day focused development session, in which developers pair in a room and focus on building a particular subsystem. see http://plone.org/events/sprints

    TAL
        Template Attribute Language

    TODO - code marker in source code
        The TODO marker in source code record new features, non-critical optimization notes, design changes, etc.

    XXX - code marker in source code
        XXX is a marker in the comments of the source code that should only be used during development to note things that need to be taken care of before a final (trunk) commit. Ideally, one should not expect to see XXXs in released software. XXX shall not be used to record new features, non-critical optimization, design changes, etc. If you want to record things like that, use TODO comments instead. People making a release shouldn't care about TODOs, but they ought to be annoyed to find XXXs.

    ZCML
        Zope Configuration Markup Language. Zope 3 separates policy from the actual code and moves it out to separate configuration files, typically a 'configure.zcml' file in a buildout. This file configures the Zope instance. 'Configuration' might be a bit misleading here and should be thought or more as wiring. ZCML, the XML-based configuration language that is used for this, is tailored to do component registration and security declarations, for the most part. By enabling or disabling certain components in ZCML, you can configure certain policies of the overall application. In Zope 2, enabling and disabling components means to drop in or remove a certain Zope 2 product. When it's there, it's automagically imported and loaded. This is not the case in Zope 3. If you don't enable it explicitly, it will not be found. 

    ZEO server
        ZEO (Zope Enterprise Objects) is the load-balancing system used with Zope. The ZEO server is an storage server that allows multiple Zope instances, called ZEO clients, to connect to a single database. For additional info, see the related chapter in The Zope Book.

    Zope instance
        An operating system process that handles HTTP interaction with a Zope database (ZODB). In other words, the Zope web server process. Alternatively, the Python code and other configuration files necessary for running this process.

        One Zope installation can support multiple instances. Use the buildout recipe plone.recipe.zope2instance to create new Zope instances in a buildout environment.
        Several Zope instances may serve data from a single Data.fs using a ZEO server on the back-end.

    Zope product
        A special kind of Python package used to extend Zope. In old versions of Zope, all products were directories inside the special Products directory of a Zope instance; these would have a Python module name beginning with "Products". For example, the core of Plone is a product called CMFPlone, known in Python as Products.CMFPlone.


