---
title: "How often do Ruby's stack struct definitions change?"
date: 2017-12-19
url: https://jvns.ca/blog/2017/12/19/how-much-does-the-ruby-abi-change-/
slug: how-much-does-the-ruby-abi-change-
word_count: 1102
---


Hello! I am doing some research for my Ruby profiler this week, and so I thought I’d write the
research in a blog post. This is all stuff I’m trying to figure out this morning so it’s all pretty
early-stage.


Basically I’m trying to figure out if I can define a finite fixed set of Ruby struct layouts in my
Ruby profiler at compile time (RUBY_2_3_0, RUBY_2_4_0, etc) or if I need to get the struct layouts
at runtime using DWARF. If you are interested in this and have ideas about this post I’d love to
hear them on twitter / by email.


Before I dive in the gnarly question of “how often does vm_core.h” change in ways that I care
about?", let’s start with a little background.


### how do you get the current Ruby stack out of a Ruby program?


The main question a sampling profiler needs to answer (over and over and over… :)) is “what’s the
stack right now?”.


If you run gdb on a Ruby 2.1 process with debug symbols installed you can get the


```
(gdb) p ((struct RString*) ruby_current_thread.cfp.iseq.location.label).as
$1 = {heap = {len = 7378148951706596193, ptr = 0x0, aux = {capa = 0, shared = 0}}, ary = "asdfasdf", '\000' <repeats 15 times>}

```


In this case you see `ary = "asdfasdf"` because the name of the current function is `asdfasdf`.
Neat! That’s pretty simple.


I was pretty specific about saying “on a Ruby 2.1 process” though. What about Ruby 2.2.3? 2.3.0?
1.9.3? 2.4.0? 2.5.0? Does this `ruby_current_thread.cfp.iseq.location.label` incantation change? Do
the internal struct layouts change? The answer is “yes”, and I’m trying to figure out how **often**
it changes


### 2 ways of decoding the stack: DWARF and including a header file


Suppose I want to “run” `ruby_current_thread.cfp.iseq.location.label` from a separate process
from my running Ruby program.  To be able to do this, I need to be able to get memory from the
Ruby program (which we’ll consider solved here) and then decode that memory into the right C
structs. How do you figure out how the memory maps to the C structs in the Ruby program? 2 possible ways!

1. Hope the Ruby process has DWARF debug symbols installed and use those (this is how gdb works)
2. Compile my profiler against the right Ruby header files ahead of time


pyflame uses approach #2 (it compiles against Python’s header files) and gdb uses approach #1 (it
has a DWARF parser built into it). The **reason** approach #2 works well for pyflame is that there
are only 3 different possible variations of header files that it needs to be aware of (python 2,
python 3.4, python 3.6).


Dealing with DWARF is a pain and not every Ruby process has debug symbols, so I’d prefer to be able
to use approach #2. This post is me trying to figure out what could get in the way of approach #2
working!


### questions I want to answer in this post


I’m interested in 2 questions:

- How many changes to the core Ruby structs to I need to know about? Is it just 3 or so (like with
Python) or are there a lot more?
- are there any `#ifdefs` I need to be worried about messing with my struct layout?


What’s this about ifdefs? Well, there are a bunch of places in the Ruby interpreter where it changes
the layout of its internal structs based on some compile time values.


```
typedef struct rb_thread_struct {
    struct list_node vmlt_node;
    VALUE self;
    rb_vm_t *vm;

    rb_execution_context_t *ec;

    VALUE last_status; /* $? */

    /* for cfunc */
    struct rb_calling_info *calling;

    /* for load(true) */
    VALUE top_self;
    VALUE top_wrapper;

    /* thread control */
    rb_nativethread_id_t thread_id;
#ifdef NON_SCALAR_THREAD_ID
    rb_thread_id_string_t thread_id_string;
#endif

```


### Structs I care about


I think the main structs I care about are `rb_thread_struct`, `rb_iseq_struct`,
`rb_iseq_location_struct`, and `rb_iseq_constant_body`. Here are links to
those struct definitions in 5 different Ruby versions.


**Ruby 2.1.0**

- [rb_thread_struct](https://github.com/ruby/ruby/blob/v2_1_0/vm_core.h#L524-L653)
- [rb_iseq_struct](https://github.com/ruby/ruby/blob/v2_1_0/vm_core.h#L206-L324)
- [rb_iseq_location_struct](https://github.com/ruby/ruby/blob/v2_1_0/vm_core.h#L196-L202)


**Ruby 2.2.0**

- [rb_thread_struct](https://github.com/ruby/ruby/blob/v2_2_0/vm_core.h#L600-L737)
- [rb_iseq_struct](https://github.com/ruby/ruby/blob/v2_2_0/vm_core.h#L197-L348)
- [rb_iseq_location_struct](https://github.com/ruby/ruby/blob/v2_2_0/vm_core.h#L187-L193)


**Ruby 2.3.0**

- [rb_thread_struct](https://github.com/ruby/ruby/blob/v2_3_0/vm_core.h#L666-L778)
- [rb_iseq_struct](https://github.com/ruby/ruby/blob/v2_3_0/vm_core.h#L390-L403)
- [rb_iseq_constant_body](https://github.com/ruby/ruby/blob/v2_3_0/vm_core.h#L267-L386)
- [rb_iseq_location_struct](https://github.com/ruby/ruby/blob/v2_3_0/vm_core.h#L259-L265)


**Ruby 2.4.0**

- [rb_thread_struct](https://github.com/ruby/ruby/blob/v2_4_0/vm_core.h#L699-L821)
- [rb_iseq_struct](https://github.com/ruby/ruby/blob/v2_4_0/vm_core.h#L392-L405)
- [rb_iseq_constant_body](https://github.com/ruby/ruby/blob/v2_4_0/vm_core.h#L272-L388)
- [rb_iseq_location_struct](https://github.com/ruby/ruby/blob/v2_4_0/vm_core.h#L264-L270)


**Ruby 2.5.0rc1**

- [rb_thread_struct](https://github.com/ruby/ruby/blob/v2_5_0_rc1/vm_core.h#L786-L854)
- [rb_iseq_struct](https://github.com/ruby/ruby/blob/v2_5_0_rc1/vm_core.h#L405-L420)
- [rb_iseq_constant_body](https://github.com/ruby/ruby/blob/v2_5_0_rc1/vm_core.h#L285-L401)
- [rb_iseq_location_struct](https://github.com/ruby/ruby/blob/v2_5_0_rc1/vm_core.h#L250-L256)


### Some changes

- In Ruby 2.2.0, there’s a new `struct list_node vmlt_node` at the beginning of `rb_thread_struct`. This was introduced
in [f11db2a60](https://github.com/ruby/ruby/commit/f11db2a60). I think 2.2.0 is the first release
that has that commit. Requires a new header file.
- In Ruby 2.2.0, there’s a new `stack_max` field in the `rb_iseq_struct` struct. Requires a new header file.
- In Ruby 2.3.0, most of the contents of the `rb_iseq_struct` struct are moved into the `struct rb_iseq_constant_body *body;` field. (so you need `iseq.body.location` instead of `iseq.location`). Requires a code change.
- In Ruby 2.4.0, the layout of `rb_iseq_constant_body` changes again. Requires a new header file.
- In Ruby 2.5.0, there’s a major refactor where the `ruby_current_thread` global variable is
replaced with `ruby_current_execution_context_ptr`. The `rb_thread_struct` struct is also
completely different. This change happens in [837fd5e49473](https://github.com/ruby/ruby/commit/837fd5e494731d7d44786f29e7d6e8c27029806f).
Requires code changes.


there are more changes that I haven’t found/cataloged yet, I might update this post later but for
now I’m bored.


### these are a lot of changes!


It seems like the situation with the Ruby structs defining the Ruby stack is very different from the
situation in Python – instead of only having 3 versions to worry about, the struct layouts of the
structs I care about change every major Ruby version. (and probably also in the minor versions
releases? I haven’t checked yet.). the two options I see right now are

- Use DWARF (because then I don’t have to worry about the struct layout changes, only the ones that
require code changes)
- Get headers for every minor Ruby version (2.3.1, 2.3.2, 2.3.3, 2.3.4, etc). I made [this quick list](https://gist.githubusercontent.com/jvns/6ea9a449dcb4c77f2cf8686bd3a2cd7e/raw/6c7004e70eba0f973f24ca5d7eb30bf027be2b21/ruby-versions.txt) and it seems like there are maybe.. 40 minor ruby versions? That is a lot but not an infinite amount. In Rust I could use bindgen to generate Rust bindings for all those ruby versions and just like.. commit all the versions into my repository. This seems kinda like more work up front but it would be nice to have all the possible weird struct definitions at compile time. And maybe I could get away with less than 40 versions somehow.


Quick aside: there’s an [interesting-looking research project by Stephen Kell called liballocs](https://github.com/stephenrkell/liballocs) which makes it easier to work with DWARF. Here’s [an example C file it generates (gzipped)](http://www.cl.cam.ac.uk/~srk31/private/tmp/libc-2.24.so-meta.c.gz) (from libc). Mostly linking to it so I remember to come back to it later.


That’s all for now! I’ll continue looking at this later.
