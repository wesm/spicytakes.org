---
title: "The Big Ball of Mud and Other Architectural Disasters"
date: 2007-11-26
url: https://blog.codinghorror.com/the-big-ball-of-mud-and-other-architectural-disasters/
slug: the-big-ball-of-mud-and-other-architectural-disasters
word_count: 1918
---

Mistakes are inevitable on any software project. But mistakes, if handled appropriately, are OK. Mistakes can be intercepted, adjusted, and ultimately addressed. The root of deep, fatal software project problems is *not knowing when you’re making a mistake*. These types of mistakes tend to fester into massive, systemic project failure. That’s why I’m fond of [citing McConnell’s list of classic mistakes](https://blog.codinghorror.com/escaping-from-gilligans-island/); I find it helpful to review every so often as a sort of [triage self-check](https://blog.codinghorror.com/not-all-bugs-are-worth-fixing/). I ask myself – **am I making any of these mistakes without even realizing it?**


I suppose this could lead to a sort of project hypochondria, where you’re constantly defending against mysterious, unseen project illnesses. I don’t know about you, but I’d much rather be working on a project with a paranoid project manager than an oblivious one. [Only the paranoid survive](https://web.archive.org/web/20071213175440/http://www.intel.com/pressroom/kits/bios/grove/paranoid.htm).


Perhaps that’s also why I enjoy Brian Foote and Joseph Yoder’s [Big Ball of Mud paper](http://www.laputan.org/mud/) so much. This paper was originally presented at the 1997 [conference on Patterns Languages of Programs](https://web.archive.org/web/20080509064507/http://st-www.cs.uiuc.edu/~plop/), amusingly acryonymed PLoP. It describes **classic *architectural* mistakes in software development**.


> The architecture that actually predominates in practice is the BIG BALL OF MUD.
> A BIG BALL OF MUD is haphazardly structured, sprawling, sloppy, duct-tape and bailing wire, [spaghetti code jungle](http://www.cs.brandeis.edu/~dkw/C-humor/pasta.txt). We’ve all seen them. These systems show unmistakable signs of unregulated growth, and repeated, [expedient repair](https://web.archive.org/web/20071201144157/http://home.swbell.net/mck9/cobol/style/rewrite.html). Information is shared promiscuously among distant elements of the system, often to the point where nearly all the important information becomes global or duplicated. The overall structure of the system may never have been well defined. If it was, it may have eroded beyond recognition. Programmers with a shred of architectural sensibility shun these quagmires. Only those who are unconcerned about architecture, and, perhaps, are comfortable with the inertia of the day-to-day chore of patching the holes in these failing dikes, are content to work on such systems.
> Still, this approach endures and thrives. Why is this architecture so popular? Is it as bad as it seems, or might it serve as a way-station on the road to more enduring, elegant artifacts? What forces drive good programmers to build ugly systems? Can we avoid this? Should we? How can we make such systems better?


It’s a great read. The authors enumerate seven architectural pathologies:


1. [**Big Ball of Mud**](http://www.laputan.org/mud/mud.html#BigBallOfMud)
(a.k.a. *Shantytown*, *Spaghetti Code*)

kg-card-begin: html

> Shantytowns are usually built from common, inexpensive materials and simple tools. Shantytowns can be built using relatively unskilled labor. Even though the labor force is “unskilled” in the customary sense, the construction and maintenance of this sort of housing can be quite labor intensive. There is little specialization. Each housing unit is constructed and maintained primarily by its inhabitants, and each inhabitant must be a jack of all the necessary trades. There is little concern for infrastructure, since infrastructure requires coordination and capital, and specialized resources, equipment, and skills. There is little overall planning or regulation of growth. Shantytowns emerge where there is a need for housing, a surplus of unskilled labor, and a dearth of capital investment. Shantytowns fulfill an immediate, local need for housing by bringing available resources to bear on the problem. Loftier architectural goals are a luxury that has to wait. 
> Maintaining a shantytown is labor-intensive and requires a broad range of skills. One must be able to improvise repairs with the materials on-hand, and master tasks from roof repair to ad hoc sanitation. However, there is little of the sort of skilled specialization that one sees in a mature economy. 
> All too many of our software systems are, architecturally, little more than shantytowns. Investment in tools and infrastructure is too often inadequate. Tools are usually primitive, and infrastructure such as libraries and frameworks, is undercapitalized. Individual portions of the system grow unchecked, and the lack of infrastructure and architecture allows problems in one part of the system to erode and pollute adjacent portions. Deadlines loom like monsoons, and architectural elegance seems unattainable.

kg-card-end: html

2. [**Throwaway Code**](http://www.laputan.org/mud/mud.html#ThrowAwayCode)
(a.k.a. *Quick Hack, Kleenex Code, Disposable Code, Scripting, Killer Demo, Permanent Prototype, Boomtown*)

kg-card-begin: html

> A homeowner might erect a temporary storage shed or car port, with every intention of quickly tearing it down and replacing it with something more permanent. Such structures have a way of enduring indefinitely. The money expected to replace them might not become available. Or, once the new structure is constructed, the temptation to continue to use the old one for “a while” might be hard to resist. 
> Likewise, when you are prototyping a system, you are not usually concerned with how elegant or efficient your code is. You know that you will only use it to prove a concept. Once the prototype is done, the code will be thrown away and written properly. As the time nears to demonstrate the prototype, the temptation to load it with impressive but utterly inefficient realizations of the system’s expected eventual functionality can be hard to resist. Sometimes, this strategy can be a bit too successful. The client, rather than funding the next phase of the project, may slate the prototype itself for release.

kg-card-end: html

3. [**Piecemeal Growth**](http://www.laputan.org/mud/mud.html#PiecemealGrowth)
(a.k.a. *Urban Sprawl, Iterative-Incremental Development*)

kg-card-begin: html

> Urban planning has an uneven history of success. For instance, Washington D.C. was laid out according to a master plan designed by [the French architect L’Enfant](http://en.wikipedia.org/wiki/Pierre_Charles_L'Enfant). The capitals of Brazil (Brasilia) and Nigeria (Abuja) started as paper cities as well. Other cities, such as Houston, have grown without any overarching plan to guide them. Each approach has its problems. For instance, the radial street plans in L’Enfant’s master plan become awkward past a certain distance from the center. The lack of any plan at all, on the other hand, leads to a patchwork of residential, commercial, and industrial areas that is dictated by the capricious interaction of local forces such as land ownership, capital, and zoning. Since concerns such as recreation, shopping close to homes, and noise and pollution away from homes are not brought directly into the mix, they are not adequately addressed. 
> Most cities are more like Houston than Abuja. They may begin as settlements, subdivisions, docks, or railway stops. Maybe people were drawn by gold, or lumber, access to transportation, or empty land. As time goes on, certain settlements achieve a critical mass, and a positive feedback cycle ensues. The city’s success draws tradesmen, merchants, doctors, and clergymen. The growing population is able to support infrastructure, governmental institutions, and police protection. These, in turn, draw more people. Different sections of town develop distinct identities. With few exceptions, (Salt Lake City comes to mind) the founders of these settlements never stopped to think that they were founding major cities. Their ambitions were usually more modest, and immediate.

kg-card-end: html

4. [**Keep It Working**](http://www.laputan.org/mud/mud.html#KeepItWorking)
(a.k.a. *Vitality, Baby Steps, Daily Build, First Do No Harm*)

kg-card-begin: html

> Once a city establishes its infrastructure, it is imperative that it be kept working. For example, if the sewers break, and aren’t quickly repaired, the consequences can escalate from merely unpleasant to genuinely life threatening. People come to expect that they can rely on their public utilities being available 24 hours per day. They (rightfully) expect to be able to demand that an outage be treated as an emergency. 
> Software can be like this. Often a business becomes dependent upon the data driving it. Businesses have become critically dependent on their software and computing infrastructures. There are numerous mission critical systems that must be on-the-air twenty-four hours a day/seven days per week. If these systems go down, inventories can not be checked, employees can not be paid, aircraft cannot be routed, and so on. 
> There may be times where taking a system down for a major overhaul can be justified, but usually, doing so is fraught with peril. However, once the system is brought back up, it is difficult to tell which from among a large collection of modifications might have caused a new problem. Every change is suspect. Deferring such integration is a recipe for misery.

kg-card-end: html

5. [**Shearing Layers**](http://www.laputan.org/mud/mud.html#ShearingLayers)

kg-card-begin: html

> The notion of SHEARING LAYERS is one of the centerpieces of Brand’s [How Buildings Learn](http://www.amazon.com/exec/obidos/ASIN/0140139966/codihorr-20). Brand, in turn synthesized his ideas from a variety of sources, including British designer Frank Duffy, and ecologist R. V. O’Neill.
> Brand quotes Duffy as saying: “Our basic argument is that there isn’t any such thing as a building. A building properly conceived is several layers of longevity of built components.” 
> Brand distilled Duffy’s proposed layers into these six: Site, Structure, Skin, Services, Space Plan, and Stuff. Site is geographical setting. Structure is the load bearing elements, such as the foundation and skeleton. Skin is the exterior surface, such as siding and windows. Services are the circulatory and nervous systems of a building, such as its heating plant, wiring, and plumbing. The Space Plan includes walls, flooring, and ceilings. Stuff includes lamps, chairs, appliances, bulletin boards, and paintings.
> These layers change at different rates. Site, they say, is eternal. Structure may last from 30 to 300 years. Skin lasts for around 20 years, as it responds to the elements, and to the whims of fashion. Services succumb to wear and technical obsolescence more quickly, in 7 to 15 years. Commercial Space Plans may turn over every 3 years. Stuff is, like software, subject to unrelenting flux.

kg-card-end: html

6. [**Sweeping It Under The Rug**](http://www.laputan.org/mud/mud.html#SweepingItUnderTheRug)
(a.k.a. *Potemkin Village, Housecleaning, Pretty Face, Quarantine, Hiding it Under the Bed, Rehabilitation*)

kg-card-begin: html

> One of the most spectacular examples of sweeping a problem under the rug is the concrete sarcophagus that Soviet engineers constructed to put a 10,000 year lid on the infamous reactor number four at [Chernobyl](http://en.wikipedia.org/wiki/Chernobyl_disaster), in what is now Ukraine.
> If you can’t make a mess go away, at least you can hide it. Urban renewal can begin by painting murals over graffiti and putting fences around abandoned property. Children often learn that a single heap in the closet is better than a scattered mess in the middle of the floor.

kg-card-end: html

7. [**Reconstruction**](http://www.laputan.org/mud/mud.html#Reconstruction)
(a.k.a. *Total Rewrite, Demolition, Plan to Throw One Away, Start Over*)

kg-card-begin: html

> Atlanta’s Fulton County Stadium was built in 1966 to serve as the home of baseball’s Atlanta Braves, and football’s Atlanta Falcons. In August of 1997, the stadium was demolished. Two factors contributed to its relatively rapid obsolescence. One was that the architecture of the original stadium was incapable of accommodating the addition of the “sky-box” suites that the spreadsheets of ‘90s sporting economics demanded. No conceivable retrofit could accommodate this requirement. Addressing it meant starting over, from the ground up. The second was that the stadium’s attempt to provide a cheap, general solution to the problem of providing a forum for both baseball and football audiences compromised the needs of both. In only thirty-one years, the balance among these forces had shifted decidedly. The facility is being replaced by two new single-purpose stadia. 
> Might there be lessons for us about unexpected requirements and designing general components here?

kg-card-end: html

The first step in dealing with a problem is to **admit you have one**. If you catch glimpses of any of these themes in your current software project, I encourage you to read the relevant sections in the paper, which goes into much more detail– nd provides ideas for remediation strategies.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
[project management](https://blog.codinghorror.com/tag/project-management/)
[software project failures](https://blog.codinghorror.com/tag/software-project-failures/)
[technical debt](https://blog.codinghorror.com/tag/technical-debt/)
