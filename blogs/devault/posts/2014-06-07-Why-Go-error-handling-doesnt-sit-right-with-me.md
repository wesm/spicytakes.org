---
title: "Go's error handling doesn't sit right with me"
date: 2014-06-07
url: https://drewdevault.com/2014/06/07/Why-Go-error-handling-doesnt-sit-right-with-me.html
slug: Why-Go-error-handling-doesnt-sit-right-with-me
word_count: 621
---

I’ll open up by saying that I am not a language designer, and I do like a lot of
things about Go. I just recently figured out how to describe why Go’s error
handling mechanics don’t sit right with me.

If you aren’t familiar with Go, here’s an example of how Go programmers might do
error handling:

```
result, err := SomethingThatMightGoWrong()
if err != nil {
    // Handle error
}
// Proceed
```

Let’s extrapolate this:

```
func MightFail() {
    result, err := doStuffA()
    if err != nil {
        // Error handling omitted
    }
    result, err = doStuffB()
    if err != nil {
        // Error handling omitted
    }
    result, err = doStuffC()
    if err != nil {
        // Error handling omitted
    }
    result, err = doStuffD()
    if err != nil {
        // Error handling omitted
    }
}
```

Go has good intentions by removing exceptions. They add a lot of overhead and
returning errors isn’t a bad thing in general. However, I spend a lot of my time
writing assembly. Assembly can use similar mechanics, but I’m spoiled by it (I
know, spoiled by assembly?) and I can see how Go could have done better. In
assembly,  `goto`  (or instructions like it) are the only means you have of
branching. It’s not like other languages where it’s taboo - you pretty much  *have* 
to use it. Most assembly also makes it fancy and conditional. For example:

```
goto condition, label
```

This would jump to  `label`  given that  `condition`  is met. Like Go, assembly
generally doesn’t have exceptions or anything similar. In my own personal flavor
of assembly, I have my functions return error codes as well.  Here’s how it’s
different, though. Let’s look at some code:

```
call somethingThatMightFail
jp nz, errorHandler
call somethingThatMightFailB
jp nz, errorHandler
call somethingThatMightFailC
jp nz, errorHandler
call somethingThatMightFailD
jp nz, errorHandler
```

The difference here is that all functions return errors in the same way - by
resetting the Z flag. If that flag is set, we do a quick branch (the  `jp` 
instruction is short for  `jump` ) to the error handler. It’s not clear from looking
at this snippet, but the error code is stored in the A register, which the
 `errorHandler`  recognizes as an error code and shows an appropriate message for.
We can have one error handler for an entire procedure, and it feels natural.

In Go, you have to put an if statement here. Each error caught costs you three
lines of code in the middle of your important logic flow. With languages that
throw exceptions, you have all the logic in a readable procedure, and some error
handling at the end of it all. With Go, you have to throw a bunch of
3-line-minimum error handlers all over the middle of your procedure.

In my examples, you can still return errors like this, but you can do so with a
lot less visual clutter. One line of error handling is better than 3 lines, if you
ask me. Also, no one gives a damn how you format assembly code, so if you wanted
to do something like this you’d be fine:

```
call somethingThatMightFail
  jp nz, errorHandler
call somethingThatMightFailB
  jp nz, errorHandler
call somethingThatMightFailC
  jp nz, errorHandler
call somethingThatMightFailD
  jp nz, errorHandler
```

Or something like this:

```
call somethingThatMightFail  \ jp nz, errorHandler
call somethingThatMightFailB \ jp nz, errorHandler
call somethingThatMightFailC \ jp nz, errorHandler
call somethingThatMightFailD \ jp nz, errorHandler
```

The point is, I think Go’s error handling stuff make your code harder to read and
more tedious to write. The basic idea - return errors instead of throwing them -
has good intentions. It’s just that how they’ve done it isn’t so great.
