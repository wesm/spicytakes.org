---
title: "Ritual Brilliance: How a pair of Shrek ears shaped Linden Lab culture by making failure funny — and safe"
date: 2023-05-30
url: https://charity.wtf/2023/05/30/ritual-brilliance-how-a-pair-of-shrek-ears-shaped-linden-lab-culture-by-making-failure-funny-and-safe/
word_count: 2203
---


*[Originally posted on the now-defunct “Roadmap: A Magazine About Work” website, on May 30th, 2023. [A pretty, nicely-formatted PDF version of this article can be downloaded here.](https://charity.wtf/wp-content/uploads/2025/02/Ritual-brilliance-_-Roadmap-1.pdf) Thanks to Molly McArdle for editing!]*


If you talk to former Lindens about the company’s culture—and be careful, because we will do so *at length*—you will eventually hear about the Shrek ears.


When you saw a new person wearing the Shrek ears, a [matted green-felt ](https://www.amazon.com/Pms-Shrek-Dress-Up-Ears/dp/B000UXUSD6)headband with ogre ears on it, you introduced yourself, congratulated them warmly, and begged to hear the story of how they came to be wearing them. Then you welcomed the new person to the team (“You’re truly one of us now!”) and shared a story about a time when you did something even dumber than they did.


My first job after (dropping out of) college was at [Linden Lab](https://lindenlab.com), the home of *Second **Life*. I joined in 2004 and stayed for nearly six years, during which the company grew from around 25 nerds in a room to around 400 employees who worked out of offices in Brighton, San Francisco, Menlo Park, and Singapore, or their own homes—wherever they were.


When I think back on that time now, almost two decades later, I’m puzzled by the Shrek ears phenomenon. I wasn’t exactly powerful then, at barely 20 years old. Not only was this my first real job, I was also the first woman engineer, and I made *tons* of mistakes. Shouldn’t I have found the practice of being systematically singled out and spotlighted for my errors humiliating, shaming, and traumatic?


Yet I remember loving the tradition and participating with joy and vigor. Everyone else seemed to love it, too. The practice spread beyond engineering and out into the rest of the company, not by fiat but because individual people would voluntarily track down the Shrek ears and put them on their own head. (I’m not imagining this, right?)


## Step 1, break production; Step 2, put on Shrek ears


Here’s how it worked: The first time an engineer broke production or caused major outage, they would seek out the ears and put them on for the day. The ears weren’t a mark of shame—they were a **badge of honor**! Everyone breaks production eventually, if they’re working on something meaningful.


If people saw you wearing the ears, they would eagerly ask, “What happened? How did you find the problem? What was the fix?” Then they would regale you with their own stories of breaking production or tell you about the first outage they caused. If the person was self-flagellating or being too hard on themselves, the Shrek ears gave their colleagues an excuse to kindly but firmly correct it on the spot. It was Linden’s way of saying, *Hey, we don’t do that here*: “You did the reasonable thing! How can we make the system better, so the next person doesn’t stumble into the same trap?”


In those days, Linden was running a massively distributed system across multiple data centers on three continents, and doing so without the help of DevOps, CI/CD, GitHub, virtualization, the cloud, or infrastructure as code. We had an incredibly high-performing operations team, with a thousand-to-one server-to-ops engineer ratio, which was a real achievement in the days when the role required doing everything from racking and stacking boxes in the colocation center to developing your own automation software.


**Failures were just fucking inevitable.** In a world like that, devoid of the entire toolchain ecosystem we’ve come to rely on, you just had to learn to roll with it, absorb the hits, and keep moving fast. You could only test so much in staging; it was more important to get it out into production and watch it—understand it—there. It was better to invest in swift recovery, graceful degradation, and decoupling services than to focus on trying to prevent anything from going wrong. (Still is, as a matter of fact.)


This might all sound a little overwrought to you—maybe even dangerous or irresponsible. Didn’t we care about quality? Were we bad engineers?


## The Shrek ears were “blameless retros” before there were blameless retros


I assure you, we cared. The engineers I worked with at Linden were of at least as high a caliber as the engineers I later worked with at Facebook (and a whole lot more diverse). In this specific place and time, the Shrek ears were what we needed to alleviate paralysis and fear of production, and to encourage the sharing of knowledge—even if anecdotal—about our systems.


In retrospect, **the Shrek ears were a brilliant piece of social jujitsu**. There was an element of shock value or contrarianism in celebrating outages instead of getting all worked up about them. But the larger purpose of the ears was to reset people’s expectations (especially in the case of new hires) and reprogram them with a different set of values: Linden’s values.


In the years since those early days at Linden, the industry has developed an entire language and set of practices around dealing with the aftermath of incidents: blameless post mortems, retrospectives, and so on. But those tools weren’t available to us at the time. What we did have was the Shrek ears. A couple of times a month something would break, the ears would be claimed, and we would all go around reminding one another that **failure is both inevitable and ridiculous**, and that no one is going to get mad at you or fire you when it happens.


## Failure is always a question of when, not if


It’s important to note that you never saw anyone get teased or shamed for wearing the ears or for breaking production. There was a script to follow, and we all knew it. We learned it from watching others put on the ears, or by donning them ourselves. On a day when the Shrek ears had appeared, people would gather around at lunch or at the bar after work and swap war stories, one-upping one another and laughing uproariously.


Every new engineer was told, “If you never break production, you probably aren’t

doing anything that really matters or taking enough risks.”


It’s also important to emphasize that the ears were opt-in, not opt-out. You didn’t have to do it. And if you did take them, you could expect a wave of sympathy, good humor, and support. It affirmed that **you deserved to be here,** that you were part of the team.


And though the Shrek ears started in engineering, people in sales, marketing, accounting, and other departments picked them up over the years. It was a process of voluntary adoption, not a top-down policy. Someone would announce in IRC that they were wearing the ears today, and why. The camaraderie and laughter that ensued were infectious—and made it easier and easier over time for people to be transparent about what wasn’t working.


## Rituals exist to instill values and train culture


In *Rituals for Work,* Kursat Ozenc defines rituals as “actions that a person or group does repeatedly, following a similar pattern or script, in which they’ve imbued symbolism and meaning.” **Ritual exists to instill a value, create a mindset, or train a reflex.**


And this particular ritual was extremely effective at taking lots of scared engineers and teaching them, very quickly:


✨ It is safe to fail✨

✨ Failure is constant✨

✨ Failure is fucking hilarious✨


At Linden, failure was not something to be ashamed of or to hide from your teammates. We understood that it’s not something that happens only to careless or inexperienced people. In fact, the senior people have the funniest fuckups—because what they are trying to do is insanely hard. **The Shrek ears taught us that you fail, you laugh, you drink whiskey, you move on.**


Other companies had similar rituals around the same time—Etsy famously had the “[three-armed sweater](https://www.infoq.com/articles/crafting-resilient-culture/),” which they would pass around to whoever had last broken production. But I’ve never again worked at a place where mistakes were discussed as freely and easily across the entire company as they were at Linden Lab. And I think the Shrek ears had a lot to do with that.


Their point was never to single out the person who had made a mistake and humiliate them, but the exact opposite. By putting on the ears, you said not just “Hi, I made a mistake” but also “I’m going to be brave about it, so we can all collectively learn and improve.” **It was a ritualized act of bravery** rewarded by affirmation, empathy, and acceptance. At Linden, the Shrek ears weren’t just a terrific tool for promoting team coherence and creating a sense of belonging. They also provided structure to help individuals and teams recover from scary events, and even traumas.


## In so many ways, Linden Lab was ahead of its time


Linden was an extremely strange workplace when I was there, and it inspired unusually strong devotion, which we self-deprecatingly referred to as “the Kool-Aid.” It can be difficult to convey just how radical and weird it was at the time because the world has changed so much since then, and so many of the company’s “weird” philosophies have since gone mainstream. (Though not all: using “Kool-Aid” as a casual phrase to denote “excessive enthusiasm” or “cult-like devotion” is now recognized by many as being in poor taste. After all, people actually died at the Jonestown massacre.)


In a lot of ways, Linden culture (and *Second Life* technology) was profoundly, recognizably modern, and similar to the best workplaces of today, 20+ years later.


[Philip Rosedale](https://www.linkedin.com/in/philiprosedale/), Linden’s founder and CEO, is an inventor and technologist who believed it was every inch as interesting and important to experiment with company culture as with the virtual worlds we built. Except we did it all from scratch: building the technology and the culture together. And this led us down some weird rabbit holes, such as a cron job that [rsynced the entire file system ](https://www.slideshare.net/slideshow/system-imager20051215/149955)down over thousands of live servers every night. And the Shrek ears.


There was a period when “Choose your own work” was a company core value, and there were effectively no managers. (Not every experiment worked!) We went all-in on a fully distributed company culture at a time when practically no one else had. We ran a massively distributed, high-concurrency virtual world at a time before microservices, sharded databases, config management virtualization, AWS, or SRE and DevOps.


## I can understand why people now find this story horrifying


With the distance of time, I get why the Shrek ears might make you recoil. If you think “That sounds awful! What kind of monsters would do that to each other?”—you are far from alone. Any time I mention the story in public, a sizable minority of people are aghast and appalled. Representative quotes include:


> “I hope you realize how many people you traumatized by doing this to them.”


> “I wonder how many introverted people found this excruciating but were too
> afraid to say so.”


> “Office bullying is fucked up even with cute Shrek ears.”


Even:


> “We heard about the Shrek ears from an engineer we interviewed. He was telling us how great they were, but we were all so horrified that we declined to hire him because of it.”


And they’re right. **It sounds awful to us now**. It really does! It sounds like we were singling people out for their failures, like a dunce cap. I wouldn’t be surprised to someday learn that, in fact, a small number of people *did* felt pressured into using the ears, or hated them and were too afraid to say something. But how do we account for the fact that this tradition was so deeply beloved by so many—and that we are still fondly reminiscing about it more than 15 years later? It had a purpose.


Linden Lab was an incredibly progressive company for its time: very anti-hierarchical, very much about empowering people to be creative and independent. It also was *by far* the most diverse company I’ve ever worked in (other than [Honeycomb](http://honeycomb.io), which I cofounded and where I’m CTO), with lots of women and genderqueer and trans people and people of color. We were way out on the sensitive branch relative to tech at that time. It’s tough to square this knowledge of what Linden was like as a place with the reactions some people outside the organization have to the Shrek ears.


I think this is, above all, a sign of progress. So many questionable practices that were ordinary back then—like referring to everyone as “guys,” using terms like “master/slave” for replication, or throwing alcohol-sloshed parties—are now rightfully frowned upon. We have become more sensitive to people’s differences and more clued into the power dynamics of the workplace. It’s far from perfect, but it is a lot better.


As a ritual, the Shrek ears were powerful and did the job. They were also fun—proving once again that **making something goofy is the best way to make it stick**. But I can’t imagine plopping Shrek ears on a new hire who has just broken production in 2023. And honestly, I think that’s probably a good thing. It’s time for new rituals.
