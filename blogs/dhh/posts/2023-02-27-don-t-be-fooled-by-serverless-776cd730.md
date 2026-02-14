---
title: "Don't be fooled by serverless"
date: 2023-02-27
url: https://world.hey.com/dhh/don-t-be-fooled-by-serverless-776cd730
slug: don-t-be-fooled-by-serverless-776cd730
word_count: 554
---

Cloud aficionados love pinning the true promise of the cloud on serverless functions and services. Not getting the savings you thought you would with the cloud? It's because you didn't go serverless. Frustrated with the complexity of the cloud? Serverless! Performance questions? SERVERLESS! Serverless has become a mantra to chant because it's still appears just magic enough that most people won't question the fundamentals. But you should.
Let's start at the beginning. Clouds, and VPS's before that, work on the age-old principle of buying in bulk and selling by the piece. You run one big server for $1,000/month, then you rent it out to seven people for $200/month, and voila, you've cleared a $400/month profit.
That actually works well for all parties, if the seven customers aren't too taxing on the equipment or if they tax it at different times. The customers get to skip the capital outlay for the server plus get the compute they require, when they require it. This is the ideal cloud scenario.
But what happens if a customer needs the performance of a whole box, most of the time? Then they're paying $1,400/month for $1,000's worth of computing. Or maybe, because they're reserving the whole box, they'll get a deal at $1,250/month by committing to a whole year. That deal is far less obviously good on both sides. It's basically a credit agreement at a 25% APR. Tread wisely!
Enter serverless. It's the same financial mechanics as above, but you can slice the server far more thinly. Instead of renting out your one big server to seven customers at $200/month, you rent out individual function executions to 100 customers at $20/month. This now clears $1,000/month in profit instead of just $400/month. No wonder cloud providers love serverless!
Again, if you only need a few functions executed every now and then, this works out for you as a customer too (at least in the short term). But if you execute enough functions to fill the computing power of a whole box, it's a terrible deal. Not just because you'll be paying more for the same clock cycles, but also because the lock-in is immense.
The further down the rabbit hole you go with "cloud-native" services in serverless, the harder it'll be to climb out when you realize that you should own the donkey rather than rent it. And especially once you realize that paying to rent a whole donkey at the piece price of a hundred slices is an even worse deal than just renting the whole donkey by itself!
Don't be fooled by serverless. There's no magic that can change the fundamental fact that if you need all the computing cycles of a computer, you ought to own that computer. And if you start off with a proprietary serverless setup, you might well find the lock-in impossible to escape by the time the rental math no longer works.
The cloud is primarily for companies that have big swings in use – like Amazon's original AWS case of huge demand around Black Friday and Christmas, which left them with unused capacity for the rest of the year – or for early outfits that don't do enough business to either warrant owning a whole computer or spend so little on the cloud that it just doesn't matter. Serverless doesn't change that.
