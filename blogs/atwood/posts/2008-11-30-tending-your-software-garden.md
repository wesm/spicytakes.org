---
title: "Tending Your Software Garden"
date: 2008-11-30
url: https://blog.codinghorror.com/tending-your-software-garden/
slug: tending-your-software-garden
word_count: 1124
---

Software: do you write it like a book, grow it like a plant, accrete it like a pearl, or construct it like a building? As Steve McConnell notes in [Code Complete 2](http://www.amazon.com/exec/obidos/ASIN/0735619670), there’s no shortage of **software development metaphors**:


> A confusing abundance of metaphors has grown up around software development. David Gries says [writing software is a science](https://books.google.com/books?id=vv5pot-ySsEC&dq=%22david+gries%22+software+science&pg=PP1&ots=YtjTrk6clc&source=bn&sig=OVW2eoYseX6bERH5CFcLggiIbmc&hl=en&sa=X&oi=book_result&resnum=4&ct=result) (1981). Donald Knuth says [it’s an art](http://en.wikipedia.org/wiki/The_Art_of_Computer_Programming) (1998). Watts Humphrey says [it’s a process](http://en.wikipedia.org/wiki/Personal_Software_Process) (1989). [P. J. Plauger](http://en.wikipedia.org/wiki/P._J._Plauger) and Kent Beck say it’s like [driving a car](https://books.google.com/books?id=G8EL4H4vf7UC&pg=PA28&lpg=PA28&dq=%22kent+beck%22+driving+car+2000&source=web&ots=j7uLsrlYxr&sig=EydaBn1wL6kZY-KO0KTDYm0lgFk&hl=en&sa=X&oi=book_result&resnum=8&ct=result), although they draw nearly opposite conclusions (Plauger 1993, Beck 2000). Alistair Cockburn says [it’s a game](https://blog.codinghorror.com/software-development-as-a-collaborative-game/) (2002). Eric Raymond says it’s [like a bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/) (2000). Andy Hunt and Dave Thomas say it’s [like gardening](http://www.artima.com/intv/gardenP.html). Paul Heckel says it’s [like filming Snow White and the Seven Dwarfs](http://www.amazon.com/dp/0782115381) (1994). Fred Brooks says that it’s like farming, hunting werewolves, or [drowning with dinosaurs in a tar pit](http://en.wikipedia.org/wiki/The_Mythical_Man-Month) (1995). Which are the best metaphors?


I think we’re leaving one metaphor on the table which more accurately reflects the way software is built in the real world: flail around randomly and pray you succeed by [force of pure dumb luck](https://blog.codinghorror.com/escaping-from-gilligans-island/). Sometimes it even works. [Not very often](https://blog.codinghorror.com/the-long-dismal-history-of-software-project-failure/), but just enough to confuse people who should know better into thinking they’re smart, when what they really were is lucky.


The answer, of course, is **whichever metaphor helps you and your team get to the end of the project**. Personally, I see them as more of a battle cry, a way for a team to communicate a shared vision and a set of values. They’re heavy on imagery and metaphor, and light on specific, concrete advice.


Even as Steve McConnell argues that most software development metaphors come up short, he quite clearly picks a favorite, and spends quite a bit of time defending his choice. It’s not exactly a secret, as it’s in the subtitle for the book: [Code Complete](https://www.amazon.com/Complete-Microsoft-Programming-Steve-McConnell/dp/1556154844): A Practical Handbook of Software Construction.


As much as I respect Steve, my software project experience to date doesn’t match the controlled construction metaphor. I agree with Thomas Guest; [software is soft; buildings aren’t](https://web.archive.org/web/20081203074212/http://wordaligned.org/articles/why-software-development-isnt-like-construction). I’m more partial to the model that Andy Hunt and Dave Thomas promote, what I call **tending your software garden**.


![](https://blog.codinghorror.com/content/images/2025/04/image-151.png)


Programmers as farmers, if you will.


All the best software projects I’ve worked were, for lack of a better word, *alive*. I don’t mean that literally, of course. But the software was constantly and quite visibly growing. There were regular, frequent release schedules defining its evolution. There was a long term project commitment to a year out, five years out, ten years out.


To me, the parallels between farming and software development are strong and evocative. Steve disagrees.


> The weakness in the software-farming metaphor is its suggestion that you don’t have any direct control over how the software develops. You plant the code seeds in the spring, *Farmer’s Almanac* and the Great Pumpkin willing, you’ll have a bumper crop of code in the fall.


To be clear, all these metaphors are abstract and therefore heavily subject to interpretation (and/or useless, take your pick), so I don’t want to get too wrapped up in defending one.


That said, I disagree with Steve’s dismissal. The strength of the farming metaphor is the implied **commitment to the craft**. Farming is hard, unforgiving work, but there’s a yearly and seasonal ritual to it, a deep underlying appreciation of sustainable and controlled growth, that I believe software developers would do well to emulate. I also think Steve was a bit unfair in characterizing farming as “no direct control.” There’s plenty of control, but lots of acknowledged variables, as well – which I think more accurately represents the [shifting sands of software development](https://blog.codinghorror.com/bridges-software-engineering-and-god/). Farmers do their best to control those variables, of course, but most of all they must adapt to whatever conditions they’re dealt. Next season, next year, they know they’ll be back with a renewed sense of purpose to try it all again and do better. Not so coincidentally, these are also traits shared by the best software developers I’ve known.


In particular, **the rise of the web software development model has made the farming model more relevant**. Where traditional software like Office might go through a bunch of monolithic, giant construction project updates every two to three years – from Office XP, to Office 2003, to Office 2007 – websites can be deployed far more often. Seasonally, if you will. Some websites even “harvest” monthly, organically growing new features and bugfixes each time. The guys at 37Signals [apparently noticed this, too](http://www.37signals.com/svn/posts/591-brainstorm-the-software-garden).


> It recently dawned on me that software grows much in the same way that plants grow. New features are the flowers of the software world. And just as most plants aren’t flowering all year long, software isn’t sprouting features all year long. There’s flowering season. There’s new feature season. There’s infrastructure season.
> Sometimes software is working on its roots. Bolstering its infrastructure. It’s growing underground where the public can’t see it. It looks like nothing’s happening, but there’s really a lot going on. Without those roots new features can’t sprout.
> And sometimes it’s rest time. Plants rest in the winter. Software often rests in the summer (it’s too nice to work too hard in the summer). Everything can benefit from a deep breath, relaxation, and sleep. Chaotic constant growth and change doesn’t make room for order and organization. Growth requires new energy and new energy requires rest.


Another thing I’ve noticed is that tending to websites, which usually have community features and user-generated content at the forefront, feels a heck of a lot like [weeding your garden](https://blog.codinghorror.com/blacklists-dont-work/). You grow a lot of content, but not all of it is exactly what you had in mind.


> I scrutinize every comment, and I remove a tiny percentage of them: they might be outright spam, patently off-topic, or just plain mean. I like to refer to this as weeding my web garden. It’s a productivity tax you pay if you want to grow a bumper crop of comments, which, despite [what Joel says](http://www.joelonsoftware.com/items/2007/07/20.html), often [bear such wonderful fruit](https://blog.codinghorror.com/a-blog-without-comments-is-not-a-blog/). The labor can be minimized with improved equipment, but it’s always there in some form. And I’m OK with that. The myriad benefits of a robust comment ecosystem outweighs the minor maintenance effort.


And when you don’t weed your garden? The weeds threaten to choke out your crops. Eventually, your software garden looks neglected, and then abandoned.


![](https://blog.codinghorror.com/content/images/2025/04/image-150.png)


As Steve says, some software development metaphors are better than others. But when it comes to web development, at least, you could certainly do a lot worse than **tending to your software garden**.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[software engineering practices](https://blog.codinghorror.com/tag/software-engineering-practices/)
[metaphorical concepts](https://blog.codinghorror.com/tag/metaphorical-concepts/)
