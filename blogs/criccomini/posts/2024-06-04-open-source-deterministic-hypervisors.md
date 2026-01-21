---
title: "Open Source Deterministic Hypervisors Are Coming"
subtitle: "And Antithesis should open source theirs."
date: 2024-06-04T21:45:54+00:00
url: https://materializedview.io/p/open-source-deterministic-hypervisors
slug: open-source-deterministic-hypervisors
word_count: 734
---


I’m key noting atPrefect Summit 2024[$]. My talk, (tentatively) titled 5 infrastructure trends in 20 minutes, is a whirlwind tour the things I’ve been writing about on Materialized View.Register hereto check it out! The conference is virtual, totally free,  and includes talks from Prefect, Block, and Cox Automotive.


---


Deterministic simulation testing(DST) is a hot topic. With DST, Developers constrain their software so that it can be executed deterministically (the same inputs always produce the same outputs). Next, developers run multiple iterations of their tests with different inputs—usually randomized—to find unexpected behavior. When a failure occurs, developers can re-run the tests with the failed input to reproduce and debug the failure. Resonate’s blog has agood description:


> Deterministic simulation testing repeatedly executes an application in a simulated environment under changing initial conditions, monitoring that the correctness constraints are maintained across executions.


Traditionally, developers have had to write their software deterministically to do DST. This is a tall order; random numbers, clocks, network latency, hardware faults, and process scheduling must all be managed by the developers. I wrote at length about this in the a post last November:

[Viewstamped Replication in Go, Deterministic Testing at Dropbox, FoundationDB's Simulation, and more...](https://materializedview.io/p/viewstamped-replication-deterministic-simulation)
[Chris Riccomini](https://substack.com/profile/69592459-chris-riccomini)
·
November 9, 2023

View Stamped Replication in Go Joran Dirk Greef (of Tigerbeetle [$]) has me on the Viewstamped Replication band wagon. Viewstamped Replication is a consistency algorithm that predates Paxos and Raft. See Joran’s lovely talk for more details on it. There seem to be relatively few actual implementations. I’ve only seen

[Read full story](https://materializedview.io/p/viewstamped-replication-deterministic-simulation)

Still, companies such asDropbox,Resonate,TigerBeetle[$],Polar Signals,FoundationDB, and others have deemed the benefit of DST to outweigh the burden of implementing it.


ThenAntithesiscame out of stealthand completely upended the space. Antithesis built a hypervisor that gives them complete control of a container’s execution. In effect, the hypervisor makes an entire container deterministic; the code inside doesn’t have to be modified since all system calls are managed deterministically. Antithesis’s design is ground breaking. Developers can now take any containerized code and run it deterministically on Antithesis. DST for the masses.


That’s the promise at least. In practice, Antithesis is still getting off the ground.  Thereare a surprising amount of companiesusing Antithesis, but I’ve heard more than one complaint about its cost and integration complexity. These two issues are likely related. Integration is hard so Antithesis has to hand hold its customers. Hand holding is expensive so the bill goes up. I’m told quotes can reach ~$200,000. There’s no doubt in my mind that their product is worth well north of $200,000 for a large company selling infrastructure to hundreds of customers. For early stage startups, it’s a tough sell.


![](https://substackcdn.com/image/fetch/$s_!gixS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ff08520-bfab-466e-879d-a74b9993f35e_1388x402.png)

*View Post*


I fully expect Antithesis’s price to come down as integration is simplified. And they’ve already announced anopen source giveaway programto alleviate some of the problem.


In the meantime, developers are searching for alternatives.Utkarsh Srivastavaishacking on a deterministic hypervisor for QEMU;Polar Signalsmodified Go’s runtimefor non-determinism; and Meta has a (maintenance-mode) projectcalled “Hermit”, which forces deterministic execution in a container. Building a non-deterministic hypervisoris just too juicy of a problem. There will be open source implementations (Heck, Hermit already exists!).


Unrelated to any of this, there was some drama last week aroundWarpStream’s [$] Benthos forkfollowingRedpanda’spurchase, “Redpanda Connect” rebranding, and some license changes.Jay Kreps, CEO and co-founder ofConfluent, posted adetailed threadthat included this tweet:


![](https://substackcdn.com/image/fetch/$s_!jb3F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5558829-5177-4396-a052-e841e17488da_692x164.png)

*View Post*


Jay’s post got me thinking about Antithesis. I think they should open source their hypervisor.


![](https://substackcdn.com/image/fetch/$s_!pIC5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68acbdf7-12ac-4518-86ec-cbf867ccb4c4_695x169.png)

*View Post*


Yes, it’s a novel innovation, but it seems inevitable that there will be open source implementations. Most of Antithesis’s value isn’t in their hypervisor anyway. The tools to mock other systems (such as AWS), the “Software Explorer” that tests different code paths, thelog aggregationanddebugging features; these are the most valuable parts of Antithesis. And open sourcing their hypervisor could accelerate its development, thereby dropping the integration complexity. This is something Hermitstruggled with:


> There is a long tail of unsupported system calls that may cause your program to fail while running under Hermit.


Shortly aftermy post, Antithesis confirmed what I’d been hoping:


![](https://substackcdn.com/image/fetch/$s_!T6N4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e2a182f-d8e8-494b-8994-9ac431bbdfb4_1378x236.png)

*View Post*


This is exactly right! I’m not surprised that they haven’t yet open sourced the hypervisor; there’s still alpha to squeeze from it. Running an open source project is no small task either. But I’m very excited to hear it’s on their minds, and they’re planning to open up their hypervisor.
