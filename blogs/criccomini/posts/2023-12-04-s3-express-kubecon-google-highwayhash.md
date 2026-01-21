---
title: "What the Internet Says About S3 Express, the Best Talk at Kubecon, HighwayHash, and More..."
subtitle: "Amazon breaks infrastructure Twitter with S3 Express; Stateful VM live migrations with Architekt; and I highlight Google's SIMD-optimized hashing algorithm."
date: 2023-12-04T11:32:24+00:00
url: https://materializedview.io/p/s3-express-kubecon-google-highwayhash
slug: s3-express-kubecon-google-highwayhash
word_count: 881
---


## S3 Express One Zone Roundup


You’ve probably seen AWS’sS3 Express One Zone. Express is a new S3 storage class that features low latency (<10ms) access in a single availability zone. There have been plenty of takes. Rather than offer mine, I’ll share what others are saying.


> My feeling on S3 Express One Zone is it’s the right technology, at the right time with the wrong price.


— Jack Vanlightly,S3 Express One Zone, Not Quite What I Hoped For


> …the new storage class does open up an exciting new opportunity for all modern data infrastructure: the ability to tune an individual workload for low latency and higher cost or higher latency and lower costwith the exact same architecture and code.


— Richie Artoul [$],S3 Express is All You Need(HN comments)


> A more subtle point is that it could allow you to build systems that can transparently change to lower cost + higher latency, or higher cost + lower latency.


— Stanislav Kozlovski,Twitter


> Stream processing is an important aspect I believe S3 Express will greatly disrupt. Flink-like systems bring Data to the Query, whereas OLAP engines like Pinot bring Query to Data.


— Ananth Packkildurai,Thoughts on Amazon Express One and its impact in Data Infrastructure


Amazon has also posted some customer testimonial posts fromlakeFS,Clickhouse, and afew others.


Personally, I’m speedrunning the hype cycle wave and living in the trough of disillusionment right now. I agree with Jack’s take. Express is a helpful building block, but it doesn’t change storage architectures much. We still need caches and write-ahead logs (WALs) in front of S3 to reduce cost and keep high availability.


I’m curious whether express supportsS3 replication. I’m not 100% sure if this works; let me know if you’ve tried it. I also wonder whether Express will be incorporated intoS3 Intelligent-Tiering.


I’ve been cheerleading S3-as-primary-storagefor a while now. It’s great to see AWS show some love to this use case. I expect to see more products like this.


## Zero Downtime Live Migration of Stateful VMs


Richie Artoul sent me this talk with, “Watch this when you get time. It’s absolutely nuts.” He wasn’t kidding. I’m toldFelicitas Pojtinger’s talk received a standing ovation at Kubecon.


In Zero-Downtime Live Migration of Stateful VMs on Kubernetes, Felicitas explains howLoophole Labsbuilt a way to do live migrations usingnetwork block device(NDB) protocol. Loophole’sr3mapandarchitektcombine to provide VM live migrations.


Why is this important? Look no further thanmy last post, where I mentioned Neon’s QEMU usage.


> I hadn’t come across QEMU before (orDRDB, which Jack also mentions). Neon chose QEMU—a full VM—overFirecrackerbecause they wantedlive migration. Firecracker andgVisorboth only support snapshot and restore.


With r3map, microVMs like Firecracker and gVisor can now support live migrations just like heavier-weight VMs. Loophole haspatched Firecrackerto prove it.


Felicitas lists other use cases, too:

- Moving VMs to the edge (near customers, or even on their devices)
- Moving long-running processes to more powerful servers (ML/AI)
- Moving long-running processes between cloud providers (hybrid cloud)
- Moving VMs from/to local laptops for deployment and debugging


ML/AI process migration is of particular interest to me. Microsoft and Facebook have had this technology for a while (c.f.Singularity: Planet-Scale, Preemptive and Elastic Scheduling of AI Workloads). GPUs and compute are hard to come by.Cedana[$] is another company working on this problem.


## Project Highlight: HighwayHash


HighwayHashis a pseudo-random hashing library from Google. The library actually contains two algorithms:SipHashand HighwayHash. HighwayHash is SIMD-optimized andextremelyfast.


> HighwayHash is a new pseudo-random function based on SIMD multiply and permute instructions for thorough and fast hashing. It is 5.2 times as fast as SipHash for 1 KiB inputs.


I’ve beenpoking at SIMD recently. It’s neat to see a hash function using it.


Google’s also got a paper about their work:Fast keyed hash/pseudo-random function using SIMD multiply and permute. A notable caveat from the paper:


> We are not experienced cryptographers, and do not see a way to reduce the HighwayHash algorithm to provably secure constructions. This multiply-permute scheme may require new methods of cryptanalysis. In the absence of a formal proof, we rely on statistical testing


I came across HighwayHash while watching Felicitas’s stateful VM migration presentation. Loophole Labs usedMinIO’s pure-Go implementationto do file-based synchronization (think rsync or BitTorrent) when experimenting with stateful migrations.


## More Awesome Infrastructure


Keep up with new infrastructure projects as they’re added toawesome-infra. New submissions are welcome!

- Doris- Apache Doris is an easy-to-use, high performance and unified analytics database.
- Druid- Apache Druid: a high performance real-time analytics database.
- Firecracker- Firecracker is an open source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services that provide serverless operational models.
- gVisor- gVisor is an application kernel, written in Go, that implements a substantial portion of the Linux system surface.
- KVM- KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V).
- QEMU- QEMU is a generic and open source machine & userspace emulator and virtualizer.
- Virtualbox- VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.


---


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
