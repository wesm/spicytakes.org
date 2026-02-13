---
title: "Building Communities with Software"
date: 2003-03-03
url: https://www.joelonsoftware.com/2003/03/03/building-communities-with-software/
word_count: 3988
---


The social scientist Ray Oldenburg talks about how humans need a third place, besides work and home, to meet with friends, have a beer, discuss the events of the day, and enjoy some human interaction. Coffee shops, bars, hair salons, beer gardens, pool halls, clubs, and other hangouts are as vital as factories, schools and apartments [“The Great Good Place”, 1989]. But capitalist society has been eroding those third places, and society is left impoverished. In “Bowling Alone,” Robert Putnam brings forth, in riveting and well-documented detail, reams of evidence that American society has all but lost its third places. Over the last 25 years, Americans “belong to fewer organizations that meet, know our neighbors less, meet with friends less frequently, and even socialize with our families less often.” [2000] For too many people, life consists of going to work, then going home and watching TV. Work-TV-Sleep-Work-TV-Sleep. It seems to me that the phenomenon is far more acute among software developers, especially in places like Silicon Valley and the suburbs of Seattle. People graduate from college, move across country to a new place where they don’t know anyone, and end up working 12 hour days basically out of loneliness.


So it’s no surprise that so many programmers, desperate for a little human contact, flock to online communities – chat rooms, discussion forums, open source projects, and Ultima Online. In creating community software, we are, to some extent, trying to create a third place. And like any other architecture project, the design decisions we make are crucial. Make a bar too loud, and people won’t be able to have conversations. That makes for a very different kind of place than a coffee shop. Make a coffee shop without very many chairs, as Starbucks does, and people will carry their coffee back to their lonely rooms, instead of staying around and socializing like they do in the fantasy TV coffeehouse of “Friends,” a program we watch because an ersatz third place is less painful than none at all.


In software, as in architecture, design decisions are just as important to the type of community that develops or fails to develop. When you make something easy, people do it more often. When you make something hard, people do it less often. In this way you can gently encourage people to behave in certain ways which determine the character and quality of the community. Will it feel friendly? Is there thick conversation, a European salon full of intellectuals with interesting ideas? Or is the place deserted, with a few dirty advertising leaflets lying around on the floor that nobody has bothered to pick up?


Look at a few online communities and you’ll instantly notice the different social atmosphere. Look more closely, and you’ll see this variation is most often a byproduct of software design decisions.


On Usenet, threads last for months and months and go off onto so many tangents that you never know where they’ve been. Whenever a newbie stumbles by and asks a germane question, the old timers shout him down and tell him to read the FAQ. Quoting, with the “>” symbol, is a disease that makes it impossible to read any single thread without boring yourself to death by re-reading the whole history of a chain of argument which you just read in the original, seconds ago, again and again and again. Shlemiel the Painter reading.


On IRC, you can’t own your nickname and you can’t own a channel — once the last person leaves a room, anyone can take it over. That’s the way the software works. The social result was that it was often impossible to find your friends when you came back the next day, because someone else might have locked you out of your chatroom and your friends might have been forced to choose different nicknames. The only way to prevent gay bashers in Perth, Australia from taking over gay chat channels when the boys went to sleep was to create a software robot to hang around 24 hours a day and guard the channel. Many IRC participants put more effort into complicated bot-wars, attempts to take over channels, and general tomfoolery than actually having a conversation, often ruining things for the rest of us.


On most investment discussion boards, it’s practically impossible to follow a thread from beginning to end, because every post is its own page, which makes for a lot of banner ad inventory, but the latency in reading a conversation will eventually drive you nuts. The huge amount of flashing commercial crap on all four sides of the conversation makes you feel like you were trying to make friends in Times Square, but the neon lights keep demanding all the attention.


On Slashdot, every thread has hundreds of replies, many of which are identical, so the conversation there feels insipid and stupid. In a moment I’ll reveal why Slashdot has so many identical replies and the Joel on Software forum doesn’t.


And on FuckedCompany.com, the discussion board is completely, utterly worthless; the vast majority of posts consist of irrelevant profanity and general abusiveness and it feels like a fraternity rudeness contest, without any fraternity.


So, we have discovered the primary axiom of online communities:


> **Small software implementation details result in big differences in the way the community develops, behaves, and feels.**


IRC users organize themselves around bot warfare because the software doesn’t let you reserve a channel. Usenet threads are massively redundant because the original Usenet reader, “rn,” designed for 300 baud modems, never shows you old posts, only new ones, so if you want to nitpick about something someone said, you had to quote them or your nitpick won’t make sense.


With that in mind, I’d like to answer the most common questions about the Joel on Software forum, why it was designed the way it was designed, how that makes it work, and how it could be improved.


Q. Why is the software so dang simplistic?


A. In the early days of the Joel on Software forum, achieving a critical mass to get the conversation off the ground was important to prevent the empty restaurant phenomenon (nobody goes into an empty restaurant, they’ll always go into the full one next door even if it’s totally rubbish.) Thus a design goal was to eliminate impediments to posting. That’s why there’s no registration and there are literally no features, so there’s nothing to learn.


The business goal of the software that runs the forum was to provide tech support for Fog Creek’s products. That’s what paid for the development. To achieve that goal, nothing was more important than making the software super simple so that anyone could be comfortable using it. Everything about how the forum works is incredibly obvious. I don’t know of anyone who hasn’t been able to figure out how to use it immediately.


Q. Could you make a feature where I check a box that says “email me if somebody replies to my post?”


A. This one feature, so easy to implement and thus so tempting to programmers, is the best way to kill dead any young forum. Implement this feature and you may never get to critical mass. Philip Greenspun’s LUSENET has this feature and you can watch it sapping the life out of young discussion groups.


Why?


What happens is that people go to the group to ask a question. If you offer the “notify me” checkbox, these people will post their question, check the box, and never come back. They’ll just read the replies in their mailbox. The end.


If you eliminate the checkbox, people are left with no choice but to check back every once in a while. And while they’re checking back, they might read another post which looks interesting. And they might have something to contribute to that post. And in the critical early days when you’re trying to get the discussion group to take off, you’ve increased the “stickiness” and you’ve got more people hanging around, which helps achieve critical mass a lot quicker.


Q. OK, but can’t you at least have branching? If someone gets off on a tangent, that should be its own branch which you can follow or go back to the main branch.


A. Branching is very logical to a programmer’s mind but it doesn’t correspond to the way conversations take place in the real world. Branched discussions are disjointed to follow and distracting. You know what I find distracting? When I’m trying to do something on my bank’s web site and the site is so slow I can’t remember what I’m doing from one click to the next. That reminds me of a joke. Three old ladies talking. Lady 1: “I’m so forgetful the other day I was on the steps to my apartment with a bag, and I couldn’t remember if I was taking out the trash or going upstairs with the groceries.” Lady 2: “I’m so forgetful I was in my car in the driveway and I couldn’t remember if I was coming home or going to shul.” Lady 3: “Thank God, I still have my memory, clear as a bell, knock on wood. (knock knock knock). Come in, door’s open!” Branching makes discussions get off track, and reading a thread that is branched is discombobulating and unnatural. Better to force people to start a new topic if they want to get off topic. Which reminds me…


Q. Your list of topics is sorted wrong. It should put the topic with the most recent reply first, rather than listing them based on the time of the original post.


A. It could do that; that’s what many web-based forums do. But when you do that certain topics tend to float near the top forever, because people will be willing to argue about H1B visas, or what’s wrong with Computer Science in college, until the end of the universe. Every day 100 new people arrive in the forum for the first time, and they start at the top of the list, and they dive into that topic with gusto.


The way I do it has two advantages. One, topics rapidly go away, so conversation remains relatively interesting. Eventually people have to just stop arguing about a given point.


Two, the order of topics on the home page is stable, so it’s easier to find a topic again that you were interested in because it stays in the same place relative to its neighbors.


Q. Why don’t you have some kind of system so I can see what posts I’ve already read?


A. We have the best system that can be implemented in a distributed, scalable fashion: we let everyone’s browser keep track of it. Web browsers will change the color of the links you’ve already visited from blue to purple. So all we have to do is subtly change the URL for each topic to include the number of replies available; that way when there are additional replies the post will appear in the “unread” color again.


Anything more elaborate than this would be harder to build and would needlessly complicate the UI.


Q. The damn “reply” link is all the way at the bottom. This is a usability annoyance because you have to scroll all the way to the bottom.


A. This is intentional. I would prefer that you read all the posts before you reply, otherwise you may post something which is repetitive or which sounds disjointed coming after the previous last post. Of course, I can’t physically grab your eyeballs and move them from left to right, forcing you to read the entire thread before letting you post, but if I put a “reply” link anywhere but the bottom of the page that would positively encourage people to spew their little gems before they’ve read what’s already there. This is why Slashdot topics have 500 replies but only 17 interesting replies, and it’s why nobody likes to read Slashdot discussions: they sound like a classroom full of children all shouting out the same answer at the same time. (“ha ha … Bill Gates! That’s an oxymoron!”)


Q. The damn “Start a New Topic” link is all the way at the bottom…


A. Uh huh, same thing.


Q. Why don’t you show people their posts to confirm them before you post them? Then people wouldn’t make mistakes and typos.


A. Empirically, that is not true. Not only is it not true, it’s the opposite of true.


Part one: when you have a confirmation step, most people just click past it. Very few people reread their post carefully. If they wanted to reread their post carefully, they could have done it while they were editing it, but they are bored by their post already, it’s yesterday’s newspaper, they are ready to move on.


Part two: the lack of the confirmation step actually makes people more cautious. It’s like those studies they did that showed that it’s safer, on twisty mountain roads, to remove the crash barrier, because it makes people scared and so they drive more carefully, and any way, that little flimsy aluminum crash barrier ain’t gonna stop a 2 ton SUV moving at 50 mph from flying off the cliff. You’re better off, statistically, just scaring the bejesus out of drivers so they creep along at 2 miles per hour around the hairpins.


Q. Why don’t you show me the post I’m replying to, while I compose my reply?


A. Because that will tempt you to quote a part of it in your own reply. Anything I can do to reduce the amount of quoting will increase the fluidity of the conversation, making topics interesting to read. Whenever someone quotes something from above, the person who reads the topic has to read the same thing twice in a row, which is pointless and automatically guaranteed to be boring.


Sometimes people still try to quote things, usually because they are replying to something from three posts ago, or because they’re mindlessly nitpicking and they need to rebut 12 separate points. These are not bad people, they’re just programmers, and programming requires you to dot every i and cross every t, so you get into a frame of mind where you can’t leave any argument unanswered any more than you would ignore an error from your compiler. But I’ll be damned if I make it EASY on you. I’m almost tempted to try to find a way to show posts as images so you can’t cut and paste them. If you really need to reply to something from three posts ago, kindly take a moment to compose a decent English sentence (“When Fred said blah, he must not have considered…”), don’t litter the place with your <<<>>>s.


Q. Why do posts disappear sometimes?


A. The forum is moderated. That means that a few people have the magick powah to delete a post. If the post they delete is the first one in a thread, the thread itself appears deleted because there’s no way to get to it.


Q. But that’s censorship!


A. No, it’s picking up the garbage in the park. If we didn’t do it, the signal to noise ratio would change dramatically for the worse. People post spam and get rich schemes, people post antisemitic comments about me, people post nonsense that doesn’t make any sense. Some idealistic youngsters may imagine a totally uncensored world as one in which the free exchange of intelligent ideas raises everyone’s IQ, an idealized Oxford Debate Society or Speakers’ Corner. I am pragmatic and understand that a totally uncensored world just looks like your inbox: 80% spam, advertising, and fraud, rapidly driving away the few interesting people.


If you are looking for a place to express yourself in which there will be no moderation, my advice to you would be to (a) create a new forum and (b) make it popular. [Apologies to Larry Wall].


Q. How do you decide what to delete?


A. First of all, I remove radically off-topic posts or posts which, in my opinion, are only of interest to a very small number of people. If something is not about the same general topics as Joel on Software is about, it may be interesting as all heck to certain people but it’s not likely to interest the majority of people who came to my site to hear about software development.


My policy in the past has been that “off topic” includes any discussion of the forum itself, its design or usability. There’s a slightly different reason for this, almost another axiom. Every forum, mailing list, discussion group, and BBS will, all else being equal, lapse into conversations about the forum itself every week or two. Literally once a week somebody strolls in and announces his list of improvements to the forum software which he demands be made right away. And then somebody says, “look buddy you’re not paying for it Joel’s doing us a favor get lost.” And somebody else says “Joel’s not doing this out of the goodness of his heart it’s marketing for Fog Creek.” And it’s just SOOOO BORING because it happens EVERY WEEK. It’s like talking about the weather when you have nothing else to talk about. It may be exciting to the new person who just appeared on the board but it is only barely about software development, so, as Strong Bad says, “DELETED”. Unfortunately what I have learned is that trying to get people to stop talking about the forum is like trying to stop a river. But please, if you’re reading this article and you want to discuss it on the forum, please, please, do me a *huge *favor, and resist the urge.


We will delete posts which are personal, ad hominem attacks on non public personalities. I better define that. Ad hominem means it is an attack on the individual, rather than on his ideas. If you say “that is a stupid idea because…” it’s OK. If you say “you are stupid” then it’s an ad hominem attack. If it’s vicious or uncivil or libelous, I delete it. There’s one exception: because the Joel on Software forum is the best place to criticize Joel, vicious or uncivil posts about Joel are allowed to stand but only if they contain some tiny sliver of a useful argument or idea.


I automatically delete posts which comment on the spelling or grammar of a previous poster. We’ll be talking about interviews and someone will say, “It’s a wonder you can get a job with spelling like that.” It’s just super boring to talk about other people’s spelling. SUPER, SUPER boring.


Q. Why don’t you just post the rules instead of leaving it as a mystery?


A. The other day I was taking the train from the Newark Airport back to Manhattan. Besides being in general disrepair, the only thing to read was a large sign that explained very sternly and in great detail that if you misbehaved, you would be put off the train at the next stop and the police would be summoned. And I thought, 99.99999% of the people who read that sign ain’t gonna be misbehavin’, and the misbehavors couldn’t care less what the sign says. So the net result of the sign is to make honest citizens feel like they’re being accused of something, and it doesn’t deter the sociopaths at all, and it just reminds the good citizens of New Jersey endlessly that they’re in Newark, Crime Capital, where sociopaths get on the train and do Unpleasant Things and Make a Scene and have to be Put Off and the Police Summoned.


Almost everyone on the Joel on Software forum, somehow, was born with the part of the brain that tells them that it’s not civilized to post vicious personal attacks, or to post questions about learning French on a software forum, or to conduct an argument by criticizing someone’s spelling. And the other .01% don’t care about the rules. So posting rules is just a way to insult the majority of the law-abiding citizens and it doesn’t deter the morons who think their own poo smells delicious and nothing they post could possibly be against the rules.


When you address troublemakers in public, everyone else thinks you’re paranoid or feels angry at being scolded when they did nothing wrong. It’s like being in grade school again, and one idiot-child has broken a window, and now everyone has to sit there listening to the teacher giving the whole class a stern lecture on why you mustn’t break windows. So any public discussion of why a particular post got deleted, for example, is taboo.


Q. Instead of deleting posts, why don’t you have a moderation scheme, where people vote on how much they like a post, and people can choose how high the vote has to be before they read it?


A. This is, of course, how Slashdot works, and I’ll bet you 50% of the people who read Slashdot regularly have never figured it out.


There are three things I don’t like about this. One: it’s more UI complication, a feature that people need to learn how to use. Two: it creates such complicated politics that it make the Byzantine Empire look like 3rd grade school government. And three: when you read Slashdot with the filters turned up high enough that you only see the interesting posts, the narrative is completely lost. You just get a bunch of random disjointed statements with no context.


Q. Why don’t you have a registration scheme to eliminate rude posters?


A. As I explained earlier, the goal of the forum is to make it easy to post. (Remember, the software was written for tech support.) Registration schemes eliminate at least 90% of the people who might have posted, and in a tech support scenario, those 90% are going to call my toll free number.


Besides, I don’t think registration would help. If somebody is being abusive, it doesn’t help to ban them, they can trivially reregister. The idea of improving the community by requiring registration is an old one, and it’s appropriate, I think, for the Echo/Well type of conferences where you’re creating a network of people as much as you’re discussing a topic, and you charge people cash money to belong.


But requiring registration does NOT improve the quality of the conversation or the average quality of the participants. If you look closely at the signal-to-noise ratio on the Joel on Software forum, you might start to notice that the noisiest people (i.e. the people who post the most words while contributing the fewest ideas) are often the long time, hard core members who visit the forum every ten minutes. These are the people who feel the need to chime in with a “I agree with that” and replies to Every Single Topic even when they haven’t got an original thought to contribute. And they would certainly register.


Q. Any plans for the future?


A. Working on the software for the discussion forum is not a priority for me or my company: it’s good enough, it works, it has created an interesting place to talk about hard computer management problems and get ideas from some of the smartest people in the world. And I’ve got too many better things to work on. Somebody else can create the next big leap in usability for discussion forums.


I just created a New York City forum, to see if geographically based forums encourage people to get to know each other in person as well as online. In my experience, regionally- based communities cause the community to take a giant leap from a simple website to a real society, a true third place.


Creating community, in any case, is a noble goal, because it’s sorely missing for so many of us. Let’s keep plugging away at it.
