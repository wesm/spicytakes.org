---
title: "'Good Enough' Data Models"
subtitle: "Joe's Nerdy Rants #34 - Weekend reads and other stuff"
date: 2024-03-09T16:46:46+00:00
url: https://joereis.substack.com/p/good-enough-data-models
slug: good-enough-data-models
word_count: 1962
---


![Visualize a scale in perfect balance, with one side labeled "Good Enough" containing elements like check marks, simplified diagrams, and a casual, content figure. The other side, labeled "Perfect", is filled with detailed drawings, a trophy, and a figure meticulously checking every detail. Both sides are equally weighted, symbolizing the balance between the practicality of "good enough" and the idealism of striving for perfection. The background should be minimalist to emphasize the scale and the contrasting concepts on each side.](https://substackcdn.com/image/fetch/$s_!AZcD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6718e8df-b165-46d2-85b5-5edaffe36691_1024x1024.webp)


The other daySol Rashidi1and I were having lunch when I mentioned that I feel like European data modeling practices were “good” compared with those in America. I base this on my personal experiences working and chatting with European data modelers (often working at massive private European conglomerates), who are generally more thorough, strict, and detailed in their data modeling approaches than their American peers. By contrast, American data modeling practices seem typically far less rigid and formal. Though a bit of a generalization, I’ve seen enough companies and spoken with enough practitioners to say this is a pretty accurate depiction of data modeling practices on both sides of the Atlantic.


Sol seemed taken aback by my use of the word “good,” which is very subjective. She felt it unfair to compare European and American companies, where the former often move more slowly and deliberately than the latter. It's not always necessary for a data model to be flawless, as long as it facilitates decisions and actions helping move the business in the right direction. There's more opportunity to develop a cohesive and precise enterprise data model in a slower or static environment because this type of work requires more time and patience. In faster-moving business environments, business models and mandates change much more quickly, and it’s often the case that the data model iterates more quickly, often at the expense of robustness or precision.


Data modeling aims to represent a business's rules, vocabulary, and workflows as precisely as possible, and there are many strict (almost dogmatic) data modeling methodologies and approaches. However, this aim is challenging when the underlying business model constantly evolves. Sol emphasized that even if American data models might not meet European standards of perfection, they can still be considered "good" if they are fit for their purpose and satisfy the needs of the business. Precision is traded off for “good enough” and practicality for the situation. Flexibility and agility are crucial in such scenarios. Practitioners often get caught up in aiming for technical perfection and precision. While perfection can benefit a technician’s sense of craftsmanship and pride, her comment highlights that executives frequently prioritize practicality over perfection. And since executives are in charge of the direction and budget of data initiatives, practitioners should read the room and understand what’s expected of them on the spectrum of perfection or practicality.


I’m not implying that data modelers shouldn’t strive for the best data models possible. Data models should be the best for the situation at hand, focusing on outcomes over rigid processes. On one extreme, sloppy data models providing wrong or misleading data leading to detrimental decisions and actions would be professional malpractice. On another extreme, I’ve heard people (especially in Europe) strive for things like 6th normal form and the perfect Data Vault or Kimball model, to the point of claiming anything less is garbage. An ideal goal might be a data model that anticipates every question that might be asked and the data precisely conforms to the contours of the business. For the craftsman data modeler, there’s always an ideal of the perfect data model. Of course the ideal data model would be fantastic to have, and if you have a lot of time on your hands and the ability to create this ideal data model, go for it.


In a rapidly evolving business landscape, achieving perfection in data models and practices can be challenging. Having the luxury of working in a static environment doesn’t exist these days. The world moves too fast. Executives often prioritize practicality over perfection, as the business environment demands quick adaptations. While striving for an ideal state is important, it's essential to recognize that "good" is often context-dependent. Effective data models should address the immediate situation while anticipating potential future changes.


Listen to the audio clip above on this topic, which is also my5-Minute Friday on Spotify.


Also, if you haven’t done so, please sign up forPractical Data Modeling. Lots of great discussions on data modeling, and this is also where I’ll be releasing early drafts of chapters for my new data modeling book. Thanks!


---


# Cool Weekend Reads


Here are some cool things I read this week. Enjoy!


### Tech, AI, Data


Twenty Years Is Nothing (De Programmatica Ipsum)


“These days, we are used tocloningan entire project on our computer, after which we can safely plug it off the network and continue writing software in a completely disconnected way. This simple paradigm was utterly and completely unthinkable 20 years ago. And guess what: your local repository also contains the full history of every single change ever made to your project. This was a feature that, naturally, client-server systems could never provide (spoiler alert: the server had the full history, while clients had only theHEAD, so to speak).”


“The question is simple now: what comes after Git? At this point, it is probably impossible to challenge the immense popularity of Git. I say “probably” because in our industry, it is impossible to predict the future.”


This is a really good review of the history of source control over the last twenty years, and speculation about what comes after Git. Despite its flaws, I suspect Git will be around long after many of us retire from the industry.


Why pandas feels clunky when coming from R (Rasmus Baath)


I actually agree with this, being fluent in both Python/Pandas and R. If I need to do stats or pure data work, R is still my go-to “hand calculator.” The experience is much better because it’s purpose built for dataframe work.


Mamba: The Hard Way (Sasha Rush)


This is a really good read if you’re interested in theMamba paper, but either want another explanation (the paper itself might be cryptic to some).


AWS follows Google in announcing unrestricted free data transfers to other cloud providers (Techcrunch)


Good move by AWS. Hopefully Azure is next.


Also, this is an interesting tidbit, “Another issue identified by the U.K.’s Competition and Markets Authority (CMA) was interoperability, concerning areas where cloud companies design their products to not play nicely with rival services. Removing fees doesn’t necessarily remove “technical barriers to switching,” as the CMA calls it — so there could be some regulatory headwinds still to come.”


I’ll let you fill in the blanks on what that might mean…


### Biz, Culture, Other Randomness


Aggregator’s AI Risk (Stratechery)


“Remember that Aggregator power comes from controlling demand, and that their economic model depends on demand being universal; the ability to control demand is a function of providing a discovery mechanism for the abundance of supply. What I now appreciate, though, is that the abundance of supply also provided political cover for the Aggregators: sure, Google employees may have been distraught that Trump won, but Google still gave you results you were looking for. Facebook may have had designs on global community, but it still connected you with the people you cared about.


Generative AI flips this paradigm on its head: suddenly, there isn’t an abundance of supply, at least from the perspective of the end users; there is simply one answer. To put it another way, AI is the anti-printing press: it collapses all published knowledge to that single answer, and it is impossible for that single answer to make everyone happy.”


Printing press → Internet → AI. What happens next?


How AI Is Already Transforming the News Business (Politico)


Really good interview with Felix Simon, who wrote awonderful (and pretty objective) paperon AI’s impact on journalism and news. Long story short, it’s gonna be a mixed bag…


AI-first Service Businesses (Point Nine Land)


“In contrast to 2017, foundation models might perform well enough to buildfull-stack, AI-first service businesses that will ultimately look like software businesses.


What does that mean? By constraining the problem or focusing on a niche, a new company can leverage foundation models and industry-specific data to rebuild a service business from the ground up that issoautomated that it becomes scalable. Its P&L will ultimately look more like one of a software than a service business.”


Your "TAM" is Why I Have Trust Issues (Mostly Metrics)


“Here are the most common problems with TAM analyses:

1. Lack of credibility
2. Doing the big number thing
3. Taking credit for someone else’s TAM”


# New Content, Events, and Upcoming Stuff


## Monday Morning Data Chat


#### Coming up…


Ethan Aaron, and more!


#### In case you missed it…


Jean-Georges Perrin - Data Mesh, Data Contracts, Modern Data Engineering Standards, Bitol, and More (Spotify,YouTube)


Joe Reis & Matt Housley - The Demise of the Modern Data Stack & Listener Q&A (Spotify,YouTube)


Scott Taylor - Explaining Value to the Business (Spotify,YouTube)


Michel Tricot - AI's Impact on Traditional Data Practices and More! (Spotify,YouTube)


Sol Rashidi - Getting Business Value From Data, the CXO Playbook (Spotify,YouTube). Very popular episode with nearly everyone. - PINNED HERE.


## The Joe Reis Show


#### Coming up…


Sadie St. Lawrence, Jess Haberman, and many more!


#### This week…


5-Minute Friday “Good Enough” Data Models - (Spotify)


Christian Bourdeau - The Data Hiring Landscape (Spotify)


Zach Zeus - Trust Architecture, ESG, and More (Spotify)


#### In case you missed it…


5-Minute Friday - Types of Debt (Spotify)


Christophe Blefari - Why Teaching Data Engineering is Hard (Spotify)


Annie Nelson - How to Become a Data Analyst (Spotify)


5-Minute Friday - Gordon Wong and I are Dropped into a Failed Data Project  (Spotify)


Bill Inmon - History Lessons of the Data Industry. This is a real treat and a very rare conversation with the godfather himself (Spotify) - PINNED HERE.


## Events


Data Night Book Club (Paris ) - March 20.Register here


Onepoint (Paris) - March 21.Register here


J On the Beach (Malaga, Spain) - May 6-10.Register here


GenAI Conference May 20-22 (London) - May, TBA


DAMA Days (Vancouver, BC) - June, TBA


(Taking the Summer off)


DataEngBytes (Australia) - Late September/Early October, TBA


Dubai - Fall, TBA


Europe - Fall, TBA


Asia - Fall, TBA


Would you like me to speak at your event?Submit a speaking requesthere.


# Thanks! If you want to help out…


Thanks for supporting my content. If you aren’t a subscriber, please consider subscribing to this Substack.


You can also find me here:


Monday Morning Data Chat (YouTube/Spotifyand wherever you get your podcasts). Matt Housely and I interview the top people in the field. Live and unscripted. Zero shilling tolerated.


The Joe Reis Show (Spotifyand wherever you get your podcasts). My other show. I interview guests, and it’s unscripted with no shilling.


Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.


Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.


Be sure to leave a lovely review if you like the content.


Thanks! - Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.

[1](https://joereis.substack.com/p/good-enough-data-models#footnote-anchor-1-142200431)

Sol and I often have thoughtful (and sometimes heated) debates about data. We come from two different worlds. She’s a world-class data and business executive, and I’m a hardcore veteran practitioner and educator. Our worlds intersect, but almost orthogonally. We come at data from different perspectives and constantly learn something from each other.
