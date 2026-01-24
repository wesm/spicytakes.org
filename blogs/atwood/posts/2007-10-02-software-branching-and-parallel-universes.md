---
title: "Software Branching and Parallel Universes"
date: 2007-10-02
url: https://blog.codinghorror.com/software-branching-and-parallel-universes/
slug: software-branching-and-parallel-universes
word_count: 1806
---

Source control is the very [bedrock of software development](https://blog.codinghorror.com/source-control-anything-but-sourcesafe/). Without some sort of version control system in place, you can’t reasonably call yourself a software engineer. If you’re using a source control system of any kind, you’re versioning files almost by definition. The concept of versioning is deeply embedded in every source control system. You can’t avoid it.


But there’s another concept, equally fundamental to source control, which is much less frequently used in practice. That concept is **branching**. The Subversion documentation has a decent [layman’s description of branching](http://svnbook.red-bean.com/en/1.1/ch04.html):


> Suppose it’s your job to maintain a handbook for a particular division of your company. One day a different division asks you for the same handbook – but with a few parts modified specifically for them, as they do things slightly differently.
> What do you do in this situation? You do the obvious thing: you make a second copy of your document, and begin maintaining the two copies separately. As each department asks you to make small changes, you incorporate them into one copy or the other. But you often find yourself wanting to make the same change to both copies. For example, if you discover a typo in the first copy, it’s very likely that the same typo exists in the second copy. The two documents are almost the same, after all; they only differ in small, specific ways.
> This is the basic concept of a branch – a line of development that exists independently of another line, yet still shares a common history. A branch always begins life as a copy of something, and moves on from there, generating its own history.


If you don’t ever use the branching feature of your source control system, *are you really taking full advantage of your source control system?*


I find that **almost every client I visit is barely using branching at all**. Branching is widely misunderstood, and rarely implemented – even though branching, like versioning, lies at the very heart of source control, and thus software engineering.


Perhaps the most accessible way to think of branches is as **parallel universes**. They’re places where, for whatever reason, history didn’t go quite the same way as it did in your universe. From that point forward, that universe can be slightly different – or it can be radically and utterly transformed. Like the Marvel comic book series [What If?](http://en.wikipedia.org/wiki/What_If_(comics)), branching lets you answer some interesting and possibly even dangerous “what if” questions with your software development.


![](https://blog.codinghorror.com/content/images/2025/03/image-237.png)


Parallel universes offer infinite possibility. They also allow you to stay safely ensconced in the particular universe of your choice, completely isolated from any events in other alternate universes. An alternate universe where the Nazis won World War II is an interesting idea, so long as we don’t have to *live* in that universe. There could potentially be thousands of these parallel universes. Although branching offers the seductive appeal of infinite possibility with very little risk, it also brings along something far less desirable: **infinite complexity**.


The DC comic book series [Crisis on Infinite Earths](http://en.wikipedia.org/wiki/Crisis_on_Infinite_Earths) is a cautionary tale of the problems you can encounter if you start spinning off too many parallel universes.


![](https://blog.codinghorror.com/content/images/2025/03/image-238.png)


> Prior to Crisis on Infinite Earths, DC was notorious for its continuity problems. No character’s backstory, within the comic books, was entirely self-consistent and reliable. For example, Superman originally couldn’t fly (he could instead leap over an eighth of a mile), and his powers came from having evolved on a planet with stronger gravity than Earth’s. Over time, he became able to fly, his powers were explained as coming from the sun, and a more complex backstory (the now-familiar “last survivor of Krypton” origin story) was invented. Later it was altered to include his exploits as Superboy. It was altered further to include Supergirl, the bottled city of Kandor, and other survivors of Krypton, further watering down the original idea of Superman having been the sole Kryptonian to survive the destruction of his world. There was also an issue of character aging; for instance, Batman, an Earth-born human being without super powers, retained his youth and vitality well into the 1960s despite having been an active hero during World War II, and his sidekick Robin never seemed to age beyond adolescence in over 30 years.
> These issues were addressed during the Silver Age by DC creating parallel worlds in a multiverse: Earth-One was the contemporary DC Universe, which had been depicted since the advent of the Silver Age; Earth-Two was the parallel world where the Golden Age events took place, and where the heroes who were active during that period had aged more or less realistically since that time; Earth-Three was an “opposite” world where heroes were villains, and historical events happened the reverse of how they did in real life (such as, for instance, President John Wilkes Booth being assassinated by a rebel named Abraham Lincoln); Earth Prime was ostensibly the “real world,” used to explain how real-life DC staffers (such as Julius Schwartz) could occasionally appear in comics stories; and so forth. If something happened outside current continuity (such as the so-called “Imaginary Stories” that were a staple of DC’s Silver Age publications), it was explained away as happening on a parallel world, a premise not dissimilar to the company’s current “Elseworlds” imprint.


Start juggling too many parallel universes at once, and you’re bound to drop a few. In most source control systems, you can create hundreds of branches with no performance issues whatsoever; it’s the **mental overhead** of keeping track of all those branches that you really need to worry about. Your developer’s brains can’t exactly be upgraded the same way your source control server can, so this is a serious problem.


I find that the analogy of parallel universes helps developers grasp the concept of branching, along with its inevitable pros and cons. But it doesn’t get much easier from there. Branching is a complex beast. There are dozens of ways to branch, and nobody can really tell you if you’re doing it right or wrong. Here are a [few common branching patterns](http://msdn2.microsoft.com/en-us/library/aa730834(VS.80).aspx) you might recognize.


**Branch per Release**
Every release is a new branch; common changes are merged between the releases. Branches are killed off only when the releases are no longer supported.


![](https://blog.codinghorror.com/content/images/2025/03/image-239.png)


**Branch per Promotion**
Every tier is a permanent branch. As changes are completed and tested, they pass the quality gate and are “promoted” as merges into successive tiers.


![](https://blog.codinghorror.com/content/images/2025/03/image-240.png)


**Branch per Task**
Every development task is a new, independent branch. Tasks are merged into the permanent main branch as they are completed.


![](https://blog.codinghorror.com/content/images/2025/03/image-241.png)


**Branch per Component**
Each architectural component of the system is a new, independent branch. Components are merged into the main branch as they are completed.


![](https://blog.codinghorror.com/content/images/2025/03/image-242.png)


**Branch per Technology**
Each technology platform is a permanent branch. Common parts of the codebase are merged between each platform.


![](https://blog.codinghorror.com/content/images/2025/03/image-243.png)


You may notice a few emerging themes in these branch patterns:

- All branches have a clearly defined lifecycle. They either live forever, or they are eventually killed off.
- All branches are created with the intention of eventually merging, somewhere. A branch without a merge is pointless.
- As we add branches, our development model gets complicated.


But that complication is often justified. The more developers you have on a project, the higher the chances are that one of those developers will check something really bad into source control and disrupt everyone else’s work. It’s simple statistics. People make mistakes. The more developers you have, the more mistakes you’ll have. And the more developers you have, the greater the consequences when everyone’s work is simultaneously disrupted by a bad check in. So what are our options?

1. **Maximum Productivity**
Everyone works in the same common area. There are no branches, just a long, unbroken straight line of development. There’s nothing to understand, so check ins are brainlessly simple – but each check in can break the entire project and bring all progress to a screeching halt.
2. **Minimum Risk**
Every single person on the project works in their own private branch. This minimizes risk; everyone works independently, and nobody can disrupt anyone else’s work. But it also adds incredible process overhead. Collaboration becomes almost comically difficult – every person’s work has to be painstakingly merged with everyone else’s work to see even the smallest part of the complete system.


The answer usually lies somewhere between these two extremes. Like everything else, branching can be abused. Chris Birmele notes that **branching has its own set of anti-patterns** you should watch out for:

kg-card-begin: html


| **Merge Paranoia** | Merging is avoided at all cost, due to a fear of the consequences. |
| **Merge Mania** | The team spends an inordinate amount of time merging software assets rather than developing them. |
| **Big Bang Merge** | Merging has been deferred to the very end of the development effort and an attempt is made to merge all branches simultaneously. |
| **Never Ending Merge** | Merge activity never seems to end; there's always more to merge. |
| **Wrong Way Merge** | A software asset is merged with a *previous* version. |
| **Branch Mania** | Branches are created often and for no apparent reason. |
| **Cascading Branches** | Branches are never merged back to the main development line. |
| **Mysterious Branches** | Nobody can tell you what the branches are for. |
| **Temporary Branches** | The purpose of a branch keeps changing; it effectively serves as a permanent "temporary" workspace. |
| **Volatile Branches** | An unstable branch is shared by other branches or merged into another branch. |
| **Development Freeze** | All development activities are stopped during branching, merging and building new baselines |
| **Berlin Wall** | Branches are used to divide the development team members, rather than divide the work they are performing. |


kg-card-end: html

If you’ve managed to read this far, perhaps you can understand why so many software development teams are completely sold on version control, but hesitant to take on branching and merging. It’s a powerful, fundamental source control feature, sure, but it’s also complicated. If you’re not careful, the wrong branching strategy could do more harm to your project than good.


Still, I urge developers to make an effort to understand branching – *really* understand it – and explore using branching strategies where appropriate on their projects. Done right, the mental cost of the branching tax pales in comparison to [the benefits of concurrent development](http://www.ericsink.com/scm/scm_branches.html) it enables. **Embrace the idea of parallel universes in your code**, and you may find that you can get more done, with less risk. Just try to avoid a crisis on infinite codebases while you’re at it.

[software development](https://blog.codinghorror.com/tag/software-development/)
[version control](https://blog.codinghorror.com/tag/version-control/)
[branching](https://blog.codinghorror.com/tag/branching/)
[source control](https://blog.codinghorror.com/tag/source-control/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
