---
title: "Town Car Version Control"
date: 2013-03-11
url: https://www.joelonsoftware.com/2013/03/11/town-car-version-control/
word_count: 1028
---


The team at Fog Creek is releasing a major new version of [Kiln](http://www.fogcreek.com/kiln) today. Kiln is a distributed version control system.


One of the biggest new features is Kiln Harmony, which lets you operate on Kiln repositories using either Git or Mercurial. So you can push changes to a Kiln repo using Git and then pull them using Mercurial. This means that you never have to decide whether you want to use Git or Mercurial. Religious war: averted.


But, I’m getting ahead of myself!


For those of you that have been living under a rock, the single biggest change in developers’ lives in the last decade (besides [Stack Overflow](http://stackoverflow.com/), natch) is [Distributed Version Control](https://www.joelonsoftware.com/items/2010/03/17.html). DVCS is such an important improvement over the previous generation of centralized version control (Subversion, CVS, etc.) that it’s a required upgrade, even though it’s honestly a bit harder to use.


The popular DVCS options are Git and Mercurial. Both are open source. They are very, very similar in capabilities and operation; in fact, they are so similar that Kiln Harmony hides all the differences, so you can use any Git *or* Mercurial tool to work with any Kiln repository.


If Git and Mercurial are open source, why are people making money selling them?


The short answer is that the open source tools are kind of raw. They’re dune buggies. Powerful, yes, and sufficient for a college project, but as it turns out, people buy Cadillacs, not dune buggies, to drive around in, because they like to have windshield wipers, 14-way power adjustable seats, and a way to start the engine from twenty feet away. Just in case you live in a Hollywood movie and the ignition has been hooked up to a bomb.


[Fog Creek](http://www.fogcreek.com/) (and others, notably [GitHub](https://github.com/)) are making money selling version control by providing a whole bunch of features that make the overall code management experience easier and more useful. For example, we both provide professional, secure hosting, a web management and administration interface, and somebody you can call for help.


Where we differ is that Kiln is more focused on the corporate market, while GitHub was designed for open source projects. I think of Kiln as the corporate Lincoln Town Car, while GitHub is kind of a VW Minibus. Both are eminently better choices than using raw Git.


So, specifically, Kiln gives you corporate things like:

- code reviews
- access control and permissions
- fast code search
- a news feed to follow code you care about


GitHub gives you things that match the sociology of open source projects:

- public home pages
- a social network, with profiles
- fork and pull workflow


Since internal corporate projects have a very different sociology than open source projects, Kiln is very different than GitHub. On internal projects, almost all code that is developed is eventually used, although it needs to be reviewed, so Kiln kind of assumes that everything you do is most likely going to end up in the main code base, and we have a slick code review system.


On open source projects, contributions can come from volunteers all over the Internet, many of whom are happy to fork the code for their own needs. So GitHub provides a social network, emphasizes the ease of forking someone else’s code (something you’re unlikely to do in a closed corporate environment), and has a thing called a [pull request](https://help.github.com/articles/using-pull-requests) that matches the way people tend to collaborate on open source projects without advance coordination.


ANYWAY, back to the new version of Kiln.


When Tyler and Ben built Kiln 1.0, they built it on Mercurial. Why? Well, Mercurial had pretty much all the same concepts as Git, but Git was historically unfriendly to Windows which is used by many of our corporate clients. We also thought that the Mercurial command line (hg) was a bit closer to Subversion (svn) which a lot of programmers were already used to.


So, long story short, we decided Mercurial was about 1% better than Git and that’s the way we went. We didn’t want to start a holy war, and we liked Git, but we just had a feeling that all else being equal, Mercurial was *marginally* better than Git.


We still think that, but in the years since Kiln first shipped, GitHub has taken the world by storm, creating an ecosystem around Git that more than makes up for its minor failings. Today Git is without a doubt more popular. So we knew we needed to add Git to Kiln.


We could have done it the lazy way: support both kinds of repositories and make you choose which one to use. Maybe add some nice conversion tools.


But we are not lazy. We decided to do it the *awesome* way.


We decided that the awesome way would be to make Kiln fully bilingual. It stores every repo in *both* formats. It automatically converts everything back and forth, always. The translation is 1:1, reversible, and round-trippable. Whatever you do to a Kiln repository using Git will be immediately visible to Mercurial users and vice versa.


Every user of every Kiln repo can choose either Mercurial or Git, and everything always works.


You can push in Git, and pull in Mercurial. Or vice versa. Or both.


A team that uses Mercurial internally (and barely understands Git) can push their code to GitHub and interact with the GitHub community.


If your team likes Git but you prefer Mercurial yourself, you can use a different version control system than everybody else on your team and, honestly, they don’t even have to know.


If your team is using Mercurial today but you want to switch to Git, you can move over — one person at a time. If Joe in Accounting refuses to move, it doesn’t matter. He can keep using Mercurial.


Everything maps. Everything round-trips.


There are some other big improvements in the version of Kiln available today. Super-fast code search. SSH and IP-whitelisting for security. Project READMEs. A bunch of other improvements throughout the interface that will be a huge upgrade for anyone already using Kiln. If you’re interested, you can [start a free trial online](https://secure.fogcreek.com/kiln/try).
