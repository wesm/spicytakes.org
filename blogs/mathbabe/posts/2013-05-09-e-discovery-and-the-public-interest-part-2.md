---
title: "E-discovery and the public interest (part 2)"
date: 2013-05-09
url: https://mathbabe.org/2013/05/09/e-discovery-and-the-public-interest-part-2/
word_count: 428
---


Yesterday I wrote [this short post](https://mathbabe.org/2013/05/08/e-discovery-and-the-public-interest/) about my concerns about the emerging field of e-discovery. As usual [the comments](https://mathbabe.org/2013/05/08/e-discovery-and-the-public-interest/#comments) were amazing and informative. By the end of the day yesterday I realized I needed to make a much more nuanced point here.


Namely, I see a tacit choice being made, probably by judges or court-appointed “experts”, on how machine learning is used in discovery, and I think that the field could get better or worse. I think we need to urgently discuss this matter, before we wander into a crazy place.


And to be sure, the current discovery process is fraught with opacity and human judgment, so complaining about those features being present in a machine learning version of discovery is unreasonable – the question is whether it’s better or worse than the current system.


**Making it worse: private code, opacity**


The way I see it, if we allow private companies to build black box machines that we can’t peer into, nor keep track of as they change versions, then we’ll never know why a given set of documents was deemed “relevant” in a given case. We can’t, for example, check to see if the code was modified to be more friendly to a given side.


Besides the healthy response to this new revenue source of competition for clients, the resulting feedback loop will likely be a negative one, whereby private companies use the cheapest version they can get away with to achieve the best results (for their clients) that they can argue for.


**Making it better: open source code, reproducibility**


What we should be striving for is to use only open source software, saved in a repository so we can document exactly what happened with a given corpus and a given version of the tools. It will still be an industry to clean the data and feed in the documents, train the algorithm (whilst documenting how that works), and interpreting the results. Data scientists will still get paid.


In other words, instead of asking for interpretability, which is a huge ask considering the massive scale of the work being done, we should, at the very least, be able to ask for *reproducibility* of the e-discovery, as well as transparency in the code itself.


Why reproducibility? Then we can go back in time, or rather scholars can, and test how things might have changed if a different version of the code were used, for example. This could create a feedback loop crucial to improve the code itself over time, and to improve best practices for using that code.
