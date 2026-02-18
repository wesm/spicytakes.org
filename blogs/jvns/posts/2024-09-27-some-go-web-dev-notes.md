---
title: "Some Go web dev notes"
date: 2024-09-27
url: https://jvns.ca/blog/2024/09/27/some-go-web-dev-notes/
slug: some-go-web-dev-notes
word_count: 1472
---


I spent a lot of time in the past couple of weeks working on a website in Go
that may or may not ever see the light of day, but I learned a couple of things
along the way I wanted to write down. Here they are:


### go 1.22 now has better routing


I’ve never felt motivated to learn any of the Go routing libraries
(gorilla/mux, chi, etc), so I’ve been doing all my routing by hand, like this.


```
	// DELETE /records:
	case r.Method == "DELETE" && n == 1 && p[0] == "records":
		if !requireLogin(username, r.URL.Path, r, w) {
			return
		}
		deleteAllRecords(ctx, username, rs, w, r)
	// POST /records/<ID>
	case r.Method == "POST" && n == 2 && p[0] == "records" && len(p[1]) > 0:
		if !requireLogin(username, r.URL.Path, r, w) {
			return
		}
		updateRecord(ctx, username, p[1], rs, w, r)


```


But apparently [as of Go 1.22](https://go.dev/blog/routing-enhancements), Go
now has better support for routing in the standard library, so that code can be
rewritten something like this:


```
	mux.HandleFunc("DELETE /records/", app.deleteAllRecords)
	mux.HandleFunc("POST /records/{record_id}", app.updateRecord)

```


Though it would also need a login middleware, so maybe something more like
this, with a `requireLogin` middleware.


```
	mux.Handle("DELETE /records/", requireLogin(http.HandlerFunc(app.deleteAllRecords)))

```


### a gotcha with the built-in router: redirects with trailing slashes


One annoying gotcha I ran into was: if I make a route for `/records/`, then a
request for `/records` [will be redirected](https://pkg.go.dev/net/http#hdr-Trailing_slash_redirection-ServeMux) to `/records/`.


I ran into an issue with this where sending a POST request to `/records`
redirected to a GET request for `/records/`, which broke the POST request
because it removed the request body. Thankfully [Xe Iaso wrote a blog post about the exact same issue](https://xeiaso.net/blog/go-servemux-slash-2021-11-04/) which made it
easier to debug.


I think the solution to this is just to use API endpoints like `POST /records`
instead of `POST /records/`, which seems like a more normal design anyway.


### sqlc automatically generates code for my db queries


I got a little bit tired of writing so much boilerplate for my SQL queries, but
I didn’t really feel like learning an ORM, because I know what SQL queries I
want to write, and I didn’t feel like learning the ORM’s conventions for
translating things into SQL queries.


But then I found [sqlc](https://sqlc.dev/), which will compile a query like this:


```

-- name: GetVariant :one
SELECT *
FROM variants
WHERE id = ?;


```


into Go code like this:


```
const getVariant = `-- name: GetVariant :one
SELECT id, created_at, updated_at, disabled, product_name, variant_name
FROM variants
WHERE id = ?
`

func (q *Queries) GetVariant(ctx context.Context, id int64) (Variant, error) {
	row := q.db.QueryRowContext(ctx, getVariant, id)
	var i Variant
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Disabled,
		&i.ProductName,
		&i.VariantName,
	)
	return i, err
}

```


What I like about this is that if I’m ever unsure about what Go code to write
for a given SQL query, I can just write the query I want, read the generated
function and it’ll tell me exactly what to do to call it. It feels much easier
to me than trying to dig through the ORM’s documentation to figure out how to
construct the SQL query I want.


Reading [Brandur’s sqlc notes from 2024](https://brandur.org/fragments/sqlc-2024) also gave me some confidence
that this is a workable path for my tiny programs. That post gives a really
helpful example of how to conditionally update fields in a table using CASE
statements (for example if you have a table with 20 columns and you only want
to update 3 of them).


### sqlite tips


Someone on Mastodon linked me to this post called [Optimizing sqlite for servers](https://kerkour.com/sqlite-for-servers). My projects are small and I’m
not so concerned about performance, but my main takeaways were:

- have a dedicated object for **writing** to the database, and run
`db.SetMaxOpenConns(1)` on it. I learned the hard way that if I don’t do this
then I’ll get `SQLITE_BUSY` errors from two threads trying to write to the db
at the same time.
- if I want to make reads faster, I could have 2 separate db objects, one for writing and one for reading


There are a more tips in that post that seem useful (like “COUNT queries are
slow” and “Use STRICT tables”), but I haven’t done those yet.


Also sometimes if I have two tables where I know I’ll never need to do a `JOIN`
beteween them, I’ll just put them in separate databases so that I can connect
to them independently.


### Go 1.19 introduced a way to set a GC memory limit


I run all of my Go projects in VMs with relatively little memory, like 256MB or
512MB. I ran into an issue where my application kept getting OOM killed and it
was confusing – did I have a memory leak? What?


After some Googling, I realized that maybe I didn’t have a memory leak, maybe I
just needed to reconfigure the garbage collector! It turns out that by default (according to [A Guide to the Go Garbage Collector](https://tip.golang.org/doc/gc-guide)), Go’s garbage collector will
let the application allocate memory up to **2x** the current heap size.


[Mess With DNS](https://messwithdns.net)’s base heap size is around 170MB and
the amount of memory free on the VM is around 160MB right now, so if its memory
doubled, it’ll get OOM killed.


In Go 1.19, they added a way to tell Go “hey, if the application starts using
this much memory, run a GC”. So I set the GC memory limit to 250MB and it seems
to have resulted in the application getting OOM killed less often:


```
export GOMEMLIMIT=250MiB

```


### some reasons I like making websites in Go


I’ve been making tiny websites (like the [nginx playground](https://nginx-playground.wizardzines.com/)) in Go on and off for the last 4 years or so and it’s really been working for me. I think I like it because:

- there’s just 1 static binary, all I need to do to deploy it is copy the binary. If there are static files I can just embed them in the binary with [embed](https://pkg.go.dev/embed).
- there’s a built-in webserver that’s okay to use in production, so I don’t need to configure WSGI or whatever to get it to work. I can just put it behind [Caddy](https://caddyserver.com/) or run it on fly.io or whatever.
- Go’s toolchain is very easy to install, I can just do `apt-get install golang-go` or whatever and then a `go build` will build my project
- it feels like there’s very little to remember to start sending HTTP responses
– basically all there is are functions like `Serve(w http.ResponseWriter, r *http.Request)` which read the request and send a response. If I need to
remember some detail of how exactly that’s accomplished, I just have to read
the function!
- also `net/http` is in the standard library, so you can start making websites
without installing any libraries at all. I really appreciate this one.
- Go is a pretty systems-y language, so if I need to run an `ioctl` or
something that’s easy to do


In general everything about it feels like it makes projects easy to work on for
5 days, abandon for 2 years, and then get back into writing code without a lot
of problems.


For contrast, I’ve tried to learn Rails a couple of times and I really *want*
to love Rails – I’ve made a couple of toy websites in Rails and it’s always
felt like a really magical experience. But ultimately when I come back to those
projects I can’t remember how anything works and I just end up giving up. It
feels easier to me to come back to my Go projects that are full of a lot of
repetitive boilerplate, because at least I can read the code and figure out how
it works.


### things I haven’t figured out yet


some things I haven’t done much of yet in Go:

- rendering HTML templates: usually my Go servers are just APIs and I make the
frontend a single-page app with Vue. I’ve used `html/template` a lot in Hugo (which I’ve used for this blog for the last 8 years)
but I’m still not sure how I feel about it.
- I’ve never made a real login system, usually my servers don’t have users at all.
- I’ve never tried to implement CSRF


In general I’m not sure how to implement security-sensitive features so I don’t
start projects which need login/CSRF/etc. I imagine this is where a framework
would help.


### it’s cool to see the new features Go has been adding


Both of the Go features I mentioned in this post (`GOMEMLIMIT` and the routing)
are new in the last couple of years and I didn’t notice when they came out. It
makes me think I should pay closer attention to the release notes for new Go
versions.
