---
title: "Using an Agile Software Process with Offshore Development"
description: "For the last four years Thoughtworks has operated a lab in 	Bangalore India to support our software development projects in 	North America and Europe. Traditional approaches to offshore 	development a"
date: 2006-07-18T00:00:00
tags: ["agile"]
url: https://martinfowler.com/articles/agileOffshore.html
slug: agileOffshore
word_count: 6546
---


One of the fundamental tenets of any agile software methodology
is the importance of communication between the various people involved
in software development. Furthermore agile methods put a large premium
on improving communication through face-to-face communication. As the
agile manifesto states âThe most efficient and effective method of
conveying information to and within a development team is face-to-face
conversation.â Extreme Programming emphasizes this with its practice
of a single open development space where the team can work closely
together. Cockburn's book spends a lot of time talking about the
importance of physical proximity in agile methods.


Another trend that's been grabbing the software development world
recently is the move to offshore development, where much of the
development work is done in lower paid, ahem more cost effective
countries. Offshore development seems opposed to agile development in
a couple of ways. For a start it immediately goes against the notion
of physical proximity, since by definition offshore developers are a
long way away. Secondly most offshore organizations favor the
plan-driven approach where detailed requirements or designs are
sent offshore to be constructed.


So the fundamental question is whether agile techniques can be
used in an offshore setting. If so how does it compare to using an
plan-driven methodology (the term I'll use here for non-agile)?


The experiences I'm writing about here are based on work done
over the last few years by Thoughtworks. We opened an office in
Bangalore India in 2001 and have done several projects which have used
a Bangalore based team. We've also done some offshore development with
our Australian offices. In these projects we've committed to using as
much of an agile approach as possible, since we believe that agility is
an approach that's in the best interests of our customers. In this
essay I'll describe some of the lessons we've learned so far.


To help provide some context, it's worth talking a little about
the way in which we've setup the Bangalore office. We expected the
office to be used primarily as an offshore development environment, so
we recruited mostly application developers. The majority were hired
directly out of college and we seasoned the mix with some more
experienced developers. It was very important to us that we retained
our very high hiring standards (typically we only offer jobs to about
1 in 100 applicants), and we continued the model in India. As a result
we have a very talented group of developers with a mix of
experience levels. At the beginning we brought over several more experienced US
and UK
developers, to mentor the newer developers on both software
development and the agile/XP practices we've come to enjoy. Currently
we have about 150 developers in Bangalore.


## Lessons Learned


### Use Continuous Integration to Avoid Integration
Headaches


I've heard several stories about problems with integrating
the work across multi-site teams. Even with a lot of care put into
defining interfaces, integration problems still rear their ugly head.
Often this is because it's very hard to properly specify the
semantics of an interface, so even if you have all the signatures
right, you still get tripped up on assumptions about what the
implementation will actually do.


The earliest XP practice to really take hold at Thoughtworks
was Continuous Integration, and we've become so accustomed to it that
we were determined to use it with our offshore development. So from
the beginning we've put everyone on a single code base, with
CruiseControl running to both build and run tests. This way everyone
is kept close to the mainline, whatever their location happens to
be.


Everyone has been delighted with how well this works. Its
main benefit is that problems that plague other groups with
integration just don't happen to us. The continuous integration and
test process flushes out many integration problems very quickly, as a
result they can be fixed before they become hard to find.


CruiseControl's web page allows all sites to see what's going
on abroad. First thing in the morning you can check the CruiseControl
web page to see what changes have been made by the other sites. It
provides an easy way to catch up on what's going on at the other end
of the world.


This does require good build discipline, where developers
strive hard not to break the build, and fix it immediately if it
becomes broken. It's generally accepted practice that if you commit
changes to the mainline, you should not go home until you have
received the email message from CruiseControl that says that your
changes resulted in a successful build. A late night bad build is much
more serious when the remote office is running off the same build.


Although world-wide Continuous Integration is resoundingly
popular, we have run into some problems. Communication pipes aren't as
wide and reliable as we'd like, so many source control operations can
get awkward from a remote site. In general we keep the build servers
in the same site as the majority of developers, but remote sites can
find it takes an annoyingly long time to get a fresh update from the
mainline. The longer the communication lines are, the more they are
prone to anything from glitches to lines being down for a while. 
Having the repository accessible 24 hours makes it annoying to take it
down to do backups. All of these issues would mitigated by a clustered
code repository, but we haven't experimented with anything like that
yet.


We have found that some source-code control systems are
				particularly prone to long and painful check-outs -
				particularly if they are not configured well. It's worth
				spending time on finding ways to speed up check-out times, and
				indeed changing source code control systems if you're stuck
				with one that doesn't handle remote working very well.


(Interestingly people assume that these communication problems
			are specifically a problem with a remote site like India - but
			we've found problems often occur with the infrastructure in the
			west too. Continuous Integration requires good connectivity,
			often better connectivity than people are used to.)


Even with the best connectivity, however, there can be
				problems if a system requires services that are locked inside
				an onshore firewall. You'll need to build good [test doubles](https://martinfowler.com/bliki/TestDouble.html)
				for these services so the system can be effectively tested in
				the development environment.


### Have Each Site Send Ambassadors to the Other Sites


As I've said above, agile methods stress the importance of
face to face human interaction. Even if everyone cannot be co-located,
moving some people about clearly helps a lot. From the beginning we
decided to ensure that at all times there was someone from the US team
present in India to facilitate the communication. Such an ambassador
already knows the US based people and thus adds his personal contacts
to help everyone communicate.


We've now expanded this to several levels. We found it useful
to send a US developer and a US analyst to India to communicate on
both technical and requirements levels. It's also valuable to send
someone from India to the US team. The plane fares soon repay
themselves in improved communication.


One of the benefits of a business-oriented ambassador on the
offshore team is that it helps provide business context to the
offshore team. Building software off just a list of requirements
misses out a lot business context - developers are told what to do
without being told why it's important. The why often makes a big
difference in doing the what properly.


An important part of the ambassador's job is to communicate
gossip. On any project there's a lot of informal communication. While
much of this isn't important, some of it is - and the trouble is that
you can't tell which is which. So part of an ambassadors job is to
communicate lots of tidbits which don't seem important enough for more
formal communication channels.


We usually rotate the ambassadors every few months (and in
			some cases every few weeks), since if
an ambassador spends too long abroad they lose contact with home. This
makes it easier for the ambassadors, who don't want to be away for too
long. It also allows more people to get to know the remote team by
spending time as an ambassador. In choosing ambassadors it's very
important to pay attention to individual needs and preferences. Some
people don't want to spend several months thousands of miles away from
home, so they shouldn't be ambassadors.


We've also found that it's important for project managers to
spend some time as ambassadors. Much of a project manager's job is to
help resolve conflicts and flush out problems before they become
serious. Experience working on both side of the telephone line is
really important for them to do that effectively.


Ambassadors are an important part of trust building and
				gelling across the wire. As a result it's essential to send
				out ambassadors as early as possible in the project. If a
				project runs for a while without ambassadors in place,
				miscommunications and bad feelings will develop that take a
				lot of work to fix. Ambassadors reduce this risk, but need to
				be there early on before problems start setting in.


### Use Contact Visits to build trust


Ambassadors are semi-permanent people who spend several
months in the 'other' location. This is vital, but not enough. There
are also needs to be further contacts that involve a wider range of
people. These visits help to create and maintain the relationships
which need to be in place for remote communication to work
effectively.


You can think of two kinds of contact visits: seeding visits
occur early the in the project and are intended to create the
relationships, while maintaining visits help keep the relationship
going.


Seeding visits should be planned for early in the project and
should be pretty substantial in length - two weeks is the minimum.
It's important for seeding visits to be working trips, since the whole
point is to get people used to working with each other, so they should
be arranged around some joint task.

- Send some onshore customers and project managers to an
offshore site to create an initial release plan.
- Have the offshore analysts come onshore to take part in
early requirements gathering sessions.
- Have some onshore developers visit the offshore team for
the offshore team's first iteration working with an existing code
base.
- Have the offshore team visit the onshore location -
					particularly if it's on a client site.


Whatever the reason, remember that the primary purpose of the
visit isn't to do the task, but to the build the working
relationships. It's a common mistake with these things to cram so many
tasks into the visit that there's little time for the vital human
communication. So keep the work pace relaxed, and don't be afraid to
schedule in something informal where the hosts can show the visitors
around and get some informal contacts going. Dinners and sightseeing
can often be the most useful activity that the visitors do with the
hosts.


It is important to get seeding visits in as soon as you
				can. Without decent personal relationships it is likely that
				you will run into problems due to miscommunication and lack of
				trust. These problems will take a lot of energy to repair and
				can easily cause lasting damage to the project. So seed early
				to head these problems off.


A special variant of the seeding visit is important if you
				have developers on multiple sites from the beginning. In this
				case it's important to get the developers, or at least the
				senior developers, together to build the first few
				iterations. It's in these iterations that the crucial
				architectural decisions will get made, it's important to have
				proximity during this period. Without this you can get a split
				where different teams make different decisions, or one team
				makes a decision that the other team doesn't understand.


Once the seeding is done, then less intense maintenance
visits should be used to keep the contact going. These can be shorter
but should be frequent, a one-week visit every couple of months is the
minimum for these.  Again they should be focused on necessary tasks,
one good task to do with these is a retrospective. Don't be afraid to
use longer and more frequent visits if you sense communication
problems between the teams or if a significant issue comes up. We've
noticed that it's particularly useful to have a longer contact visit
if significant changes occur to the system design.


Gifts, particularly those that help spread culture, are
				always worth bringing. We particularly like people to bring
				gifts of snack food or sweets that are specialties of the
				remote location.


### Don't Underestimate the Culture Change


One of the hardest parts of introducing agile methods into an
organization is the cultural change it causes. Indeed we've found that
this is the major reason why organizations have problems with adopting
agile methods. Many companies operate with a command and control model
which assumes that seniors make decisions and lower level people carry
them out. To make agile methods work you need much more autonomy and decision
making by the doers.


We find this to be a big problem in western companies, but
the problem is amplified in Asia since Asian cultures reinforce
deference to superiors. (A training course I saw from a
major Indian contracting company defined management as âthe science of
controlâ.) In this environment people are often discouraged from
asking questions, talking about problems, warning about unfeasible
deadlines, or proposing alternatives to
perceived instructions from superiors.


Western teams need to be wary of this tendency and should
				push back when they sense an eastern team is passively
				agreeing. Beware that polite acceptance is often a sign of an
				important issue not getting discussed. In addition western
				teams need be wary of sounding authoritative - which reinforces
				this kind of situation.


The bad news for this is that getting teams to be more
pro-active is an uphill battle, and one that inevitably takes a lot of
time. You can never assume that problems will be raised, even when
they are spotted. Getting people used to a distributed control style
of management takes longer than you think.


But there is good news. Once people realize they have the
freedom, and the responsibility, of making decisions - they seem to
really relish it. Several of our Indian team told me how their friends
in other companies cannot believe how much autonomy they are given.
This autonomy is a great motivator, allowing people to be both more
productive and able to grow into greater responsibility. Offshore team
members gain the trust the understanding to make decisions instead of
waiting for the onshore team, which lead to a lot of delays. For me one of
the most interesting things we will discover  is what the longer term
effects are of this cultural impact, both in Asia and in the West.


Seeding visits play an important role here. People are much
				more likely to raise issues if they have a good personal
				relationship.


Even talking about these cultural issues can cause
			problems. Some (western) industry analysts who saw a draft of
			this article said that this section was patronizing and
			offensive. One of our developers in Bangalore said I'm being far
			too mild. Another commented that it's an issue, but questioned
			as to whether it was worse that it is in many western
			companies. But there seems to be some consensus that there are
			cultural forces in Asia that reinforce command and control, and
			that this is changing.


(This is a particularly sharp issue for Thoughtworks. We have
a pronounced anti-authority attitude that's striking even in the US.
We decided from the beginning that we would retain that same culture
in India. I'm glad to say that we certainly seem to be
succeeding.)


### Use wikis to contain common information


We've played around with various ways to hold common
information, our favorite so far is a wiki. Wikis work well because
they are simple to use, can be worked with any browser, and are simple
to set up.


Any common information can be put there, [story](https://martinfowler.com/bliki/UserStory.html) cards, design
guidelines, build instructions, notes on progress - anything that needs to be written
down for reference by the team. We've found it's very useful to use
the change notification capability that many wikis have, so that page
changes trigger notifications through email or an RSS feed.


Wikis are by nature unstructured, and this lack of structure
is part of the benefit. The team can usually evolve their own
structure on the wiki as the project grows. This does mean that
someone needs to act as a gardener to  make sure it doesn't get
overgrown.


### Use Test Scripts to Help Understand the Requirements


With greater distance, you need to put more ceremony into
communicating requirements. We've been able to do that while still
sticking to many of the techniques that we use in single-site
development.


Increasingly I've found that more mature XP teams use
acceptance tests as ways of communicating requirements. Such teams get
test scripts written out before the start of an iteration to help
clarify the requirements and give the development team a concrete
target to aim at. One style that's worked well is for a US based
customer to write a short narrative (a couple of pages) to flesh out a
feature (story in XP lingo). An Indian based analyst/tester then
creates test scripts for this story. This can be done either for
automated or manual testing, although we very much prefer automated
tests. As the scripts are developed the US and Indian analysts
coordinate by email and IM as well as regular (2-3 times a week)
conference calls to review the test scripts.


We've found that this has very much helped both the Indian
analyst and the US customer really understand the requirements.
Writing out the tests forces the Indian analyst to really understand
what's needed and to ask questions of the US customer as questions
turn up. The developers find it easier to ask questions of the Indian
analyst rather than dig through the test scripts, so having an Indian
analyst/tester is still important. Search engines are good, but humans
are often easier to work with.


The biggest problem we found with this technique is to
				engage the client staff in doing it. As a result on the
				majority of projects we haven't been able to do it - but when
				we have we've found the approach valuable.


### Use Regular Builds to Get Feedback on Functionality


When people consider the requirements gathering in agile
methods, they often fail to see the importance of the feedback loop.
Often the requirements process is seen as analysts providing
requirements, which developers go off and implement. At some later
point somebody checks to see if the developers have implemented
what they were asked for. On an agile project, the close proximity
between customer and developer allows the customer to monitor progress
much more frequently, which allows them to spot misunderstandings more
quickly. Furthermore  a partially developed system can also educate
the customer, for often there's a difference between what's asked for
and what's needed - and usually that's not apparent until there's some
working software.


Having regular integrated builds allows a US customer to pull
down last night's work and try it out. While this isn't quite as
immediate as co-location, it still allows the customer to correct any
misunderstandings quickly; as well as allowing them to refine their
own understanding of the requirements.


To make this work, it's critical to sort out the environment
			issues so that you properly duplicate the environment on both
			sides of the ocean. There's nothing worse than onshore people
			pulling down a build, finding problems, and the offshore people
			being unable to duplicate the problem due to environment
			configuration issues. Make sure the environment is sorted out
			early, and ensure someone is around to fix any environment
			problems if they appear.


Make sure people look at what's built regularly, even if it's
			only partial functionality. The quicker someone looks at a
			piece of work, the quicker they can spot any
			miscommunication. Often people like to wait until something is
			finished before showing it to others. In these situations,
			however, it isn't worth the wait.


Scrum has long advocated that the development team does a
				demo to the customers at the end of every iteration. We've
				adopted this practice pretty widely now - we call it a
				showcase. With remote teams we like to do a remote showcase,
				where the offshore developers show the new features in the
				software with the help of remote desktop software. Getting the
				remote team to do this is another example of taking every
				opportunity to build links between offshore and onshore, and
				between developers and customers.


### Use Regular Short Status Meetings


Agile methods promote regular short status meetings for the
entire team (Scrums in Scrum, stand up meetings in XP). Carrying this
over to remote groups is important, so they can coordinate with other
teams. Time zones are often the biggest problem here, particularly
between the US and India where any time is awkward for somebody. In
our earlier projects we found that twice a week stand-ups seemed to work well
and provide enough coordination.


In our more recent projects we've made a greater use of the
			wiki, and this has reduced the need for cross-shore
			stand-ups. Now we do stand-ups within a shore's team, but not
			between the different shores. We do however do daily cross-shore
			meetings, but these don't involve the entire team - just those
			who focus on the cross shore collaboration. With small teams,
			however, we do do the cross-shore stand-ups.


We've found that it's a good habit to start conference
				calls with chit chat on local news. Recent odd bits of local
				color - politics, sport, weather - helps each side get a sense
				of the broader life context on the other side of the wire. (It
				strikes me that this is probably obvious to anyone other than
				us nerds - when people are heavily task-oriented it's easy to
				lose sight of the broader context in which we live.)


With time zone problems it's important for both sides to give
and take in picking the time for calls. One of our clients would only
do the calls during their business day, which forced the Indian folks
to come in at very awkward hours. Pushing all the onus on one side to
accommodate isn't helpful for smooth collaboration.


This lack of knowledge, or consideration, runs into other
				areas as well. One project scheduled a major release during
				the Indian holiday of [Diwali](http://en.wikipedia.org/wiki/Diwali), which is the equivalent of
				asking an American team to working over
				Thanksgiving. Fortunately we were able to convince them to
				change the date. Even in less serious cases remember that
				holidays are rarely shared, so you'll often get times when one
				team is in holiday mode while another team is in a regular
				work week.


### Use Short Iterations


In general agile methods use shorter iterations than a lot of
other iterative approaches. At Thoughtworks almost all projects use
iterations of one or two weeks in length. A few of the more experienced Indian developers have
worked at places which use two to three month iterations and they
report that the shorter iterations are much better.


A couple of years ago our distributed projects tended to
prefer two week iterations since they found it was difficult to use
shorter iterations, but this has changed. Now we've learned how to do
one week iterations comfortably on a distributed project.


### Use an Iteration Planning Meeting that's Tailored for Remote
Sites


On most of our projects we've found that a planning meeting
at the beginning of each iteration that involves the whole team really
helps to get everyone coordinated on the next chunk of work. I've
noticed that most of our projects have come up with their own
variation of the Iteration Planning Meeting (IPM) to suit the local
circumstances. (This kind of self-adaptation is an important part of
agile processes.)


A remote team adds its own set of constraints, particularly
when you have awkward time zone issues. However despite the pain of
awkward meeting times, we still find the IPM to be extremely
useful.


Before the IPM the US customer sends narratives for each
scheduled feature (story) which we like to turn into test scripts
before the IPM. During this period any questions are handled by email.
Just before the IPM the development team breaks the features down into
finer grained tasks. These task breakdowns are shared with the US for
feedback.


All of this pre-work shortens the phone call which now
concentrates on any issues that come up from the task breakdown. We
find the calls usually last around a half to a couple of hours. It is
important to keep the actual phone meeting short, as these kinds of
remote meetings are particularly arduous.


### When Moving a Code Base, Bug Fixing Makes a Good Start


Two of our projects involved taking a large (hundreds of
thousands of lines of code) code base and moving substantial
development of the code base to the Bangalore lab. In both of these
projects the Indian team began with a few iterations of bug fixing
before they started adding new functionality.


Starting with bug fixes allowed the Indian team to become
familiar with the code base, before they did substantial work on it,
since bug fixes involve more code reading than changing. Although this
worked well, there is some concern that more experienced people may
consider it to be a stigma to be doing only bug fixes. While some
people may perceive this as a problem I believe that working on bug
fixes or very localized feature changes is one of the best ways to get
familiar with a large new code base.


The nature of communication of bug fixing can also make it
				an easier activity to work with offshore. Onshore teams can spend
				their day mapping out details of bugs, which can be
				communicated to the offshore team and worked on during the
				onshore night. The onshore team can then review the fixes the
				next day. I must stress that this is not more efficient than
				having an on-site team fix the bugs, due to the communication
				difficulty, but it can be a less complicated way of working
				with an offshore team.


### Separate teams by functionality not activity


Much of the traditional thinking on the onshore/offshore
boundaries is based on the activity that people do. So analysis and
design is done onshore, construction done offshore, and acceptance
testing is done onshore. This obviously fits well with the waterfall
model.


We've found that contrary to this, matters improve when we
make the offshore team handle as many activities as possible. So we
prefer to see them do as much analysis and design as possible, subject
to the limitations that the requirements are coming from onshore. When
we do split an effort with onshore and offshore development teams, we
do this along functionality grounds rather than activities. We break
the system into broad modules and let the offshore team tackle some of
these modules. However unlike most groups that do this, we don't make
a big effort to design and freeze the interfaces between these
modules: continuous integration and weak code ownership allow the
module interfaces to evolve as development goes on.


An important part of this is to grow the analyst part of the
offshore team. The more someone local to the developers understands of
the business, the more the development team can develop
efficiently. Instead of having to wait overnight to answer a question,
developers can get answers right away - which removes blocks to progress.
All this means that you have to focus on growing the business knowledge
of the offshore analyst. This takes time, but the local knowledge is a
vital counterpart to the business knowledge onshore.


A corollary to this is to not divide teams by horizontally
				(having one team do presentation and another do database). In
				general I [prefer a functional staff organization](https://martinfowler.com/bliki/PreferFunctionalStaffOrganization.html) - and remote teams exacerbate the problems of
				dividing teams by layers.


The most important thing to remember here is the dominant
				power of [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html) - the structure of the system will mirror
				the structure of the team that built it. That means that it's
				important to separate distributed teams by modules that are as
				loosely couples as possible.


### Expect to need more documents.


Agile methods downplay documentation from the observation
that a large part of documentation effort is wasted. Documentation,
however, becomes more important with offshore development since the
face to face communication is reduced. This work is, in a way, a waste
since it wouldn't be needed if the whole team was co-located. But
given the offshore model, you need to do them - so they are part of
the price of doing things offshore. That's a price in the time for
people to write them, the added time because it's harder for people to
understand many things from a document, and also a price in
frustration when people are using them.


As well as documents, you also have more need for more active
collaboration tools: wikis, issue tracking tools and the like. On the
whole it seems that it's often better to favor tools that impose less
structure, that way the team can fit them better into how they want to
work (one of the reasons that wikis can work so well.)


I always advise teams to check their documents into a
				version control system so people can easily get the most up to
				date material. This is particularly important when you are
				doing remote work.


Whether it's documents or anything else, remember that other
people's templates won't work for you, and you won't come up with the
right scheme at the beginning. Make sure there's plenty of
communication about the form of the documents and how well they are
working. Expect to evolve the structure of documents as you learn what
works best for your team.


> There are two keys to
> successful documentation on agile projects. The first is finding the
> point of âjust enoughâ documentation. This is difficult to determine
> and will vary by project. Fortunately, the iterative nature of agile
> development allows you to experiment until you get it right. The
> second key to successful agile documentation is to not get attached to
> it or have unrealistic hopes of keeping it updated. Documentation must
> be created to serve a specific purpose, and after it has served that
> purpose you'll all probably have more important things to do than keep
> updating the documents. It may seem counter-intuitive, but it's often
> better to produce fresh documentation the next time some is clearly
> required. A side benefit of starting over each time you need to
> document part of your project is that it's great incentive to keep
> your documentation efficient!
> -- [[Simons]](http://www.informit.com/isapi/product_id~%7BA6DD6BC5-B290-4CC5-9F24-67E8A683E36D%7D)


### Get multiple communication modes working early


Different communication tools work for different kinds of
			problems. At the minimum make sure you have a wiki, instant
			messaging, and good telephone connections.


Instant messaging is good for quick questions and answers,
			but a particular strength of IM is that it tells you when people
			are available at their desks. You do have to get into the habit
			keeping your IM status fresh, but that information is always
			useful. We see a surge of communication during overlap hours,
			which is particularly valuable when those overlap hours are short.


Many companies these days block
				instant messaging believing it to be a distraction. It always
				hurts us because it stops ThoughtWorkers asking questions of
				folks on other projects. It particularly hurts offshore
				projects as it removes informal one-to-on contacts.


If it's more than a quick few messages then it's best to
			switch to phones. Make sure that it's easy to just pick up a
			phone. People shouldn't be deterred by fears of the cost of
			phone calls, a phone call will usually save money on
			misunderstands.


We've found a lot of value in video
				presentations. Short lectures about the background of the
				project that can be recorded and sent over to the remote
				team. These are often easier to prepare than a document,
				easier to sit through (if they're not too long) and crucially
				they also help the personal contact, since it's easier to get
				a broader picture of someone from a video than from a
				document. They aren't so good for details, but work better for
				a broad picture.


Email can often be a mixed blessing. In particular we've
found that it's good to discourage person-to-person email in favor of
broadcast newsgroups or mailing lists. It's too easy for a piece of
information not to go to someone who needs it, or be unable to find
it. By posting messages and requests in a newsgroup, everyone can see
the messages and it's easy to search. People find it easy to skip over
threads that they aren't interested in.


Getting multi-cast rather than one-to-one communication can
				also be done with real time tools. A couple of teams have
				reported good effects from using [Campfire](http://www.campfirenow.com/). (IRC could be used
				in a similar way, although I haven't heard it mentioned yet.)


Perhaps the trickiest thing to sort out is how to
				communicate the big picture - the vision of the project. Most
				communication, and discussion about communication,
				concentrates on the day-to-day details. It's important to get
				these right, but there's a danger that in focusing on the
				day-to-day nobody pays attention to the overall vision.


This can hurt because lots of people make habitual small
				decisions based on their perception of the big vision. These
				small decision add up, so if there's no communication of the
				big picture problems can sneak up on you.


This issue is particularly important for
				communicating the business context of a project. Often remote
				communication focuses too much on tactical details - what need
				to be built this week. But many technical decisions need a
				broader strategic context - so it's important for the remote
				team to have a broader picture of the direction the project,
				and the business, wants to take.


This kind of communication is often lacking in on-site
				projects, particularly when there is a lot of organizational
				barriers between business and technology. Remote development
				teams exacerbate this problem - just as distributed
				development exacerbates most communication difficulties.


## Costs and Benefits of Offshore Development


There's still many differences of opinion, both within the general
enterprise software world and within Thoughtworks, about the costs
and benefits of using offshore development. The reason why most people
look to offshore is to reduce costs, noting the significantly lower
rates that you find from offshore vendors. However it's foolish to
look only at rates. Rates are only one component of costs, and in any
case you have to look at the entire return on investment. Most people
in the software industry know, or should know, that productivity
differences between developers are far greater than salary differences
- and even the rate differentials offered by offshore aren't
necessarily greater than that. Offshore work also introduces extra
costs and risks that may offset the rate differential.


The biggest consequence is the effect on communication.
Offshore makes communication harder both due to the distance, which
makes it difficult to meet face to face, and the timezone offset. Both
of these increase the likelihood of building the wrong functionality as
miscommunications  occur over requirements. While techniques such as
using ambassadors tries to reduce it, there's still going to be some
effect. Also the distance between development and business also
reduces the motivation of the development team,since they have no
personal relationship to build on.


Of course a high ceremony organization that uses documents as
the primary communication mechanism will not suffer as much from this.
Essentially their communication has already taken all the damage from
lack of direct contact, so the offshore effect is less notable. Agile
methods try to restore the direct contact in order to improve
communication. Our experience is that even if an agile approach
suffers from the communication difficulties of offshore, it's still
better than a documentation-driven approach.


Another trend may work to help with this problem. Increasingly
companies are moving other business process functions offshore. If a
company moves its accounting function to India, then software to
support them can be built in India more easily than it could be in the
west. If this kind of movement of business work offshore continues,
then Indian development could become the onshore alternative.


Another benefit of offshore that's coming up is the use of 24
hour development to reduce time to market. The benefit that touted is
that by putting hands on the code base at all hours of the day,
functionality gets written faster. Frankly I think this is a totally
bogus argument, since I don't see what adding people does in
India that it wouldn't do by adding them to the onshore team. If I
need to add people, it's more efficient to do it while minimizing the
communication difficulties.


The nugget in the 24 hour development idea is that despite the
tech slowdown it's still not easy to get talented developers. So often
you can't get enough talented developers in the onshore location, so
an offshore team is valuable for their talent rather than any lower
cost.


Among all these differences my point of view is clear: I'm
sitting on the fence!


## The Future of Offshore and Agile


As I write this, offshore development is very fashionable, but
it's still too early to really understand its true strengths and
pitfalls. Certainly anyone doing it because they think they'll get cost
savings similar to the rate differences is seriously deluding
themselves. Some people talk about all software development moving to
the third world in the same way that the steel industry did, others
think that after a period of fascination the offshore industry will
dry up. My crystal ball just shows me what's in front of me, in a
slightly distorted way.


One conclusion is clear, anyone who thinks that onshore
developers will triumph because they are more skilled is very wrong.
We've found that we can hire just as talented developers in India as
we can in North America and Europe.


The weak spots of offshore development come from culture and
distance with the business. Because agile development works best with
close communication and an open culture, agilists working offshore
feel the pain much more than those using plan-driven approaches. But
it's still less pain than the plan-driven methods themselves!


We may never really understand the pros and cons offshore
development. Software development is an activity who's output is
impossible to measure. As such we'll never have hard numbers to prove
one approach better than another. What we will see is growing
qualitative feedback on the benefits of agility and offshore
development - these qualitative assessments will determine if either,
or both, will survive.


---
