---
title: "Java garbage collection can be really slow"
date: 2016-04-22
url: https://jvns.ca/blog/2016/04/22/java-garbage-collection-can-be-really-slow/
slug: java-garbage-collection-can-be-really-slow
word_count: 633
---


Yes, friends, I know this is news to absolutely nobody. But today I had up-close-and-personal problems with Java garbage collection for the first time so I am going to tell you about it.


So! I was running a program. I set the Java memory limit to 4 gigabytes (`-Xmx4G`). I ran it on a file with one million lines. Done. no problem. Next: 8 million lines. It took… well.. more than 8 times longer. Way longer. Then it crashed with an out of memory error.


I was fine with it crashing (if you’re out of memory, you’re out of memory! I get it!) But why did it take so long to run? I asked [Erik](https://twitter.com/d6) for some help, because he is the best and knows a lot about Java performance.


He suggested this JVM flag: `-XX:+PrintGCDetails`. This is my new favorite JVM flag.


I started the program. It started out by printing out some stuff like this:


```
[GC
    [PSYoungGen: 142816K->10752K(142848K)] 246648K->243136K(375296K),
    0,0935090 secs
]
[Times: user=0,55 sys=0,10, real=0,09 secs]

```


These are “young gen” collections. I still don’t totally understand how the young gen collections work. I know that they only collect new objects, and use a different algorithm from full collections. The most important thing to know is that young gen collections are fast. mine were taking 0.09 seconds and freeing many many megabytes of memory. Maybe a gigabyte? Fast.


Then, things got bad. The program slowed wayyyy down. It would do 0.2 seconds of work, and then some thing like:


```
[Full GC
    [PSYoungGen: 10752K->9707K(142848K)]
    [ParOldGen: 232384K->232244K(485888K)] 243136K->241951K(628736K)
    [PSPermGen: 3162K->3161K(21504K)],
    1,5265450 secs
]
[Times: user=10,96 sys=0,06, real=1,53 secs]

```

- me: PROGRAM. You can’t just stop for 1.5 seconds after working for 0.2 seconds! That makes no sense
- program: uh, yeah i can.


These are full collections that do mark-and-sweep over every object in memory and make sure we collect everything we can. Everything. This can be very very slow (2 seconds is a very long time to stop!).


I thought this was really interesting and surprising. I knew GC was important but did not know that it could bring a program to a screeching halt. But apparently it can!


The many objects in the old generation were still used every time it collected, so it had to constantly iterate over those objects and ask “can I free you yet?” “nope.” “can I free you yet?” “nope.” “can I free you yet?” “nope.”.


### memory pressure


Now I think I understand what memory pressure is on the JVM! If your application is using 3.5GB of memory normally, and has a limit of 4G, then it may constantly need to garbage collect and slow your program waaaaaay down. If you had a memory limit of 20GB, that same program (using the same amount of memory) would be able to run faster because it wouldn’t need to constantly try to garbage collect the same objects all the time.


So this was bad. I do not have a story of redemption for you here yet (Presumably we can make it better by looking at what the objects are and using less objects. Did you know that you can get a histogram of which kinds of objects are taking up all the space with `jmap -histo $pid`? It’s the best.)


But it was interesting! Now we know that garbage collection can ruin your program’s day, what memory pressure is, and that memory pressure is bad.


I read this article about [garbage collection](http://www.infoq.com/articles/Java_Garbage_Collection_Distilled) that I don’t fully understand by Martin Thompson that concludes with


> GC tuning can become a highly skilled exercise that often requires application changes to reduce object allocation rates or object lifetimes.


which is to say “sometimes the only way is to make your program stop allocating so much memory”
