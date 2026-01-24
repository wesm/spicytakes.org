---
title: "A Modest Namespace Proposal"
date: 2005-01-19
url: https://blog.codinghorror.com/a-modest-namespace-proposal/
slug: a-modest-namespace-proposal
word_count: 355
---

Jon Galloway recently pointed out [something that’s been bothering me](http://weblogs.asp.net/jgalloway/archive/2005/01/06/347876.aspx) for a while:


> *I’m happy to see the huge growth of community contributed code – things like RSS.NET, sharpziplib, ftp classes to tide us over ’til .NET 2.0, etc. But one thing that bothers me is the namespaces. The .NET System namespaces are beautifully organized. Community / open source code namespaces are an anarchistic babel. Those that originate from a big company usually start with the company name, those that come from larger project usually take the the project’s name. One-off code snips / hobbyist / micro-projects usually contain a random concatenation of some or all of the following words: monkey, alien, squishy, bug, fuzzy, code, util, works, MyNamespace, namespace, ware, example, contrib, and lib: monkeyCode, fuzzyAlienWare, utilLib, bugware, etc. This is the case I’m talking about.*


Instead of answering Jon’s implied question, I think we should be asking ourselves if we need to do this at all. Rather than blindly slapping 20+ characters of namespace on the front of all your classes “just because,” **I have a modest proposal for you: how about no namespace at all?**


Almost every time I see namespaces used, they’re not functional. They don’t solve any collision or duplication problems for me. They’re little more than **vanity license plates for the author’s code**.


For example. I built this class MhtBuilder. It lets you duplicate the “Save as single file” functionality in IE using 100% managed code. It’s not going to cure cancer or anything, but it’s useful, not that common, and worth sharing. So I [posted it on CodeProject](https://web.archive.org/web/20050122095947/http://www.codeproject.com/vb/net/MhtBuilder.asp). Do I really need to call this class...

- CodingBadass.MhtBuilder
- MonkeyAlienSquishyBugFuzzyCodeUtilWorks.MhtBuilder
- AtwoodHeavyIndustries.MhtBuilder
- MegaCorp.MhtBuilder


C’mon. Let’s stop kidding ourselves. What does this accomplish? How many MhtBuilder classes are out there that I need to distinguish between? If you’re distributing **signed binaries with no source**, then you can arguably make a case that you need a namespace. Otherwise, stop with the veiled ego tripping, give your class a good descriptive name, and have the cojones to [leave it at that](https://blog.codinghorror.com/kiss-and-yagni/).

[namespaces](https://blog.codinghorror.com/tag/namespaces/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[community-contributed code](https://blog.codinghorror.com/tag/community-contributed-code/)
[.net](https://blog.codinghorror.com/tag/net/)
[organization](https://blog.codinghorror.com/tag/organization/)
