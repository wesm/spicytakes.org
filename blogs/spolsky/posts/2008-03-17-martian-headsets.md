---
title: "Martian Headsets"
date: 2008-03-17
url: https://www.joelonsoftware.com/2008/03/17/martian-headsets/
word_count: 4748
---


You’re about to see the mother of all flamewars on internet groups where web developers hang out. It’ll make the Battle of Stalingrad look like that time your sister-in-law stormed out of afternoon tea at your grandmother’s and wrapped the Mustang around a tree.


This upcoming battle will be presided over by Dean Hachamovitch, the Microsoft veteran currently running the team that’s going to bring you the next version of Internet Explorer, 8.0. The IE 8 team is in the process of making a decision that lies perfectly, exactly, precisely on the fault line smack in the middle of two different ways of looking at the world. It’s the difference between conservatives and liberals, it’s the difference between “idealists” and “realists,” it’s a huge global jihad dividing members of the same family, engineers against computer scientists, and Lexuses vs. olive trees.


And there’s no solution. But it will be really, really entertaining to watch, because 99% of the participants in the flame wars are not going to understand what they’re talking about. It’s not just entertainment: it’s required reading for every developer who needs to design interoperable systems.


The flame war will revolve around the issue of something called “web standards.” I’ll let [Dean introduce the problem](http://blogs.msdn.com/ie/archive/2008/03/03/microsoft-s-interoperability-principles-and-ie8.aspx):


> All browsers have a “Standards” mode, call it “Standards mode,” and use it to offer a browser’s best implementation of web standards. Each version of each browser has its own Standards mode, because each version of each browser improves on its web standards support. There’s Safari 3’s Standards mode, Firefox 2’s Standards mode, IE6’s Standards mode, and IE7’s Standards mode, and they’re all different. We want to make IE8’s Standards mode much, much better than IE7’s Standards mode.


And the whole problem hinges on the little tiny decision of what IE8 should do when it encounters a page that claims to support “standards”, but has probably only been tested against IE7.


What the hell *is* a standard?


Don’t they have standards in all kinds of engineering endeavors? (Yes.)


Don’t they usually work? (Mmmm…..)


Why are “web standards” so frigging messed up? (It’s not *just* Microsoft’s fault. It’s your fault too. And Jon Postel’s (1943-1998). I’ll explain that later.)


*There is no solution*. Each solution is terribly wrong. Eric Bangeman at *ars technica* [writes](http://arstechnica.com/news.ars/post/20071219-ie8-goes-on-an-acid2-trip-beta-due-in-first-half-of-2008.html), “The IE team has to walk a fine line between tight support for W3C standards and making sure sites coded for earlier versions of IE still display correctly.” This is incorrect. It’s not a fine line. It’s a line of negative width. There is no place to walk. They are damned if they do and damned if they don’t.


That’s why I can’t take sides on this issue and I’m not going to. But every working software developer should understand, at least, how standards work, how standards should work, how we got into this mess, so I want to try to explain a little bit about the problem here, and you’ll see that it’s the same reason Microsoft Vista is selling so poorly, and it’s the same issue I [wrote about](https://www.joelonsoftware.com/articles/APIWar.html) when I referred to the Raymond Chen camp (pragmatists) at Microsoft vs. the MSDN camp (idealists), the MSDN camp having won, and now nobody can figure out where their favorite menu commands went in Microsoft Office 2007, and nobody wants Vista, and it’s all the same debate: whether you are an Idealist (”red”) or a Pragmatist (”blue”).


Let me start at the beginning. Let’s start by thinking about *how to get things to work together*.


What kinds of things? Anything, really. A pencil and a pencil sharpener. A telephone and a telephone system. An HTML page and a web browser. A Windows GUI application and the Windows operating system. Facebook and a Facebook Application. Stereo headphones and stereos.


At the point of contact between those two items, there are all kinds of things that have to be agreed, or they won’t work together.


I’ll work through a simple example.


Imagine that you went to Mars, where you discovered that the beings who live there don’t have the portable music player. They’re still using boom boxes.


You realize this is a huge business opportunity and start selling portable MP3 players (except on Mars they’re called Qxyzrhjjjjukltks) and compatible headphones. To connect the MP3 player to the headphones, you invent a neat kind of metal jack that looks like this:


Because you control the player and the headphone, you can ensure that your player works with your headphones. This is a ONE TO ONE market. One player, one headphone.


****


Maybe you write up a spec, hoping that third parties will make different color headphones, since Marslings are very particular about the color of things that they stick in their earlings.


****


And you forgot, when you wrote the spec, to document that the voltage should be around 1.4 volts. You just forgot. So the first aspiring manufacturer of 100% compatible headphones comes along, his speaker is only expecting 0.014 volts, and when he tests his prototype, it either blows out the headphones, or the eardrums of the listener, whichever comes first. And he makes some adjustments and eventually gets a headphone that works fine and is just a couple of angstroms more fierce than your headphones.


More and more manufacturers show up with compatible headphones, and soon we’re in a ONE TO MANY market.


****


So far, all is well. We have a de-facto standard for headphone jacks here. The written spec is not complete and not adequate, but anybody who wants to make a compatible headphone just has to plug it into your personal stereo device and test it, and if it works, all is well, they can sell it, and it will work.


Until you decide to make a new version, the Qxyzrhjjjjukltk 2.0.


The Qxyzrhjjjjukltk 2.0 is going to include a *telephone* (turns out Marslings didn’t figure out cell phones on their own, either) and the headphone is going to have to have a built-in microphone, which requires one more conductor, so you rework the connector into something totally incompatible and kind of ugly, with all kinds of room for expansion:


****


And the Qxyzrhjjjjukltk 2.0 is a complete and utter failure in the market. Yes, it has a nice telephone thing, but nobody cared about that. They cared about their large collections of headphones. It turns out that when I said Marslings are very particular about the color of things that they stick in their ears, I meant it. Most trendy Marslings at this point have a whole *closet* full of nice headphones. They all look the same to you (red), but Marslings are very, very finicky about shades of red in a way that you never imagined. The newest high-end apartments on Mars are being marketed with a headphone closet. I kid you not.


So the new jack is not such a success, and you quickly figure out a new scheme:


****


Notice that you’ve now split the main shaft to provide another conductor for the microphone signal, but the trouble is, your Qxyzrhjjjjukltk 2.1 doesn’t really know whether the headset that’s plugged in has a mic or not, and it needs to know this so it can decide whether to enable phone calls. And so you invent a little protocol… the new device puts a signal on the mic pin, and looks for it on the ground, and if it’s there, it must be a three conductor plug, and therefore they don’t have a mic, so you’ll go into backwards compatibility mode where you only play music. It’s simple, but it’s a protocol negotiation.


It’s not a ONE-MANY market any more. All the stereo devices are made by the same firm, one after the other, so I’m going to call this a SEQUENCE-MANY market:


Here are some SEQUENCE-MANY markets you already know about:

1. Facebook | about 20,000 Facebook Apps
2. Windows | about 1,000,000 Windows Apps
3. Microsoft Word | about 1,000,000,000 Word documents


There are hundreds of other examples. The key thing to remember is that when a new version of the left-hand device comes out, it has to maintain auto-backwards-compatibility with all the old right-hand accessories meant to work with the old device, because those old accessories could not possibly have designed with the new product in mind. The Martian headphones are already made. You can’t go back and change them all. It’s much easier and more sensible to change the newly invented device so that it *acts like* an old device when confronted with an old headphone.


And because you want to make progress, adding new features and functionality, you also need a new protocol for new devices to use, and the sensible thing to do is to have both devices negotiate a little bit at the beginning to decide whether they both understand the latest protocol.


SEQUENCE-MANY is the world Microsoft grew up in.


But there’s one more twist, the MANY-MANY market.


A few years pass; you’re still selling Qxyzrhjjjjukltks like crazy; but now there are lots of Qxyzrhjjjjukltk clones on the market, like the open source FireQx, and lots of headphones, and you all keep inventing new features that require changes to the headphone jack and it’s driving the headphone makers *crazy* because they have to test their new designs out against *every Qxyzrhjjjjukltk clone* which is costly and time consuming and frankly most of them don’t have time and just get it to work on the most popular Qxyzrhjjjjukltk 5.0, and if that works, they’re happy, but of course when you plug the headphones into FireQx 3.0 lo and behold they explode in your hands because of a slight misunderstanding about some obscure thing in the spec which nobody really understands called *hasLayout*, and everybody understands that when it’s *raining *the *hasLayout* property is *true *and the voltage is supposed to increase to support the windshield-wiper feature, but there seems to be some debate over whether hail and snow are *rain* for the purpose of *hasLayout*, because the spec just doesn’t say. FireQx 3.0 treats snow as rain, because you need windshield wipers in the snow, Qxyzrhjjjjukltk 5.0 does not, because the programmer who worked on that feature lives in a warm part of Mars without snow and doesn’t have a driver’s license anyway. Yes, they have driver’s licenses on Mars.


And eventually some tedious bore writes a lengthy article on her blog explaining a trick you can use to make Qxyzrhjjjjukltk 5.0 behave just like FireQx 3.0 through taking advantage of a bug in Qxyzrhjjjjukltk 5.0 in which you trick Qxyzrhjjjjukltk into deciding that it’s raining when it’s snowing by melting a little bit of the snow, and it’s ridiculous, but everyone does it, because they have to solve the *hasLayout* incompatibility. Then the Qxyzrhjjjjukltk team fixes that bug in 6.0, and you’re screwed again, and you have to go find some new bug to exploit to make your windshield-wiper-equipped headphone work with either device.


NOW. This is the MANY-MANY market. Many players on the left hand side who *don’t* cooperate, and SCRILLIONS of players on the right hand side. And they’re *all making mistakes* because To Err Is Human.


****


And of course this is the situation we find ourselves in with HTML. Dozens of common browsers, literally *billions* of web pages.


And over the years what happens in a MANY-MANY market is that there is a hue and cry for “standards” so that “all the players” (meaning, the small players) have an equal chance to being able to display all 8 billion web pages correctly, and, even more importantly, so that the *designers* of those 8 billion pages only have to test against one browser, and use “web standards,” and then they will know that their page will also work in *other* browsers, without having to test every page against every browser.


See, the idea is, instead of many-many testing, you have many-standard and standard-many testing and you need radically fewer tests. Not to mention that your web pages don’t need any browser-specific code to work around bugs in individual browsers, because in this platonic world there are no bugs.


That’s the ideal.


In practice, with the web, there’s a bit of a problem: no way to test a web page against the standard, because there’s no reference implementation that guarantees that if it works, all the browsers work. This just doesn’t exist.


So you have to “test” in your own head, purely as a thought experiment, against a bunch of standards documents which you probably never read and couldn’t completely understand even if you did.


Those documents are *super* confusing. The specs are full of statements [like](http://www.w3.org/TR/CSS21/visuren.html) “If a sibling block box (that does not float and is not absolutely positioned) follows the run-in box, the run-in box becomes the first inline box of the block box. A run-in cannot run in to a block that already starts with a run-in or that itself is a run-in.” Whenever I read things like that, I wonder how *anyone* correctly conforms to the spec.


There is no practical way to check if the web page you just coded conforms to the spec. There are [validators](http://validator.w3.org/), but they won’t tell you what the page is supposed to look like, and having a “valid” page where all the text is overlapping and nothing lines up and you can’t see anything is not very useful. What people do is check their pages against one browser, maybe two, until it looks right. And if they’ve made a mistake that just happens to look OK in IE and Firefox, they’re not even going to know about it.


And their pages may break when a future web browser comes out.


If you’ve ever visited the ultra-orthodox Jewish communities of Jerusalem, all of whom agree in complete and utter adherence to every iota of Jewish law, you will discover that despite general agreement on what constitutes kosher food, that you will not find a rabbi from one ultra-orthodox community who is willing to eat at the home of a rabbi from a different ultra-orthodox community. And the web designers are discovering what the Jews of Mea Shearim have known for decades: just because you all agree to follow one book doesn’t ensure compatibility, because the laws are so complex and complicated and convoluted that it’s almost impossible to understand them all well enough to avoid traps and landmines, and you’re safer just asking for the fruit plate.


Standards are a great goal, of course, but before you become a standards fanatic you have to understand that due to the failings of human beings, standards are sometimes misinterpreted, sometimes confusing and even ambiguous.


The precise problem here is that you’re pretending that there’s one standard, but since nobody has a way to test against the standard, it’s not a real standard: it’s a platonic ideal and a set of misinterpretations, and therefore the standard is not serving the desired goal of reducing the test matrix in a MANY-MANY market.


DOCTYPE is a myth.


A mortal web designer who attaches a DOCTYPE tag to their web page saying, “this is standard HTML,” is committing an act of hubris. There is no way they know that. All they are really saying is that the page was *meant* to be standard HTML. All they *really* know is that they tested it with IE, Firefox, maybe Opera and Safari, and it seems to work. Or, they copied the DOCTYPE tag out of a book and don’t know what it means.


In the real world where people are imperfect, you can’t have a standard with just a spec–you *must have *a super-strict reference implementation, and everybody has to test against the reference implementation. Otherwise you get 17 different “standards” and you might as well not have one at all.


And this is where [Jon Postel](http://en.wikipedia.org/wiki/Jon_Postel) caused a problem, back in 1981, when he coined the [robustness principle](http://tools.ietf.org/html/rfc793): “Be conservative in what you do, be liberal in what you accept from others.” What he was trying to say was that the best way to make the protocols work robustly would be if everyone was very, very careful to conform to the specification, but they should be also be extremely forgiving when talking to partners that don’t conform exactly to the specification, as long as you can kind of figure out what they meant.


So, technically, the way to make a paragraph with small text is <p><small>, but a lot of people wrote <small><p> which is technically incorrect for reasons most web developers don’t understand, and the web browsers forgave them and made the text small anyway, because that’s obviously what they wanted to happen.


Now there are all these web pages out there with errors, because all the early web browser developers made super-liberal, friendly, accommodating browsers that loved you for *who you were* and didn’t care if you made a mistake. And so there were lots of mistakes. And Postel’s “robustness” principle didn’t really work. The problem wasn’t noticed for many years. In 2001 Marshall Rose finally [wrote](http://tools.ietf.org/html/rfc3117):


> Counter-intuitively, Postel’s robustness principle (“be conservative in what you send, liberal in what you accept”) often leads to deployment problems. Why? When a new implementation is initially fielded, it is likely that it will encounter only a subset of existing implementations. If those implementations follow the robustness principle, then errors in the new implementation will likely go undetected. The new implementation then sees some, but not widespread deployment. This process repeats for several new implementations. Eventually, the not-quite-correct implementations run into other implementations that are less liberal than the initial set of implementations. The reader should be able to figure out what happens next.


Jon Postel should be honored for his enormous contributions to the invention of the Internet, and there is really no reason to fault him for the infamous robustness principle. 1981 is prehistoric. If you had told Postel that there would be 90 million untrained people, not engineers, creating web sites, and they would be doing all kinds of awful things, and some kind of misguided charity would have caused the early browser makers to accept these errors and display the page anyway, he would have understood that this is the wrong principle, and that, actually, the web standards idealists are right, and the way the web “should have” been built would be to have very, very strict standards and every web browser should be positively *obnoxious *about pointing them *all out to you* and web developers that couldn’t figure out how to be “conservative in what they emit” should not be allowed to author pages that appear *anywhere* until they get their act together.


But, of course, if that had happened, maybe the web would never have taken off like it did, and maybe instead, we’d all be using a gigantic Lotus Notes network operated by AT&T. *Shudder.*


Shoulda woulda coulda. Who cares. We are where we are. We can’t change the past, only the future. Heck, we can barely even change the future.


And if you’re a pragmatist on the Internet Explorer 8.0 team, you might have [these words from Raymond Chen](http://blogs.msdn.com/oldnewthing/archive/2003/12/23/45481.aspx) seared into your cortex. He was writing about how Windows XP had to emulate buggy behavior from old versions of Windows:


> Look at the scenario from the customer’s standpoint. You bought programs X, Y and Z. You then upgraded to Windows XP. Your computer now crashes randomly, and program Z doesn’t work at all. You’re going to tell your friends, “Don’t upgrade to Windows XP. It crashes randomly, and it’s not compatible with program Z.” Are you going to debug your system to determine that program X is causing the crashes, and that program Z doesn’t work because it is using undocumented window messages? Of course not. You’re going to return the Windows XP box for a refund. (You bought programs X, Y, and Z some months ago. The 30-day return policy no longer applies to them. The only thing you can return is Windows XP.)


And you’re thinking, hmm, let’s update this for today:


> Look at the scenario from the customer’s standpoint. You bought programs X, Y and Z. You then upgraded to Windows XPVista. Your computer now crashes randomly, and program Z doesn’t work at all. You’re going to tell your friends, “Don’t upgrade to Windows XPVista. It crashes randomly, and it’s not compatible with program Z.” Are you going to debug your system to determine that program X is causing the crashes, and that program Z doesn’t work because it is using undocumentedinsecure window messages? Of course not. You’re going to return the Windows XPVista box for a refund. (You bought programs X, Y, and Z some months ago. The 30-day return policy no longer applies to them. The only thing you can return is Windows XPVista.)


The [victory of the idealists over the pragmatists at Microsoft](https://www.joelonsoftware.com/articles/APIWar.html), which I reported in 2004, [directly explains why Vista is getting terrible reviews and selling poorly](http://www.nytimes.com/2008/03/09/business/09digi.html?pagewanted=all).


And how does it apply to the IE team?


> Look at the scenario from the customer’s standpoint. You visit 100 websites a day. You then upgraded to IE 8. On half of them, the page is messed up, and Google Maps doesn’t work at all.


> ****


> You’re going to tell your friends, “Don’t upgrade to IE 8. It messes up every page, and Google Maps doesn’t work at all.” Are you going to View Source to determine that website X is using nonstandard HTML, and Google Maps doesn’t work because it is using non-standard JavaScript objects from old versions of IE that were never accepted by the standards committee? Of course not. You’re going to uninstall IE 8. (Those websites are out of your control. Some of them were developed by people who are now dead. The only thing you can do is go back to IE 7).


And so if you’re a developer on the IE 8 team, your first inclination is going to be to do exactly what has always worked in these kinds of SEQUENCE-MANY markets. You’re going to do a little protocol negotiation, and continue to emulate the old behavior for every site that doesn’t *explicitly* tell you that they expect the new behavior, so that all existing web pages continue to work, and you’re only going to have the nice new behavior for sites that put a little flag on the page saying, “Yo! I *grok* IE 8! Give me all the new IE 8 Goodness Please!”


And indeed that was [the first decision](http://alistapart.com/articles/beyonddoctype) [announced](http://blogs.msdn.com/ie/archive/2008/01/21/compatibility-and-ie8.aspx) by the IE team on January 21st. The web browser would accommodate existing pages silently so that nobody had to change their web site by acting like the old, buggy IE7 that web developers hated.


A pragmatic engineer would have to come to the conclusion that the IE team’s first decision was right. But the young idealist “standards” people went nuclear.


IE needed to provide a web standards experience *without* requiring a special “Yo! I’m tested with IE 8!” tag, they said. They were sick of special tags. Every frigging web page has to have thirty seven ugly hacks in it to make it work with five or six popular browsers. Enough ugly hacks. 8 billion existing web pages be damned.


And the IE team flip-flopped. Their [second decision](http://blogs.msdn.com/ie/archive/2008/03/03/microsoft-s-interoperability-principles-and-ie8.aspx), and I have to think it’s not final, their second decision was to do the idealistic thing, and treat all sites that claim to be “standards-compliant” as if they have been designed for and tested with IE8.


*Almost every web site I visited with IE8 is broken in some way.* Websites that use a lot of JavaScript are generally completely dead. A lot of pages simply have visual problems: things in the wrong place, popup menus that pop under, mysterious scrollbars in the middle. Some sites have more subtle problems: they look ok but as you go further you find that critical form won’t submit or leads to a blank page.


These are *not* web pages with errors. They are usually websites which were carefully constructed to conform to web standards. But IE 6 and IE 7 didn’t really conform to the specs, so these sites have little hacks in them that say, “on Internet Explorer… move this thing 17 pixels to the right to compensate for IE’s bug.”


And IE 8 *is *IE, but it no longer has the IE 7 bug where it moved that thing 17 pixels left of where it was supposed to be according to web standards. So now code that was written that was completely reasonable no longer works.


IE 8 can’t display most web pages correctly until you give up and press the “ACT LIKE IE7″ button. The idealists don’t care: they want those pages changed.


Some of those pages can’t be changed. They might be burned onto CD-ROMs. Some of them were created by people who are now dead. Most of them created by people who have no frigging idea what’s going on and why their web page, which they paid a designer to create 4 years ago, is now not working properly.


The idealists rejoiced. Hundreds of them descended on the IE blog to actually say nice things about Microsoft for the first times in their lives.


I looked at my watch.


Tick, tick, tick.


Within a matter of seconds, you started to see people on the forums showing up like [this one](http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=2972194&SiteID=1):


> I have downloaded IE 8 and with it some bugs. Some of my websites like “HP” are very difficult to read as the whole page is very very small… The speed of my Internet has also been reduced on some occasions. Whe I use Google Maps, there are overlays everywhere, enough so it makes it ackward to use!


Mmhmm. All you smug idealists are laughing at this newbie/idjit. The consumer is not an idiot. [She’s your wife](http://en.wikiquote.org/wiki/David_Ogilvy). So stop laughing. 98% of the world will install IE8 and say, “It has bugs and I can’t see my sites.” They don’t give a flicking flick about your stupid religious enthusiasm for making web browsers which conform to some mythical, platonic “standard” that is not actually implemented anywhere. They don’t want to hear your stories about messy hacks. They want web browsers that work with actual web sites.


So you see, we have a terrific example here of a gigantic rift between two camps.


The web standards camp seems kind of Trotskyist. You’d think they’re the left wing, but if you happened to make a website that claims to conform to web standards but doesn’t, the idealists turn into Joe Arpaio, America’s Toughest Sheriff. “YOU MADE A MISTAKE AND YOUR WEBSITE SHOULD BREAK. I don’t care if 80% of your websites stop working. I’ll put you all in jail, where you will wear pink pajamas and eat 15 cent sandwiches and work on a chain gang. And I don’t care if the whole county is in jail. The law is the law.”


On the other hand, we have the pragmatic, touchy feely, warm and fuzzy engineering types. “Can’t we just default to IE7 mode? One line of code … Zip! Solved!”


Secretly? Here’s what I think is going to happen. The IE8 team going to tell everyone that IE8 will use web standards by default, and run a nice long beta during which they beg people to test their pages with IE8 and get them to work. And when they get closer to shipping, and only 32% of the web pages in the world render properly, they’ll say, “look guys, we’re really sorry, we really wanted IE8 standards mode to be the default, but we can’t ship a browser that doesn’t work,” and they’ll revert to the pragmatic decision. Or maybe they won’t, because the pragmatists at Microsoft have been out of power for a long time. In which case, IE is going to lose a lot of market share, which would please the idealists to no end, and probably won’t decrease Dean Hachamovitch’s big year-end bonus by one cent.


You see? No right answer.


As usual, the idealists are 100% right in principle and, as usual, the pragmatists are right in practice. The flames will continue for years. This debate precisely splits the world in two. If you have a way to buy stock in Internet flame wars, now would be a good time to do that.
