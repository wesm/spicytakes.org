---
title: "Using C++ STL Algorithms without Lambdas is an Advantage"
date: 2009-11-30
url: https://blog.mempko.com/using-c-stl-algorithms-without-lambdas-is-an-advantage/
slug: using-c-stl-algorithms-without-lambdas-is-an-advantage
word_count: 251
tags: ['#wordpress', '#Import 2024-11-03 23:36']
---



A common complaint about C++ is that there are no lambdas (this will  be fixed in C++0x), and most claim this makes STL algorithms like  for_each, transform, accumulate almost useless because you have to  create functions or functors somewhere else.


Not having lambdas is a **GOOD **thing. Although it can be annoying to create  all these little functions/functors, there is an important advantage in  doing so.


It forces you to think more modularly and you end up  divide-and-conquering a problem.


It helps you think about your program on a higher level and also  helps promote usability. Lambdas by definition are not reusable.


Here is an example


> BoundingBox parseBounds(const string& bounds)
> {
>     //code that does parsing
>     .....
>     return result;
> } 
> vector<BoundingBox> createBounds(const vector<string>& bounds)
> { 
>     vector<BoundingBox> result;
>     transform(bounds.begin(), bounds.end(),
>         back_inserter(result), parseBounds);
>     return result;
> }


If you use the STL algorithms you will be forced to write  parseBounds. It is obvious that a function which converts a string to a  BoundingBox will be useful in the future. If you wrote the loop yourself  or had lambdas, you might have been tempted to write the conversion directly  in createBounds.


When I write C++ I rarely write my own loops and I think it is a good  discipline to pick up because it will force you to break your code up.  It becomes almost impossible to write monolithic functions and also  encourages code reuse. Best of all, your algorithms start looking simpler.

