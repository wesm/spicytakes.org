---
title: "Rust in 2018: it's way easier to use!"
date: 2018-01-13
url: https://jvns.ca/blog/2018/01/13/rust-in-2018--way-easier-to-use/
slug: rust-in-2018--way-easier-to-use
word_count: 2895
---


I’ve been using [Rust](https://www.rust-lang.org/en-US/) on and off since late 2013. 4 weeks ago, I
picked up Rust again, and the language is SO MUCH EASIER than it was the last time I tried it (May 2016). I
think that’s really exciting! So I wanted to talk about why I like using Rust today, and a couple of
ideas for where Rust could go in the next year!  (as a response to the [call for community
blogposts](https://blog.rust-lang.org/2018/01/03/new-years-rust-a-call-for-community-blogposts.html))


### me & Rust


I’m an intermediate Rust programmer (definitely not advanced!). Right now I’m writing a profiler in
Rust, which is about 1300 lines of Rust code so far. In 2013 I [wrote a tiny 400-line “operating system’](https://jvns.ca/blog/2014/03/12/the-rust-os-story/) in Rust (basically a small keyboard
driver).


Despite not having much Rust experience (less than 10 weeks of actively using it), I think Rust has
already enabled me to do a lot of awesome things! Like – I’m writing a Ruby profiler in Rust which
extracts Ruby stack traces from arbitrary Ruby programs with only access to its PID, its memory
maps, and the ability to read memory from the process. And it works! Like, I still have some work to
do to get out the first release, but on my laptop it works across **35 different Ruby versions**
(from 1.9.1 to 2.5.0)! It works even if the Ruby program’s symbols are stripped and there’s no
debug info!


That feels really astonishing and magical to me, and I really don’t think I could have accomplished
so much so quickly without Rust.


### Rust’s compiler is more helpful than it was in 2016


One cool thing about being a sporadic Rust user is seeing the huge improvements in the compiler! I
last used Rust (for the same ruby profiler project) in May 2016.


In 2016, my experience of using the Rust compiler was that it was hard. In my [RustConf talk in 2016](https://jvns.ca/blog/2016/09/11/rustconf-keynote/), I said:


> I spend a lot of time being frustrated with the Rust compiler, but I still like it because it lets
> me do things I probably wouldn’t get done otherwise.


I don’t spend as much time being frustrated with the Rust compiler anymore. But it’s not because
I’ve learned a lot more about Rust (I haven’t, yet!) I think it’s mostly because the **compiler is
more helpful**.


This is of course not by magic, it’s because of a huge amount of work on the part of Rust
contributors.
In Rust’s [2017 roadmap](https://blog.rust-lang.org/2017/02/06/roadmap.html), they announced a
focus on productivity for 2017, saying:


> A focus on productivity might seem at odds with some of Rust’s other goals. After all, Rust has
> focused on reliability and performance, and it’s easy to imagine that achieving those aims forces
> compromises elsewhere—like the learning curve, or developer productivity. Is “fighting with the
> borrow checker” an inherent rite of passage for budding Rustaceans? Does removing papercuts and
> small complexities entail glossing over safety holes or performance cliffs?


and


> Our approach with Rust has always been to bend the curve around tradeoffs, as embodied in the
> various pillars we’ve talked about on this blog:


I love this approach (“we’re going to make it easier to use WITHOUT compromising reliablity or
performance at all”), and I feel like they’ve really delivered on it.


But! When talking about the compiler I’ve tried to be careful to say “easier” instead of “easy” – I
think probably there’s some limit to how “easy” Rust can be! There are of course things about Rust
(like compile-time thread safety guarantees!) where fundamentally you do need to think carefully
about what your program is doing exactly. So I don’t expect or want Rust to be “just as easy as
Python” or anything.


### Examples of awesome compiler error messages from today


To show how Rust’s compiler is good: here are a few real examples of compiler error messages I’ve
gotten in the last day or two. I just found all of these by scrolling back though my terminal.


Here’s the first one:


```
error[E0507]: cannot move out of borrowed content
  --> src/bin/ruby-stacktrace.rs:85:16
   |
85 |         if let &Err(x) = &version {
   |                ^^^^^-^
   |                |    |
   |                |    hint: to prevent move, use `ref x` or `ref mut x`
   |                cannot move out of borrowed content

```


This error is incredibly helpful!! I just followed the instructions: I put `ref x` instead of `x`
and my program totally compiled!! This happens relatively often now – I just do what the compiler
tells me to do, and it works!


Here’s another example of a simple error message: I accidentally left out the parameter to `Err()`.
Here I just think it’s nice that it underlines the exact code with the problem.


```
error[E0061]: this function takes 1 parameter but 0 parameters were supplied
   --> src/bin/ruby-stacktrace.rs:154:25
    |
154 |             if trace == Err() {
    |                         ^^^^^ expected 1 parameter

```


One last nice example: I forgot to import the right `Error` type. Rust very helpfully
suggests 4 different `Error` types I might have wanted to use there! (I wanted `failure::Error`,
which is on the list!).


```
error[E0412]: cannot find type `Error` in this scope
   --> src/lib.rs:792:84
    |
792 |     ) -> Result<Box<Fn(u64, pid_t) -> Result<Vec<String>, copy::MemoryCopyError>>, Error> {
    |                                                                                    ^^^^^ not found in this scope
help: possible candidates are found in other modules, you can import them into scope
    |
739 |     use failure::Error;
    |
739 |     use std::error::Error;
    |
739 |     use std::fmt::Error;
    |
739 |     use std::io::Error;

```


### there are still annoying parts (and they’re being worked on)


There are of course still some times where the language doesn’t behave in the way I want. For
example, I have this type `ruby_stacktrace::address_finder::AddressFinderError` which implements the
`Error` trait. So I should just be able to return an `AddressFinderError` when an `Error` is
expected, right? No!!


Instead Rust complains:


```
   Compiling ruby-stacktrace v0.1.1 (file:///home/bork/work/ruby-stacktrace)
error[E0308]: mismatched types
  --> src/bin/ruby-stacktrace.rs:86:20
   |
86 |             return version;
   |                    ^^^^^^^ expected struct `failure::Error`, found enum `ruby_stacktrace::address_finder::AddressFinderError`
   |
   = note: expected type `std::result::Result<_, failure::Error>`
              found type `std::result::Result<_, ruby_stacktrace::address_finder::AddressFinderError>`

```


I know how to fix this: I can hack around it by writing `return Ok(version?)` and then my program
will compile. But the compiler doesn’t tell me how to fix it and it doesn’t give me any super
clear clues about what to do.


But!!! Basically every single time I have an irritating issue like this, I ask Kamal about it (who
writes more Rust than me), and he says “oh yeah, there’s an RFC for that, or at least people are
actively talking about how to fix that!”.


2 specific examples of irritations which have accepted RFCs (which means they’re on the road to
being fixed!):

- There’s an annoying thing where sometimes you need to insert braces around parts of your code to get it to compile. And there’s an accepted RFC called [non-lexical lifetimes](https://github.com/rust-lang/rfcs/blob/master/text/2094-nll.md) to basically make Rust smarter about variable lifetimes!
- When I work with references (which is always!!) I often end up with a situation where the compiler tells me I need to add or remove an ampersand somewhere (like in the first compiler error message I gave). The accepted RFC [Better ergonomics for pattern-matching on references](https://github.com/rust-lang/rfcs/blob/master/text/2005-match-ergonomics.md) makes working with references easier without sacrificing any performance or reliablity! So cool!  The [match ergonomics feature](https://github.com/rust-lang/rust/blob/master/src/doc/unstable-book/src/language-features/match_default_bindings.md) is now in Rust nightly!


It makes me really happy that the Rust community continues to invest time into ergonomics issues
like this. These are all individually relatively small annoyances, but when a large number of them
are fixed I think it really makes a big positive difference to the experience of using of the language.


### easy tradeoffs: `.clone()`


Another thing I love about Rust is that there are **easy ways to avoid doing hard things**. For
example!! I have this function called `get_bss_section` in my program. It’s pretty simple – it just
iterates through all the binary sections of an ELF file and returns the section header for the
section called `.bss`.


```
pub fn get_bss_section(elf_file: &elf::File) -> Option<elf::types::SectionHeader> {
        for s in &elf_file.sections {
            match s.shdr.name.as_ref() {
                ".bss" => {
                    return Some(s.shdr.clone());
                }
                _ => {}
            }
        }
        None
    }
}

```


I was getting a bunch of ownership errors in the compiler, and I really didn’t feel like dealing
with them. So I made an easy tradeoff! I just called `.clone()` which copied the memory and the
problem went away. I could go back to focusing on my actual program logic!


I think being able to make tradeoffs like this (where you make the program a little easier to write
and sacrifice a little bit of performance) is great when starting out with Rust. The thing I love
the most about this particular tradeoff is that it’s **explicit**. I can search for every place I use
`.clone()` in my program and audit them – are they functions that are called a lot? Should I be
worried? I just checked and everywhere I use `clone()` in my program is in functions at the
beginning of the program that only get called once or twice. Maybe I’ll optimize them later!


### Rust’s crate ecosystem is great


In my program, I parse ELF binaries. It turns out that there’s a [crate to do that: the elf crate!](https://docs.rs/elf/0.0.10/elf/).


Right now I’m using the [elf](https://docs.rs/elf/) crate for that. But there’s also the
[goblin](https://docs.rs/goblin/0.0.13/goblin/) crate, which supports Linux (ELF), Mac (Mach-o), and
Windows (PE32) binary formats!! I’ll probably switch to that at some point. I love that these
libraries exist and that they’re well documented and easy to use!


Another thing I love about Rust crates (and Rust in general) is – I feel like they doesn’t usually
add unnecessary abstractions on top of the concepts they’re exposing. The structs in the `elf` crate
are like – `Symbol`, `Section`, `SectionHeader`, `ProgramHeader`.. the concepts in an ELF file!


When I found a weird thing I’d never heard of that I needed to use (the `vaddr` field in the program
header), it was right there! And it was called `vaddr`, which is the same thing it’s called in the C
struct.


### Cargo is amazing


Cargo is Rust’s package manager and build tool and it’s great. I think this is pretty well known.
This is especially apparent to me right now because I’ve been using Go recently – There are lots of
things I like about Go but Go package management is extremely painful and Cargo is just so easy to
use.


My dependencies in my `Cargo.toml` file look something like this. So simple!


```
[dependencies]
libc = "0.2.15"
clap = "2"
elf = "0.0.10"
read-process-memory = "0.1.0"
failure = "0.1.1"
ruby-bindings = { path = "ruby-bindings" } # internal crate inside my repo

```


### Rust gives me total control (like C!)


In Rust I can control every single aspect of what my program is doing – I determine exactly what
system calls it makes, what memory it allocates, how many microseconds it sleeps for – everything.
I feel like anything I could do in a C program, I can do in Rust.


I really love this. Rust isn’t my go-to language for most programming tasks (if I wanted to write a
web service, I probably wouldn’t personally use Rust. See [are we web yet](http://www.arewewebyet.org/) if you’re interested in web services in Rust though!). I feel kind of like Rust is my superhero
language!  If I want to do some weird systemsy magical thing, I know that it’ll be possible in Rust.
Maybe not easy, but possible!


### bindgen & macros are amazing


I wrote blog posts about these already but I want to talk about these again!


I [used bindgen](https://jvns.ca/blog/2017/12/21/bindgen-is-awesome/) to generate Rust struct
definitions for every Ruby struct I need to reference (across 35 different Ruby version). It was
kind of… magical? Like I just pointed at some internal Ruby header files (from my local clone of
the Ruby source) that I wanted to extract struct definitions from, told it the 8 structs I was
interested in, and it just worked.


I think the fact that bindgen lets you interoperate so well with code written in C is really
incredible.


Then I used macros (see: [my first rust macro](https://jvns.ca/blog/2017/12/24/my-first-rust-macro/)) and wrote a bunch of code that
referenced those 35 different struct versions made sure that my code works properly with all of them.


And when I introduced a new Ruby version (like 2.5.0) which had internal API changes, the compiler
said “hey, your old code working with the structs from Ruby 2.4 doesn’t compile now, you have to
deal with that”.


### What should Rust’s 2018 goals be?


In [New Year’s Rust: A Call for Community Blogposts](https://blog.rust-lang.org/2018/01/03/new-years-rust-a-call-for-community-blogposts.html) the Rust core team asked for the community to write blog posts about what they think the Rust language’s goals should be in 2018.  I read and enjoyed a lot of these posts. My favourite two are Aaron Turon’s post: [Rust in 2018: a people perspective](http://aturon.github.io/blog/2018/01/09/rust-2018/) and withoutboats’ [My Goals for Rust in 2018](https://boats.gitlab.io/blog/post/2018-01-08-goals-for-rust/)


I really loved how withoutboats closed their blog post:


> When a programmer with experience in higher level languages begins to use Rust, the space of
> programs that they now have the technology to write expands dramatically. I want to see the kinds
> of programs that emerge when systems programming knowledge is widespread and easy to acquire, when
> anyone with an interest can take the skills they already have and use it to start tinkering in
> domains that once might have seemed inaccessible to them, such as operating systems, network
> protocols, cryptography, or compilers.


Here are my 2 ideas for goals!


### Goal 1: A major release marketed as “Rust: it’s easier to use now”


I think Rust has a huge opportunity to empower people to write interesting and difficult programs
that they couldn’t have written without Rust. Like profilers! Networking software! Debuggers!
Operating systems!


But for people to use Rust, I think it’s important to **tell them that Rust is easier to work with
now**.


I live with an enthusiastic Rust programmer (Kamal) who pays close attention to Rust language
developments and who I talk to about Rust. And I didn’t realize that there had been so many
improvements to Rust’s usability until I started using it again!! So if I didn’t realize I imagine
most other people didn’t either :)


I think Rust has a bit of a reputation for being hard to learn. And of course it’s always going to
be a little bit hard! But I think it would be great to have a Firefox Quantum-style release being
like “hey, did you get frustrated with the Rust compiler when you last tried Rust? We worked on it a
lot! Give us another shot!”


### Goal 2: Explain on rust-lang.org who the Rust programming language is for


I think it’s still a bit hard (especially for newcomers!) to tell which people and what projects
Rust is a good choice for. Like – Rust is really cool and it’s for a lot of different kinds of
people  but it’s still a bit of a specialized thing, and it’s actually not for everyone. So who is
it for? (the [friends of rust page](https://www.rust-lang.org/en-US/friends.html) is the best
resource I know)


Rust is great about being inclusive (“Rust could be for you!”) but IMO “here are 10 specific groups
of people Rust is for” is dramatically more useful than a generic inclusive statement.


Here are a few suggestions for how to answer the question “Who is Rust for?”: (these aren’t meant to
be exclusive, but they are intended to be pretty specific! I think Rust is probably for all these
people, and many more :))

- Rust is **for people who wish they could write C**/C++ programs but found those languages too
unapproachable.
- Rust is **for people building large, complex, performance-sensitive systems software projects**.
Large parts of Firefox are written in Rust and Rust contributed to significantly improving
Firefox’s performance.
- Rust is **for C/C++ experts** who want better compile-time guarantees about undefined behavior.
- Rust is **for people who want to write secure systems code** that’s safe from buffer overflows and
other undefined behavior.
- Rust is **for students** and people who are interested in learning about systems concepts. Many
people have learned about topics like operating systems development through Rust.
- Rust is **for embedded programmers** who want the power of higher-level languages but need code that
compiles to be as small and efficient as C code.
- Rust is **for companies**! Here are some stories about how people are building businesses on Rust.
- Rust is **for people who want to build the Rust programming language**. We’d love you
to contribute to the Rust language.


Also – who **isn’t** Rust for? What are groups Rust’s **wants** to be for but isn’t for yet? What group
of people is Rust explicitly not trying to serve?


I think it’s exciting that Rust serves such different groups of people – like I think Rust is for
people who wish they could write C/C++ but find those languages hard, and that Rust is **also** for
C/C++ experts who want more from their systems programming languages.


That’s all! I am very excited about Rust in 2018 and about continuing to work in Rust for the next
10 weeks!
