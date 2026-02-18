---
title: "Calling C from Rust"
date: 2016-01-18
url: https://jvns.ca/blog/2016/01/18/calling-c-from-rust/
slug: calling-c-from-rust
word_count: 300
---


Yesterday I asked [Kamal](https://twitter.com/kamalmarhubi) how to call C code from Rust, for a project I’m thinking about. It turned out to be a little harder than I expected! Largely because I don’t know Rust well, and fixing compiler errors is nontrivial. 30 minutes and some number of inscrutable-to-me compiler errors later, we figured it out.


I want to do something pretty simple – copy the string “Hello, world!” and print it.


Here’s the Rust code that calls C. It doesn’t use any special libraries – just Rust.


```
extern {
    // Our C function definitions!
    pub fn strcpy(dest: *mut u8, src: *const u8) -> *mut u8;
    pub fn puts(s: *const u8) -> i32;
}

fn main() {
    let x = b"Hello, world!\0"; // our string to copy
    let mut y = [0u8; 32]; // declare some space on the stack to copy the string into
    unsafe {
      // calling C code is definitely unsafe. it could be doing ANYTHING
      strcpy(y.as_mut_ptr(), x.as_ptr()); // we need to call .as_ptr() to get a pointer for C to use
      puts(y.as_ptr());
    }
}

```


I’m mostly writing this down so that I don’t forget, but maybe it will be useful for you too!


Along the way I found out that `cargo` (Rust’s build tool) is super easy to get started with – all you need to do is run


```
$ cargo new --bin my-project
$ cd my-project
$ cargo run
   Compiling my-project v0.1.0 (file:///home/bork/work/my-project)
     Running `target/debug/my-project`
Hello, world!

```


and you have a new Rust project that you can run with `cargo run`!


Rust is way easier to install than it was in 2013, though I still find the error messages hard to understand.


There might be more of these short project-notes posts to come – hopefully some of you will find them interesting!
