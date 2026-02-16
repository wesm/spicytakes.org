---
title: "Two weeks with Terraform"
date: 2016-02-23
url: https://charity.wtf/2016/02/23/two-weeks-with-terraform/
word_count: 2037
---


I’ve been using terraform regularly for 2-3 weeks now.  I have terraformed in rage, I have terraformed in delight.  I thought it might be helpful to share some of my notes and lessons learned.


#### **Why Terraform?**


Because I am fucking *sick *and* tired* of not having versioned infrastructure.  Jesus christ, the ways my teams have bent over backwards to fake infra versioning after the fact (nagios checks running ec2 diffs, anyone?).


Because I am starting from scratch on a green field project, so I have the luxury of experimenting without screwing over existing customers.  Because I generally respect [Hashicorp](https://www.hashicorp.com/) and think they’re on the right path more often than not.


If you want versioned infra, you basically get to choose between 1) [AWS CloudFormation](https://aws.amazon.com/cloudformation/) and its wrappers ([sparkleformation](https://github.com/sparkleformation), [troposphere](https://github.com/cloudtools/troposphere)), 2) [chef-provisioner](https://github.com/chef/chef-provisioning), and 3) [Terraform.](https://www.hashicorp.com/blog/terraform.html)


The orchestration space is very green, but I think Terraform is the standout option.  (More about why later.)  There is precious little evidence that TF was developed by or for anyone with experience running production systems at scale, but it’s … definitely not as actively hostile as CloudFormation, so it’s got that going for it.


#### First impressions


Stage one: my terraform experiment started out great.  I read a bunch of stuff and quickly spun up a VPC with public/private subnets, NAT, routes, IAM roles etc in < 2 days.  This would be nontrivial to do in two days *without* learning a new tool, so TOTAL JOY.


Stage two: spinning up services.  This is where I started being like … “huh.  Has anyone ever actually used this thing?  For a real thing?  In production?”  Many of the patterns that seemed obvious and correct to me about how to build robust AWS services were completely absent, like any concept of a subnet tier spanning availability zones.  I did some inexcusably horrible things with variables to get the behavior I wanted.


Stage three: … *modules*.  Yo, all I wanted to do was refactor a perfectly good working config into modules for VPC, security groups, IAM roles/policies/users/groups/profiles, S3 buckets/configs/policies, autoscaling groups, policies, etc, and my entire fucking world just took a dump for a week.  SURE, I was a TF noob making noob mistakes, but I could not believe how hard it was to debug literally anything..


This is when I started tweeting sad things.


> my kingdom for a printf, or a linter, or — dear god — the ability to step through the run and print out types & values.
> — Charity Majors (@mipsytipsy) [February 10, 2016](https://twitter.com/mipsytipsy/status/697253381295837185?ref_src=twsrc%5Etfw)


The best (only) way of debugging terraform was just reading really, really carefully, copy-pasting back and forth between multiple files for hours to get all the variables/outputs/interpolation correct.  Many of the error messages lack any context or line numbers to help you track down the problem.  Take this prime specimen:


```
Error downloading modules: module aws_vpc: Error loading .terraform
/modules/77a846c64ead69ab51558f8c5be2cc44/main.tf: Error reading 
config for aws_route_table[private]: parse error: syntax error
```


Any guesses?  Turned out to be a stray ‘}’ on line 105 in a different file, which HCL vim syntax highlighting thought was A-OK.  That one took me a couple hours to track down.


Or this:


```
aws_security_group.zookeeper_sg: cannot parse '' as int: 
strconv.ParseInt: parsing "": invalid syntax
```


Which *obviously* means you didn’t explicitly define some inherited port as an int, so there’s a string somewhere there lurking in your tf tree.  (*Obviously* in retrospect, I mean, after quite a long time poking haplessly about.)


Later on I developed more sophisticated patterns for debugging terraform.  Like, uhhh, bisecting my diffs by commenting out half of the lines I had just added, then gradually re-adding or re-commenting out more lines until the error went away.


Security groups are the worst for this.  SO MANY TIMES I had security group diffs run cleanly with “tf apply”, but then claim to be modifying themselves over and over.  Sometimes I would track this down to having passed in a variable for a port number or range, e.g. “cidr_blocks = [“${var.ip_range}”]”.  Hard-coding it to “cidr_blocks [“10.0.0.0/8″]” or setting the type explicitly would resolve the problem.  Or if I accidentally entered a CIDR range that AWS didn’t like, like 10.0.20.0/20 instead of 10.0.16.0/20.  The change would apply and usually it would work, it just didn’t think it had worked, or something.  TF wasn’t aware there was a problem with the run so it would just keep “successfully” reapplying the diff every time it ran.


#### Some advice for TF noobs

- As @[phinze](http://twitter.com/phinze) told me, “modules are basically like functions — a variable is an argument, output is a return value”.  This was helpful, because that was completely unintuitive to me when I started refactoring.  It took a few days of wrestling with profoundly inscrutable error messages before modules really clicked for me.
- Strings.  Lists.  [You can only pass variables around as strings](https://www.terraform.io/docs/configuration/interpolation.html).  Split() and join() are your friends.  Oh my god I would sell so many innocent children for the ability to pass maps back and forth between modules.
- [No interpolation for resource names](https://github.com/hashicorp/terraform/issues/3888) makes me so sad.  Basically you can either use local variable maps, or multiple lists and just … run those index counters like a boss I guess..
- Use AWS termination protection for stateful services or anything risky once you’re in production.  Use create_before_destroy on resources like ASG launch configs.  Use “don’t destroy” where you must — but as sparingly as possible, because that basically breaks the entire TF model.
- If you change the launch config for an ASG, like replacing the AMI for example, you might expect TF to kick off an instance recycle.  It will not.  You must manually terminate the instances to pick up the new config.
- If you’re collaborating with a team — ok, even if you’re not — find a remote place to store the tfstate files.  Try S3 or github, or shell out for Atlas.  Local state on laptops is for losers.
- TF_LOG=DEBUG has never once been helpful to me.  I can only assume it was written for the Hashicorp developers, not for those of us using the product.


Errors returned by AWS are completely opaque.  Like “You were not allowed to apply this update”.  Huh?  Ok well if it fails on “tf plan”, it’s probably a bad terraform config.  If it successfully plans but fails on “tf apply”, your AWS logic is probably at fault.


Terraform does not do a great job of surfacing AWS errors.


For example, here is some terraform output:


```
tf output: "* aws_route_table.private: InvalidNatGatewayID.NotFound
: The natGateway ID 'nat-0e5f4ea507113b423' does not exist"
```


Oh!~  Okay, I go to the AWS console and track down that NAT gateway object and find this:


```
"Elastic IP address [eipalloc-8583b7e1] is already associated"
```


Hey, that seems useful!  Seems like TF just timed out bringing up one of the route tables, so it tried assigning the same EIP twice.  It would be nice to surface more of this detail into the terraform output, I hate having to resort to a web console.


Last but not least: one time I changed the *comment string* on a security group, and “tf plan” went into an infinite dependency loop.  I had to roll back the change, run terraform destroy against all resources in a bash for loop, and create an new security group with all new instances/ASGs just to change the comment string.  **You cannot change comment strings or descriptions for resources without the resources being destroyed. ** This seems PROFOUNDLY weird to me.


#### Wrapper scripts


Lots of people seem to eventually end up wrapping terraform with a script.  Why?

- There is no concept of a $TF_ROOT.  If you run tf from the wrong directory, it will do some seriously confusing and screwed up shit (like duping your config, but only some of it).
- If you’re running in production, you prob do not want people to be able to accidentally “terraform destroy” the world with the wrong environment
- You want to enforce test/staging environments, and promotion of changes to production after they are proven good
- You want to automatically re-run “tf plan” after “tf apply” and make sure your resources have converged cleanly.
- So you can add slack hooks, or hipchat hooks, or github hooks.
- Ummm, have I mentioned that TF can feel somewhat undebuggable?  Several people have told me they create rake tasks or YML templates that they then generate .tf files from so they can debug those when things break.  (Erf …)


#### **Okay, so …..**


God, it feels I’ve barely gotten started but I should probably wrap it up.[*]  Like I said, I think terraform is best in class for infra orchestration.  And orchestration is a thing that I desperately want.  Orchestration and composability are the future of infrastructure.


But also terraform is green as fuck and I would not recommend it to anyone who needs a 4-nines platform.


Simply put, there is a lot of shit I don’t want terraform touching.  I want terraform doing as little as possible.  I have already put a bunch of things into terraform that I plan on taking right back out again.  Like, you should never be running a userdata.sh script after TF has bootstrapped a node.  Yuck.. That is a job for your cfg management, or *possibly* a job for packer or a custom firstboot script, but *never* your orchestration tool!  I have already stuffed a bunch of Route53 DNS into TF and I will be ripping that right back out soon.  **Terraform should not be managing any kind of dynamic data.  **Or service registry, or configs, or ….


Terraform is fantastic for defining the bones of your infrastructure.  Your networking, your NAT, autoscaling groups, the bits that are robust and rarely change.  Or spinning up replicas of production on every changeset via Travis-CI or Jenkins — yay!  Do that!


But I would not feel safe making TF changes to production every day.  And you should delegate any kind of reactive scaling to ASGs or containers+scheduler or whatever.  I would never want terraform to interfere with those decisions on some arbitrary future run.


Which is why it is important to note that terraform does not play nicely with others.  It wants to own the whole thing.  [Monkeypatching TF onto an existing infra is kind of horrendous](https://github.com/hashicorp/terraform/issues/581).  It would be nice if you could tag certain resources or products as “this is managed by some other system, thx”.


#### So: why terraform?


Well, it is fairly opinionated.  It’s actively developed by some really smart people.  It’s moving fast and has most of the momentum in the space.  It’s composable and interacts well with other players iff you make some good life choices.  ([Packer](http://packer.io), for example, is amazing, by far the most unixy utility of the Hashicorp library.)


Just look at the rate of bug fixes and releases for Terraform vs CloudFormation.  Set aside crossplatform compatibility etc, and just look at the energy of the respective communities.  Not even a fair fight.


Want more?  Ok, well I would rather adopt one opinionated philosophy for my infrastructure, supplementing where necessary, than duct tape together fifty different half baked philosophies about how software and infrastructure should work and spend all my time mediating their conflicts.  (This is one of my beefs with CloudFormation: ***AWS has no opinions,*** only slobbering, squidlike, directionless-flopping optionalities.  And while we’re on the topic it also has nothing like “tf plan” for previewing changes, so THAT’S PRETTY STUPID TOO.)


I do have some concerns about [Hashicorp](https://www.hashicorp.com/) spreading themselves too thin on too many products.  Some of those products probably shouldn’t exist.  Meh.


Terraform has a ways to go before it feels predictable and debuggable, but I think it’s heading in the right direction.  It’s been a fun couple weeks and I’m excited to start contributing to the ecosystem and integrating with other components, like chef-solo & consul.


**[*]** OMGGGGGGG, I never even got to the glorious horrors of the [terraforming gem](https://github.com/dtan4/terraforming) and how you are most definitely going to end up manually editing your *.tfstate files.  Ahahahahaa.


**[**]** Major thanks to @[phinze](http://twitter.com/phinze), @[solarce](http://twitter.com/solarce), @[ascendantlogic](http://twitter.com/ascendantlogic), @[lusis](http://blog.lusis.org/blog/2015/10/12/terraform-modules-for-fun-and-profit/), @[progrium](http://twitter.com/progrium) and others who helped me limp through my first few weeks.
