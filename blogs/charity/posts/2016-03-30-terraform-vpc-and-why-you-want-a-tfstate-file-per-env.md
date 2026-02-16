---
title: "Terraform, VPC, and why you want a tfstate file per env"
date: 2016-03-30
url: https://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/
word_count: 2595
---


Hey kids!  If you’ve been following along at home, you may have seen my earlier posts on [getting started with terraform](http://charity.wtf/2016/02/23/two-weeks-with-terraform/) and figuring out what [AWS network topology](http://charity.wtf/2016/03/23/aws-networking-environments-and-you/) to use.  You can think of this one as like if those two posts got drunk and hooked up and had a bastard hell child.


Some context: our terraform config had been pretty stable for a few weeks.  After I got it set up, I hardly ever needed to touch it.  This was an explicit goal of mine.  (I have *strong feelings* about delegation of authority and not using your orchestration layer for configuration, but that’s for another day.)


And then one day I decided to test drive Aurora in staging, and everything exploded.


Trigger warning: rants and scary stories about computers ahead*.*  The first half of this is basically a post mortem, plus some tips I learned about debugging terraform outages.  The second half is about why you should care about multiple state files, how to set up and manage multiple state files, and the migration process.


## First, the nightmare


This started when I made a simple tf module for Aurora, spun it up in staging, assigned a CNAME, turned on multi-AZ support for RDS, was really just fussing around with minor crap in staging, like you do.  So I can’t even positively identify which change it was that triggered it, but around 11 pm Thursday night the *entire fucking world* blew up.  Any terraform command I tried to run would just crash and dump a giant crash.log.


```
Terraform crashed! This is always indicative of a bug within Terraform.
```


So I start debugging, right?  I start backing out changes bit by bit.  I removed the Aurora module completely.  I backed out several hours worth of changes.  It became clear that the tfstate file must be “poisoned” in some way, so  I disabled remote state storage and starting performing surgery on the local tfstate file, extracting all the Aurora references and anything else I could think of, just trying to get tf plan to run without crashing.


What was especially crazy-making was the fact that I could apply *any* of the modules or resources to *any* of the environments independently.  For example:


```
 $ for n in modules/* ; do terraform plan -target=module.staging_$n ; done
```


… would totally work!  But “terraform plan” in the top level directory took a giant dump.


I stabbed at this a bunch of different ways.  I scrolled through a bunch of 100k line crash logs and grepped around for things like “ERROR”.  I straced the terraform runs, I deconstructed tens of thousands of lines of tfstates.  I spent far too much time investigating the resources that were reporting “errors” at the end of the run, which — spoiler alert — are a **total red herring**.  Stuff like this —


```
 15 module.staging_vpc.aws_eip.nat_eip.0: Refreshing state... (ID: eipalloc-bd6987da)
 16 Error refreshing state: 34 error(s) occurred:
 17 
 18 * aws_s3_bucket.hound-terraform-state: unexpected EOF
 19 * aws_rds_cluster_instance.aurora_instances.0: unexpected EOF
 20 * aws_s3_bucket.hound-deploy-artifacts: unexpected EOF
 21 * aws_route53_record.aurora_rds: connection is shut down
```


It’s all totally irrelevant, disregard.


It’s like 5 am by this point which is why I feel only slightly less fucking retarded about the fact that [@stack72](http://twitter.com/stack72) had to gently point out that **all you have to do is find the “panic” in the crash log**, because terraform is written in Go so OF COURSE THERE IS A PANIC buried somewhere in all that dependency graph spew.  God, I felt like such an idiot.


massive thanks to [@stack72](https://twitter.com/stack72?ref_src=twsrc%5Etfw) who showed me this on thursday, and [@phinze](https://twitter.com/phinze?ref_src=twsrc%5Etfw) for adding it to the docs!  [https://t.co/IAlhRvFn0C](https://t.co/IAlhRvFn0C)— Charity Majors (@mipsytipsy) [March 19, 2016](https://twitter.com/mipsytipsy/status/711327350781124609?ref_src=twsrc%5Etfw)


## The painful recovery


I spent several hours trying to figure out how to recover gracefully by isolating and removing whatever was poisoned in my state.  Unfortunately, some of the techniques I used to try and systematically validate individual components or try to narrow down the scope of the problem ended up making things much, much worse.


For example: applying individual modules (“terraform apply -target={module}”) can be *extremely* problematic.  I haven’t been able to get an exact repro yet, but it seems to play out something like this: if you’re applying a module that depends on other resources that get dynamically generated and passed into it, but you aren’t applying the modules that do that work in the same run, **terraform will sometimes just create them again**.


Like, a whole duplicate set of all your DNS zones with the same domain names but different zone ids, or a duplicate set of VPCs with the same VPC names and subnets, routes, etc, and you only find out if it gets to a point where it tries to create one of those rare resources where AWS actually enforces unique names, like autoscaling groups.


And yes, I do run tf plan.  Religiously.  But when you’re already in a bad state and you’re trying to do unhealthy things with mutated or corrupt tfstate files … shit happens.  And thus, by the time this was all over:


**I ended up deleting my entire infrastructure by hand, three times.**


I’m literally talking about clicking select-all-delete in the console on fifty different pages, writing grungy shell scripts to cycle through and delete every single AWS resource, purging local cache files, tracking down resources that exist but don’t show up on the console via the CLI, etc.


Of course every time I purged and started from scratch, it had to create a new zone ID for the root domain, so I had to go back and update my registrar with the new nameservers because each AWS zone ID is associated with a different set of resolvers.  Meanwhile our email, website, API etc were all unresolvable.


If we were in production, this would have been one of the worst outages of my career, and that’s … saying a lot.


if we were really in production that would have been a 16+ hour outage, email, www, everything, and i was *only adding staging envs*— Charity Majors (@mipsytipsy) [March 18, 2016](https://twitter.com/mipsytipsy/status/710803216733048832?ref_src=twsrc%5Etfw)


So … Hi!  I learned a bunch of things from this.  And I am *SO GLAD* I got to learn them before we have any customers!


## The lessons learned


(in order of least important to most important)


### 1. Beware of accidental duplicates.


It actually really pisses me off how easily you can just nonchalantly and unwaryingly create a duplicate VPC or Route53 zone with the same name, same delegation, same subnets, etc.  Like why would anyone ever WANT that behavior?  I blame AWS for this, not Hashicorp, but jesus christ.


So that’s going on my “Wrapper Script TODO” list: literally check AWS for any existing VPC or Route53 zone with the same name, and bail on dupes in the plan phase.


(And by the way — this outage was hardly the first time I’ve run into this.  I’ve had tf  unexpectedly spin up duplicate VPCs many, many, many times.  It is *not* because I am running apply from the wrong directory, I’ve checked for any telltale stray .terraforms.  I usually don’t even notice for a while so it’s hard to figure out what exactly I did to cause it, but definitely seems related to applying modules or subsets of a full run.  Anyway, I am literally setting up a monitoring check for duplicate VPC names which is ridiculous but whatever, maybe it will help me track this down.)


(Also, I really wish there was a $TF_ROOT.)


### 2. Tag your TF-owned resources, and have a kill script.


This is one of many great tips from [@knuckolls](http://twitter.com/knuckolls) that I am totally stealing.  Every taggable resource that’s managed by terraform, give it a tag like “Terraform: true”, and write some stupid boto script that will just run in a loop until it’s successfully terminates everything with that tag + maybe an env tag.  (You probably want to explicitly exclude some resources, like your root DNS zone id, S3 buckets, data backups.)


But if you get into a state where you *can’t* run terraform destroy, but you *could* spin up from a clean slate, you’re gonna want this prepped.  And I have now been in that situation at *least* four or five times not counting this one.  Next time it happens, I’ll be ready.


Which brings me to my last and most important point — actually the whole reason I’m even writing this blog post.  (she says sheepishly, 1000 words later.)


### 3. Use separate state files for each environment.


Sorry, let me try  this again in a font that better reflects my feelings on the subject:


USE SEPARATE STATE FILES.


FOR EVERY ENVIRONMENT.


This is about limiting your blast radius.  Remember: this whole thing started when I made some simple changes to *staging.*


To ***STAGING**.*


But all my environments shared a state file, so when something bad happened to that state file they all got equally fucked.


**If you can’t safely test your changes in isolation away from prod, you don’t have infrastructure as code.**


Look, you all know how I feel about terraform by now.  I love composable infra, terraform is the leader in the space, I love the energy of the community and the responsiveness of the tech leads.  I am hitching my wagon to this horse.


It is still as green as the motherfucking Shire and you should assume that every change you make could destroy the world.  So your job as a responsible engineer is to add guard rails, build a clear promotion path for validating changesets into production, and limit the scope of the world it is capable of destroying.  This means separate state files.


So Monday I sat down and spent like 10 hours pounding out a version of what this could look like.  There aren’t many best practices to refer to, and I’m not claiming my practices are the bestest, I’m just saying I built this thing and it makes sense to me and I feel a lot better about my infra now.  I look forward to seeing how it breaks and what kinds of future problems it causes for me.


just spent 10 hours refactoring ~4k lines of terraform but now i have VPC environments & isolated state files & modularized everything from— Charity Majors (@mipsytipsy) [March 29, 2016](https://twitter.com/mipsytipsy/status/714699980288704512?ref_src=twsrc%5Etfw)

the vpc and routes and peering and public dns up to databases and ASGs and bootstrapping and sw deploy and i am so stupidly happy right now— Charity Majors (@mipsytipsy) [March 29, 2016](https://twitter.com/mipsytipsy/status/714700266881294340?ref_src=twsrc%5Etfw)


## HOWTO: Migrating to multiple state files


### Previous config layout, single state file


If you want to see some filesystem ascii art about how everything was laid out pre-Monday, here you go.


Basically: we used s3 remote storage, in a bucket with versioning turned on.  There was a top-level .tf file for each environment {production,dev,staging}, top-level .tf files for env-independent resources {iam,s3}, and everything else in a module.


Each env.tf file would call out to modules to build its VPC, public/private subnets, IGW, NAT gateway, security groups, public/private route53 subdomains, an auto-scaling group for each service (including launch config, int or ext ELB, bastion hosts, external DNS, tag resources, and so forth.


### **New config layout, with state file per environment**


In the new world there’s one directory per environment and one base directory, each of which has their own remote state file (you source the init.sh file to initialize a new environment, after that it just works if you run tf commands from that directory).  “Base” has a few resources that don’t correspond to any environment — s3 buckets, certain IAM roles and policies, the root route53 zone.


Here’s an ascii representation of the new filesystem layout:


All env subdirectories have a symlink to ../variables.tf and ../initialize.tf.  Variables.tf declares has the default variables that are shared by all environments — things like


```
$var.region, $var.domain, $var.tf_s3_bucket
```


Initialize.tf contains empty variable declarations for the variables that will be populated in each env’s .tfvars file, things like like


```
$var.cidr, $var.public_subnets, $var.env, $var.subdomain_int_name
```


Other than that, each environment just invokes the same set of modules the same way they did before.


The thing that makes all this possible?  Is this little sweetheart, [terraform_remote_state](https://www.terraform.io/docs/providers/terraform/r/remote_state.html):


```
resource "terraform_remote_state" "master_state" {
  backend = "s3"
  config {
    bucket = "${var.tf_s3_bucket}"
    region = "${var.region}"
    key = "${var.master_state_file}"
  }
}

```


It was not at all apparent to me from the docs that you could not only store your remote state, but ***also query values from it**.**  ***So I can set up my root DNS zones in the base environment, and then ask for the zone identifiers in every other module after that.


```
module "subdomain_dns" {
  source = "../modules/subdomain_dns"
  root_public_zone_id = "${terraform_remote_state.master_state.output.route53_public_zone}"
  root_private_zone_id = "${terraform_remote_state.master_state.output.route53_internal_zone}"
  subdomain_int = "${var.subdomain_int_name}"
  subdomain_ext = "${var.subdomain_ext_name}"
}

```


**How. Fucking. Magic. is that.**


SERIOUSLY.  This feels so much cleaner and better.  I removed hundreds of lines of code in the refactor.


(I hear Atlas doesn’t support symlinks, which is unfortunate, because I am already in love with this model.  If I couldn’t use symlinks, I would probably use a Makefile that copied the file into each env subdir and constructed the tf commands.)


### **Rolling it out**


Switching from single statefile to multiple state files was by far the trickiest part of the refactor.  First, I started by building a new dev environment from scratch just to prove that it would work.


Second, I did a “terraform destroy -target=module.staging”, then recreated it from the env_staging directory by running “./init.sh ; terraform plan -var-file=./staging.tfvars”.  Super easy, worked on the first try.


For production and base though, I decided to try doing a **live migration** from the shared state file to separate state files without any production impact.  This was mostly for my own entertainment and to prove that it could be done.  And it WAS doable, and I did it, but it was preeeettty delicate work and took about as long as literally everything else combined. (~5 hours?).  Soooo much careful massaging of tfstate files.


(Incidentally, if you ever have a syntax error in a 35k line JSON file and you want to find what line it’s on, I highly recommend [http://jsonlint.com](http://jsonlint.com).  Or perhaps just reconsider your life choices.)


#### Stuff I still don’t like


There’s too much copypasta between environments, even with modules.  Honestly, if I could pass around maps and interpolate


```
$var.env
```


into every resource name, I could get rid of _so_ much code.  But Paul Hinze says that’s a bad idea that would make the graph less predictable and he’s smarter than me so I believe him.


### TODO


There is lots left to do, around safety and tooling and sanity checks and helping people not accidentally clobber things.  I haven’t bothered making it safe for multiple engineers  because right now it’s just me.


This is already super long so I’m gonna wrap it up.  I still have a grab bag of tf tips and tricks and “things that took me hours/days to figure out that lots of people don’t seem to know either”, so I’ll probably try and dump that out too before I’ve moved on to the next thing.


Hope this is helpful for some of you.  Love to hear your feedback, or any other creative ways that y’all have gotten around the single-statefile hazard!


P.S. Me after the refactor was done =>


i'm like floating on air i'm so high, so just gonna pose with my chompy pal and my flask and get my ass home [pic.twitter.com/hvgqlrj3Ex](https://t.co/hvgqlrj3Ex)— Charity Majors (@mipsytipsy) [March 29, 2016](https://twitter.com/mipsytipsy/status/714701330988863488?ref_src=twsrc%5Etfw)
