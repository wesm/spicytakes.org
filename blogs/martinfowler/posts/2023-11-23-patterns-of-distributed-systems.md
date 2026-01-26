---
title: "Catalog of Patterns of Distributed Systems"
description: "Distributed systems provide a particular challenge to program. They often     require us to have multiple copies of data, which need to keep synchronized.     Yet we cannot rely on processing nodes wo"
date: 2023-11-23T00:00:00
url: https://martinfowler.com/articles/patterns-of-distributed-systems/
slug: patterns-of-distributed-systems
word_count: 735
---


# Catalog of Patterns of Distributed Systems


23 November 2023


Distributed systems provide a particular challenge to program. They
      often require us to have multiple copies of data, which need to keep
      synchronized. Yet we cannot rely on processing nodes working reliably, and
      network delays can easily lead to inconsistencies. Despite this, many
      organizations rely on a range of core distributed software handling data
      storage, messaging, system management, and compute capability. These
      systems face common problems which they solve with similar solutions.


In 2020 I began collecting these solutions as patterns, publishing them
      on this site as I developed them. In 2023 these were published in the book
      [Patterns of Distributed
      Systems](https://martinfowler.com/books/patterns-distributed.html). On this site I now have short summaries of each pattern, with
      deep links to the relevant chapters for the online eBook publication on
      oreilly.com (marked on this page with [).](https://learning.oreilly.com/library/view/patterns-of-distributed/9780138222246)


## [Clock-Bound Wait](clock-bound-wait.html)Â Â


Wait to cover the uncertainty in time across cluster nodes before 
          reading and writing values so that values 
          can be correctly ordered across cluster nodes.


## [Consistent Core](consistent-core.html)Â Â


Maintain a smaller cluster providing stronger consistency to allow the large data cluster to coordinate server activities without implementing quorum-based algorithms.


## [Emergent Leader](emergent-leader.html)Â Â


Order cluster nodes based on their age within the cluster to allow
            nodes to select a leader without running an explicit election.


## [Fixed Partitions](fixed-partitions.html)Â Â


Keep the number of partitions fixed to keep 
          the mapping of data to partition unchanged when 
          the size of a cluster changes.


## [Follower Reads](follower-reads.html)Â Â


Serve read requests from followers to achieve better throughput 
          and lower latency


## [Generation Clock](generation-clock.html)Â Â


A monotonically increasing number indicating the generation of the server.


## [Gossip Dissemination](gossip-dissemination.html)Â Â


Use a random selection of nodes to pass on information to ensure it reaches all 
   the nodes in the cluster without flooding the network


## [HeartBeat](heartbeat.html)Â Â


Show a server is available by periodically sending a message to all the other servers.


## [High-Water Mark](high-watermark.html)Â Â


An index in the write-ahead log showing the last successful replication.


## [Hybrid Clock](hybrid-clock.html)Â Â


Use a combination of system timestamp and logical timestamp to have versions as date and time, which can be ordered


## [Idempotent Receiver](idempotent-receiver.html)Â Â


Identify requests from clients uniquely so you can ignore duplicate requests when client retries


## [Key-Range Partitions](key-range-partitions.html)Â Â


Partition data in sorted key ranges to efficiently handle 
    range queries.


## [Lamport Clock](lamport-clock.html)Â Â


Use logical timestamps as a version for a value to allow ordering of values across servers


## [Leader and Followers](leader-follower.html)Â Â


Have a single server to coordinate replication across a set of servers.


## [Lease](lease.html)Â Â


Use time-bound leases for cluster nodes to coordinate their activities.


## [Low-Water Mark](low-watermark.html)Â Â


An index in the write-ahead log showing which portion of the log can be discarded.


## [Majority Quorum](majority-quorum.html)Â Â


Avoid two groups of servers making independent decisions 
  by requiring majority for taking every decision.


## [Paxos](paxos.html)Â Â


Use two consensus building phases to reach safe consensus even
    when nodes disconnect


## [Replicated Log](replicated-log.html)Â Â


Keep the state of multiple nodes synchronized by using a write-ahead log that is replicated to all the cluster nodes.


## [Request Batch](request-batch.html)Â Â


Combine multiple requests to optimally utilise the network


## [Request Pipeline](request-pipeline.html)Â Â


Improve latency by sending multiple requests on the connection without waiting for the response of the previous requests.


## [Request Waiting List](request-waiting-list.html)Â Â


Track client requests which require responses after the 
            criteria to respond is met based on responses from 
            other cluster nodes.


## [Segmented Log](segmented-log.html)Â Â


Split log into multiple smaller files instead of a single large file for easier operations.


## [Single-Socket Channel](single-socket-channel.html)Â Â


Maintain the order of the requests sent to a server by using a single TCP connection


## [Singular Update Queue](singular-update-queue.html)Â Â


Use a single thread to process requests asynchronously to maintain order without blocking the caller.


## [State Watch](state-watch.html)Â Â


Notify clients when specific values change on the server


## [Two-Phase Commit](two-phase-commit.html)Â Â


Update resources on multiple nodes in one atomic operation


## [Version Vector](version-vector.html)Â Â


Maintain a list of counters, one per cluster node, to detect concurrent updates


## [Versioned Value](versioned-value.html)Â Â


Store every update to a value with a new version, to allow reading historical values.


## [Write-Ahead Log](write-ahead-log.html)Â Â


Provide durability guarantee without the storage data structures to be flushed to disk,
        by persisting every state change as a command to the append only log.
