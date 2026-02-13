---
title: "From the “you call this agile?” department"
date: 2006-11-15
url: https://www.joelonsoftware.com/2006/11/15/from-the-you-call-this-agile-department/
word_count: 602
---


Dmitri Zimine has [a hypothetical story](http://www.agileadvice.com/archives/2006/11/how_two_hours_c.html) of how interrupting a programmer for a two hour emergency request needed to close some sale can actually waste two weeks. “If Sarah spends just two hours thinking of her old project, she loses a day of productive work on the new one,” he says.


I agree that [context switching is harmful](https://www.joelonsoftware.com/articles/fog0000000022.html). Absolutely.


Dmitri points out that the development manager should “tell the developer to stick to the original plan. Offer to protect her from switching her mind context. Remind her how cool it is to work single-mindedly on an important and interesting project. Ensure her that I’ll handle the pressure.”


This sounds like something I would agree with, too. I completely agree that management has a responsibility to provide an [abstraction layer for programmers](https://www.joelonsoftware.com/articles/DevelopmentAbstraction.html), so programmers can pretend that the outside world doesn’t exist while they work on code.


However, something in the conclusion here strikes me as odd. Dmitri is only looking at one side of the cost/benefit equation. He’s laid out a very convincing argument why Sarah should not interrupt her carefully planned two week iteration, but he hasn’t even mentioned arguments for the other side: the important sale that will be lost.


Agile development is supposed to be about *agility*. It’s supposed to mean that you can change plans quickly. It’s not supposed to be about rigid programming teams who are so slavishly devoted to their Two Week Plans that they can’t rearrange their schedule a bit to serve the needs of the customer. Dmitri’s conclusion, I’m afraid, strikes me as the very *opposite* of agile development. Agile is *not* supposed to be about swapping out one set of bureaucratic, rigid procedures for another equally rigid set of procedures that still doesn’t take customer’s needs into account.


I don’t know the details of this hypothetical example. Maybe in real life the customer’s needs weren’t really that urgent. But maybe they were? Maybe this customer would have saved the company and made everyone a web 3.0 millionaire, but Sarah’s doctrinaire insistence on following the Two Week Plan (because it was “agile”) made them lose interest? Not sure… there’s only one side of the story here.


Recently Microsoft released a new version of Internet Explorer. They introduced a bug in proxy detection code which caused a very small number of [Copilot](https://www.copilot.com) customers to experience crashes. Meanwhile, the Copilot development team, informally known inside Fog Creek as “Ben,” was busy trying to get Copilot 2.0 out the door. But you know what? Our customers who had installed IE 7 were experiencing crashes. This was not acceptable. Ben stopped what he was doing, installed the old version of the compiler, checked out the old source code, fixed the crash, and pushed a patch out to the server. It interrupted and delayed Copilot 2.0, and the context switching was harmful. But it was still the right decision to make. Being able to do mentally difficult things like context switching makes our product better. This Is Why Programmers Get The Big Bucks. The whole reason you gave them Aeron chairs, unlimited M&Ms, free catered lunches, and the kickass computers with the 30″ LCDs is so they can deal with new bugs Microsoft introduced in their code by messing up a DLL that used to work.


Yes, context switching is painful. Yes, you need to take into account the costs of context switching when you interrupt someone’s work. But every decision has pros and cons and when I hear a manager who is just talking about the cons without considering the pros, that manager is not doing their job.
