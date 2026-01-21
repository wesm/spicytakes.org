---
title: "Virtual Machines Are Getting Better"
subtitle: "Unikernels, GPU checkpointing, and VM migration are going to reshape the cloud."
date: 2024-10-23T12:11:17+00:00
url: https://materializedview.io/p/virtual-machines-are-getting-better
slug: virtual-machines-are-getting-better
word_count: 510
---


Virtual machines (VMs), containers, and serverless execution models have been around for a while. Until recently, these technologies have offered fairly generic features. Consequently, theykind ofwork for many use cases, buttrulywork for relatively few.


Microservices, serverless functions, AI, batch computation, stateful services, and other use cases all need special features to work well. Serverless functions need fast start times, AI and LLM workloads need GPUs, and many use cases could benefit from better state snapshotting technology. Yet, serverless functions suffer from high cold startsbetween 100ms and 1 second. Snapshots are slow, and only migrate certain pieces of state such as memory, while leaving other pieces, such as GPU state or network addresses behind. And GPU support in these execution models is spotty at best.


VM snapshots are useful when recovering from a failure or migrating execution to a new machine. Moving your workload to a different machine (or cloud) could save money, unlock better GPUs, or speed up training and inference.Cedana﹩,Modal﹩, andMicrosofthave beenworking on this problemfor some time.


This is why I’m excited to see a spate of recent developments that target cold start, snapshot, and GPU requirements.


GPU features are evolving quickly.gVisoradded GPU supportlast year,NVIDIArecently open sourced theircuda-checkpointtool, andFirecrackerhad a meetingon October 9th, 2024 to discuss GPU support.


NVIDIA’s cuda-checkpoint is particularly important.CUDAoffers GPU APIs meant for generic computation (not gaming). Such APIs are widely used in AI models and LLMs. As developers execute operations on a GPU, the GPU’s memory accumulates state. This GPU data is very difficult to read directly, which poses a problem if you wish to snapshot a machine’s state. Now cuda-checkpoint offers a simple, bare-bones, free tool to do GPU checkpoint and recovery.


For serverless functions,unikernelssuch asUnikraftnow boastsingle digit boot timesandfast snapshotting. This should enable faster cold starts and scale-to-zero, which will result in cost savings. Many unikernels toutincreasedsecurityin multi-tenant environments, as well. As unikernels addKubernetessupport, I expect adoption to increase, so non-serverless workloads like microservices will benefit. I’ve also heard there are benefits for specific verticals such as gaming.


Meanwhile,Loophole Labshas launchedArchitectto simplify VM migrations. They’ve built some really slick tech that incrementally snapshots and migrates both memory state and network bindings between machines. Architect purports to migrate faster than a spot instance preemption occurs, which would allow for huge cost savings for many workloads.


These developments will have a big impact on how we think about the cloud. We will, for example, see more multi-cloud adoption as state is easier to migrate and GPUs are harder to come by.Yingjun Wu(Founder ofRisingWave) pointed me toSkyPilot, aUC Berkeleyproject that offers multi-cloud deployment specifically for AI, LLM, and batch workloads. Serverless functions might supplant service oriented applications, too.Vercelhas been doinggreat work here. These are big shifts with big implications.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
