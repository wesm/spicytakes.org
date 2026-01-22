---
title: "Money in politics: the BFF project"
date: 2013-07-16
url: https://mathbabe.org/2013/07/16/money-in-politics-the-bff-project/
word_count: 896
---


*This is a guest post by [Peter Darche](http://peterdarche.com/), an engineer at [DataKind ](http://datakind.org/)and recent graduate of NYU’s ITP program.  At ITP he focused primarily on using personal data to improve personal social and environmental impact.  Prior to graduate school he taught in NYC public schools with Teach for America and Uncommon Schools.*


We all ‘know’ that money influences the way congressmen and women legislate; at least we certainly believe it does.  According to poll conducted by law professor Larry Lessig for his book Republic Lost, 75% of respondents (Republican and Democrat) said that ‘money buys results in Congress.’


And we have good reason to believe so. With [astronomical sums](http://money.cnn.com/2012/11/05/news/economy/campaign-finance/index.html) of campaign money flowing into the system and [costly](http://en.wikipedia.org/wiki/Medicare_Part_D#Criticisms), [public-welfare reducing](http://en.wikipedia.org/wiki/Copyright_Term_Extension_Act#Opposition) legislation coming out, it’s the obvious explanation.


But what does that explanation really tell us? Yes, a congresswoman’s receiving millions dollars from an industry then voting with that industry’s interests reeks of corruption. But, when that industry is responsible for 80% of her constituents’ jobs the causation becomes much less clear and the explanation much less informative.


The real devil is in the details. It is in the ways that money has shaped her legislative worldview over time and in the small, particular actions that tilt her policy one way rather than another.


In the past finding these many and subtle ways would have taken a herculean effort: untold hours collecting campaign contributions, voting records, speeches, and so on. Today however, due to the efforts of organizations like the [Sunlight Foundation](http://sunlightfoundation.com/) and [Center for Responsive Politics](http://opensecrets.org), this information is online and programmatically accessible; you can write a few lines of code and have a computer gather it all for you.


The last few months [Cathy O’Neil](cathyoneil.org), Lee Drutman (a Senior Fellow at the Sunlight Foundation), myself and others have been working on a project that leverages these data sources to attempt to unearth some of these particular facts. By connecting all the avenues by which influence is exerted on the legislative process to the actions taken by legislators, we’re hoping to find some of the detailed ways money changes behavior over time.


The ideas is this: first, find and aggregate what data exists related to the ways influence can be exerted on the legislative process (data on campaign contributions, lobbying contributions, etc), then find data that might track influence manifesting itself in the legislative process (bill sponsorships, co-sponsorships, speeches, votes, committee memberships, etc). Finally, connect the interest group or industry behind the influence to the policies and see how they change over time.


One immediate and attainable goal for this project, for example, is to create an affinity score between legislators and industries, or in other words a metric that would indicate the extent to which a given legislator is influenced by and acts in the interest of a given industry.


So far most of our efforts have focused on finding, collecting, and connecting the records of influence and legislative behavior. We’ve pulled in lobbying and campaign contribution data, as well as sponsored legislation, co-sponsored legislation, speeches and votes. We’ve connected the instances of influence to legislative actions for a given legislator and visualized it on a timeline showing the entirety of a legislator’s career.


Here’s an example of how one might use the timeline. The example below is of Nancy Pelosi’s career. Each green circle represents a campaign contribution she received, and is grouped within a larger circle by the month it was recorded by the FEC. Above are colored rectangles representing legislative actions she took during the time-period in focus (indigo are votes, orange speeches, red co-sponsored bills, blue sponsored bills). Some of the green circles are highlighted because the events have been filtered for connection to health professionals.


Changing the filter to Health Services/HMOs, we see different contributions coming from that industry as well as a co-sponsored bill related to that industry.


Mousing over the bill indicates its a proposal to amend the Social Security act to provide Medicaid coverage to low-income individuals with HIV. Further, looking around at speeches, one can see a relevant speech about the children’s health insurance. Clicking on the speech reveals the text.


By combining data about various events, and allowing users to filter and dive into them, we’re hoping to leverage our natural pattern-seeking capabilities to find specific hypotheses to test. Once an interesting pattern has been found, the tool would allow one to download the data and conduct analyses.


Again, It’s just start, and the timeline and other project related code are internal prototypes created to start seeing some of the connections. We wanted to open it up to you all though to see what you all think and get some feedback. So, with it’s pre-alphaness in mind, what do you think about the project generally and the timeline specifically?  What works well – helps you gain insights or generate hypotheses about the connection between money and politics – and what other functionality would you like to see?


The demo version be found [here](http://pdarche.github.io) with data for the following legislators:

- Nancy Pelosi
- John Boehner
- Cathy McMorris Rodgers
- John Boehner
- Eric Cantor
- James Lankford
- John Cornyn
- Nancy Pelosi
- James Clyburn
- Kevin McCarthy
- Steny Hoyer


Note: when the timeline is revealed, click and drag over content at the bottom of the timeline to reveal the focus events.
