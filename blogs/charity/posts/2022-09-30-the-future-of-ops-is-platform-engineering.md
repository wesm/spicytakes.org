---
title: "The Future of Ops is Platform Engineering"
date: 2022-09-30
url: https://charity.wtf/2022/09/30/the-future-of-ops-is-platform-engineering/
word_count: 2680
---


First published on 2022-09-30 at [https://www.honeycomb.io/blog/future-ops-platform-engineering.](https://www.honeycomb.io/blog/future-ops-platform-engineering.)


Two years ago I wrote a piece in The New Stack about the [Future of Ops Careers](https://thenewstack.io/the-future-of-ops-careers/). Towards the end, I wrote:


> *The reality is that jack-of-all-trades systems infrastructure jobs are slowly vanishing: the world doesn’t need thousands of people who can expertly tune postfix, SpamAssassin, and ClamAV—the world has Gmail. (…)*
> *Building infrastructure and operational expertise used to be bundled together into a single role. But the industry is now bifurcating along an infrastructure fault line, and the overlap between infrastructure-oriented engineers and operationally-minded engineers is swiftly eroding. Engineers who love this work increasingly have a choice to make. Either you can 1) go deep on infrastructure by joining a company that does infrastructure as a service, or 2) go broad on operability by joining a company to help them do as little infrastructure as possible.*


I described the second category as “operations engineering minus the infrastructure,” dedicated to evaluating and assembling a production stack of third-party platform providers, enabling software engineers to self-serve their services and own their own code in production. I said:

- Your job will be to aggressively minimize the cycles your org devotes to infrastructure by finding effective ways to outsource or minimize infra labor. Your job is to NOT go deep if there is any workable alternative.
- Your job will be to work cross-functionally with all the other software engineering teams, looking for ways to speed up their time to value and helping them own their own code in production.
- Your job will be to move past the kludgey old models of “outsourcing” to sophisticated understandings of how and where to leverage abstractions that can radically accelerate development.


That second category I was describing now has a name. We call those teams “platform engineering.”


## The fifty-year arc of software careers


In the beginning, there were people who wrote and ran software. At some point, we spun away ops skills from dev skills into two different professions, but that turned out to be a ginormous mistake, so along came DevOps to reunify them. Nowadays, ops as an independent profession is in the process of fading out. Companies are spinning down their ops teams left and right. Engineers who formerly identified as sysadmins or operations have turned into DevOps engineers, and soon there will just be “software people” again. This is the way of things.


Please note that this is NOT the same thing as saying “ops is dead,” or “ops skills are no longer valuable or needed1.” Our systems are only getting more complex, more difficult to operate, and simultaneously more critical to life on earth, which means that operational excellence has never been more desperately needed (and if you don’t respect that, 🌈 you deserve to suffer 🌈).


The industry story of the past three to five years has been us trying to figure out how to help software engineers own their own code in production2, phasing out dedicated ops teams, and aggressively outsourcing as much infrastructure as possible.


*As we should*. Developer cycles are the scarcest resource in your company, and you want to spend as many of those as possible on your core product: the crown jewel, the code that makes you a business. Money is cheaper than engineering cycles, and teams that are focused on their core business will always outperform teams whose focus is spread across dozens of non-revenue-generating projects. Let someone else build and run all the dependencies and adjacencies.


**Before**: some engineers wrote code, and some engineers ran code.


**Now**: all engineers write code, and all engineers run the code they write.


## Platform engineering is what stands between you and darkness


When you start talking about putting software engineers on call for their own code, and generally being more involved in production, some percentage of the time you will hear back a guttural wail of despair: *“You can’t expect me to know EVERYTHING about EVERYTHING!”*


Quite right; we can’t. Platform engineering teams are part of the answer to this perfectly reasonable complaint. It’s not that you’re being asked to do or understand more *in toto*, but the distribution of labor and responsibility is shifting:


**Before**: some engineers wrote code, and some engineers ran code.


**Now: **all engineers write code, and all engineers run the code they write—but we divide the areas of responsibility by layer or function.


## The emergence of a minimum viable self-serve tier


In the earliest days of a company, your first few engineers end up bootstrapping an infrastructure by reading AWS docs or blog posts, or asking a friend for recommendations to get started. They might start by setting up a managed container service, or configuring Terraform, and for a while everybody deploys and owns their own code, just as god intended.


But cognitive limits kick in pretty quickly. The maze of APIs and SDKs and components out there is simply bewildering, even for an experienced ops hand. Before long, it becomes *someone’s* job to make good decisions, pick a suite of compute and storage options that serve the team’s needs, and write some tooling that pulls everything into a coherent whole—which, at a minimum, lets you:

1. Run tests and generate new artifacts
2. Deploy artifacts, version them, and roll back
3. Instrument, monitor, and debug
4. Store data somewhere, manage schemas and migrations
5. Adjust capacity as needed
6. Define and commit all components (and their relationships) as code


Once these are built, it should be trivial for an engineer to come along and spin up a new service using templates and components from existing services. It should be much simpler and easier to use the blessed paths than anything else, and there should be friction if you go off the beaten path.


Congratulations! You’ve just been platformed 🎉. One of the key principles of any developer platform is that *it should be easy to do the right things, and hard to do the wrong things*.


## The differences between platform engineering and traditional ops


Platform teams are typically staffed by engineers who are comfortable writing software. Not just scripting and automation, but writing tests and doing code reviews. Platform teams also operate much more like product development teams do, with product managers (and occasionally, designers, developer advocates, or UX researchers).


This doesn’t mean that everybody on a platform team has to have originally been a software engineer; in fact, a super common failure condition for platform teams is simply thinking all they need to do is hire software engineers to build developer tools. **A strong platform team has an equally deep grounding in operations experience and software development.** Individuals who are experts in both areas are fairly rare, but you can pull together a strong, well-rounded *team* by assembling a mix of SWEs (with some ops experience) and ops or DevOps engineers (with some software experience) and having them learn and grow from each other.


Platform teams are decidedly cloud-native; they actually mostly involve platforms built atop the cloud itself—PaaS, IaaS, everything-aaS, serverless, and so forth.


Ops/DevOps teams are oriented around *managing infrastructure, *often several generations of infrastructure. Their turf is everything from data centers and bare metal up through virtualization, containers, and the cloud (they aren’t so much cloud-native as cloud-enabled). They measure themselves on things like SLOs and the DORA metrics. You know they’re doing a good job if the system is up/available and users are happy.


Platform teams are oriented around *providing a good experience for developers to self-serve and self-manage their code. *The more swiftly and easily developers can move, the better your platform team. Operational excellence, in the platform model, is actually more the responsibility of the other engineering teams (and/or an adjacent SRE team) than that of the platform team.


Platform teams typically work higher up the stack than operations, DevOps, or SRE teams do, and they involve a great deal less infrastructure. On the contrary, platform teams are bent on paying other people to run as much shit as possible, preserving their own scarce development cycles for their core product.


Here is a somewhat tongue-in-cheek table of the similarities and differences between the archetypes.


## Platform engineers vs. DevOps engineers



|  | **Platform Engineer** | **Ops (or DevOps) Engineer** |
| **% of job spent writing code** | > 50% | < 50% |
| **Rest of time spent** | Gathering product requirements, doing user research, architecture discussions, optimizing internal workflows, researching new tools and developer productivity ideas, reviewing other teams’ diffs for impact, performance tuning, helping other engineers own & scale their code, fixing CI/CD pipelines. | Fixing cron jobs, automating old setup docs, converting PXE/rsync to Chef/Puppet, converting Chef/Puppet to Terraform, converting VMs to containers, deploying software, debugging broken deploys, writing monitoring checks, doing retros, building out new services, pairing with software engineers to understand and debug their code, investigating weird shit, documentation, etc. |
| **Responsible for** | Enabling internal teams to self-serve their ability to run and own their code in production. Creating standard, reusable components and processes. [Defining golden paths](https://charity.wtf/2018/12/02/software-sprawl-the-golden-path-and-scaling-teams-with-agency/). | Infrastructure capacity planning, scaling, performance tuning, upgrading. Reliability and resiliency, SLOs and monitoring/alerting. Delivering quality experience to customers. |
| **Builds for** | Internal developer teams | Customers |
| **Development style** | Infrastructure as a product | Infrastructure as code |
| **Works with product managers** | Yes | No |
| **Works with UX researchers or designers** | Sometimes | No |
| **Dashboards & graphs** | Uses APM, observability, tracing. Cares a lot about instrumentation and OpenTelemetry. | Uses metrics, logs, dashboards; monitoring, alerting, and agent/sidecar/blackbox telemetry. |
| **What ‘coding’ means to them** | Developing new features & services, writing tests. These are (primarily) software people who do systems. | Automation, configuration, DSLs, extending and debugging existing code. These are systems people who do software. |
| **Preferred language** | Go, Rust | Python, Ruby |
| **Time spent in Linux** | Hardly any | A lot |
| **Succeeds when** | Developers can easily choose good defaults, self-serve their infra, and own their own code in production. | Infrastructure is scalable, secure, cost-effective, reliable, and customers are happy. |
| **Native terrain** | Serverless, *aaS, APIs for everything (cloud-native and above). | Instances, VMs, containers, regions, multi-cloud (everything “below,” but up to and including the cloud). |
| **Databases** | Uses hosted DBs | Runs their own, blending automation & DBA expertise |
| **SSH** | No | Yes |
| **Shell** | REPL | bash/zsh |
| **Mantra** | “Run Less Software” | “Cattle, Not Pets” |



## What about DevOps vs. SRE?


Countless words have been spilled on the difference between DevOps and SRE3, which I won’t rehash.


Here’s what I’ll say: DevOps, to me, feels like a relevant concept for companies that have a lot of infrastructure to wrangle. Companies that do in fact have dev teams and ops teams, or dev teams and DevOps teams (🙄), tend to have a lot of operational shit to automate, test, and run. They use config management, virtualization, *and* containers, often managing several generations worth of technology, possibly even down to data centers and bare metal. DevOps is for companies that have some combination of bare metal, VMs, regions, AZs, multi-cloud, networking devices, self-managed databases, etc.


DevOps is capacious. It contains multitudes. DevOps writes code, and DevOps has a fuckload of code to manage.


It is also on its way to becoming irrelevant. We are swiftly entering a post-DevOps world.


SRE, to me, feels different. I associate SRE with very large companies, where they *mostly* have software engineers owning their own code in production, but maybe still struggle with it a bit. SREs are often embedded within software engineering teams or product groups, and they focus a lot on, well, reliability, as the name suggests.


This means they do less infrastructure jockeying or automating (although they still do some coding). They typically have a lot to say about instrumentation, monitoring and observability, and cross-functional coordination. They run incident response and do blameless retros, and they tend to be experts at scaling.


If a company has both a DevOps team and SRE, typically I expect to see the SRE team more on the frontlines, involved with incidents, telemetry, etc., and DevOps teams more on the backburner, slinging pipes and plumbing.


## Observability engineering as a case study


In the same piece I referenced earlier, I also wrote about the role of observability teams. I said they should largely no longer be running their own monitoring and graphing software in-house. Yet there is still a place for observability teams to exist: they remain a critical link between outsourced solutions and internal developer needs.


> *That team should write libraries, generate examples, and drive standardization; ushering in consistency, predictability, and usability. They should partner with internal teams to evaluate use cases. They should partner with your vendors as roadmap stakeholders. They might also write glue code and helper modules to connect disparate data sources and create cohesive visualizations. Basically, that team becomes an integration point between your organization and the outsourced work.*


I originally wrote this about observability, but it could just as easily be used to describe platform engineering as a whole. This is the role—being the bridge between other vendors and your own core software. It’s a very high-leverage place to sit.


## Ops is dead, long live ops


I’ve spent a lot of time thinking about this because we’ve had such a hard time nailing down exactly who the Honeycomb customer is. Sometimes our buyer is an ops team buying it for their SWEs, sometimes it’s SREs in the midst of an outage, sometimes it’s a VP or director of engineering, or an architect, or a CTO, or a “full stack” engineering team, or even a product manager. It is hard to form a snappy answer out of that list.


The first couple questions every new go-to-market candidate asks us are “who is your buyer?” and “how do we help them?” To which I respond with a five minute ramble where I list every above persona and each of their pain points. Hardly the concrete answer they would like to receive.


As it goes, [sociotechnical](https://www.honeycomb.io/blog/the-future-of-software-is-a-sociotechnical-problem) trends come and go. A year ago, Christine and I were speculating that platform engineering might be on the verge of consolidating the necessary ingredients that makes up our ideal buyer:

1. Writing and shipping code, and needing to understand their own code
2. Positioned to help other teams with their instrumentation patterns and tooling
3. Firmly cloud-native+ and untethered to hardware or traditional infrastructure


To my delight, since that conversation, these trends have only accelerated—and I, for one, welcome our new platform engineering overlords to the observability table. ☺️


If you’d like to learn more about platform engineering, we’ll be running a Twitter space on ✨ October 20th ✨ at 12:00 p.m. PT. [Come join us](https://twitter.com/i/spaces/1vOxwMnyXpPGB)! I’ll be there along with two colleagues and we’ll be answering your questions and shedding more light on the topic.


---


1  *I do hear people saying that, and it used to make me fucking furious, but now I just smugly remind myself how much self-inflicted suffering they are in for. Disrespecting operational expertise is the shortest path to never again sleeping through the night.*


2 *It is rather incredible how rapidly this idea has taken off. When we started talking about putting developers on call for their code in 2016, people got seriously angry with us. Before that, the only twitter mention I could find of putting devs on call was one by (of course) Adrian Cockcroft, but by 2019-2020 it had stopped being controversial and soon became common wisdom.*


3 *I actually wrote one of those myself: [DevOps vs SRE: Delayed Coverage of the Dumbest War](https://charity.wtf/2016/06/30/devops-vs-sre-delayed-coverage-of-the-dumbest-war/)). LMAO. I think Liz had the final word on this back in … 2017? 2018? … when she said something like [class SRE implements DevOps](https://datacentremagazine.com/events/whats-difference-between-devops-and-sre). And yes, DevOps is a philosophy or a methodology and not a job title, etc.*
