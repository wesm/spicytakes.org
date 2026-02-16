---
title: "Software Sprawl, The Golden Path, and Scaling Teams With Agency"
date: 2018-12-02
url: https://charity.wtf/2018/12/02/software-sprawl-the-golden-path-and-scaling-teams-with-agency/
word_count: 2233
---


Stop me if you’ve heard this one before.


The company is growing like crazy, your engineering team keeps rising to the challenge, and you are ferociously proud of them. But some cracks are beginning to show, and frankly you’re a little worried. You have always advocated for engineers to have broad latitude in technical decisions, including choosing languages and tools. This autonomy and culture of ownership is part of how you have successfully hired and retained top talent despite the siren song of the Faceboogles.


But recently you saw something terrifying that you cannot unsee: your company is using *all* the languages, *all* the environments, *all* the databases, *all* the build tools. Shit!!! Your ops team is in full revolt and you can’t really blame them. It’s grown into an unsupportable nightmare and something MUST be done, but you don’t know what or how — let alone how to solve it while retaining the autonomy and personal agency that you all value so highly.


I hear a version of this everywhere I’ve gone for the past year or two. It’s crazy how often I’ve seen it. I’ve been meaning to write my answer up for ages, and here it (finally) is.


First of all: you aren’t alone. **This is extremely common among high-performing teams, **so congratulations. Really!


There actually seems to be a direct link between teams that give engineers lots of leeway to own their technical decisions and that team’s ability to hire and retain top-tier talent, particularly senior talent. Everything is a tradeoff, obviously, but accepting somewhat more chaos in exchange for a stronger sense of individual ownership is usually the right one, and leads to higher-performing teams in the long run.


Second, there is actually already a well-trod path out of this hole to a better place, and it doesn’t involve sacrificing developer agency. It’s fairly simple! Just five short steps, which I will describe to you now.


## How to build a golden path and reverse software sprawl

1. Assemble a small council of trusted senior engineers.
2. Task them with creating a recommended list of default components for developers to use when building out new services. This will be your Golden Path, the path of convergence (and the path of least resistance).
3. Tell all your engineers that going forward, **the Golden Path will be fully supported by the org.** Upgrades, patches, security fixes; backups, monitoring, build pipeline; deploy tooling, artifact versioning, development environment, even tier 1 on call support. Pave the path with gold. Nobody HAS to use these components … but if they don’t, they’re on their own. They will have to support it themselves.
4. Work with team leads to draw up an umbrella plan for adopting the Golden Path for their current projects as well as older production services, as much as is reasonable or possible or desirable. Come up with a timeline for the whole eng org to deprecate as many other tools as possible. **Allocate real engineering time** to the effort. Hell, make a party out of it!
5. After the cutoff date (and once things have stabilized), establish a regular process for reviewing and incorporating feedback about the blessed Path and considering any proposed changes, additions or removals.


There you go. That’s it. Easy, right??


(It’s *not* easy. I never said it was easy, I said it was *simple. 👼🏼*)


Your engineers are currently used to picking the best tool for the job by optimizing locally. What data store has a data model that is easiest for them to fit to their needs? Which language is fastest for I/O throughput? What are they already proficient in? What you need to do is start building your muscles for optimizing *globally.* Not in isolation of other considerations, but in conjunction with them. It will always be a balancing act between optimizing locally for the problem at hand and optimizing globally for operability and general sanity.


(Oh, incidentally, requiring an engineer to write up a proposal any time they want to use a non-standard component, and then defend their case while the council grills them in person — this will be nothing but good for them, guaran-fucking-teed.)


Let’s go into a bit more detail on each of the five points. But **quick disclaimer**: this is not a prescription. I don’t know your system, your team, your cultural land mines or technical interdependencies or anything else about your situation. I am just telling stories here.


### 1. Assemble your council


Three is a good number for a council. More than that gets unwieldy, and may have trouble reaching consensus. Less than three and you run into SPOFs. You *never* want to have a single person making unilateral decisions because a) the decision-making process will be weaker, b) it sets that person up for too much interpersonal friction, and c) it denies your other engineers the opportunity to practice making these kinds of decisions.

- Your council members need technical breadth more than depth, and should be widely respected by engineers.
- At least one member should have a long history with the company so they know lots of stupid little details about what’s been tried before and why it failed.
- At least one member should be deeply versed in practical data and operability concerns.
- They should *all* have enough patience and political skill to drive consensus for their decisions. Absolutely no bombthrowers.


If you’re super lucky, you just tap the three senior technologists who immediately come to mind … your mind and everyone else’s. If you don’t have this kind of automatic consensus, you may want to let teams or orgs nominate their own representative so they feel they have some say.


### 2. Task the council with defining a Golden Path


Your council cannot vanish for a week and then descend from the mountain lugging lists engraved on stone tablets. The process of discovery and consensus is what validates the result.


The process must include talking to and gathering feedback from your engineers, talking to experts outside the company, talking to teams at other companies who are farther along using that technology, coming up with detailed pro/con lists and reasons for their choices. *Maybe* sometimes it includes prototyping something or investigating the technical depths … but yeah no mostly it’s just the talking.


You need your council members to have enough political skill to handle these conversations deftly, building support and driving consensus through the process. Everybody doesn’t have to love the outcome, but it shouldn’t be a *surprise* to anyone by the end.


### 3. Know where you’re going


Your council should create a detailed written plan describing which technologies are going to be supported … and a stab at what “supported” means. (Ask the experts in each component what the best practices are for backups, versioning, dependency management, etc.)


You might start with something like this:


> * Backend lang: Go 1.11           ## we will no longer be supporting
> backend scripting languages
> * Frontend lang: ReactJS v 16.5
> * Primary db: Aurora v 2.0        ## Yes, we know postgres is "better", 
> but we have many mysql experts and 0 pg experts except the one guy 
> who is going to complain about this.  You know who you are.
> * Deploy pipeline: github -> jenkins + docker -> S3 -> custom k8s 
> deploy tooling
> * Message broker: kafka v 2.10, confluent build
> * Mail: SES
> * .... etc


Circulate the draft regularly for feedback, especially with eng managers. Some team reorganization will probably be necessary to bear the new weight of your support specifications, and managers will need some lead time to wrangle this.


This is also a great time to reconceive of the way on call works at your company. But I am not going to go into all that here.


### 4. Set a date, draft a plan: go!


Get approval from leadership to devote a certain amount of time to consolidating your stack and paying down a lump sum of tech debt. It depends on your stage of decay, but a reasonable amount of time might be “**25% of engineering time for three months**“. Whatever you agree to, make sure it’s enough to make the world demonstrably better for the humans who run it; you don’t want to leave them with a tire fire or you’ll blow your credibility.


The council and team leads should come up with a rough outer estimate for how long it would take to rewrite everything and move the whole stack on to the Golden Stack. (It’s probably impossible and/or would take years, but that’s okay.) Next, look for the quick wins or swollen, inflamed pain points.

- If you are running two pieces of functionally similar software, like postgres and mysql, can you eliminate one?
- If you are managing something yourself that AWS could manage for you (e.g. postfix instead of SES, or kafka instead of kinesis), can you migrate that?
- If you are managing anything yourself that is not core to your business value, in fact, you should try to not manage it.
- If you are running any services by hand on an AWS instance somewhere, could you try using a service?
- If you are running your own monitoring software, etc … can you not?
- If you have multiple versions of a piece of software, can you upgrade or consolidate on one version?


The hardest parts are always going to be the ones around migrating data or rewriting components. Not everything is worth doing or can afford to be done in the time span of your project time, and that’s okay.


Next, brainstorm up some carrots. Can you write templates so that anybody who writes a service using your approved library, magically gets monitoring checks without having to configure anything? Can you write a wrapper so they get a bunch of end-to-end tests for free? Anything you can do to delight people or save them time and effort by using your preferred components is worth considering.


(By the way, if you don’t have any engineers devoted to internal tooling, you’re probably way overdue at this point.)


Pay down as much debt as you can, but be pragmatic: it’s better to get rid of five small things than one large thing, from a support perspective. Your main goal is to shrink the number of types of software your team has to support, particularly databases.


Do look for ways to make it fun, like … running a competition to see who can move the most tools to AWS in a week, or throwing a hack week party, or giving dorky prizes like trophies that entitle you to put your manager on call instead of you for a day, etc.


### 5. Make the process sustainable


After your target date has come and gone, you probably want to hold a post mortem retrospective and do lots of listening. (Well — first might I recommend a bubble bath and a bottle of champagne? But *then* a post mortem.)


Nothing is ever fixed forever. The company’s needs are going to expand and contract, and people will come and go, because change is the only constant. So you need to bake some flex into your system. How are you going to handle the need for changes to the Golden Path? Monthly discussions? An email list? Quarterly meetings with a formal agenda? I’ve seen people do all of these and more, it doesn’t really matter afaict.


Nobody likes a cabal, though, so the original council should gradually rotate out. I recommend replacing one person at a time, one per quarter, and rotating in another senior engineer in their place. This provides continuity while giving others a chance to learn these technical and political skills.


In the end, engineers are still free to use any tool or component at any time, just like before, only now they are solely responsible for it, which puts pressure on them not to do it unless REALLY necessary. So if someone wants to propose adding a new tool to the default golden path, they can always add it themselves and gain some experience in it before bringing it to the council to discuss a formal place for it.


## That’s all folks


See, wasn’t that simple?


*(It’s never simple.)*


I dearly wish more people would write up their experiences with this sort of thing in detail. I think engineering teams are too reluctant to show their warts and struggles to the world — or maybe it’s their executives who are afraid? Dunno.


Regardless, I think it’s actually a highly effective recruiting tool when teams aren’t afraid to share their struggles. The companies that brag about how awesome they are are the ones who come off looking weak and fragile. Whereas you can always trust the ones who are willing to laugh about all the ways they screwed up. Right?


In conclusion, don’t feel like an asshole for insisting on some process here. **There *should *be friction around adding new components to your stack**. (Add in haste, repent at leisure, as they say.) Anybody who argues with you probably needs to be exposed to way, way more of the support load for that software. That’s my professional opinion.


Anyway. You win or you die. Good luck with your sprawl.


charity
