---
title: "A programmer's view of the Universe, part 2:  Mario Kart"
date: 2008-12-27
url: https://steve-yegge.blogspot.com/2008/12/programmers-view-of-universe-part-2.html
word_count: 4511
---

This is the second installment of a little series of discussions.  They're not much more than that, just discussions.  And I hope I'm
*inviting*
discussion rather than quenching it.  But I'll be honest — the goal of this series is to pound a stake through the heart of a certain way of thinking about the world that has become quite popular.  If my series fails in that regard, I hope it may still provide some entertainment value.
Part one,
[The fish](http://steve-yegge.blogspot.com/2008/10/programmers-view-of-universe-part-1.html)
, was about a twisty line and a fish's examination of it. Today we move to a twisty plane.
**Embedded Systems**
There are many kinds of computer programs, and many ways to categorize them.  One of the broadest and most interesting program categories is
*embedded systems*
.  These systems are the centerpiece of today's little chat.
Embedded systems are a bit tricky to define because they come in so many shapes and sizes.  Loosely speaking, an embedded system is a little world of its own: an ecosystem with its own rules and its own behavior.  So an embedded system need not even be a computer program: a fish tank is also a kind of embedded system.
We call them
*embedded*
systems because they exist within the context of a
*host system*
.  The host system provides the machinery that allows the embedded system to exist, and to do whatever it is that the embedded system likes to do.
For fish tanks, the host system is the tank itself, which you may purchase from a pet store.  A tank has walls for holding the water in, filters and pumps for keeping the water clean, lights for keeping the fish and plants alive a little longer, and access holes for putting your hand through to clean the tank.  There's not much to it, really.  The embedded system is everything inside: the water, the plants, the rocks, the fish, and the little treasure chest with bubbles coming out.
For computer games, another popular kind of embedded system, the host system is the computer that runs the game: a PC, a game console, a phone, anything that can make a game exist for a while so that you may play it.
Programmers have been building embedded systems for many decades: a whole lifetime now.  It is a well-studied, well-understood, well-engineered subject.  Gamers understand many of the core principles intuitively; programmers, even more so.  But in order to apply all that knowledge
*outside*
the domain of embedded systems, we will need some new names for the core ideas.
The most important name is the One-Way Wall.  I do not have a better name for it.  It is the most important concept in embedded systems.  In lieu of a good name, I will explain it to you, and then the name will stand for the thing you now understand.  It's the best I could come up with.
But first let's dive into an embedded system and see what this wall looks like from the inside.
**Mario Kart**
I will assume you've played
, or you've at least watched someone else play it.  Mario Kart is the ultimate racing game in terms of sacrificing realism for fun.  It bears so little resemblance to reality that it's a wonder it tickles our senses at all.  The Karts skid around with impossible coefficients of friction, righting themselves from any wrong position, and generally making a mockery of the last four centuries of advances in physics.
It's really fun.
Mario Kart, like all games, has a boundary around the edge of the playing area.  In Mario Kart you bump into it more often than in most other games, which is part of the reason I chose it to be our Eponymous Hero.  If you want to win a race, you will need to become quite good at accelerating around corners, which means you will spend a fair amount of time bumping up against an invisible wall.
You know the wall I'm talking about, right?  It's invisible, so you can see right past it to the terrain beyond.  But the wall is there, and you are not permitted to venture beyond it.
In slower-paced games, when you arrive at the invisible map boundary, you will sometimes be told by the game: "You can't go that way.  Turn back!"  And since that is your only option, you comply.  These invisible boundaries are non-negotiable.
In other games, you may stop on contact with the boundary, or perhaps bounce off.  But the boundary is always there.
Imagine Mario and Luigi chatting about the you-can't-go-that-way wall.  Their conversation might go something like this:
**Mario:**
"Luigi, my brother!"
**Luigi:**
"Maaaarioooooo!"
**Mario:**
"Yes, Luigi.  I am a here.  Tell me my brother, why is it that every a time I a spin around the cactus in the third a bend of the Desert a Track, I get a stuck and have to start accelerating from nooooothing?"
**Luigi:**
"Whaaaaa?"
**Mario:**
"Brother, the Desert a Track!  It's Number a Three!  You know the big a bend, where you have to slow down?  I am always a forgetting to slow, and I just a stop.  Just a like that!"
**Luigi:**
"I don't know, Brother.  That Bowser, he is always a squishing me right before I hit that turn, and I am a flat like a pan a cake for a looooong a time."
**Mario:**
"What about that a time two races ago, where Wario hit you and you a spun around and you a headed for the hill, and you got a stuck and wailed for me?"
**Luigi:**
"Ah, that Wario!  I will get him next a time!"
**Mario:**
"Why did you not just turn around then?"
**Luigi:**
"My Kart, it did not a move, no matter how I wailed."
**Mario:**
"That is a what I am a speaking of, Brother.  Your Kart moves in all other places, but if you head for the hills, it just a stops a suddenly!"
**Luigi:**
"I a
*hate*
a stopping a suddenly."
**Mario:**
"Yes, Brother.  So do I.  But why can we not traverse that a part of the hill?  What is on the other a side?"
**Luigi:**
"I think it is Track 4, Brother.  They do not want you to wind up in the lake."
**Mario:**
"Whaaaa?  Who is this a 'they'?  And why can we a not see the lake from a Track a 3?  I think there is a nothing there, Brother.  Just a more hills."
**Luigi:**
"No, my brother.  I think it is a Track a 4.  Or maybe Track a 2.  There must be a something there."
**Mario:**
"Perhaps you are a right, my brother.  We should get a back to a racing now.  We can talk a more about a this after the next a race."
**Luigi:**
"Yes, brother.  I will a get that Wario this a time!"
**Well-formed nonsensical questions**
In our Highly Realistic Dialog, Mario is wondering about the Invisible Boundary at the edge of the track.  He asks his brother the seemingly obvious question: "What is on the other side?"
As a gamer, if you pause to consider the question at all, the answer seems to be: "Nothing I care about."  The invisible (or sometimes visible) Boundary seems just like any other wall.  It is designed to keep you in where you're at, or out of where you're not, depending on your point of view.
But the gamer's view is that the boundary
*does*
have another side.  You have no way to get there, but it exists.  For maximum gameplay immersion a game universe needs to appear consistent.  Thus, when you peer through the wall it appears that the other side is just more of the same.
To an embedded systems programmer, Mario's question is complete nonsense, like a fish asking the temperature of the water on the other side of the glass.  There
*is*
no water on the other side, and for that matter a fish can't ask questions, so the question itself is based on nonsense premises.
From a perspective within the Mario Kart universe, the "other side" of the Invisible Boundary is... a kind of nothingness.  The embedded world quite literally
*ends*
at the boundary.  The level designers usually try to make it appear as if the current world continues on, but this is an illusion.  They discontinue the model's polygons beyond the line of sight.  Put another way, the water stops at the edge of the tank.
The nothingness beyond the Invisible Boundary of an embedded system is much deeper and more significant than simply not having objects there.  In that nothingness there is no programmatic substrate upon which to
*place*
objects.  If you were to ask: "What lies between Mario's head and Luigi's head," the answer may well be "nothing", since no game objects may overlap the line between their heads at the particular time you ask the question.  But that "nothing" is qualitatively different from the "nothing" on the other side of the Invisible Boundary.  Between Mario and Luigi there is a
*space*
– a place in their universe where objects and forces and logic apply, even if they are Mario Kart's twisted versions of physics and logic.  That universe ends abruptly at the surface of the boundary.
The question "What's on the other side" is well-formed in a strictly mathematical sense.  You could project a line from Mario to the nearest boundary, and ask the more precise question: "If Mario is at distance D from nearest boundary B, what overlaps the point P obtained by extending the Mario-boundary line L to a distance D beyond B?"  ("Whaaaaa?")
The new formulation of the question is more well-formed, but it is every bit as semantically nonsensical.
**What's really on the other side**
In the context of the Mario Kart universe, the system boundary truly only has on side, and Mario and Luigi are on that side.  From their perspective, we can't meaningfully ask the question "What's on the other side?"  However, there
*is*
a semantically significant interpretation of "the other side" of that invisible boundary.  To get to this better answer we must leave Mario's universe.
From the perspective of an embedded systems programmer, the entire Mario Kart universe is data structures laid out in the memory space of some machine.  There is a program — the game engine — that
*interprets*
the data in a way that makes it appear to be a universe that is similar to ours in various intuitively appealing ways, yet different from our universe in various fun ways.
It is very unlikely that the polygons and other level data are laid out in strictly contiguous order in the host machine's memory space.  It is more likely that they are spread out, with gaps, like dominoes spilled on a tile floor.
The question "What's on the other side?", when viewed from the perspective of a systems programmer, might be phrased more precisely and meaningfully as follows: "What occupies the memory spaces adjacent to the memory used by the Track Three Desert Level?"
This is the same as Mario's question, but we had to step outside the Mario Kart universe in order to ask the question in a way that made sense.  The Mario Kart universe, like most game universes and in fact most embedded systems, is designed to appear
*complete*
.  There is apparently "stuff" beyond the boundary; you just can't go that way.
When we step up into the host system and ask the analogous question about the "other side", both the question and the potential answers become much more complex: many orders of magnitude more complex, in fact.  Fortunately, due to the Mario Kart system being so simple, increasing the complexity still gives us a vaguely accessible problem.
Let's try to cook up an answer to this new, more complex question regarding the contents of the program memory space on the "other side" of the invisible wall.
In terms of atomic program units (say, bits or bytes), the amount of memory used by a game like Mario Kart is actually high enough to defy our sense of scale.  A game with hundreds of megabytes or gigabytes of runtime data has billions of discrete elements, which is too many for us to keep track of individually.  One of the key jobs of a programmer is to organize their code so that the elements can be managed at human-CPU scale: up to seven "things" at a time.  But this organization can't mask the fact that billions of individual elements exist, each with its own role to play in supporting the embedded system.
Hence, even for a game as "simple" as Mario Kart, we're stuck imagining how it works internally.  Even the programmers who built the game have only a dim and incomplete mental model of the game.  It's like building a skyscraper, or a city: you build it a piece at a time, and it's rarely fruitful to try to picture everything inside of it simultaneously.
Anything that goes wrong or is out of place in the program could take days to track down with state of the art tools.  That's just how it is.  We're not able to comprehend large problems all at once; we can only attempt it in small increments.
Bearing this necessarily incomplete understanding in mind, what exactly
*would*
we find in the machine memory between the elements of Mario and Luigi's track mini-universe?
The answer is familiar to programmers and perhaps surprising to non-programmers.  The answer is:
*almost anything*
.  It could be elements of a different program, or random garbage not being interpreted by any program, or supplemental data for the Mario Kart universe, such as language translation strings.  Or Luigi could be right: it could be Track 4, pre-cached for the next race.  Perhaps not exactly the way he's imagining it, but...  close.
**Moving beyond the Wall**
Our little visualization of the host system's memory raises another natural question: what would happen if you "zapped" Luigi's Kart across the boundary?
This question isn't entirely as nonsensical as "what's on the other side?"  With the proper programming tools, you might be able to observe changes in the machine memory as Luigi's Kart moves, and these changes might follow an observable pattern that leads to a relevant prediction of sorts.
As just one possibility, Kart motion might be represented as shifting a Kart memory structure along the sequential indexes of an in-memory array.  This arrangement is unlikely for performance reasons, but it's certainly possible, and should serve to illustrate the point.  If you were to find that moving Luigi's Kart ten meters (in the scale of Luigi's track universe) resulted in a structure motion of 1000 memory addresses, then you might make the reasonable prediction that in another ten meters his representation would move another 1000 addresses.
This might well put him beyond the end of the physical memory array.  In most real-world scenarios this would be a bug, and would result in some sort of nasty response from the machine, such as a game crash.  Or in a more user-friendly environment, the game engine might simply prevent his motion in that direction and move him back into his universe.  This might put his Kart in an uncomfortable position, but it will at least be a
*real*
position according to the logic of the Mario Kart universe.  At least the Kart won't have disappeared.
However, it is
*infinitesimally*
possible that Luigi's Kart could be moved into another physical machine process in the host system — say, another instance of Mario Kart running on a time-sharing operating system or virtual machine — in such a way that Luigi and his cart physically disappear from the old universe (a process address space) and appear in the new universe (another process address space).
Even if this infinitely remote possibility were to occur, chances are high that the sudden appearance of Luigi and his Kart would wreak local or even global havoc in the new universe.  He might get lucky and crush Bowser into a pan-a cake, but more likely he would wind up stuck in a stone wall or a hill, unable to move.  Or even more likely, his Kart's memory structure would be copied into a non-game area, such as the translation string section, and Luigi's sudden mysterious appearance might manifest as nothing more than garbled speech from one of the other characters.
There are many possibilities, too many to imagine.  The most important takeaway here is that no matter how
*unlikely*
Luigi's safe intra-universe migration may be, it is
*possible*
.  With some external help from the host system, it would even be straightforward: perhaps no more than a few days work from a skilled programmer.
In real-world programs sharing adjacent address spaces, it's improbable (but possible!) that migrating data from one process to another in a randomly chosen destination spot would have semantically meaningful results in the destination address space.
To put it in simpler terms: under just the right circumstances, Luigi could teleport to the other side, and wind up in a different world.
**Ghosts in the machine**
An embedded system is a little environment.  My Betta in the previous installment of this little series lived in a very simple embedded system.  Its most obvious difference from my own environment is that the tank was filled with water, while my room was filled with air.  The differences from the host system can yield different behavior and different rules.  In the fish tank, the rules are only a little different — for example, most things are more buoyant inside the tank.  In a virtual embedded system, the rules and behavior might be
*completely*
different from those of the host system.  It all depends on how the embedded system was designed to work.
Every embedded system has a containing surface, which might be called its frontier.  The frontier is
*one-sided*
in the sense that the rules of the embedded system may simply stop at the boundary: there is no "other side".  In some embedded systems (such as a Euclidean space embedded in a non-Euclidean space), even the supposedly intuitive notion of extending a line across the boundary only has meaning on one side, the "inside" of the frontier.
If there is a formal mathematical term for this One-Sided Frontier idea, I've yet to come across it, and I've spent quite some time looking.  If you have any suggestions, let me know.  The closest I could find are the spaces that are undefined in noncontinuous functions, such as the Tangent function for a value of 90 or 270 degrees.  If you ask a question
at these values of
, the answer is something like "You can't go that way."
So the other side of the frontier is
.  This statement has a deep, almost philosophical meaning to programmers.  It does
**not**
mean "nothing"; no, no no!  It means
*anything*
.  It is a modern-day Wand of Wonder, a Bag of Tricks, a Horn of Plenty, a Box of Chocolates.  You never know what you're going to get.
If a computer program's code inadvertently reaches into
, then it has stepped across a mystical wall into another universe, and anything could happen.  It's as if Gremlins have taken over the machine.  Your PC speaker might beep erratically or continuously.  Your video array might burst into random fireworks.  Your printer might fire up and print out mysterious symbols.  Your program may even continue to operate normally, but with the addition of unexplainable and unrepeatable phenomena.
I have seen all these things happen.  All C/C++/assembly programmers have seen bugs like this — program bugs with "crazy" behavior.  The bugs are so spooky, and so hard to track down, that computers are now designed to be gatekeepers at the Wall, and when you try to step across they say STOP!  It's much better to be blocked immediately than to let your program wander into
, where ghosts may take hold of your data in ways that may even cause your legal department to take notice.  Stranger things have happened, as they say.
This computerized gatekeeping is commonly called "protected mode".  The computer checks every addressing instruction, and any time a program tries to access the memory area outside its own, things halt immediately.  When you see the message "segmentation fault", or a blue screen of death, or some other sign that a fatal, unrecoverable program error has occurred, it is almost always because someone or something in the embedded system tried to escape.
**Holes in the Wall**
From the perspective of a computer game, the system frontier is relatively uninteresting.  It's not much different from any other obstacle.
However, in other embedded systems these frontiers are almost mystical in nature.  They provide endless fascination for computer scientists working in the domain of
*programming languages*
, which are yet another kind of embedded system.
To see how it works, let's consider the situation in Mario Kart, which is simpler.
In Mario Kart, most of the racers are computerized opponents, or AIs.  A few of them, usually at least one, are controlled by people, using steering wheels or other physical controllers.  Sometimes (e.g. in simulation mode) all the opponents may be computerized.
In order for people to interact with the embedded system, there must be some way to send information back and forth across the system frontier.
Coming from the Mario Kart side, we typically have video and sound signals.  The embedded system generates these signals and sends them to your TV or device.
Coming from the people side, we typically have motion input: which way to move the Karts.  The signals begin as your physical motions: buttons you press, or in newer controllers, the direction you tilt the controller.  They are sent from the host system to the embedded system and they generally produce observable effects in the embedded system.  Like magic!
Mario Kart is especially interesting because the external camera is physically present within the game.  You can see it in the instant replays of your races: a little guy with a camera, floating behind you on a little cloud.  The game designers have arranged things so that you can almost never see him while racing, because he's always flying behind your head, along your line of sight.
But he's there.  And in fact that camera is
*always*
there, in all video games.  It's just that the Mario Kart designers have chosen to reify him as a cute little turtle guy with a camera, floating behind you on a cloud.
The external camera is a one-way hole in our one-way wall: it sends data
*out*
of the embedded system.  For all intents and purposes it also sends the sound data, since the sounds are usually scaled as a function of distance from the camera.
During a race, there's a lot of stuff going on in the embedded system, and there's a lot of stuff going on in the host system.  But they constrain their communication via mostly-invisible channels, and these channels are restricted in the kinds of communication they may convey.  Your controller can send motion inputs, but (at least today) it can't send video data.  And (at least today) the characters in the game can't control your arms and legs, the way you can control theirs.
Hopefully now you should have a mental picture of this magical wall between an embedded system and the Great Undefined Beyond on the "other side" of its system frontier.  The wall may have deliberate holes in it: channels, really.  Information may flow across these channels in predefined ways.  And the channels are almost always invisible to occupants of the embedded system.
**Reflections**
I've spent a lot of effort telling you about a rather strange, twisty kind of surface: the frontier of an embedded system.  This frontier exists for all embedded systems.  It may have "holes" (data channels) in it.  The number and nature of these channels is entirely up to the designers of the embedded system.  Programmers sometimes call these channels "reflection" or "metaprogramming".
The holes in the frontier may or may not be detectable within the embedded system itself.  They may only be detectable within the host system. This, again, is up to the designers.  For most of the embedded systems I know of, the channels are "well defined", in the form of application programming interfaces offered to either the embedded system or the host system for communicating across the frontier.
But you need a channel for this kind of communication.  Setting it up is usually not cheap.  And setting up meta-reflection (in other words, being able to "see" the channel from within the embedded system or host system) is even more work.
So most of the time, channels through the embedded system frontier are completely invisible and undetectable from inside the embedded system.  They're quite real, and information flows either one way or both ways, but they
*cannot*
be detected from within the embedded system, and their behavior is intrinsically non-repeatable via experimentation.
When data comes across these invisible channels, stuff "just happens" in the embedded system, with no clear indicator nor explanation as to why.
In our discussion so far, I have intentionally blurred the distinction between the host system (such as a fish tank or a game console device) and the host system's host system (such as your bedroom or living room).  But you've probably noticed by now that
*all*
host systems are embedded in some larger system.  This is just the way things work.  The fish tank is in your bedroom, which is a system embedded in a house, which is a system embedded in a neighborhood, embedded in a county, a nation, a continent, a planet, a solar system, a galaxy, a universe.
It's perhaps not as clear in the case of fish tanks, but host systems often overlap and even cooperate.  A city is composed of many interleaved subsystems.  So is your body.  It's not always a simple containment relationship.  Systems are made of, and communicate with, other systems.
But one way or another,
*all*
systems are embedded systems.
There is no reason to assume that our Universe works any differently.  Our Universe is a system; that much should be self-evident.  It has boundaries; astronomers and astrophysicists have recently even determined that the boundary appears to be a dodecahedron.
We are already painfully aware of the question "what happened before the Big Bang, if in fact the Big Bang occurred in the way all the evidence suggests", and its inherent nonsensicality.  What happened before the beginning of Time?  What lies beyond the end of the Universe?
Programmers already know intuitively the answer to these questions.  The answer is:
is there.
*Undefined*
is
**not**
the same as "nothing", no indeed.  It's
*anything*
.  And we can't go that way.
This has ramifications for the way we think about things today.
I believe I will have more to say about this soon.  Right now I think I will go play Mario Kart: a game as fun as any I think I've ever played.