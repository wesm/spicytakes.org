---
title: "Package Customization"
description: "A common question in IT departments is whether to provide a   capability by building custom software or by buying a package. For longer   than I've been programming the debate has raged about how to m"
date: 2011-07-06T00:00:00
tags: ["bad things", "programming environments"]
url: https://martinfowler.com/bliki/PackageCustomization.html
slug: PackageCustomization
word_count: 1065
---


A common question in IT departments is whether to provide a
  capability by building custom software or by buying a package. For longer
  than I've been programming the debate has raged about how to make
  that choice. My base position on this is founded on the
  [UtilityVsStrategicDichotomy](https://martinfowler.com/bliki/UtilityVsStrategicDichotomy.html). Boiled down this means that
  if the business process you are supporting is part of your
  competitive advantage you should build custom software, if not you
  should buy a package and adjust your business process to fit the way
  the package works.


Despite the clear excellence of my opinion, not a lot of
  companies seem to do this. Often they neglect the dichotomy, which
  is one problem. But the problem I want to focus on here is the
  common trap when they buy a package.


You'll notice above I said âbuy a package and adjust your
  business process to fitâ. I have two reasons to say this. Firstly if
  you are buying a package to support a utility business process, then
  there's no differentiation in the business process - therefore you
  might as well do that business process in a way that fits the
  package. Of course this is a very software-person-centric view of
  the world. Despite the fact that a team isn't doing differentiable
  work, they'd still rather do it their way, rather than the way some
  silly software package wants to do it. As someone who believes in
  people over process, I naturally have a lot of sympathy with that
  point of view.


But the result of this natural action is that companies start
  doing significant customization of the package… and this is where
  the trouble begins. The fact is that most packages aren't designed
  in such a way as to make customization really viable, at least not on
  a significant scale. Typically they lack what my colleague Scott Shaw
  calls âdeliverabilityâ - such things as support for version control,
  testing, and a deployment pipeline. This makes changes brittle and
  hard to control.


You can bear this if your customization is small, but in many
  situations it isn't. Recently a colleague came across a package
  customization that ran to 300KLOC of customization code. That's more
  code than the entire codebase of our Studios product suite, twice as
  much as the codebase for one of our larger client projects that's
  been running a strategic business for a decade. Once you're at those
  sizes you cannot expect to manage without the tools and processes
  that you'd use for custom software.


This problem tends to come most to a head when the vendor
  releases an upgrade of your package, and you find that there is a
  prohibitive amount of work involved in doing the upgrade because the
  customizations will break with the upgrade. Gartner recently
  estimated that [it would take $500
  billion](http://www.gartner.com/it/page.jsp?id=1439513) to bring corporate systems up to latest versions (rising
  to $1 trillion by 2015). That's a big number, but the real cost is
  how much money has been wasted in customizations that weren't
  worthwhile or could have been cheaper with a purely custom route.


So what can you do about it? First off, I think it's important to
  be somewhat hard-nosed about package customization for utility
  business functions. Is the cost on the software side really worth
  it? Although agile approaches matter less for utility functions, the
  notion of taking small steps is valuable. Can you use the package
  without customizations initially and try to see how well it works in
  practice? People will naturally be uncomfortable with the change,
  because people naturally are. But given some time they may find that
  things they thought would matter now matter much less.


We can look more seriously about how customization is done. Some
  approaches are more difficult to deliver than others. Look for
  someone else that's done a similar level of customization on an
  older version of the package, and find out what it took for them to
  upgrade. That may help get a truer picture of the costs. In general
  for packages we should treat upgradeability as first-class
  cross-functional requirement.


When you get a vendor to customize a package, it's very hard to
  get them to follow the customer's delivery practices. The risk that
  they won't follow those practices is high and should be taken into
  account as part of your risk planning.


A lot of organizations try to limit the number of languages or
  frameworks they use. We must remember that many of these
  customizable packages are, in effect, another language or
  platform. As a result any arguments made against adopting another
  language should apply equally well to a package customization
  effort.


Indeed a common argument against introducing new languages is
  that it makes it hard to find developers in that language. This
  issue is usually particularly true for packages, since these often
  offer a narrow range of employment opportunities. Furthermore the
  nature of much package customization work deters able people, which
  makes it even harder to find good people who are more comfortable
  with polyglot programming. It may be that the costs involved with
  the difficulty of hiring people could be greater than any cost
  saving in using the package over a custom development in a
  mainstream programming platform.


Rather than customize the package, look to see if the package can
  expose data and functionality through an effective API, and write
  custom applications for custom capabilities. Often people don't like this
  because it means they have to use separate applications for
  different parts of the same work-flow. That may be a smaller burden
  to bear, and can be made smaller with web interfaces. Vendors may
  make this hard as it can reduce lock-in, but ease of collaboration
  should be an important part of choosing which vendor to go with.


But herein lies a trap. One of the big sources of customization
  is integrating between different vendor packages. This is a big
  reason to prefer a single vendor for multiple packages rather than
  picking best-of-breed. Picking a single vendor makes it easier to do
  the integration as it's in their interest to get it right. If it's a
  utility business function, then the value of best-of-breed packages is
  limited anyway.


What it all boils down to is that package environments usually
  provide a very poor platform for software development. Such packages
  cost a lot more to customize and keep current than many people tend
  to think.
