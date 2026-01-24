---
title: "A Scripter at Heart"
date: 2009-01-25
url: https://blog.codinghorror.com/a-scripter-at-heart/
slug: a-scripter-at-heart
word_count: 1024
---

What’s the difference between **a programming language and a scripting language**? Is there even a difference at all? Larry Wall’s epic [Programming is Hard, Let’s Go Scripting](https://www.perl.com/pub/2007/12/06/soto-11.html/) attempts to survey the scripting landscape and identify commonalities.


> When you go out to so-called primitive tribes and analyze their languages, you find that structurally they’re just about as complex as any other human language. Basically, you can say pretty much anything in any human language, if you work at it long enough. Human languages are Turing complete, as it were.
> Human languages therefore differ not so much in what you can say but in what you must say. In English, you are forced to differentiate singular from plural. In Japanese, you don’t have to distinguish singular from plural, but you do have to pick a specific level of politeness, taking into account not only your degree of respect for the person you’re talking to, but also your degree of respect for the person or thing you’re talking about.
> So languages differ in what you’re forced to say. Obviously, if your language forces you to say something, you can’t be concise in that particular dimension using your language. Which brings us back to scripting.
> How many ways are there for different scripting languages to be concise?
> How many recipes for borscht are there in Russia?


Larry highlights the following axes of language design in his survey:

- Binding: Early or Late?
- Dispatch: Single or Multiple?
- Evaluation: Eager or Lazy?
- Typology: Eager or Lazy?
- Structures: Limited or Rich?
- Symbolic or Wordy?
- Compile Time or Run Time?
- Declarational or Operational?
- Classes: Immutable or Mutable?
- Class-based or Prototype-based?
- Passive data, global consistency or Active data, local consistency?
- Encapsulatation: by class? by time? by OS constructs? by GUI elements?
- Scoping: Syntactic, Semantic, or Pragmatic?


It’s difficult to talk about Larry Wall without pointing out that [Perl 6](http://en.wikipedia.org/wiki/Perl_6) has been missing in action for a very long time. In this 2002 [Slashdot interview with Larry](http://interviews.slashdot.org/article.pl?sid=02/09/06/1343222&mode=thread&tid=145), he talks about Perl 6 casually, like it’s just around the corner. Sadly, it has yet to be released. That’s not quite [Duke Nukem Forever](http://en.wikipedia.org/wiki/Duke_Nukem_Forever) vaporware territory, but it’s darn close.


While interesting, I have to admit that I have a problem with all this pontificating about the nature of scripting languages, and the endlessly delayed release of Perl 6. **Aren’t Mr. Wall’s actions, on some level, contrary to the spirit of the very thing he’s discussing?** The essence of a scripting language is *immediate gratification*. They’re [Show, Don’t Tell](https://blog.codinghorror.com/show-dont-tell/) in action.


In fact, my first programming experiences didn’t begin with a compile and link cycle. They began [something like this](https://blog.codinghorror.com/everything-i-needed-to-know-about-programming-i-learned-from-basic/):


![](https://blog.codinghorror.com/content/images/2025/04/image-288.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-287.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-286.png)


As soon as you booted the computer, the first thing you were greeted with is that pesky blinking cursor.


It’s right there, inviting you.


*C’mon. Type something. See what happens*.


That’s the ineffable, undeniable beauty of a scripting language. You don’t need to read a giant Larry Wall article, or wait 8 years for Perl 6 to figure that out. It’s right there in front of you. Literally. Try entering this in your browser’s address bar:

kg-card-begin: html

```
javascript:alert(‘hello world’);
```

kg-card-end: html

But it’s not *real* programming, right?


My first experience with *real* programming was in high school. Armed with a purchased copy of the [the classic K&R book](https://www.amazon.com/dp/0131103628) and a pirated C compiler for my [Amiga 1000](https://en.wikipedia.org/wiki/Amiga_1000), I knew it was finally time to **put my childish AmigaBASIC programs aside**.


![](https://blog.codinghorror.com/content/images/2025/04/image-285.png)


I remember that evening only vaguely (in my defense: I am old). My mom was throwing some kind of party downstairs, and one of the guests tried to draw me out of my room and be social. She was a very nice lady, with the best of intentions. I brandished my K&R book as a shield, holding it up and explaining to her: “No. You don’t understand. This is important. I need to learn what’s in this book.” Tonight, *I become a real programmer*. And so I began.


What happened next was **the eight unhappiest hours of my computing life**. Between the painfully slow compile cycles and the torturous, unforgiving dance of pointers and memory allocation, I was almost ready to give up programming altogether. C wasn’t for me, certainly. But I couldn’t shake the nagging feeling that there was something altogether *wrong* with this type of programming. How could C suck all the carefree joy out of my stupid little AmigaBASIC adventures? This language took what I had known as programming and contorted it beyond recognition, into something stark and [cruel](https://blog.codinghorror.com/is-worse-really-better/).


I didn’t know it then, but I sure do now. **I hadn’t been programming at all. I had been scripting.**


I don’t think my revulsion for C is something I need to apologize for. In fact, I think it’s the other way around. I’ve just been waiting for the rest of the world to catch up to [what I always knew](https://web.archive.org/web/20050209234429/http://www.oreillynet.com/pub/wlg/3190).


> The reason why dynamic languages like Perl, Python, and PHP are so important is key to understanding the paradigm shift. Unlike applications from the previous paradigm, web applications are not released in one to three year cycles. They are updated every day, sometimes every hour. Rather than being finished paintings, they are sketches, continually being redrawn in response to new data.
> In my talk, I compared web applications to Von Kempelen’s famous hoax, the mechanical Turk, a 1770 mechanical chess playing machine with a man hidden inside. **Web applications aren’t a hoax**, but like the mechanical Turk, they do have a programmer inside. And that programmer is sketching away madly.


Now, I do appreciate and admire the seminal influence of C. In the right hands, it’s an incredibly powerful tool. Every language has its place, and every programmer should choose the language that best fits their skillset and the task at hand.


I know, I know, I’ll [never be a real programmer](https://ericsink.com/entries/c_morse_code.html). But I’ve come to terms with my limitations, because I’m a scripter at heart. `<3`

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[scripting languages](https://blog.codinghorror.com/tag/scripting-languages/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[turing complete](https://blog.codinghorror.com/tag/turing-complete/)
