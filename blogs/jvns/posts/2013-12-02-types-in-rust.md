---
title: "Day 35: Types in Rust, for beginners"
date: 2013-12-02
url: https://jvns.ca/blog/2013/12/02/types-in-rust/
slug: types-in-rust
word_count: 781
---


I found understanding Rust types really confusing, so I wrote up a
small tutorial for myself in an attempt to understand some of them.
This is by no means exhaustive. There is a
[types section](http://static.rust-lang.org/doc/master/rust.html#type-system)
in the manual, but it has nowhere near enough examples.


This assumes that you’ve read the sections about
[owned](http://static.rust-lang.org/doc/master/tutorial.html#ownership)
and
[borrowed](http://static.rust-lang.org/doc/master/tutorial.html#borrowed-pointers)
pointers in the Rust tutorial, but not much else.


I’m not talking about managed pointers (`@`) at all. A lot of the
difficulty with Rust types is that the language is constantly
changing, so this will likely be out of date soon.


First, a few preliminaries: it’s easier to play with types if you have
a REPL and can interactively check the types of objects. This isn’t
really possible in Rust, but there are workarounds.


## To start out: some help


### How to get a Rust REPL


There is no working Rust REPL. However, you can use
[this script](http://sprunge.us/ahKj) to approximate one – it
compiles what you put into it and prints the result. You can’t use the
results of what you did previously, though. Save as `rustci`.


### How to find the type of a variable


**Edit:** The fantastic [Daniel Micay](https://github.com/thestinger)
showed me this function to find the type of a variable. It’s included
in the `rustci` script above, so you can just do


`let x = 2; type_of(&x)`


to print the type of `2`. Amazing. Note that you have to call
`type_of` with `&x` and not `x`.


The function is:


```
fn type_of<T>(_: &T) -> &'static str {
    unsafe {
        (*std::unstable::intrinsics::get_tydesc::<T>()).name
    }
}

```


**Hackier approach:**


You can also generate a compiler error with the type of a variable `y`
like this:


```
fn y() {}
let x: () = y;

```


It’s a hack, but it will give you an error like this:


```
error: mismatched types: expected `()` but found `fn()` (expected () but found extern fn)

```


which tells us that the type of `f` is `fn()`.


## The types!


### Primitive types


This is an incomplete list.


Integers (signed and unsigned): `int`, `uint`, `i8`, `i16`, `i32`, `i64`, `u8`, `u16`, `u32`, `u64`


Floats: `f32`, `f64`


Booleans: `bool`


**Primitive type examples**


```
let x: uint = 2;
let y: u8 = 40;
let z: f32 = abc;

```


### Vectors


There are 3 possible types for a vector of `u8`: `[u8, ..N]`, `&[u8]`, `~[u8]`


`[u8]` by itself is not a type.


`[u8, ..5]` is a fixed-size vector of `u8` of length 5.


**Vector Examples**


```
// Fixed size vector
let x : [uint, ..10] = [5, ..10]; // [5,5,5,5,5,5,5,5,5,5]

// Create a variable size owned vector
let mut numbers1 : ~[uint]= ~[0, 1, 2, 3, 4, 5];

// Create a variable size borrowed vector. This is also called a "vector slice".
let mut numbers2 : &[uint]= &[0, 1, 2];
let mut slice: &[uint] = numbers1.slice(0, 3);

```


### Strings and characters


Some string types include: `&str`, `~str`, and `&'static str`.


A string is represented internally as a vector of bytes. However,
`str` by itself is *not* a type, and there are no fixed-size strings.
You can convert any of the string types to a byte vector `&[u8]`.


`char` is a 32-bit Unicode character.


**String Examples**


```
use std::option::Option;
// Static string
let hello: &'static str = "Hello!";
let hello2: &str = "Hello!";

// Owned string
let owned_hello: ~str = ~"Hello!";

// Borrowed string
let borrowed_hello = &owned_hello;

// Character
let c: char = 'a';

// Indexing into a string gives you a byte, not a character.
let byte: u8 = owned_hello[1];

// You need to create an iterator to get a character from a string.
let c: Option<char> = owned_hello.chars().nth(2);

// Switch to the string's representation as bytes
let bytes: &[u8] = owned_hello.as_bytes();

```


### Functions


For a function `fn(a: A) -> B`


`fn(A)->B` is a type, So are `&(fn(A)->B)`, `~(fn(A)->B)`, but you need to add parens right now.


You probably only want to use `fn(A)->B`, though.


**Function type examples**


```
fn foo(a: int) -> f32 {
    return 0.0;
}
let bar: fn(int) -> f32 = foo; 
let baz: &(fn(int) -> f32) = &foo;

```


### Closures


The type of a closure mapping something of type `A` to type `B` is `|A| -> B`. A closure with no arguments or return values has type `||`.


**Closure type examples**


```
let captured_var = 10; 
let closure_no_args = || println!("captured_var={}", captured_var); 
let closure_args = |arg: int| -> int {
  println!("captured_var={}, arg={}", captured_var, arg); 
  arg
};

// closure_no_args has type ||
// closure_args has type |int| -> int

fn call_closure(c1: ||, c2: |int| -> int) {
  c1();
  c2(2);
}

call_closure(closure_no_args, closure_args);

```


### Raw pointers


For any type `T`, `*T` is a type.
