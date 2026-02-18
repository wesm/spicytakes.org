---
title: "How do Ruby & Python profilers work?"
date: 2017-12-17
url: https://jvns.ca/blog/2017/12/17/how-do-ruby---python-profilers-work-/
slug: how-do-ruby---python-profilers-work-
word_count: 2133
---


Hello! As a precursor to writing a Ruby profiler I wanted to do a survey of how existing Ruby &
Python profilers work. This also helps answer a question a lot of folks have been asking me, which
is “How **do** you write a profiler?”


In this post, we’re just going to focus on CPU profilers (and not, say, memory/heap profilers). I’ll
explain some basic general approaches to writing a profiler, give some code examples, and take a
bunch of examples of popular Ruby & Python profilers and tell you how they work under the hood.


There are probably some mistakes in this post (as research for this post I read parts of the code
for 14 different profiling libraries and most of those I hadn’t looked at before today), please let
me know what they are!


### 2 kinds of profilers


There are 2 basic kinds of CPU profilers – **sampling** profilers and **tracing** profilers.


Tracing profilers record every function call your program makes and then print out a report at
the end. Sampling profilers take a more statistical approach – they record your program’s stack
every few milliseconds and then report the results.


The main reason to use a sampling profiler instead of a tracing profiler is that sampling profilers
are lower overhead. If you just take 20 or 200 samples a second, that’s not very time consuming. And
they’re pretty effective – if you’re having a serious performance problem (like 80% of your time is
being spent in 1 slow function), 200 samples a second will often be enough to figure out which
function to blame!


### The profilers


Here’s a summary of the profilers we’ll be discussing in this post. (from [this gist](https://gist.github.com/jvns/b81eb039f6373bc577d7dbdd978581b5)). I’ll explain the jargon in this table (`setitimer`, `rb_add_event_hook`, `ptrace`) a bit later on. The interesting thing here is that all profilers are implemented using a pretty small set of fundamental capabilities.


**Python profilers**



| Name | Kind | How it works |
| [cProfile](https://docs.python.org/2/library/profile.html#module-cProfile) | Tracing | `PyEval_SetProfile` |
| [line_profiler](https://github.com/rkern/line_profiler) | Tracing | `PyEval_SetTrace` |
| [pyflame](https://github.com/uber/pyflame) ([blog post](https://eng.uber.com/pyflame/)) | Sampling | ptrace + custom timing |
| [stacksampler](https://github.com/nylas/nylas-perftools) | Sampling | setitimer |
| [statprof](https://github.com/bos/statprof.py) | Sampling | setitimer |
| [vmprof](https://github.com/vmprof/vmprof-python) | Sampling | setitimer |
| [pyinstrument](https://github.com/joerick/pyinstrument) | Sampling | `PyEval_SetProfile` |
| [gprof](https://bitbucket.org/rushman/gprof) (greenlet) | Tracing | [greenlet.settrace](https://greenlet.readthedocs.io/en/latest/#tracing-support) |
| [python-flamegraph](https://github.com/evanhempel/python-flamegraph) | Sampling | profiling thread + custom timing |
| [gdb hacks](http://poormansprofiler.org/) | Sampling | ptrace |



“gdb hacks” isn’t a Python profiler exactly – it links to website talking about how to implement a
hacky profiler as a shell script wrapper around gdb. It’s relevant to Python because newer versions
of gdb will actually unwind the Python stack for you. Kind of a poor man’s pyflame.


**Ruby profilers**



| Name | Kind | How it works |
| [stackprof](https://github.com/tmm1/stackprof) by tmm1 | Sampling | setitimer |
| [perftools.rb](https://github.com/tmm1/perftools.rb) by tmm1 | Sampling | setitimer |
| [rblineprof](https://github.com/tmm1/rblineprof) by tmm1 | Tracing | `rb_add_event_hook` |
| [ruby-prof](https://github.com/ruby-prof/ruby-prof) | Tracing | `rb_add_event_hook` |
| [flamegraph](https://github.com/SamSaffron/flamegraph) | Sampling | stackprof gem |



### Almost all of these profilers live inside your process


Before we start getting into the details of these profilers there’s one really important thing –
all of these profilers except `pyflame` run **inside** your Python/Ruby process. If you’re inside a
Python/Ruby program you generally have pretty easy access to its stack. For example here’s a simple
Python program that prints the stack of every running thread:


```
import sys
import traceback

def bar():
    foo()

def foo():
    for _, frame in sys._current_frames().items():
        for line in traceback.extract_stack(frame):
            print line

bar()

```


Here’s the output. You can see that it has the function names from the stack, line numbers,
filenames – everything you might want to know if you’re profiling.


```
('test2.py', 12, '<module>', 'bar()')
('test2.py', 5, 'bar', 'foo()')
('test2.py', 9, 'foo', 'for line in traceback.extract_stack(frame):')

```


In Ruby, it’s even easier: you can just `puts caller` to get the stack.


Most of these profilers are C extensions for performance reasons so they’re a little different but C
extensions to Ruby/Python programs also have really easy access to the call stack.


### How tracing profilers work


I did a survey of all the Ruby & Python tracing profilers in the tables above: `rblineprof`,
`ruby-prof`, `line_profiler`, and `cProfile`. They all work basically the same way. All of them
record all function calls and are written as C extensions to reduce overhead.


How do they work? Well, both Ruby and Python let you specify a callback that gets run when various
interpreter events (like “calling a function” or “executing a line of code”) happen. When the
callback gets called, it records the stack for later analysis.


I think it’s useful to look exactly where in the code these callbacks get set up so I’ll link to the
relevant line of code on github for all of these.


In Python, you can set up that callback with `PyEval_SetTrace` or `PyEval_SetProfile`. It’s
documented in this [Profiling and Tracing](https://docs.python.org/3/c-api/init.html#c.Py_tracefunc)
section of the Python documentation. The docs say “`PyEval_SetTrace` is similar to
`PyEval_SetProfile`, except the tracing function does receive line-number events.”


The code:

- `line_profiler` sets up its callback using `PyEval_SetTrace`: see [line_profiler.pyx line 157](https://github.com/rkern/line_profiler/blob/4e3ce5957932806da86cbe27c75470c105d51acf/_line_profiler.pyx#L157-L158)
- `cProfile` sets up its callback using `PyEval_SetProfile`: see [_lsprof.c line 693](https://github.com/python/cpython/blob/1b7c11ff0ee3efafbf5b38c3c6f37de5d63efb81/Modules/_lsprof.c#L693) (cProfile is [implemented using lsprof](https://github.com/python/cpython/blob/1b7c11ff0ee3efafbf5b38c3c6f37de5d63efb81/Lib/cProfile.py#L9))


In Ruby, you can set up a callback with `rb_add_event_hook`. I couldn’t find any documentation for
this but here’s how it gets called


```
rb_add_event_hook(prof_event_hook,
      RUBY_EVENT_CALL | RUBY_EVENT_RETURN |
      RUBY_EVENT_C_CALL | RUBY_EVENT_C_RETURN |
      RUBY_EVENT_LINE, self);

```


The type signature of `prof_event_hook` is


```
static void
prof_event_hook(rb_event_flag_t event, VALUE data, VALUE self, ID mid, VALUE klass)

```


This seems pretty similar to Python’s `PyEval_SetTrace`, but more flexible – you can pick which
events you want to be notified about (like “just function calls”).


The code:

- `ruby-prof` calls `rb_add_event_hook` here: [ruby-prof.c line 329](https://github.com/ruby-prof/ruby-prof/blob/9465159ad4ac3dc97b607106bc7b09da3c629389/ext/ruby_prof/ruby_prof.c#L329)
- `rblineprof` calls `rb_add_event_hook` here: [rblineprof.c line 649](https://github.com/tmm1/rblineprof/blob/6030b7c696779bb733fc4101346975f8e5d13911/ext/rblineprof.c#L649)


### Disadvantages of tracing profilers


The main disadvantage of tracing profilers implemented in this way is that they introduce a fixed
amount for every function call / line of code executed. This can cause you to make incorrect
decisions! For example, if you have 2 implementations of something – one with a lot of function
calls and one without, which take the same amount of time, the one with a lot of function calls will
**appear** to be slower when profiled.


To test this a tiny bit, I made a small file called `test.py` with the following contents and
compared the running time of `python -mcProfile test.py` and `python test.py`. `python test.py` ran
in about 0.6s and `python -mcProfile test.py` ran in about 1s. So for this particular pathological
example `cProfile` introduced an extra ~60% overhead.


```
def recur(n):
    if n == 0:
        return
    recur(n-1)

for i in range(5000):
    recur(700)

```


The documentation for cProfile says:


> the interpreted nature of Python tends to add so much overhead to execution, that deterministic
> profiling tends to only add small processing overhead in typical applications


This seems like a pretty reasonable assertion – the example program earlier (which does 3.5 million function
calls and nothing else) obviously isn’t a typical Python program, and almost any other program would
have less overhead.


I didn’t test `ruby-prof` (a Ruby tracing profiler)’s overhead, but its README says:


> Most programs will run approximately twice as slow while highly recursive programs (like the
> fibonacci series test) will run three times slower.


### How sampling profilers mostly work: setitimer


Time to talk about the second kind of profiler: sampling profilers!


Most Ruby & Python sampling profilers are implemented using the `setitimer` system call.
What’s that?


Well – let’s say you want to get a snapshot of a program’s stack 50 times a second. A way to do
that is:

- Ask the Linux kernel to send you a signal every 20 milliseconds (using the `setitimer` system
call)
- Register a signal handler to record the stack every time you get a signal.
- When you’re done profiling, ask Linux to stop sending you signals and print the output!


If you want to see a practical example of `setitimer` being used to implement a sampling profiler, I
think [stacksampler.py](https://github.com/nylas/nylas-perftools/blob/2e9f72ee74587e0dea5ba4826cd60a093c8869f0/stacksampler.py) is the best example – it’s a useful, working, profiler, and it’s only about 100 lines of Python. So cool!


A reason stacksampler.py is only 100 lines in Python is – when you register a Python function
as a signal handler, the function gets passed in the current stack of your Python program. So the
signal handler `stacksampler.py` registers is really simple:


```
def _sample(self, signum, frame):
   stack = []
   while frame is not None:
       stack.append(self._format_frame(frame))
       frame = frame.f_back

   stack = ';'.join(reversed(stack))
   self._stack_counts[stack] += 1

```


It just gets the stack out of the frame and increases the number of times that particular stack has
been seen by one. Very simple! Very cool!


Let’s go through all the rest of our profilers that use `setitimer` and find where in their
code they call `setitimer`:

- `stackprof` (Ruby): in [stackprof.c line 118](https://github.com/tmm1/stackprof/blob/578043c0bc218509218134f9f91c21dab808c7ff/ext/stackprof/stackprof.c#L118)
- `perftools.rb` (Ruby): in [this patch which seems to be applied when the gem is compiled (?)](https://github.com/tmm1/perftools.rb/blob/82122f4d47539483fd341c0c8f48cfe032580474/patches/perftools-objects.patch#L28)
- `stacksampler` (Python): [stacksampler.py line 51](https://github.com/nylas/nylas-perftools/blob/2e9f72ee74587e0dea5ba4826cd60a093c8869f0/stacksampler.py#L51)
- `statprof` (Python): [statprof.py line 239](https://github.com/bos/statprof.py/blob/1a33eba91899afe17a8b752c6dfdec6f05dd0c01/statprof.py#L239)
- `vmprof` (Python): [vmprof_unix.c line 294](https://github.com/vmprof/vmprof-python/blob/660fda55c004033fac9fd27017af2450c6bd904f/src/vmprof_unix.c#L294)


One important thing about `setitimer` is that you need to decide **how to count time**. Do you want
20ms of real “wall clock” time? 20ms of user CPU time? 20 ms of user + system CPU time? If you look
closely at the call sites above you’ll notice that these profilers actually make different choices about how to `setitimer`
– sometimes it’s configurable, and sometimes it’s not. The [setitimer man page](http://man7.org/linux/man-pages/man2/setitimer.2.html) is short and worth reading to understand all the options.


[@mgedmin on twitter](https://twitter.com/mgedmin/status/942789932128534528) pointed out one
interesting downside of using `setitimer`. [this issue](https://github.com/23andMe/djdt-flamegraph/issues/4)  and [this issue](https://github.com/23andMe/djdt-flamegraph/issues/5) have a bit more detail.


> One INTERESTING downside of setitimer-based profilers is that the timers cause signals!  Signals sometimes interrupt system calls!  System calls sometimes take a few milliseconds!  If you sample too frequently, you can make your program keep retrying the same syscall *forever*!


### Sampling profilers that don’t use setitimer


There are a few sampling profilers that doesn’t use `setitimer`:

- `pyinstrument` uses `PyEval_SetProfile` (so it’s sort of a tracing profiler in a way), but it
doesn’t always collect stack samples when its tracing callback is called. Here’s [the code that chooses when to sample a stack trace](https://github.com/joerick/pyinstrument/blob/15b94a63693837b97daea60e717ae835f77b7635/pyinstrument/profiler.py#L41-L45) See [this blog post](http://joerick.me/posts/2017/12/15/pyinstrument-20/) for more on that decision. (basically: `setitimer` only lets you profile the main thread in Python)
- `pyflame` profiles Python code from outside of the process using the `ptrace` system call. It basically just does a loop where it
grabs samples, sleeps, and repeats. Here’s the [call to sleep](https://github.com/uber/pyflame/blob/4a9c3dea4939261b0c1becb77ec700426aa1f2fb/src/prober.cc#L403).
- `python-flamegraph` takes a similar approach where it starts a new thread in your Python process
and basically grabs stack traces, sleeps, and repeats. Here’s the [call to sleep](https://github.com/evanhempel/python-flamegraph/blob/6b70f9068cb987a2b1942fbf048fc88a7a644c40/flamegraph/flamegraph.py#L73).


All 3 of these profilers sample using wall clock timing.


### pyflame blog posts


I spent almost all my time in this post on profilers other than `pyflame` but `pyflame` is actually
the one I’m the most interested in because it profiles your Python program from a separate process,
and that’s how I want my Ruby profiler to work too.


There’s a lot more to how it does that. I won’t get into it here but Evan Klitzke has written
a lot of really good blog posts about it:

- [Pyflame: Uber Engineering’s Ptracing Profiler for Python](https://eng.uber.com/pyflame/)
introducing pyflame
- [Pyflame Dual Interpreter Mode](https://eklitzke.org/pyflame-dual-interpreter-mode) about how it
supports both Python 2 and Python 3 at the same time
- [An Unexpected Python ABI Change](https://eklitzke.org/an-unexpected-python-abi-change) on adding
Python 3.6 support
- [Dumping Multi-Threaded Python Stacks](https://eklitzke.org/dumping-multi-threaded-python-stacks)
- [Pyflame packages](https://eklitzke.org/pyflame-packages)
- an [interesting issue with ptrace + syscalls in Python](https://github.com/eklitzke/ptrace-syscall)
- [Using ptrace for fun and profit](https://eklitzke.org/ptrace), [ptrace (continued)](https://eklitzke.org/ptrace-continued)


and there’s more at [https://eklitzke.org/](https://eklitzke.org/). All really interesting stuff that I’m going to read more
carefully – maybe ptrace is a better approach than `process_vm_readv` for implementing a Ruby
profiler! `process_vm_readv` is lower overhead because it doesn’t stop the process, but it also can
give you an inconsistent snapshot because it doesn’t stop the process :). In my experiments getting
inconsistent snapshots wasn’t too big of a problem but I think I’ll do some experimentation here.


### That’s all for now!


There are a lot of important subtleties I didn’t get into in this post – for example I basically
said `vmprof` and `stacksampler` are the same (they’re not – vmprof supports line profiling and
profiling of Python functions written in C, which I believe introduces more complexity into the
profiler). But some of the fundamentals are the same and so I think this survey is a good starting
point.
