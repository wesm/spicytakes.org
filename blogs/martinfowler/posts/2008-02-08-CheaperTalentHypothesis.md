---
title: "Cheaper Talent Hypothesis"
description: "One of the commonly accepted beliefs in the software world is 	that talented programmers are more productive. Since weCannotMeasureProductivitythis is a belief that cannot be 	proven, but it seems rea"
date: 2008-02-08T00:00:00
tags: ["productivity", "recruiting", "thoughtworks"]
url: https://martinfowler.com/bliki/CheaperTalentHypothesis.html
slug: CheaperTalentHypothesis
word_count: 1170
---


One of the commonly accepted beliefs in the software world is
	that talented programmers are more productive. Since we 
	[CannotMeasureProductivity](https://martinfowler.com/bliki/CannotMeasureProductivity.html) this is a belief that cannot be
	proven, but it seems reasonable. After all just about every human
	endeavor shows some people better than others, often markedly
	so. It's also commonly observed by programmers themselves, although
	it always seems to be remarked on by those who consider themselves to be
	in the better talented category.


Naturally better programmers cost more, either as full-time hires
	or in contracting. But the interesting question is, despite this,
	**are more expensive programmers actually cheaper?**


On the face of it, this seems a silly question. How can a more
	expensive resource end up being cheaper? The trick, as it is so
	often, is to think about the broader picture of cost and value.


Although the technorati generally agree that talented programmers
	are more productive than the average, the impossibility of
	measurement means they cannot come up with an actual figure. So
	let's invent one for argument sake: 2. If you can find a factor-2
	talented programmer for less than twice of the salary of an average
	programmer - then that programmer ends up being cheaper. To state this  more generally: *If the cost premium for
	a more productive developer is less than the higher productivity of
	that developer, then it's cheaper to hire the more expensive
	developer.* The cheaper talent hypothesis is that the cost
	premium is indeed less, and thus it's cheaper to hire more
	productive developers even if they are more expensive.


In case anyone hasn't noticed this hypothesis is a key part of
	our philosophy at Thoughtworks and is one of the main reasons why I
	ended up switching from an independent consultant to join. We
	believe we actually end up cheaper for our clients, even though our
	rates were higher. Of course, we do have difficulty persuading many
	clients that this is true - that lack of objective productivity
	measures strikes again. I still remember a meeting with one
	prospective client complaining about how our rates were higher than
	a company who had made a previous, failed, attempt at the system we
	were bidding on. We had to politely point out that paying less rates
	for a project that delivered no value was hardly a financially
	prudent strategy.


There are some notable consequences to the the cheaper talent
	hypothesis. Most notably is one that it actually follows a positive
	scaling effect - the bigger the team the bigger the benefits of
	cheaper talent. Let's assume we actually have put together a team of
	ten talented developers to run a project in some alternative
	universe where we have actually measures that they are twice as
	productive as the average - and thus do cost exactly twice as much
	to hire. In this case you might naturally assume that a rival team
	of average programmers would be a team of twenty.


The trouble is that that assumption assumes productivity scales
	linearly with team size, which again observation indicates isn't the
	case. Software development depends very much on communication
	between team members. The biggest issue on software teams is making
	sure everyone understands what everyone else is doing. As a result
	productivity scales a good bit less than linearly with team size. As
	usual we have no clear measure, but I'm inclined to guess at it
	being closer to the square root. If we use my evidence-free guess as
	the basis then to get double the productivity we need to quadruple
	the team size. So our average talent team needs to have forty people
	to match our ten talented people - at which point it costs twice as much.


Another factor that plays a role here is time-to-market. Let's
	assume two teams of four people, one talented and one average. To
	stack the deck of our argument against our talented team, discount
	the previous paragraphs, and assume the talented team is only twice
	as productive as the average team. If the talented team charges
	twice as much then can we assume that it doesn't matter financially
	which team we pick?


I'm afraid the talented team wins again. They'll complete the
	project in half of the time of the average team, which means that
	the customer will start yielding value from the delivered software
	earlier. This earlier value, compounded by the time value of
	money, represents a financial gain for picking the talented team,
	even thought their cost per output is the same.


Agile development further accelerates this effect. A talented
	team has a faster cycle time than an average team. This allows the
	full team to explore options faster: building, evaluating,
	optimizing. This accelerates producing better software, thus
	generating higher value. This compounds the time-to-market
	effect. (And it's natural to assume that a talented team is more
	likely to produce better software in any case.)


Faster cycle time leads to a better external product, but perhaps
	the greatest contribution a talented team can make is to produce
	software with greater internal quality. It strikes to me that the
	productivity difference between a talented programmer and an average
	programmer is probably less than the productivity difference
	between a good code-base and an average code-base. Since talented
	programmer tend to produce good code-bases, this implies that the
	productivity advantages compound over time due to internal quality too.


All this sounds, at least to me, like a highly compelling
	argument. It's also one that's widely accepted (at least by
	programmers who consider themselves talented). But it's far off
	being accepted by the software industry as a whole. We can tell this
	because  the premium for talented developers (in terms of
	salary/contracting fees) is less than the 
	productivity difference. Probably the major reason for this the
	inability to objectively measure productivity. A hirer cannot have
	objective proof that a more expensive programmer is actually more
	productive. Only the higher cost is objective. As a result a hirer
	has to match a subjective judgment of higher value against an objective higher
	cost. Many hirers, even if they believe the talented programmer is
	worthwhile personally, isn't prepared to justify the full higher
	cost to managers, HR, and purchasing.


This effect is compounded by the difficulty in making even a
	subjective assessment. At Thoughtworks we rely on  peer assessment -
	developers abilities are assessed by fellow team members. The result
	is hardly pinpoint precision, but it's the best anyone can do.


Which all points out that hiring and retaining talented
	programmers is hard work. Hiring and assessment is hard work. You
	have to deal with people with very individual desires, which are
	even more important to track as they are effectively underpaid. So
	a hirer is faced with certain extra work and higher costs versus
	only a judgment call for higher productivity.


So I understand the situation but don't accept it. I believe that
	if the software industry is to fulfill its potential it needs to
	recognize the cheaper talent hypothesis and close the gap between
	high productivity and higher compensation.
