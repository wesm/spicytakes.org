---
title: "Parallelism and Serialization"
date: 2013-12-05
url: https://mrocklin.github.io/blog/work/2013/12/05/Parallelism-and-Serialization
slug: Parallelism-and-Serialization
word_count: 640
---

**tl;dr:**  Multiprocessing in Python is crippled by  `pickle` s poor function
serialization.  The more robust serialization package  `dill`  improves the
situation.  Dill-based solutions for both  `multiprocessing`  and
IPython.parallel make distributed computing simple again.

To leverage the cores found in modern processors we need to communicate
functions between different processes.  I.e. if we have some function in one
process

then we need to communicate that functionality  *and all functionality on which
it depends*  to our other worker processes.

To communicate this function we translate it down into a blob of text, ship
that text over a wire, and then retranslate that text back into a fully
operational function.  This process, called  *serialization* , is like
the teleporters in Star Trek; it takes an important thing (function or crew
member) translates it into something manageable (text or bits) moves it quickly
to some other location, and then reassembles it correctly (we hope!)  Just as
accidents happen in Star Trek it’s easy for function serialization to go awry.

### Pickle

The standard serialization package in Python is  `pickle` .  The  `pickle`  package
can serialize and deserialize most Python objects, not just functions.

How does Pickle go about serializing functions?

Pickle specifies a function using its module name (see  `math`  on the left) and
its function name (see  `sin`  in the middle).  Sadly this approach fails for
many cases.  In particular  `pickle`  fails to serialize the following

* Methods
* Lambdas
* Closures
* Some functions defined interactively

Most large projects use at least one (often all) of these features.  This makes
multiprocessing a pain.

### Multiprocessing

We care about function serialization because we want to send one function to
many processes in order to leverage parallelism.  The standard way to do this
is with the  `multiprocessing`  module.  One simple approach is with the  `Pool` 
abstraction

But  `multiprocessing`  uses  `pickle`  and so inherits its limitations.  Here it
fails to serialize and broadcast a lambda  `square`  function.

I rarely see  `multiprocessing`  in the wild.  I suspect that this is because
poor function serialization makes it a pain for any but the most trivial
of projects.

### `dill`  replaces  `pickle`

The  `dill`  library is a drop-in alternative to  `pickle`  that  *can*  robustly
handle function serialization.

As a result most of the speed-bumps of using multiprocessing  *should* 
disappear.

### Dill and Multiprocessing

The makers of  `dill`  apparently know this and so have developed their own fork
of  `multiprocessing`  that uses dill.  This resides in the  `pathos`  library

### Dill and IPython Parallel

You should know about IPython parallel.

The IPython notebook has gotten a lot of press recently.  The notebook became
possible after the project was restructured to separate computation and
interaction.  One important result is that we can now perform computation in a
process while interacting in a web browser, giving rise to the ever-popular notebook.

This same computation-is-separate-from-interaction concept supports other
innovations.  In particular IPython parallel uses this to create a simple
platform for both multiprocessing and distributed computing.

```
mrocklin@notebook:~$ ipcluster start --n=4
mrocklin@notebook:~$ ipython
```

Note that this system handles the lambda without failing.  IPython performs
some custom serializations on top of  `pickle` .  Unfortunately these
customizations still don’t cover  *all*  use cases.  Fortunately IPython provides
hooks to specify your preferred serialization technique.  Thanks to a recent
change, IPython views now provide a convenient  `.use_dill`  method.

A more explicit treatment of switching IPython’s serializers to dill can be
found in  [this notebook](http://nbviewer.ipython.org/5241793) .

## Acknowledgements

My interest into multiprocessing and serialization was originally spurred by a
talk by  [Ian Langmore](http://ianlangmore.com/about) .

The  `dill`  project is developed by  [Mike
Mckerns](http://www.cacr.caltech.edu/~mmckerns/my) .  Several people have
pointed it out to me.  These include
 [@asmeurer](https://github.com/asmeurer) ,
 [@themodernscientist](https://twitter.com/themodernscientist) ,
 [@twiecki](https://twitter.com/TWiecki) ,
and  [@lidavidm](https://github.com/lidavidm) .

## Issues

Thanks to  [@mmckerns](http://www.cacr.caltech.edu/~mmckerns/my)  and
 [@minrk](https://github.com/minrk/)  for their recent interactions to resolve
issues related to this topic.

* [https://github.com/uqfoundation/dill/issues/15](https://github.com/uqfoundation/dill/issues/15)
* [https://github.com/uqfoundation/pathos/issues/2](https://github.com/uqfoundation/pathos/issues/2)
* [https://github.com/ipython/ipython/issues/4551](https://github.com/ipython/ipython/issues/4551)
