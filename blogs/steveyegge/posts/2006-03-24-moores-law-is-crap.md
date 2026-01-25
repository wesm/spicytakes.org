---
title: "Moore's Law is Crap"
date: 2006-03-24
url: https://steve-yegge.blogspot.com/2006/03/moores-law-is-crap.html
word_count: 3235
---

Sometimes people ask me how I find time to go learn new stuff.  Here's the answer: you make time.
Nobody ever likes that kind of answer, but we all know it's the real one.
My brother Dave put on some pretty serious weight after he graduated from high school.  He'd gone from playing varsity football to working two jobs
*and*
going to college full time.  It didn't help that one of his jobs was pizza delivery, and the other was waiting tables.  Soon he was a fat, fat kid.  Went from a buck-eighty to a deuce and a half, at least, maybe a deuce sixty.
One day he saw a truck with a bumper sticker on it that said: "Lose weight now, ask me how!"  So he pulled up next to the truck at the next stoplight, and said to the two cowboy-types in it: "How do I lose weight?"  They yelled back: "Just lose weight, ya fat pig!  Haw haw haw HAW HAW HAW HAW!" and then drove off.
Dave was sad about this advice for a brief while, but eventually he brightened up, because he did know how to lose weight.  Cripes, he'd been a champion varsity football player two years prior.  It's not like there's any magic to it.  He went and bought a mountain bike, started riding the crap out of it, joined a gym, watched what he ate, and lost about 85 pounds over the next year.
I was 145 pounds 2 years ago today, after a similar 2-year diet and exercise kick that took me down from a deuce and a half myself.  Then I fell off the wagon — it happens — and put on 50 pounds over the next 2 years.  It sucks, but there's no magic.  Two months ago I finally started going to the gym every day, 7 days a week, and my legs are sore every day.  My weight hasn't improved at all yet.  But it will.  You just have to work at these things consistently.
But you knew that, didn't you?
This isn't a self-help blog, by the way.  I'm not in that business.  I'm not here to help, since I don't actually know the answers.  I'm just here to rant, and pose occasional questions.  It's what I do, when I'm not doing other stuff.
I don't know why I blog.  I'm just compelled; it just happens whether I like it or not.  Don't read too much into my blogs.  My opinions change from day to day.  The only things I've learned, the only universal constants, are that I don't know very much, and that public whale explosions are just about the funniest thing human beings can experience during our stay on Earth.  I don't know why that is, either.
Today's blog is truly a rant; I just need to get this particular one off my chest, so my gym partner Todd can listen to me rant about something different next week.
**The Big Choice**
We all have to choose how to spend the time we're given.
If you don't choose, it just slips right by you.  I know.  On a trip to Vegas not too long ago, I made a pit stop in a casino restroom, and as I was washing my hands, there was this older guy there, also washing his hands.  On a whim, I asked, "Hey man, how old are you?"
His reply?  "Seventy-two! I have a son: I remember the day he was born like it was yesterday! I was holding him just like so.  Well, guess what, he turned 40 years old just last week!  It goes by in a flash!  Before long, you'll be lookin' at THIS!"  He pointed at his wrinkled mug, and concluded his monologue with: "Haw, haw, haw!  HAW HAW HAW *cough* *cough* HAW *cough* *hack* HAW HAW HAW HAW HAW!" and walked out.  I think I made his day, although I can't exactly say he made mine.
When you graduate from college (or high school, for that matter), you have a simple choice facing you.  You can either keep learning, or you can stop.
There is an almost unbelievably easy heuristic for knowing whether you're learning.  It goes like this: no pain, no gain.  Learning is hard.  If it's easy, then you're coasting; you're not making yourself better at something fundamentally new that you couldn't do before.
In other words, it's just like working out.  You've gotta mix it up.  If you're sore every day, then you're getting good workouts (assuming you can tell the difference between "good" soreness and "injury" soreness; if you're not sure, go ask a professional.)
When you do study, there's a lot of appeal to studying what you already know, because it's less painful.  And of course to become an expert at any field, you have to focus on it pretty hard for a long time.  But cross-training is well established in sports; you don't typically become a world-class baseball player by just playing baseball all the time.  You have to do other kinds of workouts and exercises to maximize your strength, agility and endurance gains.
Cross-training improves you every bit as rapidly in other disciplines.  That includes programming.  If you're cranking out code as easily as breathing, then if you're getting better at all, it's so gradual that you'd never notice it happening.  You won't have great insights until you get new perspectives from working hard, even if only occasionally, at stuff
*other*
than what you already know.
Being in school full-time is an amazing luxury, one that's hard to appreciate when you're actually there, because learning is painful.  But trust me on this one: it's even more painful when all you have is scraps of time here and there.
While you're in school, assuming you make a reasonable effort at applying yourself once in a while, you learn a fantastic amount, and you learn it at a fantastic rate.  Later you'll learn at a slower rate; it's pretty much guaranteed.  Non-educational activities will inevitably intrude and consume the majority of your time.
Hence the choice.  After you graduate, you can either learn a little, or not at all.
If you're in the "not at all" camp, well you've made your choice, and I respect it.  You'll probably be happier than I am.  I'm tormented by how slowly I have to move as a programmer.  I now believe programming languages have failed.  All of them.  The programming world is a giant body shop, and we're building huge pyramids with millions of years of hard labor.  I believe that stuff should be easier than it is, and it pisses me off that most people are so content with the state of the art, because it means they're not helping make it better.
To me, mainstream languages have failed because they're still fundamentally serial, fundamentally early von Neumann, fundamentally single-box languages.  They're all vying for the position of "least crappy", and the current winner (whether it's Python, Ruby, Lisp, name your favorite) is just that:  the least crappy.  Because they're all focused on finding more elegant ways to express mostly-serial computations for crap computers.  That, or faking parallelism poorly with threads, if the language supports them at all.
Sure, there have been some interesting attempts at parallel languages.
[Erlang](http://www.erlang.org)
is one of the better-known ones, and it's actually quite cool.  But Erlang has failed too, because
*you*
haven't heard of it.
**Programming's Biggest Problem**
Our industry is in a seriously ugly position, right now, as we speak.  Most of the hardware designers are focused on keeping Moore's Law going, because that's where the money is.  They want that doubling every 18 months.  Today it's probably quite within our reach to get 10x every 18 months, if we'd agree to focus on parallelism (in the massively distributed computing sense.)
But programmers like XML, to the point of focusing on it to an unhealthy extent.  Same with C++.  And Java.  They like these things because they work, and because they like to minimize the amount of crap they have to learn.  Because learning is painful.  Remember?  You might think I've gone way off track, off the deep end, even, but this
*is*
the same thread.
Let's face it: a parallel language will have to be radically different if it's to break free of the von Neumann Turing-machine rat race we're in.  If we move to cellular automata, or in fact any other parallel computational model that's resilient to node failures, then we'll need a new language, because the current serial languages will perform badly, or be horribly hard to manage, or both.
Cell or grid (or whatever) parallel computing will have a radically different internal economy.  It'll need new data structures, new algorithms, new instruction sets, new everything.  You
*do*
realize that John von Neumann was an economist, right?  Among (many) other things, he was an economist, and it influenced the design of his first computer, that one right there on your desk.
The computing machine JvN built was created in an environment very similar to the one in the movie Apollo 13, where the folks at Houston had to build a carbon-dioxide remover out of exactly the free junk available on the spacecraft, and then explain it to the crew so they could build their own copy of it.
Johnny went out collected a bunch of engineers: materials engineers, electrical engineers, mechanical engineers, everyone who had some spare junk.  They came up with a design for a computation machine that just barely sufficed, one that could be built out of the crap they had available at the time: vacuum tubes, magnetic drums, wire, duct tape.
As he was creating this thing, Johnny was focusing on what he was calling the "internal economy" of the resulting machine.  Secondary storage accesses were painfully slow.  Memory accesses were faster.  Register accesses were very fast.  And so on.  So he designed representations, data structures, and algorithms that were appropriate for that particular machine, the one he was building from spare parts.
If he'd made the machine out of Brazilian rainforest army ants, or mechanical gears, or falling dominoes with marionettes to pick them up again, his data structures and algorithms would have been very, very different.  There are some commonalities, sure — you need numbers, and arithmetic, and functions, and data storage, and sorting, and so on.  But what's most efficient for army ant computers isn't going to be most efficient for vacuum tube computers.
You
*do*
realize you can make a computing machine out of just about anything, right?  And they don't all have to work like Turing machines do.  Turing was one of the greatest geniuses of the century, but he'd have been the first person to tell you that there are infinitely many machine designs capable of the same computations.  His was just one model, and his professor's (which led to Lisp) was just one other model.  But who's to say they're the best models?
Some computing machines are more efficient at certain computations than others.  Some are more practical to build than others.  Some are faster than others.  Some are more robust, or more inherently parallel.
You
*do*
realize that your brain is such a machine, right?  And that it's 100,000 times faster than today's computers at pattern-matching tasks, because while JvN's machine operates serially, your neurons can all fire independently.
Let me give you a hint: your brain's operating system isn't written in C++.
Is our industry ever going to get out of this amazing backwater of a gridlock, this evolutionary dead-end we're in, where we programmers act like army ants, churning out loops and SOAP calls and UML diagrams as if we're weaving cloth with the very fabric of the computational universe?
If it ever happens, and by God I hope to witness it in my lifetime, then the computers and languages and data structures and algorithms are all going to have to change simultaneously.  Because a language optimized for a serial computer will perform like crap along
*some*
important dimension of performance, probably more than one.  But we can't switch wholesale to parallel languages either, because they'll perform like crap on today's computers: again, for some value of "perform" that's not worth discussing here, but it'll be some form of either computer-performance or people-performance.
And programmers are nothing if not fanatically obsessed with performance.  Kinda ironic, huh?
Half the irony stems from knowing that there are far more productive languages out there than the ones most of us are using.  But most of them perform poorly on our hardware, because these languages are targeting meta-virtual machines, typically "defined" (informally) by the capabilities of the language itself. And if you're not targeting exactly the hardware you're on, the impedance mismatch will slow the language down.
That's the problem with most JVM languages other than Java: they need
*hardware*
(think ants!  anything can be hardware!) to support operations like long-jumps and tail-call optimization, but the JVM doesn't export those facilities as part of its abstract machine definition.
Same goes for Lisp.  It can't get the performance break it deserves because the hardware available today isn't a Lisp machine.  They've built them, and I can assure you that C++ would be the loser slug of a language on a Lisp machine.  But, alas, performance isn't the only thing programmers care about.  They also care about not having to learn anything new.
That's the other half of the irony.  Programmers are obsessed with performance, and they'll go to almost any length to fiddle with their algorithms and data representations in order to eek every last cycle and byte from their programs.  Any length, that is, except for learning a new language on new hardware.  Even if it would get them a thousand-X performance improvement for the same productivity.  Or a 1000x productivity improvement for the same performance.
Because they don't want to learn anything hard.  No gain, no pain, problem solved.
And that's where we're at.  Moore's Law is crap.  If we ever want to be 10x as productive
*and*
computationally efficient, let alone 1000x, then our whole computing model will have to change at once.  Nothing else will do.  The incremental approaches have all failed.  It's got to be a revolutionary change.
If everything changes all at once, that's going to pose a bit of a problem for the folks on the Zero Learning curve, wouldn't you say?  Don't freak out and mail me about this, either, because I'm a pessimist now, at least about this particular topic, and I doubt we'll ever get out of our rut.  We're ignoring the First Law of Holes.
You
*do*
realize that John von Neumann spent the last 10 years of his life singlehandedly developing a theory of computing based on cellular automata?  The computer you're reading this blog rant on was his frigging prototype!  He was going to throw it out and make a better one!  And then he died of cancer, just like my brother Dave did, just like so many people with so much more to give and so much more life to live.  And we're not making headway on cancer, either, because our computers and languages are such miserable crap.
You have no idea the pain I feel when I sit down to program.  I'm walking on razor blades and broken glass.  You have no idea the contempt I feel for C++, for J2EE, for your favorite XML parser, for the pathetic junk we're using to perform computations today.  There are a few diamonds in the rough, a few glimmers of beauty here and there, but most of what I feel is simply indescribable nausea.
Are you beginning to see why I prefer to work with programmers who stay on the Upward Curve after they get out of school?  Because even while we're grubbing around in the dirt — just a sorry bunch of illiterate, innumerate cavemen, here in the very heart of the Stone Age of programming — at least these upward-curve programmers give me some
*hope*
.  Hope that if something better comes along, they'll give it a try, a serious try, the old college try.  Or hope, even, that they'll build that "something better" with me.
Fat chance.  But hope can keep ya going for a good long while.
**Baby Steps**
It's all still fun, though.  Broken glass and razor blades aren't so bad, when I think about how much worse my lot in life could be, had I been born in a different time or place.  I've got it pretty good, and so have you, in all probability.
At my current job
they feed us and massage us like Kobe cows, and I'm surrounded by unbelievably brilliant people, all way smarter than me, and we're doing great stuff together.  Make no mistake: my blog whining is all relative to a totally imaginary future, one which in all likelihood, should it ever come to pass, will be filled with even more whining about totally imagined
*new*
futures.  It's just in our nature to whine.  But really, I have no complaints.
I put a lot of stock in fun.  And family.  And trying to live my life in such a way that I won't have any major regrets when the game's over.  So there's the first part of my schedule: having fun.
If you want to be on an upward curve, just make some time for it, and make it a habit.  That's all there is to it.  It doesn't matter if you're trying to get better at programming, or math, or fitness, or flying kites, or even humanity's Number One Fear, even worse than the fear of Death: public speaking.  You just work your way up, a little at a time.
I can't promise you any satisfaction from the upward curve.  You'll get better at a lot of things, and you'll have plenty of interesting insights.  You may even get a better job, or build some software that makes you famous, or just have more fun at what you do.  But you won't have much time for television.  Something will have to give.  We all have to choose how to play our time, and it's a zero-sum game.
If, like me, you're dissatisfied with the current state of affairs, well, believe you me, you can find a lot of consolation in a book on math, or machine learning, or compiler construction, or on just about anything that promises to help in some small way.
You do have to learn to put up with the pain of learning, though, and make it a habit to push yourself a little each day.
As far as the actuals go, well, you'll just have to find an approach that works for you personally.  You might only be able to devote one quiet hour a week to studying, but like unit testing, or working out, or brushing your teeth, it's better than not doing it at all.
Just try to have fun, and hopefully the rest will fall into place.

---

Notes
Permit me to assure you that I do not ever speak in
*any way*
for my current employer.  Like, don't you even think it for one second.  They're them, I'm me, and let's leave it at that.  In fact, I don't even work there.  My friend does.  And neither me nor my friend speaks for them.  OK?  OK.