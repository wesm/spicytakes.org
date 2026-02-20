---
title: "The Sorrows of Java Printing"
date: 2006-06-27
url: https://www.kalzumeus.com/2006/06/28/the-sorrows-of-java-printing/
slug: the-sorrows-of-java-printing
word_count: 512
---


I spent another six hours on the project yesterday. Four hours was spent writing printing code, which is suprisingly difficult in Java (as soon as you’re not printing plain text on the default printer God help you).


On the plus side, writing mountains of boring code is one [barrier to entry](http://onstartups.com/Home/tabid/3339/articleType/ArticleView/articleId/595/Default.aspx). I think it accounts for the paucity of programs solving my need at the moment: most of them are web apps which delegate printing to the browser (which elegantly solves the printing problem at the cost of depriving you of fine-grained control over your program — I’m praying my output clocks the web apps on visual inspection). One of my shareware competitors (one of only a handful who have a desktop app) has apparently discovered the same thing: their program, on Download.com, lists as one of its limitations (paraphrased) “sometimes introduces random output into printed documents”. Thats hopefully something I can avoid.


Anyhow, my quest to get a document formatted exactly the way I wanted it involved tearing up my code about three different times, because I had tried a variety of approaches to printing it. The quick-and-dirty way to print formatted text in Java is to print as HTML. Unfortunately, I discovered belatedly that many printing services my customers will have installed do not support printing HTML directly (whoopsie, I’m spoiled from work).


So, having already gone to the trouble of formatting it as HTML, I decided to make an EditorPane and initialize it from that HTML, then print the EditorPane. Now, while I’ve been programming AWT/Swing for going on 6 years now I’ve never before had to play with EditorPanes that much, and there are some gotchas.


Gotcha #1: EditorPanes render HTML differently than either IE or Mozilla, and in particular they just *can’t* render some HTML elements I need to do (like, say, correctly specifying the width and height of table cells).


So I did it the way I had dismissed at the outset for taking too long — creating my own printing object offscreen and printing that — and, applying painful experience that I got along the way, stripped out 80% of my code and had it done in about 2 hours.


Now, there are some other issues with printing in Java: lets say you want to print a Swing Component. Good for you, but there is a dead zone in the Java API as far as printing services are concerned: Java will format the output and get it to the printer for you but you have to accomplish things like, e.g., printer discovery, etc more or less on your own.


I was saved by [freely available code](http://www.apl.jhu.edu/~hall/java/Swing-Tutorial/Swing-Tutorial-Printing.html) which walks you through the whole printing process. While I had to essentially rip its guts out because I need more finegrained control of printer settings, I would have been lost in confusing and incomplete Java documentation without that site. Hats off to you, professor. (Note: the code is public domain, not GPLed. As an off-again, on-again OSS developer myself I try to be religious about respecting license restrictions.)
