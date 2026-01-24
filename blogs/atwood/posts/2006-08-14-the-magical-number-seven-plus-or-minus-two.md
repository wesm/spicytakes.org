---
title: "The Magical Number Seven Plus or Minus Two"
date: 2006-08-14
url: https://blog.codinghorror.com/the-magical-number-seven-plus-or-minus-two/
slug: the-magical-number-seven-plus-or-minus-two
word_count: 697
---

The seminal 1956 George Miller paper [The Magical Number Seven, Plus or Minus Two](http://psychclassics.yorku.ca/Miller/): Some Limits on Our Capacity for Processing Information is a true classic. In it, Miller observed that the results of a number of 1950s era experiments in short-term memory had something in common: **most people could only retain 5 to 9 items in their short-term memory**.


This study is commonly cited as the reason why Bell chose to make telephone numbers exactly 7 digits long. I can’t find any formal citations to support this, but the timing is right: by 1957 or thereabouts, most telephone numbers in the US were standardized to the 7-digit format.


5551212


Are human beings only capable of holding between 5 and 9 pieces of information in their heads at once? **That’s only 2.5 bits of information.** If you read the text of the paper, you’ll quickly find that even Miller himself found [the magic number seven](http://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two) a bit serendipitous:


> And finally, what about the magical number seven? What about the seven wonders of the world, the seven seas, the seven deadly sins, the seven daughters of Atlas in the Pleiades, the seven ages of man, the seven levels of hell, the seven primary colors, the seven notes of the musical scale, and the seven days of the week? What about the seven-point rating scale, the seven categories for absolute judgment, the seven objects in the span of attention, and the seven digits in the span of immediate memory? For the present I propose to withhold judgment. Perhaps there is something deep and profound behind all these sevens, something just calling out for us to discover it. But I suspect that it is only a pernicious, Pythagorean coincidence.


The 7 digit figure might be a little optimistic. Other research has shown the number to [be closer to 4](https://web.archive.org/web/20070208201657/http://www.bbsonline.org/Preprints/OldArchive/bbs.cowan.html). Even telephone numbers aren’t commonly expressed as seven digits. They’re expressed as a group of three digits and four digits, with a dash to separate them:


**555-1212**


And the area code is separated, too:


**434-555-1212**


So which is it? Can people remember 7 digits at once? Or are they really remembering chunks of 3 digits, 3 digits, and 4 digits?


I think **magical numbers are a red herring**. There are some interesting coincidences, however, such as Edward Hall’s conclusion that [the perfect group size](http://37signals.com/svn/archives2/edward_hall_the_perfect_group_size_812.php) is 8-12 people:


> Fortunately, something is known both empirically and scientifically about the influence exerted by size on groups and the effect of size on how the groups perform. Research with business groups, athletic teams, and even armies around the world has revealed there is an ideal size for a working group. This ideal size is between eight and twelve individuals. This is natural, because man evolved as a primate while living in small groups... to 12 persons can know each other well enough to maximize their talents. In groups beyond this size, the possible combinations of communication between individuals get too complex to handle; people are lumped into categories and begin the process of ceasing to exist as individuals. Tasks than can’t be handled by a group of eight to 12 are probably too complex and should be broken down further. Participation and commitment fall off in larger groups – mobility suffers; leadership doesn’t develop naturally but is manipulative and political.


The value of this magical number lies in knowing the point of diminishing returns. Every group should strive to be as small as possible. Once the group size exceeds 8-12 people, break into another group.


Similar advice applies to software design. **Ideally users shouldn’t have to remember anything**. Once they have to remember *more* than 7 items, it’s definitely time to redesign.

- In a well-designed system, you should never need to fall back on your faulty, unreliable short-term memory.
- The fewer bits of information users have to remember, the better.
- Use chunking and grouping aggressively to reduce the amount of information to remember.


Magical numbers are fun. But the ideal group size is always one, and the ideal number of things I should need to keep in my short-term memory is zero.

[psychology](https://blog.codinghorror.com/tag/psychology/)
[memory](https://blog.codinghorror.com/tag/memory/)
[information processing](https://blog.codinghorror.com/tag/information-processing/)
[cognitive science](https://blog.codinghorror.com/tag/cognitive-science/)
[human factors](https://blog.codinghorror.com/tag/human-factors/)
