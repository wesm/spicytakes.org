---
title: "Talk at Yale: Part 1 of 3"
date: 2007-12-03
url: https://www.joelonsoftware.com/2007/12/03/talk-at-yale-part-1-of-3/
word_count: 2967
---


> *This is part one of the text of a talk delivered to the Yale Computer Science department on November 28. The rest of the talk will be published tomorrow and Wednesday.*


I graduated with a B.S. in Computer Science in 1991. Sixteen years ago. What I’m going to try to do today is relate my undergraduate years in the CS department to my career, which consists of developing software, writing about software, and starting a software company. And of course that’s a little bit absurd; there’s a famous part at the beginning of MIT’s Introduction to Computer Science where [Hal Abelson](http://www-swiss.ai.mit.edu/~hal/hal.html) gets up and explains that Computer Science isn’t about computers and it isn’t a science, so it’s a little bit presumptuous of me to imply that CS is supposed to be training for a career in software development, any more than, say, Media Studies or Cultural Anthropology would be.


I’ll press ahead anyway. One of the most useful classes I took was a course that I dropped after the first lecture. Another one was a class given by [Roger Schank](http://www.engines4ed.org/hyperbook/misc/rcs.html) that was so disdained by the CS faculty that it was not allowed to count towards a degree in computer science. But I’ll get to that in a minute.


The third was this little gut called CS 322, which you know of as CS 323. Back in my day, CS 322 took so much work that it was a 1½ credit class. And Yale’s rule is, that extra half credit could only be combined with other half credits from the same department. Apparently there were two other 1½ credit courses, but they could only be taken together. So through that clever trickery, the half credit was therefore completely useless, but it did justify those weekly problem sets that took 40 hours to complete. After years of students’ complaining, the course was adjusted to be a 1 credit class, it was renumbered CS 323, and still had weekly 40 hour problem sets. Other than that, it’s pretty much the same thing. I loved it, because I love programming. The best thing about CS323 is it teaches a lot of people that they just ain’t never gonna be programmers. This is a good thing. People that don’t have the benefit of [Stan](http://www.cs.yale.edu/people/faculty/eisenstat.html) teaching them that they can’t be programmers have miserable careers cutting and pasting a lot of Java. By the way, if you took CS 323 and got an A, we have [great summer internships at Fog Creek](http://www.fogcreek.com/Jobs/SummerIntern.html). See me afterwards.


As far as I can tell, the core [curriculum](http://students.yale.edu/oci/ycps/ycpsProgramCourses.jsp?subject=CPSC&dept=Computer%20Science) hasn’t changed at all. 201, 223, 240, 323, 365, 421, 422, 424, 429 appear to be almost the same courses we took 16 years ago. The number of CS majors is actually up since I went to Yale, although a temporary peak during the dotcom days makes it look like it’s down. And there are a lot more interesting electives now than there were in my time. So: progress.


For a moment there, I actually thought I’d get a PhD. Both my parents are professors. So many of their friends were academics that I grew up assuming that all adults eventually got PhDs. In any case, I was thinking pretty seriously of going on to graduate school in Computer Science. Until I tried to take a class in Dynamic Logic right here in this very department. It was taught by [Lenore Zuck](http://www.cs.uic.edu/~lenore/), who is now at UIC.


I didn’t last very long, nor did I understand much of anything that was going on. From what I gather, Dynamic Logic is just like formal logic: Socrates is a man, all men are mortal, therefore Socrates is mortal. The difference is that in Dynamic Logic truth values can change over time. Socrates was a man, now he’s a cat, etc. In theory this should be an interesting way to prove things about computer programs, in which state, i.e., truth values, change over time.


In the first lecture Dr. Zuck presented a few axioms and some transformation rules and set about trying to prove a very simple thing. She had a computer program “f := not f,” f is a Boolean, that simply flipped a bit, and the goal was to prove that if you ran this program an even number of times, f would finish with the same value as it started out with.


The proof went on and on. It was in this very room, if I remember correctly, it looks like the carpet hasn’t been changed since then, and all of these blackboards were completely covered in the steps of the proof. Dr. Zuck used proof by induction, proof by reductio ad absurdum, proof by exhaustion—the class was late in the day and we were already running forty minutes over—and, in desperation, proof by graduate student, whereby, she says, “I can’t really remember how to prove this step,” and a graduate student in the front row says, “yes, yes, professor, that’s right.”


And when all was said and done, she got to the end of the proof, and somehow was getting exactly the opposite result of the one that made sense, until that same graduate student pointed out where, 63 steps earlier, some bit had been accidentally flipped due to a little bit of dirt on the board, and all was well.


For our homework, she told us to prove the converse: that if you run the program “f := not f” n times, and the bit is in the same state as it started, that n must be even.


I worked on that problem for hours and hours. I had her original proof in front of me, going in one direction, which, upon closer examination, turned out to have all kinds of missing steps that were “trivial,” but not to me. I read every word about Dynamic Logic that I could find in [Becton](http://www.library.yale.edu/science/library/engineering.html), and I struggled with the problem late into the night. I was getting absolutely nowhere, and increasingly despairing of theoretical computer science. It occurred to me that when you have a proof that goes on for pages and pages, it’s far more likely to contain errors in the proof as our own intuition about the trivial statements that it’s trying to prove, and I decided that this Dynamic Logic stuff was really not a fruitful way of proving things about actual, interesting computer programs, because you’re more likely to make a mistake in the proof than you are to make a mistake in your own intuition about what the program “f := not f” is going to do. So I dropped the course, thank God for shopping period, but not only that, I decided on the spot that graduate school in Computer Science was just not for me, which made this the single most useful course I ever took.


Now this brings me to one of the important themes that I’ve learned in my career. Time and time again, you’ll see programmers redefining problems so that they can be solved algorithmically. By redefining the problem, it often happens that they’re left with something that can be solved, but which is  actually a trivial problem. They don’t solve the real problem, because that’s intractable. I’ll give you an example.


You will frequently hear the claim that software engineering is facing a quality crisis of some sort. I don’t happen to agree with that claim—the computer software most people use most of the time is of ridiculously high quality compared to everything else in their lives—but that’s beside the point. This claim about the “quality crisis” leads to a lot of proposals and research about making higher quality software. And at this point, the world divides into the geeks and the suits.


The geeks want to solve the problem automatically, using software. They propose things like unit tests, test driven development, automated testing, dynamic logic and other ways to “prove” that a program is bug-free.


The suits aren’t really aware of the problem. They couldn’t care less if the software is buggy, as long as people are buying it.


Currently, in the battle between the geeks and the suits, the suits are winning, because they control the budget, and honestly, I don’t know if that’s such a bad thing. The suits recognize that there are diminishing returns to fixing bugs. Once the software hits a certain level of quality that allows it to solve someone’s problem, that person will pay for it and derive benefit out of it.


The suits also have a broader definition of “quality.” Their definition is about as mercenary as you can imagine: the quality of software is defined by how much it increases my bonus this year. Accidentally, this definition of quality incorporates a lot more than just making the software bug-free. For example, it places a lot of value on adding more features to solve more problems for more people, which the geeks tend to deride by calling it “[bloatware](https://www.joelonsoftware.com/articles/fog0000000020.html).” It places value on aesthetics: a cool-looking program sells more copies than an ugly program. It places value on how happy a program makes its users feel. Fundamentally, it lets the users define their own concept of [quality](https://www.joelonsoftware.com/design/1stDraft/02.html), and decide on their own if a given program meets their needs.


Now, the geeks are interested in the narrowly technical aspects of quality. They focus on things they can see in the code, rather than waiting for the users to judge. They’re programmers, so they try to automate everything in their life, and of course they try to automate the QA process. This is how you get unit testing, which is not a bad thing, don’t get me wrong, and it’s how you get all these attempts to mechanically “prove” that a program is “correct.” The trouble is that anything that can’t be automated has to be thrown out of the definition of quality. Even though we know that users prefer software that looks cooler, there’s no automated way to measure how cool looking a program is, so that gets left out of the automated QA process.


In fact what you’ll see is that the hard-core geeks tend to give up on all kinds of useful measures of quality, and basically they get left with the only one they can prove mechanically, which is, does the program behave according to specification. And so we get a very narrow, geeky definition of quality: how closely does the program correspond to the spec. Does it produce the defined outputs given the defined inputs.


The problem, here, is very fundamental. In order to mechanically prove that a program corresponds to some spec, the spec itself needs to be extremely detailed. In fact the spec has to define everything about the program, otherwise, nothing can be proven automatically and mechanically. Now, if the spec does define everything about how the program is going to behave, then, lo and behold, it contains all the information necessary to generate the program! And now certain geeks go off to a very dark place where they start thinking about automatically compiling specs into programs, and they start to think that they’ve just invented a way to program computers without programming.


Now, this is the software engineering equivalent of a perpetual motion machine. It’s one of those things that crackpots keep trying to do, no matter how much you tell them it could never work. If the spec defines precisely what a program will do, with enough detail that it can be used to generate the program itself, this just begs the question: how do you write the spec? Such a complete spec is just as hard to write as the underlying computer program, because just as many details have to be answered by spec writer as the programmer. To use terminology from information theory: the spec needs just as many bits of [Shannon entropy](http://en.wikipedia.org/wiki/Information_entropy) as the computer program itself would have. Each bit of entropy is a decision taken by the spec-writer or the programmer.


So, the bottom line is that if there really were a mechanical way to prove things about the correctness of a program, all you’d be able to prove is whether that program is identical to some other program that must contain the same amount of entropy as the first program, otherwise some of the behaviors are going to be undefined, and thus unproven. So now the spec writing is just as hard as writing a program, and all you’ve done is moved one problem from over here to over there, and accomplished nothing whatsoever.


This seems like a kind of brutal example, but nonetheless, this search for the holy grail of program quality is leading a lot of people to a lot of dead ends. The Windows Vista team at Microsoft is a case in point. Apparently—and this is all based on blog [rumors](http://minimsft.blogspot.com/2006/05/copying-xerox-vista-mistakes-and-vp.html) and innuendo—Microsoft has had a long term policy of eliminating all software testers who don’t know how to write code, replacing them with what they call SDETs, Software Development Engineers in Test, programmers who write automated testing scripts.


The old testers at Microsoft checked lots of things: they checked if fonts were consistent and legible, they checked that the location of controls on dialog boxes was reasonable and neatly aligned, they checked whether the screen flickered when you did things, they looked at how the UI flowed, they considered how easy the software was to use, how consistent the wording was, they worried about performance, they checked the spelling and grammar of all the error messages, and they spent a lot of time making sure that the user interface was consistent from one part of the product to another, because a consistent user interface is easier to use than an inconsistent one.


None of those things could be checked by automated scripts. And so one result of the new emphasis on automated testing was that the Vista release of Windows was extremely inconsistent and unpolished. Lots of obvious problems got through in the final product… none of which was a “bug” by the definition of the automated scripts, but every one of which contributed to the general feeling that Vista was a downgrade from XP. The geeky definition of quality won out over the suit’s definition; I’m sure the automated scripts for Windows Vista are running at 100% success right now at Microsoft, but it doesn’t help when just about every tech reviewer is advising people to stick with XP for as long as humanly possible. It turns out that nobody wrote the automated test to check if Vista provided users with a compelling reason to upgrade from XP.


I don’t hate Microsoft, really I don’t. In fact, my first job out of school was actually at Microsoft. In those days it was not really a respectable place to work. Sort of like taking a job in the circus. People looked at you funny. Really? Microsoft? On campus, in particular, it was perceived as corporate, boring, buttoned-down, making inferior software so that accountants can do, oh I don’t know, spreadsheets or whatever it is that accountants do. Perfectly miserable. And it all ran on a pathetic single-tasking operating system called MS-DOS full of arbitrary stupid limitations like 8-character file names and no email and no telnet and no Usenet. Well, MS-DOS is long gone, but the cultural [gap](https://www.joelonsoftware.com/articles/Biculturalism.html) between the Unixheads and the Windows users has never been wider. This is a culture war. The disagreements are very byzantine but very fundamental. To Yale, Microsoft was this place that made toy business operating systems using three-decades-old computer science. To Microsoft, “computer sciency” was a bad word used to make fun of new hires with their bizarre hypotheses about how [Haskell](http://haskell.cs.yale.edu/yale/) is the next major programming language.


Just to give you one tiny example of the Unix-Windows cultural war. Unix has this cultural value of separating user interface from functionality. A righteous Unix program starts out with a command-line interface, and if you’re lucky, someone else will come along and write a pretty front end for it, with shading and transparency and 3D effects, and this pretty front end just launches the command-line interface in the background, which then fails in mysterious ways, which are then not reflected properly in the pretty front end which is now hung waiting for some input that it’s never going to get.


But the good news is that you can use the command line interface from a script.


Whereas the Windows culture would be to write a GUI app in the first place, and all the core functionality would be tangled up hopelessly with the user interface code, so you could have this gigantic application like Photoshop that’s absolutely brilliant for editing photos, but if you’re a programmer, and you want to use Photoshop to resize a folder of 1000 pictures so that each one fits in a 200 pixel box, you just can’t write that code, because it’s all very tightly bound to a particular user interface.


Anyway, the two cultures roughly correspond to highbrow vs. lowbrow, and in fact, it’s reflected accurately in the curriculum of computer science departments throughout the country. At Ivy League institutions, everything is Unix, functional programming, and theoretical stuff about state machines. As you move down the chain to less and less selective schools Java starts to appear. Move even lower and you literally start to see classes in topics like Microsoft Visual Studio 2005 101, three credits. By the time you get to the 2 year institutions, you see the same kind of SQL-Server-in-21-days “certification” courses you see advertised on the weekends on cable TV. Isn’t it time to start your career in (different voice) Java Enterprise Beans!


> *(Part two will appear tomorrow).*
