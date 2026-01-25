---
title: "Get that job at Google"
date: 2008-03-12
url: https://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html
word_count: 4710
---

I've been meaning to write up some tips on interviewing at Google for a good long time now.  I keep putting it off, though, because it's going to make you mad.  Probably.  For some statistical definition of "you", it's very likely to upset you.
Why?  Because... well, here, I wrote a little ditty about it:

```
Hey man, I don't know that stuffStevey's talking abooooooutIf my boss thinks it's importantI'm gonna get fiiiiiiiiiiredOooh yeah baaaby baaaay-beeeeee....
```

I didn't realize this was such a typical reaction back when I first started writing about interviewing, way back at other companies.  Boy-o-howdy did I find out in a hurry.
See, it goes like this:
**Me:**
blah blah blah, I like asking question X in interviews, blah blah blah...
**You:**
Question X?  Oh man, I haven't heard about X since college!  I've never needed it for my job!  He asks that in
*interviews*
?  But that means someone out there thinks it's important to know, and, and... I don't know it!  If they detect my ignorance, not only will I be summarily fired for incompetence without so much as a thank-you, I will also be unemployable by people who ask question X!  If people listen to Stevey, that will be everyone!  I will become homeless and destitute!  For not knowing something I've never needed before!  This is horrible!  I would attack X itself, except that I do not want to pick up a book and figure enough out about it to discredit it.  Clearly I must yell a lot about how stupid Stevey is so that nobody will listen to him!
**Me:**
So in conclusion, blah blah... huh?  Did you say "fired"?  "Destitute?"  What are you talking about?
**You:**
Aaaaaaauuuggh!!! *stab* *stab* *stab*
**Me:**
That's it.  I'm never talking about interviewing again.
It doesn't matter what X is, either.  It's arbitrary.  I could say: "I really enjoy asking the candidate
*(their name)*
in interviews", and people would still freak out, on account of insecurity about either interviewing in general or their knowledge of their own name, hopefully the former.
But THEN, time passes, and interview candidates come and go, and we always wind up saying: "Gosh, we sure wish that obviously smart person had prepared a little better for his or her interviews.  Is there any way we can help future candidates out with some tips?"
And then nobody actually does anything, because we're all afraid of getting stabbed violently by People Who Don't Know X.
I considered giving out a set of tips in which I actually use variable names like X, rather than real subjects, but decided that in the resultant vacuum,
*everyone*
would get upset.  Otherwise that approach seemed pretty good, as long as I published under a pseudonym.
In the end, people really need the tips, regardless of how many feelings get hurt along the way.  So rather than skirt around the issues, I'm going to give you a few mandatory substitutions for X along with a fair amount of general interview-prep information.
**Caveats and Disclaimers**
This blog is not endorsed by Google.  Google doesn't know I'm publishing these tips.  It's just between you and me, OK?  Don't tell them I prepped you.  Just go kick ass on your interviews and we'll be square.
I'm only talking about general software engineering positions, and interviews for those positions.
These tips are actually generic; there's nothing specific to Google vs. any other software company.  I could have been writing these tips about my first software job 20 years ago.  That implies that these tips are also timeless, at least for the span of our careers.
These tips obviously won't get you a job on their own.  My hope is that by following them you will perform your very best during the interviews.
**Oh, and um, why Google?**
Oho!  Why Google, you ask?  Well let's just have that dialog right up front, shall we?
**You:**
Should I work at Google?  Is it all they say it is, and more?  Will I be serenely happy there?  Should I apply immediately?
**Me:**
Yes.
**You:**
To which ques... wait, what do you mean by "Yes?"  I didn't even say who I am!
**Me:**
Dude, the answer is Yes.  (You may be a woman, but I'm still calling you Dude.)
**You:**
But... but... I am paralyzed by inertia!  And I feel a certain comfort level at my current company, or at least I have become relatively inured to the discomfort.  I know people here and nobody at Google!  I would have to learn Google's build system and technology and stuff!  I have no credibility, no reputation there – I would have to start over virtually from scratch!  I waited too long, there's no upside!  I'm afraaaaaaid!
**Me:**
DUDE.  The answer is Yes already, OK?  It's an invariant.  Everyone else who came to Google was in the
*exact same position*
as you are, modulo a handful of famous people with beards that put Gandalf's to shame, but they're a very tiny minority.  Everyone who applied had the same reasons for
*not*
applying as you do.  And everyone here says: "GOSH, I SURE AM HAPPY I CAME HERE!"  So just apply already.  But prep first.
**You:**
But what if I get a mistrial?  I might be smart and qualified, but for some random reason I may do poorly in the interviews and not get an offer!  That would be a huge blow to my ego!  I would rather pass up the opportunity altogether than have a chance of failure!
**Me:**
Yeah, that's at least partly true.  Heck, I kinda didn't make it in on my first attempt, but I begged like a street dog until they gave me a second round of interviews.  I caught them in a weak moment.  And the second time around, I prepared, and did much better.
The thing is, Google has a well-known false negative rate, which means we sometimes turn away qualified people, because that's considered better than sometimes hiring unqualified people.  This is actually an industry-wide thing, but the dial gets turned differently at different companies.  At Google the false-negative rate is pretty high.  I don't know what it is, but I do know a lot of smart, qualified people who've not made it through our interviews.  It's a bummer.
But the really important takeaway is this:
*if you don't get an offer, you may still be qualified to work here*
.  So it needn't be a blow to your ego at all!
As far as anyone I know can tell, false negatives are completely random, and are unrelated to your skills or qualifications.  They can happen from a variety of factors, including but not limited to:
1. you're having an off day
2. one or more of your interviewers is having an off day
3. there were communication issues invisible to you and/or one or more of the interviewers
4. you got unlucky and got an Interview Anti-Loop

**Oh no, not the Interview Anti-Loop!**
Yes, I'm afraid you have to worry about this.
What is it, you ask?  Well, back when I was at Amazon, we did (and they undoubtedly still do) a LOT of soul-searching about this exact problem.  We eventually concluded that every single employee E at Amazon has at least one "Interview Anti-Loop": a set of other employees S who would not hire E.  The root cause is important for you to understand when you're going into interviews, so I'll tell you a little about what I've found over the years.
First, you can't tell interviewers what's important.  Not at any company.  Not unless they're specifically asking you for advice.  You have a very narrow window of perhaps one year after an engineer graduates from college to inculcate them in the art of interviewing, after which the window closes and they believe they are a "good interviewer" and they don't need to change their questions, their question styles, their interviewing style, or their feedback style,
*ever again*
.
It's a problem.  But I've had my hand bitten enough times that I just don't try anymore.
Second problem: every "experienced" interviewer has a set of pet subjects and possibly specific questions that he or she feels is an accurate gauge of a candidate's abilities.  The question sets for any two interviewers can be widely different and even entirely non-overlapping.
A classic example found everywhere is: Interviewer A always asks about C++ trivia, filesystems, network protocols and discrete math.  Interviewer B always asks about Java trivia, design patterns, unit testing, web frameworks, and software project management.  For any given candidate with both A and B on the interview loop, A and B are likely to give very different votes.  A and B would probably not even hire each other, given a chance, but they both happened to go through interviewer C, who asked them both about data structures, unix utilities, and processes versus threads, and A and B both happened to squeak by.
That's almost always what happens when you get an offer from a tech company.  You just happened to squeak by.  Because of the inherently flawed nature of the interviewing process, it's highly likely that
*someone*
on the loop will be unimpressed with you, even if you are Alan Turing.  Especially if you're Alan Turing, in fact, since it means you obviously don't know C++.
The bottom line is, if you go to an interview at
*any*
software company, you should plan for the contingency that you might get genuinely unlucky, and wind up with one or more people from your Interview Anti-Loop on your interview loop.  If this happens, you will struggle, then be told that you were not a fit at this time, and then you will feel bad.  Just as long as you don't feel meta-bad, everything is OK.  You should feel
*good*
that you feel bad after this happens, because hey, it means you're human.
And then you should wait 6-12 months and re-apply.  That's pretty much the best solution we (or anyone else I know of) could come up with for the false-negative problem.  We wipe the slate clean and start over again.  There are lots of people here who got in on their second or third attempt, and they're kicking butt.
You can too.
**OK, I feel better about potentially not getting hired**
Good!  So let's get on to those tips, then.
If you've been following along
*very*
closely, you'll have realized that I'm interviewer D.  Meaning that my personal set of pet questions and topics is just my own, and it's no better or worse than anyone else's.  So I can't tell you what it is, no matter how much I'd like to, because I'll offend interviewers A through X who have slightly different working sets.
Instead, I want to prep you for some general topics that I believe are shared by the majority of tech interviewers at Google-like companies.  Roughly speaking, this means the company builds a lot of their own software and does a lot of distributed computing.  There are other tech-company footprints, the opposite end of the spectrum being companies that outsource everything to consultants and try to use as much third-party software as possible.  My tips will be useful only to the extent that the company resembles Google.
So you might as well make it Google, eh?
First, let's talk about non-technical prep.
**The Warm-Up**
Nobody goes into a boxing match cold.  Lesson:  you should bring your boxing gloves to the interview.  No, wait, sorry, I mean: warm up beforehand!
How do you warm up?  Basically there is short-term and long-term warming up, and you should do both.
Long-term warming up means: study and practice for a week or two before the interview.  You want your mind to be in the general "mode" of problem solving on whiteboards.  If you can do it on a whiteboard, every other medium (laptop, shared network document, whatever) is a cakewalk.  So plan for the whiteboard.
Short-term warming up means: get lots of rest the night before, and then do intense, fast-paced warm-ups the morning of the interview.
The two best long-term warm-ups I know of are:
1)
**Study a data-structures and algorithms book**
.  Why?  Because it is the most likely to help you beef up on problem identification.  Many interviewers are happy when you understand the broad class of question they're asking without explanation.  For instance, if they ask you about coloring U.S. states in different colors, you get major bonus points if you recognize it as a graph-coloring problem, even if you don't actually remember exactly how graph-coloring works.
And if you do remember how it works, then you can probably whip through the answer pretty quickly.  So your best bet, interview-prep wise, is to practice the art of recognizing that certain problem classes are best solved with certain algorithms and data structures.
My absolute favorite for this kind of interview preparation is Steven Skiena's
.  More than any other book it helped me understand just how astonishingly commonplace (and important) graph problems are – they should be part of every working programmer's toolkit.  The book also covers basic data structures and sorting algorithms, which is a nice bonus.  But the gold mine is the second half of the book, which is a sort of encyclopedia of 1-pagers on zillions of useful problems and various ways to solve them, without too much detail.  Almost every 1-pager has a simple picture, making it easy to remember.  This is a great way to learn how to identify hundreds of problem types.
Other interviewers I know recommend
.  It's a true classic and an invaluable resource, but it will probably take you more than 2 weeks to get through it.  But if you want to come into your interviews
*prepped*
, then consider deferring your application until you've made your way through that book.
2)
**Have a friend interview you.**
The friend should ask you a random interview question, and you should go write it on the board.  You should keep going until it is complete, no matter how tired or lazy you feel.  Do this as much as you can possibly tolerate.
I didn't do these two types of preparation before my first Google interview, and I was absolutely shocked at how bad at whiteboard coding I had become since I had last interviewed seven years prior.  It's hard!  And I also had forgotten a bunch of algorithms and data structures that I used to know, or at least had heard of.
Going through these exercises for a week prepped me mightily for my second round of Google interviews, and I did way, way better.  It made all the difference.
As for short-term preparation, all you can really do is make sure you are as alert and warmed up as possible.  Don't go in cold.  Solve a few problems and read through your study books.  Drink some coffee: it actually helps you think faster, believe it or not.  Make sure you spend at
*least*
an hour practicing immediately before you walk into the interview.  Treat it like a sports game or a music recital, or heck, an exam: if you go in warmed up you'll give your best performance.
**Mental Prep**
So!  You're a hotshot programmer with a long list of accomplishments.  Time to forget about all that and focus on interview survival.
You should go in humble, open-minded, and focused.
If you come across as arrogant, then people will question whether they want to work with you.  The best way to appear arrogant is to question the validity of the interviewer's question – it really ticks them off, as I pointed out earlier on.  Remember how I said you can't tell an interviewer how to interview?  Well, that's
*especially*
true if you're a candidate.
So don't ask: "gosh, are algorithms really all that important?  do you ever need to do that kind of thing in real life?  I've never had to do that kind of stuff."  You'll just get rejected, so don't say that kind of thing.  Treat every question as legitimate, even if you are frustrated that you don't know the answer.
Feel free to ask for help or hints if you're stuck.  Some interviewers take points off for that, but occasionally it will get you past some hurdle and give you a good performance on what would have otherwise been a horrible stony half-hour silence.
Don't say "choo choo choo" when you're "thinking".
Don't try to change the subject and answer a different question.  Don't try to divert the interviewer from asking you a question by telling war stories.  Don't try to bluff your interviewer.  You should
*focus*
on each problem they're giving you and make your best effort to answer it fully.
Some interviewers will not ask you to write code, but they will
*expect*
you to start writing code on the whiteboard at some point during your answer.  They will give you hints but won't necessarily come right out and say: "I want you to write some code on the board now."  If in doubt, you should ask them if they would like to see code.
Interviewers have vastly different expectations about code.  I personally don't care about syntax (unless you write something that could obviously never work in any programming language, at which point I will dive in and verify that you are not, in fact, a circus clown and that it was an honest mistake).  But some interviewers are really picky about syntax, and some will even silently mark you down for missing a semicolon or a curly brace,
*without telling you*
.  I think of these interviewers as – well, it's a technical term that rhymes with "bass soles", but they think of themselves as brilliant technical evaluators, and there's no way to tell them otherwise.
So ask.  Ask if they care about syntax, and if they do, try to get it right.  Look over your code carefully from different angles and distances.  Pretend it's someone else's code and you're tasked with finding bugs in it.  You'd be amazed at what you can miss when you're standing 2 feet from a whiteboard with an interviewer staring at your shoulder blades.
It's OK (and highly encouraged) to ask a few clarifying questions, and occasionally verify with the interviewer that you're on the track they want you to be on.  Some interviewers will mark you down if you just jump up and start coding,
*even if you get the code right*
.  They'll say you didn't think carefully first, and you're one of those "let's not do any design" type cowboys.  So even if you think you know the answer to the problem, ask some questions and talk about the approach you'll take a little before diving in.
On the flip side, don't take too long before actually solving the problem, or some interviewers will give you a delay-of-game penalty.  Try to move (and write) quickly, since often interviewers want to get through more than one question during the interview, and if you solve the first one too slowly then they'll be out of time.  They'll mark you down because they couldn't get a full picture of your skills.  The benefit of the doubt is rarely given in interviewing.
One last non-technical tip: bring your own whiteboard dry-erase markers.  They sell pencil-thin ones at office supply stores, whereas most companies (including Google) tend to stock the fat kind.  The thin ones turn your whiteboard from a 480i standard-definition tube into a 58-inch 1080p HD plasma screen.  You need all the help you can get, and free whiteboard space is a real blessing.
You should also practice whiteboard space-management skills, such as not starting on the right and coding down into the lower-right corner in Teeny Unreadable Font.  Your interviewer will not be impressed.  Amusingly, although it always irks me when people do this, I did it during my interviews, too.  Just be aware of it!
Oh, and don't let the marker dry out while you're standing there waving it.  I'm tellin' ya:  you want minimal distractions during the interview, and that one is surprisingly common.
OK, that should be good for non-tech tips.  On to X, for some value of X!  Don't stab me!
**Tech Prep Tips**
The best tip is: go get a computer science degree.  The more computer science you have, the better.  You don't have to have a CS degree, but it helps.  It doesn't have to be an advanced degree, but that helps too.
However, you're probably thinking of applying to Google a little sooner than 2 to 8 years from now, so here are some shorter-term tips for you.
**Algorithm Complexity**
: you need to know Big-O.  It's a must.  If you struggle with basic big-O complexity analysis, then you are almost guaranteed not to get hired.  It's, like, one chapter in the beginning of one theory of computation book, so just go read it.  You can do it.
**Sorting**
: know how to sort.  Don't do bubble-sort.  You should know the details of at least one n*log(n) sorting algorithm, preferably two (say, quicksort and merge sort).  Merge sort can be highly useful in situations where quicksort is impractical, so take a look at it.
For God's sake, don't try sorting a linked list during the interview.
**Hashtables**
: hashtables are arguably the single most important data structure known to mankind.  You
*absolutely have to know how they work*
.  Again, it's like one chapter in one data structures book, so just go read about them.  You should be able to implement one using only arrays in your favorite language, in about the space of one interview.
**Trees**
: you should know about trees.  I'm tellin' ya: this is basic stuff, and it's embarrassing to bring it up, but some of you out there don't know basic tree construction, traversal and manipulation algorithms.  You should be familiar with binary trees, n-ary trees, and trie-trees at the very
*very*
least.  Trees are probably the best source of practice problems for your long-term warmup exercises.
You should be familiar with at least one flavor of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree.  You should actually know how it's implemented.
You should know about tree traversal algorithms:  BFS and DFS, and know the difference between inorder, postorder and preorder.
You might not use trees much day-to-day, but if so, it's because you're avoiding tree problems.  You won't need to do that anymore once you know how they work.  Study up!
**Graphs**
Graphs are, like, really
*really*
important.  More than you think.  Even if you already think they're important, it's probably more than you think.
There are three basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list), and you should familiarize yourself with each representation and its pros and cons.
You should know the basic graph traversal algorithms: breadth-first search and depth-first search.  You should know their computational complexity, their tradeoffs, and how to implement them in real code.
You should try to study up on fancier algorithms, such as Dijkstra and A*, if you get a chance.  They're really great for just about anything, from game programming to distributed computing to you name it.  You should know them.
Whenever someone gives you a problem,
*think graphs*
.  They are the most fundamental and flexible way of representing any kind of a relationship, so it's about a 50-50 shot that any interesting design problem has a graph involved in it.  Make absolutely sure you can't think of a way to solve it using graphs before moving on to other solution types.  This tip is important!
**Other data structures**
You should study up on as many other data structures and algorithms as you can fit in that big noggin of yours.  You should especially know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise.
You should find out what NP-complete means.
Basically, hit that data structures book hard, and try to retain as much of it as you can, and you can't go wrong.
**Math**
Some interviewers ask basic discrete math questions.  This is more prevalent at Google than at other places I've been, and I consider it a Good Thing, even though I'm not particularly good at discrete math.  We're surrounded by counting problems, probability problems, and other Discrete Math 101 situations, and those innumerate among us blithely hack around them without knowing what we're doing.
Don't get mad if the interviewer asks math questions.  Do your best.  Your best will be a heck of a lot better if you spend some time before the interview refreshing your memory on (or teaching yourself) the essentials of combinatorics and probability.  You should be familiar with n-choose-k problems and their ilk – the more the better.
I know, I know, you're short on time.  But this tip can really help make the difference between a "we're not sure" and a "let's hire her".  And it's actually not all that bad – discrete math doesn't use much of the high-school math you studied and forgot.  It starts back with elementary-school math and builds up from there, so you can probably pick up what you need for interviews in a couple of days of intense study.
Sadly, I don't have a good recommendation for a Discrete Math book, so if you do, please mention it in the comments.  Thanks.
**Operating Systems**
This is just a plug, from me, for you to know about processes, threads and concurrency issues.  A lot of interviewers ask about that stuff, and it's pretty fundamental, so you should know it.  Know about locks and mutexes and semaphores and monitors and how they work.  Know about deadlock and livelock and how to avoid them.  Know what resources a processes needs, and a thread needs, and how context switching works, and how it's initiated by the operating system and underlying hardware.  Know a little about scheduling.  The world is rapidly moving towards multi-core, and you'll be a dinosaur in a real hurry if you don't understand the fundamentals of "modern" (which is to say, "kinda broken") concurrency constructs.
The best, most practical book I've ever personally read on the subject is Doug Lea's
.  It got me the most bang per page.  There are obviously lots of other books on concurrency.  I'd avoid the academic ones and focus on the practical stuff, since it's most likely to get asked in interviews.
**Coding**
You should know at least one programming language really well, and it should
*preferably*
be C++ or Java.  C# is OK too, since it's pretty similar to Java.  You will be expected to write some code in at least some of your interviews.  You will be expected to know a fair amount of detail about your favorite programming language.
**Other Stuff**
Because of the rules I outlined above, it's still possible that you'll get Interviewer A, and none of the stuff you've studied from these tips will be directly useful (except being warmed up.)  If so, just do your best.  Worst case, you can always come back in 6-12 months, right?  Might seem like a long time, but I assure you it will go by in a flash.
The stuff I've covered is actually mostly red-flags: stuff that really worries people if you don't know it.  The discrete math is potentially optional, but somewhat risky if you don't know the first thing about it.  Everything else I've mentioned you should know cold, and then you'll at least be prepped for the baseline interview level.  It could be a lot harder than that, depending on the interviewer, or it could be easy.
It just depends on how lucky you are.  Are you feeling lucky?  Then give it a try!
**Send me your resume**
I'll probably batch up any resume submissions people send me and submit them weekly.  In the meantime, study up!  You have a lot of warming up to do.  Real-world work makes you rusty.
I hope this was helpful.  Let the flames begin, etc.  Yawn.