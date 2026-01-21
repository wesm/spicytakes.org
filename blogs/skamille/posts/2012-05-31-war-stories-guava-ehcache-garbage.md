---
title: "War Stories: Guava, Ehcache, Garbage Collection"
date: 2012-05-31
url: https://www.elidedbranches.com/2012/05/war-stories-guava-ehcache-garbage.html
word_count: 690
---

We're in the process of moving all of our major business logic out of our clunky Drupal frontend to Java backend services, and we took another big step down that road this week by moving all of the logic for filtering of our product grids to our new integration service. This release was the culmination of months of work and planning that started at the beginning of the year, and it gets us over a major functionality hump. The results are looking good, we've saved almost 3s average page load time for this feature. Yes, that's right, three seconds
*per page load*
.
As you may guess from the title of this post, the release was not entirely smooth for our infrastructure team. The functionality got out successfully, but two hours after we released we started noticing slowness on the pages, and a quick audit showed frequent full GCs on the services. Some rogue caching was being exercised much more than we had seen during load testing. After some scrambling, we resized the machines and restarted the VMs with more memory. Fortunately the cache would only get so big, and we could quickly throw more memory onto the machines (thank the cloud!). Crisis averted, we set to fixing the caching so that we wouldn't hit slow FGCs.
The fix seemed fairly straightforward; take the cache, which was originally caching parameters mapped to objects, and instead just cache the object primary ids. So the project lead coded up the fix, and we pushed it out.
Here's the fix. Notice anything wrong? I didn't. We're big fans of
[Guava](http://code.google.com/p/guava-libraries/)
and use List transformers all over the place in our code base. So we load test that again, and it looks ok for what our load tests are minimally worth, so we push it onto one of our prod boxes and give it a spin.
At first, it seemed just fine. It hummed along, seeming to take less memory, but slowly but surely the heap grew and grew, and garbage collected more and more. We took it out of the load balancer, forced a full GC, and it still had over 600m of active heap memory. What was going on?
I finally took a heap dump and put the damned thing into
[MAT](http://www.eclipse.org/mat/)
. Squinting at it sideways showed me that the memory was being held by
[Ehcache](http://ehcache.org/)
. No big surprise, we knew we were caching things. But why, then, was it so big? After digging into the references via
[one of the worst user interfaces known to man](http://www.eclipse.org/mat/about/path_2_gc_roots.png)
, I finally got to the bottom of an element, and saw something strange. Instead of the cache element containing a string key and a list of strings as the value, it contained some other object. And inside that object was another list, and a reference to something called "function", that pointed to our base class.
As it turns out, Lists.transform is a lazy function. Instead of applying the transformer to the list immediately and returning the results, you get back an object that acts like a list but only applies the transform on the objects as you retrieve them the first time. Which is great for saving a bit of time up front, but absolutely terrible if you're caching the result to save yourself memory. Now, to be fair, Guava tells you that this is lazy in the javadoc:
But not until you get to the third part of the doc, and we are even lazier than Guava in our evaluation. So, instead of caching the list as it is returned from Lists.transform, we call Lists.newArrayList on the result and cache that. Finally, problem solved.
The best part of this exercise was teaching other developers and our ops folks about the
[JVM monitoring tools I've mentioned before](http://whilefalse.blogspot.com/2012/03/java-console-monitoring-basics-j-series.html)
; without jstat -gc and jmap I would have been hard-pressed to diagnose and fix this problem as quickly as I did. Now at least one other member of my team understands some of the fundamentals of the garbage collector, and we've learned a hard lesson about Guava and caching that we won't soon forget.