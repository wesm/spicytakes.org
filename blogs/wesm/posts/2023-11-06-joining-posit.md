---
title: "Joining Posit’s Polyglot Data Science Mission"
date: 2023-11-06T00:00:00
tags: ["work", "open source", "posit"]
slug: joining-posit
word_count: 1283
source_file: blog/joining-posit/index.qmd
content_type: blog
---

## Summary

**TL;DR** I am joining [Posit][1] today as a Principal Architect where
I will advocate for the needs of the PyData ecosystem in Posit’s work
as well as continue advancing critical open source initiatives to
accelerate progress in the polyglot [“Data Science without Borders”
mission][2].

In this post, I will review some of the back story of how I got
involved with Posit (known formerly as RStudio) and why I’m betting on
the company as a major player in the data science world.

## Early Connections

I first met [J.J. Allaire][9] and learned about RStudio in May 2012
(which feels like a lifetime ago) at the [R/Finance conference][3] in
Chicago. J.J. had spent the last several years working with Joe Cheng
to build a new open source IDE for R, but the project had not yet
developed into a business. A year earlier, I had taken leave from my
PhD program to spend a self-funded sabbatical year working on pandas
and writing my book [*Python for Data Analysis*][4]. It was still just
the beginning of our journeys as open source entrepreneurs.

At that first meeting over 11 years ago, J.J. and I bonded over a
shared passion for increasing the use of open source software in data
science and statistical computing ecosystems, shifting mindshare away
from popular closed source systems like MATLAB and SAS. From that
perspective, the R and Python communities had a lot more to gain from
collaborating with each other (and thus united against commercial or
closed source alternatives) than competing (other than in friendly or
constructive ways that would promote innovation and progress). It
wasn’t clear yet what form future collaborations might take, and of
course a more pressing problem at the time was figuring out how to
increase the scale of our open source contributions while making it
financially sustainable for ourselves and our families.

2012 was also an eventful time for the Python community. I founded
DataPad with early pandas developer Chang She, and Travis Oliphant and
Peter Wang founded [Anaconda][5]. This was also the year that the
IPython notebook emerged and the nascent data science ecosystem
started working thinking more about cross-language standards to enable
multi-language interactive computing environments.

## Building Open Source, Sustainably

I have written and spoken at length in blog posts, conference talks,
and podcasts about my personal path as an open source project and
community builder and the challenges around the different funding and
support models. I recently detailed how I pursued support for [Apache
Arrow][15] in my blog post announcing my [transition out of my
full-time role with Voltron Data][6]. Building open source sustainably
over a long period of time is difficult, and I’ve found that when I
meet with other open source developers we often spend much more time
talking about project sustainability, funding strategies, and
maintainer burnout as opposed to technology problems we want to solve
or other aspirational project goals. A great book on this topic in
general is Nadia Asparouhova’s [*Working in Public*][7].

When [we announced Ursa Labs in 2018][8], I wrote about the “traps”
associated with different open source funding models. This includes
consulting contracts, depending on a big company, or raising venture
capital. Conflicts often emerge pitting the interests of the open
source projects and communities against the need to generate revenue
and become profitable. Posit is a rare example of a company that has
managed to build a commercially successful business while maintaining
a healthy relationship with the open source communities that it
supports. This has not been an accident, and I think there were a few
key early factors that put them on this path. First, J.J. had been
successful early in his career creating the popular [ColdFusion][19]
web development framework during the dot-com era, and as a result he
was able to work in “bootstrap” mode on the RStudio IDE for several
years to avoid an unhealthy dependence on venture funding. Second, he
brought in a trusted business partner, Tareef Kawaf, to grow the
revenue-generating side of Posit’s business, enabling J.J. to maintain
a mostly technical focus. Lastly, Posit recruited R community leader
Hadley Wickham to become its Chief Scientist in late 2012 to spearhead
the company’s open source developments and to make sure the company
would be a consistent force for good in the open source community.

As I explored different funding strategies for Apache Arrow
development starting in 2016, J.J., Hadley, and Tareef were essential
advisors to me as I navigated the complexities of launching such an
ambitious new project. When [Hadley and I created Feather][10] in
early 2016, we discussed ways for the R and Python communities to work
together for the benefit of the whole open source ecosystem. To do
that, we knew we needed to develop new language-independent computing
frameworks like Arrow and interoperability standards like the Jupyter
kernel protocol which could enable the development of portable
infrastructure for data science.

In early 2018, I reconnected with J.J. and Hadley to explore
partnering with Posit (then still RStudio) to financially support
Apache Arrow development, ultimately leading to the [creation of Ursa
Labs][11]. During these meetings, J.J. shared RStudio’s aspirations to
become a [Public Benefit Corporation][12] (which it ultimately did in
January 2020), adding its “open source data science for public good”
mission to its corporate charter. Another aspiration was to expand its
software efforts to the Python ecosystem and beyond. RStudio made good
on this in July 2022 by becoming Posit, reflecting its larger mission
as “the open source data science company”. I believe the company’s
mantras of technical excellence, sustainable growth, and supporting
the public good position it to be a force for progress and innovation
in the data science world for many years to come.

## Posit, Day Zero

For the last 8 years, I have been focused on building and growing the
[Apache Arrow][15] ecosystem and some related projects like [Ibis][13]
and [Apache Parquet][14]. This has taken place in multiple corporate
auspices (Cloudera and Two Sigma), a not-for-profit industry
consortium (Ursa Labs), and most recently a venture-backed startup
(Voltron Data). Lately, my work creating Apache Arrow and Voltron Data
and getting them off the ground had reached an inflection point where
I felt that I could safely step away from my full-time CTO role. As I
considered how I could best position myself to continue making an
impact in the open source data science ecosystem for a long period of
time, the choice was obvious.

Multi-language technology for data science has come a long way since
my initial forays in open source in 2009 with pandas, and in many ways
it still feels like we are just getting started. I wrote at length
about the [themes of composability, modularity, and reuse][16] for
data systems, and we're seeing many of the same trends in the more
general space of interactive computing. Just as Arrow has brought
about a unified cross-language computing layer for data analytics,
projects like [Jupyter][17] and more recently [Quarto][18] have had a
similar impact on interactive computing and technical publishing,
respectively. Only ten years ago these projects didn't exist, and
today we have already begun to take them for granted.

At Posit, I will be wearing two hats: one as a software entrepreneur
contributing toward the company's continued sustainable growth, and
the other as an open source developer, where you'll see me continue to
support the PyData and Arrow ecosystems and the emerging [Composable
Data Stack][16]. I'm excited to see what comes next.

[1]: https://posit.co
[2]: https://www.youtube.com/watch?v=wdmf1msbtVs
[3]: https://www.rinfinance.com/
[4]: https://wesmckinney.com/book/
[5]: https://www.anaconda.com/
[6]: https://wesmckinney.com/blog/voltron-data-transitions/
[7]: https://www.amazon.com/Working-Public-Making-Maintenance-Software/dp/B08KWR85F8/?&_encoding=UTF8&tag=quantpytho-20&linkCode=ur2&linkId=9dcfec8c0a80e0337a01833af7fec90a&camp=1789&creative=9325
[8]: https://ursalabs.org/blog/announcing-ursalabs/
[9]: https://en.wikipedia.org/wiki/Joseph_J._Allaire
[10]: https://posit.co/blog/feather/
[11]: https://ursalabs.org/blog/announcing-ursalabs/
[12]: https://posit.co/blog/rstudio-pbc/
[13]: https://ibis-project.org
[14]: https://parquet.apache.org
[15]: https://arrow.apache.org
[16]: https://wesmckinney.com/blog/looking-back-15-years/
[17]: https://jupyter.org/
[18]: https://quarto.org/
[19]: https://en.wikipedia.org/wiki/Adobe_ColdFusion