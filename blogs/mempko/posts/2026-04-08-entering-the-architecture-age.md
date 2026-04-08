---
title: "Entering The Architecture Age"
date: 2026-04-08
url: https://blog.mempko.com/entering-the-architecture-age/
word_count: 1166
---


![Entering The Architecture Age](https://blog.mempko.com/content/images/2026/04/gooser-2.jpg)


Software development over the last 60+ years has been the equivalent of pyramid building. We see the great pyramids today and marvel at their scale, but their shape is a necessary shape because the people at that time had not yet discovered architecture. Architecture is about making previously unseen structures using as little material as possible. Software so far has been about layers of abstractions. We have microcode, assembly, kernels, human-readable programming languages, operating systems, userland tools, libraries, frameworks, and applications. If software has a geometry (and there is a mathematical argument I can make that it does, but that's beyond the scope of this article), it's shaped today like a pyramid.


The frontier LLMs have gotten so good at building on top of this pyramid that people are now creating applications as one person that would have taken a team of 100 people ten years ago. But ultimately LLMs are just building on top of this pyramid, and are integrating inside applications, but their usefulness is about utilizing everything below them on this giant software pyramid.


OpenClaw has become very popular and it's powerful. People are using it to automate their lives. But OpenClaw's success isn't about creating a new software architecture. Its success is the confluence of tools built on this software pyramid that finally came together. OpenClaw's usefulness does not stand alone; it requires Skills (which are just calling tools). Those tools are just programs on this pyramid. Agents share a memory (markdown files) and wake up via a cron-like mechanism. These are just old ideas that currently exist in every machine today. If you have used Unix, you understand the power of small tools working together to build something more complex. Everyone uses Unix today via their phones, where iOS and Android are built on top of it.


So if anyone can build sophisticated applications and can now keep stacking on top of this pyramid, then how can the next company building software today create a competitive edge? My prediction is that if we keep building on top of this pyramid, then the edge must come from complexity.


Jamie Zawinski, one of the original Netscape engineers, coined what became known as the Law of Software Envelopment: "Every program attempts to expand until it can read mail. Those programs which cannot so expand are replaced by ones which can." The new version of this is that software grows in complexity until its components can't fit inside an LLM context window. I call this The Window Tax.


But I would argue maybe there is another way to be competitive. Maybe we should abandon the pyramid. Maybe we should discover architecture. With LLMs we have the ability now to start from a new foundation and quickly build a competitive system without the baggage of today's software. Something that is much smaller, more efficient, and far more capable.


I have always loved object-oriented systems like Smalltalk and Erlang. The core idea in these systems is that you have objects (which are little computers) that can receive and send messages. Alan Kay, who created Smalltalk at Xerox PARC in the early 1970s, was inspired by biology. Complex life on this planet is made out of cells. Cells are like little computers and communicate with each other via chemical message passing. Each cell has its own internal state, responds to signals from its environment, and can send signals to other cells. Crucially, cells don't communicate through a central specification document. A white blood cell encountering a pathogen doesn't look up an API. It reads chemical signals on the cell surface and responds. This core idea is what inspired Smalltalk. Kay later said that "the big idea is messaging," not objects or classes. And we know a system like this can scale. The human body is made up of trillions of cells all talking with each other. The internet is another object-oriented system. It's a bunch of computers sending messages to each other. We know this scales because it's the largest system we have ever built. It has an estimated 30 billion connected nodes all talking with each other. Since the internet started, all the atoms in the system have been replaced, but it has never shut down. This is the power of great architecture.


If we had the ability to create the next computing system that can span the globe, what would it look like? I thought to myself, now that we have LLMs, they are great at handling ambiguity. One problem with the internet (the biggest object-oriented system) is that we have to painstakingly create these objects, define which messages they handle, and specify which ones they send. This problem isn't new. CORBA in the 1990s, SOAP and WSDL in the 2000s, and later protocols like UPnP all tried to make services self-describing so they could discover and talk to each other dynamically. They all collapsed under the weight of rigid schemas, verbose XML contracts, and version incompatibilities.


So I asked myself, what if you could "ask" the object, how should I communicate with you? What do you do, and how would I accomplish some task with you? That's when the answer came to me: we can have all objects implement a very simple message handler called "ask" where you can query it in plain English (or whatever language) and it replies. And since LLMs are actually very good at generating code in the small, an LLM can take the response and generate an object that could communicate with that same object. Natural language succeeds where schemas failed because it is inherently flexible. An LLM can handle ambiguity, paraphrase, and partial information in a way that WSDL negotiation never could.


I call it the [Ask Protocol](https://abject.world/ask-protocol/?ref=blog.mempko.com).


Here's a concrete example. Imagine you have an object that manages a calendar and another that manages email. The email object receives a message about a dinner invitation for Friday at 7pm. It doesn't have a hardcoded integration with the calendar object. Instead, it sends an "ask" message: "I have a dinner invitation for Friday at 7pm, can you help me with this?" The calendar object responds describing how it handles scheduling. The LLM generates the glue code on the fly, and the event gets created. No API documentation, no SDK, no integration sprint. Two objects that have never seen each other before, cooperating through natural language negotiation. Just like cells reading chemical signals on each other's surfaces.


I started building a system called [Abject](https://abject.world/?ref=blog.mempko.com) (which stands for AI Object) that implements this concept. The whole system is built as a bunch of objects communicating with each other (Smalltalk or Erlang style) where each object has this "ask" handler.


I'm not sure if this is the future of computing architecture. What I do know is that object-oriented systems scale and have created trillions of dollars in wealth (the internet). We now have the ability to create objects quickly via LLMs. All you have to do is ask.
