Python Users Group Singapore
============================

This is source repository for [pugs.org.sg](http://pugs.org.sg). We use [pelican](http://docs.getpelican.com/) to build the site which is hosted on [GitHub pages](http://pages.github.com/).


How to contribute
-----------------

1. Fork and clone
2. Install pelican if needed (`pip install -r requirements.txt`)
3. Add new content (`markdown`) or fix styling or templates in `theme`
4. Check the result: `make html`, `make devserver`, `http://localhost:8000`
5. Publish: `make ghp`
