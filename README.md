# Python Users Group Singapore

This is source repository for [pugs.org.sg](http://pugs.org.sg). We use [pelican](http://docs.getpelican.com/) to build the site. 

The site is hosted on Netlify, a deployment will be triggered simply by pushing a commit into the master branch.

The build command is `make publish`.

The devserver command is `make devserver`

## How to contribute

1. Fork and clone
1. Don't forget `git submodule init` and `git submodule update`
1. Install pelican if needed (`pip install -r requirements.txt`)
1. Add new content (`markdown`) or fix styling or templates in `theme`
1. Check the result: `make html`, `make devserver`, `http://localhost:8000`
1. Publish: `make ghp`
