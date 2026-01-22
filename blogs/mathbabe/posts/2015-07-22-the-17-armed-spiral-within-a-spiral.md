---
title: "The 17-armed spiral within a spiral"
date: 2015-07-22
url: https://mathbabe.org/2015/07/22/the-17-armed-spiral-within-a-spiral/
word_count: 882
---


Last Friday I visited my high school math camp, [HCSSiM](http://www.hcssim.org/), where I became a nerd. I also taught there multiple times over the years, and in 2012 I [blogged my lectures](https://mathbabe.org/hcssim-2012/).


Why the visit? You see, we loyal alums of HCSSiM have a tradition of going back every July 17th to celebrate “Yellow Pig day,” which consists of a talk where founder and director [(David) Kelly](https://en.wikipedia.org/wiki/David_Kelly_(mathematician)) talks extensively about fun facts regarding the number 17, which happens before dinner, and then after dinner we sing “yellow pig carols” and eat an enormous amount of cake in the shape of a yellow pig. You can learn more about this ridiculous and hilarious tradition [here](https://en.wikipedia.org/wiki/User:Samir/Yellow_Pigs_Day).


Anyhoo, this year we (I went with other nerds) missed the 17 talk because of traffic in Connecticut but we made it for the dinner and carols. Luckily at dinner I had the chance to talk to Kelly, and I asked him if there were any new 17 facts this year. He told me there was one, and it was slightly mysterious. This post is an attempt to explain it a bit.


The mathematical set-up is explained [here](http://math.stackexchange.com/questions/1336443/ulam-spiral-and-triangular-numbers). Namely, we start with something called the [Ulam Spiral](https://en.wikipedia.org/wiki/Ulam_spiral), which is simply a way to label the boxes of an infinite two-dimensional grid with the natural numbers. You start at some place and then spiral outwards from there. Here’s a picture:


The center of the Ulam Spiral


OK, so the first thing to say is that, when you label the plane like this, primes tend to cluster along lines. I think this is what Ulam thought was cool about his spiral:


Primes are black. This is the spiral with 200 layers.


Now comes the observation. You need to know what a [triangular number](https://en.wikipedia.org/wiki/Triangular_number) is first, though. Namely, it’s a number that corresponds to counting up how many dots you need to form a triangle. We say the nth triangular number corresponds to a triangle with n rows. Here are the first few:


You can also draw these triangles so that consecutive ones fit together to form squares.


When you highlight the triangular numbers in the Ulam Spiral, instead of the primes, then you get something that looks weird:


Green dots are triangular numbers within the Ulam Spiral.


OK so if you count those spiral arms, you’ll see there are 17 of them. But does that last forever? And if so, why?


Well, the answer is going to be yes. And here’s a rough proof. Rough because it uses asymptotic limits, so technically I will not show that the above picture extends perfectly, but rather that it eventually does look like a spiral with 17 arms.


A famous story about Gauss tells us that the formula for the nth triangular number is


Also, by construction of the Ulam Spiral, the bottom right corner of each “spiral layer” is an odd square, and that if we call that number  there will be  boxes on the very next layer, corresponding to the 4 sides of the next layer plus the 4 corners of the next layer.


Now imagine that there’s a triangular number right on that bottom right corner. That would mean that for some


or in other words that


This is when things get asymptotic. Imagine that  is very very large. That would mean that  is too (everything here is a positive integer), and in particular that the  term would dwarf the  term above. In other words, we could approximate:


My next question is, how many triangular numbers would lie on the next layer of the spiral? Well, as we said above there are  spots in the next layer, which we will approximate by  and the triangular number coming after  is  which is  bigger than  corresponding to adding one layer to a triangle with  rows. We will approximate  by  again ignoring small terms.


For that matter, the next few triangular numbers after  come regularly, about  spots after the first. Therefore there are about  triangular numbers in the next row of the Ulam spiral. That comes out to  which is about 2.83.


So far we’ve figured out that, when  is huge, then after meeting the th triangular number on the th row, we will see two more, and get most of the way to a third, by going one more row.


Now let’s do that 6 more times. After traveling 6 rows past a triangular number, we will meet about  more triangular numbers. But


which is very close to 17. So after traveling the Ulam Spiral for 6 rows, we will just about hit 17 triangular numbers, which will be more or less evenly spaced from each other.


What this means is that we should expect to see a spiral with 17 arms, but that when the picture is enlarged to include a very large number of rows, we will see the spiral shifting very slightly to the other direction.


By the way, I didn’t figure this out immediately. First I had a most delightful time understanding when, exactly, square numbers and triangular numbers coincide. In other words, I wanted to understand when there is a  and an  so that:


or


I might write this up in another post, but play around with it for a while if you get bored on the subway.
