---
title: "All I want is to know what's different"
subtitle: "Rather than trying to guarantee correctness, what if we tried to guarantee consistency?"
date: 2023-06-09T16:44:39+00:00
url: https://benn.substack.com/p/all-i-want-is-to-know-whats-different
slug: all-i-want-is-to-know-whats-different
word_count: 1984
---


![Bill Walsh: A Football Life - The West Coast Offense - YouTube](https://substackcdn.com/image/fetch/$s_!x3Ei!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a5a9bb0-9b9b-41b4-b23f-315f3f1abe53_1280x720.jpeg)

*The score does not, in fact,take care of itself.*


Here are two methods for figuring out if some business metric is accurate:

1. Start with the metric and trace backwards, through its entire lineage graph, through every prerequisite calculation and transformation, through every upstream table that sits behind it, through every ingestion pipeline, all the way to the every source system of record that logged each original data point, and validate that, at each step of the computational process, every event is recorded, every logical definition is correct, and every test is passing. Confirm that your data contracts are alerting you of all known possible errors. Review the statistical distributions of incoming data streams for anomalous behavior. Check the CloudWatch logs1for dropped events. Audit Salesforce. Thoroughly inspect everything. And once you’ve proven the negative—that nothing is wrong—call the metric accurate.
2. Check if historical values of the metric are the same today as they were yesterday.


As data people, we seem to favor2the first approach. We create3data contracts that catalog what we expect source data to look like when it arrives in our warehouses. We build observability tools that constantly monitor that data for outliers. We write tests in dbt that confirm dates are dates, numbers are numbers, and unique keys are unique. We set up alerts that tell us when a pipeline stalls, when a job errors out, or when we’ve hit Marketo’s API limit and can no longer sync marketing data into Snowflake.


Despite all this effort, we still struggle to deliver metrics that people can trust. As Tristansaid a few days ago, we’ve built a massive technical system to support that goal, and yet, it’s still a system that most people side-eye—and some people work around entirely. The institution, to borrow Tristan’s term, is not good enough.


You could argue, I suppose, that we’re just not there yet. These tools are new; we need to learn how to use them. Features arestill getting built; best practices arestill being written; data contracts are still uncommon;4the data mesh isstill a dream. Over time, we’ll build our cathedral, brick by brick, release by release, blog post by blog post.


Maybe, but I’m skeptical. I’d contend that we’ve struggled to get people to trust our work because our approach to earning that trust—Method 1—is fatally flawed. The road from raw data to reliable metric has a limitless variety of potholes; there can be no system, no matter how complete or comprehensive, that can tell us we’ve patched all of them. Contracts, observability tools, data tests—these are mallets for playing whack-a-mole against an infinite number of moles.


More importantly, Method 1 isn’t how other people decide if they should trust the things that we produce. They don’t check our various observability dashboards and continuous integration tests; they don’t blindly accept our results when all of pipelines behind them are green; they don’t say, “There are no errors in Fivetran and the PR got a ‘lgtm’ GIF, so sure, I’ll gamble my career on these numbers.”


No,everyone else uses Method 2: “Do I believe this number, given what I believed yesterday?”


We do this so instinctively that we often don’t even notice. When I put together board decks, the most nerve-wracking moment was comparing the metrics in this quarter’s deck to the same numbers in last quarter’s charts. Nothing turns your stomach over faster than realizing you’ve accidentally revised all of your historical ARR figures. Conversely, there’s no better feeling than seeing all the graphs line up, and confirming that what you thought was true then is also what you think is true now.


In other words, trust isn’t built by confirming our sources; it’s built viamathematical induction. More than anything, our confidence in this month’s KPI report depends on our confidence in last month’s KPI report, and how well the historical numbers match across the two.


Of course, you could be wrong both times; matching numbers aren’t necessarilyrightnumbers. But as far as rough and easily accessible heuristics go, it’s pretty good. And the more iterations that match—if a metric’s historical charts have been consistent for eight quarterly reports in a row—the more trust that it inspires.5


# To trust the output, test the output


So, whenTristan asks, “How do we empower data consumers to assess the credibility of MDS-generated data products?,” that’s my answer: Tell me if what I’m looking at is the same today as it was yesterday.


Don’t tell me that there aren’t any stale pipelines; timely syncs can still sync bad data. Don’t tell me that the tests are passing; even the best analystscan’t come close to anticipatingall of the ways that a “simple” problem can go wrong. Don’t tell me a report is verified, or is owned by someone I trust; so too isGuy Fieri’s Cereal Milk Milkshake with Fireball and Marshmallow Vodka™, and I’d still be skeptical of it if it was a month old. Instead, tell me that the dashboard that currently says we made$3.7 million on the weekend of August 1, 2003said the same thing yesterday, and the day before that, and in September of 2003.6Thatcheckmark—the one that says this number has been consistent for years, that this metric isLindy—is one I’ll trust.


This isn’t to say there isn’t value in checking the inputs; check those too!7But we should recognize that trust is built, and blown up, by the outputs—and specifically, the consistency of those outputs. If we want to build faith in our analytical institutions, we shouldn’t telling people what’s working or broken, or what’s right or wrong; instead, we should tell people what’s changed.


What might we build if that was the goal? A few ideas:


When we define keyentities, track how they evolve. If there’s a table of purchases or customers, let me define which columns should be immutable—purchase date, contract amount, initial customer segment, etc.—and tell me when they’re different today than they were yesterday. Don’t just validate source schemas andrun unit testson dummy data, and assume that the combination will produce the correct calculations on production data. Check the results of those calculations directly, using their earlier values as the test condition.


In BI tools, cache rolling snapshots of key dashboards. For time series, automatically compare the current values on the dashboard with those from a prior few days, and show people when the two have drifted apart. Dashboard consumers are doing this already; we might as well do it for them. Better to proactively tell people when something has gone awry rather than have them find out in the middle of a testy board meeting.8


Sometimes, the problem isn’t that some metric has changed; it’s that someone’s looking at two different metrics without knowing it. They wanted ARR and found bookings; they started with sales volume by state that included sales tax, and ended with a version that excluded it. Here, BI tools could do more to either direct people to or away from certain metrics, using some mechanic like Google’s “Showing results for…” when you misspell something. Keep track of what metrics people often use, and warn them when they’re looking at something that they might confuse with what they usually see.


The point here isn’t that these specific ideas are good; they might be terrible, or impossible to implement.9The point is to reframe the problem around validating outputs instead of inputs. It’s to think about building trust by focusing directly on what undermines that trust—inconsistent and unreliable results. It’s to recognize that, in data, we can think we did everything right, andthe score still may not take care of itself.


# The offset test


How do we know if we’re catching bad outputs? This is my thought experiment:


Suppose that you’ve got a table of customer contracts, sorted by the date the customer signed. Through some inexplicable error, all of the values in the contract amount column got offset by one row.10The contract amount of the first customer was replaced by that of the second customer; the second customer’s contract amount is now is that of the third customer; and so on.


Everythingis now wrong. Every customer contract is incorrect; every revenue metric is broken. It’s an analytical catastrophe; the sort of mistake that costs data teams their jobs, CEOs their reputation, andshareholders $2.2 billion dollars.


Do our systems catch it?


Today, the answer seems to be no. No pipeline is down or delayed. No schemas have changed; no data is invalid. All our unit tests would still pass. No statistical distributions are any different. There are no anomalies or outliers. To today’s stack, this cataclysmic error isn’t an error at all.11


I don’t think we’ll ever trust the modern data stack until we can confidently prevent this error. So long as it’s possible, we’ll perpetually find ourselves double-checking our dashboards and fielding concerns from skeptical stakeholders. Because in data, there are only two possible constants: Consistent metrics or consistent questions. Until we have the former, all we’ll get is the latter.

[1](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-1-127141251)

I wasn’t sure if I had any problems, so I tried to check the CloudWatch logs, and now I know I haveat least one problem.

[2](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-2-127141251)

Or at least,attempttomonetize.

[3](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-3-127141251)

Or at least,talkabout.

[4](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-4-127141251)

Actually—are they? This is a real question. As buzzy as the concept has become, I’ve only ever heard of two formal implementations of data contracts: AtConvey, and atGoCardless. Trace through the links in nearly every post about data contracts, and you’ll wind up on one of these two stories.


Are there a lot more data contracts running in production out there? Have lots of companies built data contracts, but don’t recognize them as such? This isn’t a criticism of data contracts (I have a post in the backlog called “An about-face on data contracts”); I truly can’t tell if these things are nowhere, everywhere, or everywhere but called something else.

[5](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-5-127141251)

You could argue, if you wereconceited blowhard, that there’s actually no such thing as a “right” number. You could say that metrics are constructs; that if we encode ARR to include trial revenue and we all believe ARR should include trial revenue, ARR does, definitionally,include trial revenue; that metrics aren’t a physical truth but a social one; that the consistency of social belief in a metric—i.e., how long it matches its historical self—is the only true measure of its correctness. But let’s leave those arguments toclowns who like to cosplaying as philosophersand assume that metrics can, in fact, be Right or Wrong. The main point still holds: The more consistent a metric is, the more people have likely checked it and thought, “yeah I buy that,” and the more likely it’s Right.

[6](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-6-127141251)

One day, after we finally solve all of this data nonsense, this blog will finally pivot into what it’s wanted to be this whole time: Anthropological examinations of early 2000s culture. Pitbull,obviously, is at the top of that list. ButGiglimight be second.


I mean, just look atthis thing. A $75 million budget that grossed less than a tenth of that. Bennifer, v1. A supporting cast of Al Pacino and Christopher Walken. AnAcademy Award-nominated directorwho straight-up quit directing movies after it came out. (And honestly, atrailerthat doesn’t lookthatbad? It’s(500) Days of Summer,withBoiler RoomBen Affleckinstead of JGL. Which, put that way, sounds kinda intriguing?)

[7](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-7-127141251)

Well, maybe. On metered databases like Snowflake and BigQuery, running tests and observability applications costs money, so these checks aren’t free.

[8](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-8-127141251)

Or so I heard, from, uh, a friend.

[9](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-9-127141251)

In my defense, I came up with them while distracted by a 23-run, 33-hit,walked-off slugfest, ahome run robberyin a national championship game,andovertimein the Stanley Cup Finals.

[10](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-10-127141251)

Some analyst decided to use this table to test theInfinite Hotel Paradox, I guess.

[11](https://benn.substack.com/p/all-i-want-is-to-know-whats-different#footnote-anchor-11-127141251)

Datafold, I think, is the one exception to this. As I understand the product, Datafold would in fact catch this. Shoutout, Datafold.
