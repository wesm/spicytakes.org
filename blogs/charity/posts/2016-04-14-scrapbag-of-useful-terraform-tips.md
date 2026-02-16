---
title: "Scrapbag of useful Terraform tips"
date: 2016-04-14
url: https://charity.wtf/2016/04/14/scrapbag-of-useful-terraform-tips/
word_count: 1611
---


After some kinda ranty posts about [terraform](https://charity.wtf/2016/02/23/two-weeks-with-terraform/) and [AWS and networking](https://charity.wtf/2016/03/23/aws-networking-environments-and-you/) and [orchestration life in general](http://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/), it feels like a good time to braindump some helpful tidbits.


Side note — a few people have asked me to open source my terraform config.  I’m actually super open to sharing it, but a) it’s still changing a lot and b) tf modules aren’t really reusable yet.  They just aren’t.  Eventually we’ll reach a maturity point where a tf module library makes sense, but open source tf modules haven’t been super helpful for me and I don’t expect mine will be any better.


I *did* embed a bunch of meaty gists in this post with some of the more interesting configs.  Let me know if you want to see more, I will happily send it to you, I just don’t want to be maintaining an OS repo right now.


So here are a few things that took me minutes, hours, or days to figure out, that hopefully will now take you less time.


### ICMP for security groups


If you want your hosts to be pingable, you have to put this stanza in your security group.  The “from_port = 8” isn’t in the [security group docs](https://www.terraform.io/docs/providers/aws/r/security_group.html); I found it in this [github issue.](https://github.com/hashicorp/terraform/issues/1313)  Not being a networking person myself, I literally never would have guessed it.  If you want to read up more, here’s [more about why.](http://www.networksorcery.com/enp/protocol/icmp/msg8.htm)


```
  ingress {
    from_port = 8 
    to_port = 0 
    protocol = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

```


**Here is a [gist for my bastion security groups](https://gist.github.com/charity/beb44266cadfd935ab6a838bfe917f38).**  Note that all the security groups are in the aws_vpc module, which gets invoked separately by each environment.


Security groups are stackable in VPC, which is glorious.  But most of the time I thought I was having a problem with VPCs or routes or networking, it turned out to be a security group problem, or an interaction between the two.


Since you have no ability to debug AWS networking via normal linux utilities, my best debugging tip for VPC networking is still, when you get really stuck open up ***all*** the SG ports and see if that fixes it.  (Preferably in, you know, a *staging* environment, not prod …)


### Resource description fields != comment fields


Do* not* use your resource description fields as comments about those resources.


It *feels* like they should be comment strings, doesn’t it?  Well, they aren’t.  If you change your “comment” terraform will try to destroy and recreate the resource (which may or may not even work, if it’s like a security group that all your environments and other resources happen to inherit.  Hypothetically speaking.)


This isn’t a Hashicorp thing, it’s an AWS thing.  You can’t go edit the description in the console, either — try it!  It’s like a smelly, lingering remnant of the bad old days before we had tags.


So use tags, or use comments in your code.  Don’t use descriptions for documentation


### Picking VPC ranges


The max # of hosts you can have in any VPC is a /16.  Probably don’t start your numbering with 10.0.0.0/16, just in case you ever want to peer with anyone else, who almost certainly started with 10.0.0.0/16 too.


### Route tables


Only one route table can be associated with each subnet.  (Again, NONE of your routes will show up in netstat -nr or any of the normal Linux tools, which is fucking infuriating.)


I recommend not using [aws_route_table](https://www.terraform.io/docs/providers/aws/r/route_table.html) with an inline blob of routes, but instead using [aws_route](https://www.terraform.io/docs/providers/aws/r/route.html) resources.  These are additive resources, so it gives you more fine-grained control if you want different environments to have different routing tables.


### Peering VPCs


[Peering is so fucking rad](https://www.terraform.io/docs/providers/aws/r/vpc_peering.html).  I’m so, so happy with it.  Peering makes VPC-per-env tractable and flexible and not horribly annoying.


In order to peer VPCs, if you have a separate state file per environment (which you [really should](https://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/)), you will need to [import remote state.](https://www.terraform.io/docs/state/remote/s3.html)  It’s not very obvious from the documentation, but this is an incredibly powerful feature.  It lets you refer to variables from remote state files just like they were modules.


I use S3 for saving state, with versioning turned on for the bucket.


I have a locked-down dev VPC which is automatically peered with all other VPCs and allowed to ssh into them, but can’t connect to any other ports in those VPCs.  (Using security groups, but also [network ACLs for an extra sanity check](https://www.terraform.io/docs/providers/aws/r/network_acl.html).)  And none of the other VPCs are peered with each other, so none of the test or staging or prod environments can accidentally connect to each other.


I ran into a few things while setting up peering.  (Relevant context: I have both 4 public subnets and 4 private NAT subnets for each VPC, one subnet per availability zone.)

- First, like I said, I had to refactor my aws_route_table into a bunch of aws_route resources, because I didn’t want the route tables to look the same for every environment (staging shouldn’t be able to talk to prod but dev should, etc)
- If you own both VPCs, you can set up auto-accept, which is super rad.  If not, someone has to go to the console and click ok somewhere.
- You need to include your “owner id” in the peering config, which confused me for a bit but you just have to log in as the root account and look under billing somewhere.  (I don’t remember where, google it.)
- Second, peering has to be set up in both directions before connections will actually work.  I naively assumed that if it was set up and auto-accepted from VPC-A to VPC-B, connections from VPC-A to VPC-B would work.  Nope!  you also have to establish the peering from VPC-B to VPC-A before either direction will work.
- All public subnets share a single route table, but each private subnet has its own (necessary for NAT).  So I had to set up peering from every single one of the private subnets that I wanted to be able to connect out from.


**Here’s the gist to the networking portion of my [aws_vpc module](https://gist.github.com/charity/28cbb58c913794b225afb8a0fefac542).  **(The rest of the module is mostly just security groups.)


And some sample peering configs (you need one for each VPC, like I mentioned, so it’s bidirectional for each pair).  **Here’s a gist [snippet from the dev side](https://gist.github.com/charity/7858eb05dffb47043e8310087ac4dfa7), and the [paired snippet from the staging side.](https://gist.github.com/charity/2ceebb7e86318a9477178f454dc2c733)**


(You can tell how confident I was in these changes by how I named the resources, and added blamey “Author” tags for a coworker who hadn’t actually started working with me yet.  I don’t think he’s noticed yet, lol.)


### NAT gateways, IGWs


You probably already set up an IGW resource for your public subnets to talk to the internet.  Just add it to every public subnet, easy breezy:


```

resource "aws_internet_gateway" "mod" {
  vpc_id = "${aws_vpc.mod.id}"
  tags { 
    Name = "${var.env}_igw"
  }
}

# add a public gateway to each public route table
resource "aws_route" "public_gateway_route" {
  route_table_id = "${aws_route_table.public.id}"
  depends_on = ["aws_route_table.public"]
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = "${aws_internet_gateway.mod.id}"
}

```


Lots of people seem to still be setting up custom Linux boxes to NAT traffic out from private subnets to the internet.  (A prominent internet service provider had an outage a couple weeks ago because they were doing this.)


Use NAT gateways instead, if you can.  They are basically just like ELBs but for natting out to the internet.  They scale out according to throughput in roughly the same way, up to 10 Gbps bursts.


BUT **MIND THE FUCKING TRAP**.  You do not attach these NAT gateways to your PRIVATE subnets, you attach them to the **PUBLIC FUCKING** **SUBNETS**, and then a route to from the private subnet to that gateway**.**  Gahhhhhh.


```
resource "aws_eip" "nat_eip" {
  count    = "${length(split(",", var.public_ranges))}"
  vpc = true
}

resource "aws_nat_gateway" "nat_gw" {
  count = "${length(split(",", var.public_ranges))}"
  allocation_id = "${element(aws_eip.nat_eip.*.id, count.index)}"
  subnet_id = "${element(aws_subnet.public.*.id, count.index)}"
  depends_on = ["aws_internet_gateway.mod"]
}

# for each of the private ranges, create a "private" route table.
resource "aws_route_table" "private" {
  vpc_id = "${aws_vpc.mod.id}"
  count = "${length(compact(split(",", var.private_ranges)))}"
  tags { 
    Name = "${var.env}_private_subnet_route_table_${count.index}"
  }
}
# add a nat gateway to each private subnet's route table
resource "aws_route" "private_nat_gateway_route" {
  count = "${length(compact(split(",", var.private_ranges)))}"
  route_table_id = "${element(aws_route_table.private.*.id, count.index)}"
  destination_cidr_block = "0.0.0.0/0"
  depends_on = ["aws_route_table.private"]
  nat_gateway_id = "${element(aws_nat_gateway.nat_gw.*.id, count.index)}"
}

```


(Thank you [@ebroder](http://twitter.com/ebroder), I would probably **NEVER** have figured this out on my own.  AWS docs are completely unintelligible on the subject.)


### A note on ELB SGs


Oh … you probably know this, but your ELBs should be in a separate / more permissive SG than the instances backing those ELBs.  You don’t want people to be able to connect directly to e.g. port 80 or 8080 on an application host, bypassing the ELB.


### ELB certificates


If you live in us-east, use the new [AWS certificate manager](https://aws.amazon.com/certificate-manager/).  It’s free and you’ll never have to worry about cert expirations ever ever again.


If you don’t — or if you didn’t notice the announcement LITERALLY A FEW DAYS BEFORE you purchased your own Digicert wildcard cert (wahhhh) — you should just add the cert to your ELB in the console and refer to the ARN in your tf configs, because otherwise your private key will be in the state file.


### Ok that’s it


Yesterday I spun up another whole new VPC clone by adding about 5 lines and copying a couple files + sed -e’ing the name of the environment.  Took about two minutes, felt like a fucking badass.  ^_^


I will now proceed to forget as much as possible about all the things I have learned about networking over the past two months.
