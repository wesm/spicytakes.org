---
title: "Profiler week 3: refactoring, better testing, and an alpha release!"
date: 2018-01-22
url: https://jvns.ca/blog/2018/01/22/profiler-week-3--refactoring--better-testing--and-an-alpha-release/
slug: profiler-week-3--refactoring--better-testing--and-an-alpha-release
word_count: 915
---


Hello! Week 3 of profiler-building is over! My main goal for last week was to release an alpha, and
I did! You can download the project & try it out at [https://github.com/rbspy/rbspy](https://github.com/rbspy/rbspy).


If you’re interested in how the project is organized, I wrote an [architecture document](https://github.com/rbspy/rbspy/blob/master/ARCHITECTURE.md) this week.


If you do find it useful, I’d be really interested to hear about what you’re using it for – you can
email me, [leave a message on gitter](https://gitter.im/rbspy/rbspy), tweet at me – anything! Also
I very much appreciate bug reports :)


For example, somebody [said on Twitter](https://twitter.com/b0rk/status/955257788028145665) that they used `rbspy snapshot` (which prints a single stack trace from the
program) to figure out why their tests were running slowly! This made me super happy =).


> I used it to profile a test run on CI: some tests suddenly became very slow; I connected to the
> container thru SSH, downloaded rbspy and took a couple of snapshots while tests were running; that
> was enough to find the cause of the problem)


### name: rbspy!


On Tuesday I polled people on Twitter for name ideas. I wanted something that was a little bit fun
(profiling is fun!), but not **too** clever – I want people to be able to actually tell what the
project does from the name. Hopefully `rbspy` will be that!


Also I drew a quick logo! It is not super fancy but I like it anyway. An alpha logo for an alpha
release :)


![](https://jvns.ca/images/rbspy.png)


### refactoring!


Last week I also refactored the project significantly. I probably spent 2-3 whole days on
trying to organize the project better – at the beginning of the week it was all basically one
1000-line file, and at the end of the week, I had files for

- initialization code (what happens every time you start the profiler)
- operating-system-specific code (want to add support for a new OS? it goes in `address_finder.rs`!)
- ruby-version-specific code (want to add Ruby 2.5.1 support? That goes here in `ruby_version.rs`)
- UI code (all in `main.rs`, right now)


My most useful strategy for refactoring was to write an [architecture document (which you can read!)](https://github.com/rbspy/rbspy/blob/master/ARCHITECTURE.md). Basically I tried to explain to
an outsider how the project was put together, found parts that really didn’t make sense, and then
refactored until those parts were easier to explain.


I don’t think it’s “perfect” (what is?) but the organization was easier for me to work with at the
end of the week, and Kamal said it made more sense to him too.


### better testing with core dumps!


This week we also got some significantly better testing implemented – now there are a bunch of core
dumps in the rbspy-testdata repo ([https://github.com/rbspy/rbspy-testdata/tree/master/data)](https://github.com/rbspy/rbspy-testdata/tree/master/data)).


During the tests, we

- load the core dumps
- try to read a stack trace from those core dumps as if it was a real Ruby process
- compare the stack trace we read to the expected output


Kamal [wrote the code to make a core dump mimic a real process](https://github.com/rbspy/rbspy-testdata/blob/431814a7eb50b0bde083b2a52be9e5f68e117518/src/lib.rs)
and it’s really simple and clever. This whole testing strategy is Kamal’s idea and he actually
implemented the key ideas 1.5 years ago. Also it was his idea to keep the core dumps in a separate
`rbspy-testdata` repository so that we can keep several megabytes of coredumps for testing without
making the main repo huge.


I’m very happy to have these tests and they make me feel a lot more confident that the project is
actually doing the right thing. And they let me make improvements! For example – right now I have a
core dump of a process where rbspy gives me an error if I try to get a stack trace out of it. Once I
fix the issue (to do with calling C functions), I can check that core dump into `rbspy-testdata`,
add a test, and make sure it stays fixed!


One more example of a thing these tests helped me do – I needed to get both the relative and the
absolute path to a file in Ruby 1.9.3. Figuring out how to do this was pretty simple (I did a little `git blame` and then this [commit showed me the way](https://github.com/ruby/ruby/commit/bac9f65f707e8ffcb79389e5b10b32addc94dc01)).
With the Ruby 1.9.3 core dump, I could add code to get the relative & absolute path, run
`get_stack_trace` on the core dump, and assert that I got the expected answer! Really easy!


### contributors!


I published my first release last night. So far 3 people have created issues and I’ve merged a pull
request from one of those people! This is exciting because one of my major goals is to get more
people contributing to rbspy so it’s a sustainable project and not just me.


### this week: Mac support & container support


This week I’m hoping to add Mac support! I don’t own a Mac, but my plan is to rent a cloud VM for a
week or so and develop on that.


I also have a bug to do with C function-calling support that I’m hoping to fix. Also container
support: right now if you try to profile a process running in a container from outside the
container it won’t work because because the process is in a different filesystem namespace. That
shouldn’t be too hard to fix.


At some point I also want to start investigating memory profilers – maybe I can add a memory
profiler to rbspy? I have no idea what’s involved in that yet! We’ll see!
