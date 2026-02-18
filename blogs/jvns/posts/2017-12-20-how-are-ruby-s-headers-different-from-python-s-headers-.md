---
title: "How are Ruby's headers different from Python's headers?"
date: 2017-12-20
url: https://jvns.ca/blog/2017/12/20/how-are-ruby-s-headers-different-from-python-s-headers-/
slug: how-are-ruby-s-headers-different-from-python-s-headers-
word_count: 1108
---


This is another research-y post, most things in here I learned in the last 24 hours so likely some
of it is wrong.


Today and yesterday I’ve been trying to figure out how the public header files Ruby exposes are
different from the header files Python exposes (how are their public C APIs different?). You can get
these headers in the libruby-dev / libpython-dev Debian packages. These header files live in
/usr/include/{ruby-2.3.0|python-VERSION} on my laptop, and they’re one of the interfaces that
Python/Ruby provide that I don’t usually think about that much. These header files are what you use
when you’re writing a C extension for the language (like numpy) or embedding the language.


My stake in this is that I’m trying to do for Ruby essentially what [pyflame](https://github.com/uber/pyflame) does for Python, so understanding how Ruby is different from Python is very useful to me. pyflame uses Python’s public headers. Can my profiler use the corresponding Ruby headers? I don’t think so!


A reason these are important is that there’s an expectation that they be somewhat stable – obviously they change from version to version sometimes, but they need to be more stable than Python/Ruby’s internal header files. The [structs I was talking about yesterday](https://jvns.ca/blog/2017/12/19/how-much-does-the-ruby-abi-change-/) are all **internal** Ruby VM structs, so they change a lot.


### Python is embeddable


One fact that I learned yesterday is – you can embed Python in your C programs! Here are the [docs on embedding Python](https://docs.python.org/2/extending/embedding.html). Some examples of programs that embed Python include Sublime Text, Maya, Blender, Inkscape, Nuke – a lot of graphics / 3D modelling programs. There are more listed at on [Python’s Wikipedia page](https://en.wikipedia.org/wiki/Python_(programming_language)#Uses).


I also found this [argument/rant from Glyph that you shouldn’t embed Python](https://twistedmatrix.com/users/glyph/rant/extendit.html) interesting reading.


### Ruby is embeddable


There isn’t any documentation on [http://ruby-lang.org](http://ruby-lang.org)  (that I can find) about embedding Ruby. But when I said on twitter that ruby wasn’t embeddable, Matz replied and said “CRuby is also embeddable. But mruby has better API for embedding.” Obviously he’s right that CRuby is embeddable, so let’s find out what’s up!


First – [https://github.com/mruby/mruby](https://github.com/mruby/mruby) is a lightweight implementation of Ruby intended for embedding. The README says that the syntax is Ruby 1.9 compatible. Neat!


But what about CRuby being embeddable? Let’s investigate that. The first point of documentation is [doc/extension.rdoc](https://github.com/ruby/ruby/blob/098c8d5491add1475dbf7fb8889bd53f47d5c8ca/doc/extension.rdoc) in the Ruby repo (previously called README.ext). The most useful docs I found was [the Pragmatic Programmer chapter “Extending Ruby”](http://ruby-doc.com/docs/ProgrammingRuby/html/ext_ruby.html).


mruby seems to be more popular for embedding than CRuby but at least one popular program embeds
CRuby/MRI: [RPG Maker](http://www.rpgmakerweb.com/)! (thanks to [Florian](https://twitter.com/Argorak/status/943546606808334337) for pointing this out)


### Cool example of embedding Ruby: filtering syscalls!


Quick tangent: this slide deck on [hijacking syscalls with Ruby](https://speakerdeck.com/franckverrot/rubykaigi-2016-hijacking-syscalls-with-ruby) from Franck Verrot is really interesting! Basically it describes a way to make sure that your programs are only running ‘allowed’ system calls. Here’s how it works as far as I can tell:


Create a .so library that uses embedded ruby to load a ‘policy.rb’ file that dynamically filters / logs system calls
Add that library to your LD_LIBRARY_PATH for the programs you want to check


The slide deck says that this was reasonably efficient.


Anyway, this is not about cool ways to embed Ruby. Let’s move on.


### Ruby bindings: Everything is a VALUE


One surprising/interesting thing to me about the Ruby headers – the type returned by almost every function is `VALUE`. The equivalent to that for Python seems to be `PyObject` but there are more types than PyObject in there. And PyObject has a [struct definition](https://github.com/python/cpython/blob/1f1a34c3145781628e10534440017b3b43211a60/Include/object.h#L106-L110), whereas VALUE is an opaque pointer (`typedef uintptr_t VALUE;`).


To get an idea of what “everything returns `VALUE`” looks like in practice, here are the functions you can use to define classes in Ruby:


```
VALUE  rb_define_class(char *name, VALUE superclass")
   Defines a new class at the top level with the given name and superclass (for class Object, use rb_cObject). 
VALUE  rb_define_module(char *name")
   Defines a new module at the top level with the given name. 
VALUE  rb_define_class_under(VALUE under, char *name, VALUE superclass")
   Defines a nested class under the class or module under. 
VALUE  rb_define_module_under(VALUE under, char *name")
   Defines a nested module under the class or module under. 
void  rb_include_module(VALUE parent, VALUE module")
   Includes the given module into the class or module parent. 
void  rb_extend_object(VALUE obj, VALUE module")
   Extends obj with module. 
VALUE  rb_require(const char *name")
   Equivalent to ``require name.'' Returns Qtrue or Qfalse. 

```


### Structs Ruby and Python expose in their bindings


Let’s talk about structs! In the public header files Ruby and Python export (which live in the libruby-dev / libpython-dev packages in Debian), there are struct definitions. How are those different? I found it useful to just list all the structs they export. Here’s the list!


Ruby 2.3.0:  `RArray`, `RBasic`, `RClass`, `RComplex`, `RData`, `RFile`, `RMatch`, `RObject`, `RRegexp`, `RString`, `RStruct`, `RTyped`.


Python 3.5: `PyAddrPair`, `PyASCIIObject`, `PyAsyncMethods`, `PyBaseExceptionObject`, `PyBufferProcs`, `PyByteArrayObject`, `PyBytesObject`, `PyCellObject`, `PyCFunctionObject`, `PyCodeObject`, `PyCompactUnicodeObject`, `PyCompilerFlags`, `PyComplexObject`, `PyCoroObject`, `PyCursesWindowObject`, `PyDateTime`, `PyDescrObject`, `PyDictObject`, `PyFloatObject`, `PyFrameObject`, `PyFunctionObject`, `PyFutureFeatures`, `PyGC`, `PyGenObject`, `PyGetSetDef`, `PyGetSetDescrObject`, `PyHash`, `PyHeapTypeObject`, `PyImportErrorObject`, `PyInstanceMethodObject`, `PyInterpreterState`, `PyListObject`, `PyLockStatus`, `PyMappingMethods`, `PyMemAllocatorDomain`, `PyMemAllocatorEx`, `PyMemberDef`, `PyMemberDescrObject`, `PyMemoryViewObject`, `PyMethodDescrObject`, `PyMethodObject`, `PyModuleDef`, `PyNumberMethods`, `PyObject`, `PyObjectArenaAllocator`, `PyOSErrorObject`, `PySequenceMethods`, `PySetObject`, `PySliceObject`, `PySTEntryObject`, `PyStopIterationObject`, `PyStructSequence`, `PySyntaxErrorObject`, `PySystemExitObject`, `PyThreadState`, `PyTracebackObject`, `PyTryBlock`, `PyTupleObject`, `PyType`, `PyTypeObject`, `PyUnicodeErrorObject`, `PyUnicodeObject`, `PyVarObject`, `PyWrapperDescrObject`


Python gives you a lot more structs than Ruby, and those structs in general I think have more fields. The structs I want access to are like `PyThreadState`, and they’re not in Ruby’s public header files.


### What interfaces does Ruby’s C API provide for getting stack traces?


An API for getting stack frames was added to Ruby in commit
[774bff0adb](https://github.com/ruby/ruby/commit/774bff0adb44eaf5c806afb1bf9eff65d26b2f1f) on
October 7, 2013 – the main function here seems to be `rb_profile_frames`. This is a **function**
though so to call it you need to be in the same Ruby process, not in a separate process.


I went to look at the [stackprof](https://github.com/tmm1/stackprof) profiler and its initial commit is from
[October 10, 2013](https://github.com/tmm1/stackprof/commit/58aa917f54a83185b1f3fe651a84fb44abb95ba6) – 3 days after the new profiler feature was released. Makes sense!


Here’s what stackprof’s initial release notes say:


samples are taken using a combination of two new C-APIs in ruby 2.1:

- signal handlers enqueue a sampling job using `rb_postponed_job_register_one`.
this ensures callstack samples can be taken safely, in case the VM is garbage collecting
or in some other inconsistent state during the interruption.
- stack frames are collected via `rb_profile_frames`, which provides low-overhead C-API access
to the VM’s call stack. no object allocations occur in this path, allowing stackprof to collect
callstacks for in allocation mode.


### that’s all for now


There are probably more important differences between Ruby’s header files and Python’s header files
that I don’t know about yet. That’s enough blogging for today though!
