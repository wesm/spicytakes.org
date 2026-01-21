---
title: "The World's Computer"
date: 2024-02-26
url: https://geohot.github.io/blog/jekyll/update/2024/02/26/the-worlds-computer.html
slug: the-worlds-computer
word_count: 306
---

# The World's Computer

Feb 26, 2024

This was the tagline of Ethereum, and it’s really smart. Sadly, I feel they have lost their way with Proof of Stake, and wish they would go back to focusing on building a reasonable world computer.

In 2024, it’s still painfully annoying to stand up a database. This is the only thing big tech really has, to the point that I often use Google Sheets or a GitHub repo effectively as a database. Sure, you could use a hosted MySQL on Azure, but dealing with backups, redundancy, and configuration makes it so annoying.

Another fact about databases is that the world only needs one of them. Standing up multiple databases is usually done for throughput or sandboxing reasons, nothing fundamental. Just create more “tables”

One properly built database can kill big tech. The database needs to handle all the throughput in the world, never go down, and handle permissioning (which is all smart contracts should do).

The Ethereum network is averaging 13 transactions per second. This is way too small. Let’s look at a few sources of data we want in our database.

There’s 21,510 credit card transactions per second. There’s 6,000 tweets per second (and maybe 5x more for other actions), for a total of 30,000 tps. E-mail is much bigger, at 4,000,000 tps. How many pushes to all the GitHub repos? Total, we are probably looking at order of magnitude 10,000,000 tps.

If there’s 8 billion people on the planet, they do some database write action on average about every 10 minutes. That seems right.

Ethereum is off by a factor of a million. Though I suspect the world’s compute is growing faster than the world’s transactions per second. Once a single machine can handle the worlds transactions, big tech falls.

Who’s building the 10M TPS ethereum?
