---
title: "Everybody Loves BitTorrent"
date: 2007-02-19
url: https://blog.codinghorror.com/everybody-loves-bittorrent/
slug: everybody-loves-bittorrent
word_count: 947
---

The traditional method of distributing large files is to put them on a central server. Each client then downloads the file directly from the server. It’s a gratifyingly simple approach, but *it doesn’t scale*. For every download, the server consumes bandwidth equal to the size of the file. You probably don’t have enough bandwidth to serve a large file to a large audience, and even if you did, your [bandwidth bill](https://blog.codinghorror.com/the-economics-of-bandwidth/) would go through the roof. The larger the file, the larger the audience, the worse your bandwidth problem gets. It’s [a popularity tax](https://blog.codinghorror.com/the-popularity-tax/).


With [BitTorrent](http://en.wikipedia.org/wiki/BitTorrent), you also start by placing your large file on a central server. But once the downloading begins, something magical happens: as clients download the file, **they share whatever parts of the file they have with each other**. Clients can opportunistically connect with any other client to obtain multiple parts of the file at once. And it scales perfectly: as file size and audience size increases, the bandwidth of the BitTorrent distribution network also increases. Your server does less and less work with each connected client. It’s an elegant, egalitarian way of sharing large files with large audiences.


**BitTorrent radically shifts the economics of distribution**. It’s one of the most miraculous ideas ever conceived on the internet. As far as I’m concerned, there should be a Nobel prize for computing, and [the inventor of BitTorrent](http://en.wikipedia.org/wiki/Bram_Cohen) should be its first recipient.


There’s a great [Processing visualization](https://blog.codinghorror.com/dynamic-lightweight-visualization/) of BitTorrent in action which explains it far better than I can. The original visualization is not only down semi-permanently, but also written for an ancient version of [Processing](http://processing.org/). I grabbed a cached copy of the code and updated it for the latest version of Processing.


![animated visualization of BitTorrent in action](https://blog.codinghorror.com/content/images/2019/09/bittorrent-animation.gif)


This meager little animated GIF doesn’t do the highly dynamic, real-time nature of the visualization justice. I highly recommend [downloading Processing](http://processing.org/download/index.html) and downloading [the updated bittorrent visualization code](https://web.archive.org/web/20070222085835/http://www.codinghorror.com/blog/files/bittorrent-visualization-processing.txt), so you can see the process from start to finish on your own machine. It’s beautiful.


But as as wonderful and clever as BitTorrent is, it isn’t perfect. As an avid BitTorrent user, I’ve noticed the following problems:

1. **BitTorrent is a terrible Long Tail client**.
The efficiency of BitTorrent is predicated on popularity. The more people downloading, the larger the distribution network gets. But if what you want is obscure or unpopular – part of [the long tail](http://www.thelongtail.com/) – BitTorrent is painfully, brutally slow. With only a handful of clients sharing the workload, you’re better off using traditional distribution methods.
2. **BitTorrent, although distributed, is still centralized**.
Download work is shared by the clients, but how do the clients locate each other? Traditionally this is done through a centralized server “tracker,” or list of peers. This means BitTorrent is vulnerable to attacks on the centralized server. Once the server is out of commission, the clients have no way of locating each other, and the whole distribution network grinds to a halt. There are alternatives which allow clients to share the list of peers amongst themselves, such as [distributed hash tables](http://en.wikipedia.org/wiki/Distributed_hash_table), but centralized tracking is more efficient.
Also, in order to even begin a BitTorrent download, you must first know where to obtain a .torrent file. It’s a chicken-and-egg problem which also implies the existence of a centralized server out there somewhere.
3. **BitTorrent is unsuitable for small files, even if they are extremely popular.**
The BitTorrent distribution network is predicated on clients sharing pieces of the file during the download period. But if the download period is small, the opportunity window for sharing is also small; at any given time only a few users will be downloading. This is another scenario where you’re unlikely to find any peers, so you’re better off with traditional distribution methods.
4. **BitTorrent relies on client altruism.**
There’s no rule that says clients *must* share bandwidth while they’re downloading. Although most BitTorrent clients default to uploading the maximum amount a user’s upstream connection allows, it’s possible to dial the upload rate down to nothing if you’re greedy. And some users may have their firewalls configured in such a way that they *can’t* upload data, even if they wanted to. There’s no way to punish bad peers for not sharing, or reward good peers for sharing more. Furthermore, every torrent needs a “seed” – a peer with 100% of the file downloaded – connected at all times. If there is no seed, no matter how many peers you have, none of the peers will never be able to download the entire file. It’s considered a courtesy to stay connected if you have 100% of the file downloaded and no other seeds are available. But again, this is a convention, not a requirement. It’s entirely possible for a torrent to “die” when there are no seeds available.


The BitTorrent model is innovative, but it isn’t suitable for every distribution task. The centralized server model is superior in most cases. But **centralized distribution is a tool for the rich**. Only highly profitable organizations can afford massive amounts of bandwidth. BitTorrent, in comparison, is highly democratic. BitTorrent gives the people whatever they want, whenever they want it – by collectively leveraging the tiny trickle of upstream bandwidth doled out by most internet service providers.


But just because it’s democratic doesn’t mean BitTorrent has to be synonymous with intellectual piracy. BitTorrent has legitimate uses, such as [distributing World of Warcraft patches](http://arstechnica.com/news/posts/1079538547.html). And Amazon’s S3 directly [supports the torrent protocol](http://noisemore.wordpress.com/2006/03/14/amazon-s3-has-bittorrent-support/).


BitTorrent, in short, **puts distribution choices back in the hands of the people**. And that’s why everybody loves BitTorrent. Everyone, that is, except the [MPAA](http://en.wikipedia.org/wiki/MPAA) and [RIAA](http://en.wikipedia.org/wiki/RIAA).

[distributed systems](https://blog.codinghorror.com/tag/distributed-systems/)
[p2p networking](https://blog.codinghorror.com/tag/p2p-networking/)
[file sharing](https://blog.codinghorror.com/tag/file-sharing/)
[bandwidth optimization](https://blog.codinghorror.com/tag/bandwidth-optimization/)
[peer-to-peer networks](https://blog.codinghorror.com/tag/peer-to-peer-networks/)
