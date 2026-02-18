---
title: "Why Ruby’s Timeout is dangerous (and Thread.raise is terrifying)"
date: 2015-11-27
url: https://jvns.ca/blog/2015/11/27/why-rubys-timeout-is-dangerous-and-thread-dot-raise-is-terrifying/
slug: why-rubys-timeout-is-dangerous-and-thread-dot-raise-is-terrifying
word_count: 923
---


This is already documented in [Timeout: Ruby’s most dangerous API](http://www.mikeperham.com/2015/05/08/timeout-rubys-most-dangerous-api/). And normally I don’t like making blanket statements about language features. But I had a bad day at work because of this issue. So today, we’re talking about Timeout! :)


First! What is Timeout? Let’s say you have a bunch of code, that might be slow. A network request, a long computation, whatever.  Ruby’s [timeout documentation](http://ruby-doc.org/stdlib-2.1.2/libdoc/timeout/rdoc/Timeout.html) helpfully says


> Timeout provides a way to auto-terminate a potentially long-running operation if it hasn’t finished in a fixed amount of time.


```
require 'timeout'
status = Timeout::timeout(5) {
  # Something that should be interrupted if it takes more than 5 seconds...
}

```


AWESOME. This is so much easier than wrangling network socket options which might be set deep inside some client library. Seems great!


I tried using Timeout at work last week, and it resulted in an extremely difficult to track down bug. I felt awesome about tracking it down, and upset with myself about creating it in the first place. Let’s talk a little more about this (mis)feature.


## Timeout: how it works (and why Thread.raise is terrifying)


Its implementation originally seems kind of clever. You can read [the code here](https://github.com/ruby/ruby/blob/trunk/lib/timeout.rb#L72). It starts a new thread, which sets the original thread to `x`, sleeps for 5 seconds, then raises an exception on the main thread when it’s done, interrupting whatever it was doing.


```
begin
  sleep sec
rescue => e
  x.raise e
else
  x.raise exception, message
end

```


Let’s look at the documentation on [Thread.raise](http://ruby-doc.org/core-1.9.3/Thread.html#method-i-raise). It says:


> Raises an exception (see Kernel::raise) from thr. The caller does not have to be thr.


This is where the implications get interesting, and terrifying. This means that an exception can get raised:

- during a network request (ok, as long as the surrounding code is prepared to catch `Timeout::Error`)
- during the cleanup for the network request
- during a `rescue` block
- while creating an object to save to the database afterwards
- in **any** of your code, regardless of whether it could have possibly raised an exception before


Nobody writes code to defend against an exception being raised **on literally any line**. That’s not even possible. So `Thread.raise` is basically like a sneak attack on your code that could result in almost anything. It would probably be okay if it were pure-functional code that did not modify any state. But this is Ruby, so that’s unlikely :)


Timeout uses Thread.raise, so it is not safe to use.


## Other languages and Thread.raise


So, how do other languages approach this? Go doesn’t have exceptions, Javascript doesn’t have threads – let’s talk about Python, Java, and C#, and C++.


**Java** has [java.lang.Thread.stop](http://docs.oracle.com/javase/6/docs/api/java/lang/Thread.html#stop%28java.lang.Throwable%29), which does essentially the same thing. It was deprecated in Java 1.2, in 1998, disabled entirely in Java 8, and its documentation reads:


> **Deprecated.** This method is inherently unsafe. See stop() for details. An additional danger of this method is that it may be used to generate exceptions that the target thread is unprepared to handle (including checked exceptions that the thread could not possibly throw, were it not for this method). For more information, see [Why are Thread.stop, Thread.suspend and Thread.resume Deprecated?.](http://docs.oracle.com/javase/6/docs/technotes/guides/concurrency/threadPrimitiveDeprecation.html)


**Python** has [thread.interrupt_main()](https://docs.python.org/2/library/thread.html#thread.interrupt_main), which does the same thing as Ctrl+C-ing a program from your terminal. I’m not really sure what to say about this – certainly using `thread.interrupt_main()` also isn’t really a good idea, and it’s more limited in what it can do. I can’t find any reference to anybody considering using it for anything serious.


**C#** has `Thread.Abort()` which throws a `ThreadAbortException` in the thread. Googling it finds me a series of [StackOverflow discussions](http://stackoverflow.com/questions/1559255/whats-wrong-with-using-thread-abort) & forum posts about how it’s dangerous and should not be used, for the reasons we’ve learned about.


**C++**: `std::thread`s [are not interruptible](http://en.cppreference.com/w/cpp/thread/thread).


## Not just an implementation issue


This is not just an implementation issue in Ruby, and you can read [a great comment on Reddit illustrating this](https://www.reddit.com/r/programming/comments/3ui1sw/why_rubys_timeout_is_dangerous_and_threadraise_is/cxfg98b). The whole premise of a general timeout method that will interrupt an arbitrary block of code like this is flawed. Here’s the API again:


```
require 'timeout'
status = Timeout::timeout(5) {
  # Something that should be interrupted if it takes more than 5 seconds...
}

```


There is no way to safely interrupt an arbitrary block of code. **Anything** could be happening at the end of that 5 seconds.


However! All is not lost if we would like to interrupt our threads. Let’s turn to Java again! (you know all the times we say Ruby is more fun than Java? TODAY JAVA IS MORE FUN BECAUSE IT MAKES MORE SENSE.) Java has a [Thread.interrupt](https://docs.oracle.com/javase/tutorial/essential/concurrency/interrupt.html) method, which sends `InterruptedException` to a thread. But an InterruptedException is only allowed to be thrown at specific times, for instance during `Thread.sleep`. Otherwise the thread needs to explicitly call `Thread.interrupted()` to see if it’s supposed to stop.


## On documentation


I don’t know. It’s possible that everybody knew that `Timeout` was a disaster except for me, and that I should have thought more carefully about what the implications of this `Thread.raise` were. But I’m thinking of making a pull request on the Ruby documentation with slightly stronger language than


> Timeout provides a way to auto-terminate a potentially long-running operation if it hasn’t finished in a fixed amount of time.


and


> Raises an exception (see Kernel::raise) from thr. The caller does not have to be thr.


The Java approach (where they deprecated it with a strong warning and then disabled the method entirely) seems more like the right thing.
