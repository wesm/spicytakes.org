---
title: "Hardware Clocks on AWS, SIMD Explored, Distributed Transactions Without XA, and more..."
subtitle: "AWS Time Sync gets microsecond accuracy and hardware clocks; I discover AWS Nitro; A brief overview of SIMD; and the Epoxy paper explores distributed transactions without XA."
date: 2023-11-20T11:24:31+00:00
url: https://materializedview.io/p/ptphc-ntrio-aws-simd-explored-epoxy-transactions
slug: ptphc-ntrio-aws-simd-explored-epoxy-transactions
word_count: 949
---


## AWS Time Sync in Microseconds


Amazon Web Services added microsecond-level accuracy toTime Sync Servicelast week.


> Today, we announced thatwe improved the Amazon Time Sync Serviceto microsecond-level clock accuracy on supported Amazon EC2 instances.


Time Sync now runs with double-digit microsecond accuracy. Amazon, somewhat cryptically, explains why you should care:


> These clocks can be used to more easily order application events, measure 1-way network latency, increase distributed application transaction speed, and incorporate in-region and cross-region scalability features while also simultaneously simplifying technical designs.


Reasoning about time globally is really helpful for distributed systems. I first came across the idea of a global GPS (and atomic) clock inSpanner: Google’s Globally-Distributed Databaseand its concept ofTrueTime.


> TrueTime is a highly available, distributed clock that is provided to applications on all Google servers. TrueTime enables applications to generate monotonically increasing timestamps: an application can compute a timestamp T that is guaranteed to be greater than any timestamp T' if T' finished being generated before T started being generated.


You automatically get improved accuracy if you’re using NTP with Time Sync. AWS’s public NTP server (time.aws.com) also received the update.(Aside: Here’s alist of NTP serversfrom Google, Facebook, Cloudflare, Apple, and more.)


You’ll need to use aprecision time protocol (PTP)client to get microsecond granularity. For those unfamiliar, Meta introduces PTP inHow Precision Time Protocol is being deployed at Meta. AWS’spostdemonstrates instance configuration with its PTP Hardware Clock (PHC).


## Time Sync on Nitro


Time Sync’s improved precision is made possible byAWS Nitro.


> The new PHC device is part of the AWS Nitro System, so it is directly accessible on supported bare metal and virtualized Amazon EC2 instances without using any customer resources.


Nitro provides AWS building blocks to assemble different hardware profiles easily. One such building block is a hardware clock card. Nitro has been around for years, but I had no idea (I’m teamGCP).


My reaction to Nitro was, “So, like, ISA, VLB, and PCI slots?” Conceptually, yes. Concretely, no. There’s a heavy focus on security and isolation. Learn more here:


## SIMD Explainer


I spent time this week learning aboutSingle instruction, multiple data (SIMD). Rust’sBeginner’s Guide to SIMDis a good introduction.


> SIMD stands forSingle Instruction, Multiple Data. In other words, SIMD is when the CPU performs a single action on more than one logical piece of data at the same time. Instead of adding two registers that each contain onef32value and getting anf32as the result, you might add two registers that each containf32x4(128 bits of data) and then you get anf32x4as the output.


Here’s what SIMD looks like in practice (n.b. Brandeis’sCS146aexample is from 2015):


```
// simd.rs
#![feature(core)]

use std::simd::f32x4;

fn main() {
    // create simd vectors
    let x = f32x4(1.0, 2.0, 3.0, 4.0);
    let y = f32x4(4.0, 3.0, 2.0, 1.0);

    // simd product
    let z = x * y;

    // like any struct, the simd vector can be destructured using `let`
    let f32x4(a, b, c, d) = z;

    println!("{:?}", (a, b, c, d));
}
```


Why is SIMD a big deal? Matrix operations are useful—something I wish I knew when taking Linear Algebra in college—particularly for vector search andrunning LLMs on CPUs. Elastic Search talks about their usage inAccelerating vector search with SIMD instructions:


> At the heart of Lucene's vector search implementation lie three low-level primitives used when finding the similarity between two vectors: dot product, square, and cosine distance.


Video games and DSP havebenefited from SIMD for years.


> …nearly every modern video game console since 1998 has incorporated a SIMD processor somewhere in its architecture


There are all kinds of other applications, too. Common array operations likesorting,filtering, andsearchingare all optimizable with SIMD.


## Paper Highlight: Epoxy


I had the chance to talk toPeter KraftandQian Liearlier this year. At the time, we spoke aboutApiary, a transactional function-as-a-service (FaaS) platform. Since then, they’ve published a VLDB ‘23 paper,Epoxy: ACID Transactions Across Diverse Data Stores.


Epoxy is a protocol for providing transactions across heterogeneous data stores. The protocol solves the same problem asX/Open XAwith two improvements:

1. Epoxy does not require data stores to implement any protocol, itself.
2. Unlike X/Open XA, Epoxy provides transactional isolation, not just atomicity.


Epoxy requires a “shim” in front of each data store. The shims manage transactional isolation and work with a transaction coordinator to ensure atomic commits.


![](https://substackcdn.com/image/fetch/$s_!68iH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F821c3513-62f2-4dc2-8902-383181cad0b1_902x448.png)


Murat Demirbaswrite agood blog poston the transaction protocol.


Epoxy isn’t without tradeoffs, though. All systems interacting with an Epoxy’d table must do so through the Epoxy shim. At least one system—the coordinator—must provide transactions; this is usually an RDBMS like PostgreSQL or MySQL. Transactions also require some client code:


```
def reserve (hotelId, customerData):
  ctxt = epoxy.beginTransaction()

  # Check room availability in Postgres.
  res = pg.query("SELECT avail FROM Hotels WHERE hotel = hotelId")

  if res == 0:
    epoxy.commitTransaction (ctxt)
    return false # No room available.

  # Update availability in Postgres.
  pg.update("UPDATE Hotels SET avail = res −1 WHERE hotel = hotelId")

  # Make a reservation in MongoDB.
  epoxy.update(
    context = ctxt,
    secondary = mongo,
    key = hotelId,
    record = customerData)

  epoxy.commitTransaction(ctxt)
  return true
```


Client code like this is pretty standard, but it’s still something to be aware of.


Peter and Qian have founded a startup,DBOS. They are working onOperon, “A Typescript framework built on databases.” Operon’s API looksinterseting; it’s got a lot of decorators.


## More Awesome Infrastructure


Keep up with new projects as they’re added to theawesome-infraGithub repo. New projects and startups welcome! SeeCONTRIBUTING.mdand thePR template.

- AutoMQ- Cloud native implementations of Kafka and RocketMQ.
- Kafka- An open-source distributed event streaming platform.


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
