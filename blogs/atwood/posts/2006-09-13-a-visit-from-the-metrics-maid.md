---
title: "A Visit from the Metrics Maid"
date: 2006-09-13
url: https://blog.codinghorror.com/a-visit-from-the-metrics-maid/
slug: a-visit-from-the-metrics-maid
word_count: 701
---

For the last few days, I’ve been surveying a software project. Landing on a planet populated entirely by an alien ecosystem of source code can be overwhelming. That’s why the first first thing I do is bust out my **software tricorder** – [static code analysis tools](https://blog.codinghorror.com/managed-code-analysis-tools/).


The two most essential static code analysis tools, for .NET projects, are [nDepend](http://www.ndepend.com/) and [FxCop](https://web.archive.org/web/20060809224545/http://www.gotdotnet.com/team/FxCop/). Like real software tricorders, they produce reams and reams of data – lots of **raw metrics on the source code**.


Even basic metrics can identify potential trouble spots and/or areas of interest in the code, such as...

- Methods that are too large or too small.
- Classes that are too large or too small.
- Methods that are too complex (as measured by [cyclomatic complexity](http://en.wikipedia.org/wiki/Cyclomatic_complexity)).
- Methods with too many parameters (more than [7 plus or minus 2](https://blog.codinghorror.com/the-magical-number-seven-plus-or-minus-two/)).
- Methods with too many local variables.
- Classes with an excessively deep inheritance structure.
- Types that are excessively large.


These simple metrics are already quite valuable. You can imagine how valuable more advanced software metrics could be, such as [code coverage](http://software.ericsink.com/articles/Code_Coverage.html). Or how quickly you’re finding and fixing bugs. And more advanced static analysis tools can offer literally [hundreds of recommendations](http://msdn2.microsoft.com/en-us/library/ee1hzekz.aspx), ranging from mundane to mission-critical.


Having more data about your software development project can never be bad. The real trick, of course, lies in interpreting all that data, and deciding how to act on it. There’s **a huge temptation to become a meter maid – to use the metrics as a reward or punishment system**.


![](https://blog.codinghorror.com/content/images/2025/05/image-359.png)


If Joe wrote a method with a cyclomatic complexity of 52, then he better get slapped with a complexity ticket, right? No excess complexity in the simplicity zone, you idiot!


Not necessarily. **Responsible use of the metrics is just as important as collecting them in the first place.** [Gregor Hohpe elaborates](http://www.eaipatterns.com/ramblings/41_metrics.html):


> Some of the most hated people in San Francisco must be the meter maids, the DPT people who drive around in golf carts and hand out tickets to anyone who overslept street cleaning or did not have enough quarters for the meter. On some projects, the most hated people are the metric maids, the people who go around and try to sum up a developer’s hard work and intellectual genius in a number between 1 and 10.
> Many managers love metrics: “You can’t manage it if you can’t measure it.” I am actually a big proponent of extracting and visualizing information from large code bases or running systems (see [Visualizing Dependencies](http://www.eaipatterns.com/ramblings/11_dependencies.html)). But when one tries to boil the spectrum between good and evil down to a single number we have to be careful as to what this number actually expresses.


Martin Woodward calls this [the measurement dilemma](http://www.woodwardweb.com/vsts/000284.html).


> The reporting aspects of [Team Foundation Server](https://web.archive.org/web/20060906130756/http://msdn.microsoft.com/vstudio/teamsystem/team/default.aspx?pull=/library/en-us/dnvs05/html/teamfoundatwrk.asp) are a new, more accurate instrument to take measurements inside your software development process. But you need to be wary about the things you measure. The metrics need to mean something useful rather than just be interesting. The effect of taking the metric should be carefully considered before taking it. This is not a new problem. But because Team Foundation Server makes it so easy to get data out of the system, the temptations are greater.


Martin also references the [Heisenberg Uncertainty Principle](http://en.wikipedia.org/wiki/Uncertainty_principle), which states that you can’t measure something without changing it. I believe this is true for software development metrics **only if you are using that metric to reward or punish.**


Recording metrics on your project can be beneficial *even if you don*’*t explicitly act on them*. Having a public “wall of metrics” might be a better idea. It can be a focal point for discussion about what the metrics mean to the team. This gives everyone on the project an opportunity to discuss and reflect, and act on the metrics as they deem appropriate. Maybe the team will even remove a few metrics that are of no value.


What metrics do you find helpful on *your* software projects? What metrics do you find not so helpful? And if you have no project metrics to talk about, well, what are you waiting for?

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[static code analysis](https://blog.codinghorror.com/tag/static-code-analysis/)
[.net](https://blog.codinghorror.com/tag/net/)
[metrics](https://blog.codinghorror.com/tag/metrics/)
