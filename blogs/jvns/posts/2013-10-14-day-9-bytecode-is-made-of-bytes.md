---
title: "Day 9: Bytecode is made of bytes! CPython isn't scary!"
date: 2013-10-14
url: https://jvns.ca/blog/2013/10/14/day-9-bytecode-is-made-of-bytes/
slug: day-9-bytecode-is-made-of-bytes
word_count: 332
---


Today I paired with one of the fantastic Hacker School facilitators,
[Allison](http://akaptur.github.io/)  on fixing some bugs in a bytecode
interpreter. [byterun](https://github.com/nedbat/byterun) is a pure python interpreter for the bytecode that
CPython generates, written for learning & fun times.


Allison has a
[great blog post](http://akaptur.github.io/blog/2013/08/14/python-bytecode-fun-with-dis/)
about how to use the `dis` module to look at
the bytecode for a function which you should totally read.


## A few things I learned


The CPython interpreter is mostly in one 3,500 file called `ceval.c` ([see it on github!](https://github.com/python/cpython/blob/master/Python/ceval.c)). The main part of this file is a 2,000-line switch statement – `switch(opcode) {...`. Ack.


But! This file is surprisingly not-scary. Or Allison is just amazing at making
things seem not scary. So for example there’s a `BINARY_SUBTRACT` opcode
which, well, subtracts things.


Here’s the actual for serious C code that handles this:


```
TARGET(BINARY_SUBTRACT) {
    PyObject *right = POP();
    PyObject *left = TOP();
    PyObject *diff = PyNumber_Subtract(left, right);
    Py_DECREF(right);
    Py_DECREF(left);
    SET_TOP(diff);
    if (diff == NULL)
        goto error;
    DISPATCH();
}

```


{:lang=‘c’}


So, what does this do?

1. Get the arguments off the stack
2. Subtract them by looking up `left.__sub__(right)`
3. Decrease the number of references to `left` and `right` for garbage collection reasons
4. Put the result on the stack
5. If `__add__` doesn’t return anything, throw an exception
6. `DISPATCH()`, which basically just means “go to the next instruction”


I could TOTALLY WRITE THAT.


We spent some time reading the C code that deals with exception handling in
Python. It was pretty confusing, but I learned that you can do `raise ValueError from Exception` to set the cause of an exception.


Basically the lesson here is

1. Allison is the best. Pairing with her on [byterun](https://github.com/nedbat/byterun) is the most fun thing
2. It’s actually possible to read the C code that runs Python!
3. Bytecode is made of bytes. Like, there are less than 256 instructions and each one is a byte. I did not realize this until today. Laugh all you want =D
