---
title: "LD_PRELOAD is super fun. And easy!"
date: 2014-11-27
url: https://jvns.ca/blog/2014/11/27/ld-preload-is-super-fun-and-easy/
slug: ld-preload-is-super-fun-and-easy
word_count: 431
---


On Monday I went to Hacker School, and as always it was the most fun
time. I hung out with [Chase](http://blog.chaselambda.com/) and we had
fun with dynamic linkers!


I’d been hearing for a while that you can override arbitrary function
calls in a program using an environment variable called `LD_PRELOAD`.
But I didn’t realize how easy it was! Chase and I started using it and
we got it working in, like, 5 minutes!


I googled “LD_PRELOAD hacks”, clicked on [Dynamic linker tricks: Using LD_PRELOAD to cheat, inject features and investigate programs](http://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/),
and we were up and running.


The first example on that page has you write a new random function that
always returns 42.


```
int rand(){
    return 42; //the most random number in the universe
}

```


That is LITERALLY ALL THE CODE YOU HAVE TO WRITE. Then you


```
gcc -shared -fPIC unrandom.c -o unrandom.so
export LD_PRELOAD=unrandom.so

```


and now every program you run will always return 42 for rand()!


We did a bunch of investigations into how tmux works, which was super
fun. [Chase wrote it up on his blog](http://blog.chaselambda.com/2014/11/25/how-tmux-starts-up-an-adventure-with-linux-tools.html),
and now I understand about daemonization way better.


We very quickly ran into the question of “okay, what if you want to call
the original `printf`?” from your hacked printf? That’s also explained
in the “Dynamic linker tricks” article! (in the “Being transparent”
section, using `dlsym`)


Somebody explained to me at some point that if you work for the NSA and
you’re trying to spy on what information a program is using internally,
tools like LD_PRELOAD are VERY USEFUL.


### How it works


There is a very wonderful
[20 part series about linkers](http://lwn.net/Articles/276782/) that I
am going to keep recommending to everyone forever.


When you start a dynamically linked program, it doesn’t have all the
code for the functions it needs! So what happens is:

- the program gets loaded into memory
- the dynamic linker figures out which other libraries that program
needs to run (`.so` files)
- it loads them into memory, too!
- it connects everything up


`LD_PRELOAD` is an environment variable that says “Whenever you look for
a function name, look in me first!”. So if you didn’t want your program
to be attacked like this, you could:

- statically link your program
- check for the `LD_PRELOAD` environment variable, and complain (though
the attacker could also LD_PRELOAD the function that lets you read
environment variables… :) )


I’m sure there will be more Exciting Stories about LD_PRELOAD for you
all in the future, but this is all the stories I have for today.
