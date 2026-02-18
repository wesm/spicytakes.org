---
title: "New tool: an nginx playground"
date: 2021-09-24
url: https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground/
slug: new-tool--an-nginx-playground
word_count: 1473
---


Hello! On Wednesday I was talking to a friend about how it would be cool to
have an nginx playground website where you can just paste in an nginx config
and test it out. And then I realized it might actually be pretty easy to build,
so got excited and started coding and I built it. It’s at
[https://nginx-playground.wizardzines.com](https://nginx-playground.wizardzines.com) and the source is at [github.com/jvns/nginx-playground](https://github.com/jvns/nginx-playground).


Here’s a screenshot:


![](https://jvns.ca/images/nginx-playground-screenshot.jpg)


For the rest of the post I’m mostly going to talk about how I built the
project, because there were a few decisions that weren’t obvious to me.


### how to use it


You need to enter both an nginx config and a `curl` or `http` command to make a
HTTP request to that nginx instance


And then you click “Run” in the top right, and it’ll output either:

1. the results of the command you executed (if nginx started successfully), or
2. the nginx error logs (if nginx failed to start)


### why a playground?


I find that playgrounds really help me learn – it’s incredibly useful to be
able to quickly and safely experiment and try out different options without
worrying that Something Terrible is going to happen if you make a mistake.


And nginx in particular is EXTREMELY finicky to configure, so I think it’s
extra important to have a playground for nginx to quickly test things out.


Here are 3 playgrounds I’ve made in the past:

- [SQL playground](https://sql-playground.wizardzines.com), which uses [sql.js](https://github.com/sql-js/sql.js/) to let you run arbitrary SQLite queries on some small example data
- [CSS examples](https://css-examples.wizardzines.com), which uses [codepen](https://codepen.io) to show some examples of surprising CSS behaviour that you can play with
- [DNS lookup](https://dns-lookup.jvns.ca/), which makes DNS queries to any website you want


and a few other great playgrounds that others have made:

- [CodePen](https://codepen.io) for CSS/JS/HTML
- [regexr](https://regexr.com/) for regular expressions
- [db-fiddle](https://www.db-fiddle.com/) for SQL
- this [nginx location match tester](https://nginx.viraptor.info/) that reimplements nginx’s location matching in typescript


### building it quickly by keeping it simple


This site has

1. a static frontend (using vue.js and tailwind, my usual frontend stack)
2. a Go backend with a single API endpoint that just does 1 thing (run an nginx config)


This made pretty easy to build the project quickly (I just needed to write 1
backend endpoint and then a frontend that uses that endpoint!). This is also
how the [dns lookup](https://dns-lookup.jvns.ca) tool I made works – I like this
approach a lot and I think I’ll do other projects in the same way.


Let’s talk about what that backend code does when the frontend makes a request
to it!


### what happens when you make a request


Here’s what the Go backend does when you click ‘run’: (also here’s a [gist with the code right now](https://gist.github.com/jvns/edf78e7775fea8888685a9a2956bc477))

1. write the config to a temp file
2. create a new network namespace (`ip netns add $RANDOM_NAMESPACE_NAME`)
3. start [go-httpbin](https://github.com/mccutchen/go-httpbin) on port 777 so that people can use that as a backend in their nginx configs
4. start nginx
5. wait 100ms to make sure nginx started, if it failed then return nginx’s error logs to the client
6. run the command that the user requested (and make sure that the command starts with `curl` or `http`)
7. return the command’s output
8. done


### the security problem


The whole point of the tool is to let people run arbitrary nginx
configurations, and it’s easy to imagine how that could result in the server
being compromised. But I wanted run the service for free and not spend a lot of
money on hosting. So I wanted to just use 1 shared server for all requests.


This kind of thing often stops me from doing projects like this, but this one
felt a little more tractable to me.


### the security approach: a little bit of isolation, a little bit of YOLO


Here’s how I decided to approach the security to start, after talking to a friend about it:

1. Host the frontend on a CDN, separately from the backend (so that if the backend gets compromised nobody can serve malware from the frontend)
2. Don’t use a database, just browser local storage (can’t hack the database if there isn’t one!)
3. Put every nginx in its own network namespace, don’t let it connect to the internet
4. Use fly.io’s free tier (so it’s isolated on its own VM, as far as I know it doesn’t have
access to anything sensitive, and I can potentially destroy and redeploy the
VM every hour if I want to)
5. Ask people to be nice in the FAQ (that’s the “YOLO” part :) )


I think that with these constraints, the only bad things that could happen are:


a. Someone gets access to the test nginx configs of other people using the website at the same time
b. Someone replaces the backend API server so that it returns some sort of malicious or offensive output.
c. Someone tries to mine bitcoin on the tiny instance it’s running on (1 shared CPU, 256 MB RAM)


I don’t think any of those are thaaaat harmful in the grand scheme of things,
though it’s possible I’m missing something. Someone already showed how to read
the `/etc/passwd` file which is fun, but there’s nothing sensitive in
there.


I might switch to running each nginx in a container later instead of just
running it in a network namespace, but I didn’t do it initially because I
thought it might be too slow – it’s already a bit slow.


Speaking about slow, let’s talk about performance.


### some notes on performance


Like I mentioned before, this backend is running on a pretty small instance
(1 shared CPU, 256 MB RAM). Here are some quick notes on that:

1. the frontend runs on a CDN, so the backend only gets used when someone
actually executes an nginx config. That takes a lot of pressure off the tiny backend.
2. According to the server logs, each request seems to take about 400ms right now. That’s
not too bad!
3. It’s running on a server in Toronto right now, so I guess it’s be slower
for people far away from Toronto. I could fix that by running more fly
servers in more locations though.
4. I used a Go clone of [httpbin](https://httpbin.org) instead of the original
Python version, since I figured the Go version would be lighter weight
5. The frontend performance isn’t great – the CSS and JS is all in separate
files. I didn’t want to use an `npm build` step to combine them because I’m
pretty bad at Javascript and I’m always worried my Javascript build will
break and then I’ll be too lazy to fix it and then it’ll be impossible for
me to deploy changes.
6. I added a little rocket ship gif that plays while the backend is running to
make it a little more fun to wait


The silliest performance problem I had was that I was originally stopping the
nginx worker processes by sending them a SIGKILL signal. But that killed just
the main process and not the worker processes, so then I was leaking nginx
worker processes, which eventually made the instance run out of memory. Sending
nginx processes a `SIGTERM` instead made it shut down everything correctly and
fixed that problem.


### the design


The design basically just copies [jsfiddle](https://jsfiddle.net) and [codepen](https://codepen.io/pen).


In particular JSFiddle does a nice simple thing where it calculates the height
of the main area as `calc(100vh - 60px)` and the header has height `60px`. I
wouldn’t have thought of that on my own but it seems to work really well.


I used [CodeMirror](https://codemirror.net/) for syntax highlighting because
that’s what jsfiddle and codepen both seem to do, it was super easy to set up,
and it turns out it even has an `nginx` and a `shell` mode! It’s everything I
could have dreamed of :)


The main hiccup with CodeMirror was that I initially wanted to use a `vue-codemirror`
integration and there wasn’t one for Vue 3, but I decided that it was
unnecessary and just wrote my own tiny integration that updates Vue when
the textbox is updated. (basically just `this.nginx_codemirror.on('change', cm => this.nginx_config = cm.getValue())`)


You can see the Javascript code at [script.js](https://nginx-playground.wizardzines.com/script.js) but there’s
really not a lot of it.


### still to do: add more example nginx configs


I’m still not quite sure what the examples should be, but I think I want to
provide a few more template nginx configs to use as starting points.


### this was easier to build than I thought


This was a lot easier to build than I thought it would be! It makes me want to
build playgrounds for other programs too, though I’m not sure which one would
be next. HAProxy seems like an obvious similar choice.
