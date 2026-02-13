---
title: "So, how’s that retirement thing going, anyway?"
date: 2019-12-05
url: https://www.joelonsoftware.com/2019/12/05/so-hows-that-retirement-thing-going-anyway/
word_count: 789
---


For the last couple of months, Prashanth Chandrasekar has been getting settled in as the [new CEO of Stack Overflow](https://www.joelonsoftware.com/2019/09/24/announcing-stack-overflows-new-ceo/). I’m still going on some customer calls and have a weekly meeting with him, but I have freed up a lot of time. I’m also really enjoying discovering just how little I knew about running medium-sized companies, as I watch Prashanth rearrange everything—for the better. It’s really satisfying to realize that the best possible outcome for me is if he proves what a bad CEO I was by doing a much better job running the company.


Even though I live in Manhattan’s premier NORC (“Naturally Occurring Retirement Community,”) I’m thinking of this time as a [sabbatical](https://www.joelonsoftware.com/2000/03/18/more-on-sabbaticals/), not retirement. And in fact I’m really, really busy, and, in the interest of deflecting a million questions about what I’m doing nowadays, thought I’d update my long-suffering readers here.


![](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2019/12/IMG_9590-scaled.jpg?fit=730%2C548&ssl=1)

*This adorable little fella, Cooper, is two. If your web app needs a mascot, apply within.*


I’m chairman of three companies. You probably know all about Stack Overflow so I’ll skip ahead.


Fog Creek Software has been renamed [Glitch](https://glitch.com/), “the friendly community for building the web.” Under CEO [Anil Dash](http://anildash.com/), they have grown to [millions of apps](https://www.theverge.com/2019/7/9/20683018/glitch-2-5-million-apps-code-remix-anil-dash) and raised a decent [round of money](https://glitch.com/culture/glitch-raises-30m-series-a-round-from-tiger-global/) to accelerate that growth. I think that in every era there has to be some kind of simplified programming environment for the quiet majority of developers who don’t need fancy administration features for their code, like git branches or multistep deployment processes; they just want to write code and have it run. Glitch is aimed at those developers.


The third company, [HASH](https://hash.ai/), is still kind of under the radar right now, although today they put a whole bunch of words up on their website so I guess I can give you a preview. HASH is building an open source platform for doing simulations. It’s a great way to model problems where you have some idea of how every agent is supposed to behave, but you don’t really know what all that is going to add up to.


For example, suppose you’re a city planner and you want to model traffic so that you can make a case for a new bus line. You can, sort of, pretend that every bus takes 50 cars off the road, but that’s not going to work unless you can find 50 commuters who will all decide to take your new bus line… and the way they decide is that they check if the bus is actually going to save them time and money over just driving. This is a case where you can actually simulate the behavior of every “agent” in your model, like [Cities: Skylines](https://en.wikipedia.org/wiki/City-building_game) does, and figure out the results. Then you can try thousands or millions of different potential bus routes and see which ones actually reduce traffic.


This kind of modeling is incredibly computationally intensive, but it works even when you don’t have a closed-form formula for how bus lines impact traffic, or, in general, how individual agents’ behavior affects overall outcomes. This kind of tool will be incredibly useful in far-ranging problems, like epidemiology, econometrics, urban planning, finance, political science, and a lot of other areas which are not really amenable to closed-form modeling or common “AI” techniques. (I love putting AI in “scare” “quotes”. There are a lot of startups out there trying to train machine learning models with way too little data. Sometimes the models they create just reproduce the bad decision making of the humans they are trained on. In many cases a model with simulated agents running a white box algorithm is going to be superior).


Ok, so those are the three companies I’m still working on in some way or another. That still leaves me with a couple of free days every week which I’m actually using to work on some electronics projects.


![](https://i1.wp.com/www.joelonsoftware.com/wp-content/uploads/2019/12/IMG_7374-scaled.jpg?fit=730%2C236&ssl=1)


In particular, I’m really into pixel-addressable RGB LEDs, like those WS2812b and APA102-type things. Right now I’m [working](https://blinkylights.blog/) on designing a circuit board that connects a Teensy 3.2 controller, which can drive up to 4416 LEDs at a high frame rate, to a WizNET Ethernet adapter, and then creating some software which can be used to distribute 4416 pixels worth of data to each Teensy over a TCP-IP network in hopes of creating huge installations with hundreds of thousands of pixels. If that made any sense at all, you’re probably already a member of the [LEDs ARE AWESOME](https://www.facebook.com/groups/LEDSAREAWESOME/) Facebook group and you probably think I’m dumb. If that doesn’t make any sense, rest assured that I am probably not going to burn down the apartment because I am very careful with the soldering iron almost every time.


![](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2019/12/img_7185-scaled.jpg?resize=730%2C548&ssl=1)
