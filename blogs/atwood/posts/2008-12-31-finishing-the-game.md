---
title: "Finishing The Game"
date: 2008-12-31
url: https://blog.codinghorror.com/finishing-the-game/
slug: finishing-the-game
word_count: 946
---

In [yesterday’s post](https://blog.codinghorror.com/the-problem-of-the-unfinished-game/), I asked this question:


> Let’s say, hypothetically speaking, you met someone who told you they had two children, and one of them is a girl. **What are the odds that person has a boy and a girl?**


Most people answer 50%.


Unfortunately, this isn’t correct.


This problem, although seemingly simple, is hard to understand. For cognitive reasons that are not fully understood, while our intuitions regarding *a priori *possibilities are fairly good, we are easily misled when we try to use probability to quantify our knowledge. This is a fancypants way of saying there were almost a *thousand* comments on that post, with not a lot of agreement to be found.


The key thing to bear in mind here is that **we have been given additional information**. If we *don’t* use that information, we arrive at 50% – the odds of a girl or boy being born to any given pregnant woman. That’s true insofar as it goes, but it’s the answer to a different, much simpler question, and certainly not the answer to the question we asked.


Our question contains additional information:

1. The person has two children.
2. One of those children is a girl.


We can use that information to come up with a better, more correct answer. **We know this person has two children**. What are all possible combinations of two children?


`BB, GB, BG, GG`


![](https://blog.codinghorror.com/content/images/2025/04/image-257.png)


**We know that one of the children is a girl**. This rules out one of those possible combinations of two children (BB), so we’re left with:


`GB, BG, GG`


![](https://blog.codinghorror.com/content/images/2025/04/image-256.png)


Of the remaining three possibilities, *two* include boys.


`GB, BG`


Thus, **the odds of this person having a boy and a girl is 2/3 or 66%**.


I noticed a few comments where people complained that the GB and BG possibilities are the same thing, and should have been reduced to


`BG/GB, GG`


Which equates to 1/2 or 50%.


If you made this mistake, you’re in good company: so did [Blaise Pascal](http://en.wikipedia.org/wiki/Blaise_Pascal), as the book [The Unfinished Game](http://www.amazon.com/dp/0465009107): Pascal, Fermat, and the Seventeenth-Century Letter that Made the World Modern explains.


![](https://blog.codinghorror.com/content/images/2025/04/image-255.png)


Here’s how Keith Devlin describes the famous letter:


> In 1654, the gambler Antoine Gombaud, whose noble title was the Chevalier de Mere, apporached his friend Pascal with some questions about games of chance, including the problem of the unfinished game. After some thought, Pascal found a possible solution but was not completely sure his reasoning was correct. Accordingly, he sent his ideas to Fermat to see if his countryman agreed with the argument. The brief exchange of letters that ensued – and one letter in particular – represented one of the most profound advancements in the history of mathematical thought.


I’ll tell you one thing I learned from this book: **It’s amazing how many early advancements in math were based on gambling**. I guess it’s sort of the same historical relationship between video technology and pornography. Not that there’s anything wrong with that. Anyway, the “unfinished game” I alluded to in my previous post title is the central topic of these letters between Blaise Pascal and [Pierre Fermat](http://en.wikipedia.org/wiki/Pierre_de_Fermat). Here’s a modernized, slightly simplified version of it:


> Two players, Harry and Ted, place equal bets on who will win the best of 5 coin tosses. In each round, Harry always chooses heads (H), and Ted always chooses tails (T). Suppose they are forced to abandon the game after 3 coin tosses, with Harry ahead 2 to 1. What is the fairest way to divide the pot?


Let’s enumerate all possible outcomes from the 2 remaining coin tosses.


`HH HT TH TT`


Only 1 of these 4 possibilities allows Ted to win. Thus, if the game has to be abandoned, the pot should be split 3/4 to Harry and 1/4 to Ted.


But, since Harry is already ahead 2 to 1, you might argue that it’s nonsensical to consider all those “extra” possibilities; as soon as Harry gets that third head on a coin toss, the game is over. Thus, **we only need to consider possibilities where the game would actually continue**:


`H TH TT`


By this accounting, Harry would get 2/3 of the pot, and Ted 1/3. We know this is wrong. By leaving the game “unfinished” and not enumerating every possibility – we’ve made a mistake. But how?


You don’t need to be a mathematician to prove this. I’m just a crappy programmer, and even my crappy code can brute force the answer by simulating results from thousands of games.

kg-card-begin: html

```

var rand = new Random();
var results = new Dictionary<string, int>();
int tosses = 2;
for (int i = 0; i < 10000; i++)
{
string result = “HHT”;
for (int toss = 0; toss < tosses; toss++)
{
result += (rand.Next(2) == 0) ? “H” : “T”;
if (Regex.Matches(result, “H”).Count == 3 || Regex.Matches(result, “T”).Count == 3) break;
}
if (results.ContainsKey(result))
results[result]++;
else
results.Add(result, 1);
}
foreach (var item in results)
{
Console.WriteLine(item.Key + “ : ” + item.Value);
}

```

kg-card-end: html
kg-card-begin: html


| `HHTTT` | 2,438 |
| `HHTTH` | 2,457 |
| `HHTH` | 5,105 |


kg-card-end: html

**The unfinished games are not equally likely!** But the results are definitely clear, and agree with what the **equally likely finished games** predicted: 75% for Harry, and 25% for Ted.


I’ve made awfully similar “unfinished game” mistakes before, in particular when [writing a card shuffling algorithm](https://blog.codinghorror.com/the-danger-of-naivete/). It was my hope in presenting this problem that you’ll be able to recognize it too the next time you see it, even if the math behind it is not at all intuitive.

[probability](https://blog.codinghorror.com/tag/probability/)
[logical reasoning](https://blog.codinghorror.com/tag/logical-reasoning/)
[statistics](https://blog.codinghorror.com/tag/statistics/)
