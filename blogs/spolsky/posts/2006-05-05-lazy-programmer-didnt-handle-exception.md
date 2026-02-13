---
title: "Lazy Programmer, Didn’t Handle Exception"
date: 2006-05-05
url: https://www.joelonsoftware.com/2006/05/05/lazy-programmer-didnt-handle-exception/
word_count: 382
---


try()
{
…
}
catch(Exception *)
{
   print(“call customer service”);
}
// i guess i’m done!


I called the numbers listed, and went through several layers of menus and waiting. Of course, the person who answered at Cingular had no idea what to do. He found someone walking around his call center who told him to call some other number. He called that number, went through voice menu hell, and finally got told to call some *other* number. Now he’s calling that, and of course, it’s just ringing the guy next to him, who has no idea what to do, either. Of course they don’t. It’s a friggin’ unhandled exception.


Eventually they got me to another customer service representative who had been trained just to ask me what I was trying to do (add another couple of lines to my account) and do it. That’s not really a solution.


One of the hallmarks of a broken system is when there’s just no possible way that the programmer who is writing code that talks to customers can ever get feedback from those customers about bugs, because the call center is outsourced to a different company than the software development project is outsourced to. Everyone is trying their hardest to do their job but management has set it up so that it’s impossible.


Now, on to wireless companies in the USA. In the last ten years I can’t think of *one time* when a wireless company has been able to handle the basic things I’ve asked for (new service, cancel service, port a phone number) without 45 minutes of unbelievably incompetent service. Over the years I’ve used Sprint, the old AT&T, Cingular, and BellAtlantic, and they’re all pretty much equally messed up. All of them suffer from hard working shlubs who are stuck in a situation created by incompetent managers, who have built esoteric mountains of complicated and brittle systems with a million moving parts, 3/4’s of them outsourced, where it’s simply impossible to get anything done.


**What does your code do to contact you when things go badly wrong? **We use [BugzScout](http://www.fogcreek.com/FogBugz/docs/40/Articles/BugzScout.html) to report unhandled problems directly into our own [FogBugz](http://www.fogcreek.com/FogBugz) database. But even if you call our customer service line you get a human who is sitting right next to the programmer.
