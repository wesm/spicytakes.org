---
title: "Updating The Single Most Influential Book of the BASIC Era"
date: 2021-12-31
url: https://blog.codinghorror.com/updating-the-single-most-influential-book-of-the-basic-era/
slug: updating-the-single-most-influential-book-of-the-basic-era
word_count: 1326
---

In a way, these two books are [responsible for my entire professional career](https://blog.codinghorror.com/everything-i-needed-to-know-about-programming-i-learned-from-basic/).


![](https://blog.codinghorror.com/content/images/2025/02/image-255.png)


With early computers, you didn’t boot up to a fancy schmancy desktop, or a screen full of apps you could easily poke and prod with your finger. No, **those computers booted up to the command line.**


![](https://blog.codinghorror.com/content/images/2025/02/image-256.png)


From here, if you were lucky, you might have a cassette tape drive. If you knew the right commands, you could type them in to load programs from cassette tape. But that was an expensive add-on option with early personal computers. For many of us, if we wanted the computer to do anything, we had to type in entire programs from books like [101 Basic Computer Games](https://en.wikipedia.org/wiki/BASIC_Computer_Games), by hand... [like so](https://www.atariarchives.org/basicgames/showpage.php?page=2).


![](https://blog.codinghorror.com/content/images/2025/02/image-257.png)


Yep, believe it or not, circa 1983, *this was our idea of a good time*. No, we didn't get out much. The book itself was a sort of greatest hits compilation of games collected from Ahl’s seminal [Creative Computing Magazine](https://www.atarimagazines.com/creative/v10n11/66_Dave_tells_Ahl__the_hist.php) in the 1970s:


> As soon as Ahl made up his mind to leave DEC, he started laying the groundwork for Creative Computing. He announced intentions to publish the magazine at NCC in June 1974 and over the next few months contacted prospective authors, got mailing lists, arranged for typesetting and printing, and started organizing hundreds of other details.
> In addition, he also moved his family to Morristown, NJ, and settled into his new job at AT&T. He had little spare capital, so he substituted for it with “sweat equity.” He edited submitted articles and wrote others. He specified type, took photos, got books of “clip art,” drew illustrations, and laid out boards. He wrote and laid out circulation flyers, pasted on labels, sorted and bundled mailings.
> By October 1974, when it was time to specify the first print run, he had just 600 subscribers. But Ahl had no intention of running off just 600 issues. He took all the money he had received, divided it in half, and printed 8000 copies with it. These rolled off the presses October 31, 1974. Ahl recounts the feeling of euphoria on the drive to the printer replaced by dismay when he saw two skids of magazines and wondered how he would ever get them off the premises. Three trips later, his basement and garage were filled with 320 bundles of 25 magazines each. He delivered the 600 subscriber copies to the post office the next day, but it took nearly three weeks to paste labels by hand onto the other 7400 copies and send them, unsolicited, to libraries and school systems throughout the country.


I also [loved Creative Computing](https://blog.codinghorror.com/the-best-of-creative-computing/), but it was a little before my time:

- 1971 – Ahl ports the programs from FOCAL to BASIC.
- 1973 – 101 BASIC Computer Games is first published by DEC.
- 1974 – Ahl founds [Creative Computing](https://en.wikipedia.org/wiki/Creative_Computing_(magazine)) magazine and acquires the rights to the book from DEC.
- 1977 – the “trinity” of [Apple II](https://en.wikipedia.org/wiki/Apple_II) 🖥️, [PET ](https://en.wikipedia.org/wiki/Commodore_PET) ️🖥️, and [TRS-80 ](https://en.wikipedia.org/wiki/TRS-80) 🖥️ microcomputers are released to the public, all with BASIC built in, at prices regular people could mostly afford. 🙌
- 1978 – a second edition of BASIC Computer Games is released, this time published by Ahl himself.


As you can see, there’s no way average people in 1973-1976 were doing a whole lot with BASIC programs, as *they had no microcomputers capable of running BASIC to buy! *It took a while for inexpensive personal computers to trickle down to the mainstream, which brings us to roughly 1984 when the sequels started appearing.


There was a half-hearted attempt to [modernize these early BASIC programs](https://social.technet.microsoft.com/wiki/contents/articles/16765.basic-computer-games-small-basic-edition.aspx) in 2010 with SmallBasic, but I didn’t feel these ports did much to bring the code up to date, and overall had little relevance to modern code practices. You can compare the [original 1973 BASIC Civil War](https://pastebin.com/j4jzGd4V) with the [2010 SmallBasic port](https://pastebin.com/5q1B0t2C) to see what I mean:


![](https://blog.codinghorror.com/content/images/2025/02/image-258.png)


Certainly we can do a bit better than merely removing the line numbers? What about our old buddy the subroutine, *merely the *[*greatest invention in computer science*](https://blog.codinghorror.com/the-greatest-invention-in-computer-science/)? It’s nowhere to be seen. 🤔


So it was with considerable enthusiasm that I contacted [David H. Ahl](https://en.wikipedia.org/wiki/David_H._Ahl), the author, and asked for permission to create a website that attempted to truly update all these ancient BASIC programs.


![](https://blog.codinghorror.com/content/images/2025/02/image-259.png)


Thankfully, permission was granted. It’s hard to understate [how important this book was](https://time.com/69316/basic/) to an entire generation of programmers. At one point, **there were more copies of this book in print than there were personal computers, period!**


> ... in 1973, DEC published an anthology, *101 BASIC Computer Games*. The book quickly went into a second printing, for a total of 10,000 copies sold. “That was far more books than there were computers around, so people were buying three, four, five of them for each computer.”


It went on to be the [first computer book to sell a million copies](https://en.wikipedia.org/wiki/BASIC_Computer_Games#Reception). Quite a legacy.


I think we owe it to the world to bring this book up to date using **modern, memory safe languages that embody the original spirit of BASIC, **and modern programming practices including subroutines.


So let’s do this. **Please **[**join us on GitHub**](https://github.com/coding-horror/basic-computer-games), where we’re updating those original 101 BASIC games in 10 memory safe, general purpose scripting languages:

- Java / Kotlin
- Python
- C#
- VB.NET
- JavaScript
- Ruby
- Perl
- Lua


(Edit: as of March 2022, we’ve a) offered Kotlin as an alternative to Java, b) removed Pascal since we can’t guarantee memory safety there, and replaced it with Rust, which very much can, and c) added Lua which *just* cracked the top 20 in TIOBE and strongly meets the scripting and memory safe criteria.)


Now, bear in mind these are *very* primitive games from the 1970s. They aren’t going to win any awards for gameplay, or programming sophistication. But they *are *[precious artifacts of early computing](https://en.wikipedia.org/wiki/Early_mainframe_games) that deserve to be preserved for future generations, including the wonderful [original art by George Beker](http://www.bekerbots.com/botbooks.htm).


![](https://blog.codinghorror.com/content/images/2022/01/Chomperanimated2.gif)


**We need your help to do this right**, and *collaboratively together*, as with all modern programming projects. Imagine we’re all typing these programs in simultaneously together online, all over the world, instead of being isolated alone in our room in 1984, cursing at the inevitable typo we made somewhere when typing the code in by hand out of the book. 🤬


Thanks Mr. Ahl. And a *big* thanks to everyone who contributed to this project when it was in beta, announced only on Twitter:

- Oscar Toledo ([nanochess](https://github.com/nanochess))
- Tim Buchalka ([journich](https://github.com/journich))
- Dave LeCompte ([tsmaster](https://github.com/tsmaster))
- Nezumi Ronin ([NezumiRonin](https://github.com/NezumiRonin))
- Daniel Piron ([danielpiron](https://github.com/danielpiron))
- Darren Cardenas ([darrencardenas](https://github.com/darrencardenas))
- Alvaro Frias ([qequ](https://github.com/qequ))
- Jamie McCarthy ([jamiemccarthy](https://github.com/jamiemccarthy))
- Roger Bamforth ([rbamforth](https://github.com/rbamforth))
- Peter Ruderman ([pgruderman](https://github.com/pgruderman))
- Piotr Czajkowski ([pczajkowski](https://github.com/pczajkowski))
- Jack Boyce ([jkboyce](https://github.com/jkboyce))
- [epvanhouten](https://github.com/epvanhouten)
- Topher Lamey ([clamey](https://github.com/clamey))
- [kt--](https://github.com/kt--)
- Tom Armitage ([infovore](https://github.com/infovore))
- Richard Nienaber ([rjneinaber](https://github.com/rjnienaber))
- [marvin826](https://github.com/marvin826)
- Aldrin Misquitta ([aldrinm](https://github.com/aldrinm))
- [olliehcrook](https://github.com/olliehcrook)
- Gustavo ‘Gus’ Carreno ([gcarreno](https://github.com/gcarreno))
- Nahid Mondol ([NahidMondol](https://github.com/NahidMondol))


To encourage new contributions, by the end of 2022,** for every functioning program submitted in each of the 10 indicated languages, I’ll donate $5 to **[**Girls Who Code**](https://girlswhocode.com/). Before beginning, please [read the guidelines](https://github.com/coding-horror/basic-computer-games/blob/main/README.md) in the readme, and if you have questions, [scan through this discussion topic](https://discourse.codinghorror.com/t/updating-101-basic-computer-games-for-2022-and-beyond/7927). And most of all, remember, [this stuff is supposed to be fun](https://blog.codinghorror.com/remember-this-stuff-is-supposed-to-be-fun/).


(I don’t want to be “that one guy,” so I’m also looking for project co-owners who can help own and organize this effort. If this is a project that *really* appeals to you, show me what you can do and let’s work together as a team.)


Perhaps as your new year’s resolution you can see fit to carve off some time to take part in **our project to **[**update a classic programming book**](https://github.com/coding-horror/basic-computer-games) – *one of the most influential books in computing history* – for 2022 and beyond! 🎉

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[basic programming](https://blog.codinghorror.com/tag/basic-programming/)
[computer history](https://blog.codinghorror.com/tag/computer-history/)
[computer games](https://blog.codinghorror.com/tag/computer-games/)
