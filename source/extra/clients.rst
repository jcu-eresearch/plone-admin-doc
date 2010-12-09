Working with users
==================

As a developer, remember that the users are who will be the ones keeping you in a job. Listen to them, and strive to be happy through their many questions, and seek to meet their requirements in the best possible way.

Here's some friendly suggestions on how to take care of users and point them in the right direction:

 * First, consider if you should be the one answering their given question or questions.  Most collaborative sites should have their own site administrator whom users should be contacting.  Otherwise, if the site has been implemented in a university environment, then their help desk may be the suitable contact.  If the site you're answering questions about is one such site, then direct the user to contact their site administrator first.  Don't be shy about it -- odds are that you're busy!

      * If the site doesn't have an administrator, consider getting someone to be one.  Unless it's actually in your job description to run user support for a client, you shouldn't need to be.
      * Check if the user has looked at the Plone Help site yet (this site).  If not, direct them to it, as it'll probably answer their question.  If it doesn't, then consider answering their request by way of creating a new FAQ page and sending them to that.
      * Otherwise, if it's a technical question that's coming your way, then it's probably yours, so jump to it.

 * Make sure you ask them for all relevant information.  It's no use trying to troubleshoot a Plone problem if someone says "I can't access the site" or "it says there's an error message". Try and ask the following:

      * What was the error message, or what were you doing when it happened?
      * Is the problem site-wide or just in one specific area?
      * If it's access trouble, can you access the site from another computer or do any pages load at all?

 * If a site is using LDAP or another external authentication method and a user used to be able to log in and now can't, it's probably because that service has changed, not our site.  It's always a possibility some underlying system issue may be causing it, but for the most part, it will likely be the user isn't authenticating with the right credentials.  Test the site yourself, and if you have no troubles, then direct the user to their relevant help desk for assistance.

      * The point mentioned above applies to database-connected Plone/Zope instances as well.  For example, if your Plone instance integrates with an Oracle or other relational database, and you immediately start receiving errors, then consider whether it could be likely that database that changed.  This is the life of working with systems beyond our control.


