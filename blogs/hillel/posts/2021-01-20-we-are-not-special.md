---
title: "We Are Not Special"
date: 2021-01-20
url: https://www.hillelwayne.com/post/we-are-not-special/
slug: we-are-not-special
word_count: 3610
---

*This is part two of the crossover project. Part one is [here](https://www.hillelwayne.com/post/are-we-really-engineers/) and part three is [here](https://www.hillelwayne.com/post/what-we-can-learn/). A conference talk based on this work is now available [here](https://www.hillelwayne.com/talks/crossover-project/).*


> No one thinks about moving the starting or ending point of the bridge midway through construction. *-Justin Cave*
> I had to move a bridge. *-Anonymous*1


Carl worked as a mechanical verification engineer: he tested oil rigs to see how much they vibrated. Humans work and live on oil rigs for long stretches of time, and if they vibrate too much it can be impossible to sleep. While rigs are designed to stay below the threshold, the design and the final version often diverge.


Currently, he was explaining how they find oil. After drilling a hole, he said, “you might also want to add other additives, like acid or hazelnut shells, but also-”


I stopped him. “Hazelnut shells?”


He smiled. “Your oil reservoir is not like a balloon full of oil. It’s more like a porous structure in the rock.” When drilling in, you might hit a sudden loss of pressure in the pipe. This is extremely dangerous as you don’t know if you’ve broken into the open ocean or have just hit a local void. In the latter case, digging further and suddenly hitting a high pressure area could destroy the pipe. By pumping in hazelnut shells they can gradually fill in small voids and test if they are still in the structure, gradually equalizing the pressure if they are.


According to Carl, oil companies are the biggest purchasers of hazelnut shells in Norway.


---


Debates about traditional versus software engineering revolve around what makes us different.  The clichés here come from a different camp than the “what makes an engineer” clichés. The ways people try to define “engineering” often work to marginalize software. Differences like “we don’t have licenses” or “we’re not rigorous” are ways of saying that software is less prestigious, less “good” than traditional engineering. As we saw in the [last essay](https://www.hillelwayne.com/post/are-we-really-engineers/), most of these don’t hold up, and the crossover engineers think the two jobs are much closer in nature than people who have only done one.


When people talk about the fundamental differences, in contrast, they’re usually not aiming to delegitimize software development. Rather, the implicit emphasis is on making software “special”. Making software something that can’t be understood by the narrow lens of engineering.


I see this as a defense mechanism. If software is so different from trad, then it’s okay for us to “not be engineers”. We can say that, sure, we aren’t planning upfront, but that’s because software requirements change so much faster than everywhere else. We don’t apply engineering because we shouldn’t be applying engineering. A good example of this is the [NoEstimates movement](https://techbeacon.com/app-dev-testing/noestimates-debate-unbiased-look-origins-arguments-thought-leaders-behind-movement): because estimates are difficult to make in software, supposedly unlike trad engineering, we should do away with them entirely.


There’s just one problem with this: as software engineers, we deeply misunderstand the nature of trad engineering. We are not special. Almost everything we think is unique about software appears in every other field of engineering. The upside of this is that—well, we are not special. Almost everything we think is awful about software is something everyone else struggles with, too.


## The claimed differences


There’s a fallacy in comparing “trad”, which is an umbrella of different engineering disciplines, to software. Most arguments about engineering don’t go much beyond “software vs engineering”, or conflate “engineering” with civil engineering. All of the subfields are different, and the qualities of one don’t reflect on the qualities of others. After a few interviews, I settled on a set of “universal” differences to discuss:

1. Traditional engineering is best done in a Waterfall style, while software is best done in an Agile one.
2. Trad engineering is very predictable, while software is very unpredictable.
3. Engineering is mostly about manufacture, while code is mostly about design, because “the code is the design”.
4. Trad engineering is much more rigorous than software engineering is.
5. Software moves much faster than traditional engineering does.


These aren’t all wrong. As we’ll see later, there are absolutely some differences between software and trad. But the majority of the differences are “wrong”, or at least lacking critical nuance.


### Traditional is Waterfall, Software is Agile


If there’s one thing we think is uniquely software, it’s Agile.


As it’s told, Agile was a rejection of “Waterfall”, the old paradigm Winston Royce invented in 1970. Royce came up with the Waterfall model to mimic how “real” engineers built buildings. Waterfall says that you should do everything in a strict order, only progressing to the next stage of development when the current stage is completed. You only develop after you complete design, only test after you finish development, etc. This works for “real” engineering but utterly fails for software, where requirements change and often the customer doesn’t know what they want before you build it. So this is rejected by the [Agile Manifesto](https://agilemanifesto.org/) in 2001, and everybody lived happily ever after.


Of course, this story is more fiction than fact. While Waterfall was a dominant model for some time, it was never quite as strict as we think it was today. Nor was it all that ubiquitous: most developers in the 70s and 80s were either working with an ad hoc plan or working in one of the many, many, many “incremental” models that were in fashion, like the [Spiral Model](https://en.wikipedia.org/wiki/Spiral_model) and the [V Model](https://en.wikipedia.org/wiki/V-Model). Agile wasn’t a radical shift as much as a natural consequence of the trends at the time.


But all that is tangential to the core claim: software engineering is Agile, while trad engineering is Waterfall. And this, unsurprisingly, is a significant oversimplification.


It’s true that traditional engineers do a lot more upfront design and spend more time in dedicated testing than software engineers do. But this doesn’t mean they have Waterfall level rigidity, nor does it mean that our Agile is alien to them. Rather, spending a lot of time in phases is a natural consequence of the economic model. When iterations are longer and more expensive it makes more sense to spend more time planning them out. But people use “design” and “implement” in very different ways. When a civil engineer does a scale model, is that design or implementation? When an automotive engineer makes a [full clay replica](http://www.bbc.com/autos/story/20161111-why-car-designers-stick-with-clay) of a car to test its aesthetics and aerodynamics, is that design or implementation?


> When it comes to things like making circuit boards, it’s pretty common for things not to work the first time. You have to do it again, and you have to send it out to the factory and do it again. You know it costs you another however many £1000 and another two weeks on the schedule. *-Mike (electrical)*


We see Agile-like innovations in every industry. Many tunnels today are built with [Austrian Tunneling](https://tunnelingonline.com/understanding-the-new-austrian-tunnel-method-natm/), which relies on iterative development and lots of room for improvisation. The *Handbook of Industrial Engineering* emphasises cross-collaboration and rapid client feedback. Even the most Waterfall form of engineering, civil engineering, gradually shifts to a more Agile-like process once construction starts. People need open communication and adaptation to deal with on-the-ground issues in building.


Why do we think software needs Agile and not Waterfall? Unpredictability. The Waterfall model only makes sense if we can accurately predict and estimate the obstacles inherent in our projects. Because software is unpredictable, the argument goes, we can’t use Waterfall. It could be that halfway through planning, we decide we need to start over. Is it any different for engineers? Is their work any more predictable, more certain than ours?


### “Software is More Unpredictable”


> *Laughter* *-Dawn, Matt, Steve, Mike, Mat, Another Matt*


Part of this misconception comes from us seeing the results of the engineering process, not the process itself. We don’t see the friction, the overruns, the delays that happen because someone built the wall one inch to the left, or when a critical supplier goes out of business. To assume that software is uniquely unpredictable is a special kind of arrogance.


Another part comes from how fast software seems to change. It feels like every year or two there is a new dominant framework or language that everybody’s trying to switch to. We expect that traditional engineering doesn’t have the same constant churn of tooling and paradigm. To an extent, it doesn’t. But less churn is not the same as no churn, and there are many other ways that things can become unpredictable. One chip designer, Steve, found this especially funny:


> In the environment of software world, people are thinking ‘what’s the new JavaScript bundler of the month.’ In the hardware world, it’s ‘what can the silicon fab people do for us this month.’ If the foundry has new machinery to create chips, your plans change. Not as fast as libraries do, but still pretty fast. *-Steve (electrical)*


There are too many anecdotes to go into them all. Territory claims changing in the middle of construction, hardened procedures suddenly and permanently failing, new discoveries well into development. One person talked about how frustrating it is to start work on a bridge foundation, only to find that *this particular soil* freezes in a weird way that makes it liquefy too much in an earthquake. Back to the drawing board.


### “The Code is the Design”


> [Code is design] was a reaction to the people who think “Oh, if we just build a beautiful model in UML and then autogenerate all the code from UML then everything will be fine.”


That’s from [Nick Coghlan](http://www.curiousefficiency.org/). I was surprised when he reached out for an interview; I knew about him as a core CPython developer. Before that, though, he was a systems integration engineer for Boeing. “The diplomatic style of system architecture”, he called it. Boeing would have multiple independent systems- in his example, an airplane, air traffic control, and an antenna array. He had to work with all three teams to make sure they built compatible interfaces. Integration work, essentially. He saw “software is design” as the fundamental difference between his old job and his current one.


Others weren’t so sure. “From my view,” said one, “it was all design”, from the first schematics of the CPU to the final chips rolling out of the foundry. All of their time was spent on design, just like software. Construction was the easy part: just hand the design over to a foundry and get back completed chips.


Of course, the chips will come back flawed, which means a change in design. Design and construction aren’t nearly as disjoint as we software engineers think. Many of the mechanical engineers felt this strongly. The constructed product might show issues in the design, or it might show issues in the circumstances of construction. Mike, one mechanical engineer, called it “fettling”. Tweaking the design to deal with the slight imperfections of the construction process. Every construction changes the design, which changes the construction.


Beyond that, there’s another problem: “design” is not well specified. Are we talking about the architectural overview? The formal specification? The detailed blueprints? If the code is the design then what’s the formal specification of our code? For complex projects there are a lot of different kinds of design at a lot of different levels of detail. If you look at [bridge plans](https://www.dot.state.mn.us/bridge/pdf/abc/br-62646-plan.pdf), you see there are many layers of fractal detail.


I think this is another case where what we mean by design and construction really vary between different kinds of engineering. Yes, in civil engineering the construction phase takes the most time and money, but that’s civil engineering. And only certain kinds of civil engineering, too, the “bridges and buildings” work. The same kind of work on which we base our stereotypes.


> I find myself having to explain that there are many aspects of civil engineering that you wouldn’t specifically consider. […] I tell people it refers to anything that you need to build the city. *-Jen (civil)*


### Rigor


> There’s like a 1,000,000 million times more checks and balances in software than in traditional engineering. […] Whenever someone’s tweeting about, like Excel horror stories *laughter* I have amazing Excel horror stories […] there’s days that I am shocked skyscrapers don’t fall over daily and planes don’t crash. *-Mat*


People say that trad engineering is a lot more rigorous than software. Trad engineers reason carefully from first principles rather than copy-paste. This is usually presented as a problem with software that we need to change to become “real” engineering. It’s also wrong.


First of all, any less rigor we have isn’t entirely cultural, because the essential nature of software makes it a viable tradeoff. Nick explained it as a difference in “validating assumptions”: “you reach a point with the easiest way to check if your assumption is right is to just go in and do it.” Software lets us gather empirical information more easily, which itself is a source of rigour.


But statements about rigor are predicated on the end results of software being different, that trad products are more coherent and less slapdash. That’s not true. For example, we keep much better records and use more comprehensive verification. I heard plenty of horror stories of critical information stored in Excel sheets and old filing cabinets, growing obsolete and corrupt. Plenty would kill to get the same kind of automated testing we treat as a given.


> You can **always** add more brackets. *-Carl*


## The Real Differences


So how is software *different* from everything else? A few ways.


### Consistency


> Software is entirely synthesized. It’s bounded entirely by logic. It doesn’t wear out like a spring, right? It just does what it’s supposed to do. The only thing that can actually go wrong is the specifications. The software was bad. *-Nathan*


Software is far more consistent than any other kind of engineering. We usually think of software as a giant mess, a haze of interdependencies and incompatible hardware, but we actually have it pretty nice. If I give you a sorting function, you can expect it to sort. You do not expect it to sort a given list of (nonpathological) numbers only 95% of the time. That would be ridiculous.


By contrast, let’s look at physical materials. In electrical engineering, a core component is the resistor: a wire that reduces the flow of current. Resistors are measured in ohms, and commodity off-the-shelf resistors can range from a single ohm to hundreds of millions of ohms. Many commodity resistors follow a color chart to make identifying the resistance easy:


![A resistor color chart](https://www.hillelwayne.com/post/crossover-project/img/Resistor_Color_Code_Chart.jpg)

*(source)*


So a band with green, blue, red will have 5600 ohms. Note the last band, though: that specifies the tolerance. The color code only describes the theoretical resistance: if the tolerance band is gold, that means the resistor can vary by up to 5%. If you have a batch of 100 of these resistors, some will be 5320 ohms, some will be 5880 ohms, and the only way to know which is which is to test each one individually. And this is to say nothing about wear and tear, or how resistance varies with temperature, etc.


This is the case of all physical materials. One of my favorite discoveries on the internet, well before I started this project, was the [Fastenal labs page](https://www.fastenal.com/en/59/fastenal-engineering).  Fastenal makes screws. [One of their pages](https://www.fastenal.com/en/70/corrosion) warns against using stainless steel screws on an aluminum plate.


Software engineering has nothing on that.


### Velocity


> The code is the spec for how the hardware should be running. In traditional engineering, we would have to do all that same work to share the spec, but then we have to wait and, like, let the fab or the machine shop finish building the damn thing. And then we’d have to sit there and install it either ourselves or hire somebody. And then we’d have to run testing on it for several weeks to see if it worked or not. *-Matt (chemical)*


This is irrefutable. We can change software much faster than anybody else can change their systems. Several engineers told me that changes had a quantifiable price tag: every time you needed to adjust something, you knew you were taking $5000 from the budget. Whereas I can change some code and run all the tests in seconds.


The closest I found to this in any other field was chemical engineering. “I’d go in the morning and look at what went wrong last night,” said Raja, a former chemical engineer. Something like a one minute turnover would be unheard of, and that’s already in the fastest field of non-software engineering.


This is the nature of our material. And it’s also why other engineering fields are progressively using more software by creating these design tools and simulations, engineers can prototype their ideas with software before implementing them.


There is also a darker side to this. Because software can iterate faster than trad, trad often relies on software to compensate for problems in physical equipment.


> The software engineer is being squeezed by the rest of the team. They’re usually asked to save everyone’s bacon. If something is not quite working in the electronics or mechanics, often you can work around it with a software kludge. *-Mike*


And sometimes this reliance has catastrophic consequences. In 2019 over 300 people died in two 737 MAX airplane crashes. Investigation pinned this to a bug in the “Maneuvering Characteristics Augmentation System” (MCAS), one of the automated flight control systems. But Boeing only added MCAS in the first place to compensate for late-discovered issues with the plane’s [aerodynamic profile](https://leehamnews.com/2018/11/14/boeings-automatic-trim-for-the-737-max-was-not-disclosed-to-the-pilots/). Rather than fix a trad issue with trad engineering,  Boeing opted for the software kludge, and then people died.


### Constraints


> They have a [chip] time budget, you have a time budget, you say ‘I can’t quite make it. Do you have a little slop there? Can I get a fraction of a nanosecond?’ *-Steve*


One implicit undercurrent in all the interviews was the notion of constraint. There are hard physical limits that their products needed to obey. It has to be light enough, or strong enough, or resistant enough, or run cool enough. There is a known quantity they have to maximize or minimize.


Constraints are present in software, too. Code must fit in the memory of an embedded hardware device, the sensor needs a response in exactly 10 cycles, the API must stay under the rate limit. But constraints in software tend to be soft constraints. It is bad to go over them and the more we go over the worse it gets. We can slightly fudge the line if doing so will give us other benefits, like faster development time or simpler algorithms. In traditional engineering, most constraints are hard constraints. If the area of your box is a bit too wide then it won’t fit in the door.2


Sometimes this leads to unusual solutions. One time Carl’s team had to install a [screw conveyor](https://en.wikipedia.org/wiki/Screw_conveyor) in an oil rig, then discovered it was just a couple inches too tall for the room. They couldn’t shrink the equipment, and they couldn’t raise the ceiling, since there were another four floors above it. The team’s solution? Cut a hole in the ceiling, put the equipment in, then put a box around the hole on the next floor so that nobody trips over it. Now that change is permanently part of the rig’s structure, something that has to be accommodated in every future change forever. And that leads to another difference: software engineers can undo their kludges. Trad engineers cannot.


## Do the differences make us special?


While there are many ways we are different, there’s a difference between being “different” and being “special”. Yes, mechanical and electrical engineers don’t have to deal with the same security concerns we do. They also don’t have to deal with weather patterns to the same degree that civil engineers need to, and none of those three need to deal with the problems inherent in chemical engineering. Every field of engineering has unique challenges and software is no different.


But they are all much more similar than they are different. Every field values upfront, abstract thinking, tidy work, and a good kludge in just the right place. Every field faces shifting requirements and unknown unknowns. Every field is siloed from the others: we know as little about the work of mechanical engineers as chemical engineers do. Many times in my interviews, people asked what the other fields of engineering were like. Nobody ever gets a chance to leave their bubble.


And it’s a good thing that software isn’t special. It means that we can learn a lot on how to make software better from these other fields. And it means that they have a lot to learn from us. Because surprisingly, there are some ways that we are better at engineering than traditional engineers. Next time, we’ll cover what we can learn and what we can teach.


*Part three,* [What Engineering Can Teach (and Learn from) Us](https://www.hillelwayne.com/post/what-we-can-learn/), *is available [here](https://www.hillelwayne.com/post/what-we-can-learn/). If you enjoyed these essays, I have a [weekly newsletter](https://buttondown.email/hillelwayne/) and am on [Twitter](https://twitter.com/hillelogram).*


*Thanks to Glenn Vanderburg, [Chelsea Troy](https://chelseatroy.com/), [Will Craft](https://twitter.com/craftworksxyz), and [Dan Luu](https://www.danluu.com) for feedback, and to all of the engineers whom I interviewed.*


---

1. They were not a crossover and so aren’t part of the interviews.
 [return]
2. Some software follows hard constraints, too: if the printer skips a bit then your document is ruined. But “real-time computing” makes up a small minority of the software space.
 [return]
