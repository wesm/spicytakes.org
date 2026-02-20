---
title: "Staging Servers, Source Control & Deploy Workflows, And Other Stuff Nobody Teaches You"
date: 2010-12-12
url: https://www.kalzumeus.com/2010/12/12/staging-servers-source-control-deploy-workflows-and-other-stuff-nobody-teaches-you/
slug: staging-servers-source-control-deploy-workflows-and-other-stuff-nobody-teaches-you
word_count: 3503
---


I worked for almost three years as a cog in a Japanese megacorporation, and one of the best parts about that experience (perhaps even worth the 70 hour weeks) was that they taught me how to be a **professional** engineer.  Prior to doing so, my workflow generally involved a whole lot of bubble gum, duct tape, and praying.  I spent a lot of time firefighting broken software as a result, to the detriment of both my customers and myself.  Talking to other software developers has made me realize that I’m not the only person who was never taught that there are options superior to bubblegum.  If you aren’t lucky enough to work at a company that has good engineering in its very DNA, you’re likely to not know much about them.


This strikes me as the industry’s attitude to source control a few years ago, prior to a concerted evangelization movement by people like [Joel Spolsky](http://www.joelonsoftware.com/articles/fog0000000043.html).  It is virtually impossible to overstate how much using source control improves software development.  Our industry has changed in major ways since 2000, but our best practices (and knowledge of those best practices) are lagging a few years behind.  We could really use a Joel Test 2010 edition, for a world where “you should have build scripts for desktop software which can complete the build in one step” is largely an anachronism and where the front page to the website is no longer hand-coded in Notepad but, rather, is a shipping piece of software which can break in two hundred ways.


You’re not going to get the Joel Test 2010 here, mostly because I’m not Joel and there is no particular reason any company should judge its development practices relative to mine.  What I *would* like to give is some practical pointers for implementing three practices which, if you’re not already doing, will **greatly improve** the experience of writing software for the web:

1. Staging servers
2. Version control workflows
3. Tested, repeatable deployments


## Staging Servers


What is a staging server?  The basic idea is that it is **staging = production – users.** (If you’re Facebook, Google, or IMVU, you are lightyears ahead of this article and have some system where there are multiple levels of staging/production and where you can dynamically change them.  You already have geniuses working on your infrastructure.  Listen to them.  This article is for people who don’t have any option between “code runs on developer’s laptop” and “code runs in production.”)


Why do we have staging servers?  So that anything that is going to break on production **breaks on the staging server first**.  For this reason, you want your staging server to be as **similar to the production environment as you can possibly make it**.  If the production environment processes credit cards, the staging environment processes credit cards.  This means that if, e.g., your configuration for the payment gateway is borked, you’ll find out about that on the staging server prior to pushing it live to production and, whoopsie, not actually being able to get money from people.  If your production server uses Ruby 1.9, your staging server uses 1.9.  If the production server uses memcached on port 12345, the staging server uses memcached on port 12345.


(Many folks have systems which exist on more than one physical machine.  I don’t — I’m a small business where 2 GB of RAM is enough for anything I want to do.  If you have multiple machines, strike “staging server” and read as “staging system” below: all the benefits for having a separate staging server are still beneficial when your staging environment actually has fifteen physical servers running 47 VMs.)


Setting up a staging server *should be easy*.  If it is not easy, *you already have a problem* in your infrastructure, you just don’t know it yet: you’ve cobbled together your production server over time, usually by manually SSHing into it and tweaking things without keeping a log of what you have done.  (Been there, done that, got the “I Created A Monster” T-shirt.)  There isn’t a written procedure or automated script for creating it from the bare metal.  If you had that procedure written, you should be able to execute it and create a staging server that works inside of an hour.


Most people won’t be able to do this if they haven’t given thought to the matter before.  That is fixable, and should be fixed.  It has substantial benefits: if you have a repeatable procedure for provisioning a production system, then when disaster strikes you will be able to confidently execute that procedure and end up with a production system.  (Confidence is important since you’ll probably be terrified and rushed when you need to do this, and rushed terrified people make unnecessary mistakes.)


If you’re working on Rails, I highly recommend using [Deprec](https://github.com/mbailey/deprec)/[Capistrano ](https://github.com/capistrano/capistrano)with all new projects.  In addition to making it very easy to get a full Rails stack working on your deployment environment of choice , it helps automate routine deployment and server maintenance, and has mostly sensible defaults.  (I have only one quibble with deprec : it installs software from source rather than using your system’s package manager.  That means that upgrading e.g. Nginx two years down the road is needlessly hard and error prone, when instead you could just have used apt-get in the first place and then updating is a piece of cake.)


You can also use Fabric, Chef, Fog, or a similar system to script up building new environments.  Pick whichever strikes your fancy.  Try to recreate your production environment, down to a T, on another host at your VPS/cloud/etc provider, or on another physical machine if you actually still own machines.  Keep tweaking the script until it produces something which actually matches your production environment.  You now have a procedure for creating a staging server, and as an added bonus it also works for documenting your production environment in a reproducible fashion.


One nice thing about keeping your server configuration in scripts rather than just splayed across fifteen different places on the server (/etc/environment, /etc/crontab, /usr/local/nginx/conf/apps/AppName.conf, etc) is that it lives in source control.  Your cron jobs?  If they’re in source control, you’ll have a written record of what they are, what they’re supposed to do, and why they just blew up when you bork the underlying assumptions eight months down the line.  Your Nginx config?  If it is in source control, you’ll understand *why* you added that new location setting for static images only.  The voodoo in your postfix config?  A suitably descriptive commit note means you’ll never have to think about reproducing the voodoo again.


After you have the script which will produce your staging environment, you probably want to make a minimum number of alterations from production.  Many companies will want their staging environment to be non-public — that way, customers don’t see code before it is ready, and critical issues never affect the outside world.  There are many ways to do this: ideally, you’d just tweak a setting on your firewall and bam, nobody from the public Internet can get to your staging environment.  However, this is a wee bit difficult to pull off for some of us.  For one, I don’t actually have a hardware firewall (I use iptables on each VPS individually).


My staging environment simply includes a snippet in Nginx which denies access to everyone except a particular host (which I can proxy through).  This breaks integration with a few outside services (e.g. Twilio and Spreedly, which needs callbacks), so I make exceptions for the URLs those two need to access.  The more complicated your staging server configuration gets relative to production, the more likely you are to compromise its utility**.  Try to avoid exceptions.**


****That said, there are a couple that are too valuable to not make.  For example, my staging server has a whitelist of email addresses and phone numbers owned by me.  Through the [magic of monkeypatching](http://www.pastie.org/1370140), attempting to contact anyone else raises an exception.  That sounded a little paranoid until that day when I accidentally created an infinite loop and rang every number in the database a hundred times.  (My cell phone company *loves* me, but folks who accidentally collided with test data sure would not have.)


How do you get data to populate the staging server?  I use seed scripts and add more data by hand.  (I also have DB dumps available, but they tend to go stale against the current schema distressingly quickly: I recommend seed scripts.)  You can also dump the production DB and load it into the staging DB.  **Think long and hard before you do this.** For one, it is likely to be way, way the heck out of bounds for regulated industries.  For another, your staging server is probably going to periodically be insecure — insecurity is failure and **failure is what the staging server is for**.  Slurping all of the data out of a staging environment has caused many companies smarter than you to have to go into disaster management mode.  **Please be careful**.


### So you’ve got a staging server?  Now what?


At the simplest, you access your staging server with a browser and try to break things.  When you break things, you fix things, then you redeploy the staging server and try to break them again.  This is what you are probably doing right now with production, except that your customers don’t have to see broken things when you break things.


Eventually, you can script up attempts to break things, using e.g. Selenium.  Then when you break things, you add them to the list of things that Selenium tries to break.  If you run that against the staging server after every code check in (a process known as continuous integration), you’ll quickly catch regressions before they disrupt paying customers.  This is a wee bit harder than just having a staging server — OK, a lot harder — but **you’ll get clear, obvious advantage out of every increment of work you do** on this path, so don’t let present inability to be Google prevent you from getting started.


## Version Control & Deployment Workflows


Everyone should use version control, but people tend to use version control differently.  Git is very popular in the Rails community, but *there are probably no two companies using git the same way*.  The key thing is that you agree with your team on how you use version control — document your assumptions, document your processes, then apply them religiously.  This will reduce conflicts on the team, reduce mistakes, and help you get more out of your tools.


There are a million ways to use version control and most of them are perfectly OK.  I’m going to mention mine, but it isn’t the canonical Right Way, it is just one way which works for a (very) small company.  Yours will likely be different, but you can see some of the things which go into design of a version control workflow.


### Assumptions I Make About Life, The Universe, And Everything

1. I use git.  Git has notion of branches, tags, and remotes (physically distinct repositories) — if you don’t know what these are, Google for [getting started with git].
2. **I generally work alone or with a very small team.** (This assumption underpins very important parts of my workflow.  It won’t expand very well to a 200 man distributed team, but it might well work for 2 ~ 5 people.)
3. There is exactly one canonical repository, origin.  Developers maintain other repositories on their workstation.  Automated processes like deployment happen only with reference to the origin.  Code existing outside of the origin does not officially exist yet, for any purpose.  The history preserved in the origin is, in principle, sacred.
4. There is a branch called deploy.  The HEAD of deploy (the most recent code on it) is presumptively ready to be put into production.
5. Tags are used to take snapshots of the code base and preserve them in amber with a human readable name.  Right before we deploy to either production or staging, the HEAD gets tagged, so that we can easily find it later, with a simple naming convention (I use production_release_X and staging_release_X, where X just increments upwards — some people might prefer timestamps).  Production release tags are never deleted.  Staging tags get periodically culled when convenient to do so.
6. Development of any feature expected to take longer than a few hours happens on a feature branch.  (I do occasional work right on deploy locally, for issues of the “Minor copy edit on dashboard.” variety.  This would be one of the first things to go if I were working on a larger team.)


So how does this actually work in practice?  Let’s say I’m implementing a new feature.  I create a new branch to work on.  I code a bit, creating local commits with *wild abandon* any time I have accomplished something which I don’t want to lose.  When I believe code to be functional, I fire a capistrano task which tags the current head of my branch, pushes that tag to origin, and deploys it to the staging server.  I then continue testing on the staging server, for example verifying that Twilio integration actually works with Twilio (which cannot conveniently access localhost:3000 on my laptop).  I continue writing code, committing, tagging, and pushing to the staging server until the feature is ready.


Then, I switch back to the deploy branch and merge in my feature branch (with –no-ff, which creates a commit message just for the merge — this handily groups the twenty or thirty commits I just made into one easily readable story for myself later).  I then tag a production release (manually — this is entirely to force me to think through whether I’m ready for a production release), verify that there is no diff between it and the most recent staging release, and then push the new tag to origin.  I then fire the Capistrano task which checks out the new deployment tag and restarts the server.


What does this get me versus my previous SVN workflow for Bingo Card Creator, which was “Work only on one branch, commit stuff when I think it is ready, and deploy the trunk manually on occasion”?

1. I cause much less downtime for the production server due to reasons like *svn commit -m ‘Whoops, forgot a setting in production.rb’* and *svn commit -m ‘r1234 introduced dependency on foobar gem without putting it in environment file, causing rake gems:install to not load it.  Mongrels then failed to restart.’*
2. My deploy branch has a *relatively* clean history, so when things start to break next year in production, finding the change sets which eventually caused the breakage will be less of a needle in the haystack search than finding them in SVN is.  SVN’s history is 1800 unedited commits, recording my stream of consciousness as they happened.  My stream of consciousness is frequently stupid, particularly when I’m panicking because the server is down.
3. This decouples the staging server from production in a clean fashion (so that I can advance the staging server a feature or three at a time if I want to), but guarantees that when I’m actually ready to deploy, I’m deploying exactly what did not break on the staging server.
4. Tagging releases gives you an Oh Crikey button, as in Oh Crikey, that last release broke stuff.  You can quickly rollback the deploy to a known good tag, isolate the changes which broke production, and fix them.
5. Deploy scripts manage releases with multiple moving parts a lot better than I do, even when I’m working from a checklist.


By the way, git gives you many options for recovering from problems — even severe problems — without requiring either gymnastics or a full-blown CSI investigation to discover what happened later.  For example, let’s pretend I just deployed tag production_deploy_82, and have discovered some issue serious enough to require an immediate rollback to production_deploy_81, which is known to be good:


How you clean up the mess on the server is up to you: good options include “deploy 81 again”, “tag a release 83 equivalent to 81, then deploy it”, and “rollback to the copy of 81 which still exists on the server.”  (Capistrano includes deploy:rollback, which will do exactly this.)  Any of these will work, just always do it the same way to avoid stepping on each others’ toes.  I prefer tagging a new release so that I can add a descriptive message explaining why 82 just created an emergency.


This is important because it leaves a paper trail — if you’re pulling a release from production, something just went seriously wrong with your processes.  **Emergencies are not supposed to happen** – anything that lets an issue get that far isn’t just a one-off failure of whatever broke, it is a series of failures of the systems/processes designed to prevent failures from getting that far.  After you’ve put out the fire, [investigate what went wrong](http://www.startuplessonslearned.com/2009/07/how-to-conduct-five-whys-root-cause.html) and tweak your processes such that a similar failure in the future gets caught prior to bringing down production.  **The sleep you save may be your own**.


**Scaling this to more programmers**: Do whatever works for you!  I would probably create a staging branch and have folks integrate stuff into the staging branch when it was ready to go to the official staging environment.  I also might make per-developer staging environments: since creating one from the bare metal is supposed to be essentially free, let them all have their own where they can be reckless without spoiling the experience of other developers.  We can worry about code interaction on the “real” staging server.  Then, have folks communicate when they consider everything they have on staging ready for release, and release when everybody says it is ready.


The important thing is that, whatever process you use, you document it, teach it, and enforce it.


## Stuff Your Deployment Script Might Not Do Today But Probably Should

1. Depending on your scale and how you use e.g. memcached, it might be safe to purge the cache on every re-deploy, which will prevent some hard to diagnose bugs.  At a certain scale, this is virtually a recipe for taking your site down in a cache stampede, but I’m not Facebook and having capacity problems means that I am probably already vacationing at my hollowed-out volcano lair.
2. Tell everybody on the team that you just deployed.  I know some teams who have an IRC channel with a bot who announces redeploys.  A quick email CCed to five developers also probably suffices.
3. Restart worker processes.  This is easy to forget but, if you do it by hand, you’ll eventually forget and then have two versions of the application in production at once.  If you’re not prepared for that, it *will* bite you on the hindquarters when, e.g., the application servers ask the workers to execute methods that the workers do not know now exist in the code base.
4. Do sanity checks.  You can go arbitrarily deep with complexity here.  For a first cut, mine for Appointment Reminder restarts the application server, counts ten seconds, then tries to access an internal URL.  If the application server isn’t up, or if the action at that URL blows up for any reason, the deployment script fails the deploy, rolls back to a known-good version, and sends me a very crossly worded email.  (You can do this for the staging server, too.)
5. Integrate with other systems which manage the state of your code/business.  For example, I use [Hoptoad](http://www.hoptoadapp.com).  Hoptoad keeps track of exceptions and mails you when they happen, in such a fashion that your inbox doesn’t get buried by e.g. Googlebot deciding to do an impromptu fuzz test on your website.  I mark all exceptions as resolved every time I deploy to the environment they happened in.  You could also e.g. update an internal wiki by adding a new page specific to the deployment, automatically update your bug tracker to change the status of the bugs that you (presumably) just squashed, or start a new cohort for your stats tracking.


## Is There Anything You Would Like To Add?


The trend towards openness with regards to technical practices on the Internet is a major, major win for everybody in our industry.  Best practices do not have to be passed from master to apprentice as oral lore.  Like OSS, since they’re often glue rather than competitive advantages (for many companies — not all), sharing them mostly doesn’t hurt you and can improve the situation of everybody.  So, in that spirit, if you’ve got anything you’d like to add, particularly for how you do things or how you would adapt this advice outside the scope of a very small business, I’d love to hear about it either in the comments or on your own blog (feel free to leave a link if it is relevant.)
