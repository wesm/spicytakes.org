---
title: "Dynamic, Lightweight Visualization"
date: 2007-01-25
url: https://blog.codinghorror.com/dynamic-lightweight-visualization/
slug: dynamic-lightweight-visualization
word_count: 653
---

Edward Tufte’s [print world](https://blog.codinghorror.com/printer-and-screen-resolution/) is filled with [stunningly beautiful visualizations](http://visualcomplexity.com/vc/). Even seemingly mundane things like [visualizations of Ruby](http://blog.nicksieger.com/articles/2006/10/27/visualization-of-rubys-grammar), Java, and JavaScript grammars can be beautiful. But they’re static. They don’t move. They’re not interactive.


That’s where Ben comes in.


If you haven’t visited [Ben Fry’s website](http://benfry.com/) before, I envy the experience you’re about to have. (Be sure to visit [his old MIT site](http://acg.media.mit.edu/people/fry/), too.) Ben Fry is **Edward Tufte armed with a compiler**. Ben produces incredible dynamic visualizations with his custom Java-based, open-source [processing language](http://processing.org/). It even comes with its own custom IDE:


> We think most “integrated development environments” (Microsoft Visual Studio, Codewarrior, Eclipse, etc.) tend to be overkill for the type of audience we’re targeting with Processing. For this reason, we’ve introduced the ‘sketchbook’ which is a more lightweight way to organize projects. As trained designers, we’d like the process of coding to be a lot more like sketching. The sketchbook setup, and the idea of just sitting down and writing code (without having to write two pages to set up a graphics context, thread, etc.) is a small step towards that goal.
> The idea of just writing a short piece of code that runs very easily (via a little run button) is a direct descendant of John Maeda’s work in [Design By Numbers](http://dbn.media.mit.edu/), and our experiences maintaining it. (Yes, other languages and environments have done this first, but in our case, the concept is drawn from DBN.)


It’s amazing stuff, more akin to sketching than coding. Browse through [the examples gallery](https://web.archive.org/web/20070125051549/http://processing.org/learning/index.html) to get a sense of what’s possible.


![Processing-examples](https://blog.codinghorror.com/content/images/uploads/2007/01/6a0120a85dcdae970b016303735ee7970d-800wi.jpg)


Ben’s latest Processing visualizations, [baseball salary vs. performance](http://benfry.com/salaryper/), and [isometric blocks](http://benfry.com/isometricblocks/), are like **pages from an Edward Tufte book come to life**. And who can forget his classic zipdecode?


If you’ve gone this far with Java-based visualization, you might as well continue on to [IBM’s Many Eyes site](https://web.archive.org/web/20070127040311/http://services.alphaworks.ibm.com/manyeyes/home). You can’t write your own visualization code here; you’re stuck with the predefined visualizations they provide. You *can*, however, upload and share the data sets you’re using to visualize from.


But you might wonder, *what’s with all the Java?* Couldn’t we do this dynamic visualization stuff with something more lightweight, something more appropriate for a web page?

- **JavaScript** is a possibility. After all, we had Wolfenstein 5k, a JavaScript clone of Wolfenstein 3D written [in only 5 kilobytes of JavaScript](http://alistapart.com/articles/5k/), way back in 2002. Sadly, it doesn’t work in any modern browser, or even in any Microsoft OS newer than Windows XP Service Pack 2. But it’s an impressive piece of work nonetheless. It foreshadowed just how reliant the web would become on JavaScript. One such JavaScript visualization, Kyle Scholz’s music recommendation connected graph, is ponderously slow. It leaves me wondering if JavaScript is really up to the task of visualization, even with the [HTML Canvas element](http://en.wikipedia.org/wiki/Canvas_(HTML_element)).
- What about **Flash**? Surely visualization is a better use for Flash than the [legions of advertisements](https://blog.codinghorror.com/a-world-of-endless-advertisements/) (and, now, *video* advertisements) I’m subjected to every day. Although I can find some isolated visualizations in Flash, I’m not seeing a vibrant visualization community there.
- On the Windows side, there’s some hope for **Windows Presentation Foundation**, which ships in every Vista box. [WPF](http://en.wikipedia.org/wiki/Windows_Presentation_Foundation), and its lightweight cousin WPF/E, could enable lightweight, *hardware accelerated* visualization – something that’s sorely lacking from all the other options. To see what I mean, try [this WPF 3D sample](https://web.archive.org/web/20061116044344/http://thewpfblog.com/?p=53), which runs entirely in the browser. But the technology is far too new to have any kind of community.


If I wanted to see static illustrations, I’d read a book. But dynamic visualizations aren’t quite there yet for web pages. Right now, you have to pick your technology poison. They all have their downsides. Still, it’s something worth striving for. I yearn for **the day when web pages are regularly illustrated with the kind of beautiful, dynamic visualizations that Ben Fry creates**.

[java](https://blog.codinghorror.com/tag/java/)
[processing language](https://blog.codinghorror.com/tag/processing-language/)
[dynamic visualization](https://blog.codinghorror.com/tag/dynamic-visualization/)
[interactive visualizations](https://blog.codinghorror.com/tag/interactive-visualizations/)
[lightweight ide](https://blog.codinghorror.com/tag/lightweight-ide/)
