---
title: "Hacker School Day 1: Messing around with the stack in C"
date: 2013-09-30
url: https://jvns.ca/blog/2013/09/30/hacker-school-day-1-messing-around-with-the-stack-in-c/
slug: hacker-school-day-1-messing-around-with-the-stack-in-c
word_count: 210
---


Today was the first day of [Hacker School](http://hackerschool.com).
There were tons of amazing people and it was fun and a bit overwhelming.


I paired with [Daphne](https://github.com/lifeissweetgood) on a shell in
C which is called [_dash](https://github.com/lifeissweetgood/_dash)
right now. She is fantastic and taught me tons of things about C.


When trying to tokenize strings in our shell, we ran into a super
unintuitive bug.  Here’s the [gist](https://gist.github.com/jvns/6772832) of it:


```
#include <stdio.h>

void set_strings(char*** strings) {
  char* strs[] = {"banana"};
  *strings = strs;
}

int main() {
  char** strings;
  set_strings(&strings);
  printf("First print: '%s'\n", strings[0]);
  char* s = "abc";
  printf("Second print: '%s'\n", strings[0]);
}

```


So this looks like normal code that would print “banana” twice. But
here’s what actually happens:


```
bork@kiwi ~/w/h/gists> gcc write-to-stack.c&& ./a.out
First print: 'banana'
Second print: 'UH�WAVAUE1TE1H�H�'

```


As I understand it, this is because this line:


```
char* strs[] = {"banana"};

```


gets allocated on the *stack* and not on the *heap*. So the pointer in
`strings` points to the stack and when you do something like setting a
variable, it becomes something weird. It took us a while to figure out
what was going on. YAY!


It’s sort of exciting to get bugs that are (as far as I know) totally
impossible in Python.
