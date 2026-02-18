---
title: "Bindgen: awesome Rust tool for generating C bindings"
date: 2017-12-21
url: https://jvns.ca/blog/2017/12/21/bindgen-is-awesome/
slug: bindgen-is-awesome
word_count: 844
---


Yesterday I made a category for these ruby profiler posts on my blog because I think there
will be a lot of them. It’s at [https://jvns.ca/categories/ruby-profiler](https://jvns.ca/categories/ruby-profiler).


Hello! Today I am excited about bindgen, an awesome Rust tool for generating bindings from C header files. It has a
[great user’s guide](https://rust-lang-nursery.github.io/rust-bindgen/).


This post is about what bindgen is, why I think it’s cool, and experiments I have been doing with bindgen for my Ruby profiler.


### bindgen: #include for Rust


To me the dream of Rust is “it gives you all the power of C, but with a more powerful compiler, better documentation, better tools (`cargo`), and a great community”. I think bindgen is a really important part of “great tools”!


Suppose you want to include a C library in your program. In C, this is easy: just include the header file.


```
#include <library_header_file.h>

…. call functions from library here ...

```


So if Rust has “all the power of C” (and interoperates so well with C), you should be able to just `#include` a header file from a C library and have it just work, right?


Almost! You can run `bindgen cool_header_file.h -o rust-bindings.rs` and it’ll automatically generate Rust struct definitions or function declarations that will let you link in the C library. So simple!


Here’s [the bindgen output for Python.h](https://gist.githubusercontent.com/jvns/38c9f29ba4a6f08e05004aac4e8c5c10/raw/4371d7d081b163c5f8930c334ec348eac1642e2e/python-bindings.rs) as an example. It’s 24,000 lines. Here are a couple of representative bits: the PyCodeObject struct & the declaration of the eval function.


```
// A struct!
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct PyCodeObject {
    pub ob_refcnt: Py_ssize_t,
    pub ob_type: *mut _typeobject,
    pub co_argcount: ::std::os::raw::c_int,
    pub co_nlocals: ::std::os::raw::c_int,
    pub co_stacksize: ::std::os::raw::c_int,
    pub co_flags: ::std::os::raw::c_int,
    pub co_code: *mut PyObject,
    … and more ...
}
// A function declaration!
extern "C" {
 # [ link_name = "\u{1}_Z15PyEval_EvalCode" ]
    pub fn PyEval_EvalCode(
        arg1: *mut PyCodeObject,
        arg2: *mut PyObject,
        arg3: *mut PyObject,
    ) -> *mut PyObject;
}

```


Then you can include this file in your Rust project as a module, link with libpython, and start
using libpython in your Rust program! Cool!


### cool bindgen features


Bindgen can do some really cool things:

- Whitelist types that you want to generate bindings for if you don’t want the whole header file
- Generate #[derive(Debug)] annotations for C structs so you can easily print them out with `println!(“{:?}”, my-struct)`. This is SO USEFUL when debugging!!!!
- It seems to handle `#ifdefs` and stuff okay – I threw a pretty complicated set of header files at it and it seems ok so far.
- Pick which Rust compiler version you want to target


### what I’m doing with bindgen


I wanted to do something weird: `#include` vm_core.h, which is an internal header file in Ruby. And I didn’t actually want to just include one `vm_core_h`, I wanted to generate bindings for 33 different Ruby versions (since vm_core.h is an internal header file, the structs I care about are [constantly changing](https://jvns.ca/blog/2017/12/19/how-much-does-the-ruby-abi-change-/)).


This appears to be something that `bindgen` can help with me with! Here are the generated bindings for 33 Ruby versions (2.1.1 to 2.5.0rc1): [https://github.com/jvns/ruby-stacktrace/tree/77708ffb0db6682df546170bf09753a195afa7d5/src/bindings](https://github.com/jvns/ruby-stacktrace/tree/77708ffb0db6682df546170bf09753a195afa7d5/src/bindings). Bindgen generated about 6MB of code. (the rest of the code on that branch is kind of a mess since I’m hacking around trying to see if this approach is workable).


Once I have all those bindings in my repository, I can `use bindings::ruby_2_2_0::*;` to get the right types for Ruby 2.2.0. Really simple!


Here’s the bindgen incantation I ran to get the bindings for Ruby 2.3.0. (I just put this in a script and ran a for loop to generate all 33 versions).


```
bindgen /tmp/headers/2_3_0/vm_core.h\
    -o bindings.rs \
    --impl-debug true \
    --no-doc-comments \
    --whitelist-type rb_iseq_constant_body \
    --whitelist-type rb_iseq_location_struct \
    --whitelist-type rb_thread_struct \
    --whitelist-type rb_iseq_struct \
    --whitelist-type rb_control_frame_struct \
    --whitelist-type rb_thread_struct \
    --whitelist-type RString \
    --whitelist-type VALUE \
    -- \
    -I/tmp/headers/2_3_0/include \
    -I/tmp/headers/2_3_0/ \
    -I/usr/lib/llvm-3.8/lib/clang/3.8.0/include/ # my bindgen doesn’t find the clang headers properly for some reason

```


### generating bindings at build time


You might have noticed that I committed the bindings I generated into my repository. This is not
actually the recommended way to use bindgen – they recommend in general that you generate your
bindings during your build.


How to do that is [documented really nicely in the bindgen user’s guide](https://rust-lang-nursery.github.io/rust-bindgen/library-usage.html).


Basically you create a `build.rs` file that runs during your build and uses the bindgen library to generate bindings. I think I like the approach of having a `build.rs` + Cargo.toml instead of a Makefile a lot – it seems easier to maintain. And you can declare separate build dependencies in Cargo.toml!


### cbindgen: reverse bindgen


Someone on Twitter pointed me to [cbindgen](https://github.com/eqrion/cbindgen), a tool to go the
other way and generate C bindings for your Rust code. Neat!


### gonna continue experimenting


I’m still not sure if this approach of “let’s generate bindings for 33 different ruby versions and commit them into my repository” will work. But I figure the best way to find out it to keep trying it and see how it goes! If it doesn’t work then I’ll go back to using DWARF.
