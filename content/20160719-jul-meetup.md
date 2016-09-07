Title: July 2016 meetup
Slug: 2016-jul-meetup
Author: Ivan
Date: 2016-09-07
Category: meetings
Tags: dev-practice

[postfactum]

# Talk

**Hear no evil, see no evil, patch no evil: Or, how to monkey-patch safely**.

By [Graham Dumpleton](http://www.dscpl.com.au)

*Abstract*:

Python is a dynamic programming language and has a strong tradition of adhering
to a programming style called duck-typing. This means that it is possible to
easily modify an application's code while it is running. One might wish to do
this for various reasons, including enhancing the functionality of code,
correcting errant behaviour, or adding instrumentation or debugging code.

Making such code modifications can be tricky though and not done correctly can
potentially interfere with the operation of the original code, through
destroying introspection abilities, not honouring the duck-typing mantra or due
to being applied at the wrong time.

If you do need to do monkey patching though, the 'wrapt' library is your friend,
with its transparent object proxy wrappers and post import hook mechanism, it
allows you to safely monkey patch code to modify its behaviour.

Come learn about the 'wrapt' library and the joys, but also the dangers, of
monkey patching.

*Speaker*: Graham is the author of mod_wsgi, a popular module for hosting
Python web applications with the Apache HTTPD web server. He has a keen
interest in Docker and Platform as a Service (PaaS) technologies, and is a
Fellow of the Python Software Foundation and Member of the Apache Software
Foundation. He is currently a developer advocate for OpenShift at Red Hat.

----

[meetup page](https://www.meetup.com/Singapore-Python-User-Group/events/232538900/),
[video](https://engineers.sg/video/hear-no-evil-see-no-evil-patch-no-evil-singapore-python-user-group--911) (thanks [engineers.sg](https://engineers.sg)).

Thanks again to [PayPal](https://www.paypal.com/sg) for hosting.
