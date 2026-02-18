---
title: "Day 22: getting OAuth to work in Rails"
date: 2020-12-08
url: https://jvns.ca/blog/2020/12/08/day-22--getting-oauth-to-work-in-rails/
slug: day-22--getting-oauth-to-work-in-rails
word_count: 561
---


Today my goal was to set up OAuth login for a Rails project.


This was all pretty confusing because a) I don’t understand Rails yet and b) I
decided to use an authentication library called Devise on top of it that I also
don’t understand.


But one nice thing about Rails is that there are about 10 billion blog posts &
Stack Overflow questions that make it possible to figure out what’s going on
even if you don’t really know anything.


### following tutorials without understanding them is kind of fun (but doesn’t work, of course)


I found an extremely nice content marketing tutorial on the digital ocean blog called [How To Configure Devise and OmniAuth for Your Rails Application](https://www.digitalocean.com/community/tutorials/how-to-configure-devise-and-omniauth-for-your-rails-application)
explaining how to set up OAuth with Rails. I followed all the steps without really understanding them and it kind of worked! Hooray.


This worked mostly fine when setting up GitHub login, but I also needed to
implement a custom OAuth provider (for the Recurse Center OAuth), and so I
learned a few things while fixing the bugs with that. Here they are.


### it’s important to request the user’s information from the OAuth provider


I was just using OAuth for login, not to access an API, and (based on a very
sketchy understanding of how OAuth works) I had this vague notion that once the
OAuth server sent my application an access token, it would be “done”.


But I’d copied this [template for creating a custom Omniauth provider from the docs](https://github.com/omniauth/omniauth-oauth2) and filled in all the
fields, and it didn’t work!


It turns out that I’d misunderstood this line of code:


```
access_token.get('/me')

```


which I thought meant “get the `/me` field from a hashmap called
`access_token`” but which *actually* means “make an HTTP request to the OAuth
provider’s API using the access token, and get the path `/me`”. This is where
the user’s name / email address / etc comes from, so it’s pretty important to
get right.


I’d gotten the path wrong (since I didn’t realize it was a HTTP request at
all!), and fixing the path made my OAuth integration work.


### you need to set the `X-FORWARDED-PROTO` header to `https`


In OAuth, you need to send a `redirect_uri` to the OAuth provider (eg GitHub)
with the URL of the page on your site to go back to.


In my case, this `redirect_uri` was supposed to be
`https://mysite.com/users/auth/github/callback`. But my application was sending
a `http` URL instead of an `https` URL. What? Why?


It turns out that something in Rails (I’m still not sure what honestly) looks
at the `X-FORWARDED-PROTO` header from nginx to decide whether to build `https`
or `http` links. My site was behind a Cloudflare proxy, so the requests coming
into the site were all HTTP requests, and so my app thought `http://...` was
the correct URL to use.


But it was not!!!


I added a


```
proxy_set_header X-FORWARDED-PROTO https; 

```


and everything was fixed.


### tomorrow: maybe stop using devise?


Originally I thought I needed Devise to use the Omniauth gem, but it seems like
maybe I don’t ([according to this explanation on Railscasts](http://railscasts.com/episodes/241-simple-omniauth)).


And devise seems pretty complicated, so now that I have everything working I’m
considering totally removing it and instead just using Omniauth. We’ll see if I
feel like doing that or if it’s more fun to add actual features.
