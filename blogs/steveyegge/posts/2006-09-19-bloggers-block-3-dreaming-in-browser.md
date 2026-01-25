---
title: "Blogger's Block #3: Dreaming in Browser Swamp"
date: 2006-09-19
url: https://steve-yegge.blogspot.com/2006/09/bloggers-block-3-dreaming-in-browser.html
word_count: 4803
---

*Part 3 of an N-part series of short (well, fast, anyway) posts intended to clear out my bloggestive tract.*
I've been doing a lot of JavaScript and DHTML and AJAX programming lately.  Increasing quantities of it.  Boy howdy.  The O'Reilly DHTML book has gotten big enough to crush a Volkswagon Bug, hasn't it?  And my CSS book has gone from pristine to war-torn in under a month.  I've managed to stay in the Dark Ages of web programming for the past 10 years: you know, HTML, a little CGI, font color="red".  Way old school.  And now I'm getting the crash-course.  The more I learn, the more I wish I'd known it for longer.  Although then I'd have had to live through the long transition from Dark Ages to the muchly-improved situation we have today.  Far from
*good*
, to be sure, but it's improved dramatically since last I looked.
JavaScript is probably the most important language in the world today.  Funny, huh?  You'd think it would be Java or C++ or something.  But I think it just might be JavaScript.
For one thing, despite JavaScript's inevitable quirks and flaws and warts and hairy boogers and severe body odor, it possesses that magical property that you can get stuff done really fast with it.  Well, if you can find any halfway decent tools and libraries for it, that is.  Which you can't, not without effort.  But the situation is improving.  Slow and steady wins the race and all.  JavaScript is definitely the tortoise to Java's hare.
See, JavaScript has a captive audience.  It's one of those languages you just have to know, or you get to miss out on Web programming, and in case you hadn't noticed, thick clients are like Big Hair these days.  Most non-technical people I know pretty much live in their browsers, and they only emerge periodically to stare in puzzlement at iTunes or a game or something, and wonder
*why isn't it in the browser*
, because everything else useful seems to be.  It's where the whole world is.  To non-technical people, of course.  Which is, like, practically everyone.
We technical folks like to eye browsers with suspicion, and for a good reason.  They're not platforms.  They're sort of like platforms, but they're missing all this
*stuff*
you normally expect from platforms.  The DHTML book (which covers pretty much the only semi-reliable intersection of the browser platforms) is, for all its massive size, still just one book, and any platform worth its salt will need a whole shelf.
It turns out if you dig deep into Mozilla (aka Netscape, aka Firefox, aka SeaMonkey, aka SwampMonster, I mean the thing really has way too many farging names already), you'll find that it actually
*is*
a relatively full-featured platform.  It's not quite as general-purpose as an OS (or Java), but it's certainly big and hairy enough to be making threats in that general direction.
But my God, it's
*sooooooo*
ugly.  It's got well over a decade of ugly packed in there.  "Hello, World" in Mozilla is six or seven files in as many different languages.  I kid you not.  It's worse than Hello, World was back in the Petzold days of Win32 programming.  You have your XUL file and your JavaScript file and your CSS file and your manifest.rdf and your i18n.something and I can't remember what all else.  And then you have to build them together (using some
*other*
files) to make even
*more*
files: a JAR file and an XPI file at a minimum.  That's one gnarly-ass introductory program.
Me, I kinda prefer Python's version:

```
print "Hello, world!"
```

Color me silly with font="red", but it just seems cleaner to me.
And then when you try to graduate from Hello, World to something that seems like it should be only epsilon more difficult, like, say, "Get me a list of the user's bookmarks", you officially launch off into this eerie XPCOM world where you have to write dozens and dozens of lines of JavaScript code that looks
*nothing at all*
like you'd imagine it should, if you closed your eyes and thought to yourself: "I wonder what the JS code for getting bookmarks would look like?"
Look, I'll even show ya:

```
/** * Returns a sorted list of bookmark objects.  Each object * has properties name, url, and (optional) kw. * @return bookmark list:  an array of anonymous objects, each * with "name", "url" and "kw" fields.  Sorts the list by name * if sort is true. */function getBookmarkList(doSort) {  var rdf = Components.classes["@mozilla.org/rdf/rdf-service;1"].    getService(Components.interfaces.nsIRDFService);      var bmks = rdf.GetDataSource("rdf:bookmarks");  var NC_NS = "http://home.netscape.com/NC-rdf#";  var kwArc = rdf.GetResource(NC_NS + "ShortcutURL");  var urlArc = rdf.GetResource(NC_NS + "URL");  var nameArc = rdf.GetResource(NC_NS + "Name");  var rdfLiteral = Components.interfaces.nsIRDFLiteral;  var e = bmks.GetAllResources();  var items = [];  while(e.hasMoreElements()) {    var r =  e.getNext().QueryInterface(        Components.interfaces.nsIRDFResource);    var urlR = bmks.GetTarget(r, urlArc, true);    var kwR = bmks.GetTarget(r, kwArc, true);    var nameR = bmks.GetTarget(r, nameArc, true);    if (!(nameR && urlR)) {      continue;    }    var item = {};    item.name = nameR.QueryInterface(rdfLiteral).Value;    item.url = urlR.QueryInterface(rdfLiteral).Value;    if (kwR) {      item.kw = kwR.QueryInterface(rdfLiteral).Value;    }    items.push(item);  }  if (doSort) {    items.sort(function(a, b) {        return (a.name.upcase() < b.name.upcase()) ? -1 : 1;      });  }  return items;}
```

Shouldn't there be a "getBookmarks()" in there somewhere?  I mean, what
*is*
all that crap?
Admittedly this function does a
*little*
extra, what with the sorting, but that's only 5 lines of code, because JavaScript came with
[verbs](http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html)
included, thank you so much Brendan.  And those 5 lines are actually fairly sane; I mean, you can read them and say "hey, that's sorting!"  But as the rest of the code, what we seem to have is a serious failure to separate infrastructure from business logic.  We're trying to take the patient's temperature here, and they're making us saw the poor guy open and grub around in his intestines looking for the right spot to stick the thermometer.  So to speak.
In any case, that's not really JavaScript's fault; it's Firefox's fault.  I have trouble keeping them separate in my head sometimes, because I, unlike the rest of the Free World, have the balls not to support Internet Explorer.  For my personal stuff, anyway.  (Or so I believe at the moment.  Time will tell.)
That's what's really holding JavaScript back, you know.  And it's holding back CSS, and DOM, and all the other standards.  We have this little impasse problem.  You know the song and dance: Microsoft didn't want Netscape to be a competing platform, so they built IE and gave it away for free, and for a brief while they even had a better product, so they captured enough market share.
And then... nothing.  Oh, sure, they've made a few half-assed attempts to make IE standards-compliant, sort of, but only after making many full-assed attempts to distort those standards to give Microsoft competitive advantages.  I've heard that directly from folks working on the relevant teams over there.  Microsoft cheerfully shows up at the standards meetings to make
*damn sure*
they screw up the APIs for everyone else.  You know.  Microsoft-style.  Sorta like how DirectX was bugly compared to OpenGL.  Or Win32 compared to *nix.  Or MFC compared to any sane object system (e.g. TurboPascal and TurboC).  Or COM compared to CORBA.  (I mean, you have to work
*hard*
to be worse than CORBA.)  Microsoft has always been awful at making APIs, always always always, and I've decided over the years to credit this to malice rather than incompetence.  Microsoft isn't incompetent, whatever else they might be.  Burdened, yes; incompetent, no.
Why am I talking about them side-by-side with JavaScript?  Because the standoff between Microsoft and the Forces of Neutrality (open standards and the like) is the main thing that's holding JavaScript back.  Nobody wants to build an amazingly cool website that only works in FireFox/Opera/(insert your favorite reasonably standards-compliant browser here).  Because they're focused on the short term, not the long term.  It would only take one or two
*really*
killer apps for Mozilla to take back the market share from Microsoft.  That, or a whole army of pretty good ones.  People don't like downloading new stuff (in general), and they also don't like switching browsers.  But they'll do it if they know they have to in order to use their favorite app.
Everyone knows all this; not a jot of it is news to anyone, but nobody wants to be the one to make a clean break from IE.  It might bankrupt them.  Great app, nobody sees it, company goes bust.  So the killer apps will have to come from the fringe, the margin, the anarchy projects engineers do on the side — at least at companies where engineers have a little free time for innovation.  Excepting only go-for-broke startups, most places can't (or won't) bet the farm on a Firefox-only application.  So even though the spec is moving forward, or maybe sideways, DHTML in the real world has been in near-stasis for years.
In any event, the whole MSIE standoff isn't the only thing holding JavaScript back.  There are definitely other contributors.
One big problem is that it's JavaScript.  Nobody wants to use
*JavaScript*
.
I'm serious.  It's not that it's a bad language (it's not); it's just not the language
*they*
want to use.  You know.  Them.  You.  Everyone who has a favorite programming language.  Most people only want to use one, their favorite, whatever they're best with, and when they switch to a different one, they're slower.  They feel stifled, held back, uncomfortable.  That feeling goes away in under a month of immersion in a new language, but most engineers begrudge that time fiercely, probably because they don't realize it's only a month.
So many folks who take a stab at browser programming wind up saying "oh GOSH, why can't I use BLUB, man this really SUCKS!"  and then instead of writing their killer web app, they go off and write some lame-ass toolkit that compiles their language into JavaScript, or tries to be a Firefox plugin, or tries to be a Frankensteinian compiled-together monstrosity like Apache and mod_perl was.
The funny thing is, they wouldn't be gaining a damn thing with a new language, except
*maybe*
libraries, but even that's somewhat doubtful.  The standard library and runtime for
*any*
respectable general-purpose programming language are pretty big: definitely too big to expect everyone in the world to download.  And that's the problem.  You'd have to get everyone to do it.  Might as well work on your own browser at that point.  Oh, you can bet a bunch of people run off to do that, too, utterly overlooking the fact that nobody will use it even if it's great (like Opera), because it's not the browser they're accustomed to, and it has no killer app.
But if they wrote a killer app... oh, but that would have to be in JavaScript...  well, maybe we can come up with a way to write it in XYZ instead!  That's right — a bunch of would-be web app programmers are stuck in a vicious circle trying to break into a market that has one of the weirdest monopolies in history: IE (and to a tiny extent, Firefox and Safari: the Dr.  Pepper and RC Cola of browsers, respectively) maintains its monopolistic lock not through overt control, but through apathy on the part of users worldwide.
And that apathy extends to the browser makers themselves.  Microsoft and Apple have no reason to try to make their browsers competing platforms; quite the opposite in fact.  So almost no innovation happens in IE and Safari, compared to the innovation (in Apple's case) or purchase and/or me-tooing of other innovations (in Microsoft's) going on outside the browser groups at those companies.
OK, but what about Firefox?  Why don't they, you know, innovate?  Well, they're trying, I think, but for what I'm guessing are probably tangled historical reasons — which manifest as the developers often being gridlocked politically — Mozilla lacks what Fred Brooks Jr. calls "conceptual integrity" in his classic "The Mythical Man-Month".  [Which, incidentally, remains today the most vitally relevant book on software engineering, over 30 years after it was written.]  The Mozilla folks would have to do a
*lot*
of serious re-thinking in order to reduce XUL's "Hello, World" down to a few lines of code in a single language.  And I'm not convinced that kind of thinking is happening in the Firefox camp right now.  It's not that they're not thinking
*at all*
; don't get me wrong.  They're just not thinking about radical, revolutionary user-level simplifications to the basic framework.
Like, the kind of radical simplification
[Ruby on Rails](http://www.rubyonrails.org)
introduced for server-side web programming.  Yeah, yeah, I know, you hate Ruby because it's not the language you learned at your mother's teat, for God's sake.  Despite Ruby's near-perfect Conceptual Integrity Index, you'd sooner quit your job and become a sanitation engineer than spend a day or three just learning the language and being done with it.  But whatever your feelings on Ruby,
*Rails*
has caused a huge stir, because it took something that everyone assumed had to be ugly now and for all time, and it built layers and scaffolding on top that smoothed over a tremendous amount of that ugliness.  Made it almost purty, even.
Rails — now
*that's*
the kind of simplification I'm talking about.  Screw all the XML minilanguages (XUL, XBL, X*L).  Screw the RDF.  You need to be able to do
*everything*
in JavaScript.  JSON is just good enough and parseable enough and language-interoperable enough to replace all of them.  For that matter, screw CSS.  I don't mean the CSS spec, not the relatively elegant constraint system they have in place; I just mean the CSS syntax, since it's one more language piled onto the heap.  The whole selector minilanguage is nifty, but does it
*really*
need to be different from XPath?  I mean, aren't they both doing path expressions to select things in the DOM?  Jeez!
Am I spouting heresy or common sense here?  It depends who you're asking.  There are a
*lot*
of "web developers" in the world.  Lots and lots.  And they, my friends, are the last thing holding JavaScript back.
Because nobody wants to be a web developer.  No self-respecting, rootin'-tootin', core-dump-debugging
*programmer*
wants to be one, anyway.  That's sissy stuff.  That's what most non-web programmers think, whether they use Java or C++ or C# or Perl or Python or Haskell or what-have-you.  There's a deep-seated cultural perception problem in our industry about this, and I think it has a lot of root causes.
One cause, and let's be honest here, is that a lot of web developers were self-taught, weaned from text to HTML to onclick="foo.hide()" and onwards to CSS and DOM and more complex JavaScript, and thence on to CGI and PHP and VB and ActiveX and SVG and Flash and the rest of the gigantic mess of barely-interoperable languages we have to work with for web programming,
*not one of which*
covers the whole spectrum the way C++ or Java does.  You have to mix and match them (always poorly) in order to achieve some effect that usually would have been trivial using a thick-client framework.
So we really have two reasons at play here: one is that web developers mostly taught themselves, which means they're generally not very good at what "real" programmers of course consider "real" programming, so diving into web programming hasn't been considered very glamorous, nor a very good career move.  The other is that the field is so littered with new, ugly languages and technologies (again, not one of which is a turn-key solution) that most folks who
*do*
try it wind up fleeing.
I mean, I'm all in favor of MVC, but I think Common Sense and its kissing-cousin Conceptual Integrity will both tell you that M, V and C don't need to be three separate languages.  And the manifest and build information needn't be a fourth and fifth, respectively.  And i18n a sixth.  And the XPCOM system services an effective seventh.  And the server-side languages Nth through Zth.  It just doesn't make any sense.
Which is in no small part why you keep hearing about Ruby on Rails, even though you really just wish it would go away so you don't have to learn it.  Rails has the laws of physics (or at least economics) on its side.  Rails is like one of those bizarre
[tunnel diodes](http://en.wikipedia.org/wiki/Tunnel_diode)
, where the electrons on one side of the barrier
[tunnel](http://en.wikipedia.org/wiki/Quantum_tunneling)
to the other side
*without traveling the distance in between*
(at least in the classical-mechanics sense of "traveling").  They just sort of appear on the other side, instantaneously, because being on the other side is a lower quantum energy state, and tough shit if you don't like it.
People want Rails to go away because it has Ruby in the name: you can't use it like a library, nooooo, it has to be in some other language, and other languages are bad by axiomatic decree.  Programmers are lazy: they've found that the greedy algorithm gets them there with the least energy expenditure most of the time, and switching languages requires much more energy than integrating a new library, no matter how godawfully complex and ultimately useless the library is.  Which is why the Java community is thrashing around with like 50 competing frameworks for server side web programming.  Oh, and the Python community too.  And, um, all of the rest of them too.
Well, if you happen to be doing web programming, Ruby on Rails defies classical language mechanics by actually being a lower energy state.  That's right; it's
*more lazy*
to learn Rails than it is to try to get your web framework to be that productive, so people are just tunneling over to it like so many electrons.
This phenomenon
*will*
happen in the browser space.  I can assure you it will.  It's an economic certainty.  There's money at play here, lots and LOTS of money; every company in the world wants a cool website.  Not just a cool website; they want cool apps.  Companies are realizing — glacially, yes, belatedly, yes, but inexorably — that most people with computer access in the world today live inside their browser, and they'd prefer not to leave it.
"Everyone in the world" — that's an awful lot of money at stake.
So as soon as "Scheme on Skis" or "JavaScript on Jets" or whatever comes along, that Rails-like radical simplification of the huge ugly Browser Swamp, the game will change almost overnight.
I'm not sure exactly how it'll pan out.  Rails is basically a big code generator, a big compiler, in a sense.  The "language" is Rails itself — there's precious little actual Ruby in a Rails app, surprisingly enough, although there's tons underneath — and the target platform is the Browser Swamp.  It's not a seamless abstraction; you still need to know CSS and HTML (at least), and you need to know a fair bit about HTTP and relational databases and web servers and all that crapola you need for "Hello, World" on the web.
But maybe that was the right choice.  Maybe if DHH had defined an entire DSL for web programming in pure Ruby, with
*all*
the DHTML auto-generated, it wouldn't have been as popular.  In the long run, I think the pure-Ruby approach (or pure-
*anything*
, as long as it's a single language that supports declarative programming, which rules Java out) is economically superior, because there's less to learn, and more purchase for optimizations, error-checking and the like.  But in the short term, meaning today, the hybrid approach seems to be doing well.
The alternative to a Rails-like multi-language hybrid is to do the whole ball of wax in a single language.  Lisp and Scheme folks have, of course, warmed to this idea, and they all write macros that generate HTML, which winds up being way cleaner than you might guess.  But not many frameworks have taken the approach of generating
*all*
the JavaScript.  The
[GWT](http://code.google.com/webtoolkit/)
is one, of course, but you'd have to be a pretty doggurn die-hard Java programmer to go that way.  I'm sure it'll improve with time, but the biggest stumbling block, amusingly enough, is that it's
*not JavaScript*
.  JavaScript is still King in the browser space, and ironically it's like programming to the "bare metal" compared to using a Java-to-JavaScript compiler.  So JavaScript what the "real" web programmers prefer to use.
And we've come full circle.
Isn't this great?  Me, I'm loving it.  Yeah, it's a crap sandwich and we all have to take a bite.  But it's also a greenfield opportunity, a land rush, a high-energy state just dying to become a low-energy state.  Who's going to solve it?  What will the solution look like?
One option I haven't really discussed is the incumbent: maybe the standards committees will eventually evolve cross-browser support into a platform that
*doesn't*
drive most programmers into I'll-write-my-own-dammit frenzies.  I mean, it's a LOT better than it was in 1997.  Look at
[Google Spreadsheets](spreadsheets.google.com)
or
[Writely](http://www.writely.com)
or
[GMail](http://www.gmail.com)
or
[Google Maps](http://maps.google.com)
(anyone notice a pattern here?) — would any of these really have been possible in 1997?  Heck, I doubt it: they're barely possible today.  But they make it pretty obvious which way thick clients are headed, don't they?
Hang on — you're not still a thick-client programmer, are you?  Oh dear.  You'd better get yourself a DHTML book and an AJAX book, and right-quick.  Oh, you're above that client stuff, you're a server-side programmer then, are you?  Bully for you!  I don't blame you.  I hid there for many years myself; server-side is a haven of sanity, isn't it?  But I think you'll find that adding web programming to your skills lineup will go a long way; you'll be able to wire up those nifty backends you're writing in ways that real-live people will appreciate.  Like, say, your family.  And real employers too.  They like the web.  There's money there.  So DHTML/AJAX a great Mixin skill; it complements just about anything else you know how to do.
Anyway, I've pretty much belched out the barest outlines of my browser-ish thoughts for today: just enough for a blog entry, so I'll wrap up.
Ooooh, and it's a Blogger's Block entry!  This Blogger's Block series has been great for the ol' creative juices.  Just write about whatever you want, no worries, and it all flows nicely.
The only thing that could
*possibly*
go wrong is me reading the comments.
**What?**
I had a realization last night as I was juuuust falling asleep.  The realization I had was that I have all my realizations just as I'm falling asleep.  Or just as I'm waking up.  There's something magical about that time, and I think I know what it is.
I think you (or at least "I", but I think maybe "we") are highly creative when we're nearly asleep because all the pressure's off.  You can't go to sleep if you're under a lot of pressure — not easily, at any rate.  Nobody can follow us into our dreams, so we go there alone, and when you're alone with yourself, you can
*be*
yourself.  We've put shields in place to prevent us from saying or doing stupid things in public, and those shields come down when we're asleep.
That's why you always have those amazing dreams that you want to write down in the morning, the ones that would make a great movie screenplay or spy-thriller novel.  Your mind is in a creative frenzy, and you mostly suppress it during the day.
Well, you can't say stuff in a public blog without getting some criticism, which is why most employees at most companies (that's
*you*
, an all likelihood) are reticent to try it.  There's not much to be gained, and a lot of potential downside.  People have been fired over their blogs, for instance, although those are relatively rare cases, and the blogger in question is almost invariably a jackass.  For most bloggers it's more subtle.  If you're speaking in a public forum
*and*
sufficient people appear to be listening, then it's hard not to be perceived as a spokesperson (of sorts) for the company.  Scoble's the canonical example, but you can easily find others who fit the profile.
If your company has an ad-hoc, out-of-band, quasi-pseudo-spokesperson on the loose, the person is a risk.  Sort of.  I mean, it's lose-lose.  If the person is cheerleading, well, nobody likes a fanboy.  (It's a truly ugly word, isn't it?  "Fanboy" is the new F-word.)  If it's badmouthing, well,
*that's*
not too cool either.  But hey, one person's fawning is another person's badmouthing, right?  There are two sides to any interesting opinion (otherwise it's not going to be very interesting), so anything a blogger says in public is going to be criticized by some percentage of the readers.  So no matter what, the company the blogger works for is taking some indirect heat, and it's risky to hope that the positive side of the blog, if any, will make up for it.
Well then.  That's why bloggers like me always have to give you the following disclaimer: I don't speak for Google.  Not even a little bit.  For the reasons I've outlined above, the best I can really hope for is that they choose to look the other way when I blog.  It's the best any blogger can hope for.  It's what I'm hoping for.
I'm a frigging Google fanboy, though; that's going to be really hard to hide, so I'll just be honest with you.  F-word, I hate that F-word.  But it fits in this case.  I'll try my best to be objective.  Google's a terrible place to be when you're on a diet, for instance.
In any case, my sleepy realization has effectively solved my Blogger's Block problem.  I couldn't write because I was too worried about what other people (i.e., you) would think.  Yeah, I care about you too much.  You!  I think that gradually piled on resistance, and it was getting harder and harder for me to write past it.  You can see it pretty clearly in the "Clothes for the Soul" post, which I don't care all that much about — it was just a thought-exercise, after all, and was supposed to be fun.  But then I got all defensive at the end, which made commenters all defensive, and I made a mess, all because I was trying so hard to avoid criticism.
So the solution is simple: I won't read the comments.
ZZZZZzzzzzzzooooooooompf — and just like that, in a flash, I'm alone with my thoughts.  Amazing.  Really.  I can feel a chill; it's like I didn't know I was in a haunted house until all the ghosts left, all at once.
La la la, La la la, I can say whatever I want, and I needn't know 'til I'm dead what anyone else thought of it.  Nobody mentions my blog at work, by and large, since it's awkward to do so. (I assume this is the case for all bloggers — we don't have any cultural conventions for it, so it's like the third time you pass someone in the hall and you both carefully avoid eye contact.)  So if I don't read the comments, then I really
*am*
alone with my thoughts.
That's how I was able to write some of my more interesting things back at Amazon; initially nobody read my blog, so I was writing for an audience of at most about 5 people, and then only if I pestered them to read it, which I almost never did.
So no reading comments.  My blogs may not be any better for it, but I'm sure I'll be much happier.  Oh, you can bet I'll be tempted.  Maybe I won't be able to resist.  Must... *pant* ... resiiiiist... augh!  But I think I'll be able to hold out.  Why?  Because for this entire entry I've felt like I'm just about to fall asleep.  Well, that's because I
*was*
; it's been a long day, and I didn't start until 1am, and it's 4:30am now.  So yeah.  Sleeeep.
But it's a nice feeling.  Much nicer than the Russian Roulette of reading the comments on my blogs.  "Uh-huh, uh-huh, yep, *BANG* aaaaah!" <blood pressure shoots up to 190/150>.  High blood pressure is a recipe for some pretty questionable blogging, I think, and it's not too good for your health, either.
So!  Tell me what you th... er, tell others what you think!  I'll be hiding under my desk, hoping the monsters go away.
And learn DHTML!  You won't like it, but you'll be glad all the same.
'night.

---

p.s. some light reading:


|  |  |  |  |

