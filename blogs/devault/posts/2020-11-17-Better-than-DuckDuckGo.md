---
title: "We can do better than DuckDuckGo"
date: 2020-11-17
url: https://drewdevault.com/2020/11/17/Better-than-DuckDuckGo.html
slug: Better-than-DuckDuckGo
word_count: 880
---

[DuckDuckGo](https://duckduckgo.com)  is one of the long-time darlings of the
technophile’s pro-privacy recommendations, and in fact the search engine that I
use myself on the daily. They certainly present a more compelling option than
many of the incumbents, like Google or Bing. Even so, DuckDuckGo is not good
enough, and we ought to do better.

I have three grievances with DuckDuckGo:

1. **It’s not open source.**  Almost all of DDG’s software is proprietary, and
they’ve demonstrated  [gross incompetence](https://github.com/duckduckgo/Android/issues/527)  in privacy in what little
software they have made open source. Who knows what else is going on in the
proprietary code?
2. **DuckDuckGo is not a search engine** . It’s more aptly described as a search
engine frontend. They  *do*  handle features like bangs and instant answers
internally, but their actual search results come from third-parties like
Bing. They don’t operate a crawler for their search results, and are not
independent.
3. **The search results suck!**  The authoritative sources for anything I want to
find are almost always buried beneath 2-5 results from content scrapers and
blogspam. This is also true of other search engines like Google. Search
engines are highly vulnerable to abuse and they aren’t doing enough to
address it.

There are some FOSS attempts to do better here, but they all fall flat.
 [searX](https://github.com/bauruine/searx/)  is also a false search engine
— that is, they serve someone else’s results.  [YaCy](https://yacy.net/) 
has their own crawler, but the distributed design makes results untolerably
slow, poor quality, and vulnerable to abuse, and it’s missing strong central
project leadership.

We need a real, working FOSS search engine, complete with its own crawler.

Here’s how I would design it.

First, YaCy-style decentralization is  *way*  too hard to get right, especially
when a search engine project already has a lot of Very Hard problems to solve.
Federation is also very hard in this situation — queries will have to
consult  *most*  instances in order to get good quality results, or a novel
sharding algorithm will have to be designed, and either approach will have to be
tolerant of nodes appearing and disappearing at any time. Not to mention it’d be
slow! Several unsolved problems with federation and decentralziation would have
to be addressed on top of building a search engine in the first place.

So, a SourceHut-style approach is better. 100% of the software would be free
software, and third parties would be encouraged to set up their own
installations. It would use standard protocols and formats where applicable, and
accept patches from the community. However, the database would still be
centralized, and even if programmable access were provided, it would not be with
an emphasis on decentralization or shared governance. It might be possible to
design tools which help third-parties bootstrap their indexes, and create a
community of informal index sharing, but that’s not the focus here.

It would also need its own crawler, and probably its own indexer. I’m not
convinced that any of the existing FOSS solutions in this space are quite right
for this problem. Crucially, I would  *not*  have it crawling the entire web from
the outset. Instead, it should crawl a whitelist of domains, or “tier 1”
domains. These would be the limited mainly to authoritative or high-quality
sources for their respective specializations, and would be weighed upwards in
search results. Pages that these sites link to would be crawled as well, and
given tier 2 status, recursively up to an arbitrary N tiers. Users who want to
find, say, a blog post about a subject rather than the documentation on that
subject, would have to be more specific: “$subject blog posts”.

An advantage of this design is that it would be easy for anyone to take the
software stack and plop it on their own servers, with their own whitelist of
tier 1 domains, to easily create a domain-specific search engine. Independent
groups could create search engines which specialize in academia, open standards,
specific fandoms, and so on. They could tweak their precise approach to
indexing, tokenization, and so on to better suit their domain.

We should also prepare the software to boldly lead the way on new internet
standards. Crawling and indexing non-HTTP data sources (Gemini?  Man pages?
Linux distribution repositories?), supporting non-traditional network stacks
(Tor? Yggdrasil? cjdns?) and third-party name systems (OpenNIC?), and anything
else we could leverage our influence to give a leg up on.

There’s a  *ton*  of potential in this domain which is just sitting on the floor
right now. The main problem is: who’s going to pay for it? Advertisements or
paid results are  *not*  going to fly — conflict of interest. Private, paid
access to search APIs or index internals is one opportunity, but it’s kind of
shit and I think that preferring open data access and open APIs would be
exceptionally valuable for the community.

If SourceHut eventually grows in revenue — at least 5-10× its
 [present revenue](https://sourcehut.org/blog/2020-11-11-sourcehut-q3-2020-financial-report/)  — I intend to sponsor this as a public
benefit project, with no plans for generating revenue. I am not aware of any
monetization approach for a search engine which squares with my ethics and
doesn’t fundamentally undermine the mission. So, if no one else has figured it
out by the time we have the resources to take it on, we’ll do it.
