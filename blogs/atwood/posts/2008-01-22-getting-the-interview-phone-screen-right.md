---
title: "Getting the Interview Phone Screen Right"
date: 2008-01-22
url: https://blog.codinghorror.com/getting-the-interview-phone-screen-right/
slug: getting-the-interview-phone-screen-right
word_count: 1518
---

The job market for software developers is hot. This is great news for programmers, but it makes the interview process challenging for potential employers. A reader recently wrote me expressing some concern about the interview process:


> You mention Vertigo requiring **a code sample, then a phone screening, then a hands-on test in the face-to-face**. We have a very similar process, but somehow a large percentage of the candidates who make it to the hands-on test are very poor and should have been eliminated at step 1 or 2. The signal to noise ratio is terrible. It costs a great deal to spend so much time doing face-to-face interviews with people who often should not be developers in the first place. I am curious how much light you might be able to shed on the specifics of your requirements on candidates. What part of the process is the most effective in separating the cream, how and why?


It is **very expensive to get the phone screen wrong –** a giant waste of time for everyone involved.


![](https://blog.codinghorror.com/content/images/2025/03/image-442.png)


The best phone screen article you’ll ever find is Steve Yegge’s [Five Essential Phone-Screen Questions](http://steve.yegge.googlepages.com/five-essential-phone-screen-questions), another gift to us from Steve’s stint at Amazon.


Steve starts by noting two critical mistakes that phone screeners should do their best to avoid:

1. **Don’t let the candidate drive the interview.** The interviewer should do most of the talking, guiding the conversation along until they’re satisfied the candidate knows the answers to the questions (or has given up).
2. **Watch out for one-trick ponies.** Candidates who only know one particular language or programming environment, and protest complete ignorance of everything else, are a giant red warning flag.


The point of the phone screen is not for the candidate to drone on about what they’ve done. The interviewer should push them out of their comfort zone a bit and ask them *related* questions about things they haven’t seen or done before. Ideally, you want to know how this person will react when they face something new, such as *your* codebase.

kg-card-begin: html

> In an effort to make life simpler for phone screeners, I’ve put together this list of Five Essential Questions that you need to ask during an SDE screen. They won’t guarantee that your candidate will be great, but they will help eliminate a huge number of candidates who are slipping through our process today.
> **Coding.** The candidate has to write some simple code, with correct syntax, in C, C++, or Java.
> **OO design.** The candidate has to define basic OO concepts, and come up with classes to model a simple problem.
> **Scripting and regexes.** The candidate has to describe how to find the phone numbers in 50,000 HTML pages.
> **Data structures.** The candidate has to demonstrate basic knowledge of the most common data structures.
> **Bits and bytes.** The candidate has to answer simple questions about bits, bytes, and binary numbers.
> Please understand: **what I’m looking for here is a total vacuum in one of these areas.** It’s OK if they struggle a little and then figure it out. It’s OK if they need some minor hints or prompting. I don’t mind if they’re rusty or slow. What you’re looking for is candidates who are utterly clueless, or horribly confused, about the area in question.

kg-card-end: html

Of course, you’ll want to modify this process to reflect the realities at your shop – so I encourage you to read the entire article. But Steve does provide some examples to get you started:


**Coding**


> Write a function to reverse a string.
> Write function to compute Nth Fibonacci number.
> Print out the grade-school multiplication table up to 12x12.
> Write a function that sums up integers from a text file, one int per line.
> Write function to print the odd numbers from 1 to 99.
> Find the largest int value in an int array.
> Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.


Good candidates for the coding problem are verifiably simple, with basic loops or recursion and perhaps a little formatted output or file I/O. All we want to know is whether they really do know how to program or not. Steve’s article predates it, but I’d be remiss if I didn’t mention [Why Can't Programmers... Program?](https://blog.codinghorror.com/why-cant-programmers-program/) here. The FizzBuzz problem is quite similar, and it's shocking how often interviewees can’t do it. It’s a bit hard to comprehend, like a potential truck driver somehow not being able to find the gas pedal or shift gears.


**Object-Oriented Programming**


> Design a deck of cards that can be used for different card game applications.
> Model the Animal kingdom as a class system, for use in a Virtual Zoo program.
> Create a class design to represent a filesystem.
> Design an OO representation to model HTML.


We’re not saying anything about the pros and cons of OO design here, nor are we asking for a comprehensive, low-level OO design. These questions are here to determine whether candidates are familiar with the basic principles of OO, and more importantly, whether the candidate can produce a reasonable-sounding OO solution. We’re looking for understanding of the basic principles, as described in [the Monopoly Interview](https://blog.codinghorror.com/the-monopoly-interview/).


**Scripting and Regular Expressions**


> Last year my team had to remove all the phone numbers from 50,000 Amazon web page templates, since many of the numbers were no longer in service, and we also wanted to route all customer contacts through a single page.
> Let’s say you’re on my team, and we have to identify the pages having probable U.S. phone numbers in them. To simplify the problem slightly, assume we have 50,000 HTML files in a Unix directory tree, under a directory called /website. We have 2 days to get a list of file paths to the editorial staff. You need to give me a list of the .html files in this directory tree that appear to contain phone numbers in the following two formats: (xxx) xxx-xxxx and xxx-xxx-xxxx.
> How would you solve this problem? Keep in mind our team is on a short (2-day) timeline.


This is an interesting one. Steve says 25% to 35% of all software development engineer candidates cannot solve this problem at all – even with lots of hints and given the entire interview hour. What we’re looking for is a general reluctance to reinvent the wheel, and some familiarity with scripting languages and regular expressions. To me, this question indicates whether a developer will spend days doing programming work that he or she could have neatly avoided with, perhaps, a quick web search and some existing code that’s already out there.


**Data Structures**


> What are some really common data structures, e.g. in `java.util`?
> When would you use a linked list vs. a vector?
> Can you implement a Map with a tree? What about with a list?
> How do you print out the nodes of a tree in level-order (i.e. first level, then 2nd level, then 3rd level, etc.)
> What’s the worst-case insertion performance of a hashtable? Of a binary tree?
> What are some options for implementing a priority queue?


A candidate should be able to demonstrate a basic understanding of the most common data structures. More specifically, the big ones like arrays, vectors, linked lists, hashtables, trees, and graphs. They should also know the fundamentals of “big-O” algorithmic complexity: constant, logarithmic, linear, polynomial, exponential, and factorial. If they can’t, that’s a huge warning flag.


**Bits and Bytes**


> Tell me how to test whether the high-order bit is set in a byte.
> Write a function to count all the bits in an int value; e.g. the function with the signature `int countBits(int x)`
> Describe a function that takes an int value, and returns true if the bit pattern of that int value is the same if you reverse it (i.e. it’s a palindrome); i.e. `boolean isPalindrome(int x)`


As Steve says, “*Computers don’t have ten fingers, they have one. So people need to know this stuff.”* You shouldn’t be treated to an uncomfortable silence after asking a candidate what 2^16 is; it’s a special number. They should know it. Similarly, they should know the fundamentals of AND, OR, NOT and XOR – and how a bitwise AND differs from a logical AND. You might even ask about signed vs. unsigned, and why bit-shifting operations might be important. They should be able to explain why the old programmer’s joke, “why do programmers think Oct 31 and Dec 25 are the same day?” is funny.


Performing a thorough, detailed phone screen is a lot of work. But it’s worth it. Every candidate eliminated through the phone screen saves at least 8 man-hours of time that would have been wasted by everyone in a hands-on test. Each time an unqualified candidate makes it to the hands-on test, you should be asking yourself – **how could we have eliminated this candidate in the phone screen?**

[interview process](https://blog.codinghorror.com/tag/interview-process/)
[phone screening](https://blog.codinghorror.com/tag/phone-screening/)
[candidate selection](https://blog.codinghorror.com/tag/candidate-selection/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technical assessment](https://blog.codinghorror.com/tag/technical-assessment/)
