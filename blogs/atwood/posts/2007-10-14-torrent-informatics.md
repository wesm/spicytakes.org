---
title: "Torrent Informatics"
date: 2007-10-14
url: https://blog.codinghorror.com/torrent-informatics/
slug: torrent-informatics
word_count: 972
---

[uTorrent](http://www.utorrent.com/) is my favorite torrent client. It’s such a joy to use – a tiny, native application that offers a best-of-breed implementation of the [BitTorrent](http://en.wikipedia.org/wiki/BitTorrent) protocol. [Everybody loves BitTorrent](https://blog.codinghorror.com/everybody-loves-bittorrent/), and I love it too. I’m not the only one. By some estimates, torrent data may account for as much as 35% of all internet traffic.


I recently rented the television series [Boomtown](http://en.wikipedia.org/wiki/Boomtown) from Netflix, but I belatedly realized that the particular episode I really wanted to see was a part of season two. Unfortunately, Boomtown, like so many other great shows, was cancelled in its prime. In this case, it was cancelled right in the middle of season two – and the incomplete season was never released on DVD. What’s a poor, law-abiding citizen of the United States of America to do?


BitTorrent to the rescue. I was able to locate a torrent of all the Boomtown episodes, and I’m downloading it now.


I’ve talked before about the remarkable parity between the [uTorrent web user interface](https://blog.codinghorror.com/are-web-interfaces-good-enough/) and the windows user interface. However, as good as the web UI is, it pales in comparison to **the incredibly deep informatics that uTorrent provides on the state of your BitTorrent download**. I love poring over the torrent metrics; they’re beautifully presented – an excellent example of how to visually depict a complex set of data in a meaningful way. Let’s take a quick visual tour through the main tabs in uTorrent; I’ll point out the most interesting parts.


On the **General Tab**, we can see that the torrent is fairly well seeded. That’s important, because the biggest weakness of the torrent system is that it requires a certain level of popularity to work at all. In our case, the availability graphic is a nice, solid blue – there are no red bars indicating missing sections. The darker the bars, the more copies of that particular section are available in the swarm.


It’s also indicated numerically; an availability of 1 means the entire file is available. That’s the minimum, assuming you want to download everything. An availability of 5.93 indicates there are almost 6 complete copies of the torrent data in the swarm. It’s no coincidence that there are also 6 peers with a complete copy of the data – these critically important peers are known as “seeds” The other 19 peers will remain peers until they manage to download 100% of the data, and then they become seeds too. If a torrent loses all its seeds, it is in deep trouble.


![uTorrent general tab](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877701be0970c-pi.png)


On the **Files Tab**, we can see the state of individual files in the torrent. There’s a nice little graphic next to each file that shows how many pieces of the files have been downloaded. The blue sections indicate parts of the file that have been successfully downloaded; green sections indicate parts of the file that are being downloaded right now.


You can also tag files with a priority, so they’re retrieved in a particular order. Well, roughly – the torrent protocol retrieves in random order from whatever’s available in the peer swarm, so order is never guaranteed. Or, you can set them to “skip” if you don’t want to retrieve those files. Since I already rented all the season 1 DVDs, I set all the season 1 episodes to skip, and I switched the particular season 2 episode I wanted to “high.” This will prevent me from becoming a seed, but it dramatically shortens my download time.


![uTorrent files tab](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877701be5970c-pi.png)


On the **Peers Tab**, we can get a glimpse into the democratic nature of the BitTorrent protocol. These are our fellow peers and seeds, sharing whatever bits of the data they have with everyone else in the swarm. Given enough peers, downloads are fast for everyone. uTorrent conveniently does a DNS lookup and shows little flags next to each peer, so you can get a sense of how global the BitTorrent protocol really is.


![uTorrent peers tab](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877701be9970c-pi.png)


On the **Pieces Tab**, we can see the real-time state of the current pieces we’re downloading from our peers in the swarm. Dark blue means downloaded; light blue means requested but not yet downloaded.


![uTorrent pieces tab](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877701bf0970c-pi.png)


On the **Speed Tab**, we can view a history of transfer rates over time, including both upload and download speeds. BitTorrent is a shared download, so you’re supposed to give as much as you get – although altruism is difficult to enforce.


![uTorrent speed tab, transfer rates](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877701bf4970c-pi.png)


Another section of the **Speed Tab** shows an incredibly detailed breakdown of disk activity. BitTorrent is designed to download *enormous* files. This torrent is over 8 GB in size, for example. With such large amounts of data in play, managing disk caches and optimizing disk activity is unusually important.


![uTorrent speed tab, disk metrics](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877701bfa970c-pi.png)


Most of this is also explained in the official [uTorrent FAQ](https://web.archive.org/web/20071014003437/http://www.utorrent.com/faq.php), and it goes into greater detail, too.


I’ll admit that I tend to completely geek out on the way Torrent **exposes all the inner workings of the BitTorrent protocol in such a beautiful, highly visual way**. It never takes the easy way out and renders as a boring table of numbers when a visualization would work better. I think many programs could learn a lot from the way uTorrent so effortlessly presents the mountain of data it is processing internally.


I think there’s a deeper lesson here as well. **The commercial market failed me**. As far as I can tell, there’s no way I could obtain these elusive season 2 Boomtown episodes through legitimate channels. I was only able to obtain them through a torrent graciously seeded and shared by fellow Boomtown enthusiasts. Perhaps that’s the real beauty of BitTorrent – it’s the world’s most efficient and democratic distribution network, because it’s driven entirely by us.

[torrent client](https://blog.codinghorror.com/tag/torrent-client/)
[bittorrent protocol](https://blog.codinghorror.com/tag/bittorrent-protocol/)
[utorrent](https://blog.codinghorror.com/tag/utorrent/)
[internet traffic](https://blog.codinghorror.com/tag/internet-traffic/)
[torrenting](https://blog.codinghorror.com/tag/torrenting/)
