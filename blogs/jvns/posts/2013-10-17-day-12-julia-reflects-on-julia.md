---
title: "Day 12: Why Julia likes Julia"
date: 2013-10-17
url: https://jvns.ca/blog/2013/10/17/day-12-julia-reflects-on-julia/
slug: day-12-julia-reflects-on-julia
word_count: 547
---


Firstly, I will never get tired of the fact that Julia is called Julia.
It is the best. It however makes it *really* hard to search for email
with “Julia” in them in my inbox.


But! We have Serious Coding Business to discuss.


According to [http://julialang.org](http://julialang.org), Julia is a
“high-level, high-performance dynamic programming language for
technical computing”. If you want actual explanations  of what Julia is
and how it works, there is pretty good documentation there.


I’ve been programming in Julia for about a week now. So now is a good
time to share my Extreme Julia Expertise. Hopefully someone will correct
me if I’ve said anything terribly wrong here.


### Things I like about Julia


#### 1) It’s like Python


The syntax is like Python’s syntax. It’s dynamic. It’s fun to write.


#### 2) It lets me use the IPython notebook (via [IJulia](http://github.com/JuliaLang/IJulia.jl))


This is *huge* for me. Over the last year, the IPython notebook has
become one of my main programming environments. I find the ability to
quickly change and run code without having to switch contexts really
useful.


#### 3) The community seems lovely.


So I’m partly biased here because Stefan, one of the creators of Julia,
has been at Hacker School all week and he is a lovely guy. But I’ve been
spending some one in the Julia issue queue as well and all those people
are lovely as well.


#### 4) It’s like C


This is kind of the opposite of “it’s like Python”. In Julia when you
make a type declaration


```
type Range
    start::Int64
    end::Int64
end

```


{:lang=‘julia’}


it really only takes up 2 Int64s worth of space! It also means that I
can write code that is C-like – I’ve been working from a gzip tutorial
which has lots of C code examples, and they’re pretty straightforward
to port into Julia.


#### 5) You can look at the LLVM code for your functions!


So far this is more ‘cool’ than ‘useful’ for me, but it is so cool!


So you can see this is just 2 LLVM instructions!


```
julia> function blah(x)
           x+2
       end
blah (generic function with 1 method)
julia> code_llvm(blah, (Int64,))

define i64 @julia_blah(i64) {
top:
  %1 = add i64 %0, 2, !dbg !3829
  ret i64 %1, !dbg !3829
}

```


#### 6) A lot of Julia is written in Julia


So if you want to add to the standard library or improve Julia’s type
inference, you can do it in Julia! I think this is a pretty huge selling
point, because having to switch to a different language to make your fast is
no fun.


Multiple dispatch is also pretty neat. I may write more about it later,
because I’m not able to articulate yet why it gives me nice programming
patterns.


### Things I don’t like about Julia


The REPL starts pretty slowly – it takes about 2 seconds. I think that
right now all my frustrations with Julia are actually around the REPL
– there are a few things that possible to do in programs but impossible
in the REPL.


I also often redefine functions many many times while iterating on some
code, and sometimes that makes Julia get confused and I need to restart my
session.


That is a pretty small thing, though!
