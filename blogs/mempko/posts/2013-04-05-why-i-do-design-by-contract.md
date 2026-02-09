---
title: "Why I do Design by Contract"
date: 2013-04-05
url: https://blog.mempko.com/why-i-do-design-by-contract/
slug: why-i-do-design-by-contract
word_count: 866
tags: ['code dbc tdd', '#wordpress', '#Import 2024-11-03 23:36']
---



Behind all the hoopla of TDD, ATDD, BDD, I lumber on writing code using [Design by Contract](https://en.wikipedia.org/wiki/Design_by_contract?ref=blog.mempko.com). To those unfamiliar with it, I wanted to give my reasons for preferring it over TDD.


Imagine this is your software


That my friends is an egg.


It isn’t a stinky egg. Those lines are input to your software. I’ll get back to the egg in a second.


The idea behind Design by Contract is that before you implement your functions, you explicitly state your assumptions about the input, output and internal structure. A function has attributes it REQUIREs about it’s input so that the function can ENSURE specific properties about the output. This is different than defensive programming and it is different from TDD, because contracts stop the execution of your code! Let me give you trivial example C++11 example from [Firestr](http://github.com/mempko/firestr?ref=blog.mempko.com)


```


u::array convert(const users& us)
{
    u::array a;
    for(auto u : us)
    {
        CHECK(u);
        a.add(convert(*u));
    }
    ENSURE_EQUAL(a.size(), us.size());
    return a;
}


```


This is a function which converts a list of users into an encoded array which gets written on the network wire. At the end of the function I use a special macro called ENSURE_EQUAL, which checks to make sure the values are equal. If they are not, the values are printed and the program quits.


You can find the specific implementation of the macro [here](https://github.com/mempko/firestr/blob/master/src/util/dbc.hpp?ref=blog.mempko.com).


If you were using TDD, you might write a test instead that looks like this, before you write your code.


```


void test_ensure_convert_creates_same_size_encoded_array
{
    users us = mock.get_users();
    u::array ar = convert(us);
    ASSERT_EQUAL(ar.size(), us.size());
}


```


However, having the asserts in your code has several distinct advantages. First, having the requirements by the code makes them easier to find and see. Second, the checks run for all input your program ever receives instead of specific cases that you create in your test. Third, in the days of multi-threaded code, having your checks run as your code runs will reveal many threading bugs. What if another thread adds users as convert is being run? Having the checks always run will catch these kinds of bugs.


While TDD tests software modules in isolation, most bugs happen in how modules are connected.


By stating your requirements as executable code, your code will find the bugs for you. The contracts guarantee that all units connected are satisfying their obligations.


Let’s get back to our egg.


As input enters your program, you must sanitize it and check it to make sure it is acceptable. For this you can use the standard techniques like error codes and exception handling. Once the input gets past the hard shell, it enters the gooey inside where your algorithms and business logic lies. At this point you can use HARD CORE contracts which constantly check your assumptions and requirements. You can write your logic as though the input is properly sanitized, no need for defensive programming.


This creates a clean separation between where input is assumed to be dirty, and when input is assumed to be valid for your logic.


As a contract fails, it will print a stack trace and abort the program. This guarantees two things.


1. Your code will NOT run for long if you have bugs or wrong assumptions. This motivates people to fix bugs.

2. Your code WILL fail close to the problem instead of somewhere down the line.


This simplifies testing and debugging dramatically. In a debug build, you can even have the compiler automatically run a debugger at the point of failure. It also allows you to implement an incredibly powerful testing technique pioneered by Haskell’s QuickCheck.


Because your pre and post conditions are stated explicitly by your code, you can write tests which create random values within the domain of your input and test your code for correct behaviour and output. And because the checks always run, you can test high level modules in this way to make sure the *connections*, the call graph, the stuff in *between* is correct instead of just individual units. This is more powerful than unit testing and more powerful than simple integration testing, or “higher level” testing.


For my projects at work, we achieve 90% code coverage with these techniques. We run hundreds of thousands of tests instead of the thousands you would have with TDD.


It reminds me of the famous parable about the blind old men touching an elephant for the first time to figure out what it is. The first touches the trunk and says “An elephant is like a tree”. The second touches the ears and says “The elephant is like curtain!”, the third touches the tail and says “The elephant is like a paint brush”.


What is less known is the parable about the blind elephants touching the man. They never knew what a man was so the blind elephants decided to find one and touch him. They found a man and touched him with their legs. They all happily agreed “A man is a pancake, flat and round!”


TDD is like touching your code blind, DBC is like crushing your code flat. As they say “Work smarter, not harder”. Write tests that write tests for you. Crush your code.

