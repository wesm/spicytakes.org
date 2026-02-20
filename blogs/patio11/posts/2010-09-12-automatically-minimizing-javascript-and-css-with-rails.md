---
title: "Automatically Minimizing Javascript and CSS with Rails"
date: 2010-09-12
url: https://www.kalzumeus.com/2010/09/12/automatically-minimizing-javascript-and-css-with-rails/
slug: automatically-minimizing-javascript-and-css-with-rails
word_count: 86
---


If you obsess over your YSlow and/or Page Speed performance scores, you might be wondering how to get your Rails app to automatically crunch Javascripts and CSS files without actually requiring cumbersome rake tasks to be repeated during every deploy.  Fear not: you can quickly monkeypatch Rails to do this.

1. Copy [this gist](http://gist.github.com/7176) into your lib/ directory.
2. Create a config/initializers/javascript_minimization.rb as described [here](http://davetroy.blogspot.com/2007/12/automatic-asset-minimization-and.html).
3. Use your javascript_include_tag and stylesheet_include_tag helpers as normal, with the caching option turned on.
4. Watch your users save 100kb.
