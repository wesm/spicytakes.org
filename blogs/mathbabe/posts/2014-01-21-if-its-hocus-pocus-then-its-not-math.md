---
title: "If it’s hocus pocus then it’s not math"
date: 2014-01-21
url: https://mathbabe.org/2014/01/21/if-its-hocus-pocus-then-its-not-math/
word_count: 1027
---


A few days ago there was a kerfuffle over [this “numberphile” video](http://numberphile.com/videos/analytical_continuation1.html), which was blogged about in Slate [here by Phil Plait](http://www.slate.com/blogs/bad_astronomy/2014/01/17/infinite_series_when_the_sum_of_all_positive_integers_is_a_small_negative.html) in his “Bad Astronomy” column, with a followup post [here](http://www.slate.com/blogs/bad_astronomy/2014/01/18/follow_up_the_infinite_series_and_the_mind_blowing_result.html) with an apology and a great quote from my friend [Jordan Ellenberg](http://quomodocumque.wordpress.com/).


The original video is hideous and should never have gotten attention in the first place. I say that not because the subject couldn’t have been done well – it could have, for sure – but because it was done so poorly that it ends up being destructive to the public’s most basic understanding of math and in particular positive versus negative numbers. My least favorite line from the crappy video:


> I was trying to come up with an intuitive reason for this I and I just couldn’t. You have to do the mathematical hocus pocus to see it.


What??


Anything that is hocus pocus* isn’t actually math*. And people who don’t understand that shouldn’t be making math videos for public consumption, especially ones that have MSRI’s logo on them and get written up in Slate. Yuck!


I’m not going to just vent about the cultural context, though, I’m going to mention what the actual mathematical object of study was in this video. Namely, it’s an argument that “prove” that we have the following identity:


Wait, how can that be? Isn’t the left hand side positive and the right hand side negative?!


This mathematical argument is familiar to me – in fact it is very much along the lines of stuff we sometimes cover at the math summer program [HCSSiM](http://www.hcssim.org/) I teach at sometimes (see my notes from 2012 [here](https://mathbabe.org/hcssim-2012/)). But in the case of HCSSiM, we do it quite differently. Specifically, we use it as a demonstration of *flawed mathematical thinking*. Then we take note and make sure we’re more careful in the future.


If you watch the video, you will see the flaw almost immediately. Namely, it starts with the question of what the value is of the infinite sum


But here’s the thing, that *doesn’t actually have a value*. That is, it doesn’t have a value until you assign it a value, which you can do but then you might want to *absolutely positively must* explain how you’ve done so. Instead of that explanation, the guy in the video just acts like it’s obvious and uses that “fact,” along with a bunch of super careless moving around of terms in infinite sums, to infer the above outrageous identity.


To be clear, sometimes infinite sums do have pretty intuitive and reasonable values (even though you should be careful to acknowledge that they too are assigned rather than “true”). For example, any geometric series where each successive term gets smaller has an actual “converging sum”. The most canonical example of this is the following:


What’s nice about this sum is that it is naively plausible. Our intuition from elementary school is corroborated when we think about eating half a cake, then another quarter, and then half of what’s left, and so on, and it makes sense to us that, if we did that forever (or if we did that increasingly quickly) we’d end up eating the whole cake.


This concept has a name, and it’s *convergence*, and it jibes with our sense of what would happen “if we kept doing stuff forever (again at possibly increasing speed).” The amounts we’ve measured on the way to forever are called *partial sums*, and we make sure they converge to the answer. In the example above the partial sums are  and so on, and they definitely converge to 1.


There’s a mathematical way of defining convergence of series like this that the geometric series follows but that the  series does not. Namely, you guess the answer, and to make sure you’ve got the right one, you make sure that *all of the partial sums are very very close* to that answer if you go far enough, for *any* definition of “very very close.”


So if you want it to get within 0.00001, there’s a number N so that, after the Nth partial sum, all partial sums are within 0.00001 of the answer. And so on.


Notice that if you take the partial sums of the  series you get the sequence  which doesn’t get closer and closer to anything. That’s another way of saying that there is no naively plausible value for this infinite sum.


As for the first infinite sum we came across, the  that *does* have a naively plausible value, which we call “infinity.” Totally cool and satisfying to your intuition that you worked so hard to achieve in high school.


But here’s the thing. Mathematicians are pretty clever, so they haven’t stopped there, and they’ve assigned a value to the infinite sum  in spite of these pesky intuition issues, namely , and in a weird mathematical universe of their construction, which is wildly useful in some contexts, that value is internally consistent with other crazy-ass things. One of those other crazy-ass things is the original identity


[Note: what would be really cool is if a mathematician made a video explaining the crazy-ass universe and why it’s useful and in what contexts. This might be hard and it’s not my expertise but I for one would love to watch that video.]


That doesn’t mean the identity is “true” in any intuitively plausible sense of the word. It means that mathematicians are scrappy.


Now here’s my last point, and it’s the only place I disagree somewhat (I think) with Jordan in his tweets. Namely, I really do think that the intuitive definition is qualitatively different from what I’ve termed the “crazy-ass” definition. Maybe not in a context where you’re talking to other mathematicians, and everyone is sufficiently sophisticated to know what’s going on, but definitely in the context of explaining math to the public where you can rely on number sense and (hopefully!) a strong intuition that positive numbers can’t suddenly become negative numbers.


Specifically, if you can’t make any sense of it, intuitive or otherwise, and if you have to ascribe it to “mathematical hocus pocus,” then you’re definitely doing something wrong. Please stop.
