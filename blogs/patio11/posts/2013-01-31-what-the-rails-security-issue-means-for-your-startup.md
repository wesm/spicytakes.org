---
title: "What The Rails Security Issue Means For Your Startup"
date: 2013-01-31
url: https://www.kalzumeus.com/2013/01/31/what-the-rails-security-issue-means-for-your-startup/
slug: what-the-rails-security-issue-means-for-your-startup
word_count: 4522
---


January has been a very bad month for Ruby on Rails developers, with two high-severity security bugs permitting remote code execution found in the framework and a separate-but-related compromise on rubygems.org, a community resource which virtually all Ruby on Rails developers sit downstream of.  Many startups use Ruby on Rails.  Other startups don’t but, like the Rails community, may one day find themselves asking What Do We Do When Apocalyptically Bad Things Happen On Our Framework of Choice?  I thought I’d explain that for the general community.


**Nota bene**: I’m not a professional security researcher.  Mostly, I sell software.  In the course of doing that, I (very occasionally) do original security research.  I did no significant amount for these bugs, aside from mitigating them for my own applications.  I am currently engaged in a Ruby on Rails security safari, and anticipate publishing the results of that in February, after responsible disclosure to the relevant security teams.  If you don’t know enough to know whether I’m trustworthy with regards to generic advice, pay someone you trust to get advice on this.


**Don’t skip this post** because you’re not a Rails developer.  If you’re reading this blog, this matters to you.


## Background: What Has Been Happening in Rails-land?


Ruby on Rails recently released two sets of security patches (announcements [here](https://groups.google.com/forum/?fromgroups=#!topic/rubyonrails-security/61bkgvnSGTQ) and [here](https://groups.google.com/forum/?fromgroups=#!topic/rubyonrails-security/1h2DR63ViGo)), in response to related vulnerabilities discovered in the frameworks.


**How bad were those bugs?** Severity: Apocalyptic.  They permitted attackers to execute arbitrary code on virtually ever Ruby on Rails application, without requiring that the application do anything to enable the attack other than “be hooked up to the Internet.”


**What does “execute arbitrary code” mean?  **Literally, it means that the attacker can choose to have your server execute any code they can dream up.  In practice, it means that you lose the server that the code is executing on.  Any further access to that server or applications on should be assumed to be compromised.


**What went wrong?  **This has been covered in more detail by security researchers, in posts such as [here](http://ronin-ruby.github.com/blog/2013/01/09/rails-pocs.html) and [here](http://ronin-ruby.github.com/blog/2013/01/28/new-rails-poc.html).  A brief description: Ruby on Rails makes extensive use of a serialization format called [YAML](http://www.yaml.org/YAML_for_ruby.html), most commonly (you might think) for reading e.g. configuration files on the server.  The core insight behind the recent spat of Rails issues is that **YAML deserialization is extraordinarily dangerous**.  YAML has a documented and “obvious” feature to deserialize into arbitrary objects.   Security researchers became aware in late December that just initializing well-crafted objects from well-chosen classes can cause arbitrary code to be executed, without requiring any particular cooperation from the victim application.  Since then, the **bug hunt has been on**: security researchers have been actively finding lots of ways in the Ruby on Rails code base, and in related code bases, to cause the application to deserialize YAML which is in some way under the control of the attacker.


So far this has included:

- Rails, for programmer convenience, used YAML to implement JSON deserialization.  JSON is designed to get into Rails quite easily indeed — just POST it at the server, wham, YAML.load(attacker_data) happened.  (The actual mechanics of achieving that were more complicated, but that’s the practical upshot.)
- Rails allows XML documents to include YAML attributes.  That decision has caused a bit of head scratching, since it seems like a curious choice for most programmers in the community, but be that as it may this allowed posting XML at Rails apps to be trivially exploited.
- Rubygems used YAML to hold metadata about each gem submitted to it.  An attacker was able to create a malicious gem, cause the Rubygems web application to evaluate the metadata contained in it, and thereby compromise the Rubygems server infrastructure.
- **February will see more compromises, with my certainty of this prediction approaching my certainty that the sun will rise tomorrow.**  There exist many, many other code paths in Rails to get to YAML.load().  Some of them will be found to be amenable to attackers, either (worst case) for all or substantially all Rails applications or (still bad case) to Rails applications whose application logic involuntarily cooperates with the attack.  (i.e. In the worst case, attackers root every unpatched Rails app on the Internet.  In the best case, attackers only root some apps and they often have to have an expert do a modicum of marginal work to do so.)


**Ruby on Rails security sucks lolz amirite?** No.  Well, no to the nuance.  Software security does, in general, suck.  Virtually every production system has security bugs in it.  When you bring pen testers in to audit your app, to a first approximation, your app will lose.  While Ruby on Rails cherishes its Cool-Kid-Not-Lame-Enterprise-Consultingware image, software which is absolutely Big Freaking Enterprise consultingware, like say the J2EE framework or Spring, have seen similar vulnerabilities in the past.  The recent bugs were, contrary to some reporting, not particularly trivial to spot.  They’re being found at breakneck pace right now precisely because they required substantial new security technology to actually exploit, and that new technology has unlocked an exciting new frontier in vulnerability research.  It sucks for users of Rails that Rails is currently on the bleeding edge — believe me, after having lost 3 consecutive nights to patching my own applications, I know — but it would suck much, much worse if the Bad Guys had found these first and just proceeded to remote-own every Rails app on the Internet.  **That is, by the way, an achievable scenario**.


**Was anyone actually compromised?**  Yes.  The first reported compromise of a production system was in an industry which hit the trifecta of amateurs-at-the-helm, seedy-industry-by-nature, and under-constant-attack.  It is imperative that you understand that **all Rails applications will eventually be targeted** by this and similar attacks, and **any** vulnerable applications will be owned, **regardless** of absence of these risk factors.


**Will anyone else be compromised?  **Yes.  Thousands upon thousands of Ruby on Rails applications will be compromised using these vulnerabilities and their spiritual descendants, and this will happen for years.

- Many Rails developers have not reacted to this news with the alacrity they should have.  (See next question.)  These applications **may be compromised already**.
- There are many Rails applications which were created years ago, which are not under active development any more, for whom no-one is responsible for applying security patches.  Any of these applications which are publicly routable on the Internet **will be compromised**.
- There are many Rails applications which are installed by end users, some of whom do not have security expertise.  For example, Redmine — an open source developer productivity tool — is commonly installed at individual companies.  Every publicly accessible Redmine instance which is not patched **will be compromised**.
- Ruby on Rails lacks a CMS with the mindshare of, say, WordPress, which is good, because every unpatched Ruby on Rails CMS delivered to a non-technical company to serve as their website or backend to their mobile application **will be compromised**.
- There are many developers who are not presently active on a Ruby on Rails project who nonetheless have a vulnerable Rails application running on localhost:3000.  If they do, eventually, their local machine **will be compromised**. (Any page on the Internet which serves Javascript can, currently, root your Macbook if it is running an out-of-date Rails on it. No, it does not matter that the Internet can’t connect to your localhost:3000, because your browser can, and your browser will follow the attacker’s instructions to do so. It will probably be possible to eventually do this with an IMG tag, which means any webpage that can contain a user-supplied cat photo could ALSO contain a user-supplied remote code execution.)
- Many companies — including ones which do not even consider themselves Ruby on Rails shops — nonetheless have a skunkworks project running somewhere.  For example, they might have a developer who coded a quick one-off analytics app, which is accessible outside the firewall so that sysadmins could check server loads from home.  If the app is on the public Internet, it **will be compromised**.
- Many Ruby on Rails shops have good development practices and no longer have the “monorail” anti-pattern, where everything their company does is in one gigantic Rails app.  They have already patched most of their main apps, but they missed one.  Maybe it is the customer support portal at admin.example.com.  Maybe it is a publicly accessible staging server at EC2 spun up by a developer who has since left the company and not shut down because, hey, $20 a month.  Maybe it is a 20% project by a junior engineer which he has on the back burner for the moment.  It doesn’t matter why this app was forgotten: if it is publicly accessible, it **will be compromised.**


**What was the proper way to react to these patches?  **Patch immediately, install a workaround immediately, or pull the plug on your application.  (“Pull the plug” means disconnect it from the Internet or shutdown the server while you get a mitigation plan into place.)  You should have distinct memories of you or someone under your employ having at least two separate incidents in the last four weeks in which they dropped everything they were doing and immediately took action to resolve these problems.  **Immediately means exactly that**: right now, not during the next schedule code spring, not tomorrow, not in an hour.


I was up at 3 AM Japan time applying these patches, twice.  If the next patch drops at 3 AM your local time, someone should be applying it *immediately*.  Computers can count to big numbers very quickly indeed.  A six hour window between a patch dropping and the start of business the next day is more than enough for an automated scanner running on a botnet to have tried compromising substantially every Rails app on the Internet.  (Do you disagree?  You are overestimating how hard it would be to find your application.)


**Aren’t you exaggerating?  Our application isn’t particularly high risk!  We aren’t high-profile, it doesn’t have obvious monetary return for exploiting it, etc etc. **Good thing you aren’t really saying that, but you might be at an Internet cafe next to an engineer who has poor reading comprehension, so help me explain this to him: *nobody needs to care about your application to compromise it using these vulnerabilities*. They can be exploited in a totally automated manner over the open Internet, requiring zero knowledge of e.g. what version of Ruby you are running, what version of Rails you are running, what your URL structure looks like, etc.  (Somebody suggested “How would you determine which servers were running Ruby on Rails?”  Answer: It’s absolutely trivial to detect Rails applications in a scalable fashion, but why bother?  **Fire four HTTP requests at every server on the Internet: if the server is added to your botnet, it was running a vulnerable version of Ruby on Rails.**)


**Aren’t you exaggerating? Clearly this would take a lot of specialized expertise to exploit!** Yep… the first time. Now that people know how the exploitation is done, however, you could do it by just copy/pasting one of the proof-of-concept scripts or b) running a browser bookmarklet. (I am not passing out that browser bookmarklet, because I think that would inevitably lead to mischief, but just know that you’re rootable in a click if you didn’t take action on this. And, by the way, have been for three weeks or so now.)


## We’re A Startup.  What Happens If We Lose A Server?


**If you lose one server, you will lose every server**, with very high confidence.  If, for example, you are a Python-using shop which had a Redmine instance running around with no code on it, and you lose that Redmine server, you can expect a skilled attacker to then pivot from that privileged location within your network to start compromising other servers on your network.  At this point, you need to have done absolutely everything right to make it impossible for that skilled attacker to prevail, and you almost certainly have not.  (Compelling evidence that you’re not as good as you think you are: you already had one vulnerable application which could be compromised over the open Internet.  To a certain philosophy, that isn’t your fault, but the attacker gets root regardless of whose fault it is.)


The actual steps a pen-tester would take to root your other boxes are pretty academic after they have one.  (For example, you can start probing other machines on the network for vulnerable services, use credentials found on your compromised machine to suborn other machines, take over routing hardware using vulnerable administration panels and then start intercepting all network traffic, etc etc.)  Just take it as a given, you will lose.  Companies much larger and smarter than you lose everything when this happens, essentially every time it happens.


## We’re A Startup.  What Happens If We Lose Every Server?


A short preview of coming attractions:

- You will lose the next several weeks out of your schedule dealing with this issue.
- You will have to take down all of your applications and rebuild all your servers from scratch.
- You can assume the attacker now has a copy of your source code, all credentials you have, all your databases, and all information you had like e.g. log files.
- Do you take credit cards?  Were you taking credit cards through an exploited application?  You now have a PCI-reportable data breach.
- Your local jurisdiction may have legal requirements that you notify the people whose data just got exposed.
- You now have a public relations nightmare on your hand.
- In addition to compromising any customer data you possessed, you have made it possible for diligent attackers to compromise those customers elsewhere.  The most trivial example is, if you did not implement password storage correctly, you have just handed the attackers a list of email addresses and associated passwords which they can now re-use on higher value targets like e.g. bank accounts or Gmail, because many users re-use their passwords everywhere.  (You use bcrypt?  Wonderful.  Did  the attackers turn it off when they rooted all your applications?  Can you conveniently check that, knowing that you cannot trust the contents of any logs on those compromised servers?  No?  OK, so instead of losing all the passwords, we can upper bound exposure at only all users who logged in since the attack started.  That’s an improvement… sort of.)


Basically, it’s Very Bad, but not the end of the world.  You’ll probably need expert help to get through it, like you would need if e.g. you got sued.  Unfortunately, lawsuits generally give you weeks of notice and progress slowly, but security vulnerabilities often give you negative several hours notice and get worse for every minute left unchecked.


## We’re A Startup.  We Don’t Use Ruby on Rails So We’re Totally Cool, Right?


Can you enumerate every account on the Internet where you have a password and also every service consumed by your business?  Go ahead, take as long as you need: it is very important that you don’t miss one.


OK, let’s start with the obvious: Look for analytics providers and other folks on that list who have instructed you to embed JS on your website.  If I do this exercise, I come up with at least three results here.  Do any of them use Ruby on Rails?  (Are you sure?  Remember, if they have at least one Rails app on their network…)  Great.  If they didn’t patch in a timely manner, you should assume that Javascript you’re embedding on your website is in the hands of the enemy.  It is now a cross-site scripting vulnerability against every page it is embedded on.  Do you embed it on e.g. log in pages or anywhere your admins expose their own all-powerful admin cookies?  Boo, now the enemy has your password / cookies / etc.


Alright, let’s move down the line: Look for anybody who implements OAuth/Facebook Connect/etc.  Do any of them use Ruby on Rails?  _Are you sure?  _If they haven’t patched, you’ve handed the union of all privileges over the linked accounts to the attackers.


Alright, let’s move down the line: Consider everybody who has a copy of a password which you re-use elsewhere.  (You shouldn’t be re-using passwords, or variants of passwords, but I ignored that advice for years so I’m betting a lot of you did, too.  Maybe not you, specifically, but you know that chap in marketing who is great with people but thinks MSWord is complicated?  Consider whether he has access to anything sensitive in your company.  He does?  Well, sucks to be you then, but good on your for password security.)  Do any of them use Ruby on Rails?  _Are you sure?  _Did they use bcrypt/scrypt/etc to properly secure passwords at rest, and did they patch these vulnerabilities fast enough to prevent attackers from pulling them off of the wire?  _Are you sure?  _If you’re not sure of all of these things, consider every password compromised and take action appropriately.


One of my friends who is an actual security researcher has deleted all of his accounts on Internet services which he knows to use Ruby on Rails.  That’s not an insane measure.  (It might even be inadequate, because all the folks who are compromised are probably going to lose their database backups as well.  Well, if they have database backups.)


**These are just a sample of ways in which these vulnerabilities can ruin your day.  They are very much not an exhaustive list.**  If you believe in karma or capricious supernatural agencies which have an active interest in balancing accounts, chortling about Ruby on Rails developers suffering at the moment would be about as well-advised as a classical Roman cursing the gods during a thunderstorm while tapdancing naked in the pool on top of a temple consecrated to Zeus while holding nothing but a bronze rod used for making obscene gestures towards the heavens.  I am putting this HTML comment here so that when a LessWrong reader says "Aha, he is clearly not intelligent enough to understand that a rationalist would not be persuaded by that argument because believing in a lightning god doesn't make lightning gods more real and, btw, Bayes theorem is awesome.", I can mention that in this instance it is more of a literary device.  By the way, if you're reading this comment because I told you to, I recommend a Bayesian update on your belief that either deism or, for that matter, use of frequentist statistics suggests lack of intelligence relative to your community.


# Somebody Dropped A 0-Day On Rubygems. What If It Happens To Me?


Yes, that certainly sucks royally.  Rubygems wasn’t even exploited using the patched Rails vulnerabilities — an attacker just learned something which worked (again, we’re on the leading, bleeding edge of security research here), applied it in a novel fashion, and compromised the Rubygems application.  As of me writing this it looks like we avoided the Ruby-ecosystem-wide apocalypse that would have happened if they had started backdooring gems, but let’s just focus on the immediate fallout: their system got compromised.  What if one of yours did, like that?


**The first step is a preventative inoculation**: If you run an application on the Internet, you should *today* establish a security contact page.  It only needs to include two things: a working, monitored email address and a PGP key.  Bonus points for giving some sort of public recognition to people who report security vulnerabilities to you in a responsible matter.  This helps to co-opt some security researchers so that they e.g. get in touch with you about the problem prior to just going ahead an exploiting it.  Software security has a curious system of social norms, where scalp collecting both builds both karma and pseudo-currency.  It’s bizarre, but just take this on faith: having a security page with a working email gives you a certain amount of We Should Avoid #’#(ing Their #()#% Up Without Asking First street cred.  (Naturally, like any social norm, that is a preventative measure rather than a panacea.  However, given that it is a well-understood norm, it gives you a bit of an edge in the PR battle should someone decide to just drop a 0-day on you.)


Good security pages to pattern after: [37signals](http://37signals.com/security) (I particularly like how this page works for responsible disclosure while, in a dual-audience fashion, also doubles as being great marketing copy), [Twilio](https://www.twilio.com/docs/security/disclosure), [Heroku](https://policy.heroku.com/security) (again, dual audience), etc.


**Have a plan for responding to security incidents.** I call mine the Big Red Button. Thomas, a security consultant friend of mine, accurately observed that these probably caused the first Big Red Button events that many folks in the Rails community have ever had to deal with. We should learn from our experiences here.


For example: I pushed the Big Red Button at 3 AM in the morning, twice this month, to apply critical security patches and work-arounds.


So did I do a great job of addressing this problem? No, I did a pretty effing atrocious job of addressing this problem. Specifically, I have two old-as-the-hills Rails apps running on 2.3.X at the moment. Waaaaay back in 2010, Mongrel and Rails had a bit of a [compatibility issue](https://rails.lighthouseapp.com/projects/8994/tickets/4690#ticket-4690-34), and I solved it via a [monkeypatch](https://gist.github.com/471663). The monkeypatch relied on a hardcoded version number, which I have been hand-incrementing every time I update Rails. It’s literally on the redeploy checklist, next to a note “TODO: This is stupid and should be fixed when I get a moment.”


I did three Rails app upgrades locally, three test suite runs, and three sets of smoke tests when applying one of these patches. The one in the middle happened to be Appointment Reminder, which is an application that has to be up during the US workday. Unfortunately, because I was exhausted while following my deployment and smoke test checklists, I a) forgot to bump the version number in that monkeypatch and b) did not follow the part of the smoke test which would have clued me on to “This is going to cause log-ins to fail on some browsers.” That resulted in some breaking downtime for some customers during the US workday, and me having to send an apology to all customers. That sucked horribly.


I have now fixed my monkeypatch to not require hard-coding the Rails version, simplified some of my deploy procedures, and am working in the next several months on beefing up my testing suite. Also, lesson learned about resolving “TODO: This is stupid” when it would take 5 minutes to do rather than having it blow up in my face.


There, that’s an experience I went through. Now you know the punchline, so hopefully you don’t have to go through it as well.


Similarly, we can observe:

- We need an updated list of all applications running on our servers, so that we know when a problem with a technology stack affects them, even though this sounds like a boring Big Freaking Enterprise IT Department requirement. (And *gulp* their dependencies.)
- For each tech stack we support, we need at least one expert following the primary source for security news for that tech stack.
- We need whomever is responsible for product development and/or ops to, effectively, carry a pager for drop-everything-and-do-it-now resolution of security issues, just like we’d do for e.g. the server has fallen over or “our building is, physically, on fire.”
- These requirements suggest minimizing the number of tech stacks we work with, even if that means passing up the new hotness occasionally.
- Just like we have e.g. insurance on the building physically burning down, we should have some upfront investment in security. Good forms might include security training, outside consulting, or (if we’ve got a lot of money) contributing work towards securing tech stacks we rely on.


## You Should Be At Defcon 2 For Most Of February


Big security vulnerabilities tend to be discovered in bunches.


Why does this happen?

- **Blood in the water attracts sharks.** Some of my security friends would hate this phrasing, because “researchers don’t *cause* vulnerabilities, they *find* vulnerabilities”, but as a businessman who depends on software for his livelihood, I had exactly zero days of the last six years spent sleepless because of the latent vulnerability in Rails, but two days this month due to the pressing need for immediate mitigation. There are many more eyes pouring over Rails — and related projects — more closely now than typically. Many of them are white hats (yay!). Some aren’t. In general, there is a virtually infinite need for software security expertise, just like there is an infinite need for software, and there is a crushing lack of expertise which can meet it. Some folks who are capable of finding vulnerabilities are, due to attention/topicality/renewed interest/commercial potential/etc, now looking at Rails as of today.
- **Technology marches on.** After you have a new exploit vector to play with, you can start applying some of the technology used to discover / develop / exploit it against other code bases, code paths, etc etc. For example, the first Rails vulnerability was parlayed within a day into a similar vulnerability in the MultiXml gem. The same underlying “YAML is very dangerous” realization enabled the Rubygems compromise. If I were working on e.g. Django, I would strongly suspect that security researchers are going to see whether they can find similar patterns on Django — it wouldn’t be the first time, since e.g. HMAC tampering vulnerability disclosures in Rails were followed up by similar findings on Django the same week.


I previously had a version of this post queued up right after the first bug dropped, but didn’t hit Publish because I got busy that weekend and thought it wouldn’t be timely anymore. That post included the lines “I will bet $1,000 at 100-to-1 odds that Rails suffers another code execution vulnerability before the end of January.” If you had hypothetically taken that bet, you would have lost.


**You should expect February to be a very trying month for the Rails community and startups in general.** Your security team should be at Defcon 2: be ready to respond to patches with *particular* alacrity, and expect there to be failures in the ecosystem outside of your ability to control them. For example, I’d make sure that you can rebuild systems without requiring access to Github / Rubygems / etc, and that’s (unfortunately) the tip of the iceberg.


## This Sounds Like A #$()#%ing Disaster


That is primarily because this is a #$()#%ing disaster.


For my part, in addition to taking steps to fortify my own businesses, I’m (as time permits) doing some pro-bono security work on Rails. I do not have results which can be published yet. I strongly suspect based on early research that I will, in February, and I strongly suspect that other researchers (both white hats and the Bad Guys) are much, much better at this than I am.


Get ready. It will get worse before it gets better.
