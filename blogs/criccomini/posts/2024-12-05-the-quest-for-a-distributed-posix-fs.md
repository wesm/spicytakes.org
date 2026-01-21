---
title: "The Quest for a Distributed POSIX-Compatible Filesystem"
subtitle: "Distributed POSIX filesystems have proven elusive, but we're getting closer. Perhaps that's all we need."
date: 2024-12-05T20:32:46+00:00
url: https://materializedview.io/p/the-quest-for-a-distributed-posix-fs
slug: the-quest-for-a-distributed-posix-fs
word_count: 824
---


Years ago, I was working onApache SamzawithJay Kreps. At one point during a discussion about Samza’s state management system, Jay turned to me and said, “You know, we wouldn’t need any of this if we had a distributed filesystem that worked.” A scalable remote filesystem with normalPOSIXsemantics would let us build distributed systems that were stateless services; we could use the distributed filesystem to store everything. This comment stuck with me and I still think about it a lot.


Alas, we didn’t have such a system at the time. But object storage systems likeS3have grown to give us all the properties we need; they areinsanely scalableand provideatomic operationsneeded for transactional workloads. Object stores are still missing POSIX semantics, though. You can’t take any old system that uses filesystem I/O libraries and use S3 as its storage layer.


In the absence of a POSIX API for S3, two approaches have emerged to leverage what object stores have to offer . The first is building S3 directly into the systems, which most database and streaming companies are doing.Neon,WarpStream,Turbopuffer, andResponsive﹩ are all in this category. The other is to wrap S3 in afilesystem in userspace(FUSE) interface or an NFS-based implementation.Amazon S3 File Gateway,JuiceFS,s3fs, andGoofysare examples of such an approach. (If you squint,Apache OpenDALfits in this category, but inverts the relationship by wrapping everything in its own API.)


Direct integration requires a storage-layer rewrite. I/O calls must be converted to S3-compatible API calls. Moreover, each system needs to figure out how to deal with higher object storage latencies, a subject I’ve written about before.

[The Cloud Storage Triad: Latency, Cost, Durability](https://materializedview.io/p/cloud-storage-triad-latency-cost-durability)
[Chris Riccomini](https://substack.com/profile/69592459-chris-riccomini)
·
April 22, 2024

I believe that the future of database persistence is object storage—S3, Google Cloud Storage, and so on. New systems like Neon, WarpStream [$], and Turbopuffer persist data in object storage to offer infinite retention, durability, replication, data warehouse integration

[Read full story](https://materializedview.io/p/cloud-storage-triad-latency-cost-durability)

Direct object storage integration makes sense for systems like databases, whose primary job is to store and query data. But for systems, frameworks, and libraries that just need to read and write files as part of a broader workload, rewriting the storage layer for object storage is too burdensome.


FUSE and NFS-based implementations present their own challenges. s3fs and other FUSE-based systems implement only a subset of the POSIX interface, often missing features such as random access writes or appends, metadata operations, atomic renames, hardlinks, and inotify features. Such limitations simply won’t work for many systems and libraries. It’s not clear if RocksDB, for example,can safely be run on EFS. And some implementations, such as JuiceFS, store files in their own block format, which limits interoperability.


The need for scalable filesystems has grown, too. Database and streaming use cases have been around for a long time, but the growth of Kubernetes and AI workloads are new. Kubernetes has made every system distributed. And with AI, multi-modal data such as audio, text, and video is a critical ingredient. Many ML and AI libraries are built with local filesystems, and those that support object storage often don’t have good caching to speed up workloads.


I think we’re finally getting to the point where we have both the technology and the demand to get us what we need: a distributed POSIX-compatible filesystem.Regatta Storageis building in this direction, with a stated goal of replacing EFS andelastic block store(EBS)general purpose(gp3) use cases.


![](https://substackcdn.com/image/fetch/$s_!T0_1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F054d5492-9aba-4c87-8f97-4750c8bcfbee_687x161.png)

*View Post*


Though Regatta doesn’t have complete POSIX compatibility, their offering is compelling. They are using NFS now, and moving to their own protocol. This should give them a lot of flexibility as they try to implement more obscure POSIX features. Even if they never get complete POSIX support, they should be able to get closer than current solutions. Regatta also provides a generic cache to reduce latency, a key ingredient for a disk-like experience. Such an architecture is akin to a generic version of Neon’sSafekeepers and Pageservers, somethingI’ve been dreaming of for a while. Plus, unlike JuiceFS, files appear in object storage as normal files rather than opaque blocks that must be accessed only through the JuiceFS interface.


I expect this area to get more competitive. Much as competition with S3 has driven AWS to improve its offering, I anticipate more EFS features in the future. Other object store providers such asTigris﹩are also well positioned to pursue this area. JuiceFS and Alluxio will also continue to make progress, too. AI-specific offerings could also emerge. Fortunately, I think the TAM is big enough (and the use cases diverse enough) to support winners for different use cases, even if the underlying technology is largely the same.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
