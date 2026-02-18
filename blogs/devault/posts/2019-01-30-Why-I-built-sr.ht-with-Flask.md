---
title: "Why I chose Flask to build sr.ht's mini-services"
date: 2019-01-30
url: https://drewdevault.com/2019/01/30/Why-I-built-sr.ht-with-Flask.html
slug: Why-I-built-sr.ht-with-Flask
word_count: 669
---

[sr.ht](https://sr.ht)  is a large, production-scale suite of web applications (I
call them “mini-services”, as they strike a balance between microservices and
monolithic applications) which are built in Python with
 [Flask](http://flask.pocoo.org/) . David Lord, one of the maintainers of Flask,
reached out to me when he heard about sr.ht and saw that it was built with
Flask. At his urging, I’d like to share the rationale behind the decision and
how it’s turned out in the long run.

I have a long history of writing web applications with Flask, so much so that I
think I’ve lost count of them by now - at least 15, if not 20. Flask’s
simplicity and flexibility is what keeps bringing me back. Frameworks like
Django or Rails are much different: they are the kitchen sink, and then some. I
generally don’t need the whole kitchen sink, and if I were given it, I would
want to change some details. Flask is nice because it gives you the basics and
lets you build what you need on top of it, and you’re never working around a
cookie-cutter system which doesn’t cut your cookies in quite the way you need.

In sr.ht’s case in particular, though, I have chosen to extend Flask with  [a new
module](https://git.sr.ht/~sircmpwn/core.sr.ht)  common to all sr.ht projects. After all, each service of
sr.ht has a lot in common with the rest. Some of the things that live in this
core module are:

* Shared jinja2 templates and stylesheets
* Shared rigging for  [SQLAlchemy](https://www.sqlalchemy.org/)  (ORM)
* Shared rigging for  [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [A little validation module](https://git.sr.ht/~sircmpwn/core.sr.ht/tree/master/srht/validation.py)  I’m very proud of
* API behavior, webhooks, OAuth, etc, which are consistent throughout sr.ht

The mini-service-oriented architecture allows sr.ht services to be deployed
ala-carte for users who only need a fraction of what we offer. This design
requires a lot of custom code to integrate all of the services with each other -
for example, all of the services use a single shared config file, which contains
both shared config options and service-specific configuration. sr.ht also uses a
novel approach to authentication, in which both user logins and API
authentication is delegated to an external service, meta.sr.ht, requiring
further custom code still. core.sr.ht additionally provides common SQLAlchemy
mixins for things like user tables, which have many common properties, but for
each service may have service-specific columns as well.

Django provides their own ORM, their own authentication, their own models, and
more. In order to meet the design constraints of sr.ht, I’d have spent twice as
long ripping out the rest of Django’s bits and fixing anything that broke in the
resulting mess. With Flask, these bits were never written for me in the first
place, which gives me the freedom to implement this design greenfield. Flask is
small and what code it does bring to the table is highly pluggable.

Though it’s well suited to many of my needs, I don’t think Flask is perfect. A
few things I dislike about it:

* First-class  [jinja2](http://jinja.pocoo.org/)  support is probably out of
scope.
* flask.Flask and flask.Blueprint should be the same thing.
* I’m not a fan of Flask’s approach to configuration. I have a better(?) config
module that I drag around to all of my projects.

And to summarize the good:

* It provides a nice no-nonsense interface for requests, responses, and routing.
* It has a lot of nice hooks for adding your own middleware.
* It doesn’t do much more than that, which means you’re free to choose and
compose other tools to make up the difference.

I think that on the whole it’s quite good. There are frameworks which are
smaller still - but I think Flask hits a sweet spot. If you’re making a
monolithic web app and can live within the on-rails Django experience, you might
want to use it. But if you are making smaller apps or need to rig things up in a
unique way - something I find myself doing almost every time - Flask is probably
for you.
