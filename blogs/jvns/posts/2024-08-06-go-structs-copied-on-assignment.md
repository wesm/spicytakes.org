---
title: "Go structs are copied on assignment (and other things about Go I'd missed)"
date: 2024-08-06
url: https://jvns.ca/blog/2024/08/06/go-structs-copied-on-assignment/
slug: go-structs-copied-on-assignment
word_count: 1264
---


I’ve been writing Go pretty casually for years – the backends for all of my
playgrounds ([nginx](https://nginx-playground.wizardzines.com/), [dns](https://messwithdns.net/), [memory](https://memory-spy.wizardzines.com/), [more DNS](https://dns-lookup.jvns.ca/)) are written in Go, but many of those projects are just a few hundred lines and I don’t come back to those codebases much.


I thought I more or less understood the basics of the language, but this week
I’ve been writing a lot more Go than usual while working on some upgrades to
[Mess with DNS](https://messwithdns.net), and ran into a bug that revealed I
was missing a very basic concept!


Then I posted about this on Mastodon and someone linked me to this very cool
site (and book) called [100 Go Mistakes and How To Avoid Them](https://100go.co) by [Teiva Harsanyi](https://teivah.dev/). It just came out in 2022 so it’s relatively new.


I decided to read through the site to see what *else* I was missing, and found
a couple of other misconceptions I had about Go. I’ll talk about some of the
mistakes that jumped out to me the most, but really the whole
[100 Go Mistakes](https://100go.co/) site is great and I’d recommend reading it.


Here’s the initial mistake that started me on this journey:


### mistake 1: not understanding that structs are copied on assignment


Let’s say we have a struct:


```
type Thing struct {
    Name string
}

```


and this code:


```
thing := Thing{"record"}
other_thing := thing
other_thing.Name = "banana"
fmt.Println(thing)

```


This prints “record” and not “banana” ([play.go.dev link](https://go.dev/play/p/kUeP2ocFtXw)), because `thing` is copied when you
assign it to `other_thing`.


### the problem this caused me: ranges


The bug I spent 2 hours of my life debugging last week was effectively this code ([play.go.dev link](https://go.dev/play/p/85FnGG86UBP)):


```
type Thing struct {
  Name string
}
func findThing(things []Thing, name string) *Thing {
  for _, thing := range things {
    if thing.Name == name {
      return &thing
    }
  }
  return nil
}

func main() {
  things := []Thing{Thing{"record"}, Thing{"banana"}}
  thing := findThing(things, "record")
  thing.Name = "gramaphone"
  fmt.Println(things)
}

```


This prints out `[{record} {banana}]` – because `findThing` returned a copy, we didn’t change the name in the original array.


This mistake is [#30 in 100 Go Mistakes](https://100go.co/#ignoring-that-elements-are-copied-in-range-loops-30).


I fixed the bug by changing it to something like this ([play.go.dev link](https://go.dev/play/p/CKZCRUwv_nG)), which returns a
reference to the item in the array we’re looking for instead of a copy.


```
func findThing(things []Thing, name string) *Thing {
  for i := range things {
    if things[i].Name == name {
      return &things[i]
    }
  }
  return nil
}

```


### why didn’t I realize this?


When I learned that I was mistaken about how assignment worked in Go I was
really taken aback, like – it’s such a basic fact about the language works!
If I was wrong about that then what ELSE am I wrong about in Go????


My best guess for what happened is:

1. I’ve heard for my whole life that when you define a function,
you need to think about whether its arguments are passed by **reference** or
by **value**
2. So I’d thought about this in Go, and I knew that if you pass a struct as a
value to a function, it gets copied – if you want to pass a reference then
you have to pass a pointer
3. But somehow it never occurred to me that you need to think about the same
thing for **assignments**, perhaps because in most of the other languages I
use (Python, JS, Java) I think everything is a reference anyway. Except for
in Rust, where you do have values that you make copies of but I think most of the time I had to run `.clone()` explicitly.
(though apparently structs will be automatically copied on assignment if the struct implements the `Copy` trait)
4. Also obviously I just don’t write that much Go so I guess it’s never come
up.


### mistake 2: side effects appending slices ([#25](https://100go.co/#unexpected-side-effects-using-slice-append-25))


When you subset a slice with `x[2:3]`, the original slice and the sub-slice
share the same backing array, so if you append to the new slice, it can
unintentionally change the old slice:


For example, this code prints `[1 2 3 555 5]` ([code on play.go.dev](https://go.dev/play/p/qssfM_NSXJD))


```
x := []int{1, 2, 3, 4, 5}
y := x[2:3]
y = append(y, 555)
fmt.Println(x)

```


I don’t think this has ever actually happened to me, but it’s alarming and I’m
very happy to know about it.


Apparently you can avoid this problem by changing `y := x[2:3]` to `y := x[2:3:3]`, which restricts the new slice’s capacity so that appending to it
will re-allocate a new slice. Here’s some [code on play.go.dev](https://go.dev/play/p/aE78JUL4-Iv) that does that.


### mistake 3: not understanding the different types of method receivers (#42)


This one isn’t a “mistake” exactly, but it’s been a source of confusion for me
and it’s pretty simple so I’m glad to have it cleared up.


In Go you can declare methods in 2 different ways:

1. `func (t Thing) Function()` (a “value receiver”)
2. `func (t *Thing) Function()` (a “pointer receiver”)


My understanding now is that basically:

- If you want the method to mutate the struct `t`, you need a pointer receiver.
- If you want to make sure the method **doesn’t** mutate the struct `t`, use a value receiver.


[Explanation #42](https://100go.co/#not-knowing-which-type-of-receiver-to-use-42) has a
bunch of other interesting details though. There’s definitely still something
I’m missing about value vs pointer receivers (I got a compile error related to
them a couple of times in the last week that I still don’t understand), but
hopefully I’ll run into that error again soon and I can figure it out.


### more interesting things I noticed


Some more notes from 100 Go Mistakes:

- apparently you can [name the outputs of your function (#43)](https://100go.co/#never-using-named-result-parameters-43), though that can have [issues (#44)](https://100go.co/#unintended-side-effects-with-named-result-parameters-44) and I’m not sure I want to
- [apparently you can put tests in a different package (#90)](https://100go.co/#not-exploring-all-the-go-testing-features-90) to
ensure that you only use the package’s public interfaces, which seems really
useful
- there are a lots of notes about how to use contexts, channels, goroutines,
mutexes, sync.WaitGroup, etc. I’m sure I have something to learn about all of
those but today is not the day I’m going to learn them.


Also there are some things that have tripped me up in the past, like:

- [forgetting the return statement after replying to an HTTP request (#80)](https://100go.co/#forgetting-the-return-statement-after-replying-to-an-http-request-80)
- [not realizing the httptest package exists (#88)](https://100go.co/#not-using-testing-utility-packages-httptest-and-iotest-88)


### this “100 common mistakes” format is great


I really appreciated this “100 common mistakes” format – it made it really
easy for me to skim through the mistakes and very quickly mentally classify
them into:

1. yep, I know that
2. not interested in that one right now
3. WOW WAIT I DID NOT KNOW THAT, THAT IS VERY USEFUL!!!!


It looks like “100 Common Mistakes” is a series of books from Manning and they
also have “100 Java Mistakes” and an upcoming “100 SQL Server Mistakes”.


Also I enjoyed what I’ve read of [Effective Python](https://effectivepython.com/) by Brett Slatkin, which has a similar “here are a bunch of
short Python style tips” structure where you can quickly skim it and take
what’s useful to you. There’s also Effective C++, Effective Java, and probably
more.


### some other Go resources


other resources I’ve appreciated:

- [Go by example](https://gobyexample.com/) for basic syntax
- [go.dev/play](https://go.dev/play/)
- obviously [https://pkg.go.dev](https://pkg.go.dev) for documentation about literally everything
- [staticcheck](https://staticcheck.dev/) seems like a useful linter – for
example I just started using it to tell me when I’ve forgotten to handle an
error
- apparently [golangci-lint](https://golangci-lint.run/) includes a bunch of different linters
