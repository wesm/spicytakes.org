---
title: "The Project Aardvark Spec"
date: 2005-08-17
url: https://www.joelonsoftware.com/2005/08/17/the-project-aardvark-spec/
word_count: 726
---


As the final version of [Copilot.com](https://www.copilot.com/) (what this spec calls “Aardvark”) went into production in early August, 2005, this spec is now of historical interest only. I’m making it available as a part of Joel on Software because many people have asked to see some samples of the kinds of specs we write at Fog Creek. (You may also be interested in my series on [Painless Functional Specifications](https://www.joelonsoftware.com/articles/fog0000000036.html).)


There was one big mistake in the spec. When I wrote it I had assumed that port 443, used by the secure (SSL) http protocol, would be open even on networks that are configured to use proxy servers. I mistakenly believed that proxy servers could not forward SSL traffic because that would appear, to the browser, to be a “man in the middle” attack. This, it turns out, was erroneous, false, and incorrect, and after shipping the first beta we discovered just how wrong it was. Thus, the final implementation of Copilot 1.0 required a lot of unplanned work to support proxy detection and different kinds of proxy servers. We got most of that work done in time for 1.0 and are now finishing off the rest of it for a release we’re calling 1.1.


That said, the extra proxy work only added about 10% to the overall development effort. The reason you write a spec is not to solve every possible problem in advance: the reason you write a spec is to solve as many problems as you possibly can in advance so that you minimize the number of surprises that come up during development. In our case, since we were working with summer interns who literally had to walk out the door and go back to school, we literally could not afford to underestimate the amount of work that was needed to build Project Aardvark or I would be stuck debugging the thing deep into September while the kids drank beer and played poker, and we couldn’t have that.


Many times, thinking things out in advance saved us serious development headaches later on. When I wrote the first draft of this spec, I had a more complicated flowchart that assumed that either party (helper or victim) could initiate the process. This became extremely complicated and convoluted for various reasons. As I worked through the screens that would be needed to allow either party to initiate the process, I realized that Aardvark would be just as useful, and radically simpler, if the helper was required to start the whole process. Making this change in the spec took an hour or two. If we had made this change in code, it would have added weeks to the schedule. I can’t tell you how strongly I believe in Big Design Up Front, which the proponents of Extreme Programming consider anathema. I have consistently saved time and made better products by using BDUF and I’m proud to use it, no matter what the XP fanatics claim. They’re just wrong on this point and I can’t be any clearer than that.


There was one other significant change we made late in the process which is not reflected in the spec. After usability testing, we discovered that people were consistently confused by our policy of having the application delete itself. This was not what users expect. We modified the final product so that the helper could check a box to cause the victim’s executable to be deleted, but it wasn’t done by default. This way the helper, who is presumably more computer savvy, could insure that no unsafe executables were left around on the victim’s computer. I think this change was about 2 hours of work, so it didn’t impact the schedule.


Finally, you’ll notice a big “coding conventions” section in the middle of the spec. Frankly, this doesn’t belong in a functional specification, and it should really have been a separate document.


Still, as I reread this spec today, I’m surprised by what a good job the [Aardvarkians](http://www.projectaardvark.com/) did implementing everything. I seriously expected we would have to cut features; instead, we shipped with everything we wanted in version 1 and even did some of the features this spec refers to as version 2 features.


[Download The Project Aardvark Spec in PDF Format (about 120KB)](https://www.joelonsoftware.com/RandomStuff/copilot_spec.pdf). If you link to the spec, please link to this page, not the PDF file itself.
