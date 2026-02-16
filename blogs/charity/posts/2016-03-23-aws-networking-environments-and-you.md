---
title: "AWS Networking, Environments and You"
date: 2016-03-23
url: https://charity.wtf/2016/03/23/aws-networking-environments-and-you/
word_count: 2104
---


Last week we hit an important milestone in the life of our baby [startup](http://twitter.com/houndexplorer): a functional production environment, with real data flowing from ingestion to storage to serving queries out!  (Of course everything promptly exploded , but whatever.)


This got me started thinking about how to safely stage and promote terraform changes, in order to isolate the blast radius of certain destructive changes.  I tweeted some random thing about it,


> hey, anyone have a strong argument for one VPC per env {staging,prod} vs single VPC with subnets for envs, managing isolation w SGs/routes?
> — Charity Majors (@mipsytipsy) [March 16, 2016](https://twitter.com/mipsytipsy/status/710224093027524608?ref_src=twsrc%5Etfw)


… and two surprisingly fun things happened.  I learned some new things about AWS that I didn’t know (after YEARS of using it).  And hilariously, I learned that I and lots of other people still believe things about AWS that **aren’t actually true **anymore.


That’s why I decided to write this.  I’m not gonna get super religious on you, but I want to recap the current set of common and/or best practices for managing environments, network segmentation, and security automation in AWS, and I also want to remind you that this post will be out of date as soon as I publish it, because things are changing pretty crazy fast.


## Multiple Environments: Why I Should Care?


An environment exists to provide resource isolation.  You might want this for security reasons, or testability, or performance, or just so you can give your developers a place to fuck around and not hurt anything.


Maybe you run a bunch of similar production environments so you can give your customers security guarantees or avoid messy performance cotenancy stuff.  Then you need a template for stamping out lots of these environments, and you need to be *really* sure they can’t leak into each other.


Or maybe you are more concerned about the vast oceans of things you need to care about beyond whatever unit tests or functional tests are running on your laptop.  Like: capacity planning, load testing, validating storage changes against production workloads, exercising failovers, etc.  Any scary changes you  have, you need a production-like env to practice in.


Bottom line: If** you can’t spin up a full copy of your infra and test it, you don’t actually have “infrastructure as code”.**  You just have … some code, and duct tape.


[https://twitter.com/phinze/status/710227204349624321](https://twitter.com/phinze/status/710227204349624321)


The basics are simple:

- Non-production environments must be walled off from production as strongly as possible.  You should NEVER be able to accidentally to connect to a prod db from staging (or from one prod env to another).
- Production and non-production environments (or all other prod envs) should share as much of the same tooling and code paths as possible.  Like, some amount asymptotically approaching 100%.  Any gaps there will inevitably, eventually bite you in the ass.


## Managing Multiple Environments in AWS


There are baaaasically three patterns that people use to manage multiple environments in AWS these days:

1. One AWS billing account and one flat network (VPC or Classic), with isolation performed by routes or security groups.
2. Many AWS accounts with consolidated billing.  Each environment is a separate account (often maps to one acct per customer).
3. One AWS billing account and many VPCs, where each environment ~= its own VPC.


Let’s start old school with a flat network.


### 1:  One Account, One Flattish Network


This is what basically everyone did before VPC.  (And ummm let’s be honest, lots of us kept it up for a while because GOD networking is such a pain.)


In EC2 Classic the best you got was security groups.  And — unlike VPC security groups — you couldn’t stack them, or change the security group of an instance type without destroying it, and there was a crazy low hard cap on the (# of secgroup rules * # of secgroups).  You could kind of gently “suggest” environments with things like DNS subdomains and config management, and sometimes you would see people literally just roll over and resort to  $ENV variables.


Most people either a) gave up and just had a flat network, or b) this happened.


[@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) we use a single vpc and more sgs than instances, it's a tangled legacy mess. I'd rather go for vpc per env/team whatever— Jan B. (@bracki) [March 16, 2016](https://twitter.com/bracki/status/710230597977956353?ref_src=twsrc%5Etfw)


At Parse we did a bunch of complicated security groups plus chef environments that let us spin up staging clusters and the occasional horrible silo’d production stack for exceptional customer requirements.  Awful.


*VPC has made this better.*  Even if you’re still using a flat network model.  You can now manage your route tables, stack security groups and IAM rules and reapply to existing nodes without destroying the node or dropping your internet connections.  You can define private network subnets with NAT gateways, etc.


[https://twitter.com/sudarkoff/status/710264656367996928](https://twitter.com/sudarkoff/status/710264656367996928)


Some people tell me they are using a single VPC with network ACLs to separate environments for ease of use, because you can reuse security groups across environments.  Honestly this seems a bit more like a bug than a feature to me, because a) you give up isolation and b) I don’t see how that helps you have a versioned, tested stack.


[https://twitter.com/tomtheguvnor/status/710226892633333762](https://twitter.com/tomtheguvnor/status/710226892633333762)


Ok moving on to the opposite of the spectrum, the crazy kids who are doing tens (or TENS OF THOUSANDS) of linked accounts.


### 2:  One AWS Account Per Environment


A surprising number of people adopted this model in the bad old EC2 Classic days, not because they necessarily wanted it but because they need a stronger security model and looser resource caps.  This is why AWS released [Consolidated Billing](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) way back in 2010.


I actually learned a lot this week about the multi-account model!  Like that you can create [IAM roles that span accounts](http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial-cross-account-with-roles.html), or that you can [share AMIs between accounts.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html).  This model is complicated, but there are some real benefits.  Like real, actual, hardcore security/perf isolation.  And you will run into fewer resource limits than jamming everything into a single account, and revoking/managing IAM creds is clearer.


Security nerds love this model, but it’s not clear that …. literally anyone else does.


[@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) i did one full AWS account per ENV as a way to fully segment (using consolidated billing to manage). felt "safer"— petecheslock@hachyderm.io (@petecheslock) [March 17, 2016](https://twitter.com/petecheslock/status/710277140764295168?ref_src=twsrc%5Etfw)


Some things that make me despise it without even trying it:

- AWS billing is ALREADY a horrendous hairball coughed up by the world’s ugliest cat, I can’t even imagine trying to wrangle multiple accounts.
- It’s more expensive, you incur extra billing costs.
- Having to explicitly list any resource you want to share between any accounts just makes me want to tear my hair out strand by strand while screaming on a street corner
- Account creation API still has manual steps, like getting certs/keypairs.
- You cannot make bulk changes to accounts, and AWS doesn’t like you having thousands of linked accounts.  Also limits your flexibility with Reserved Instances.


Here is a pretty reasonable [blog p0st](https://segment.com/blog/rebuilding-our-infrastructure/) laying out some of the benefits though, and as you can see, there are plenty of other crazy people who like it.  Mostly security nerds.


### 3:  One AWS Account, One VPC Per Environment


I have saved the best for last.  I think this is the best model, and the one I am adopting.  You spin up a production VPC, a staging VPC, dev VPC, Travis-CI VPC.  EVERYBODY GETS A VPC!#@!


One of those things that everybody seems to “know” but isn’t true is that you can’t have lots of VPCs.  Yes, it is capped at 5 by default, and many people have stories about how they couldn’t get it raised, and that used to be true.  But **the hard cap is now 200**, not 10, so VPC awayyyyyyyy my pretties!


[@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) 1 account per env, many VPCs. IAM/VPC peer makes shit easy... we run many accounts, 200+ VPCs in our prod acc— Ben Bromhead (@BenBromhead) [March 16, 2016](https://twitter.com/BenBromhead/status/710239464530923520?ref_src=twsrc%5Etfw)


Here’s another reason to love VPC <-> env mapping: orchestration is finally coming around to the party.  Even recently people were still trying to make chef-metal a thing, or developing their own coordination software from scratch with Boto, or just using the console and diffing and committing to git.


Dude, *stop.  *We are past the point where you should default to using Terraform or CloudFormation for the bones of your infrastructure, for the things that rarely change.  And once you’ve done that you’re most of the way to a reusable, testable stack.


Most of the cotenancy problems that account-per-env solved are a lot less compelling to me now that VPCs exist.


[@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) if you're doing automation, sep VPC/accounts let you fully test that automation rather than "just" app code— Adam (@uptill_3) [March 17, 2016](https://twitter.com/uptill_3/status/710397938065866752?ref_src=twsrc%5Etfw)


VPCs are here to help you think about infrastructure like regular old code.  Lots of VPCs are approximately as easy to manage as as one VPC.  Unlike lots of accounts, which are there to give you headaches and one-offs and custom scripts and pointy-clicky shit and complicated horrible things to work around.


[@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) We just have CloudFormation templates that take IP prefix and VPC ID as arguments; seems to have worked pretty well.— Alex Rasmussen (@alexras) [March 16, 2016](https://twitter.com/alexras/status/710230250504912896?ref_src=twsrc%5Etfw)


VPCs have some caveats of their own.  Like, you can only assign a /16 to any VPC.  If you’re using 4 availability zones and public subnets + natted private subnets, that’s only ~8k IPs per subnet/AZ pair.  Shrug.


[You can peer security groups across different VPCs](https://aws.amazon.com/about-aws/whats-new/2016/03/announcing-support-for-security-group-references-in-a-peered-vpc/), but not across regions (yet).  Also, if you’re a terraform user, be aware that it handles VPC peering fine but doesn’t handle multiple accounts very well.


Lots of people seem to have had issues with security group limits per VPC, even though the limit is 500 and says it can be raised by request.  I’m …. not sure what to think of that.  I *feel* like if you’re building a thing with > 500 sec group rules on a single VPC, you’re probably doing something wrong.


## Test my code you piece of shit I dare you


Here’s the thing that got me excited about this from the start though, which is having the ability to do things like test terraform modules on a staging VPC from a branch before promoting the clean changes to master.  If you plan on doing things like running bleeding-edge software in production *cough* you need allllll the guard rails and test coverage you can possibly scare up.  **VPCs help you get this** in a massive way.


Super quick example, say you’re using adding a NAT gateway to your staging cluster, you would use the remote git source with your changes:


[code language=”javascript”]

// staging

module "aws_vpc" {

  source = "git::ssh://git@github.com/houndsh/infra.git//terraform/modules/aws_vpc?ref=charity.adding-nat-gw"

  env = ${var.env}

…

}

[/code]


And then once you’ve validated the change, you simply merge your branch to master and run terraform plan/apply to production.


[code language=”javascript”]

// production

module "aws_vpc" {

  source = "github.com/houndsh/infra/terraform/modules/aws_vpc"

  env = "${var.env}"

…

}

[/code]


And for GOD’S SAKE USE DIFFERENT STATE FILES FOR EACH VPC / ENVIRONMENT okayyyyyy but that is a different rant, not an AWS rant, so let’s move along.


## In Conclusion


There are legit reasons to use all three of these models, and infinite variations upon them, and your use case is not my use case, blah blah.


But moving from one VPC to multiple VPCs is really not a big deal.  I know a lot of us bear scars, but it is *nothing* like the horror that was trying to move from EC2 Classic to VPC.


[https://twitter.com/mistofvongola/status/710239882912747524](https://twitter.com/mistofvongola/status/710239882912747524)


VPC has a steeper learning curve than Classic, but it is sooooo worth it.  Every day I’m rollin up on some new toy you get with VPC (ICMP for ELBs! composable IAM host roles! new VPC NAT gateway!!!).  The rate at which they’re releasing new shit for VPC is staggering, I can barely keep up.


[@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) we have multiple aws accounts with one vpc per. Private and public subnets in that vpc. Most non ELB aws resources in private— Alfonso (@alfonso__c) [March 16, 2016](https://twitter.com/alfonso__c/status/710232944162504704?ref_src=twsrc%5Etfw)


Alright, said I wasn’t gonna get religious but I totally lied.


**VPC is the future and it is awesome, and unless you have some VERY SPECIFIC AND CONVINCING reasons to do otherwise, you should be spinning up a VPC per environment with orchestration and prob doing it from CI on every code commit, almost like it’s just like, you know, code**.


That you need to test.


Cause it is.


*(thank you to everybody who chatted with me and taught me things and gave awesome feedback!!  knuckle tatts credit to @mosheroperandi)*
