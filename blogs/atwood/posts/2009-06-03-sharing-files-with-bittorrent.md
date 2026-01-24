---
title: "Sharing Files With BitTorrent"
date: 2009-06-03
url: https://blog.codinghorror.com/sharing-files-with-bittorrent/
slug: sharing-files-with-bittorrent
word_count: 1129
---

[Everybody loves BitTorrent](https://blog.codinghorror.com/everybody-loves-bittorrent/). And rightfully so.


> With [BitTorrent](http://en.wikipedia.org/wiki/BitTorrent), you also start by placing your large file on a central server. But once the downloading begins, something magical happens: as clients download the file, they share whatever parts of the file they have with each other. Clients can opportunistically connect with any other client to obtain multiple parts of the file at once. And it scales perfectly: as file size and audience size increases, the bandwidth of the BitTorrent distribution network also increases. Your server does less and less work with each connected client. It’s an elegant, egalitarian way of sharing large files with large audiences.
> BitTorrent radically shifts the economics of distribution. It’s one of the most miraculous ideas ever conceived on the internet. As far as I’m concerned, there should be a Nobel prize for computing, and [the inventor of BitTorrent](http://en.wikipedia.org/wiki/Bram_Cohen) should be its first recipient.


I’ve been a happy consumer of [files distributed via BitTorrent](https://blog.codinghorror.com/torrent-informatics/) for years; it was only natural that I would turn to BitTorrent to distribute our cc-wiki licensed Stack Overflow data. I figured serving a several-hundred megabyte file with BitTorrent wouldn’t be much harder than downloading one. Boy, was I ever wrong. **Sharing files with BitTorrent is *way* more complicated than downloading them!** After two frustrating hours, I finally came up with a relatively straightforward way to share a file via BitTorrent, and in the interests of saving future readers a little time, I’m documenting it here.


Now, I’m going to show you an easy way, but it isn’t technically the *easiest* way. The easiest way is to let someone else do the sharing for you. If you own content that you want to share, [LegalTorrents is the obvious choice](http://legaltorrents.com/):


> LegalTorrentstm is an online digital media community.
> We discover and distribute high quality open-license (Creative Commons) digital media and art, and provide support to Content Creators. We host creative content in its entirety, ensure fast, reliable downloads, and enable users to directly sponsor Content Creators and their work.
> We distribute content with the full permission of the rights holders and use the peer-2-peer file-sharing technology called BitTorrent.


The site is still in beta, but signup is a snap, because [they support OpenID](https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/)! I encourage anyone interested to check it out. If nothing else, **get the furtive thrill of actually downloading *legal* content through BitTorrent for once!** Yes, it can happen. Shocking, I know. Don’t worry, you crazy kids can get right back to your regular non-copyright-respecting torrenting ways immediately afterwards.


Anyway, you can’t start sharing files on LegalTorrents without some kind of special email-us-please permission, and I was in a hurry. I wanted to share files via BitTorrent *right now*. I did, and you can too! But you’ll need a few things first:

1. A copy of [uTorrent](http://www.utorrent.com/) (it’s free!)
2. Your **external IP address**; if you don’t know what it is, use [http://www.whatismyipaddress.com](http://www.whatismyipaddress.com/) to find out.
3. The uTorrent **listen port**. This is under Options | Preferences | Connection. This is typically set randomly every time uTorrent starts, so you may want to specify a more memorable value here.
4. You must have **port forwarding properly configured** so the outside world can get to your IP address and the port specified above. A full discussion of how to do this is outside the scope of this post, but it usually starts with your firewall settings and/or router configuration. uTorrent has a fairly nice help page at Options | Speed Guide that’s a good start; just click the **Test if port is forwarded properly** button on that dialog to begin.


Here’s where I hit a major roadblock: to share files via BitTorrent, [you need a tracker](http://en.wikipedia.org/wiki/BitTorrent_tracker).


> A BitTorrent tracker is a server that assists in the communication between peers using the BitTorrent protocol. It is also, in the absence of extensions to the original protocol, the only major critical point, as **clients are required to communicate with the tracker to initiate downloads**. Clients that have already begun downloading also communicate with the tracker periodically to negotiate with newer peers and provide statistics; however, after the initial reception of peer data, peer communication can continue without a tracker.


Without a tracker, you’re sort of hosed, as clients will never be able to find your file, much less each other. Unfortunately, most of the freely open, public trackers out there are sort of... disreputable. And the LegalTorrents tracker won’t track files unless they are on its creator whitelist, which involves that manual sign-up process. You’ve got precious few legit options for tracking, unless you’re willing to take a trip to the wrong side of town, and associate yourself and your files with that kind of... neighborhood. I wasn’t.


Fortunately, uTorrent has a solution: **you can become your own tracker!**

1. in uTorrent, go to Options | Preferences | Advanced.
2. Scroll down to `bt.enable_tracker` and set it to `True`
3. Restart uTorrent.


![](https://blog.codinghorror.com/content/images/2025/04/image-383.png)


Now, let’s create the torrent for the file we want to host, which will point to our newly created tracker.

1. In uTorrent, click the Create New Torrent button.
2. Select the file or directory you want to share.
3. Enter your tracker in this format: **http://my-ip-address:my-port/announce**
4. That’s it! Click Create and save the new *.torrent file you’ve created.


![](https://blog.codinghorror.com/content/images/2025/04/image-384.png)


Now go forth and share your *.torrent file with the world. Share it with anyone and everyone! The more the merrier! Any client that opens your *.torrent file **will attempt to connect to *your* tracker, download your file, and share it with other downloading clients in classic BitTorrent style**. Pat yourself on the back; you just shared a file with the world using the transformative distribution power of BitTorrent!


But you do have to keep uTorrent running as a desktop application all the time, which is sort of a bummer. What if you wanted to **share your file on a server**, or via a silent background process? No problem. It’s just a few more steps:

kg-card-begin: html

kg-card-end: html

(Obviously, replace the above paths with the actual paths that you installed uTorrent to.)


Bam – you’re sharing files with the world using BitTorrent, even when you’re not logged in. You can control everything remotely, too, by navigating your browser to the WebUI URL.


Like so many things in Windows, it ain’t pretty, but it gets the job done. It’s ironic that BitTorrent, which is justly famous for equalizing the highly asymmetric nature of most people’s internet connections, is itself so asymmetric when it comes to sharing: **trivially easy to consume, but awkward and confusing to share**. That’s too bad, because BitTorrent is such a powerful tool for sharing. Hopefully this post demystifies the process a bit!

[distributed systems](https://blog.codinghorror.com/tag/distributed-systems/)
[file sharing](https://blog.codinghorror.com/tag/file-sharing/)
[bittorrent](https://blog.codinghorror.com/tag/bittorrent/)
[peer-to-peer networking](https://blog.codinghorror.com/tag/peer-to-peer-networking/)
[content distribution](https://blog.codinghorror.com/tag/content-distribution/)
