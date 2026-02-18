---
title: "Random Code Editor Idea"
date: 2015-07-29
url: https://zedshaw.com/blog/2015-07-29-random-code-editor-idea/
slug: random-code-editor-idea
word_count: 681
---



# Random Code Editor Idea


When I teach people to code I give them this simple procedure to follow:


1. Write the skeleton of the function.
2. Write comments in English describing what that function should do.
3. Under each comment fill in the code necessary to make it work.


This procedure works for early programmers because they typically know how to write code, and know what they want it to do, but the gap between what they want and what to write is fairly large. They don’t have enough experience to close the gap, but since they can describe what they want the function to do then that’s their start.


I find that starting with **desired results** works best for beginners and early coders. Everyone uses a computer these days and know how software should work. They can describe what they want their software to do much more easily than they can write code, so starting there gets them going. Eventually after coding for a while they switch to thinking entirely in code, but even to this day when I can’t quite think of the code to write, I start with the comments and fill them in.


If I throw in testing into the teaching (usually when they’re more capable), then the procedure becomes a little more complex:


1. Write the skeleton of the function.
2. Write the test and first call of the function making it fail.
3. Write the comments in the function for what it should do.
4. Fill in the comments with code and keep expanding and running the test.


Yet, the process is still the same and focuses on describing what I want and then filling in the blanks. In writing this is the same process I tell beginning writers. Just talk out loud and say what you want to say, writing those as little notes, then fill in the paragraphs. Or, create an outline then fill it in. Same for painting, where I tell people to make a rough outline of what they want to paint, then figure out each piece of the outline.


In general, the way you can solve a complex problem that’s difficult to visualize in any medium (code, words, paint, music, etc.) is to convert the problem to a paint-by-numbers problem. Instead of just trying to do it all at once right in your head and get it right, you break it down into tiny problems, then solve each one.


What if code editors helped with this process specifically? What I mean is, imagine your process becomes this:


1. Write the test or the function skeleton, doesn’t matter, and the editor makes the other one.
2. Go into the function, and start writing comments.
3. Editor guesses at what should go there and puts it under your comment, and it keeps running the test as you type.
4. You then edit the code as it pops in, or maybe alternate through what comes up, and it keeps running and working the test to bust your function.
5. Eventually the test passes and it knows to move on to the next comment.


It’s difficult to describe, but a way to think of it is a hyper embedded version of what programmers seem to do these days anyway, which is just search through Stack Overflow, documentation, APIs, and github using most of the words you’d put into a comment to find code. Why not have the editor use fancy machine learning algorithms and a vast catalog of existing curated code to do this for you?


In addition to that, it seems possible to auto-generate enough test code to fuzz through most of what you write, especially if the language is more modern. Maybe it’s something like [AFL](http://lcamtuf.coredump.cx/afl/) generating tests that hammer your function finding things, and since it’s generating the code in the function it’s possible it could be smarter at this.


Just a random idea, but could be an interesting thing to research. Call it “Comment Driven Coding” for lack of a better name.



---


###### More from Zed A. Shaw
