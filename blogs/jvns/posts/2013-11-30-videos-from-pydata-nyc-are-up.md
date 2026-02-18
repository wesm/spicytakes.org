---
title: "Videos from PyData NYC are up!"
date: 2013-11-30
url: https://jvns.ca/blog/2013/11/30/videos-from-pydata-nyc-are-up/
slug: videos-from-pydata-nyc-are-up
word_count: 296
---


The [videos from PyData NYC](http://vimeo.com/pydata/videos) are now
up. In particular, you can now watch the
[video for my IPython Notebook + pandas tutorial](http://vimeo.com/79835526).
I’m not sure how well it translates to video, since it was a pretty
interactive tutorial and I spent a lot of the time running around in
the audience answering questions. The
[IPython Notebook](http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb)
and the
[same notebook on Wakari]([https://www.wakari.io/sharing/bundle/jvns/PyData](https://www.wakari.io/sharing/bundle/jvns/PyData) NYC 2013 tutorial) should be useful, though.


Some talks I enjoyed at PyData NYC:


**[Probabilistic Data Structures for Realtime Analytics](http://vimeo.com/79500848)**
by [Martin Laprise](https://github.com/mlaprise)


I didn’t know too much about probabilistic data structures before this
talk. He explained how Bloom filters work and when it would be
appropriate to use them, and now I know! There’s also an
[IPython Notebook](http://nbviewer.ipython.org/github/mlaprise/pydata2013-pds-talk/blob/master/pydata2013.ipynb).


My main takeaway from this talk was that you can use Bloom filters to
describe a huge amount of data, but not an *unlimited* amount of data
– the size of your Bloom filter depends on how much data you’re going
to put into it. He also described how to set up a Bloom filter where
the elements expire after a certain amount of time.


**[IPython - The Attributes of Software and How They Affect Our Work](http://vimeo.com/79832657)**
by [Brian Granger](https://github.com/ellisonbg)


I wasn’t able to make it to this talk, but everyone was abuzz about
it on Twitter afterwards, so I’m definitely going to watch the video.


**[Python at Datadog - Building High-Volume Data Systems in the Python Ecosystem](http://vimeo.com/79531980)**


At 25:27, he demos how Cython has a tool to automatically colour your
Cython code and show how optimized it is. Whoa. That is the kind of
stuff I go to conferences to learn :)


I didn’t make it to very many talks at the conference, so I’d love to
hear about what else I missed.
