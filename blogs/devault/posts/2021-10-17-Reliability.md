---
title: "Software developers have stopped caring about reliability"
date: 2021-10-17
url: https://drewdevault.com/2021/10/17/Reliability.html
slug: Reliability
word_count: 1016
---

Of all the principles of software engineering which has fallen by the wayside in
the modern “move fast and break things” mentality of  assholes  modern
software developers, reliability is perhaps the most neglected, along with its
cousin, robustness. Almost all software that users encounter in $CURRENTYEAR is
straight-up broken, and often badly.

Honestly, it’s pretty embarassing. Consider all of the stupid little things
you’ve learned how to do in order to work around broken software. Often
something as simple as refreshing the page or rebooting the program to knock
some sense back into it — most users can handle that. There are much
stupider problems, however, and they are  *everywhere* . Every morning, I boot,
then immediately hard-reboot, my workstation, because it seems to jigger my
monitors into waking up properly to do their job. On many occasions, I have used
the browser dev tools to inspect a broken web page to figure out how to make it
do the thing I want to do, usually something complicated like submitting a
form properly (a solved problem since 1993). 1

When the average person (i.e. a non-nerd) says they “don’t get computers”, I
believe them. It’s not because they’re too lazy to learn, or because they’re
backwards and outdated, or can’t keep with the times. It’s because computers are
hard to understand. They are enigmatic and unreliable.  **I**  know that when my
phone suddenly stops delivering SMS messages mid-conversation, it’s not because
I’ve been abandoned by my friend, but because I need to toggle airplane mode to
reboot the modem.  **I**  know that when I middle click a link and “javascript:;”
opens in a new tab,  an asshole  a developer wants me to left click it
instead. Most people don’t understand this! You and I, dear reader, have built
up an incredible amount of institutional knowledge about how to deal with broken
computers. We’ve effectively had to reverse engineer half the software we’ve
encountered to figure out just where to prod it to make it do the thing you
asked. If you don’t have this background, then computers are a nightmare.

It’s hard to overstate just how much software developers have given the finger
to reliability in the past 10 years or so. It’s for the simplest, silliest
reasons, too, like those web forms. My web browser has been perfectly competent
at submitting HTML forms for the past 28 years, but for some stupid reason some
 asshole  developer decided to reimplement all of the form semantics in
JavaScript, and now I can’t pay my electricity bill without opening up the dev
tools. Imagine what it’s like to not know how to do that. Imagine if you were
blind.

Folks, this is not okay. Our industry is characterized by institutional
recklessness and a callous lack of empathy for our users. It’s time for a
come-to-jesus moment. This is our fault, and yes, dear reader, you are included
in that statement. We are personally responsible for this disaster, and we must
do our part to correct it.

This is what you must do.

You must prioritize simplicity. You and I are not smart enough to be clever, so
don’t try. As the old saying goes, there are two kinds of programs: those simple
enough to obviously have no bugs, and those complicated enough to have no
obvious bugs. It is by no means easier to make the simpler kind, in fact, it’s
much more difficult. However, the simpler the system is, the easier it is to
reason about all of its states and edge cases. You do not need a
JavaScript-powered custom textbox widget. YOU DO NOT NEED A JAVASCRIPT-POWERED
CUSTOM TEXTBOX WIDGET.

On the subject of state, state is the language of robustness. When something
breaks, it’s because a state occured that you didn’t plan for. Think about your
program in terms of this state. Design data structures that cannot represent
invalid states (within reason), and then enumerate each of those possible states
and  *check*  that your application does something reasonable in that situation.

Identify your error cases, plan for them, implement that plan, and then  *test
it* . Sometimes things don’t work! Most languages give you tools to identify
error cases and handle them appropriately, so use them. And again, for the love
of god,  *test it* . If you commit and push a line of code that you have not
personally watched run and work as expected, you have failed to do your job
properly.

Prefer to use proven technologies. If you use unproven technologies, you must
use them scarcely, and you must  *personally*  understand them at an intimate
level. If you haven’t read the source code for the brand-new database engine you
heard about on HN two weeks ago, you shouldn’t be putting it into
production. 2

Finally, stop letting economics decide everything you do. Yes, developers have
finite time, and that time costs. Yes, users with annoying needs like
accessibility and internationalization are more expensive to support than the
returns they produce.  *You need to pay for it anyway* . It’s the right thing to
do. We can be profitable  *and*  empathetic. Don’t think about rushing to market
first, and instead prioritize getting a  *good product*  into your user’s hands.
Our users are not cattle. It is not our job to convert attention into money at
their expense. We need to treat users with respect, and that means testing our
goddamn code before we ship it.

Do an exercise with me. Grab a notepad and make a note every time you encounter
some software bug in production (be it yours or someone else’s), or need to rely
on your knowledge as a computer expert to get a non-expert system to work.
 [Email me](mailto:sir@cmpwn.com)  your list in a week.

1. I often also end up using the dev tools to remove the rampant ads, spyware, nagbars, paywalls, newsletter pop-ups, and spam. Do not add this shit to your website. Don’t you *dare* write that code. ↩︎
2. If you don’t have *access* to the source code, then you definitely should not be using it. ↩︎
