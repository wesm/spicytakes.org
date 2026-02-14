---
title: "Open source hooliganism and the TypeScript meltdown"
date: 2023-09-07
url: https://world.hey.com/dhh/open-source-hooliganism-and-the-typescript-meltdown-a474bfda
slug: open-source-hooliganism-and-the-typescript-meltdown-a474bfda
word_count: 858
---

I've seen a lot of true believers argue for virtues of their favorite paradigms and methods over the decades working in software. And mostly, I look at people with a passionate preference and smile. Isn't it great that people care so much about their craft that they volunteer to extol the benefits of their favorite tools! Yes it is, but there's also a fine line between being a passionate evangelist and becoming a dogmatic crusader. And a sad but critical mass of the TypeScript faithful chose the latter in response to our decision to drop their beloved compiler from our project yesterday. It was
[at times](https://twitter.com/dhh/status/1699427078586716327)
a full-on meltdown. Yuck.
Now before we go into the particulars of this meltdown, it's worth stating that there were also people with completely legitimate objections to dropping TypeScript from
[Turbo](https://turbo.hotwired.dev/)
. Mostly people with standing as active contributors or users of the framework. I'm always happy to have technical discussions in good faith with such individuals, and they're certainly entitled to their opinion on a move like this without getting tarred by association with the hooligans who showed up spoiling for a fight.
But the brunt of the debate was carried by people with absolutely no stake in the particulars of Turbo. People who showed up to crusade for a narrative that tells them only
[the incompetent](https://twitter.com/t3dotgg/status/1699476772235137036)
or
[the malevolent](https://twitter.com/Rich_Harris/status/1699490194565578882)
would deny the divine glory of their superset. To defend the honor of TypeScript, which they had somehow found besmirched by someone on the internet not being as enthusiastic about the language extensions as they are.
This lead to
[several](https://github.com/hotwired/turbo/pull/972)
[ridiculous](https://github.com/hotwired/turbo/pull/973)
pull requests for "adding TypeScript back!", complete with the pile-on rush resembling those trashing the streets after their favorite sports team lost a match. The jeering and the emojis and the rockets and the LGTMs!!! There was even
[a pull request for deleting the Turbo repository altogether](https://github.com/hotwired/turbo/pull/974)
. And
[an issue](https://github.com/hotwired/turbo/issues/977)
to have me, personally, removed from the project that 37signals founded, funded, and continues to be the primary maintainer of. Alongside
[other](https://github.com/hotwired/turbo/issues/982)
[issues](https://github.com/hotwired/turbo/issues/982)
just chanting slogans. Just absolutely unhinged open-source hooliganism.
Now maybe you could have argued some sliver of a justification for this, had it been in opposition to a tirade against the evils of TypeScript, the wholesale denigration of its users, or perhaps a petition for Microsoft just to shut the whole thing down.
[But this was none of the sort!](https://world.hey.com/dhh/turbo-8-is-dropping-typescript-70165c01)
This was one project, mostly overseen by one company, that removed TypeScript from their own project, and explained why, while allowing amble room and spirit for others to reach different conclusions for their own work.
As I said, dogmatic crusading on behalf of pieces of technology isn't exactly new. And it isn't restricted to programming tools either. I remember some epic flamewars all the way back in the old Newsgroup days on the virtues of owning a Sony PlayStation or a Sega Saturn. Equally conducted by overzealous nerds marshaling The Facts as to why one would be absolutely idiot to pick one instead of the other.
It's also not like I hold myself above the fray in all regards. I certainly used to dance the line between evangelist and crusader, particularly in the early days of Ruby on Rails. But even so, would have found it absolutely inconceivable to show up in someone's open source repository to deface its collaboration organs. This is a new variety of open source advocacy that, as I said, resembles hooliganism more than it does even 1990s newsgroup console superfans and their flamewars. And it's entirely unbecoming for a profession like ours.
I expect that most anyone with a genuine care for TypeScript will in a few days or weeks be able to look back at this meltdown with more than a little ambivalence, if not shame. To have so many key advocates engage or encourage this kind of behavior, this kind of slander, and this kind of hooliganism against those who don't share their team colors is frankly embarrassing.
It's also a weird exhibition of self-loathing in the choice of technology. TypeScript is JavaScript! It's a superset that sprinkles an appearance of type safety on top of a weakly- and dynamically-typed language. To muster such rabid animosity towards anyone celebrating the use of the subset is but an illustration of the ferocity and visciousness of minor differences.
That's the eternal wisdom of bikeshed parable. That when the stakes are low, the debate more easily becomes nasty. Showing up for a fight on something so ultimately unresolvable as whether to use compiler-based type checking or not offers the thrill of hooliganism. An opportunity to let the inhibitions drop and the freak fly, for a moment, for a single match, which will be repeated in season after season until the end of time. It's the exercise of the Id.
Look, I'm happy if you found your true calling in TypeScript. I really am. I'm an unapologetic superfan of Ruby. But please, for the love of open source culture, find another way to express your enthusiasm than by defacing collaboration organs or slandering those who JavaScript differently with accusations of incompetence or malice.
