---
title: "S3 Is Showing Its Age"
subtitle: "I'm squarely in the trough of disillusionment with S3."
date: 2024-05-22T18:17:46+00:00
url: https://materializedview.io/p/s3-is-showing-its-age
slug: s3-is-showing-its-age
word_count: 771
---


There’s no denying that S3 is a feat of engineering.Building and Operating a Pretty Big Storage Systemis a top-tier technology flex. But S3’s feature set is falling behind its competitors. Notably, S3 has no compare-and-swap (CAS) operation—something every single other competitor has. It also lacks multi-region buckets and object appends. EvenS3 Expressis proving to be lackluster.


These missing features haven’t mattered much for data lakes and offline use cases. But new infrastructure is using object storage as their primary persistence layer—somethingI’mexcitedabout. Here, S3’s feature gaps are a bigger problem.


![](https://substackcdn.com/image/fetch/$s_!kz5U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9778383-6a7b-4b24-bf1f-ef5543d9e0f0_1370x428.png)

*View Post*


## Missing Preconditions


Preconditions (also known ascompare-and-swap(CAS), conditionals, If-None-Match, If-Match, and so on) allow a client to write an object only if a certain condition is met. A client might wish to write an object only if it doesn’t exist, or update an object only if it hasn’t changed since the client last read it. CAS makes this possible. Such operations are used often for locks and transactions in distributed systems.


![](https://substackcdn.com/image/fetch/$s_!QBu2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf515bfe-eeb5-4222-88f9-1c547dc7ca39_1394x288.png)

*View Post*


S3 is the only object store that doesn’t support preconditions. Every other object store—Google Cloud Storage(GCS),Azure Blob Store(ABS), CloudflareRidiculously Reliable(R2) storage,Tigris,MinIO—all have this feature.


Instead, developers are forced to use a separate transactional store such asDynamoDBto enforce transactional operations. Building a two-phase write between DynamoDB and S3 is not technically difficult, but it’s annoying andleads to ugly abstractions.


## S3 Express One Zone Isn’t S3


I wasreally excitedabout S3 Express One Zone (S3E1Z) when it first came out. The more time I spend with it, the less impressed I am. The first wart that surfaced was a newdirectory buckettype, which Amazon introduced for Express.


![](https://substackcdn.com/image/fetch/$s_!lwgC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80fcc8e0-ecfd-447e-b195-44f4b1db2c98_684x134.png)

*View Post*


But the gaps don’t stop here. S3E1Z ismissing atonof standard S3 featuresincluding object version support, bucket tags, object locks, object tags, and MD5 checksum ETags. Thecomplete listis pretty staggering.


![](https://substackcdn.com/image/fetch/$s_!E0R-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65afc429-9f2d-444f-a32f-7566f2d6d056_1376x386.png)

*View Post*


S3E1Z buckets can’t be treated like a normal S3 buckets. As with CAS operations, developers must design around these deficiencies. And because S3E1Z is not multi-zonal, developers are left to buildquorum writesto multiple availability zones for higher availability.


Factor in S3E1Z’s high storage cost of $0.16/gig—twice elastic block store’s (EBS)  general purpose SSD (gp3) cost—and S3E1Z looks more like an expensive EBS with a half-implemented S3 API.


## No Dual-Region/Multi-Region Buckets


S3’s availability feature gaps go beyond S3E1Z. S3 doesn’t have dual-region or multi-region buckets. Such buckets are useful for higher availability. Google offersa wide range of optionsin this area.


![](https://substackcdn.com/image/fetch/$s_!fCH2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2600270f-f155-4194-991f-d13909abb629_1446x1096.png)

*Data Availability | Google Cloud Storage*


While not a must-have, higher availability buckets are certainly nice to have.


## Embracing Reality


The dream is that developers are offered an object store with all of these features: low latency, preconditions, dual-region/multi-region, and so on. But we live in reality, where engineers face a choice: abandon S3 or build around these gaps.


Turbopufferis my favorite example of a company that’s gone all-in on abandoning S3.


![](https://substackcdn.com/image/fetch/$s_!Wru1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1aaa20dc-30f7-45ae-969d-c08770d95538_1376x334.png)

*View Post*


The gamble they’ve made is that S3 will eventually get preconditions. This gamble seems reasonable since Amazon has all of the required building blocks (DynamoDB and S3) and every competitor is beating them here. I’m making the same gamble with thecloud native LSM I’m working on.


The challenge with this approach is inter-cloud network cost. All cloud providers charge for network egress. Data transferred to infrastructure running outside amazon web services (AWS) will incur network egress fees. But the inter-cloud cost for AWS users isn’t as bad as you might think.Simon Eskildsen, Turbopuffer’s founder and CEO, haswritten about this extensively.


![](https://substackcdn.com/image/fetch/$s_!2l6a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec92195c-3c7a-4a8c-8dd8-80c3f9070358_1510x782.png)

*Turbopuffer FAQ*


The benefit of this is that Turbopuffer has built a beautiful and minimalist design withjust three components: a Turbopuffer binary, a RAM/SSD cache, and Google Cloud Storage.


For many, this will seem extreme. The alternative is to house metadata in a transactional store outside of S3.


![](https://substackcdn.com/image/fetch/$s_!rvAD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66c0de8f-5971-42cf-a0ba-f877ed678d8b_1390x728.png)

*View Post*


Once you open yourself up to a separate metadata plane, you’ll find other use cases for it. The path to theslope of enlightenmentis to recognize that S3 is an object store not a file system. By embracing DynamoDB as your metadata layer, systems stand to gain a lot.


Ultimately, the decision to abandon S3 or embrace its shortcomings depends on a system’s use cases and design goals. Preconditions on S3 and a unified S3E1Z API would make this decision a lot easier, though.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
