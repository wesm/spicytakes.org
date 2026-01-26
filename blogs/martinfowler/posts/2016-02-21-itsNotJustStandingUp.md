---
title: "It's Not Just Standing Up: Patterns for Daily Standup Meetings"
description: "Daily stand-up meetings have become a common ritual of many teams, especially in Agile software development. However, there are many subtle details that distinguish effective stand-ups and a waste of "
date: 2016-02-21T00:00:00
tags: ["agile"]
url: https://martinfowler.com/articles/itsNotJustStandingUp.html
slug: itsNotJustStandingUp
word_count: 6032
---


## We stand up to keep the meeting short


The daily stand-up meeting (also known as a âdaily scrumâ, a âdaily huddleâ, âmorning roll-callâ, etc.) is simple to describe:


*The whole team meets every day for a quick status update. We stand up to keep the meeting short.*


That's it.


But this short definition does not really tell you the subtle details that distinguish an effective stand-up from a waste of time.


So how can you tell?


For experienced practitioners, when things go wrong with the stand-up, they will instinctively know what to adjust to fix the situation.


For novices, when things go wrong, it is much less likely that they'll figure out what to do... and it’s much more likely that, given no assistance, they will simply abandon the practice altogether.


This would be unfortunate since well-run stand-ups add significant value to teams.


In order to address this, it is important to make explicit the benefits and consequences of common practices for daily stand-ups. These patterns of daily stand-up meetings can help less experienced practitioners as well as remind more experienced practitioners of the reasons behind their intuition.


## What might “good” look like?


Bob Marley’s “Get Up Stand Up” starts up... acting like a Pavlovian bell as the team gets up to wander over to stand in front of the card wall without any additional prompting. That particular song is part of a rotation that plays at the same time in the morning, every day. Some people are moving cards to their correct points in the workflow, including affixing different coloured Post-Its with additional notes. A few interested people outside the direct project team have also wandered by to see how things have progressed.


Noticing that the activity at the wall has stopped, the team
    leader starts a large timer that the team had previously
    purchased; they were interested in how long the daily stand-up
    meeting actually took.


One of the team members steps up to talk about the card on the furthest right of the board, closest to the point of deployment. He’s still having some problems with the deployment script. Another team member suggests that she can help resolve that. The sequence continues from right-to-left, top-to-bottom, people describing what is happening with each of the work items, and others chiming in if they can help resolve obstacles. On the side, the team leader is recording the raised obstacles on the improvement board.


At one point, there is a slightly longer discussion exploring how to deal with a particular problem. Noticing the stall, the team leader subtly raises a finger to interrupt... just before one of the people suggest that they should take it offline.


A short time later all the cards are covered and the team leader asks if anyone else has anything else to share. Someone points out an interesting idea she had about a new feature that would make some of what was planned obsolete. This piques the interest of the product manager who always attempts to attend the stand-ups and they both agree to talk about it after.


The team leader then rolls his eyes as the team starts the traditional ending ceremony... 1... 2... 3... Excelsior! Not his thing, but he had to admit, it ended things on a high note.


People separate and start discussing various things that were raised, including the obstacles, the new ideas, and questions about certain work items.


## The particular set of problems that occur when people attempt to work together


Daily stand-up meetings are a recurring solution to a particular set of problems that occur when a group of people attempt to work together as a team.


Stand-ups are a mechanism to regularly synchronise so that teams...

- **Share understanding of goals.** Even if we thought we understood each other at the start (which we probably didn’t), our understanding drifts, as does the context within which we’re operating. A “team” where each team member is working toward different goals tends to be ineffective.
- **Coordinate efforts.** If the work doesn’t need to be coordinated, you don’t need a team. Conversely, if you have a team, I assume the work requires coordination. Poor coordination amongst team members tends to lead to poor outcomes.
- **Share problems and improvements.** One of the primary benefits of a team versus working alone, is that team members can help each other when someone encounters a problem or discovers a better way of doing something. A “team” where team members are not comfortable sharing problems and/or do not help each other tends to be ineffective.
- **Identify as a team.** It is very difficult to psychologically identify with a group if you don’t regularly engage with the group. You will not develop a strong sense of relatedness even if you believe them to be capable and pursuing the same goals.


## Patterns of daily stand-up meetings


I’ve organised the patterns to answer the following questions:

- Who attends?
- What do we talk about?
- What order do we talk in?
- Where and when?
- How do we keep the energy level up?
- How do we encourage autonomy?


## Who attends?


### All Hands


People and representatives from various areas (e.g., marketing, production support, upper management, training, etc.) wish to know about and/or contribute to the status and progress of the project. Communicating status in multiple meetings and reports requires a lot of duplicate effort.


*Therefore*


Replace some or all of the meetings and reports with the daily stand-up. Anyone who is directly involved in or wants to know about the day-to-day operation of the project should attend the single daily stand-up meeting.


*But*


People not directly involved can disrupt the stand-up if they are unclear about what is expected behaviour. This may be addressed by simply informing new participants and observers of expected norms beforehand.


Not all forms of reporting will be, nor should be, covered by the stand-up format. For example, overall project progress would be better communicated with a [Big Visible Chart](http://xprogramming.com/articles/bigvisiblecharts/) such as burn-down, burn-up, cumulative flow diagram, etc.


### Work Items Attend


***Also Known As:*** Story-focused stand-up


> if the stories are so important to the project, **they** ought to be the ones speaking in the standup
> -- [Brian Marick, âLatour 3: Anthrax and standupsâ](http://www.exampler.com/blog/2007/11/06/latour-3-anthrax-and-standups/)


People are too **Focused on the Runners, not the Baton**. That is, everyone is busy but not necessarily progressing work items.


*Therefore*


Instead of thinking of the daily stand-up as a ritual for the people, think of it as a ritual where the **Work Items Attend** (e.g., [User Stories](https://martinfowler.com/bliki/UserStory.html) in an Agile context) and the people attend only to speak for the work items... since obviously the work items can’t actually talk.


The **Yesterday Today Obstacles** questions may still be used but will be from the perspective of the work item, rather than the person. This also means that not every person may talk. There is no sense of obligation to say anything that is not relevant to progress the work.


Because of the clearer focus, it is more likely for people to raise, and sign- up to remove, obstacles without prompting.


*But*


[The lack of obligation to speak may hide problems with people who are shy or otherwise not inclined to say anything.](http://blog.mountaingoatsoftware.com/should-the-daily-standup- be-person-by-person-or-story-by-story/comment-page-1#comment-23428) This is more difficult to detect with a work-item focus.


## What do we talk about?


### Yesterday Today Obstacles


***Also Known As:*** Three Questions


Some people are talkative and tend to wander off into **Story Telling**. Some people want to engage in **Problem Solving** immediately after hearing a problem. Meetings that take too long tend to have low energy and participants not directly related to a long discussion will tend to be distracted.


*Therefore*


Structure the contributions using the following format:

1. What did I accomplish yesterday?
2. What will I do today?
3. What obstacles are impeding my progress?


These are the minimum number of questions that satisfy the goals of daily stand-ups. Other topics of discussion (e.g., design discussions, gossip, etc.) should be deferred until after the meeting.


Olve Maudal suggested that the questions should be reversed in order to emphasise the correct order of importance:


> Any impediments in your way?
> What are you working on today?
> What have you finished since yesterday?
> -- [Olve Maudal, âDaily Stand-up Meetings - Perhaps the third question should go first?â](http://olvemaudal.wordpress.com/2008/05/15/daily-stand-up-meetings- perhaps-the-third-question-should-go-first/)


Lasse Koskela proposed another form of these questions in order to emphasise that team members should not be **Reporting to the Leader**:


> Each team member updates his peers:
> In turn, each team member provides his peers with 3 pieces of information:
> Things I have done since yesterday's meeting
> Things I am going to get done today
> Obstacles that I need someone to remove
> -- [Lasse Koskela, âOn Scrum and the curse of the three questionsâ](http://radio.javaranch.com/lasse/2006/05/07/1147034972559.html)


Jonathan Rasmussen offered different wording in order to change the dynamic of the stand-up:


> What you did to change the world yesterday
> How you are going to crush it today
> How you are going to blast through any obstacles unfortunate	enough to be standing in your way
> Answering these types of questions completely changes the dynamic of the stand-up. Instead of just standing there and giving an update, you are now laying it all the line and declaring your intent to the universe.
> -- [Jonathan Rasmusson, The Agile Samurai](https://www.amazon.com/gp/product/1934356581/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1934356581&linkCode=as2&tag=martinfowlerc-20)


There are also a number of teams that have added additional questions.


[Buffer added a section where people share something they're working on to improve themselves.](http://joel.is/an-invitation-to-come-and-hack-on-buffer/)


Thomas Cagley suggests [trolling for risks](https://tcagley.wordpress.com/2014/07/18/stand-up-meetings-add-ons/).


Mark Levison has found it useful to add more targeted improvement questions. The last two questions would be changed to match the specific context.


> What did you complete yesterday?
> What do you commit to today?
> What are your impediments/obstacles?
> What Code Smell/Missing Unit Test/... did you spot yesterday?
> What improvement did you make to the code yesterday?
> -- [Mark Levison, âDaily Stand-Up Variationsâ](https://agilepainrelief.com/notesfromatooluser/2011/01/daily-stand-up-variations.html#.VsoT4ZMrLeQ)


*But*


The structure is not as important as the information the answers to the questions provide. If the information is provided in a less structured protocol, it is not important to stick to a checklist. As teams mature, you may find you want to adjust the structure, which is reflective of how this pattern has already evolved.


The larger question is whether **Yesterday Today Obstacles** is creating too much of a focus on personal commitment versus paying attention to the right things... which leads to **Walk the Board**.


### Improvement Board


***Also Known As:*** Blockage Board, Impediment Board, Kaizen Newspaper


Obstacles raised in the stand-up are not removed or otherwise addressed in a timely fashion.


*Therefore*


Post raised obstacles to an **Improvement Board**. This is a publicly visible whiteboard or chart that identifies raised obstacles and tracks the progress of their resolution. An **Improvement Board** can be updated outside of stand-ups and serves as a more immediate and perhaps less confronting way to initially raise obstacles. A common mistake is to not write large enough to allow people to read the blockages from a distance.


The simple act of writing an issue down and therefore explicitly acknowledging it is a very reliable way to reduce drawn out conversations. So even if not everyone agrees that any particular item is an obstacle, it is worth simply writing it down for discussion after the meeting has ended.


Including an occurrence count with each raised obstacle highlights which issues are generally more important to deal with first.


The board design can vary in a few ways. For example a table structure such as the following:



| Problem | Count | Containment | Countermeasure | Status |
| Name of problem | Ongoing count of occurrences | Short-term solution | Long-term solution based on root cause analysis | Plan - Do - Check - Act |



Another style is more like a task board:



| Todo | In Progress | Done |
| Index cards representing raised obstacles | Obstacle cards move here when we’re actively working on them | Obstacle cards move here when we’ve resolved them |



*But*


The **Improvement Board** risks devolving into a whinging board if too many obstacles are raised on it that the team has no influence on resolving.


## What order do we talk in?


### Last Arrival Speaks First


During a stand-up, attendees need to know who is supposed to speak first. Having the facilitator decide who should speak first is a subtle though definite force against self-organisation. The team should know without intervention who speaks first.


*Therefore*


Agree that the **Last Arrival Speaks First**. This is a simple rule that also has the added benefit of encouraging people to be punctual about showing up for the stand-up.


*But*


The last arrival is also likely to be the person who is least prepared to start off the meeting well.


### Round Robin


During a stand-up, attendees need to know who is supposed to speak next. Having a facilitator decide who speaks next is a subtle though definite force against self-organisation. The team should know without intervention who speaks next.


*Therefore*


Use a simple predetermined rule like a **Round Robin** to determine who should go next. It doesn't matter if it is clockwise or counter-clockwise. What does matter is that the team runs the meeting, not the facilitator or manager.


### Pass the Token


With simple, predictable ordering mechanisms (e.g., **Round Robin**), it is very easy for participants to ignore other speakers until it is closer to their turn. There may be a tendency to think of other things rather than pay attention to what others are saying.


*Therefore*


Introduce an unpredictable ordering mechanism, like tossing a speaking token (e.g., a ball) to determine who should speak next. Having a speaking token also simplifies deciding who speaks first as it will be the person who happens to have retrieved the token (or the first person s/he tosses the token to).


Tossing something around introduces a bit of fun to the daily stand-up ritual and thus serves as a good infection mechanism for other observing teams.


I first learned of this pattern on a project I was on with Simon Stewart. We used a small juggling ball but almost anything can be used as token. Other teams have used [rugby balls](http://edgibbs.com/2006/08/14/passing-a-rugby-ball-in-standups/) or even [plush toys](http://kanemar.wordpress.com/2006/05/13/controling-the-flow-of-daily- meetings-with-a-team-mascot/).


*But*


With larger teams, it may become difficult to remember who has already spoken. In those cases, it may be easier to stick to simpler mechanisms like **Round Robin**.


Depending on the culture of the organisation or even team, tossing a ball around may also be seen as unprofessional and would create an unnecessary negative perception of the underlying ritual.


### Take a Card


During a stand-up, attendees need to know who is supposed to speak first and after that, who is supposed to speak next. Having a facilitator decide who should speak is a subtle though definite force against self-organisation. The team is not keen on **Pass the Token** because they typically have coffee cups in their hands.


*Therefore*


[Have each team member **Take a Card** to determine which order to speak](http:// web.archive.org/web/20090526072425/http://www.robbyonrails.com/articles/2006/05/29/the- daily-stand-up-part-2). Imagine a stack of cards, each of which has a number on it. As each team member comes to the meeting, they can select a card which then tells them what order to speak in.


### Walk the Board


***Also Known As:*** Walk the Wall


> [S]tandups keep everyone busy. [W]alking the board keeps everyone focused on the most important things.
> -- Bret Pettichord via Twitter


> Another issue with the conventional format is that tasks or workstreams aren't discussed coherently; instead, each subject comes up briefly depending on the order in which team members speak. This can make it hard to tell what's really going on.
> -- [Dave Nicolette, âAn alternative format for the daily stand-upâ](http://web.archive.org/web/20090611160352/http://dnicolet1.tripod.com/ agile/index.blog?entry_id=1900488)


People are more focused on being busy than actually progressing the work so you switched to a model where **Work Items Attend** rather than people, however, even with this work item focused stand-up, it is still difficult to understand what is happening when using typical ordering mechanisms like **Round Robin** or **Pass the Token**.


*Therefore*


**Walk the Board**, that is, structure the stand-up by walking through each work item that is displayed on your visual management board.


Most Agile and Lean teams will use a visual management system to expose what is being worked on. For Agile software development, this might be called a “task board”, “story wall”, or “Kanban board”. These boards will present a process that the work items will move through. Progress is typically represented by physically moving cards across the board. Ideally, vertical positioning will indicate priority.


With this board in place, the stand-up moves through each work item from end of process to start of process (e.g., right-to-left) and from highest-to-lowest priority (e.g., top-to-bottom). You may even explicitly indicate on the board what sequence should be used.


Pawel Brodzinski proposed a [default sequence](http://brodzinski.com/2011/12/effective-standups.html):

1. Blockers
2. Expedite or emergency items
3. Items that haven't moved since last standup (likely to be stuck)
4. Everything else by priority


*But*


Obviously having a board is a pre-requisite which not all teams will have. In that case, a person-by-person structure is more appropriate.


**Walk the Board** has a much greater tendency to succumb to **Reporting to the Leader** if **Rotate the Facilitator** or some other pattern for self-organisation is not also applied.


## Where and when?


### Meet Where the Work Happens


> Do the meeting in the gemba, not a conference room.
> -- [Marc Graban, âVideo of a Daily Huddle at Everett Clinicâ](http://www.leanblog.org/2010/08/video-of-a-daily-huddle-at-everett-clinic/)


The workplace has many memory triggers about what is going on.


We also don’t want the daily meeting to require a lot of overhead coordinating, finding, and walking to rooms.


*Therefore*


**Meet Where the Work Happens**, not in a meeting room. If you have a “story wall” or “Kanban board”, meet in front of that.


*But*


Other people nearby may find the noise of the meeting disruptive. This typically indicates underlying poor workspace design but must still be acknowledged.


### Same Place, Same Time


We want the team to have a sense of ownership of the stand-up. We also want interested parties to be able to drop by to observe a stand-up to avoid having to schedule yet another status meeting. This is difficult if any particular team member is allowed to force a delay or change of location of the stand-up.


*Therefore*


Have the team agree on and run the daily stand-up at the **Same Place, Same Time**. Do not wait for stragglers, including architects and managers. The meeting is for the whole team, not for any particular individual. This is especially important if you **Use the Stand-up to Start the Day**.


Some stricter teams may impose a “fine” for latecomers. I tend to be wary of any kind of punishment mechanism and prefer discussion.


*But*


**Same Place, Same Time** is not intended to be blindly inflexible. The important thing is for the start time to be mostly consistent and rescheduling to be rare. If rescheduling is required often, it may be an indication that the start time should change. If a particular location is inconvenient for everyone to get to, it's probably an indication the location should change.


### Use the Stand-up to Start The Day


The daily stand-up meeting provides focus and awareness of outstanding issues. If it occurs late in the day, this focus and awareness is wasted.


*Therefore*


**Use the Stand-up to Start the Day**. With flexible work hours, not every team member will arrive at work at the same time. A common practice with “flex-time” is to use a set of core working hours. The start time should be at the start of these core working hours. Similarly, if team members need to arrive later for personal reasons (e.g., need to drop off kids at school), the start time should be set at a time so that everyone can attend.


*But*


There may be a tendency not to work on any project-related tasks until the stand-up. If the **Stand-up Meeting Starts the Day... Late**, this slack time may be significant. To some extent, this may simply be used as an opportunity to check e-mail, fill in timesheets, etc. but it may be worth investigating removing the stand-up as a “start of day” ritual by scheduling it later in the day.


### Don't Use the Stand-up to Start the Day


The stand-up tends to serve as the ritual to set focus for the day, especially if you **Use The Stand-up to Start the Day**. Because of this, team members tend not to work on features until the stand-up. When the meeting is not actually held first thing, this tendency may have a significant impact on productivity.


*Therefore*


**Don’t Use the Stand-up to Start the Day**. Schedule the daily stand- up meeting far enough into the day that it will not be psychologically associated as starting the day.


*But*


If the daily meeting doesn't start the day, then it can no longer be used as a shared ritual to set team focus at the start the day. Depending on the team, this price may not be worth the apparent increase in efficiency.


When there are many project using stand-ups, it is possible that multiple stand-ups are occurring simultaneously. Observers interested in multiple projects may want to change stand-up times to allow them to be able attend. This is problematic since it risks the sense of ownership for the team if an observer can force a stand-up to adjust to his/her schedule. Nevertheless, this must also be a consideration when deciding when to have the daily stand-up.


## How do we keep the energy level up?


### Huddle


> The problem that I frequently see crop up is that people have a tendency to treat the Daily Stand-up as simply individual reporting. “I did this . . . I’ll do that”—then on to the next person. The more optimum approach is closer to a football huddle.
> -- [Jeff Sutherland, âThe Origin of The Daily Stand-upâ](https://www.linkedin.com/pulse/20140926150354-136414-the-origin-of-the-daily-stand-up)


Volume of speech affects attentiveness as well as effectiveness of communication. Physical distance changes the level of volume required to communicate well. Some people don't speak loudly and don't feel comfortable doing so.


Volume of speech affects attentiveness as well as effectiveness of communication. Physical distance changes the level of volume required to communicate well. Some people don't speak loudly and don't feel comfortable doing so.


*Therefore*


The stand-up should be more of a **Huddle** than a meeting. If it's difficult to hear, bring everyone closer. Beyond allowing for a more relaxed speaking volume, being physically closer tends to cause participants to be more attentive on their own. Being able to stand physically closer is also an expression of greater trust within the team.
			If the stand-up is a new thing, it's usually enough to use hand gestures to wave people in and say something to the effect of “Let's bring it in”. If the size of the circle has been established for a while, consider explaining the reasons for closing the circle before trying to shrink it.


*But*


The team must balance closeness with personal comfort zones. Even on
			a very trusting team, there is a point when people are just standing too close for comfort. Symptoms tend to be participants that are tense and/or fidgety.


### Stand Up


Some people are talkative and tend to wander off into **Story Telling**. Some people want to engage in **Problem Solving** immediately after hearing a problem. Meetings that take too long tend to have low-energy and participants not directly related to a long discussion will tend to be distracted.


*Therefore*


Have all attendees **Stand Up** during the meeting. Use standing up to link physical with mental readiness. Physical discomfort will also remind attendees when a meeting is taking too long. A simple way to encourage this is to simply hold the meeting where there are no chairs.


*But*


Standing up tends to cause meetings to shorten, but does not guarantee that they will shorten to an optimal length. People may learn to cope with the discomfort instead of taking a more appropriate response. Also if the meetings are *not* taking too long nor wandering off-topic, standing up is an unnecessary ritual.


### Fifteen Minutes or Less


Most people will wander mentally when they are in long meetings. A long, droning meeting is a horrible, energy-draining way to start the day. A specific number helps remind us when to consider adjustment to reduce the time of the meeting.


*Therefore*


Keep the daily stand-ups to **Fifteen Minutes or Less**. As a general rule, after fifteen minutes, the average person's mind is going to wander which doesn't help with setting focus.


*But*


Fifteen minutes may even be too long for smaller teams. Because of the mind-wandering effect, even for larger teams, fifteen minutes is a good limit. Also, it is also possible to have a meeting that is too short where on ending, the attendees still have no idea what's going on nor who to talk to in order to find out.


### Signal the End


After the last person has spoken, the team may not immediately realise that the meeting is over. The gradual realisation that it's time to walk away doesn't end the meeting on a high note and may contribute to **Low Energy**.


*Therefore*


**Signal the End** of the stand-up with a throwaway phrase (e.g., [âWell, enjoy your lunch everyone.â](http://edgibbs.com/2006/08/07/signaling-the-end-of-a-standup/)) or some other action.


### Time the Meetings


It is difficult to qualitatively judge whether a stand-up is taking too long, especially if it only gradually increases in length.


*Therefore*


**Time the Meetings** and publish the results. Most of the time, attendees just don't realise the impact of **Story Telling**, not being prepared to Take It Offline, or not preparing have on how long the meeting will take. Make it quantifiable.


*But*


As with all measures, timing the meetings shouldn't be introduced unless there is an actual goal to accomplish due to a problem with energy levels. Once the goal is accomplished, the measurement should be dropped. Measuring for no particular reason leads to suspicion and metrics apathy.


Time is a proxy for energy, attention, and pace. Pay attention more to those things than the time.


### Take it Offline


Some people want to engage in **Problem Solving** immediately after hearing a problem. Meetings that take too long tend to have low-energy and participants not directly related to a long discussion will tend to be distracted. It is still important to acknowledge that further discussion will be required to solve the raised problem. Some people may find it uncomfortable to enforce the structure of the stand-up by interrupting.


*Therefore*


Use a simple and consistent phrase like “**Take It Offline**” as a reminder that such discussions should take place outside of the daily stand-up. If the discussion was **Socialising**, nothing more is required. If the discussion was **Problem Solving**, the facilitator (and eventually just the team) should ensure that the right people are nominated or sign up to deal with the issue later.


Alternatively, some teams use more indirect signaling.


For example, Mike Cohn described one that uses [a rubber rat to indicate âwe're going down a ratholeâ](http://www.marketplace.org/2012/02/20/life/hate-those-endless-meetings-try-standing).


Benjamin Mitchell described a Two Hand Rule:


> ...if anyone thinks the current conversation has gone off topic, or is no longer effective, then they raise a hand. Once a second person raises a hand then that’s a sign to stop the conversation and continue with the rest of the stand up. Those speaking can continue the conversation after the stand up has finished.
> -- [Benjamin Mitchell, âStuck in an overlong Agile stand up? Try the two hands ruleâ](http://blog.benjaminm.net/2012/02/23/overlong-agile-stand-up-two-hand-rule/)


*But*


There is a difference between **Problem Solving** and a clarifying question. Information that is not understood is not useful. The extent upon which clarifying questions are allowed should vary depending on how large the team is and whether it will impact **Fifteen Minutes or Less**.


## How do we encourage autonomy?


### Rotate the Facilitator


Team members are **Reporting to the Leader**, that is, they're only talking to the meeting facilitator instead of each other. Only the meeting facilitator is raising and addressing process issues related to the stand- up. We want the team to take ownership of the stand-up and this requires removing any dependence on a single facilitator.


*Therefore*


**Rotate the Facilitator**. Rotate assignment of a role responsible for ensuring people attend the stand-up and stick to the agreed upon rules.


*But*


Teams that are not experienced with stand-ups benefit greatly from having a coach experienced in the process. It is more that the team should be weaned into taking greater control of the stand-up. At some point, no explicit facilitator should be required at all.


### Break Eye Contact


Team members are **Reporting to the Leader**, that is, they're only talking to the meeting facilitator instead of each other. We want the team to take ownership of the stand-up and this requires removing any dependence on a single facilitator.


*Therefore*


The facilitator should **[Break Eye Contact](http://radio.javaranch.com/lasse/2006/05/07/ 1147034972559.html#comment1147110635098)** as a subtle way of reminding the speaker that s/he should be addressing the team, not just one person. One way to do this is to [move around so that the current speaker can't see the facilitator](http://www.netobjectives.com/podcasts/last20060719_podcasts.mp3).


## How do we know when a stand-up is going poorly?


> I endured regular stand-up meetings for three years. What made the meetings most painful was my boss (I'll call him Wally). His main reason for the stand-up meeting was not to increase efficiency or embrace XP as much as it was to shorten human interaction beyond anything directly related to the work product. ... For Wally, however, the stand-up meeting (like the 7 a.m. Monday meeting and the 5 p.m. Friday meeting) was a loyalty test designed to reinforce the employer- employee relationship.
> -- [Phillip A. Laplante, âStand and Deliver: Why I Hate Stand-Up Meetingsâ](http://queue.acm.org/detail.cfm?id=957730)


There are stand-up “smells” which are pretty good indicators that things are going wrong. It is important to note that even if you have no smells, this does not mean the stand-up is going right. It just means that it doesn't stink.


Most of the following smells are linked back to the previous patterns. For those that are not, the underlying issues tend to be more subtle or outside the scope of the daily stand-up, and people will have to come up with their own solutions.


### Focused on the Runners, not the Baton


People are too focused on what they are doing but neglect to consider whether their activities are actually progressing the work. Reframe the stand-up such that the **Work Items Attend**.


### Reporting to the Leader


Team members are facing and talking to the manager or meeting facilitator instead of to the team. This indicates that the daily stand-up is for the manager/facilitator when it is actually supposed to be for the team. There are various ways to break this dependence: **Rotate the Facilitator**, **Break Eye Contact**, change the form of **Yesterday Today Obstacles**, use **Pass the Token**, etc.


### People are Late


This is directly addressed by **Same Place, Same Time**, but as mentioned may indicate that the stand-up is being held at the wrong time or at the wrong place.


There are other patterns to respond to this such as imposing a fine. However, I generally would not recommend them as they imply that the issue is about extrinsic motivation when it is much more likely to be something else.


### Stand-up Meeting Starts the Day... Late


Because the stand-up is seen to start the work day, no work is done before the stand-up. Depending on how late in the morning the stand- up is, this can have a significant impact on available working hours. This leads to **Don't Use the Stand-up to Start the Day**.


### Socialising


One of the goals of the stand-up is to increase team socialisation. However, the daily stand-up is not intended for team members to “catch up” with each other on non project-related matters. It's difficult to provide examples of this since the degree to which socialising passes from team-building to distracting varies from team to team. The threshold can be detected from the behaviours of participants not directly involved in the socialisation. If their energy levels remain high, then it's probably just team-building; if their energy levels drop, then **Take It Offline** and perhaps provide another forum to act as a [Water Cooler](http://web.archive.org/web/20070103031934/http://www.easycomp.org/cgi-bin/ OrgPatterns?TheWaterCooler).


### I Can't Remember


> What did I do yesterday?... I can't remember... What am I doing today?... I dunno...


Lack of preparation causes slower pace which causes lower energy. It also risks failing **Fifteen Minutes or Less**, which further reduces energy levels.


A nice way to bypass this problem is to switch to a stand-up where **Work Items Attend** and we **Walk the Board**.


Otherwise, this is a matter of expectation of responsibility to know the answers for **Yesterday Obstacles Today**.


### Story Telling


Instead of providing a brief description of an issue, the participant provides enough details and context to cause others to tune out. The general rule is to identify obstacles during the stand-up and discuss the details after the stand-up. This can be summarised as “Tell the headline, not the whole story” or **Take it Offline**.


### Problem Solving


> It’s a time to raise issues and surface ideas, not a time for in-depth problem-solving.
> -- [Marc Graban, âVideo of a Daily Huddle at Everett Clinicâ](http://www.leanblog.org/2010/08/video-of-a-daily-huddle-at-everett-clinic/)


The key to keeping the stand-ups **Fifteen Minutes or Less** is to limit the **Story Telling** and not succumb to **Problem Solving** during the meeting. **Take it Offline**.


### Low Energy


Could indicate a slow-down of pace due to **Story Telling**, **Problem Solving**, etc. In which case **Take it Offline**. Could be simply a matter of team size. Could be the time of day which suggests trying the alternative of **Use the Stand-up to Start the Day** and **Don't Use the Stand-up to Start the Day**.


### Obstacles are not Raised


***Also Known As: ***[Travelogue](http://blog.jbrains.ca/permalink/stand-updaily-scrum-focus-on-achievement-and-commitment)


There may be several reasons for obstacles not being raised. Not remembering, high pain threshold, lack of trust in raising issues (because **Obstacles are not Removed**), no convenient way of raising issues, etc. The facilitator should take care to encourage people to raise obstacles.


Introducing an **Improvement Board** may also provide a less confronting medium. [Retrospectives](http://www.retrospectives.com/) are an effective way of discovering the underlying reason why **Obstacles are not Raised**.


### Obstacles are not Removed


With the exception of a blaming environment, the surest way to stop people from raising obstacles is to not remove them. To make it difficult to forget and/or ignore obstacles, track them publicly with an **Improvement Board**.


### Obstacles are Only Raised in the Stand-up


Stand-ups act as a safety net. At worst, an obstacle will be communicated to the greater team within one day. However, doing stand-ups is not intended to stop issues from being raised and resolved during the day. Introducing an alternative medium to raise obstacles such as an **Improvement Board** may help. If not, underlying reasons may be discovered using retrospectives.


## It’s really just standing up together every day


Hopefully this paper has provided some more insight into the subtle details of effective stand-up practices and also common problem indicators. It should be clear that a daily stand-up is not just standing up together every day.


At the end of the day, it’s important to not be too concerned about having every pattern or even having some of the smells. Remember the problems we're trying to solve. Are people energised? Are people sharing problems and ideas? Are people focused on our objectives? Are people working together as a team? Does everyone know what’s going on?


If you can answer those questions in the affirmative, the meeting is probably going okay. After all, it's really just standing up together every day.


---
