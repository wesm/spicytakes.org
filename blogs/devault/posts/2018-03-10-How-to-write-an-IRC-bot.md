---
title: "How to write an IRC bot"
date: 2018-03-10
url: https://drewdevault.com/2018/03/10/How-to-write-an-IRC-bot.html
slug: How-to-write-an-IRC-bot
word_count: 769
---

My disdain for Slack and many other Silicon Valley chat clients is  [well
known](/2015/11/01/Please-stop-using-slack.html) , as is my undying love for IRC.
With Slack making the news lately after their recent decision to disable the IRC
and XMPP gateways in a classic  [Embrace Extend
Extinguish](https://en.wikipedia.org/wiki/Embrace%2C_extend%2C_and_extinguish) 
move, they’ve been on my mind and I feel like writing about them more. Let’s
compare writing a bot for Slack with writing an IRC bot.

First of all, let’s summarize the process for making a Slack bot. Full details
are available in  [their documentation](https://api.slack.com/slack-apps) . The
basic steps are:

1. Create a Slack account and “workspace” to host the bot (you may have already
done this step). On the free plan you can have up to 10 “integrations” (aka
bots). This includes all of the plug-n-play bots Slack can set up for you, so
make sure you factor that into your count. Otherwise you’ll be heading to the
pricing page and making a case to whoever runs your budget.
2. Create a “Slack app” through their web portal. The app will be tied to the
company you work with now, and if you get fired you will lose the app. Make
sure you make a separate organization if this is a concern!
3. The recommended approach from here is to set up subscriptions to the “Event
API”, which involves standing up a web server (with working SSL) on a
consistent IP address (and don’t forget to open up the firewall) to receive
incoming notifications from Slack. You’ll need to handle a proprietary
challenge to verify your messages via some HTTP requests coming from Slack
which gives you info to put into HTTP headers of your outgoing requests. The
Slack docs refer to this completion of this process as “triumphant success”.
4. Receive some JSON in a proprietary format via your HTTP server and use some
more proprietary HTTP APIs to respond to it.

Alternatively, instead of steps 3 and 4 you can use the “Real Time Messaging”
API, which is a websocket-based protocol that starts with an HTTP request to
Slack’s authentication endpoint, then a follow-up HTTP request to open the
WebSocket connection. Then you set up events in a similar fashion. Refer to the
complicated table in the documentation breaking down which events work through
which API.

Alright, so that’s the Slack way. How does the IRC way compare? IRC is an open
standard, so to learn about it I can just read RFC 1459, which on my system is
conveniently waiting to be read at  `/usr/share/doc/rfc/txt/rfc1459.txt` . This
means I can just read it locally, offline, in the text editor of my choice,
rather than on some annoying website that calls authentication a “triumphant
success” and complains about JavaScript being disabled.

**Note** : This blog post pre-dates the commercial take-over of and subsequent
obsolescence of Freenode. The network this connects to, and channel it mentions,
no longer exist. Running these commands will not work, though the principles
remain correct.

You don’t have to read it right now, though. I can give you a summary here, like
I gave for Slack. Let’s start by not writing a bot at all - let’s just manually
throw some bits in the general direction of Freenode. Install netcat and run
 `nc irc.freenode.net 6667` , then type this into your terminal:

```
NICK joebloe
USER joebloe 0.0.0.0 joe :Joe Bloe
```

Hey, presto, you’re connected to IRC! Type this in to join a channel:

```
JOIN #cmpwn
```

Then type this to say hello:

```
PRIVMSG #cmpwn :Hi SirCmpwn, I'm here from your blog!
```

IRC is one of the simplest protocols out there, and it’s dead easy to write a
bot for it. If your programming language can open a TCP socket (it can), then
you can use it to write an IRC bot in 2 minutes, flat. That’s not even to
mention that there are IRC client libraries available for every programming
language on every platform ever - I even  [wrote one
myself!](https://github.com/SirCmpwn/ChatSharp)  In fact, that guy is probably
the fifth or sixth IRC library I’ve written. They’re so easy to write that I’ve
lost count.

Slack is a walled garden. Their proprietary API is defined by them and only
implemented by them. They can and will shut off parts you depend on (like the
IRC+XMPP gateways that were just shut down). IRC is over 20 years old and
software written for it then still works now. It’s implemented by hundreds of
clients, servers, and bots. Your CI supports it and GitHub can send commit
notifications to it. It’s ubiquitous and free. Use it!
