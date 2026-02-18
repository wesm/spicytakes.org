---
title: "Day 48: Another Go program, and a little vim configuration"
date: 2021-01-28
url: https://jvns.ca/blog/2021/01/28/day-48--another-go-program/
slug: day-48--another-go-program
word_count: 207
---


On Wednesday I was feeling tired so I didn’t do too much. I just translated my
bash script to set up device mapper from the day before to a Go program.


Today I think I’ll integrate that Go code into my main program!


### the go program: set up device mapper


I wrote a little [go code](https://gist.github.com/jvns/28ccdda7525bf64d8c88f3d252cd727f) which does
basically the same thing as the bash script from yesterday (sets up some
`/dev/mapper`s).


### some fun with vim


I never set up my vim, but when writing Go this week I decided to give the
`vim-go` plugin another shot. So far I’m using 3 features from it:

- it runs `go fmt` to I save
- I can run `<leader>gb` to build my Go program
- If I do `Ctrl+Enter`, it goes to the definition of the function


The format and builder things are fine (it doesn’t seem that much better to me
than just switching to a terminal to do the same thing), but the go to
definition thing is GREAT. I was trying to read some code from Ignite and it
made it a lot faster and easier.


Usually I do “go to definition” with a lot of grep so this was a lot faster.
