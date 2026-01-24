---
title: "Parsing Html The Cthulhu Way"
date: 2009-11-15
url: https://blog.codinghorror.com/parsing-html-the-cthulhu-way/
slug: parsing-html-the-cthulhu-way
word_count: 1317
---

Among programmers of any experience, it is generally regarded as A Bad Ideatm to attempt to parse HTML with regular expressions. How bad of an idea? It apparently drove one Stack Overflow user to [the brink of madness](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454):


> You can't parse [X]HTML with regex. Because HTML can't be parsed by regex. Regex is not a tool that can be used to correctly parse HTML. As I have answered in HTML-and-regex questions here so many times before, the use of regex will not allow you to consume HTML. Regular expressions are a tool that is insufficiently sophisticated to understand the constructs employed by HTML. HTML is not a regular language and hence cannot be parsed by regular expressions. Regex queries are not equipped to break down HTML into its meaningful parts. so many times but it is not getting to me. Even enhanced irregular regular expressions as used by Perl are not up to the task of parsing HTML. You will never make me crack. HTML is a language of sufficient complexity that it cannot be parsed by regular expressions. Even Jon Skeet cannot parse HTML using regular expressions. Every time you attempt to parse HTML with regular expressions, the unholy child weeps the blood of virgins, and Russian hackers pwn your webapp. Parsing HTML with regex summons tainted souls into the realm of the living. HTML and regex go together like love, marriage, and ritual infanticide. The <center> cannot hold it is too late. The force of regex and HTML together in the same conceptual space will destroy your mind like so much watery putty. If you parse HTML with regex you are giving in to Them and their blasphemous ways which doom us all to inhuman toil for the One whose Name cannot be expressed in the Basic Multilingual Plane, he comes. HTML-plus-regexp will liquify the n​erves of the sentient whilst you observe, your psyche withering in the onslaught of horror. Rege̿̔̉x-based HTML parsers are the cancer that is killing StackOverflow *it is too late it is too late we cannot be saved* the transgression of a chi͡ld ensures regex will consume all living tissue (except for HTML which it cannot, as previously prophesied) *dear lord help us how can anyone survive this scourge* using regex to parse HTML has doomed humanity to an eternity of dread torture and security holes *using rege*x as a tool to process HTML establishes a brea*ch between this world* and the dread realm of c͒ͪo͛ͫrrupt entities (like SGML entities, but *more corrupt) a mere glimp*se of the world of reg​**ex parsers for HTML will ins**​tantly transport a p*rogrammer's consciousness i*nto a w*orl*d of ceaseless screaming, he comes, the pestilent slithy regex-infection wil​**l devour your HT**​ML parser, application and existence for all time like Visual Basic only worse *he comes he com*es *do not fi*​ght h**e com̡e̶s, ̕h̵i**​s un̨ho͞ly radiańcé de*stro҉ying all enli̍̈́̂̈́ghtenment, HTML tags **lea͠ki̧n͘g fr̶ǫm ̡yo​͟ur eye͢s̸ ̛l̕ik͏e liq**​uid p*ain, the song of re̸gular exp​ression parsing will exti*​nguish the voices of mor​**tal man from the sp**​here I can see it can you see ̲͚̖͔̙î̩́t̲͎̩̱͔́̋̀ it is beautiful t​*he f`inal snuf`fing o*f the lie​**s of Man ALL IS LOŚ͖̩͇̗̪̏̈́T A****LL I​S L***OST th*e pon̷y he come*s he c̶̮omes he co**mes t*he* ich​**or permeat*es al*l MY FAC*E MY FACE ᵒh god n**o NO NOO̼****O​O N***Θ stop t*he an​*̶͑̾̾​̅ͫ͏̙̤g͇̫͛͆̾ͫ̑͆l͖͉̗̩̳̟̍ͫͥͨ*e̠̅s` ͎a̧͈͖r̽̾̈́͒͑e` n**​ot rè̑ͧ̌aͨl̘̝̙̃ͤ͂̾̆ ZA̡͊͠͝LGΌ ISͮ̂҉̯͈͕̹̘̱ T**O͇̹̺ͅƝ̴ȳ̳ TH̘**Ë͖́̉ ͠P̯͍̭O̚​N̐Y̡ H̸̡̪̯ͨ͊̽̅̾̎Ȩ̬̩̾͛ͪ̈́̀́͘ ̶̧̨̱̹̭̯ͧ̾ͬC̷̙̲̝͖ͭ̏ͥͮ͟Oͮ͏̮̪̝͍M̲̖͊̒ͪͩͬ̚̚͜Ȇ̴̟̟͙̞ͩ͌͝**S̨̥̫͎̭ͯ̿̔̀ͅ


The unicode action in the post is the best part of the gag. If you can't see it for some reason, here's a screenshot just in case:


![](https://blog.codinghorror.com/content/images/2025/10/stack-overflow-answer-parsing-html-the-cthulhu-way.png)


That’s right, if you attempt to parse HTML with regular expressions, you’re succumbing to the temptations of the dark god [Cthulhu’s](https://en.wikipedia.org/wiki/Cthulhu)… er… *code*.


![](https://blog.codinghorror.com/content/images/2025/04/image-445.png)


This is all good fun, but the warning here is only partially tongue in cheek, and it is born of [a very real frustration](https://web.archive.org/web/20071018202901/http://oubliette.alpha-geek.com/2004/01/12/bring_me_your_regexs_i_will_create_html_to_break_them).

kg-card-begin: html

> I have heard this argument before. Usually, I hear it as justification for seeing something like the following code:
> # pull out data between <td> tags
> ($table_data) = $html =~ /<td>(.*?)</td>/gis;
> “But, it works!” they say.
> “It’s easy!”
> “It’s quick!”
> “It will do the job just fine!”
> I berate them for not being lazy. You need to be lazy as a programmer. **Parsing HTML is a solved problem. You do not need to solve it. You just need to be lazy.** Be lazy, use CPAN and use [HTML::Sanitizer](https://web.archive.org/web/20090718212111/http://search.cpan.org/~nesting/HTML-Sanitizer-0.04/Sanitizer.pm). It will make your coding easier. It will leave your code more maintainable. You won’t have to sit there hand-coding regular expressions. Your code will be more robust. You won’t have to bug fix every time the HTML breaks your crappy regex.

kg-card-end: html

For many novice programmers, there’s something unusually seductive about parsing HTML the Cthulhu way instead of, y’know, using a library like a sane person. Which means this discussion gets reopened almost every single day on Stack Overflow. The above post from five years ago could be a discussion from *yesterday*. I think we can forgive a momentary lapse of reason under the circumstances.


Like I said, this is a well understood phenomenon in most programming circles. However, I was surprised to see a few experienced programmers [in metafilter comments](http://www.metafilter.com/86689/So-does-anyone-know-how-to-make-an-HTML-regex-parser) actually **defend the use of regular expressions to parse HTML**. I mean, they’ve heeded the [Call of Cthulhu](https://en.wikipedia.org/wiki/The_Call_of_Cthulhu)… and *liked* it.


> Many programs will neither need to, nor should, anticipate the entire universe of HTML when parsing. In fact, designing a program to do so may well be a completely wrong-headed approach, if it changes a program from a few-line script to a bulletproof commercial-grade program which takes orders of magnitude more time to properly code and support. Resource expenditure should always (oops, make that very frequently, I about overgeneralized, too) be considered when creating a programmatic solution.
> In addition, hard boundaries need not always be an HTML-oriented limitation. They can be as simple as “work with these sets of web pages,” “work with this data from these web pages,” “work for 98% users 98% of the time,” or even “OMG, we have to make this work in the next hour, do the best you can.”


We live in a world full of newbie PHP developers doing the first thing that pops into their collective heads, with more born every day. What we have here is an ongoing education problem. The real enemy isn’t regular expressions (or, for that matter, [goto](https://blog.codinghorror.com/id-consider-that-harmful-too/),) but ignorance. The only crime being perpetrated is not knowing what the alternatives are.


So, while I may *attempt* to parse HTML using regular expressions [in certain situations](https://blog.codinghorror.com/programming-is-hard-lets-go-shopping/), I go in knowing that:

- It’s generally a bad idea.
- Unless you have discipline and put very strict conditions on what you’re doing, matching HTML with regular expressions rapidly devolves into madness, *just how Cthulhu likes it*.
- I had what I thought to be good, rational, (semi) defensible reasons for choosing regular expressions in this specific scenario.


It’s considered good form to demand that regular expressions be considered verboten, totally off limits for processing HTML, but I think that’s just as wrongheaded as demanding **every trivial HTML processing task be handled by a full-blown parsing engine**. It’s more important to understand the tools, and their strengths and weaknesses, than it is to knuckle under to knee-jerk dogmatism.


So, yes, generally speaking, it *is* a bad idea to use regular expressions when parsing HTML. We should be teaching neophyte developers that, absolutely. Even though it’s an apparently never ending job. But we should also be teaching them the very real difference between [parsing HTML](http://en.wikipedia.org/wiki/Parsing) and the simple expedience of processing a few strings. And how to tell which is the right approach for the task at hand.


Whatever method you choose – just don’t leave the <cthulhu> tag open, for humanity’s sake.

[regex](https://blog.codinghorror.com/tag/regex/)
[html parsing](https://blog.codinghorror.com/tag/html-parsing/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
