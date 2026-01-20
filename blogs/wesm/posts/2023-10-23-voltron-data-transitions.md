---
title: "Voltron Data Update: Transitions"
date: 2023-10-23T00:00:00
tags: ["startups", "work"]
slug: voltron-data-transitions
word_count: 2340
source_file: blog/voltron-data-transitions/index.qmd
content_type: blog
---

## Summary

**TL;DR** I am transitioning out of my full-time CTO role at [Voltron
Data][1] so that I can expand my portfolio of entrepreneurial and open
source data projects. While no longer serving in a full-time
operational role, I will remain engaged as a Senior Advisor and will
continue driving forward work to enable fast and interoperable
analytical data systems.

In this post I will offer some highlights from the last 8 years since
the founding of [Apache Arrow][2] and [Ibis][3] in 2015, from the
creation of the not-for-profit [Ursa Labs][4] to founding [Ursa
Computing][5] and [Voltron Data][6], eventually [raising over $115M in
venture capital][7] and making massive investments in the emerging
open source [Composable Data Stack][9].

## 2015 to 2020: Cloudera, Two Sigma, Ursa Labs, and Ursa Computing

In my [September 15-year retrospective blog post][8], echoing our
joint ["Composable Data Management System Manifesto"][9] from VLDB
2023, I offered a retrospective on how working on pandas and getting
involved in the Python community starting in the late 2008 snowballed
into a cascade of projects and collaborations, culminating in the
recent focus on growing the ecosystems around projects like Apache
Arrow and Ibis, which came about in 2015 when I was still at Cloudera
(see two [blog][10][posts][11] from that era).

In early 2016, a precipitous decline in public and private enterprise
software valuations meant significant belt-tightening and a delayed
IPO at Cloudera, and I saw the writing on the wall that I would need
to look elsewhere to fund Arrow development (which at the time was not
much more than a Markdown specification and a chunk of code split off
from Apache Drill).

As fate would have it, I received a timely lifeline from technology
leaders [David Palaitis][12] and [Matt Greenwood][13] at [Two
Sigma][14], who were compelled by the prospect of open source
standards to enable better modularity and composability in data
systems. Two Sigma had already been incorporating these ideas in their
systems since the late 2000s. They offered both to hire me and to pay
for additional engineers to work with me on Arrow while also
supporting architecture work on their internal data processing
platform. Aided by this investment, we were able to get Arrow off the
ground quickly while working on real-world applications while
identifying new project extensions like [Arrow Flight][15] that would
bring enormous value. Two Sigma also [saw the potential of Ibis][16]
as an extensible and portable user interface and DSL layer for
coordinating both SQL and non-SQL analytics systems in a natural way
from Python. Motivated by this, [Phillip Cloud][17] and [Jeff
Reback][18] from the pandas core team would join me at Two Sigma to
help make a Python-based and Arrow- and Ibis-powered Python data
processing stack a reality.

A year into my tenure at Two Sigma, the ideas of interoperability,
composability, and modularity had begun to percolate more evidently in
the open source zeitgeist. I tried to articulate my perspective on
these ideas in August 2017 at my [JupyterCon talk “Data Science
without Borders”][19] (probably my favorite talk that I've
done). Right around this time, I had spotted some interesting new
GitHub repos and eventually a [press release from Anaconda, h20.ai,
and OmniSci (now Heavy.AI)][20] announcing the GPU Open Analytics
Initiative aka “GOAI”. Little did I know this would be the catalyst
for the most intense six years of my career as an open source
entrepreneur.

{{< video https://www.youtube.com/embed/wdmf1msbtVs
    title="Data Science without Borders"
>}}

I was excited by GOAI and the idea of a “GPU DataFrame”, but I did not
find much linking it to Arrow other than mentioning Arrow as
inspiration for the GPU DataFrame in a GitHub repository. So I decided
to go digging. GOAI did not initially involve a significant
engineering investment from NVIDIA, but I quickly learned that a team
there led by Josh Patterson was behind the scenes corralling many
startups to work on GOAI and to provide NVIDIA hardware for them to
develop on. It wasn’t straightforward to get included in the GOAI
group, but eventually I was able to get involved and start working to
align the efforts to the complementary goals of the (decidedly
CPU-oriented at the time) Arrow ecosystem. I learned later that the
initially-exclusive nature of the group was more driven by the intense
market rivalries amongst the major hardware vendors than anything
else.

Not long after GOAI started, Josh and team at NVIDIA were able to
secure a significant commitment of budget and headcount to be able to
build a development team inside NVIDIA to put serious developer muscle
behind the vision for open source GPU-accelerated analytics. A little
over a year after GOAI was announced, this beefed-up and now proudly
Arrow-based effort [was announced to the world at GTC Europe as
RAPIDS][21]. Hearing NVIDIA CEO Jensen Huang talk about me and Arrow
on stage in his GTC keynote brought tears to my eyes.

{{< video https://www.youtube.com/embed/G1kx_7NJJGA
    title="GTC Europe 2018: Jensen Huang"
    start="3530"
>}}

*(author's note: Arrow was created by consortium of people, not just me!)*

NVIDIA's investment in RAPIDS also came with the ability to make
strategic grants to projects and companies working on complementary
initiatives, but at the time (I was a full-time employee at Two Sigma)
it wasn’t straightforward for me to receive a development grant from
NVIDIA. I considered simply going to work at NVIDIA (which in
hindsight would have been highly lucrative), but I wanted to maintain
a close collaboration with Two Sigma and to leave the door open to
other fruitful collaborations as the Arrow ecosystem flourished. I
also perceived Arrow’s role in enabling the “Data Science without
Borders” vision, and wanted to try to engage language communities
beyond Python.

With these things in mind, in early 2018 I received a second lifeline
— this time from J.J. Allaire and Hadley Wickham at [RStudio][22] (now
known as [Posit][23]). J.J., Hadley, and I had gotten to know each
other years before that, and Hadley and I had [teamed up to create the
Feather format][24] based on Arrow to show the potential of making
Python and R work better together. We all agreed that the “language
wars” between Python and R were counterproductive, and Posit
recognized that the future of data science is polyglot. Investing in
technology like Arrow would reap huge benefits for the R ecosystem and
beyond.

J.J. offered to fund 4 full-time engineers and provide the “back
office” operations for a not-for-profit organization where we could
take in development grants from Two Sigma, NVIDIA, and others
companies. This became [Ursa Labs][4], and under this not-for-profit
structure we were able to grow the team to 7 engineers and take in
additional funding from Bloomberg, G-Research, Intel, and
others. [Neal Richardson][25] joined me to lead Ursa Labs in early
2019 and with Posit's support we were able to spend a couple of years
working on Apache Arrow with almost no administrative overhead.

By mid-2020, Neal and I began to see that the next stage of Arrow
ecosystem growth would benefit from a larger capital investment than
we could secure for a not-for-profit endeavor. I consulted [Chris
Ré][26] at Stanford, and he soon introduced me to early-stage
investors [Lip-Bu Tan][27] and [Amarjit Gill][28], who had stellar
reputations and were interested in software projects that would help
unlock the capabilities of modern hardware. I also reconnected with
[Dave Munichiello][30] and [Erik Nordlander][29] at GV (who had
invested in DataPad in 2013) for advice. It didn’t take long for us to
put together an investor syndicate, and thus Neal and I founded [Ursa
Computing][31]. Posit and Two Sigma received founders’ shares in this
new company to honor their support and commitment to the vision of
Apache Arrow.

## Starting Voltron Data: From Idea to 100+ Person Team

Shortly after the transition in late 2020 to Ursa Computing, as I was
catching up with Josh Patterson at NVIDIA, I learned that he and some
engineering leaders from the RAPIDS team were interested in exploring
data startup ideas. Our investors were thrilled about the prospect of
synthesizing the best ideas around hardware acceleration, data, and
language interfaces to create a unified software company, which we
gave the code name “Voltron Data”. It wasn’t hard to convince Josh to
jump on board with the project and become CEO, with me as
CTO. BlazingSQL, which had worked closely with the RAPIDS team, was
also keen to join the founding team. To complete the dream team, we
recruited Silicon Valley legend [Darren Haas][32], who built the first
prototype of Siri and went on to lead teams at Apple, GE Digital, and
Amazon AWS. Darren also founded [Change.org][33] and is a charismatic
team builder. With the help of a lot of legal work, we all [joined
forces to create Voltron Data][34].

Investors agreed with our technology vision, and before long we had
raised an additional $110M led by Lip-Bu Tan from Walden, on top of
the $5M that we had previously raised from GV and Walden for Ursa
Computing. This war chest has enabled us to build an amazing technical
team and make significant investments across the emerging [composable
data stack][35]. From the initial 30 or so people in Voltron Data, we
have grown to over 100, more than 20 of which are devoted to working
on open source projects like Arrow, Ibis, Substrait, and Velox.

In addition to our open source work, we have invested in collaborations
and partnerships that are aligned with growing the Apache Arrow
ecosystem and supporting the development of the composable data
stack. For example, this includes collaborations with [Snowflake][36]
and [Velox][37] as well as being a multi-year Gold sponsor of the
[DuckDB Foundation][38]. We also launched a commercial support
product, VESA, to be a development partner with organizations
replatforming on technologies like Apache Arrow and Ibis. We see these
collaborations as going hand-in-hand with new open source initiatives
like [nanoarrow][39] and [ADBC][40] which are facilitating the
transition to a more composable Arrow-based future. I’m really proud
of what the team has accomplished so far, and our commitment to code
quality and elevating engineering standards across these projects.

{{< video https://www.youtube.com/embed/pqMu18dmEdM
    title="Interview from G-Research Distinguished Speaker Series"
>}}

All startups as they transition from early- to mid-stage must focus on
specific areas of product development and revenue growth in order to
achieve long-term viability. This is especially true in 2023 and
beyond as capital markets have become much tighter than they were in
2021 and 2022. Companies that lack focus or work on too many things
generally do not fare well.

Personally, I have always been energized by the early stages of
projects: identifying a problem, working really hard to assemble a
team and bootstrap initial solutions, and then getting the project to
a point where I don’t have to be involved 100% of the time, so others
have an opportunity to step up and become leaders. This happened with
pandas (where I handed off project leadership to the core team in
2013) and has recently reached this transitional point with Arrow and
Ibis, which are extremely healthy and with excellent
leadership. Similarly, I have recently felt that I have made my most
valuable contributions to Voltron Data in helping it get off the
ground, raise money, sharpen the thesis around modular and composable
data systems, and assemble a top-notch engineering team. If I were to
remain in a long-term operational role, it might limit my ability to
pursue other impactful projects that fall too far outside of Voltron
Data’s wheelhouse.

## What’s Next For Me

Anyone who knows me knows that I don’t like the status quo and am
always looking for ways to innovate and change things for the
better. Now 38 years old, I have a much more fulfilling personal life
and better work-life balance than I did in my 20s (I wrote some
[musings about this aspect of personal development][41] around my 30th
birthday), but I am looking forward to continue catalyzing high-impact
projects to advance the data ecosystem. I plan to share more of what
I’ve been thinking about lately, but for now this post has grown long
enough.

The last eight years have been intense and exhilarating, and I’m
extremely grateful to the early Arrow faithful who were willing to
take a risk on our crazy ideas that seem a lot less crazy now. Without
the early backing from Two Sigma and RStudio/Posit, and the more
recent venture capital backing from Walden, GV, Blackrock, and others,
we would have not been able to accomplish nearly so much. There is yet
a long road ahead of us. I am excited to see where the road will lead.

## Other Things: Investing and Advising Startups

Alongside my efforts as a startup founder, I have also been active as
an angel investor or advisor in many startups that are working on
different parts of the stack where innovation is needed. This includes
[Anyscale][42], [Astral][43], [Atoma][44], [Bauplan][45],
[Dremio][46], [Earthly][47], [Fused][48], [Hex][49], [LanceDB][50],
[Motherduck][51], [Neon][52], [Quadratic][53], [Rill Data][54],
[Storytell.ai][55], [Sundeck][56], [Tabular][57], and
[Union.ai][58]. Seeing these companies develop makes me insanely
optimistic about the future.

It is only possible for an individual to spend productive time
directly working on so many projects at once, but I try to be as
helpful as I can to other passionate founders (or prospective
founders) to encourage them to work on hard problems and collaborate
to disrupt the status quo.

[1]: https://voltrondata.com
[2]: https://arrow.apache.org
[3]: https://ibis-project.org
[4]: https://ursalabs.org
[5]: https://ursalabs.org/blog/ursa-computing/
[6]: https://wesmckinney.com/blog/from-ursa-to-voltrondata/
[7]: https://techcrunch.com/2022/02/17/voltron-data-grabs-110m-to-build-startup-based-on-apache-arrow-project/
[8]: https://wesmckinney.com/blog/looking-back-15-years/
[9]: https://www.vldb.org/pvldb/vol16/p2679-pedreira.pdf
[10]: https://www.cloudera.com/about/news-and-blogs/press-releases/2015-07-20-cloudera-opens-up-new-capabilities-with-ibis.html
[11]: https://blog.cloudera.com/introducing-apache-arrow-a-fast-interoperable-in-memory-columnar-data-structure-standard/
[12]: https://www.linkedin.com/in/david-palaitis-34775131
[13]: https://www.linkedin.com/in/matt-greenwood-aa8741/
[14]: https://www.twosigma.com/
[15]: https://arrow.apache.org/blog/2019/10/13/introducing-arrow-flight/
[16]: https://www.youtube.com/watch?v=YXkyTc9mfGQ
[17]: https://github.com/cpcloud
[18]: https://github.com/jreback
[19]: https://www.youtube.com/watch?v=wdmf1msbtVs
[20]: https://h2o.ai/company/press-releases/data-science-and-deep-learning-application-leaders-form-gpu-open-analytics-initiative/
[21]: https://nvidianews.nvidia.com/news/nvidia-introduces-rapids-open-source-gpu-acceleration-platform-for-large-scale-data-analytics-and-machine-learning
[22]: https://rstudio.com
[23]: https://posit.co
[24]: https://posit.co/blog/feather/
[25]: https://www.linkedin.com/in/enpiar/
[26]: https://cs.stanford.edu/~chrismre/
[27]: https://www.linkedin.com/in/lip-bu-tan-284a7846/
[28]: https://www.linkedin.com/in/gillamarjit/
[29]: https://www.gv.com/team/erik-nordlander
[30]: https://www.gv.com/team/dave-munichiello
[31]: https://ursalabs.org/blog/ursa-computing/
[32]: https://www.linkedin.com/in/darrenhaas/
[33]: https://www.change.org/
[34]: https://wesmckinney.com/blog/from-ursa-to-voltrondata/
[35]: https://voltrondata.com/codex
[36]: https://voltrondata.com/resources/adbc-traction-duckdb-dbt-snowflake
[37]: https://voltrondata.com/resources/velox-partnership
[38]: https://duckdb.org/foundation/
[39]: https://arrow.apache.org/nanoarrow/
[40]: https://arrow.apache.org/docs/format/ADBC.html
[41]: https://wesmckinney.com/blog/whats-changed/
[42]: https://anyscale.com
[43]: https://astral.sh
[44]: https://atoma.ai
[45]: https://arxiv.org/abs/2308.05368
[46]: https://dremio.com
[47]: https://earthly.dev
[48]: https://www.fused.io
[49]: https://hex.tech/
[50]: https://lancedb.com/
[51]: https://motherduck.com/
[52]: https://neon.tech/
[53]: https://quadratichq.com
[54]: https://rilldata.com
[55]: https://storytell.ai
[56]: https://sundeck.io/
[57]: https://tabular.io/
[58]: https://union.ai/