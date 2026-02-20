---
title: "What Heartbleed Can Teach The OSS Community About Marketing"
date: 2014-04-09
url: https://www.kalzumeus.com/2014/04/09/what-heartbleed-can-teach-the-oss-community-about-marketing/
slug: what-heartbleed-can-teach-the-oss-community-about-marketing
word_count: 1859
---


If you’re a technologist and you’re not living under a rock, you’ve heard about [Heartbleed](http://www.heartbleed.com), which is a Severity: Apocalyptic bug in the extraordinarily widely deployed OpenSSL software.  Heartbleed lets anyone capable of finding a command line read encryption keys, passwords, and other private data out of affected systems.  If you don’t remember addressing this in the last 48 hours **close this window immediately and get to work**.


Now that we’re past the immediate panic phase, though, I want to share some lessons learned.  Security experts can tell you more than I can about what it means for good C coding practices in high-criticality security libraries.  I want to take a moment to point at the marketing aspects of it: how the knowledge about Heartbleed managed to spread within a day and move, literally, hundreds of thousands of people to remediate the problem.


Heartbleed is much better marketed than typical for the OSS community, principally because it has a name, a logo, and a dedicated web presence.


What’s In A Name


Remember CVE-2013-0156?  Man, those were dark days, right?


Of course you don’t remember CVE-2013-0156.


The security community refers to vulnerabilities by numbers, not names.  This does have some advantages, like precision and the ability to Google them and get meaningful results all of the time, but it makes it very difficult for actual humans to communicate about the issues.


CVE-2013-0156 was the Rails YAML deserialization vulnerability.  “Oh!  I remember that one!”, said the technologists in the room.  Your bosses don’t.  Your bosses / stakeholders / customers / family / etc also cannot immediately understand, on hearing the words “Rails YAML deserialization vulnerability”, that ***large portions of the Internet nearly died in fire***.  After I wrote a [post](https://www.kalzumeus.com/2013/01/31/what-the-rails-security-issue-means-for-your-startup/) about that vulnerability I was told for weeks by frustrated technologists about e.g. VPs nixing remediation efforts due to not understanding how critical it was.  That’s a failure of marketing.


Compare “Heartbleed” to CVE-2014-0160, which is apparently the official classification for the bug.  (I say “apparently” because I _cannot bring myself to care enough _to spend a minute verifying that.)  Crikey, what a great name that is.

- It references the factual underlying technical reality of the vulnerability, which is data leakage during a heartbeat protocol.
- It is very emotionally evocative.  Think of your associations — “my heart bleeds for you”, the Sacred Heart and associated iconography, etc.
- It **sounds serious and/or fatal**.


Geeks sometimes do not like when technical facts are described in emotionally evocative fashion.  I would agree if it were for the purpose of distortion, but “If you use OpenSSL 1.0.1a-f you could be leaking server memory” **actually is serious and/or fatal**, so describing it as such has the benefit of making people seek immediate resolution, **which should be our goal as technologists**.


Unique names (and “Heartbleed” is unique, given that you’d be hard pressed to find any mention of it which predates the vulnerability) are useful for communicating shared concepts between people.  My Twitter stream for the last few days is people sensibly discussing e.g. “Don’t forget, you can be heartbled in a client context”, “How do you fix Heartbleed on Ubuntu?”  “Depends — older versions aren’t vulnerable, newer versions can just apt-get update & upgrade”  “Thanks!”


This is a substantial improvement on conversations I’ve had about previous vulnerabilities, where you often end up discussing, e.g., “the Rails bug.”  Which one?  You know, THE bug.  Wait THE bug or the other bug?  The YAML bug.  Wait wait the YAML bug in the XML handling or the class of bugs caused by YAML deserialization?  Man, would that have been an easier month if we had all been talking about DeserialKiller.


Names which don’t involve arcane trivia like “OpenSSL 1.0.1g” are also easy to communicate with non-technical stakeholders.  If you had a launch yesterday, and you were forced to choose between making the launch date and fixing Heartbleed, you absolutely should have scrubbed the launch.  **We were all racing against for loops and the prize for 2nd place was “Our customers’ security gets horribly abused.”**  To actually scrub the launch, you might need to convince e.g. a manager that despite the company having dropped $100k on a splashy ad campaign, Heartbleed was priority #1.  The image of your lifeblood dripping out was more likely to successfully accomplish that than a CVE number.


## Clear Communication


The Heartbleed announcement should be taught in Technical Writing courses.  It is masterful communication.  Let me quickly excerpt the first three paragraphs:


The Heartbleed Bug is a serious vulnerability in the popular OpenSSL cryptographic software library. This weakness allows stealing the information protected, under normal conditions, by the SSL/TLS encryption used to secure the Internet. SSL/TLS provides communication security and privacy over the Internet for applications such as web, email, instant messaging (IM) and some virtual private networks (VPNs).


The Heartbleed bug allows anyone on the Internet to read the memory of the systems protected by the vulnerable versions of the OpenSSL software. This compromises the secret keys used to identify the service providers and to encrypt the traffic, the names and passwords of the users and the actual content. This allows attackers to eavesdrop on communications, steal data directly from the services and users and to impersonate services and users.


### What leaks in practice?


We have tested some of our own services from attacker’s perspective. We attacked ourselves from outside, without leaving a trace. Without using any privileged information or credentials we were able steal from ourselves the secret keys used for our X.509 certificates, user names and passwords, instant messages, emails and business critical documents and communication.


That is tight, precise, hard-hitting writing, of the sort which we normally associate with journalists rather than cryptographers or software engineers.  It is both technically accurate and yet comprehensible if you are not a technologist.  It doesn’t bury the lede about severity: “popular $MUMBOJUMBO software library” “allows stealing the information protected” on your “web, email, IM, and virtual private networks” “without leaving a trace” including “user names and passwords, instant messages, emails, and business critical documents and communication.”


The website goes on to provide technical details and remediation advice, but you can already tell your boss “I can’t do that today, boss.  We have to respond to heartbleed.com.”  If he spends even 30 seconds glancing at that executive summary he’ll say “Crikey.  Yep, you do.”  I particularly liked the recognition that most remediation of Heartbleed would be done by businesses, which is probably why the writer focused on “business critical documents” rather than the more anodyne “data.”  Data gets weighed by the gigabyte but business critical documents spur immediate action when threatened.


## The Benefits Of A Dedicated Web Presence


I often tell OSS practitioners to use dedicated web presences for projects they consider important, as opposed to dangling them off of (without loss of generality) Github.  Why?


People will generally try to link to something to describe a project / vulnerability / etc, and having an easy and obviously linkable canonical description is both best for clarity and best for your own personal interests as the project/etc creator.  Heartbleed.com is the canonical explanation of Heartbleed, both because people trust $8.95 domain names and because it was first published, came with a design/logo and comprehensive information, and is suitably authoritative in character.


Compare it to the best canonical reference you can find about CVE-2013-0156.  That would be an [archived copy](https://groups.google.com/forum/#!topic/rubyonrails-security/61bkgvnSGTQ) of a plain-text email, hosted on Google Groups.  It isn’t particularly attention grabbing, doesn’t really scream “citable” to either a technical or non-technical audience, and is optimized for a fairly narrow strand of practitioners rather than the much larger audience of people who should have cared about CVE-2013-0156.


## Visual Identity Is Important


The Heartbleed logo is probably one of the highest ROI uses of ~$200 in the history of software security.  (I don’t actually know whether they got it done for $200, but that is about what I paid the last time I had a logo done for an OSS project.)


Heartbleed Logo


I saw some kvetching on Twitter to the effect that the logo designer heard about Heartbleed before the distribution maintainers at e.g. Ubuntu and RedHat did.  This kvetching is wrongheaded, because the logo designer only needed the instruction “We have a project named Heartbleed.  Come up with a logo which says *serious danger*.”  rather than “Apropos of nothing, mostly non-technical logo designer, the heartbeat protocol in OpenSSL 1.0.1a through 1.0.1f has been fubared for 2 years now.  Don’t tell the Ubuntu guys though, we’re trying to keep it a secret!”


(I am, for what it is worth, absolutely agnostic on who should have preferential access to information of upcoming vulnerabilities with regards to a particular project.  This strikes me as something which should be bought from maintainers/security researchers if you care about it, but I’m only weakly committed to that.)


Why spend the extra money for a logo?  Because it suggests professionalism and dedicated effort, because it will be used exhaustively in media coverage of the vulnerability, because it further deepens the branding association of the vulnerability, the name, the logo, and the canonical web presence, and because it also suggests danger.  Is it the best logo in the history?  No.  This one won’t win design awards.  But it certainly does the job with aplomb.


OSS projects often don’t have logos or, ahem, do not devote to them the level of technical excellence that they devote to their products.  I will refrain from pulling in examples here to make my point.


## Marketing Helps Accomplish Legitimate Goals


There exists a huge cultural undercurrent in the OSS community which suggests that marketing is something that vaguely disreputable Other People do which is opposed to all that is Good And Right With The World, like say open source software.  Marketing is just a tool, and it can be used in the cause of truth and justice, too.


As technologists, the Heartbleed vulnerability posed an instant coordination problem.  We literally had to convince hundreds of thousands of people to take action *immediately.*  The consequences for not taking action immediately were going to be disastrous.  They were not limited to “mere” violations of computer security, but would have had dire economic and social consequences in the *real world*.  Livelihoods (and, likely, lives) were at stake.


Given the importance of this, we owe the world as responsible professionals to not just produce the engineering artifacts which will correct the problem, but to advocate for their immediate adoption *successfully*.  If we get an A for Good Effort but do not actually achieve adoption because we stick to our usual “Put up an obtuse notice on a server in the middle of nowhere” game plan, *the adversaries win*.  The engineering reality of their compromises cannot be thwarted by effort or the feeling of self-righteousness we get by not getting our hands dirty with marketing, it can only be thwarted by successfully patched systems.


This makes marketing an engineering discipline.  We have to get good at it, or we will fail ourselves, our stakeholders, our community, and the wider world.


More OSS marketing like Heartbleed, please.
