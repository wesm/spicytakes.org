---
title: "Day 38: Modifying gotty to serve many different terminal applications at once"
date: 2021-01-14
url: https://jvns.ca/blog/2021/01/14/day-38--modifying-gotty-to-serve-many-different-terminal-applications-at-once/
slug: day-38--modifying-gotty-to-serve-many-different-terminal-applications-at-once
word_count: 995
---


In the [last post](https://jvns.ca/blog/2021/01/13/day-37--a-new-laptop-and-a-little-vue/) I talked about a problem I was having with gotty.


I’m going to recap the problem, and then we’ll talk about what I did about it!
Basically I paired on the problem with Chetan (another Recurser) and we
solved it in a really satisfying way and it was way easier than I thought it would be.


Everything from this post is in a github repository here: [https://github.com/jvns/multi-gotty/](https://github.com/jvns/multi-gotty/)


### what’s gotty?


[gotty](https://github.com/yudai/gotty/) is a Go webserver that lets you put your terminal on a website. So
for example if you run `gotty top`, it’ll start a webserver on port 8080 where it shows the output of `top`.


Or if you run `gotty -w bash`, it’ll start bash and start a webserver where
anyone can type in commands and run them in your shell.


In my puzzle game thing I have people ssh to some virtual machines I’ve
setup. I’ve been using `gotty` to give them a terminal in the browser.


### the problem: a really fragile setup


My problem was that I needed to manage a bunch of different SSH connections
(one per puzzle that a person has open), and `gotty` only supports one session
at a time.


So I set something up where I ran a bunch of different `gotty` processes on
different ports, and then stored a mapping of which session mapped to which
port, and wrote a small go proxy server that proxied `/proxy/SESSION_ID` to the
right port number on the backend.


There were 3 different pieces in this setup:

- the `gotty` processes (potentially lots of them)
- the other go server that proxied connections to those processes
- the Rails server, which was responsible for starting the `gotty` processes on
the right ports and telling the go server which ports they were running on


### the idea: modify `gotty` so that it can manage multiple websocket connections


I wanted a much simpler setup where I could just go to
[http://mysite.com/terminal_session/SOME_ID/](http://mysite.com/terminal_session/SOME_ID/) and have the right SSH connection
automatically set up.


I’m having some trouble explaining what I want the code to do in English so
I’ll just show you some code, because it wasn’t really that much code.


### the code: really simple!


I was originally worried that it would be really complicated to modify `gotty`
to handle multiple websocket connections but actually it was very
straightforward! `gotty` had just 3 HTTP handler functions
(`handleAuthToken`, `handleWS`, and a statics handler), so all we needed to do
was call those in a slightly different way.


Here’s what the new HTTP handler we wrote looks like. It basically just has an if
statement which calls `app.handleWS` with a custom command if the path ends in
`/ws`. I think there might be a more idiomatic Go way to do this but I don’t
know what it is yet. You can see it in context [here](https://github.com/jvns/multi-gotty/blob/main/app/app.go#L239-L260)


```
func (app *App) handleRequest(w http.ResponseWriter, r *http.Request) {
	staticHandler := http.FileServer(
		&assetfs.AssetFS{Asset: Asset, AssetDir: AssetDir, Prefix: "static"},
	)
	path := r.URL.Path
	parts := strings.Split(path, "/")
	// TODO: this panics if the path doesn't have enough stuff in it
	// TODO: actually match on /proxy and don't do this strings.Split thing
	prefix := strings.Join(parts[:3], "/")
	if strings.HasSuffix(path, "/auth_token.js") {
		app.handleAuthToken(w, r)
	} else if strings.HasSuffix(path, "/ws") {
		id := parts[2]
		mapping := app.readMapping()
		if command, ok := mapping[id]; ok {
			app.handleWS(command, w, r)
		}
	} else {
		http.StripPrefix(prefix, staticHandler).ServeHTTP(w, r)
	}
}

```


The parsing code for the path here is still really bad but I’ll fix it at some
point.


The only real other code we had to write was this `readMapping` function which
maps an ID from the URL to a command to run. This is just making an HTTP
request to a server (my Rails app) and decoding some JSON:


```
func (app *App) readMapping() map[string][]string {
	resp, err := http.Get(app.commandServer)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	var mapping map[string][]string
	json.Unmarshal(body, &mapping)
	return mapping
}

```


### http.ResponseWriter and http.Request are great


The real star here is the Go `http` interfaces. Because all Go HTTP handlers
take a `http.ResponseWriter` and a `http.Request`, it’s super easy to wrap
other HTTP request handlers and make them behave slightly differently.


I’d forgotten how it worked but it was pretty easy to pick up again.


### I couldn’t use gotty as a library


We forked gotty instead of using it as a library because the functions we
needed (`handleWS` and `handleAuthToken`) were private, you can tell because
they’re lowercase and in Go the way you know if a function is private or public
is based on whether it starts with an uppercase or lowercase letter.


### pairing is magic


I paired on this with Chetan and it was SO MUCH easier to do with someone else
than on my own. I really thought this would be super hard and it wasn’t – it
was really helpful to talk it through with another person and we got the main
functionality working in just 1 hour!


### the new code works WAY BETTER than my old setup


Having everything coordinated in 1 simple Go program instead of having 3
different moving pieces to coordinate works SO MUCH BETTER. I tried it out and
basically just worked immediately and reliably instead of constantly being
flaky and failing like my old setup.


### here’s the code


I put the code on Github here: [https://github.com/jvns/multi-gotty/](https://github.com/jvns/multi-gotty/). It has
some problems (like the bad path parsing code I mentioned, and it doesn’t let you
change the accepted `Origin:` headers yet), but it does do what I wanted to do!


Here’s the [complete diff](https://github.com/jvns/multi-gotty/commit/b8c64279e8f13bd4f2c14acc71ef97ae081a50a9)
of all the code we changed / deleted in gotty to make this work. We deleted most of gotty’s command line
flags and support for a bunch of things like TLS because I didn’t need them and
I didn’t think anyone else would want to use it.
