---
title: "Defining Open Source"
date: 2007-07-06
url: https://blog.codinghorror.com/defining-open-source/
slug: defining-open-source
word_count: 704
---

As I mentioned two weeks ago, my plan is to contribute $10,000 to [the .NET open source ecosystem](https://blog.codinghorror.com/supporting-open-source-projects-in-the-microsoft-ecosystem/). $5,000 from me, and a matching donation of $5,000 from Microsoft.


There’s only two ground rules so far:

1. The project must be written in **.NET managed code**.
2. The project must be **open source**.


The first rule is simple enough; although mono and subversion are great open source projects, they aren’t written in .NET managed code, and are therefore totally ineligible. But number two is where I hit a roadblock: **how do you tell if something that calls itself “open source” is *really* open source?** Many projects think they are – or at least some users may *think* they are – but they really aren’t.


NDoc is an example of exactly this kind of tricky misunderstanding, per a comment [Chris Nahr](http://www.kynosarges.de/) left on [a related post](https://blog.codinghorror.com/open-source-free-as-in-free/):


> If [other people contributing] was his wish he kept it to himself. The source code for NDoc 2.0 was never released – Kevin claimed licensing issues as the reason. No one else could contribute, except by mailing him bug reports on his (binary-only) alpha builds.
> Kevin is now supposedly passing on the Sourceforge administration of the project to two other guys; I hope we’ll finally see a public source code release again so that willing engineers actually *can* contribute once again.


I want to avoid these kinds of problems.


To that end, here are a few criteria we need to evaluate for each nominated project, to ensure that they’re not just paying lip service to “open source:”

1. **The project must use **[**an OSI approved license**](http://en.wikipedia.org/wiki/Open-source_license)**,** or the permissive or reciprocal [shared source licenses](https://web.archive.org/web/20070816211551/http://www.microsoft.com/resources/sharedsource/licensingbasics/sharedsourcelicenses.mspx) from Microsoft. (I have to include that rider because part of the OSI’s pissing match with Microsoft is not formally recognizing Microsoft’s licenses, even though they’re absolutely in the spirit of open source.) [Pick a license, any license!](https://blog.codinghorror.com/pick-a-license-any-license/) If your project does not have a license, or if you fail to make it stupid easy for us to determine what license your project uses... your project is ineligible.
2. **The project must use a commonly available method of public source control**. SourceForge, CodePlex, Google Code, whatever. Other developers should be able to retrieve the read-only public code using a source control tool, and potentially check in changes to the codebase if granted appropriate permissions. If the only way to get to the source code is via HTTP download of a ZIP file... your project is ineligible.
3. **The project must provide public evidence that it accepts and encourages code contributions from the outside world**. Is a project truly open source if it only has *one* developer? Is a project truly open source if it has a cabal of three developers who summarily ignore all outside suggestions and contributions? All I’m looking for here is evidence of some kind of community. It doesn’t have to be a large one, necessarily, but it has to be there. The spirit of open source is active community development. If you can’t show a decent history of check ins from a reasonable variety of contributors... your project is ineligible.


This maps fairly well to the “four freedoms” of the [Free Software Foundation](http://www.gnu.org/philosophy/free-sw.html):

- The freedom to run the program, for any purpose.
- The freedom to study how the program works, and adapt it to your needs.
- The freedom to redistribute copies so you can help your neighbor.
- The freedom to improve the program, and release your improvements to the public, so that the whole community benefits.


So now the vetting process begins.


**I need your help to figure out how many of the projects nominated in the comments actually meet the criteria I’ve outlined**. I’ve put [a read-only spreadsheet online](https://web.archive.org/web/20110623174821/https://spreadsheets.google.com/pub?key=pKxDW35algYebfs8nssTjIQ) via Google documents which contains all the projects people nominated in the comments to my original post. But I can’t seem to make it editable by the world. I can only invite people in as “collaborators.” Supposedly [this link](http://spreadsheets.google.com/ccc?key=pKxDW35algYebfs8nssTjIQ&inv=everyone@everywhere.com&t=6408456595839589032&guest) allows anyone with a Google account to be a collaborator. Try that first.


Alternately, if there’s a better way to collaboratively edit a spreadsheet-like list, I’m open to suggestions!

[.net](https://blog.codinghorror.com/tag/net/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
