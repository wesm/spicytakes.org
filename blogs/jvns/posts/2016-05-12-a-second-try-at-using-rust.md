---
title: "A second try at using Rust"
date: 2016-05-12
url: https://jvns.ca/blog/2016/05/12/a-second-try-at-using-rust/
slug: a-second-try-at-using-rust
word_count: 836
---


I used Rust for the first time in late 2013, while trying to write a tiny operating system. At the time, I learned a lot and it was pretty fun, but I found the experience pretty frustrating. There were all these error messages I didn’t understand! It took forever to work with strings! Everyone was very nice but it felt confusing.


I just tried Rust again yesterday! Kamal has been trying to sell me (and [everyone else](http://kamalmarhubi.com/blog/2016/04/13/rust-nix-easier-unix-systems-programming-3/)) on the idea that if you’re doing systems-y work, and you don’t know any systems language very well, then it’s worth learning Rust.


After a day or so of trying Rust again, I think he’s right that learning Rust is easier than learning C. A few years after first trying, I feel like the language has progressed a lot, and it feels more like writing Python or some other easy language.


Some things I could do easily without working too hard

- run a process and then match a regular expression on its output
- make a hashmap, store counts in it, and print the top 10
- format strings nicely and print them
- read command line options
- allocate a lot of memory without creating a memory leak


Those things would have been really hard in C (how do you even make a hashmap???
I think you have to write the data structure yourself or something.). I probably could have figured out how to free memory in C (i hear you use `free` :) ) but honestly I don’t know how to write C and it’s very likely it would have turned into an unmaintainable mess. The things were
maybe slightly harder to do than in Python (which is a programming language that
I actually know), but I think not way way way harder. I was surprised at how easy they were!


### a sidebar on learning programming languages


I pair programmed a bunch of Rust code with Kamal, who actually knows Rust. Sometimes when I program, I try to understand everything all at once right away (“what are lifetime? how do they work? what are all these pointer types? omg!!!”). This time I tried a new approach! When I didn’t understand something, I was just like “hey kamal tell me what to type!” and he would, and then my program would work.


I’d fix the bugs that I understood, and he’d fix the bugs I didn’t, and we made a lot of progress really quickly and it wasn’t that frustrating.


I kind of enjoy the experience of having a Magical Oracle to fix my programming problems for me – having someone elide away the harder stuff so I can focus on what’s easy feels to me like a good way to learn.


Of course, you can’t let someone else fix all your hard programs *forever*. Eventually I’ll have to understand all about Rust pointers and lifetimes and everything, if I want to write Rust! I bet it’s not even all that hard. But for today I only understand like 6 things and that’s fine.


### error messages


I’ve also been mostly happy with the Rust error messages! Sometimes they’re super inscrutable, but often they’re mostly lucid. Sometimes they link to GitHub issues, and someone on the GitHub issue will have a workaround for your problem! Sometimes they come with detailed explanations!


Here’s an example:


```
$ rustc --explain E0281
`You tried to supply a type which doesn't implement some trait in a location
which expected that trait. This error typically occurs when working with
`Fn`-based types. Erroneous code example:

---
fn foo<F: Fn()>(x: F) { }

fn main() {
    // type mismatch: the type ... implements the trait `core::ops::Fn<(_,)>`,
    // but the trait `core::ops::Fn<()>` is required (expected (), found tuple
    // [E0281]
    foo(|y| { });
}
---

The issue in this case is that `foo` is defined as accepting a `Fn` with no
arguments, but the closure we attempted to pass to it requires one argument.


```


### valgrind + perf + rust = <3


another cool thing I noticed is that you can run valgrind or perf on the Rust program and figure out easily which parts of your program are running slowly! And I think the Rust program even has debug info so you can look at the source code in kcachegrind. This was really cool. I ran into a program with valgrind where my program worked fine in Rust, but when I ran it under valgrind it failed. I don’t understand why this happened at all.


### the rust docs actually seem good?


I haven’t delved super a lot into the Rust docs, but so far I’ve been happy: there’s a [book](https://doc.rust-lang.org/book/) and lots of other [documentation](https://www.rust-lang.org/documentation.html) and it’s all official on the Rust website! I think they actually paid Steve Klabnik to write docs, which is amazing.


Here is my [Rust project!](https://github.com/jvns/ruby-stacktrace). More on what it actually does later, but I’m super excited about it (for now it’s a MYSTERY :D :D).
