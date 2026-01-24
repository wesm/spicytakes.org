---
title: "Actual Performance, Perceived Performance"
date: 2008-03-02
url: https://blog.codinghorror.com/actual-performance-perceived-performance/
slug: actual-performance-perceived-performance
word_count: 828
---

If you’ve used Windows Vista, you’ve probably noticed that **Vista’s file copy performance is noticeably worse than Windows XP**. I know it’s one of the first things I noticed. Here’s the irony – Vista’s file copy is based on an improved algorithm and [actually performs *better*](https://web.archive.org/web/20080306033755/http://blogs.zdnet.com/Bott/?p=369&page=2) in most cases than XP. So how come it seems so darn slow?


Let’s start with Mark Russinovich’s typically excellent and exhaustively in-depth analysis of [Vista’s file copy algorithm](https://web.archive.org/web/20080302200209/http://blogs.technet.com/markrussinovich/archive/2008/02/04/2826167.aspx):


> Perhaps the biggest drawback of the [new Vista file copy algorithm], and the one that has caused many Vista users to complain, is that for copies involving a large group of files between 256KB and tens of MB in size, **the perceived performance of the copy can be significantly worse than on Windows XP**. That’s because the previous algorithm’s use of cached file I/O lets Explorer finish writing destination files to memory and dismiss the copy dialog long before the Cache Manager’s write-behind thread has actually committed the data to disk. With Vista’s non-cached implementation, Explorer is forced to wait for each write operation to complete before issuing more, and ultimately for all copied data to be on disk before indicating a copy’s completion. In Vista, Explorer also waits 12 seconds before making an estimate of the copy’s duration and the estimation algorithm is sensitive to fluctuations in the copy speed, both of which exacerbate user frustration with slower copies.


As Mark wryly notes, file copying is not as easy as [it might first appear](https://blog.codinghorror.com/snappy-answers-to-stupid-programming-questions/). As with so many things in life, perception is reality: if users see file copying as slower, it *is* slower. Despite all the algorithmic improvements, in spite of the superior file copy benchmark results, Vista’s file copy performance is worse than Windows XP.


I couldn’t ask for a more perfect example of this dirty little human factors secret: **perceived performance is more important than actual performance**. Fancy copy algorithms won’t necessarily help you build a fast progress bar. But understanding how your users’ brains work definitely will, as illustrated in [Rethinking the Progress Bar](http://chrisharrison.net/projects/progressbars/index.html):


> Humans do not perceive the passage of time in a linear way. This, coupled with the irregular behavior of progress bars, causes human perception of process duration to vary. **An understanding of which behaviors perceptually shorten or lengthen process duration can be used to engineer a progress bar that appears faster, even though the actual duration remains unchanged.** This paper describes an experiment that sought to identify patterns in user perception of progress bar behavior. The results are then analyzed to classify behaviors that perceptually speed up or slow down process execution.


The [study](http://chrisharrison.net/projects/progressbars/ProgBarHarrison.pdf) (pdf) used eight progress behavior functions, then tracked users’ reactions to each one.


![](https://blog.codinghorror.com/content/images/2025/04/image-10.png)


Although **all the progress bars took exactly the same amount of time** in the test, two characteristics made users think the process was faster, even if it wasn’t:

1. progress bars that moved smoothly towards completion
2. progress bars that sped up towards the end


It seems obvious in retrospect why Vista’s file copy design failed so miserably, and needed to be patched up with Service Pack 1. It’s a textbook example of these principles at work:

1. Explorer waits 12 seconds before providing a copy duration estimate, which certainly provides no sense of smooth progress.
2. The copy dialog is not dismissed until the write-behind thread has committed the data to disk, which means the copy is slowest at the end.


The idea that performance is determined largely by the user’s perception rather than actual wall-clock time can be liberating. Like a magician using skillful sleight of hand to perform magic tricks, you can seemingly alter reality. But it can also be frustrating. Even if you get the technical parts right, with hard benchmark data to back you up, subtle human perceptual factors can still negate your work, as those unfortunate Vista developers found out. What’s a poor developer [to do?](https://web.archive.org/web/20080304045442/http://blogs.zdnet.com/Bott/?p=377)


> But are both of us missing the real point of owning and using a PC? Can any stopwatch-based measurement of isolated tasks as performed by individual hardware and software components really measure the worth of a technology investment? I don’t think so.
> This is not a new question for me. Back in the early 1990s, when I was editor of the late, lamented PC Computing, we differentiated our product reviews from those of sister public PC Magazine by focusing on usability. The highly regarded PC Magazine Labs was the quintessential “speeds and feeds” shop. We focused on usability, going to the extreme of spending a small fortune (I still remember the budget battles) building a state-of-the-art usability lab and hiring usability professionals to run it.


Don’t make the same mistake the Vista development team did. Think more holistically than mere benchmarks alone. **Consider the user’s perception of the process, too**. I recommend Tog’s [Maximizing Human Performance](http://www.asktog.com/basics/03Performance.html) as a great starting point.

[file copy](https://blog.codinghorror.com/tag/file-copy/)
[performance](https://blog.codinghorror.com/tag/performance/)
[algorithms](https://blog.codinghorror.com/tag/algorithms/)
[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[cached file i/o](https://blog.codinghorror.com/tag/cached-file-i-o/)
