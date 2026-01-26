---
title: "Vcs Survey"
description: "When I discussedVersionControlToolsI said that it   was an unscientific agglomeration of opinion. As I was doing it I   realized that I could add some spurious but mesmerizing numbers to   my analysis"
date: 2010-03-08T00:00:00
tags: ["version control"]
url: https://martinfowler.com/bliki/VcsSurvey.html
slug: VcsSurvey
word_count: 723
---


When I discussed [VersionControlTools](https://martinfowler.com/bliki/VersionControlTools.html) I said that it
  was an unscientific agglomeration of opinion. As I was doing it I
  realized that I could add some spurious but mesmerizing numbers to
  my analysis by doing a survey. Google's spreadsheet makes the
  mechanics of conducting a survey really simple, so I couldn't
  resist.


![](images/vcsSurvey/summary.png)


I conducted the survey from February 23 2010 until March 3 2010
  on the Thoughtworks software development mailing list. I got 99
  replies. In the survey I asked everyone to rate a number of version
  control tools using the following options:

- Best in Class:   Either the best VCS or equal best
- OK: Not the best, but you're OK with it.
- Problematic: You would argue that the team really ought to be using something else
- Dangerous: This tool is really bad and Thoughtworks should press hard to have it changed
- No opinion: You haven't used it


The results were this:



| Tool | Best | OK | Problematic | Dangerous | No
  Opinion | Active Responses | Approval % |
| Subversion | 20 | 72 | 6 | 1 | 0 | 99 | 93% |
| git | 65 | 19 | 1 | 0 | 14 | 85 | 99% |
| Mercurial | 33 | 27 | 2 | 0 | 36 | 62 | 97% |
| ClearCase | 0 | 3 | 14 | 41 | 41 | 58 | 5% |
| TFS | 0 | 0 | 32 | 22 | 44 | 54 | 0% |
| CVS | 0 | 14 | 59 | 11 | 15 | 84 | 17% |
| Bazaar | 1 | 13 | 3 | 0 | 80 | 17 | 82% |
| Perforce | 1 | 26 | 16 | 1 | 54 | 44 | 61% |
| VSS | 1 | 1 | 11 | 64 | 22 | 77 | 3% |



As well as the raw summary values, I've added two calculated
columns here to help summarize the results.

- Active Responses: The total of responses excluding âNo
  Opinionâ. (eg for git: 65 + 19 + 1 + 0)
- Approval %: The sum of best and ok responses divided by active
  responses, expressed as a percentage. (eg for git: (65 + 19) / 85)


The graph shows a scatter plot of approval percentage and active
responses. As you can see there's a clear cluster around Subversion,
git, and Mercurial with high approval and a large amount of
responses. It's also clear that there's a big divide in approval between those
three, together with Bazaar and Perforce, versus the rest.


Although the graph captures the headline information well, there's
a couple of other subtleties I should mention.

- Although the trio of Subversion, git, and Mercurial cluster close
together on approval, git does get a notably higher amount of best
scores: (65 versus 20 and 33).
- VSS got the most âdangerousâ responses, but a couple of people
 approved of it.
- Neither TFS or ClearCase are liked much, but ClearCase got more
âdangerousâ responses than TFS (41 versus 22).
- Don't read too much into small differences as I'm sure they aren't
significant. I'm sure the difference in approval percentage between VSS, TFS,
and ClearCase isn't signifcant, but the difference between these three
and the leaders is.


Some caveats. This is a survey of opinion of ThoughtWorkers who
follow our internal software development discussion list, nothing more. It's
possible some of them may have been biased by my previous article
(although unlikely, since I've never managed to get my ThoughtBot
opinion-control software to work reliably). Opinions of tools are
often colored by processes that are more about the organization than
the tool itself. But despite these, I think it's an interesting data
point.


I should also stress the important point to take away from this
isn't the comparison between those close in the numbers, eg comparing
git and Mercurial or comparing TFS and ClearCase. Any survey like this
has a certain amount of noise in it, and I suspect the noise here is
greater than such a difference. The important point is the big
approval gap between the leading tools (Subversion, git, and
Mercurial) and the laggards - essentially the point in
[VersionControlTools](https://martinfowler.com/bliki/VersionControlTools.html).
