---
title: "Myth #6: Rails only speaks English"
date: 2008-11-17
url: https://dhh.dk/posts/35-myth-6-rails-only-speaks-english
slug: myth-6-rails-only-speaks-english
word_count: 645
---


It used to be somewhat inconvenient to deal with UTF-8 in Rails because Ruby's primary method of dealing with them was through regular expressions. If you just did a naïve string operation, you'd often be surprised by results and think that Ruby was somehow fundamentally unable to deal with UTF-8.


Take the string "Iñtërnâtiônàlizætiøn". If you were to do a string[0,2] operation and expected to get the two first characters back, you'd get "I\303" because Ruby operated on the byte level, not the character level. And UTF-8 characters can be multibyte, so you'd only get 1.5 characters back. Yikes!


Rails dealt with this [long ago](http://weblog.rubyonrails.org/2007/1/19/rails-1-2-rest-admiration-http-lovefest-and-utf-8-celebrations) by introducing a [character proxy](http://api.rubyonrails.org/classes/ActiveSupport/Multibyte/Chars.html) on top of strings that is UTF-8 safe. Now you can just do s.first(2) and you'll get the two first characters back. No surprises. Everything inside of Rails uses this, so validations, truncating, and what have you is all UTF-8 safe.


Not only that, but we actually assume that all operations are going to happen with UTF-8. The default charset for responses sent with Rails is UTF-8. The default charset for database operations is UTF-8. So Rails assumes that everything coming in, everything going out, and all that's being manipulated is UTF-8.


This is a long way of saying that Rails is perfectly capable of dealing with all kinds of international texts that can be described in UTF-8. The early inconveniences of Ruby's regular expression-based approach has long been superseded. You need no longer worry that Rails doesn't speak your language. Basecamp, for example, has content in some 70+ languages at least. It works very well.


**But what about translations and locales?**

It was long a point of contention that Rails didn't ship with a internationalization framework in the box. There has, however, long been a wide variety of plugins that added this support. There was localize, globalize, and many others. Each with their own strengths and tailored to different situations.


All these plugins have powered Rails applications in other languages than English for a long time. Some made it possible to translate strings to multiple languages, others just made Rails work well for one other given language. But whatever your translation need was, there was probably a plugin out there that did it.


But obviously things could be better and with Rails 2.2 we've made them a whole lot more so. Rails 2.2 ships with [a simple internationalization framework](http://www.artweb-design.de/2008/7/18/the-ruby-on-rails-i18n-core-api) that makes it silly easy to do translations and locales. There's a dedicated [discussion group](http://groups.google.com/group/rails-i18n), [wiki](http://rails-i18n.org/wiki), and [website](http://rails-i18n.org/) for getting familiar with this work. I've been using it in a test with translating Basecamp to Danish and really like what I'm seeing.


So in summary, Rails is very capable of making sites that need to be translated into many different locales. Before Rails 2.2, you'd have to use one of the many plugins. After Rails 2.2, you can use what's in the box for most cases (or add additional plugins for more exotic support).


**Don't forget about time zones!**

Dealing well with content in UTF-8 and translating your application into many languages goes a long way to make your application ready for the world, but most sites also need to deal with time. When you deal with time in a global setting, you also need to deal with time zones.


I'm incredibly proud of the outstanding work that Geoff Buesing lead for the implementation of time zones in Rails 2.1. It's amazing how Geoff and team were able to reduce something so complex to something so simple. And it shows the great power of being an full-stack framework. Geoff was able to make changes to Rails, Action Pack, and Active Record to make the entire experience seamless.


To lean more about time zones in Rails, see [Geoff's tutorial](http://mad.ly/2008/04/09/rails-21-time-zone-support-an-overview/) or watch [the Railscast on Time Zones](http://railscasts.com/episodes/106"").


*See the [Rails Myths](29-the-rails-myths.html) index for more myths about Rails.*

