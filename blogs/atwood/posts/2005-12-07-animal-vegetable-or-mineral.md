---
title: "Animal, Vegetable, or Mineral?"
date: 2005-12-07
url: https://blog.codinghorror.com/animal-vegetable-or-mineral/
slug: animal-vegetable-or-mineral
word_count: 1252
---

![](https://blog.codinghorror.com/content/images/2025/03/image-368.png)


The 1978 BASIC program [Animal](http://www.atariarchives.org/basicgames/showpage.php?page=4) is an animal-specific variation of [twenty questions](http://en.wikipedia.org/wiki/Twenty_questions). You think of an animal, and the computer tries to guess what animal you’re thinking of by asking a series of yes or no questions. **If the computer is stumped, the user is prompted to enter a question that would distinguish the unknown animal from the previous question.** Thus, the more the program runs, the more it “learns” about animals.


The [20 questions website](http://20q.net/) is a natural extension of Animal, but with a fancier [neural network](http://en.wikipedia.org/wiki/Neural_network) technique fed by [infinite internet monkeys](http://en.wikipedia.org/wiki/Infinite_monkey_theorem). And now it’s even available in [portable handheld game format](https://kk.org/cooltools/20q/):


> The other day Will Wright, the genius behind Sim City and the Sims, handed me this tennis ball-size orb and said, “It knows what you are thinking.” Most of the time it will guess what you have in mind after asking you twenty yes/no questions. It is eerily smart, and slightly addictive. I see it as an educational toy.
> Burned into its 8-bit chip is a neural net that has been learning for 17 years. Inventor Robin Burgener programmed a simple neural net on a DOS machine in 1988. He taught it 20 questions about a cat. He than passed the program around to friends on a floppy and had them challenge the neural net with their yes/no answers to the object they had in mind. The neural net learns only when it plays a game; no data is added except for the yes/no answers of visitors. So the more people who test it, the more they teach it. In 1995 Burgener put the now robust neural net onto the new web where anyone could play it (that is, train it) 24 hours a day. And they did. Burgener’s genius was to turn the hard tedious work of training a neural net into a fun game for humans.
> Last year, after 1 million rounds of 20 questions online, the neural net had accumulated 10 million synaptic associations. It has a 73% success rate of guessing what you thought. Burgener then compressed the 20Q code to run on a chip, and had the neural net select 2,000 of the most popular 10,000 objects it then knew about. He then had the neural net select out the most useful 250,000 synaptic connections related to those 2,000 objects, and hard wired that learning into the chip in the orb. In other words, this sphere is a handheld version of Burgener’s Twenty Questions web site. Because it knows about fewer objects than the web version, it gets confused less often, so its success rate is ironically higher.


My Mom, bless her heart, bought me one of these little handheld 20 question games. And it does work, after a fashion. Here’s a transcript of me using the 20 Questions website to figure out “egg”:


1.  Is it Animal, Vegetable, Mineral, or Other? Animal.
2.  Does it have short fur? Irrelevant.
3.  Does it make a good pet? No.
4.  Can it scratch? No.
5.  Does it have ears? No.
6.  Does it have feelings? No.
7.  Does it dig holes? No.
8.  Does it breathe? No.
9.  Is it a specific color? Yes.
10. Does it taste good fried? Yes.
11. Do you use it in public? Sometimes.
12. Does it roll? Yes.
13. Can it be used in a pie? Rarely.
14. Can it be dried? No.
15. Does it reflect objects? No.
16. Is it healthy? Sometimes.
17. I am guessing that it is an egg? **Right!**

Even though it got the right answer, I feel a little bit stupider having actually answered ridiculous questions like “can it be used in a pie” and “can it scratch.” Maybe we should blame the users for these bad questions: **garbage in, garbage out**. But you know you’re really in trouble when there’s a detailed [20 questions reference](http://barelybad.com/20_questions.htm#substance) offering extensive guidance on the very first question:

kg-card-begin: html

> To begin with, anything that’s never been alive is mineral, and everything else must therefore be either animal or vegetable (unless you count microscopic entities such as bacteria and viruses, which you should).  Here are three examples:
> If you’ve chosen as your target the clock inside London’s Big Ben, you should answer, “Mineral,” because the clock parts are made of steel and brass and copper and so on, which are minerals.
> If you’ve chosen as your target the wool sweater you’re wearing, you should say, “Animal,” because it’s made of wool, which comes from sheep, which am animals.
> And if you’ve chosen the T-shirt that your date is wearing, you should say, “Vegetable,” because it’s made of cotton, which is a plant.

kg-card-end: html

Reading a bit further on in that article, full of its contradictions and subjectivity (is a pencil vegetable or mineral?), **it’s clear that the problem isn’t the people, but the question**. Dividing the world into rigid hierarchies of any kind – whether they be animal, vegetable, mineral, or other – simply doesn’t work very well.


So if, like me, you feel stupid when playing 20 questions, that’s a perfectly rational reaction, because [structured, hierarchical categorization sucks](https://web.archive.org/web/20051210031138/http://shirky.com/writings/ontology_overrated.html):


> **We are moving away from binary categorization – books either are or are not entertainment – and into this probabilistic world, where N% of users think books are entertainment**. It may well be that within Yahoo, there was a big debate about whether or not books are entertainment. But they either had no way of reflecting that debate or they decided not to expose it to the users. What instead happened was it became an all-or-nothing categorization, “This is entertainment, this is not entertainment.” We’re moving away from that sort of absolute declaration, and towards being able to roll up this kind of value by observing how people handle it in practice.
> [. . .]
> Critically, the semantics here are in the users, not in the system. This is not a way to get computers to understand things. When del.icio.us is recommending tags to me, the system is not saying, “I know that OSX is an operating system. Therefore, I can use predicate logic to come up with recommendations – users run software, software runs on operating systems, OSX is a type of operating system – and then say ‘Here Mr. User, you may like these links.’”
> What it’s doing instead is a lot simpler: “A lot of users tagging things foobar are also tagging them frobnitz. I’ll tell the user foobar and frobnitz are related.” It’s up to the user to decide whether or not that recommendation is useful – del.icio.us has no idea what the tags mean. The tag overlap is in the system, but the tag semantics are in the users. This is not a way to inject linguistic meaning into the machine.
> It’s all dependent on human context. This is what we’re starting to see with del.icio.us, with Flickr, with systems that are allowing for and aggregating tags. **The signal benefit of these systems is that they don’t recreate the structured, hierarchical categorization so often forced onto us by our physical systems.** Instead, we’re dealing with a significant break – by letting users tag URLs and then aggregating those tags, we’re going to be able to build alternate organizational systems, systems that, like the Web itself, do a better job of letting individuals create value for one another, often without realizing it.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[artificial intelligence](https://blog.codinghorror.com/tag/artificial-intelligence/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
