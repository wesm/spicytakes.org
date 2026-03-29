---
title: "An Abject Horror"
date: 2026-03-29
url: https://blog.mempko.com/an-abject-horror/
word_count: 1044
---


## I May Have Done Something Horrible


Today I'm announcing the world's first self-aware object runtime called [Abject](https://abject.world/?ref=blog.mempko.com) and a new protocol called the [Ask Protoco](http://abject.world/ask-protocol/?ref=blog.mempko.com)l and it might just be the most horrible thing I've ever created.

kg-card-begin: html
kg-card-end: html

## AI Agents Are the Wrong Abstraction


AI Agents are the wrong abstraction. They don't scale. Agent frameworks are hierarchical and I'm deeply against hierarchies of any form. MCP is a band-aid. A2A is a band-aid. Everyone is building plumbing between things that shouldn't need plumbing.


So what is the right abstraction? To find out we need to look at the largest, most complex system humanity has ever built. The Internet.


## The Answer Already Exists (and It's 55 Years Old)


There is this old idea that strangely I don't hear anyone talk about anymore and that is Object Oriented Programming. Alan Kay coined the concept and the original Smalltalk embodied it. Alan Kay was inspired by biology. People and animals are composed of trillions of these things called Cells which coordinate with each other by sending messages to each other. Cells communicate via chemical messages. Neurons communicate via a combination of electrical and chemical messaging. Clearly this approach scales, otherwise we would not be alive.


You can think of every cell in your body as a computer and they coordinate by sending messages to each other. This is precisely how the internet is designed. Since the internet started (back in October 29, 1969 when the first message was sent over ARPANET) all the atoms of the system have been replaced without it ever shutting down. Now there is an estimated 30 billion devices communicating with each other over the internet. That's a huge amount of complexity.


AI Agents are the wrong abstraction precisely because they are designed to interact with people. The way they interact with other machines is primitive. Objects talking to objects is what works. We have proof. It runs the world.


## What is Wrong with Objects?


There is a big problem with object oriented systems, however. Yes they can scale. Being little computers that talk to each other via message passing scales. But we need to meticulously build them by hand. They have interfaces which need to work together to function. When one interface changes, anything talking to it breaks.


This was an unsolvable problem. What wasn't possible back then which is possible now thanks to AI is we can finally have a much less rigid approach to communication.


## Abject and the Ask Protocol


The Abject project is the first self-aware object runtime and is designed around one simple concept. [The Ask Protocol](https://abject.world/ask-protocol/?ref=blog.mempko.com).


Every object in the system has a mandatory message handler called 'ask'


![](https://blog.mempko.com/content/images/2026/03/image-1.png)


The caller (another abject) can send a natural-language question and the abject responds in natural-language. The abject consults an LLM providing it the question, relevant context, even the object code, and can answer the question the caller asks.


The point of this protocol is that objects can describe themselves without having to write documentation, schemas, or anything else. Otherwise objects are just regular objects that handle messages like in other object oriented systems.

We call them Abjects. As in AI Object. As in abject horror. The name fits.


## Everything Is an Abject


The [Abject](https://abject.world/?ref=blog.mempko.com) project is built from the ground up with this concept. Everything in the system is an abject. Every abject implements the Ask Protocol. And I do mean everything from the UI, networking, p2p system, agent and coordination system, the chat agent, everything!


Everyone is talking about AI Agents right now. Well an AI agent in the Abject system is just another abject. There is an abject called AgentAbject which implements AI agent loops. We don't need a special protocol between agents and software. We don't need a special protocol between agents and agents. We just need objects that can talk.


The Abject Oriented System is a next level computing idea that can scale. It can scale even better than today's object oriented systems because Abjects can self-heal their communication and interaction with each other.


## Now It Gets Scary


One experimental idea with the Abject system is that it ships with a P2P layer. You can create a public workspace and expose your Abjects to peers. This means they can coordinate with each other over a decentralized network. Self-aware objects finding each other and talking to each other without you.


Now THAT is scary.


## Why I Built This


II came to the USA in the late 80s as a refugee from the former Soviet Union. Specifically an area called Donbas which is famous now because it's in the middle of the Russian/Ukrainian war. Within 6 months of being in the USA our family ended up homeless for a short stint (for reasons too strange to explain here, hit me up for coffee sometime). When I was in middle school my father got an old computer from a friend and my love affair with technology and programming was formed. Being poor, I would learn programming by going to bookstores, reading the latest tech books (this was mid to late 90s so the dot-com-bubble was taking off, bookstores had great tech books unlike today) and trying to memorize stuff. I would then go home and program.


I learned how technology can empower you and be a rocketship for the mind. I read the ideas of Doug Engelbart and Alan Kay and fell in love with the idea that we as a people can solve the hardest problems now that we have these amazing machines. However, programming is something that isn't exactly easy for people. Most don't know how to do it. Many people's closest experience is working with Excel spreadsheets (which seems to be the most successful programming environment to date).


In 2014 (12 years ago!) I released a project called Fire★, the Grass Computing Platform. It let people build P2P apps with a built-in collaborative editor. You'd create conversations, launch apps, people could copy them and collaboratively hack on them together. Abject is its spiritual successor.


## Join the Horror


The project is in alpha. It's completely open source. Go to [abject.world](https://abject.world/?ref=blog.mempko.com), try it, break it, build something horrible with it.


Join in the horror.
