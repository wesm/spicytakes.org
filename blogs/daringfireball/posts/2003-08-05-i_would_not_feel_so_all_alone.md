---
title: "I Would Not Feel So All Alone"
date: 2003-08-05
url: https://daringfireball.net/2003/08/i_would_not_feel_so_all_alone
slug: i_would_not_feel_so_all_alone
word_count: 1410
---


When I [last wrote about Andrew Stone](http://daringfireball.net/2003/04/stoned.html), I accused him of dishonesty regarding his blatantly inaccurate anti-Carbon propaganda. I’ve reconsidered, however. I don’t think he’s dishonest, but rather that he’s in a deep state of denial.


The gist of the story: Stone is a long-time Next developer, widely regarded as a leading expert in Apple’s Cocoa application framework (which is directly descended from the Next application framework). A few months ago, his company Stone Design released a new utility for Mac OS X called [FontSight](http://www.stone.com/FontSight/FontSight.html) that displays a WYSIWYG font menu in other applications (similar to old Mac OS utilities like MenuFonts or Action WYSIWYG).


However, FontSight *only works with Cocoa applications*. This is a serious limitation, given that almost all professional Mac design software is Carbon, not Cocoa. And of course, professional designers are the main market for a font utility like FontSight.


On the FontSight web pages, Stone defends this limitation by describing Cocoa apps as the only “native” software for Mac OS X. That canard is exactly what I took Stone to task over previously. It’s just not true.


Where I went wrong, I think, is in accusing Stone of underhandedness. I made the assumption that because Stone is obviously very intelligent, that he must realize that Carbon is not a stop-gap, that it is a fundamental API layer on Mac OS X that is here to stay. Thus, I assumed, he knew that what he was saying wasn’t true, and was doing so to create FUD (fear, uncertainty, doubt) among less technically-savvy Mac users. I.e. trying to convince people to buy Stone Design software not because it’s better, but just because it’s Cocoa.


But now, a few months later, I’ve come to a different conclusion: Andrew Stone is out of his fucking mind.


Exhibit A is a May 28 post from his company weblog: [FontSight - works great with “native” Mac OS X apps](http://www.stone.com/StoneLog/StoryComments.php?story_id=43). Ignore the “Carbon isn’t ‘native’” nonsense. Just read it — it’s fascinating. The gist is that Stone is getting lots of email from people telling him that FontSight looks great, but they can’t use it (and thus won’t buy it) because it doesn’t work with their design software. Stone’s response, more or less: *Tough.*


Think about this. Potential customers are telling him exactly what they want FontSight to do to make it useful for them; and Stone is responding by saying he absolutely will not do that. That simply isn’t rational. The hole in Stone’s stance, from a business perspective, is a mile wide. There is obviously a market for a WYSIWYG font menu utility that works with the popular software people actually use.


“Utilities” are the small software packages people buy to work alongside their main applications. People aren’t going to abandon their software from Adobe, Microsoft, and Macromedia just to use a Cocoa-only menu font utility. They want a menu font utility that works with their existing software. Duh.


Late last month [Unsanity’s Rosyna Keller unveiled FontCard](http://www.unsanity.org/archives/000222.php), an upcoming Haxie that will provide a WYSIWYG font menu in both Cocoa *and* Carbon apps. Compare and contrast Keller’s comments with Stone’s. Keller readily admits that getting FontCard to work in most major Carbon applications was difficult — different apps use different techniques to create their font menus, and FontCard needs to handle each case differently — but necessary in order to create a utility that meets users’ needs. Stone, on the other hand, admits that he won’t even consider supporting Carbon applications.


## Rhapsody in Blue


And so assuming Unsanity’s FontCard works as advertised (and given Unsanity’s track record, that’s a very reasonable assumption), who in their right mind would opt for the Cocoa-only FontSight? Other than the users of an imaginary world where the Carbon APIs don’t exist, *no one*.


And so what explains Stone’s refusal to address this limitation? Hypothesis: Stone’s conception of Mac OS X remains unchanged from circa 1997, at the outset of the Apple/Next merger. Apple’s initial post-Next plans — which not coincidentally were drawn up by Next expatriates — did not include Carbon. The idea was to produce a system with one native API — the Next object-oriented application framework — and a compatibility layer for classic Mac OS software. In other words, Cocoa and Classic, but no Carbon.


To say Mac developers were less than thrilled by this plan is a gross understatement — they rejected it completely, and rightly so. Apple’s original plan more or less boiled down to replacing the Mac OS with NextStep; Mac developers had the crazy idea that it should be replaced with a new version of the Mac OS. Apple listened, the plan was revised, and six years later, here we are.


Apparently, no one sent Stone the memo. Stone heard what he wanted to hear — that his beloved Next system was replacing the Mac OS — and refuses to acknowledge that this Next-only “Mac OS” of the future was scrapped in the planning stages, replaced by a genuinely new system derived from *both* the old Next and Mac systems.


Let’s dissect Stone’s comments:


> I’ve been getting tons of email saying “FontSight is
> 	great — but it doesn’t work with InDesign or  AncientCarbonProgram X Y
> 	or Z”.


It’s worth noting that InDesign is a relative newcomer, just a few years old — much newer than, say, Stone Design’s Create.


> Folks, I’ve been slaving away for the last 15 years to bring the
> 	object technology of NeXT (now called Cocoa) to the Macintosh Masses.
> 	In 1997, Gil Amelio told all the legacy Mac developers this was the
> 	future, and they should begin an effort to rewrite their code in Cocoa
> 	(then called Rhapsody).


Stone’s argument that Carbon applications are irrelevant and/or deprecated hinges on the word of Gil Amelio? *Gil Amelio?* What Gil Amelio said in 1997 is about as relevant today as something uttered by Gerald Ford in 1975. Ancient history.


> They  decided to ignore him and instead demanded a way for the new
> 	Mac OS X to run the old macos [*sic*] 9 code. 
>  Fine, now you have old code — with all of its old bugs — running
> 	on a brand new spanking OS.


Is it worth pointing out that unless Stone has some sort of paddle connected to his machine, he probably meant *brand spanking new OS* rather than *brand new spanking OS*? Maybe. But it’s definitely worth pointing out that there’s no inherent reason why old Carbon code would contain any more bugs than old Cocoa code, and many of Stone Design’s products date back to 1989 and the early years of Next.


> These carbon [*sic*] apps are simply quick ports and DO NOT
> 	take advantage of all that is cool in Mac OS X and Cocoa like Create
> 	and other Stone Studio apps do.


Carbon apps don’t take advantage of all that Cocoa offers? Uh, nor do pure Cocoa apps take advantage of all Carbon has to offer. Duh.


> All of Apple’s new apps — iPhoto, KeyNote, Mail, TextEdit, etc. —
> 	use Cocoa — and thus FontSight works perfectly with them.


All of Apple’s new apps, that is, with the exception of ones like Final Cut, iTunes, and the Finder.


> We cannot be apologists for old carbon [*sic*] apps, so
> 	please don’t expect Stone Design to come up with ways to make those
> 	entrenched carbon [*sic*] apps work more gracefully on OS X.


This sentence encapsulates how Stone is missing the entire point. Carbon and Cocoa are developer APIs; they are of no interest whatsoever to normal Mac users. None. Really. Normal Mac users choose their software based on tangible surface qualities — the features, the human interface, their existing toolset, etc. They don’t care what programming tools were used to create their software any more than they care what CAD program was used to design their automobiles.


Stone’s entire argument against supporting Carbon applications in FontSight is about developer APIs that users don’t care about. This benefits no one — Stone Design is missing out on an untapped market, and Mac users are missing out on a potentially useful piece of software.


It’s not something to get angry about. It’s just sad.


## Further Reading


[Eric Blair refutes Stone](http://www.raoli.com/archives/2003/05/000089.php), with gusto.



| **Previous:** | [Mailsmith, an iBook, and Glider Pro Walk Into a Bar](https://daringfireball.net/2003/08/mailsmith_an_ibook_and_glider_pro_walk_into_a_bar) |
| **Next:** | [Crayolas](https://daringfireball.net/2003/08/crayolas) |


PreviousNext