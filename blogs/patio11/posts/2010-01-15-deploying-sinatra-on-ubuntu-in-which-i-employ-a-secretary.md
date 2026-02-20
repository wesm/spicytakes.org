---
title: "Deploying Sinatra On Ubuntu: In Which I Employ A Secretary"
date: 2010-01-15
url: https://www.kalzumeus.com/2010/01/15/deploying-sinatra-on-ubuntu-in-which-i-employ-a-secretary/
slug: deploying-sinatra-on-ubuntu-in-which-i-employ-a-secretary
word_count: 907
---


As [mentioned previously](https://www.kalzumeus.com/2009/12/29/twilio-phone-call-web-api-is-crazy-fun/), I really hate getting woken up at 3 AM in the morning.  This happens fairly frequently for me, though, because I live in Japan and about half of the people who call me do not. I have not been effective at getting them to check what time it is here before they call, but I certainly want them to call, and even call me in the middle of the night if it is an emergency.


So I made myself a phone secretary with [Twilio](http://www.twilio.com), their [Ruby gem](http://github.com/twilio/twilio-ruby), and [Sinatra](http://www.sinatrarb.com/) (a lightweight Ruby web framework).  I gave my friends and family a US number assigned to me by Twilio. Dialing it causes Twilio’s computer to talk to my server and figure out what I want to do with the call. The server runs a Sinatra app which checks the time in Japan and either forwards the call to the most appropriate phone or gently informs the user that it is 4:30 AM in the morning.


The code for this took 10 minutes. Reasoning my way through a deployment took, hmm, 3 hours or so. I am a programmer not a sysadmin, what can I say. I thought I’d write down what I did so that other folks can save themselves some pain.


Code (You’re probably not too interested in the exact logic, but feel free to use it as a springboard if you want to make a secretary/call forwarding app):


This script is a bit ugly but, hey, what do you want in ten minutes. (Memo to self: correct it after leaving my job.)


## Sinatra Deployment On Ubuntu


A quick look around the Internet didn’t show any cookbook recipes for deploying Sinatra. I thought I’d write up what I’m using, which uses Apache reverse proxying to Sinatra. (Instructions included for Nginx as well.) It assumes you already have your webserver running and are familiar with basic Ruby usage and the Linux command line.


1) Install the [daemons gem](http://daemons.rubyforge.org/). We’re going to daemonize Sinatra so that it runs out of our console and starts and stops without our intervention, much like Apache does.


2) Create an /opt/pids/sinatra directory. (It seemed as good a place as any.) Let a non-privileged user write to that directory, for example by executing “sudo chown www-data /opt/pids/sinatra; sudo chmod 755 /opts/pids/sinatra”. Make a note of what non-privileged user you use. I am just reusing www-data because Apache has conveniently provided him for me and he is guaranteed to not to be able to screw up anything important if he is compromised.


2) Write a quick control script and put it in the same directory as your Sinatra app (called phone_sinatra.rb for the purposes of this demonstration). I threw these in /www/var/phone.example.com/ but you can put them anywhere. Make sure the scripts are readable, but not writable, by www-data. (*sudo chmod 755 /www/var/phone.example.com/* will accomplish this: it makes only the owner able to write to it, but any user on the system — including www-data — can read from it.)


3) (Optional) Add in a reverse proxy rule to Apache or Nginx to send requests to the subdomain of your choice to Sinatra instead. I ended up deploying this through Apache, so the rule is pretty quick:


You could also do this on Nginx and it is similarly trivial.


The main reason I do this is to not have to remember non-standard ports in my URLs. It also simplifies firewall management if you’re into that sort of thing.


4) Add a control script to /etc/init.d/sinatra so that we can start and stop Sinatra just like we do other services, like Apache.


5) Tell Ubuntu to start your daemon when the computer starts up and shut it off when the computer starts down: sudo update-rc.d sinatra defaults


6) Start the service manually for your first and only time: sudo /etc/init.d/sinatra start


There you have it: Sinatra is running the application you wrote, and it will start and stop with your Ubuntu server. If you were doing this for Twilio now you’d check your Twilio account settings to make sure it has the right URL set up for your phone number, and then try calling yourself. Preferably NOT from the phone you try to forward to.


All code in this blog post was written by Patrick McKenzie in early 2010. I release it unto the public domain. Feel free to use it as the basis for your own apps.


Twilio development makes me feel like a kid in a candy store — you can affect the real world through an API, how cool is that? I think next time I have a few hours to kill I’m going to make a similar secretary for my business. I don’t give folks my phone number because a) I live in Japan and b) they don’t pay me enough to do telephone support. However, quoting a telephone number on your website instantly says “There is a real business behind this!”


I think I’ll whip up a computer secretary for the business which handles the most common two support requests (“I didn’t get my Registration Key” and “I lost my password.”), and for anything else takes their message and emails it to me. That sort of thing costs megacorporations bazillions and can be whipped up these days by a single programmer on Saturday morning for under $5 a month in operating costs. Like I said, candy store.
