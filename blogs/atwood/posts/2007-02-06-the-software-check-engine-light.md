---
title: "The Software “Check Engine” Light"
date: 2007-02-06
url: https://blog.codinghorror.com/the-software-check-engine-light/
slug: the-software-check-engine-light
word_count: 619
---

Raymond Chen notes that, in his personal experience, [users don’t read dialogs](https://blog.codinghorror.com/teaching-users-to-read/):


> **How do I make this error message go away? It appears every time I start the computer.**
> RC: What does this error message say?
> User: It says, ‘Updates are ready to install.’ I’ve just been clicking the X to make it go away, but it’s really annoying.
> **Every time I start my computer, I get this message that says that updates are ready to install. What does it mean?**
> RC: It means that Microsoft has found a problem that may allow a computer virus to get into your machine, and it’s asking for your permission to fix the problem. You should click on it so the problem can be fixed.
> User: Oh, that’s what it is? I thought it was a virus, so I just kept clicking No.
> **When I start the computer I get this big dialog that talks about Automatic Updates. I’ve just been hitting Cancel. How do I make it stop popping up?**
> RC: Did you read what the dialog said?
> User: No. I just want it to go away.
> **Sometimes I get the message saying that my program has crashed and would I like to send an error report to Microsoft. Should I do it?**
> RC: Yes, we study these error reports so we can see how we can fix the problem that caused the crash.
> User: Oh, I’ve just been hitting Cancel because that’s what I always do when I see an error message.
> RC: Did you read the error message?
> User: Why should I? It’s just an error message. All it’s going to say is ‘Operation could not be performed because blah blah blah blah blah.’


He wonders [if software should have a Check Engine light](https://web.archive.org/web/20070212035238/http://blogs.msdn.com/oldnewthing/archive/2003/09/01/54734.aspx):


> Automobile manufacturers have learned to consolidate all their error messages into one message called “Check engine.” People are conditioned to take the car in to a mechanic when the “Check engine” light goes on, and let the mechanic figure out what is wrong. Can we have a “Check engine” light for computers? Would it be feasible?


It’s an interesting concept, insofar as it relieves the users from having to look at dialogs they won’t understand anyway. But it seems highly unlikely to me that these users would pay any more attention to a subtle software Check Engine light than they do to the giant, screaming dialogs it’s replacing.


![The 'check engine' light](https://blog.codinghorror.com/content/images/uploads/2007/02/6a0120a85dcdae970b0128776ffac2970c-pi.jpg)


And there’s another problem with the automobile analogy, too. Unlike a car, computers – at least the ones connected to the internet – are perfectly capable of diagnosing and fixing themselves. **The examples Raymond provides shouldn’t have asked the user *anything*; they should have quietly gone about their business.**


If you need to update, do so. if you need to download and apply security patches in the background, do so. If you need to send crash data, do so. Silently. And do it in the background, when the PC is idle – without bothering the user.


If you’re an advanced user who want to change and control this behavior, or view the status of these activities, you can certainly do so through control panels, options dialogs, and event logs. But the rest of the world doesn’t care; they’re relying on your software to do the right thing on their behalf without subjecting them to a barrage of questions they’ll neither read nor understand.


A software check engine light is a mildly less invasive form of [stopping the proceedings with idiocy](https://blog.codinghorror.com/unnecessary-dialogs-stopping-the-proceedings-with-idiocy/). Your software should be [more considerate](https://blog.codinghorror.com/making-considerate-software/) than that.

[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[software updates](https://blog.codinghorror.com/tag/software-updates/)
[computer security](https://blog.codinghorror.com/tag/computer-security/)
