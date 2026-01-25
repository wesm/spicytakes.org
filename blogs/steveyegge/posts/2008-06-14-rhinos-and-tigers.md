---
title: "Rhinos and Tigers"
date: 2008-06-14
url: https://steve-yegge.blogspot.com/2008/06/rhinos-and-tigers.html
word_count: 11534
---

I will once again plagiarize myself by transcribing a talk I gave.
First: be warned!  I offer this gesture of respect to you — yes, you! — when I say that this is at least 20 minutes of reading.  This is long even for me.  If you're surfing reddit, gobbling up little information snacks, then it's best to think of this entry as being more like a big downer cow.  Unless you're
*really*
hungry, you should wait for it to be sliced into little bite-sized prion patties before consuming it.
If you do read it, you'll see the CJD analogy is surprisingly apt.  I ramble even more than usual, and lose my train of thought, and the slides might as well be scenes from a David Lynch movie for all the relation they have to my actual talk.
But once again I find myself astonished at how much I agree with myself, by and large.  Funny how that works.  And I made a few decent jokes here and there.  So I'm transcribing it.
If you're impatient, and I wouldn't blame you a bit, the best part is probably "Static Typing's Paper Tigers".  That might be worth reading.  As for the rest... *shrug*  If you're really starved for content, you might find some of it entertaining.
**The Setting**
I gave this talk at the
[Google I/O Conference](http://code.google.com/events/io/)
in San Francisco a few weeks ago.  My talk was boringly titled "Server-Side JavaScript on the Java Virtual Machine", and there were initially only about 40 or 50 people in the room (out of a 2500-person conference) when I started the talk.
Even though I personally thought the talk was pretty boring, people kept trickling in, and I estimate there were about 400 people stuffed in the room by the end.  It was standing-room only, and people were spilling out into the hall.  The conclusion?  The other talks must have been
*really*
boring.
After my talk it became pretty clear to me that it should have been titled "Rhinos and Tigers", so that's its new name.  I've tried to make it flow well by splitting it into arbitrary sub-sections, whose titles aren't really part of the talk.  But otherwise it's pretty much a word-for-word transcription, except with most of the umms and aaaahs elided.  I've included the subset of the slides that seemed relevant; you can find the rest at the
[Google I/O site](http://sites.google.com/site/io/server-side-javascript-on-the-java-virtual-machine)
.
So enjoy!  Or not.  I've given you plenty of warnings.  You'll see!
**Rhinos and Tigers**
Hello!  I'm Steve Yegge.  I work at Google.  I've been there about three years, and it's real nice.
I'm going to be talking about server-side scripting in general, and talking a lot about
[Mozilla Rhino](http://www.mozilla.org/rhino)
and the technology behind it.  I'm going to try to get through it in maybe 20-25 minutes, maybe 30 if I start ranting, at which point I'll open it up for questions.  I kind of want you guys to help drive how this goes.
Make sense?
*(Ed:  Well, it made sense at the time.  Sigh.)*
All right, cool.  Let's get started.
Sooo... I'm going to be talking about Server-Side JavaScript on the Java Virtual Machine.
Yes.  We've got this big animal.  Rhino.
So let's see... who here has used a JVM language before?  Oooh!  My god, lots of you, almost all of you.  Great!
Well I'm going to be talking about Rhino in particular.  I'll be making reference to other JVM languages.  I want to kind of help you see how this fits into the landscape, why you might use it, why you might not use it.
But for those of you who haven't used a JVM language, the Java Virtual Machine is sort of like .NET: you can run multiple languages on it.  You can write an interpreter in Java, or you can compile your language down to Java bytecode.  Or you can compile it down to your own bytecode; there are different ways to do it.
But typically these languages are sort of drop-in replacements for Java.  Which means you can implement classes, you can implement interfaces, you can subclass things.  It gives you an alternate syntax and semantic layer on top of the libraries, and on top of the virtual machine.
I'll assume that this makes sense... well, actually, I won't!
**FOO Chaos**
There's this dude named
[Walter Bright](http://en.wikipedia.org/wiki/Walter_Bright)
, who wrote the
[D programming language](http://www.digitalmars.com/d)
, among many other things.
*(Raise hand)*
Has anyone heard of Walter?  He's this really smart dude.  He wrote Symantec Cafe, and the game Empire [and Zortech C++].
He told me the other day, [talking about] one of my blog rants, that he didn't agree with the point that I'd made that virtual machines are "obvious"
.  You know?  I mean, of course you use a virtual machine!
But he's a compiler dude, and he says they're a sham, they're a farce, "I don't get it!"  And so I explained it [my viewpoint] to him, and he went: Ohhhhhhh.
Virtual machines are great for language interoperability.  If everybody in the world used his language, then yeah, you probably wouldn't need a virtual machine.  You'd probably still want one eventually, because of the just-in-time compilers, and all the runtime information they can get.
But by and large, we don't all use D.  In fact, we probably don't all use the same five languages in this room.  And so the VM, whether it's the CLR, or the Java VM, or Parrot, or whatever... it provides a way for us to interoperate.
Now I'll tell ya — I was at Foo Camp last summer.  I've been wanting to tell this story...  I'm telling you guys; it's the coolest story.  And it's relevant here.  Heh.  Very relevant.
So I was in this tent... you know what
[Foo Camp](http://en.wikipedia.org/wiki/Foo_Camp)
is?  It's O'Reilly's, you know,
**F**
riends
**O**
f
**O**
'Reilly invite thing that they do each summer.  It's coming up in a couple of weeks.  And people give presentations; people show up and just wander into your [presentation] tent, and wander back out if they don't like it.
So I was in this discussion at the very end of the last day, where the Apple
[LLVM](http://llvm.org/)
guy Chris [Lattner] was hosting a talk on dynamic languages running on different VMs.  And there was the Smalltalk
[Squeak](http://squeak.org/)
guy there, and there was
[Charles Nutter](http://headius.blogspot.com/)
for
[JRuby](http://jruby.codehaus.org/)
and representing the JVM.
[John Lam](http://www.blogger.com/www.iunknown.com)
was there for
[IronRuby](http://www.ironruby.net/)
and CLR, and there were the
[Parrot](http://www.parrotcode.org/)
people.  I can't even remember them all, but the whole room was
*packed*
with the VM implementors of the VMs today, and people who are implementing languages on top of them.
This was a
*smart*
group of people, and well-informed.  And you know, I was like a fly on the wall, thinking man, look at all [these brains].
And Chris, well, he let everybody go around the room and talk about why their VM was the best.  And they were all right!  That's the weird thing: every single one of them was right.  Their VM was the best for what they wanted their VM to do.
Like, Smalltalk [Squeak]'s VM was the best in the sense of being the purest, and it was the cleanest.  Whereas the Java one was the best because, you know, it has Java!  Everybody's was the best.  Parrot's was the best because it was vaporware.  Ha!  Ha, ha ha.  Sorry guys.
So!  He [Chris] asked this really innocent question.  He goes, "You know, I don't really know much about this stuff..."
Which is bad, you know.  When somebody says that to you at Foo Camp, it means they're settin' you up.
He says, "So how do these languages talk to each other?"
And the room just
*erupted*
!  It was chaos.  All these people are like, "Oh, it's easy!" And the rest of them are like "No, it's hard!"  And they're arguing, and arguing, and arguing.  They argued for an
*hour*
.
And then they stood up, still arguing, and they kept talking about it, heading into the dinner tent. And they sat down, going at it for like three hours.
It was
*chaos.*
Because some people were saying, "Well, you know, if Ruby's gonna call Python, well, uh, you just call, right?  You just share the same stack, right?"
And the others are like, "Well, what about different calling conventions?  What if they support optional vs. non-optional arguments?  What if they support default arguments?  What about the threading model?  What about the semantics of, you know, the
pointer?  What about all this
*stuff?*
"
And they're like
*(waving hands)*
"Ooooh, we'll gloss over it, gloss over it, smooth it over."  And the reply is: "You
*can't*
.  This is fundamental.  These languages work differently!"
And oh my god, it was really interesting.  And it was also very clear that it's ten years of research and implementation practice before they get this right.  Before you'll be able to have a stack of calls, where you're calling from library to function, library to function in different languages.
So today, VMs are good for interoperability, but you've gotta use a bridge.  Whether it's JRuby, or Jython, or Rhino, they provide a set of APIs — you know about
[javax.script](http://java.sun.com/javase/6/docs/api/javax/script/package-summary.html)
, right?  It's this new thing introduced to the JDK, where they try to formalize just a couple of APIs around how you call the scripting language from your language... you know, it's a sort of "reverse foreign-function interface".  And then how they call each other, maybe.
But it's all done through... kind of like serialization.  You marshal up your parameters as an array of arguments, and it's a heavyweight call that goes over [to the script runtime] and comes back, and it's like... it's a pain!  You don't want that.  But today, that's kind of what we're stuck with.
At least we have that, though, right?  I mean, try having Ruby call Python today, and they have different FFIs.  You can do it, but you definitely want the VM's help.
So, Walter, that's why you need VMs.
**Power to your users**
So!  Yeah, there's a lot of stuff I could talk about.  I gave a practice of this talk to Mike Loukides, an editor at O'Reilly, and it completely changed what I wanted to talk about.
I do want to talk about Rhino's technology; I want you to come away understanding it.  But more importantly, I want you guys to understand where this fits in this Google conference.  And where it fits in
*your*
plans, going forward.
See, it's really interesting.  We all know, or at least most of us I think agree, that server-side computing is finally starting to make inroads onto the desktop.  Fat clients aren't so much the norm anymore.  You've got applications like Google Maps, GMail, Google Docs, those kinds of apps, that are doing "desktop quality" applications in the browser, with the server handling your storage.
That's kind of one of the messages of this conference.  Everybody's doing it, right?  It's not just Google.  And it makes a certain amount of sense, so I'm not going to go into the reasons why you'd do that.  I'm assuming it's sort of a given.
*(Editor's Note: you'd be amazed at how many emails I get from people who maintain it's a fad of some sort, one that's going away, which is why I bother to make this disclaimer.)*
The interesting thing is this: all applications... who was it who said "All apps will eventually grow to the point where they can read mail, and if they don't, they'll be replaced by ones that can"?
*(audience: "JWZ")*
JWZ?
[Jamie Zawinski](http://en.wikipedia.org/wiki/Jamie_Zawinski)
.  Yeah.  It's a variant of somebody else's quote [Greg Kuperberg's], but...
So it's true, right?  Apps grow.  If you like an app, you're gonna want to start doing more and more stuff in it.  If you like it a
*lot*
, like I like Emacs, heh... you know, you like your editor.  Everybody here is a programmer, right?  You all use development environments?  Do you ever find it kind of annoying that you have to switch from your IDE to your browser?  Why isn't the IDE the browser too?  Why aren't these unified?
I mean, let's face it: I only run two apps.  Unless I need to run, like,
[OmniGraffle](http://www.omnigroup.com/applications/OmniGraffle/)
or the
, or something to do a document, or
[Keynote](http://www.apple.com/iwork/keynote/)
here to do the presentation — I just switched to Macs, so I'm learning all these names, but, this PowerPoint thing — most of the time, when I'm developing, I'm running shells, and I'm running Emacs, and I'm running a browser.  That's it!  So you kind of wish they'd be the same.
Well, once they get big enough, your IDE and Emacs and the browser have this thing in common, which is that they are
*scriptable*
!
That's the magic point at which your application becomes sort of
[alive](http://steve-yegge.blogspot.com/2007/01/pinocchio-problem.html)
.  Right?  Because people can change it, if it doesn't work the way they like it.
[GreaseMonkey](http://en.wikipedia.org/wiki/Greasemonkey)
!  Perfect example.  You don't like our web page that we give you?  Write a GreaseMonkey script and change it all around, right?  That's cool!  Scripting is really important.
I mean, Emacs, it stands for "Editor Macros", and it started off as a really thin engine, and the whole editor was written in scripts.  And now it's huge.  It has a million lines or so of Emacs-Lisp code floating around.
So it's weird... you go through this transformation, where your scripting languages are originally for, well, scripting.  And it eventually grows into application level/scale development.  OK?
Now we all see this happening in clients.  Excel, for instance, is scriptable.  And the reason that Excel is so powerful, I mean the reason that you can go to the bookstore and get a book that's
on Excel, and scientific computing people use it, whatever, is that it has a very very powerful scripting engine.
In fact, all of Microsoft Office has it.  Right?  You can fire up Ruby or Python or Perl, and you can actually control, though the COM interface, you can actually
[tell IE to open a document](http://steve.yegge.googlepages.com/scripting-windows-apps)
and scroll to a certain point in it.  Or you can open up Microsoft Word and actually... I mean, if you want to do the work, you could actually get to where you're typing into your Perl console and it's showing up over in Word.
Server-side computing has to get there.  It's
*gonna*
get there.
But how many server-side apps are user scriptable today?  Precious few.  Google has a couple, you know, like our
[JotSpot acquisition](http://en.wikipedia.org/wiki/JotSpot)
, which is [scriptable] in Rhino...
So we're talking about something that's kind of new.  I mean, we can all see it coming!  But it's still kind of new, the idea, right?  Why?
Because this is scary hard, from a security perspective.  Heh.  You're going to run code on
*my*
servers?  Uh... OK...
I mean, Yahoo! Store, you know, Paul Graham's
[Viaweb](http://en.wikipedia.org/wiki/Viaweb)
that
[went on to become Yahoo! Store.](http://www.paulgraham.com/avg.html)
People have done it, right?
I wrote a
[game](http://www.cabochon.com/)
that was really cool.
[Scriptable](http://www.cabochon.com/wiz/code_examples)
!  I mean, high school kids were teaching themselves to program so they could write areas and monsters and spells and quests for this game that I wrote, which was written in
[Java](http://www.cabochon.com/api/index.html)
and scriptable in Jython.
It's a big deal!  I mean, people want to be able to write these apps.
However, I had to live with the fact that I didn't personally have enough bandwidth to come up with a decent security model to keep them from...  it's a trust-based security model in my game.  They write a script, they could erase my hard disk, right?  So I've got to be very careful, and recognize that I can only let certain people that I trust do it.  And that I've got to be prepared for really big disasters.
Because also there's denial-of-service.  It's inadvertent: oh, their script is taking up all the bandwidth [or CPU or memory] on my server, and everybody else in the game is paralyzed.  Right?  I mean, how do you deal with it?
You've got to deal with user [i.e., programmer] throttling:  memory usage, the database or datastore usage, like Amazon's computing cloud, you know, they have a lot of this stuff in place.  But usually it's pretty coarse-grained when it gets started, right?  You get a box, and a certain amount of disk storage, and you get the whole CPU, because how are you gonna allocate CPUs out to people when the languages themselves that are being used for scripting don't support that?
*(Editor's Note: obviously you can just use process scheduling, but I'm talking more about multithreaded processes like my game, or Second Life, where many users may be scripting within the same processes.  It makes things harder.)*
We're getting there; it's happening.  But it's new.  And it's hard.  Because you don't want people to be able to go and get access to your company's proprietary code or resources and wreak havoc.  You just want to host their computing.
So when you decide you're going to take your server-side application, with its beautiful Ajax app talking to the server, and now you want open it up: to add extensibility for your end users — they're not just scripting the client; there's scripting happening on the server that's theirs — you have to make a decision!
Namely, what language are you going to give them?
We have... see, unfortunately it's hard for me to talk about Google products, because all I know are their internal code names, and not their launch names.  I can never remember them.  But we have...  something like that.  Heh.  Called... Prometheus, I think?  Uh, wha... what is it?
*(audience member: Google App Engine)*
Ahem, the
[Google App Engine](http://code.google.com/appengine/)
, of course!  Yes.  The Google App Engine.  Ahem.  Yes.
*(me: embarrassed)*
And I think it's... Python.  Right now.  But of course they want to open it up, because, it's like, you don't really want to force people to switch editors, unless you want a real fight on your hands.  You kinda don't really want to force people to switch languages either, right?  People want to use whatever they're comfortable with.
So again, you wind up with this hosted environment, where you're supporting multiple languages; which one do you pick [first]?  They picked Python.  You can pick [anything], but you've got these problems to deal with.  And I'm going to argue today that Rhino is actually a really good choice for this particular problem space.
OK, we've got people pooling up in the back here.  Is it time to invite them in?  Come on in, sit down, there's space!  All right, cool.  Yeah.  Welcome!
So yeah.  That's what I'm talking about today.  Do you guys understand the perspective now, the context?  I'm talking about server-side scripting, that either you do yourself inside your company, because you feel like you've got some logic that needs to be kind of "glue" logic — "scripting" — or, more importantly, you're opening it up to your users.  Which means you need to sandbox it, and you need to meter it and throttle it.
**Advantages of scripting on the JVM**
All right.  Yeah.  So this is a JVM language.  A JVM language can share the Java libraries, and the Java Virtual Machine.  It's really cool, right?  And really powerful.
Right off the bat, these JVM implementations of other languages, like JRuby vs. Ruby, Jython vs. Python, right?  They get all these free benefits, that may not necessarily exist in the C runtimes for these languages.
Example?  Java has a really good garbage collector these days.  A
[generational garbage collector](http://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29#Generational_GC_.28aka_Ephemeral_GC.29)
that's becoming an incremental [and/or concurrent] generational garbage collector... I mean, it's good!  Whereas for a lot of these [C-based] languages, they use mark-and-sweep, reference-counting...
Another one is native threads.  It's veeery nice to have native threads, and also have well-defined semantics for the threads and how they interact with the memory model.  I mean, a lot of these [non-JVM] languages are like, "Well, we have threads, but you probably... don't want to use them."  Because you're kind of on your own.
So what happens is people use process-switching; it's the share-nothing model.  And that's great too, for certain situations.  Provided you've got good engineering library support around it, like the
[java.util](http://java.sun.com/j2se/1.5.0/docs/api/java/util/concurrent/package-summary.html)
concurrency libraries.  They can help you design something without having to do a formal proof around it to get it to work.
That helps a lot in multicore.  It helps!  JavaScript has no [language-level] threads, because Brendan Eich says "
[over his dead body](http://weblogs.mozillazine.org/roadmap/archives/2007/02/threads_suck.html)
".  I totally understand where he's coming from on this, right?  There's certainly the "promise" of better concurrency out there.  Erlang, you know, and maybe
[STM](http://en.wikipedia.org/wiki/Software_transactional_memory)
...
But hey man, today?  I mean, right now?  You want to write something with high throughput, and you've got a lot of I/O to do, and it's parallelizable?  And you want to get a lot of throughput on one box, because it's got multiple cores?
*(shrugging)*
Well, threads get the job done.  So if you've got it in your so-called "scripting language", it's a big win.
We've got garbage collection, threads... and asynchronous I/O, right?  When Java first came out there was the whole "one thread per socket" model [actually, two], which meant that you couldn't write a webserver that could handle ten thousand concurrent requests.  It didn't matter how much memory or CPU your box had.  Anyone here ever tried to fire up 10,000 threads on one box?
Yeah...  yeah.  What happens is, the scheduler and task-switching resources for managing the threads swamp your machine.  So eventually Java wrote a
around the Unix or Windows or whatever native interfaces so you could get super-high throughput.
So all of the sudden, by sticking something on the JVM...  Sure, you initially get a bit of a hit in performance.  When these people first port a language to the Java Virtual Machine, it's usually about twice as slow, right?  BUT, it's got async I/O, and it's got [native] threads, and it's got better non-pausing (by and large) garbage collection.  And from there, they can make it smarter.
But they've also got the JIT.  I don't know, I mean, did anybody here...  I gave a
[talk on dynamic languages](http://steve-yegge.blogspot.com/2008/05/dynamic-languages-strike-back.html)
recently at Stanford, but I don't want to rehash that if you guys already know about that.
Basically I argued in that talk — successfully at Stanford, so I think that was... something — that for
[just-in-time compilers](http://en.wikipedia.org/wiki/Just-in-time_compilation)
, it's becoming pretty clear, they have a lot better access, a lot better data at runtime about how you're actually using your program right now than the compiler ever had.
So the JITs can do all kinds of inlining and optimizations that you just can't do in a compiler.  And what that means is that everybody running on this VM gets to benefit from the JIT.
So there are lots of advantages to these JVM languages.  Or .NET, if you happen to be using Microsoft stuff.  It's a good model.
**But why Rhino?**
So why Rhiiiiino?  Why JavaScript?
*(loudly)*
Who here thinks JavaScript is kind of icky?  Come on, come on, be honest.  Yeah, there we go, a couple of people.  Yeah.
Yeahhhh... and you know what?  It is!  Right?  Because, well, because of vendor implementation issues.  That's one [reason].  Also, Brendan was kind of forced to rush it out the door.  You guys know... back at Netscape, when they built JavaScript, it was called, um, LiveScript?
And Brendan was building
[Scheme](http://en.wikipedia.org/wiki/Scheme_%28programming_language%29)
for the browser.  Scheme!
Everyone in here who knows Scheme, raise your hand.
*(Many people, at least fifty, raise their hands.)*
Holy... smokes!  A lot more than I would've guessed.  Wow.
OK, well, as it happens, you guys are not "representative".
*(laughter)*
And so, Netscape kinda looked at it, and said: "Yeah, well, we did say Scheme, but, uh, there's this Java thing, this giant marketing thing, and we want to be involved with it."  And some back-door deals happened, and then they came to Brendan and said: "Make it look like Java."
So now it's Scheme with Java syntax, right?  So he had to pull a lot of all-nighters for a couple of weeks, and he came up with JavaScript.
So, you know, it's got some flaws.  Some of which make you want to go scrape your teeth on the sidewalk because it's less painful.  So it's true, but what language doesn't have some flaws?
The interesting thing about Rhino, which is an implementation of JavaScript in Java, is that there's only one language.  You don't have to worry about vendor-implementation or cross-platform problems because... it's just Rhino.  So right out of the starting gate, that's a win.
Plus, Rhino gives you the ability to work around some of the problems.  A classic one is the problem in JavaScript where you can't define non-enumerable properties.  Right?  You know how you can go
, and it'll enumerate the keys of your object as if it were a hashtable.
Nice feature, right?  And you can add properties to objects; you can go to
, which is the root object of the whole system, and add your own function(s) there.  But what happens is, you've added a function that's now enumerable in everybody's arrays, and everybody's data structures, so their
loops break.
Which means that fundamentally you can't install a library that's completely seamless and emulates Ruby or Python or some other really expressive set of library functions.  Like, you want your
and
, and your
, and...  you know what I mean?
You can't do it in browser JavaScript, so people wind up going different routes.  They either do what
[Prototype](http://prototypejs.org/)
does, and just install it, and you're screwed if you use
, but you don't use
, right?
Or they use functions.  They don't use object-oriented programming.  And you know, functional programming is great and everything, but OOP, as we've discovered in programming in the large, is a nice organizational tool.  Putting the function or method together with the thing that it's operating on is a nice way of organizing things.
So it's kind of unfortunate when you have to use functions, because if you have to say, you know,
, it gets inverted with functions:
.  You have to call from the innermost one to the outermost... it's "backwards", right?
Rhino winds up getting around that problem completely.  We did, anyway, internally.  Because it's written in Java.  So you can call the
[Rhino interface](http://www.mozilla.org/rhino/apidocs/)
.  You can call Parser, or the interpreter, or the runtime; you can do whatever you want.
So I wrote this little
function, that's like five lines of code.  It calls into the script runtime
[Java class that implements JavaScript objects](http://www.mozilla.org/rhino/apidocs/org/mozilla/javascript/ScriptableObject.html)
, which has a
[non-enumerable](http://www.mozilla.org/rhino/apidocs/org/mozilla/javascript/ScriptableObject.html#DONTENUM)
.
JavaScript has non-enumerable properties; it just doesn't let you add your own.  It's just a language flaw, right?
That [
function] enabled us, in the project I'm going to be talking about a little bit later here, to implement all of Ruby and Python's runtime — all the functions we liked — in [server-side] JavaScript, in a non-intrusive way.  We were also able to implement a class system, and all this other stuff.
So Rhino is
*not*
browser JavaScript.
Man, we've got more people pooling up at the entrances.  You guys are welcome to come in, squeeze in and sit down... come on in... welcome.  There's still space.  Especially up here kinda in the front, in the middle, where nobody wants to sit.  But trust me, it's better there.
So yeah.  Rhino's history:  it's like ten years old.  Or more?  More than ten years, maybe.  It started inside Netscape, side by side with
[SpiderMonkey](http://www.mozilla.org/js/spidermonkey/)
.  A lot of people have been hacking on it.  Rhino's pretty robust.
**Rhino at the shootout**
I have a question for ya.  I did this "JVM shootout" like three and a half years ago.  I was kind of tired of using Java for scripting, and I wanted to look at all the JVM languages.  So I did this game.  You know about the game
[Sokoban](http://en.wikipedia.org/wiki/Sokoban)
?  I would have done Sudoku if the craze had hit then.  It's a little dude who pushes these blocks around these mazes?
Well, I reimplemented this thing, which is about, you know, six or seven hundred lines of Java code.  It had a [user] interface, and a little search algorithm that had him chase your mouse.  It was just big enough of an application that I could reimplement it in like 10 different languages, and actually compare how it was speed-wise, how to use them [the languages], how well they interoperated with Java... it was an actual apples-to-apples comparison.
Most of them really, really, REALLY stank.  It was baaaad.  I mean, there are like
[250 JVM languages](http://www.is-research.de/info/vmlanguages/)
out there, but most of them are just complete toys.  But there were ten or so that were actually pretty good.  You could do anything in them, and they had decent performance, and they were good, right?
And it [the shootout] kind of petered out, because it started looking like Rhino-JavaScript was going to win.  I had this sort of
[solution selection matrix](http://en.wikipedia.org/wiki/Decision-matrix_method)
of criteria where... it was kind of a heuristic function where I weighted all these terms, right?  Just to kind of get a feel for which one [was best].
And I wanted JRuby to win.  You should never go into these comparisons wanting one of them to win, because, you know, you're either going to bias it or you're gonna be disappointed.  JRuby at the time was really slow.  It's much faster now, and everything, but at the time, it was so new.
Jython was good, but it wasn't fast enough, and the author of Jython had gone off to greener pastures.
Rhino!  Rhino had good tools, and it had good performance, and it was... JavaScript!  Eeeeww!
So I never even really... I published it, but I didn't leave it up.  I'm actually going to bring it back up again soon; I'm going to update it and do a couple of new languages.  Because I find this an eternally fascinating question, which is: what is the
[next big language](http://steve-yegge.blogspot.com/2007/02/next-big-language.html)
, especially on the JVM, going to be?
**Domain-specific languages**
Java will always have a place.  But I think there are domains, like Java Swing, you know?  The Java GUI stuff?  Java's really not very good for that.  We've kind of figured out that Object-Oriented Programming doesn't work that well for UIs.  You want it to be declarative.  HTML showed that you want a dialog, with a title bar, and a body, and it
*nests*
, to match the [UI] tree.
That works really well.  It's succinct.  Even in HTML it's succinct, right?  Whereas with a [Java-style] object-oriented language, you've got to say, you know,
,
,
,
, 'til the cows come home.  And it doesn't
*look*
anything like... you can't pattern-match it and say "ah yes!  this looks just like my UI!"
So people write these wrappers around Swing.  Like there's
[Apache Jelly](http://commons.apache.org/jelly/)
, which wound up with this XML framework to do Swing programming, that was 30% less verbose than Java.
What are the odds that XML's going to wind up being less verbose than
*anything?*
*(loud laughter)*
Really!  I mean, I was shocked.  30% less verbose.  And I looked at it, too.  They weren't cheating.  I mean, they did the best Swing implementation in Java that they could, but Jelly was better.
So there are domains for which Java is just not appropriate.  But you still maybe want to use a VM for all the reasons that I outlined earlier.
So yeah!  There's room for these other languages.  But which one?  All of them?  Are they going to solve the problem I brought up from Foo Camp earlier?  To where it doesn't matter which language you're using; they can call each other, and [mix however you like?]
I mean, how's your editor going to feel about that?  How's your team member going to feel about it?  A lot of people don't like learning new languages.
Who here doesn't like learning new languages?  Come on, be honest...
*(A few people raise hands)*
Yeah!  New languages.  No fun!
It's actually kind of... you should try it.
*(laughter)*
You know?  It is.  It's a good idea.
There's this dude — has everyone heard of
?  The Little Schemer,
,
?  Cool books, right?  Teach you functional programming in this really bizarre format that hooks you in.
[Dan Friedman](http://en.wikipedia.org/wiki/Daniel_P._Friedman)
, the guy who [was] one of the collaborators on those books — I was reading an
[article he wrote](http://www.cs.indiana.edu/hyplan/dfried/mex.pdf)
.  Early in his career he realized that languages are fundamental to computer science and to engineering; they're really important.  And he wanted to be able to learn a new language every quarter.
And after he did that for a while, he said, you know what?  I want to learn a new language every
*week*
.  OK?  And you can actually get to the point where you can do this.  Now it probably takes 2-3 months before you're actually as comfortable with the new language as you were with your favorite old one.  This happened to me with JavaScript; I was freaking out for the first couple of months, thinking "this is
[nevergonna work](http://steve-yegge.blogspot.com/2007/06/rhino-on-rails.html)
".
But eventually you get over the hump, and you're like
*(relieved sigh)*
"aaaah, yes."  Right?  You learn how to work around the problems.  It's just like learning Java or whatever your first language happened to be.  You've got to learn your way around all these problems, and you've gotta learn how things work, and how the libraries are laid out.  And all of the sudden it becomes like breathing.
So Dan Friedman, after he said he was learning a language a week, I thought, "wow, that's pretty macho."  But he said, nah, that wasn't good enough:  he wanted to be able to
*implement*
a language a week.  And he got pretty serious about it.  Spent years researching how to do this effectively.
*(Well, now I'm just speculating – Ed.)*
This is where I'd love to see engineers today.  Knowing languages will make you a better programmer.  It will!  It will even if you're not using them.  Just write a little application in it, and it opens your mind.  [Each new one] opens your mind.  And now suddenly you know the superset of all the languages out there.  So it's not scary to learn new ones.
And you can also recognize situations where a
*language*
is actually the right tool for the job.  Not a library, not a framework, not some new object or some new interface.  A language!
Case in point?
.
*(raise hand)*
Who likes to write their own giant deterministic finite automata to do string matching?  Heh.  It's weird — nobody raised their hand.
Who likes to do lots and lots of manual DOM manipulations, as opposed to, say,
?  XPath is a language, right?  DOM manipulations, you know... it depends, but usually, no:  not if you can get away with using a language for it.
I could talk for hours about that, so I'm not going to.  But, you know... it's good to learn new languages.  So I'm gonna teach you JavaScript today.  I'm gonna dive in.  So let's go!
**The right way to do unit testing**
Oh yeah.  So unit testing.  I mean, like, all the other stuff on this slide is like "blah blah blah", but then Unit Testing [in Rhino] — this was a real surprise to me.
I write a lot of Java code day to day, [out of the] probably five different languages I code in regularly.  And unit testing was always a chore.  Unit testing is a chore.
I mean, come ON.  Unit testing's a chore, right?
*(raise hand)*
Who here thinks unit tests are just a poor man's static type system?  Eh?
*(some laughter)*
Yeah!
Well, not really, since you have to write unit tests for them [the static languages] too.
*(more laughter)*
You need to write unit tests, and unfortunately in Java it's
**very painful**
.  I'm speaking into the mic now, so that everybody can hear.  Unit testing in Java is painful!
It's
*so*
painful that people, the Java... community, the Java world, has evolved
*around*
it.  OK?  They've said:  "Don't use constructors.  Constructors are baaaaad."
*(pointed pause)*
I mean... what!?
*(laughter)*
I mean, like, if you program in Ruby, say, you know that you can actually change the way the metaclass produces objects.  So if you want it to be a singleton, or you want it to meet certain... you want it to be a Mock object, you just replace the
function on the fly, and you've got yourself a Mock constructor, right?
But Java's set in stone!  So they use factories, which leads to this proliferation of classes.  And you have to use a "Dependency Injection Framework" to decouple things, right?
And it's just, like,
*(panting)*
...  We were doing business logic early on in Java.  When Java came out, it was like:  "Ooooh, it's a lot easier to write C code", basically, or C++.  Rather than focusing on your memory allocation strategy, or which of your company's six conflicting
classes you're gonna use, you get to focus on "business logic".
But unfortunately that only took you so far.  Now you're focusing on Mock object frameworks.  It [Java] only took you a little farther.
Now I
*swear*
, man, doing Mock objects in Rhino is so easy!  It's easier, even, than in JRuby or in Jython, because JavaScript has
[JSON](http://www.json.org/)
.  I didn't even know, like, the name of it when I started doing this, right?  But JSON... I've gotta show you guys this.  This is so cool.
*(flipping through slides)*
Yeah, tools, blah blah blah.  We'll come back to it.  Oh, it's way down in here.  Urrggh.  Come on... here's one!
OK.  Down on the bottom we've got some code here.  Actually on the top, too.  So I do a
with a
, and, uh... it sure looks a lot like Java code, huh?  This is one advantage of JavaScript, actually.  Java...Script, right?  Ten years later it's finally becoming the scripting language for Java?
So that syntax
*(with an obj literal following `new Runnable()`)*
is a little weird, but there's another one here that says:

```
js> obj = {run: function() { print('hi') }}
```

So I've declared an object literal, using "JSON style".  Now JSON doesn't let you do — does JSON let you do functions?  Probably not, right?  But I mean, fundamentally you're doing this declarative property-value list, right?
And so what I've got is this anonymous thing that has a named "run" property whose value is a function!  That prints "hi".  And now I can create a new
, with a new
that wraps it, and what effectively I've done is I've used that thing as the
interface [implementation], which expects a function called "run" that takes no arguments and does whatever the thread's supposed to do.
This is how you do mock objects!
I have this huuuge legacy system, right?  With hundreds of static methods.  Static methods are also bad these days, right?  Noooo static methods.  'Cuz they're not mockable.  Right?  Java has changed Java.  Because Java's not unit-testable.  So now you can't just go to the store and [buy a book and] learn Java.  You have to learn all these... fashions.  You have to learn what's in vogue.
Subclassing!
*Not*
in vogue right now.  You talk about subclassing, and people are like "NNnnnnnooooo, you should use manual delegation even though it's really hard and cumbersome and awkward."
And you're like, "but I just want to change this one method, and plus it's built into the language, and there's syntax for it, and it's kind of well-understood..."  And they just say "NO!"
It's out of favor.  For similar reasons.  Oh my god...
And I'm telling ya:  the reason unit testing is easy, is, fundamentally, the way you develop in a dynamic language is
*different*
from the way you develop in a static language:  C++, Java... OCaml, Scala, whatever.  Your favorite static language.
To a large extent, especially in C++ and Java, the way you develop is:
1. you write the code
2. you compile the code
3. you load the code
4. you run the code
5. it doesn't work
6. you back up
7. you change it again

So it's this batch cycle, right?  1950s.  Submit your punch cards, please.
In a dynamic language — and this is clearest when you're writing in Emacs Lisp [because of the
buffer] — but it's somewhat clear when you're developing in a console, in Python or Ruby, Perl, Lua, whatever, you write an expression, and you give it some mock data.
You're writing a function, you're building it on the fly.  And when it works [for that mock data], you're like, "Oh yeah, it works!"  You don't run it through a compiler.  You copy it and paste it into your unit test suite.  That's one unit test, right?  And you copy it into your code, ok, this is your function.
So you're actually proving to yourself that the thing works by construction.  Proooof by construction.
Obviously you still need your unit tests
*(er, I meant integration tests – Ed.)*
, because there's going to be higher-order semantics, you know, calling conventions between classes and methods...
Whew!  This room is really filling up.  Um, is there anything we can do to help here, guys in the back?
*(Tech guy says something inaudible in the video)*
Yeah, please!  There're more seats here.  I just want to... I don't want to get to where people can't even make it into the room.
Yeah, so unit testing.  I know you guys all hate unit testing.  So did I.  Or you say, "I looooove unit testing," but then, you know, your test coverage is still sitting at like 80%.
I'm telling you, man, this is a huge, huge thing.  It changes the way you do your development.
**Rhino's not Ruby**
And oh, yeah... I'm going to be talking shortly here about
[Rhino on Rails](http://steve-yegge.blogspot.com/2007/06/rhino-on-rails.html)
, which is this thing that I did... it's not Rhino on Rails, actually.  It's actually,
*I*
called it "Rhino's not Ruby".  Because I got kinda burned at Google for using Ruby.  Yeah.  Uh, for good reasons, good reasons.  But they were like: "No."
And so of
*course*
I called it "Rhino's not Ruby":  RnR.  Because people know JavaScript; they're kinda comfortable with JavaScript, so they were OK with it.  So I had to port Rails; it was kind of a lot of work, but, you know, well it works!  We're using it here internally; it's nice.  I mean, I actually know it's nice, because six months went by and I didn't look at it for those six months.  And for this recent project, I picked it up, and I was, like, is this gonna be gross?
But actually, it's really pretty nice.  Because you've got all the Java libraries, and all the integration with Google stuff.  It's cool.  I'll try to open-source it this year, if I forget to say that later on.
Anyway, I was writing unit tests for this thing, and... uh...
*(I completely blow my stack.  Who am I?  Where am I?)*
Have I lost where I am on the slides?
*(Duh.)*
I've diverged from the slides.  I'll come back to RnR shortly.  Basically, I got unit-testing religion.  That's the end of that sort of stack.
If you can do it easily, and you don't have to rewrite your application to be unit-testable?  Man.  That's a big difference.
So why would you
*not*
use Rhino for server-side scripting?
Well, it's not super-duper fast right now.  It's on the order of about twice as slow as Java, depending on what you're doing.  So if it really has to be super, super fast — use C++!  Right?  Naaaah, you can use Java.  Like I was saying the other day [at Stanford], it's widely admitted inside of Google — there's this whole discussion, is Java as fast as C++, right?  And Google Java developers definitely admit that it's as fast as C++.  The C++ people, well... yeah.
*(sigh)*
Let's see... if you're writing a library, then Rhino's actually not so good right now.  There is no standard library interface for scripting languages.  We haven't got there yet.  It's all, it's all related to what I told you about before, you know the calling interop.  A lot of these [languages] have their own package systems:  their own
, their own
, right?  So if you're gonna write a library, you should probably still write it in Java.  Maybe.
If you're doing a framework, where you're defining how things are called:  whether we're calling you, or you're calling us, then it's OK.
And if you really
*hate*
JavaScript, then that's, you know, that's fine...  But keep in mind, again, that you may be providing something for your end-users.  If you go out to a high school and you survey people, and you ask, "So what language are you learning?  How are you teaching yourself programming?"  It's a sure bet that a lot of them are doing Ajax stuff.  Right?  A lot of them are doing JavaScript.
If you want to make your end-users happy, and you want to immediately capture a very big user base, then no matter how you detest JavaScript (and again, Rhino-JavaScript's really not as bad as browser JavaScript, it's much better), your users probably will prefer it.  It's something to keep in mind.
All right.
**Static Typing's Paper Tigers**
And then we've got
[Scala](http://www.scala-lang.org/)
.  I've gotta mention Scala.  Who here knows... you've heard of Scala?  Yeah?
*(a few hands go up)*
Mmmmm, yeah, getting there... looks like some people, OK.
Scala is a very strongly typed language for the JVM.  It's from researchers in Switzerland; they're professors.  It's from sort of the same school of thought that static typing has evolved with over the last fifteen years in academia:  Haskell, SML, Caml, these sorts of
[H-M](http://en.wikipedia.org/wiki/Hindley-Milner)
functional languages.
And Scala's interesting because it actually takes a functional static type system and it layers... it merges it with Java's object-oriented type system, to produce....  Frankenstein's Monster.
I've got the
[language spec](http://www.scala-lang.org/docu/files/ScalaReference.pdf)
here in my backpack.  Oh, my god...  I mean, like, because it's getting a little bit of momentum, right?  So I figure I've got to speak from a position of sort of knowledge, not ignorance, when I'm dissing it.  (Heh heh.)
And so
*before*
, I was like: "Oh yeah, Scala!  Strongly typed.  Could be very cool, very expressive!"
The... the the the... the language spec... oh, my god.  I've gotta blog about this.  It's, like, ninety percent [about the type system].  It's the biggest type system you've
*ever*
seen in your life, by 5x.  Not by an order of magnitude, but man!  There are type types, and type type types; there's complexity...
They have this concept called
Meaning it's not just complexity; it's not just complexity-complexity:  it's
*parameterized*
complexity-complexity.
*(mild laughter)*
OK?  Whoo!  I mean, this thing has types on its types on its types.  It's
*gnarly*
.
I've got this Ph.D. languages intern whose a big Haskell fan, and [surprisingly] a big Scheme fan, and an ML fan. [But especially Haskell.]  He knows functional programming, he knows type systems.  I mean, he's an expert.
He looked at Scala yesterday, and he told me:  "I'm finding this rather intimidating."
I'm like, "THAT sounds like it's gonna take off!"
*(loud laughter)*
Oh yeah!
But the funny thing about Scala, the really interesting thing — you guys are the first to hear my amazing insight on this, OK? — is:  it's put the Java people in a dilemma.  There's a reeeeeeeal problem.
The problem is, the Java people say, "Well, dynamic languages, you know, suck, because they don't have static types." Which is kind of circular, right?  But what they mean, is they say:  No good tools, no good performance.  But even if you say, look, the tools and performance can get as good, they say, "Well, static types can help you write safer code!"
It's... you guys know about those talismans?  The ones, where, "What's it for?"  "To keep tigers away"?
*(some chuckling)*
Yeah?  And you know, people are like, "How do you know it keeps tigers away?"  And your reply is:
*(sneering)*
"Do you see any tigers around here!?"
*(minor laughter)*
So this is what... OK, so for a long time, for many years... and you know, I've written more Java code than most Java programmers
*ever*
will.
*(Editor's note:  nearly 1M lines in production.  Ouch.)*
So trust me.  I tried.  OK?  I'm not just coming in and saying "I don't want to learn Java."  No.  I know Java as well as the next person.
But I come to them and say, let's do proof by – say, argument by example!  You know, an existence proof.
[IMDB](http://www.imdb.com/)
is written in Perl, right?  Yahoo! – many of their properties are written in PHP.  A lot of Microsoft stuff's written in VB, right?  ASP .NET?  Amazon.com's portal site is Perl/Mason.
A lot of companies out there are building big, scalable systems – and I mean scalable in the sense of throughput and transactions, stuff like that, but also scalable in terms of human engineering — in these dynamic languages with no static types. [Using nothing more than good engineering principles.]
So... isn't that a demonstration that you don't need the static types to keep those tigers away?
And they're like:  "Well!  But!  What if... what if a tiger came?"
*(laughter)*
Right?  "People need shotguns in their house in case a bear comes through the door, right?"  The Simpsons made fun of that.
*(laughing continues)*
Yeah.  So, you know, for a long time, I was like: "Yeah, yeah, yeah.  OK.  So tigers could come.  Fine."
Scala, now, is the tiger that's going to kill Java.  Because their [type-talisman] argument now has become a paradox, similar to the Paul Graham Blub Paradox thing, right?  Because they're like, "Well, we need static typing in order to engineer good systems.  It's simply not possible otherwise."
The Scala people come in and they go:  "Your type system
*suuuuuucks*
.  It's not sound.  It's not safe.  It's not complete.  You're casting your way around it.  It doesn't actually prevent this large class of bugs.  How many times have you written
in Java?  Our type system doesn't allow [things like] that."
Our type system does what
*you*
said
*your*
type system was doing.
So, therefore, you should be using it!  ∴
And the Java people look at it and go:  "Wehellll...
*(cough cough)*
... I mean, yeah, I mean...
*(*ahem*)*
"
*(running finger under collar, as if sweating profusely)*
They say, "Welllll... you know... it's awfully... cummmmmbersome... I..."
"We can actually get around the problems in practice that you guys say your type system is solving through Good Engineering Practices."
*(laughter begins to grow)*
HA!!!
*(I point accusingly at the audience, and there's more laughter)*
Yeah.
So Scala is creating a real problem for [Java's] static typing camp now.  Because their last little bastion of why they're using it, the whole tigers argument, they're like, "Ah, well... we... we keep shotguns in our house."  [This is what they've been reduced to.]
OK?  Yeeeeahhhh...
So back to dynamic languages!
But my point was — from a previous slide actually — it's very interesting.  See, I wrote this Rails port, and it wasn't... I never got it to where it was quite as succinct as Rails, because JavaScript has curly braces and a little bit of extra syntactic cruft.  But it was close!
And then we used this framework to build this web app internally.  It was for external consumption.  It's kind of a long story that I won't go into.  But we had like 20 engineers on this thing, for close to a year.  And we had a huge application.  I mean in terms of user functionality:  Ajax-enabled pages, server-side persistence stuff... it was a big app.
And it was, like 40,000 lines of code, including the templates and the client-side JavaScript.  The whole thing!  OK?  I mean, you add in unit tests, you know, you add in everything, including build files and stuff, and this thing was up to like, maybe 55,000 lines of code.
*Thousand*
.
I mean, Java programmers would be saying, "We haven't hit 55 million yet.
*(Looking at feet)*
But, well... we're gonna."
*(laughter)*
And it's like, I tell 'em that
*(shaking head)*
, I tell 'em that, and they're like:  "Well."
*(avoiding eye contact)*
That's what they say.  "Well."
And that's, you know, that's pretty much it.
*(laughter)*
**Behind the Rhino**
So unfortunately we have thirteen minutes left.  I'm sorry.  So let's really quickly go through some of the really cool things about Rhino, the technology here.
You can JavaScript from Java, and Java from JavaScript.  Guess which one's easier?
Obviously calling Java from JavaScript is easier, because Java's really cumbersome.  It doesn't have anything to help you, so you have to do basically what I was talking about with Swing earlier.
You know.
You've got all this
*stuff*
on the Java side.  'cuz it's Java.
But, uh... but it works!  And you can do both directions.  Here's an example of a Java program to bootstrap... actually I believe this is completely standalone; it works out of the box.  It's a Rhino Demo:
This is what you need to do to create a JavaScript object called
that has a function called
.  A property called "
", sorry, whose value is "hello".
So what you do is you call
, which sets up the JavaScript runtime.  You only have to do it once.  And then you call
to create a new JavaScript object.  And then you call
to evaluate it in the context of this object.
It's one example of how you do it, but it's not too hard.  You can call back and forth.
So that means that anything that was written in JavaScript that you feel, oh Gosh this really needs to be componentized, you need to stick it down in a Java library for whatever reason:  you can do it!  You can migrate code back and forth between the JavaScript layer and the Java layer.  This is true for all JVM languages, I think.
Uh... this is the actual code that I was referring to earlier, where you can define non-enumerable properties.  I called it
.  There's some closure stuff going on here... I don't want to bore you guys.
*(Editor's note:  `Function.bind()` based on Douglas Crockford's original)*
Runtime delegation:  this is one of the reasons unit testing is really easy.  You guys know about Smalltalk, uh, method-missing?  [
actually]  It's
in Ruby.  It's the... if you call an object — I think Objective C
[probably has something like this too](http://en.wikipedia.org/wiki/Objective-c#Forwarding)
.
You call an object, and you say:  "I'm calling
", and it says:  "I don't have a
".  Right?
Normally, what happens when you do this?  In Java it goes *BARF*.  As it should, probably...
*unless*
what you really wanted to do was delegate to some other object.  Right?  "Design Patterns".  Say you want to write a Bridge that says:  "Oh!  You're calling
, but you don't want to call it on me.  You want to go to the game server, call it there, marshal it, send it back.  We'll pretend it's a remote method call."
Right?  There's a lot of stuff you've got to go through in Java to do stuff like this.  In JavaScript — as you all know, if you're using dynamic languages...
Man, we've got a huge pool of people in the back.  It's getting pretty rough.  But we're almost out of time!  Fortunately.  Heh.
OK, so let me tell you a little bit about embedded XML.  It's kind of interesting, kinda neat.  This is supported in Firefox, in some browsers.  It's a spec that Adobe and some other people,
[BEA, put together](http://en.wikipedia.org/wiki/E4X)
.
And it's cool!  Because you can say stuff like
Now of course there's this weird, big religious debate going on, between JSON advocates and XML advocates.  It's weird!  They're, like, locking horns.
When I was a kid — when I was a kid, jeez...  When I was
*twenty*
, it feels like when I was a kid — I used to have tropical fish.  And my brothers and I noticed two things about tropical fish.
One is that they die, because we're not in the tropics.
*(some laughter)*
Sad.
And the other is that if you put a bunch of different species of tropical fish in a tank together, they ignore each other... except for the ones that are the same [or nearly the same] species.  They bite each other.  That's what they do.  Fish bite each other.  They have a pecking order, right?
JSON and XML are muscling in on each others' space, and there are bristles, OK, and it's so silly!  It's silly.  The whole thing, right?  I mean, XML is better if you have more text and fewer tags.  And JSON is better if you have more tags and less text.  Argh!  I mean, come on, it's that easy.  But you know, there's a big debate about it.
Nevertheless, sometimes XML is appropriate [in JavaScript], especially if you're loading it from a file or whatever.  These literals are interesting.  And so it provides new operators and new syntax for actually going in and... it's kind of like XPath.  Except it's JavaScript-y.
And I tell you:  it is the worst documented thing on the planet!  It's horrible, man, working with E4X initially.  But... eventually you can figure it out.  And I have a document that hopefully I'll be ready to release pretty soon, that actually covers it pretty well.  And Adobe has some good documentation for it.
And then eventually it clicks, like learning any other language.  This is a minilanguage.  And you go:  "Ha, I get it!  I get it.  It's not as crazy and dumb as I thought.  It actually works."
It's kind of a neat feature.  You guys know other languages that embed XML?
[Scala does](http://www.ibm.com/developerworks/library/x-scalaxml/)
.  I don't see all of you using that, but C# 3, I think, does XML?  Coming [soon]?
*(Editor's note:  it's apparently been deprioritized by the C# team, although VB 9 has them.)*
Anyway, it's kind of an interesting approach.
**Inside the Rhino**
All right.  So this is Rhino.  Now you know.  After I explain this diagram, you'll know what you need to know about Rhino to talk to other people about it.
You start with some JavaScript code.  It goes to a parser.  That turns it into a tree.  A syntax tree.
Rhino's parser today, currently, immediately begins the next step of rewriting it as code generation.  Right away, as it's parsing.  Now this is a problem.  Because if it takes an if-statement or a switch-statement or a for-loop, and it generates sort of assembly-language like jumps to targets?  And generates labels, you know, converts it into sort of three-address code, that's eventually going to actually become three-address code:  assembly or bytecode.
Then it kind of sucks if you're trying to use the parse tree for your IDE.  To, like, syntax highlight, or pretty-print, or show errors and warnings, or whatever.  Unfortunately a lot of languages — most languages — do this because they're written by compiler guys and compiler gals.  And they don't see the value.  But unfortunately we're all doing more and more processing of code.  Language tools, right?  Frontend stuff.
So I rewrote Rhino's parser recently, and I'm currently fixing the code generator.  And I'm gonna get it out into the Rhino mainstream in a couple of weeks here.  Because my project at Google is doing a lot of code processing.  And it's a faithful representation.  So if your big beef about Rhino is that there's no Visitor over the AST:  I'm fixing that.
And then there are two paths here:  you see one on the left that goes code generator to bytecode.  And there's the bytecode, or pseudo-bytecode, for the JavaScript code up there.  And then it goes to an interpreter.  The interpreter is a big loop.  Bytecode is this [roughly] postorder traversal of the tree, that flattens it in a way that allows you to push onto a stack to evaluate the operands.
It's all actually very important; you should go
[read up on how it works](http://en.wikipedia.org/wiki/Interpreter_%28computing%29)
if you're not familiar with it, or if you've forgotten since you first learned it.
And the interpreter is actually pretty fast, because it's a loop.  There's not a lot of calling out.  I mean, there are some calls out into the runtime, but mostly it's this loop:  push, pop, push, pop.  So the JIT picks it up and can optimize it pretty well.
The reason that there's two code paths here, the reason that they wrote the interpreter — they originally had just a classfile compiler — was that compiling to a classfile is this batch/static operation, where you want it [the resulting bytecode] to be fast.  You want to do the standard, classic compiler optimizations.  You want to generate the
[control-flow graph](http://en.wikipedia.org/wiki/Control_flow_graph)
, you want to eliminate dead code, you want to do good register allocation.
In JavaScript's case, it's often possible not to generate a closure.  You can actually use Java instance variables and Java local variables instead of these heavier-weight JavaScript [activation objects].  Because at the logical level, JavaScript doesn't really even have a stack.  It has object allocations on the heap; those are your Function invocations.  Sloooow.  Right?  Because [in comparison] the Java stack translates to the C stack.
So the fact that the compiler can go through and optimize away a lot of this JavaScript dynamic stuff that's provable you're not gonna need, well, that's nice!  But it takes time.  The interpreter is a path that allows you to dynamically develop:  load code in and see how it's gonna work right now, at the unfortunate expense of the Rhino people having to maintain these two code paths.  But, you know, there's a lot shared between them.
And that's it!  The script runtime implements all the JavaScript, you know,
[Ecma spec stuff](http://www.ecma-international.org/publications/standards/Ecma-252.htm)
:
,
,
,
, the
functions.  And a lot of it just delegates down to Java where possible.
Pretty clean!  Pretty standard.  It's a pretty standard compiler, interpreter and runtime.  You're gonna see this if you dig into your favorite JVM language.  You'll probably see something similar to this.  This is actually more mature than a lot of them.  A lot of them start off by interpreting the parse tree, and it's slow from the method calls.
So this is why Rhino's fast.  Now it could be a lot faster, and we're working on it.  Hopefully, you know, these things can be as fast as Java, in the same way that Java made the claim that it can be "as fast as C++".  And for long-running applications, that's usually true.  Especially with parallelism, right?  Threads.  And especially if the JIT has a chance to look at the actual code paths being used and compile them down into machine code
*specific*
for that code path, as a fall-through.
Obviously for benchmarks, where they fire something up and run a loop a thousand times, or whatever?  C++ is faster because the JIT hasn't had any time to kick in and evaluate what's going on.  But for long-running services — which is what we're all writing, yeah?  At this Ajax conference — the JIT will kick in.  And your Rhino code now will get very close to where Java's performance is.
*(Provided you're not doing number-crunching - Ed.)*
So don't worry about that so much.
So RnR, I already talked about it.  It doesn't have a database backend yet, because we're using Google's internal store, like Bigtables.  Which is why I haven't open-sourced the thing yet.
It's weird:  somebody told me the other day, they sent me mail and said:  "I think you're today's Paul Graham".  And he meant this in the most negative connotation possible.  "You're today's Paul Graham, and RnR is the next Arc."
I was like, "What!?"  And he said, well, he's a server-side JavaScript guy.  I mean, there aren't that many, right?  Most of us are thinking client-side.  But he's a server-side JavaScript guy.  And he goes to people and says, why aren't you using server-side JavaScript?  And they say:  "We're waiting for Steve Yegge to release RnR."
And I'm... this is news to me!  I'm working on... stuff, you know.  Work.  And this [open-sourcing RnR] is part-time and everything.
This year, now that we know people are interested in it, we will release it.
*(At least we'll try for this year - Ed.)*
It's just a little weird, right?  Because Sun hired the JRuby guys, and they're doing
, and it's eventually going to be part of the Java Development Kit.  It's gonna be, you know:  it's Sun's lightweight answer to EJB and all those giant frameworks.  You want to build something quickly and use the Rails model, well, run Rails on the JVM!
So I thought:  if JRuby on Rails had been (a) ready when we started using it [i.e. writing RnR], and (b) Google would let me use Ruby, then I would have used that!  So RnR was like a transitional thing.
But... again, you know, I think that there are other people in situations where you really prefer to use JavaScript.  So yeah, I guess I'll... open-source it.  We're working on it.
This is the last slide, by the way; I know you guys are tired.  We're doing a lot of work on it.  I'm working on it personally, I mean working on Rhino.  Because I think it's all right.  I'm used to JavaScript now, and I think it's a good implementation.  It's a good compiler, so it's good practice for me, to learn how compilers work.
We've got a debugger, but we're making the debugger better.  We've got a sandboxing model, but that could definitely be wrapped up and made available to you folks.
We'd like to open-source our JSCompiler:  the thing that compresses JavaScript for Google Maps and GMail and stuff.  I know there are some open-source ones out there.  We don't think that it's competitively in our best interest to keep the thing internal.  It'd be better to get it out there so you all benefit from it, and so you can all hack on it, right?  We're working on open-sourcing our JSCompiler and other stuff.
So that's it!  I wanted to cover Rhino, but I also wanted to leave time for questions.  And I've left you
*(looking at big LED clock in the back)*
one minute and sixteen seconds for questions.  Sorry about that.
So really quickly, if there are any burning questions, I'll repeat the question and try to answer it.  Otherwise feel free to come up afterwards and chat.
**Q&A**
**Q:  Why won't Google let you use Ruby?**
Yeah, that's a good question.  Um... uh... I kinda
[wrote that up in a blog](http://steve-yegge.blogspot.com/2007/06/rhino-on-rails.html)
.  Isn't that stupid?  "Read my blog!"
The short answer is:  it imposes a tax on the systems people, which means that it's not completely self-contained within the team that's using it.  And for that reason, primarily, it's really not a good idea right now.
Any other burning questions?
**Q:  Do threads suck?**
Well, you know... they're... you know...  Yeah.  But I mean, what other options do you have?  I mean, you have multiprocessing/share-nothing, which is heavyweight and it requires more work.
So I use threads.  I'd prefer something better, but they're what we've got today.
**Q:  There are some guys that I work with, and one of their comments on JavaScript lately, since I've been wanting to use Rhino because I love JavaScript... what they brought up is that JavaScript is becoming a lot like Python, and that may or may not be such a great thing.  I wanted to know what you have to say about that.**
Ah.  OK.  Well, yeah, it already has borrowed some stuff from Python in
[JavaScript 1.7](http://developer.mozilla.org/en/docs/New_in_JavaScript_1.7)
:
, Array comprehensions, destructuring assignment.  And these are good features.  They're good.  They're not going to change it to be syntactically whitespace sensitive, right?
I don't know.  The guys working on it have really taken off in completely different directions from Python.  They're looking at an optional static type system, so in that sense it's maybe more like Groovy.  And they're looking at maybe fixing some of the bugs.
But I don't know how that's going to evolve yet.  Because there's obviously a lot of people who have skin in the game, a lot of people interested in affecting the way the spec evolves.  So it's all kind of up in the air right now.
All right, so we're really out of time.  I'd like to thank you for coming.  And please come up afterwards.  Thanks!