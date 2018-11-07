# Python Users Group Singapore

This is source repository for [pugs.org.sg](http://pugs.org.sg). We use [pelican](http://docs.getpelican.com/) to build the site which is hosted on [GitHub pages](http://pages.github.com/).

## How to contribute

1. Fork and clone
1. Don't forget `git submodule init` and `git submodule update`
1. Install pelican if needed (`pip install -r requirements.txt`)
1. Add new content (`markdown`) or fix styling or templates in `theme`
1. Check the result: `make html`, `make devserver`, `http://localhost:8000`
1. Publish: `make ghp`
