---
title: "The Road to FogBugz 4.0: Part III"
date: 2005-03-30
url: https://www.joelonsoftware.com/2005/03/30/the-road-to-fogbugz-40-part-iii/
word_count: 2215
---


One day in the summer of 2003, after my friend Uday had finally told me for about the 17th time that he would have bought [FogBugz](http://www.fogcreek.com/FogBugz) but they didn’t have any Windows servers to run it on, I decided to figure out a plan for getting a Unix version. We had looked into Chilisoft, an implementation of ASP and VBScript that runs on Unix, but we didn’t like that idea much because at the time it cost something like $1000 per server and that wouldn’t be acceptable to our customers, who could have bought a whole ‘nother Windows server for not much more than that.


One morning walking to work I thought, gosh, it would be cool to have a summer intern, and I could tell the intern to write an ASP compiler that generated PHP as its output. Then we could produce a Unix version of FogBugz from our source code automatically, and as we added new features to the ASP version, they would magically show up in the PHP version without any more work.


Lo and behold that day this kid named Jimmy calls up the office. He’s just back from Junior year in Italy and he needed a summer job. When I gave him one of my (unpublished!) interview questions (don’t look for it online, you won’t find it) he answered it in exactly the same way as I had answered the same question when Brian MacDonald asked it to me for an internship at Microsoft back in 1990. All the same false starts, the same initially-wrong answer, and eventually, the ideal answer, Jimmy was sounding like a clone of me.


Against my better judgment, knowing myself, we hired him for the summer, and thus was born the Fog Creek Summer Internship program.


Jimmy didn’t know PHP, or ASP, or Java, really, but we thought Java was a good implementation language for an ASP to PHP compiler, so he dealt. Within a few weeks we had something up and running. By the end of the summer it was pretty decent, running FogBugz like a champ, although after Jimmy went back to school, getting all the tiny details right took Michael another couple of months.


I keep calling this thing an ASP to PHP *compiler, *which leads many people to email me saying “don’t you mean *translator?*“


Let me explain.


In computer science jargon a translator IS a compiler. It’s exactly the same thing. Those are synonyms.


In common usage, people think of a compiler as generating machine code, but it doesn’t have to. Java and .NET compilers generate bytecode, for example. And [Stroustrup](http://www.research.att.com/~bs/homepage.html)‘s first C++ compiler, called [Cfront](http://en.wikipedia.org/wiki/Cfront), actually generated C code because C was portable and this made it possible to run C++ on any system that had a C compiler. When you’re inventing a new language it’s a waste of time generating machine language output for every architecture when you can just generate nice messy C code and let **cc** generate the machine language and do all the back end and optimization stuff. Cfront was terribly confusing to a lot of people because it was often referred to as a “preprocessor,” so people got the feeling that C++ was just a clever set of macros that use the old-school C preprocessor **cpp** to generate C code. Nothing could have been farther from the truth. There’s no way you could use the simplistic C preprocessor to convert C++ to C. Cfront was a complete, genuine compiler, with all the classic parts of a compiler: a lexer, a parser, an abstract syntax tree, etc., but instead of outputting machine language which would only work on one CPU, it output terrifying, yet perfectly portable, C code.


And that’s what our ASP to PHP compiler, Thistle, does. It’s a complete compiler, *not* a bunch of glorified regexps, which lexes and parses a VBScript/ASP program, creates an abstract syntax tree in memory, and then generates an “executable program” which happens to be in PHP. So I’ve been calling Thistle a “compiler” sort of to make a point, but mostly because I’m a pedantic windbag who can’t resist the opportunity to teach a little lesson to the younguns who think that a compiler has to generate machine code.


Windbagginess aside, I always get a few questions about Thistle, so I’ll answer the common ones here:


**Q. Why didn’t you use asp2php?**


The quality of the “translation” produced by asp2php is nowhere near good enough to produce production quality code. On samples we fed it, almost every generated line contained an error. There are some really subtle tricks to VBScript and PHP which asp2php seems to completely punt on.


> (OK, you really have to know? In VBScript you can assign an array to a variable one minute, and one minute later assign an object with a default method taking one integer argument to the same variable, so the expression a(1) would translate as $a[1] in the first case and $a->$default(1) in the second case, and it’s the *same expression, *and this fundamental problem was completely punted on by the designers of asp2php, probably justifiably so. In a moment I’ll tell you how we solved it.)


Furthermore, we had a hard-and-fast requirement that the generated PHP code had to work *without further tweaks*. That’s because the ASP code is a living thing which changes all the time, and we constantly regenerate the PHP code automatically. If there were *any* manual tweaks required to get the output of Thistle to work it would dramatically increase the headache of getting a PHP build. So we implemented all kinds of conditional compilation tricks, and since we controlled the compiler, we could build in all kinds of intelligence to make sure that the generated code was exactly what we wanted.


**Q. Why don’t you commercialize this great Thistle thing if it’s so great?**


Thistle is a compiler that only has to compile one program: FogBugz. That means it doesn’t need to include any logic for any features that FogBugz doesn’t use. There are lots of library functions we don’t have to translate because we never call them. And there are conventions in our code that we always adhere to that allow the compiler to take big shortcuts. That means Thistle would not work so well for anyone else off-the-shelf.


> Remember the problem of how to translate **a(1),** which could mean “look up the 2nd element of array **a**” or “call the default method of the object **a** passing the argument 1″ depending on what type **a** contains *at runtime*? This really matters, because we use arrays, and because we use the built-in class RecordSet all over the place, doing things like rs(1) which is short for rs.Item(1).Value, and since VBScript is latebound there is no way to know what code to generate in PHP until runtime, and that’s too late! The only correct thing to do in PHP would be to generate code that checks the type of **a**, and decides, at runtime, whether to do an array lookup or a method call. This is messy and slow and would suck big rocks in the kinds of tight loops where you tend to be using arrays.
> How did we fix it? Well, thanks to Hungarian notation, so callously dissed by developers who do would not recognize a superb coding convention if it walked up to them on the Shanghai Maglev train and shook their pants leg, every recordset at Fog Creek starts with the letters “rs”. And Thistle looks for the rs and say, “ah, this is a recordset, you’re not looking for an array value, you’re calling the default method,” and generates fast code. Based on your age you will either call this an evil hack (if you’re young) or an elegant hack (if you’re old); in either case it’s a huge optimization made possible by the fact that Thistle only has one program to compile. Outside of Fog Creek it wouldn’t work. All hail Hungarian notation!


One more reason we don’t commercialize it: it’s a competitive advantage to us allowing us to create server-side applications that run on Windows OR Unix (or Mac or Solaris or Linux) with a single source tree. But that’s secondary.


**Q. Are you serious about Hungarian notation?**


Yes, it’s standard at Fog Creek. We try to use something called [Apps Hungarian](http://blogs.msdn.com/larryosterman/archive/2004/06/22/162629.aspx) notation, as [invented](http://blogs.msdn.com/ericlippert/archive/2003/09/12/52989.aspx) by Simonyi, *not* the grotesque bastard Systems Hungarian notation, [misinterpreted](http://blogs.msdn.com/rick_schaut/archive/2004/02/14/73108.aspx) by Petzold and the entire Windows team. You can still read [the original paper](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnvs600/html/hunganotat.asp).


> In Apps Hungarian you still have the prefixes, but they are supposed to add semantic information, not merely repeat the type of a variable. So for example when you have a buffer size, the variable should be named “cb”, which means “count of bytes”. Whenever you’re writing C++ code that needs to deal with all kinds of strings, it’s really nice to be able to look at the variable name, and if it’s a psz, you know, oh, look, it’s a pointer to a null-terminated string, but no memory is allocated! Or if it starts with rgch, you know it’s an array of characters, with memory allocated, or rgwch, you know it’s an array of Unicode (wide) chars, or if it starts with ix you know it’s an index to something (or a primary key in SQL), etc. etc. It’s really nice when you’re manipulating unicode that cch means “count of chars” while cb means “count of bytes” since a char is not a byte, and if you ever got confused, the variable name sorts you out. And it’s really nice when you don’t remember if you have a pointer to a string or a pointer to a pointer to a string and the “p” or “pp” at the beginning sorts you out, too. Anyway, Hungarian is widely and correctly reviled by people who don’t see the point of putting dw in front of all your longs, although even that was useful in its day, but using “c” for a count or “ix” for an index is quite helpful.
> In SQL tables we use very light Hungarian to indicate the type of fields: s for strings, dt for date/time, c for a count, ix for a key, n for a number that is not a count of something or a key of some sort. The most useful aspect of this is that if a table is named Bug then you can be certain its primary key is ixBug, so whenever you’re looking at SQL anywhere in the database if you see ixBug you know it’s a foreign key pointing to the Bug table without bothering to look it up. And now without even thinking if you see this snippet of SQL: “join Bar on Foo.ixBar = Bar.ixBar” you know exactly what’s going on, and if you see “join Bar on Foo.**ixFred **= Bar.**ixBar**” then you know it’s probably wrong code because with a little bit of practice the mismatched ixFred/ixBar just jumps out at you. 
> I’m especially driven crazy by people who keep blabbing on their blogs that Hungarian makes code “less” readable. Yes, it’s less readable if you don’t know the convention, but it takes about 10 minutes to learn the convention and all the important prefixes, and people who whine about Hungarian making code “less” readable have obviously never done this. If you know what the prefixes mean Hungarian makes code more readable because every variable gives you a little bit of free, extra useful information you don’t have to go look up.


**Q. How did you handle all the runtime libraries ASP provides?**


We reimplemented them — either in VBScript, which gets translated to PHP, or directly in PHP. In most cases there is a very close PHP equivalent so the reimplementation is one line.


**Q. What about COM objects?**


That was the most work. For our own COM objects we wrote portable C++ code and we compiled that to .so’s for Unix. For one of the major third-party COM objects that we use, we reimplemented it completely in PHP using a built-in PHP library. For the built-ins like Server, Response, Request, Recordset, etc. we created our own classes which usually just call underlying PHP functionality. And our implementation of Server.CreateObject knows all the tricks and just implements a giant select statement that constructs the right kind of object so we don’t need an equivalent of COM class factories.


**Q. Was it worth it?**


Probably. FogBugz for Unix is about 10% of our sales. The effort to create it was probably 20% above the effort to create FogBugz for Windows alone. A lot of our customers are happier that we run on Unix even if they’re using the Windows version, because they know they could switch servers at any time. And finally we have a certain amount of confidence that if Microsoft ever decided to stop making VBScript/ASP work on their server OS, it would be a very simple matter to change Thistle to generate the new flavor of the week … be it Ruby.Net, Eiffel, C#, or [this Language](http://www.muppetlabs.com/~breadbox/bf/).


Tune in again tomorrow, when I’ll talk about all the other stuff we did for FogBugz 4.0 to make it a complete product, not just a computer program.
