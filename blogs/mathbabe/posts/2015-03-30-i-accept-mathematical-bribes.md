---
title: "I accept mathematical bribes"
date: 2015-03-30
url: https://mathbabe.org/2015/03/30/i-accept-mathematical-bribes/
word_count: 853
---


Last Friday I traveled to [American University and gave an evening talk](https://mathbabe.org/2015/03/26/talking-tomorrow-evening-at-american-university/), where I met [Jeffrey Hakim](http://www.american.edu/cas/faculty/jhakim.cfm), a mathematician and designer who openly bribed me.


Don’t worry, it’s not that insidious. He just showed me his nerdy math wallet and said I could have one too if I blogged about it. I obviously said yes. Here’s my new wallet:


It’s made of the same kind of flexible plastic they use on the outside of buildings. Or something. I expect it will last for many years.


You might notice there is writing and pictures on my new wallet! They are mathematical, which is why I don’t feel bad about accepting this bribe: it’s all in the name of education and fun with mathematics. Let me explain the front and back of the wallet.


The front is a theorem:


Here’s the thing, I’ve proven this. I have even assigned it to my students in the past to prove. We always use induction. This kind of identity is kind of made for induction, no? Don’t you think?


Well Jeffrey Hakim had an even better idea. His proof of Nicomachus’s Theorem is represented as a picture on the back of the wallet:


It took me a couple of minutes to see why this is a proof.


Here’s what I’d like you all to do: go think about why this is a proof of the above identity. Come back if you can’t figure it out, but if you can, just go ahead and pat yourself on your back and don’t bother reading the rest of this blogpost because it’s just going to explain the proof.


I’ll give you all a moment…


OK almost ready?


OK cool here’s why this is a proof.


First, convince yourself that this “pattern,” of building a frame of square boxes around the above square, can be continued. In other words, it’s a square of 4 1×1 boxes, framed by 2×2 boxes, framed by 3×3 boxes, and so on. It could go on forever this way, because if you focus on one side of the outside of the third layer, there are 4 3×3 boxes, so length , and we need it to also be the length inside the 4th frame, which has 3 boxes of length 4. Since , we’re good. And that generalizes when it’s the th layer, of course, since the outside of the th layer will have  boxes, each of length  making the inside of the st have  boxes, each of length .


OK, now here’s the actual trick. *What is the area of this box? *


I claim there are two ways to measure the area, and one of the ways will give you the left hand side of Nicomachus’s Theorem but the other way will give you the right hand side of Nicomachus’s Theorem.


To be honest, it’s just one bit more complicated than that. Namely, the first way gives you something that’s 4 times bigger than the left hand side of Nicomachus’s Theorem and the second way gives you something 4 times bigger than the right hand side of Nicomachus’s Theorem.


Why don’t you go think about this for a few minutes, because the clue might be all you need to figure it out.


Or, perhaps you just want me to go ahead and explain it. I’ll do that! That’s why I got the wallet!


OK, now imagine isolating the top right quarter of the above figure. Like this:


That’s a square, obviously, so its area is the square of the length of any side. But if you go along the bottom, the length is obviously  which means the area is the square of that,


And since we know we can generalize the original figure to go up to  instead of just 4, one quarter of the figure will have area  which is to say the entire figure will have area


That’s 4 times the right-hand side of the theorem, so we’re halfway done!


Next, we will compute the area of the original figure a different way, namely by simply adding up and counting all the differently colored squares that make it up. Assume that we continue changing colors every time we get a new layer.


So, there are 4 1×1 squares, and there are 8 2×2 squares, and there are 12 3×3 squares, and there are 16 4×4 squares. In the generalized figure, there would be   squares.


So if you look at the area of the generalized figure which is all one color, say the th color, it will be of the form


That means the overall generalized figure will have total area:


Since that’s just 4 times the left-hand side of the theorem, we’re done.


Notes:

- this would be a fun thing to do with a kid.
- there’s more math inside the wallet which I haven’t gotten to yet.
- After staring at the picture for another minutes, I just realized the total area of the whole (generalized) thing is obviously  which is to say that either the left-hand side or right-hand side of the original identity is one fourth of that. Cool!
