---
title: "Explaining tech's notion of talent scarcity"
date: 2023-04-25
url: https://nadia.xyz/top-talent
word_count: 3512
---


# Explaining tech's notion of talent scarcity


April 25, 2023


***TLDR:** Most conversations about “top talent” assume Pareto distribution; however, a closer examination suggests that different corporate cultures benefit from different types of talent distribution (normal, Pareto, and a third option – bimodal) according to the problem they’re trying to solve. Bimodal talent distribution is rare but more frequently observed in creative industries, including some types of software companies.*


*While Pareto companies compete for A-players (“high-IQ generalists”), bimodal companies compete for linchpins (those who are uniquely gifted at a task that few others can do). These differences account for variations in management style and corporate cultures.*


---


It was a group of consultants at McKinsey & Company who coined the “war for talent” in their [1998 report](https://www.researchgate.net/publication/284689712_The_War_for_Talent) and [subsequent book](https://www.amazon.com/War-Talent-Ed-Michaels/dp/1578514592/) of the same name, propelling the term “top talent” into the corporate executive hive-mind for the next two decades. While McKinsey refrained from offering a precise definition of talent, they thought that a shortage of  “smart, energetic, ambitious individuals” was coming, and that it would lead companies to fight to attract and retain the very best.


In software, there is a related but distinct notion of the “10x developer,” which dates at least as far back as [a 1968 study](https://dl.acm.org/doi/10.1145/362851.362858) that accidentally uncovered individual differences in programmer performance, and was further popularized by Fred Brooks’ 1975 book, [*The Mythical Man-Month*](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959/). The definition of a 10x developer is similarly vague, and its existence is frequently contested. Depending on who you ask, a 10x developer might be someone who can write code 10x faster; is 10x better at understanding product needs; makes their team 10x more effective; or is 10x as good at finding and resolving issues in their code.


Despite the similarity between these two concepts, McKinsey’s notion of *top talent* and software’s *10x developer* reveal subtle cultural differences. Both are concerned with identifying the best people to work with, but the McKinsey version defines the best as the top percentile in their field, whereas the 10x developer is often a singular, talented individual whose magic is difficult to explain or replicate.


For example, in conversations about hiring AI researchers, many people have said something to the effect of *“There are only [10-200] people in the world who can do what [highly-paid AI researcher] does.”* This is a very different statement from, say, *“We are trying to hire top AI researchers.”* In the latter case, “top” means the highest-performing slice of all AI researchers, but in the former, the assumption is that there are only a handful of people who can perform the job at all. While this idea is intuitive among software engineers, it is rarely seen in other industries.


Why can’t more people be trained to do certain tasks in software? Why aren’t there more Linus Torvaldses or John Carmacks? Will there only be 100 people, ever, who can do what some AI researchers do?


After exploring these questions, I identified three distinct models of talent distribution, which correlate strongly to industry, but vary even within industries, depending on what the company does and how mature it is:

- **Normal distribution:** Talent follows a normal distribution. Companies succeed not by attracting and retaining “top talent,” but by the strength of their processes, to which all employees are expected to conform. Frequently seen among manufacturing, construction, and logistics companies.
- **Pareto distribution:** Talent follows a Pareto distribution, skewed towards the top *nth* percentile. Companies benefit from attracting, retaining, and cultivating “A-players,” who are expected to demonstrate exceptional individual performance. Frequently seen among knowledge work and sales-centric companies.
- **Bimodal distribution:** Talent follows a bimodal distribution, where companies benefit from identifying, hiring, and retaining “linchpins,” who make up a fraction of headcount, but drive most of the company’s success. Frequently seen in creative industries (ex. entertainment, fashion, design), as well as software companies solving difficult technical problems (ex. infrastructure).


A company’s distribution type also shapes their organizational culture, which lives downstream of the types of talent they are most incentivized to seek out and hire. Most notably, we can understand the difference between what I’ll call McKinsey and Silicon Valley mindsets by understanding differences in their respective definitions of “top talent.” [1]


# Normal distribution


**Examples:** *manufacturing; freight and shipping logistics; construction*


Companies with a normal talent distribution are influenced by scientific management theory, or the “assembly line” approach, which emerged in the early 1900s in response to industrialization. This approach maximizes worker productivity while ensuring that the production process is highly predictable. Production is standardized and hierarchical, work is broken down into smaller tasks, and employees operate in lockstep as a machine.


The competitive advantage of these companies lies not in a select number of top performers, but in the strength of its processes, built on specialized knowledge that is refined through years of practice. Workers’ roles are clearly defined and rarely change. They need to be competent and reliable, but individualism is gently discouraged, as it threatens the resilience of the process. Employees take pride in maintaining performance and being part of something bigger than themselves, rather than in standing apart from their peers.


Toyota is a classic example of a company that differentiates itself through operational excellence, pioneering a more efficient approach to manufacturing throughout the second half of the 20th century. Their organizational culture is defined by “The Toyota Way” (its corporate philosophy, which emphasizes respect and a team-centric approach to continuous improvement) and the “Toyota Production System” (its manufacturing process, which emphasizes reducing waste). These philosophies tend to be emergent artifacts of tacit knowledge and practice, rather than articulated up front; The Toyota Way took decades to develop.


Companies that benefit from normal talent distribution can still experience talent scarcity: for example, a shortage of construction or warehouse workers. But scarcity usually comes from a lack of demand among workers for these jobs (due to, ex. low pay or high barriers to certification), rather than because the talent pipeline doesn’t exist at all.


# Pareto distribution


**Examples:** *management consulting, investment banking, strong sales cultures*


Companies with a Pareto talent distribution are influenced by modern management theories that emerged in the 1940s and 1950s. Peter Drucker, for example, envisioned decentralized, participatory management among employees, as well as the rise of “knowledge workers” who would play a more active role in guiding organizational strategy.


In this model, the central importance of knowledge workers and diffusion of managerial power among employees means that companies must preoccupy themselves with attracting, retaining, and cultivating “A-players,” or talent that performs at the top *nth* percentile of their field.


A-players are “high-IQ generalists’’ who can excel at many different types of tasks and are capable of handling complexity at work. As described in McKinsey’s 1998 report, executives at “high-performing” companies (defined by the top percentile of shareholder returns) were more likely to have attended a Tier 1 undergraduate school, graduated in the top 10% of one’s class, had a higher undergraduate GPA, and had a master’s degree. An A-player might also have at least one or two hobbies they’re exceptional at, whether competitive rowing, language learning, or classical piano. They tend to perform at the top of their field, regardless of what they do.


> “Companies [should not] hesitate to go outside their own industry. Sears hired Gulf War general Gus Pagonis to run its logistics; Banc One hired Taco Bell head Ken Stevens to lead retail banking.” – McKinsey’s [The War For Talent report](https://www.researchgate.net/publication/284689712_The_War_for_Talent)


A-players can be quantitatively defined and ranked against B- and C-players, which is why management consulting firms use IQ tests, math tests, and personality tests to hire A-players. Because this type of talent is easier to identify, Pareto-distribution companies often have robust recruiting programs to hire graduates straight out of college: specialized skills matter less than general competence.


Management consulting (ex. McKinsey, BCG, Bain), investment banking (ex. Goldman Sachs, JP Morgan), and Big Tech associate product manager programs (ex. Facebook, Google) all recruit heavily out of college, with plenty of interview tips and preparation materials proactively offered. Applying to one of these jobs is not so different from studying for college entrance exams or applying to a top-tier university.


If a normal-distribution company is more like socialism – where employees see themselves as part of a bigger machine, and benefits are evenly distributed – the Pareto-distribution company is more like capitalism, where rewards are unevenly distributed, accruing to the best performers. Employees are expected to be exceptional; consistently average performers who merely “meet expectations” will languish or be fired. Because not every employee can be exceptional (or else it would just be the new average), this leads to zero-sum internal competitions for power.


In terms of talent scarcity, A-players represent a comparatively small percentage of the population. But, with the benefit of twenty years’ hindsight, McKinsey probably overstated the idea that there would be a “war” for A-player talent. Senior A-players are widely known and competed for, so employers pay well to keep them from being poached. But among junior A-players, even though the pool is somewhat fixed, it’s still a big pool, relative to the number of jobs that require A-players. And they are relatively easy to identify and cultivate.


While junior A-players may be more interchangeable with one another, companies do fight for a monopoly over the talent pipeline. McKinsey, Goldman, and Google, for example, all want to be the de facto place for top college graduates looking for their first job. Although these companies are not actually competitors in terms of products, they are competitive when it comes to owning the A-player talent pool.


There is also a sort of “brain drain” paradox that occurs *within* an organization, rather than between organizations, where A-players tend to gravitate towards (or are recruited into) high-visibility management roles. This makes it harder to hire and retain A-players for lower-paying or less visible types of roles. Jan Fields, former CEO of McDonald’s, started out as a fry chef; Stuart Rose, former CEO of Marks & Spencer, started out on the sales floor. In other words, although there are other roles that could benefit from A-player skills, A-players are groomed to only do certain types of roles, so that there is no shortage of A-players competing for a small number of high-profile roles. [2]


# Bimodal distribution


**Examples:** *software infrastructure (ex. data management, cloud computing, security); hedge funds; creative industries (ex. entertainment, fashion, design)*


Companies that benefit from bimodal talent distribution succeed by attracting and retaining “linchpins,” whose unique skills provide a competitive advantage to the company. In contrast to A-players – generalists that like to solve any problem thrown at them – linchpins are specialists who are very, very good at one particular type of task, which most other people in the world cannot do.


This type of company is rare, but more frequently observed among software companies tackling difficult technical problems, as well as creative industries. Disney’s Bob Iger blocked Marvel’s CEO Ike Perlmutter from firing its president, Kevin Feige, after they acquired the company, whom Iger saw as its visionary. Apple’s history is frequently told through the dynasties of its most iconic designers: Steve Jobs, Jony Ive.


Linchpins are qualitatively defined, and are thus especially difficult to hire for, or even identify. While A-players willingly cram for their exams at Tier 1 management consulting firms, software engineers frequently criticize code interviews and hiring practices because they think they don’t accurately test for ability. The lack of consensus around what even constitutes a 10x engineer, again, points to the difficulty in quantifying linchpin talent, even if everyone ‘knows it when they see it.’


> “I came to see that the types of people who are good at pleasing admissions committees are not the types of people who are good at founding companies.” – Michael Gibson, [*Paper Belt on Fire*](https://www.amazon.com/Paper-Belt-Fire-Investors-University/dp/B0B8LT7SPQ/), reflecting on the Thiel Fellowship program, which he helped launch and run


Linchpins are more frequently observed in software because, unlike physical engineering, software has sprawling complexity. A civil engineer who builds a bridge must conform to industry standards that limit their creativity, and they are beholden to the laws of physics regardless.


But writing software has no such constraints. Solving problems with code has an infinite possibility space; what you can build, and how you build it, is only bound by imagination. New programming languages, tools, and frameworks can be invented entirely and used as needed. Unless the task is well-understood and frequently repeated, one cannot simply teach an engineer what to do in every circumstance, because there are endless “unknown unknowns” that could lead to better solutions.


Similarly, fixing bugs has an equally infinite (and frustrating) possibility space; unlike a civil engineer, who can see and inspect a malfunctioning bridge, code that doesn’t act as expected can be blamed on any number of invisible dependencies. The gap between an average and exceptional software engineer, then, is much bigger than that between an average and exceptional physical engineer, as an exceptional developer can “see” possibilities that an average one cannot, due to some amorphous combination of intelligence, creativity, and intuition. [3]


Most software companies these days don’t require linchpins, however, because they sell commoditized products without a competitive technical advantage. While these products may not have to conform to industry standards, as with physical engineering disciplines, the right tools for the task are strongly influenced by social norms. This seems to be where much of the confusion lies regarding “10x developers:” while historically, virtually all software companies were tackling difficult technical challenges, today, most probably look more like Pareto-distribution companies, and should follow a different management approach.


But companies that are building foundational technology still benefit from linchpins. For example, Snowflake was co-founded by Benoît Dageville and Thierry Cruanes, two highly respected software architects at Oracle; Databricks was co-founded by the creators of Apache Spark.


Bimodal-distribution companies benefit from what Sebastian Bensusan calls [“high variance management,”](https://blog.sbensu.com/posts/high-variance-management/) which he compares to producing a Hollywood movie instead of a Broadway play. With a live performance, an actress must be able to deliver her lines correctly at every single performance, so it’s important to select for consistency. But when filming a movie, the actress can fail six times if that means she produces one really amazing performance. Thus, a movie director can be more adventurous in deciding who to cast, as well as encourage her to take risks with her performance.


> “Talent with a creative spark…is where the bureaucratic approach is most deadly.” – Tyler Cowen, [Talent: How to Identify Energizers, Creatives, and Winners Around the World](https://www.amazon.com/Talent-Identify-Energizers-Creatives-Winners-ebook/dp/B08R2KNYVX/)


At bimodal-distribution companies, only a handful of linchpins are needed; everyone else at the company plays a supporting role. At first glance, these companies might look like they are normal distribution, because they have tightly-organized production processes, but the difference is that everyone is working in support of a single individual’s vision. Fred Brooks compared this to surgical teams in *The Mythical Man-Month*, where “few minds are involved in design and construction, yet many hands are brought to bear.”


Linchpins are usually siloed from one another: a team comprised of linchpins doesn’t necessarily produce great outcomes, versus having teams that are each centered around a linchpin, who’s paired with a supporting team.


Linchpins are more likely than A-players to produce work of public benefit, such as inventing a new technology or design, which can muddle their market value to employers. By contrast, an A-player’s value is usually confined to their employer – for example, managing teams or projects, or generating sales – which makes the return on investment clear.


Only when linchpins offer private value (ex. infrastructure providers competing to hire a software architect) will they command large sums in the market. The heated competition for AI researchers between Google and Microsoft/OpenAI, for example, is partly driven by these dynamics. Because these companies are building foundational technology, whoever aggregates the most AI researchers from a select pool of hires will have a major competitive advantage.


On the other hand, companies don’t fight to hire prolific open source developers – unless having their expertise in-house gives the company a competitive advantage – because an open source developer’s output is primarily a public good: they will produce that same value regardless of whom they work for.


## Right hands


There is also a variant of linchpins that I’ll call “right hands” (a term borrowed from [ex-Stripe Will Larson](https://lethain.com/staff-engineer-archetypes/)). Right hands are people who enjoy a uniquely high-trust, close relationship to at least one executive, and operate as a proxy for that executive’s interests.


Although right hands are often generalists, they are more similar to linchpins than A-players, because they are qualitatively defined, have a unique role that no one else can perform, and work best in silos. Like linchpins, right hands are a rare form of talent, and companies need them to achieve their most ambitious, innovative goals. They are – ideally – exceptionally competent, loyal to the company, and capable of seeing the “big picture.”


A right hand’s value is primarily derived from being an executive’s “chosen one,” which gives them unusual levels of creative working freedom. Because this freedom is so contextual, their success is typically confined to one company, and/or working with that particular executive. Right hands don’t necessarily have senior titles, nor is their true impact and favored position always visible to outsiders. Unlike A-players, they don’t tend to follow a typical corporate leadership path – they’re more likely to start their own companies afterwards, versus becoming an executive at another company. (This phenomenon can be observed among highly successful startups, which create “mafias” of early employees.)


> “I care a LOT about Stripe: when I see something out of place I feel antsy and want to fix it.” – Michelle Bu, [Payments Products Tech Lead at Stripe](https://staffeng.com/stories/michelle-bu/)


> “[W]hen Jack Welch met with The Home Depot to share what is distinctive about GE’s approach to managing growth, he took two human resources executives with him…building their bench is a crucial part of their job.” – McKinsey’s [“The War for Talent” report](https://www.researchgate.net/publication/284689712_The_War_for_Talent)


# Putting these models into practice


A company’s talent needs might change over time. For example, while Google likely started as a bimodal-distribution company to build its advantage in search, it appears to have become more of a Pareto-distribution company as the organization matured (though I’m not sure this was advantageous for its reputation as an innovator!).


Corporate culture norms can be explained by the types of talent that a company is trying to acquire or cultivate. For example:

- **OpenAI’s heavy mission focus and its unusual governance and funding structure** can be partly explained by its need to attract “linchpin” AI researchers, who are often very principled
- **OKRs, KPIs, and similar performance frameworks** are designed for Pareto-distribution companies, where performance is quantifiable and measurable against other employees
- **Zero incident culture (“X days without an accident”)** emphasizes consistency and collective responsibility, and discourages risky behavior among normal-distribution companies
- **The prototypical software company culture** (flexible hours, games and snacks in the office, “quiet areas”) was designed to attract and retain linchpin developers


Finally, different models of talent partly explain the differences between McKinsey and Silicon Valley cultures. The former is highly quantified, favors tightly-coordinated teams of overachievers, and encourages a competitive zero-sum talent environment (A-players are a fixed percentile of the overall pool, and if you’re not in, you’re out). The latter skews more qualitative, favors lone “creative genius” archetypes, and has a positive-sum approach to talent (linchpins could be lurking anywhere, and we surely haven’t uncovered them all). It could also help explain why historically, many software companies struggle to mature or produce shareholder returns in public markets, as succeeding at this scale requires transitioning organizational culture from bimodal- to Pareto-distribution. [4]


*Thanks to Sebastian Bensusan, Bernadette Doerr, and Daniel Lee for conversations that influenced the direction of this piece.*


### Notes

1. As discussed later, many if not most software companies are probably Pareto-distribution now, because they don’t compete on technical advantage. But – unlike management consulting – the software industry was historically built upon the notion of bimodal talent distribution, and is still culturally influenced by this way of seeing the world. ↩
2. See also: Peter Turchin’s notion of *elite overproduction,* or the idea that society produces too many elites for a limited number of powerful positions. ↩
3. I was struck by how every engineer I spoke to struggled to articulate this concept more precisely. The words “voodoo,” “magic,” and “alchemy” were all used. The competitive advantage of linchpins reminds me, surprisingly, of normal-distribution companies at the organizational level, where process power can’t be described or replicated because it is acquired through tacit knowledge. But in the case of software engineers, this indescribable advantage occurs at the individual level. ↩
4. I don’t know if this is true or not. It’s a hypothesis! ↩


---


*For future updates, subscribe via [newsletter](https://nayafia.substack.com/) or [RSS](https://nadia.xyz/feed.xml). Get in touch via [Twitter](https://twitter.com/nayafia).*

Google tag (gtag.js)