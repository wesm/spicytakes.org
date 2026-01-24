---
title: "The Economics of Bandwidth"
date: 2007-02-01
url: https://blog.codinghorror.com/the-economics-of-bandwidth/
slug: the-economics-of-bandwidth
word_count: 1520
---

One of the sadder recent news stories is the disappearance of [Turing award-winning researcher Jim Gray](https://web.archive.org/web/20070309124233/http://www.informationweek.com/news/showArticle.jhtml?articleID=197002918). I’ve [written about Jim’s research before](https://blog.codinghorror.com/the-popularity-tax/); he has a knack for explaining fundamental truths of computer architecture in uniquely clear ways.


For example, in [this ACM interview](https://web.archive.org/web/20070705023308/http://www.acmqueue.com/modules.php?name=Content&pa=showpage&pid=43), Jim illustrates how **the unusual economics of bandwidth can make a sneakernet worthwhile** – *if you’re sending a terabyte of data*.


> **JG** We built more than 20 of these boxes we call TeraScale SneakerNet boxes. Three of them are in circulation. We have a dozen doing TeraServer work; we have about eight in our lab for video archives, backups, and so on. It’s real convenient to have 40 TB of storage to work with if you are a database guy. Remember the old days and the original eight-inch floppy disks? These are just much bigger.
> **DP** “Sneaker net” was when you used your sneakers to transport data?
> **JG** In the old days, sneaker net was the notion that you would pull out floppy disks, run across the room in your sneakers, and plug the floppy into another machine. This is just TeraScale SneakerNet. You write your terabytes onto this thing and ship it out to your pals. Some of our pals are extremely well connected – they are part of Internet 2, Virtual Business Networks (VBNs), and the Next Generation Internet (NGI). Even so, it takes them a long time to copy a gigabyte. Copy a terabyte? It takes them a very, very long time across the networks they have.
> **DP** When they get a whole computer, don’t they still have to copy?
> **JG** Yes, but it runs around their fast LAN at gigabit speeds as opposed to the slower Internet. The Internet plans to be running at gigabit speeds, but if you experiment with your desktop now, I think you’ll find that it runs at a megabyte a second or less.
> **DP** Megabyte a second? We get almost 10 megabytes sustained here.
> **JG** That translates to 40 gigabytes per hour and a terabyte per day. I tend to write a terabyte in about 8 to 10 hours locally. I can send it via UPS anywhere in the U.S. That turns out to be about seven megabytes per second.
> **DP** How do you get to the 7-megabytes-per-second figure?
> **JG** UPS takes 24 hours, and 9 hours at each end to do the copy.
> **DP** Wouldn’t it be a lot less hassle to use the Internet?
> **JG** It’s cheaper to send the machine. The phone bill, at the rate Microsoft pays, is about $1 per gigabyte sent and about $1 per gigabyte received – about $2,000 per terabyte. It’s the same hassle for me whether I send it via the Internet or an overnight package with a computer. I have to copy the files to a server in any case. The extra step is putting the SneakerNet in a cardboard box and slapping a UPS label on it. I have gotten fairly good at that. Tape media is about $3,000 a terabyte. This media, in packaged SneakerNet form, is about $1,500 a terabyte.


Does transferring a terabyte of data via sneakernet make sense?


![](https://blog.codinghorror.com/content/images/2025/03/image-399.png)


First, consider the bandwidth capabilities and monthly cost of [a few common Internet connections](http://en.wikipedia.org/wiki/List_of_device_bandwidths).

kg-card-begin: html


|  | Cost
(month) | Download rate
per second | Upload rate
per second |
| 56.6 Modem | $15 | 5 KB | 4 KB |
| DSL | $30 | 192 KB | 24 KB |
| DSL, Premium | $50 | 384 KB | 48 KB |
| Cable | $50 | 300 KB | 30 KB |
| Cable, Premium | $80 | 600 KB | 60 KB |
| T1 | $300 | 192 KB | 192 KB |
| T3 | $1,400 | 5.4 MB | 5.4 MB |
| OC-3 | $7,500 | 19 MB | 19 MB |


kg-card-end: html

Of course, costs may vary; I chose costs that jibed with my personal experience and lined up with a few cursory searches for pricing around the web. Please let me know you think these costs are way out of line. Assuming for the sake of argument that these are representative costs and throughput rates, how much would it cost to transfer, let’s say, a **20 gigabyte high definition video file**?

kg-card-begin: html


|  | Download 20 GB | Upload 20 GB |
| 56.6 Modem | 49 days | $24.27 | 61 days | $30.34 |
| DSL | 1½ days | $1.26 | 10 days | $10.11 |
| DSL, Premium | 15 hours | $1.05 | 5 days | $8.43 |
| Cable | 19 hours | $1.35 | 8 days | $13.48 |
| Cable, Premium | 10 hours | $1.08 | 4 days | $10.79 |
| T1 | 1½ days | $12.64 | 1½ days | $12.64 |
| T3 | 1 hour | $1.98 | 1 hour | $1.98 |
| OC-3 | 17 minutes | $3.05 | 17 minutes | $3.05 |


kg-card-end: html

And **how much could we upload or download in total**, assuming we had these connections going full-bore, around the clock?

kg-card-begin: html


|  | in 24 hours | in 1 month |
|  | Download | Upload | Download | Upload |
| 56.6 Modem | 422 MB | 338 MB | 12 GB | 10 GB |
| DSL | 16 GB | 2 GB | 475 GB | 59 GB |
| DSL, Premium | 32 GB | 4 GB | 949 GB | 119 GB |
| Cable | 25 GB | 2 GB | 741 GB | 74 GB |
| Cable, Premium | 49 GB | 5 GB | 1.5 TB | 148 GB |
| T1 | 16 GB | 16 GB | 475 GB | 475 GB |
| T3 | 472 GB | 472 GB | 14 TB | 14 TB |
| OC-3 | 1.6 TB | 1.6 TB | 49 TB | 49 TB |


kg-card-end: html

Let’s say we wanted to send **a terabyte of data via sneakernet**:

- Two 500 GB hard drives weigh about five pounds; we can wrap the drives in bubble wrap and fit them in a standard FedEx box.
- It costs about $60 to send five pounds in a standard FedEx box coast-to-coast in 24 hours.
- The total transit time is 32 hours: 24 hours, plus 8 hours to copy the data on and off the drives.


*We just transferred data at the rate of 9.1 megabytes per second.* The only internet connection that’s capable of our sneakernet throughput level is the OC-3. None of the others are even close, particularly if you consider the highly asymmetric nature of consumer connections, where upload rate is a fraction of the download rate.

And what about the cost? Not including the $300 expense of the two hard drives (which I think is fair, because they’re reusable), the total cost per gigabyte breaks down like so:

kg-card-begin: html


|  | Cost per GB
Downloaded | Cost per GB
Uploaded |
| 56.6 Modem | $1.21 | $1.52 |
| DSL | $0.06 | $0.51 |
| DSL, Premium | $0.05 | $0.42 |
| Cable | $0.07 | $0.67 |
| Cable, Premium | $0.05 | $0.54 |
| T1 | $0.63 | $0.63 |
| T3 | $0.10 | $0.10 |
| OC-3 | $0.15 | $0.15 |
| Sneakernet | $0.06 | $0.06 |


kg-card-end: html

It wasn’t obvious to me, but the sneakernet math clearly works. This is exactly the kind of insight Jim Gray was famous for.

Jim also says **the cost of internet bandwidth was roughly a dollar a gigabyte for Microsoft in 2003**. Is that still how much internet bandwidth costs today? According to the figures I found, the only connection that expensive today is a modem. And [who uses modems any more?](https://blog.codinghorror.com/do-modems-still-matter/) It seems implausible that consumer internet bandwidth would be sold cheaper than large blocks of commercial internet bandwidth. Let’s take a look.

- Amazon’s S3 service charges 20 cents per gigabyte to transfer data.
- Robert X Cringely regularly gets charged 20 cents per gigabyte for NerdTV, and guesses that large bandwidth consumers like YouTube can negotiate rates as low as 10 cents per gigabyte.
- Mitch Ratcliffe did a survey of internet providers and found that most charge 85 cents per gigabyte, and he proposes YouTube could negotiate a rate of 45 cents per gigabyte.


I’m not sure who to believe. It’s a good sign that most estimates are under the $1.00 per gigabyte rate that Jim quoted in 2003. **I’d like to think that the cost of internet bandwidth is getting less expensive over time.** High bandwidth costs lead to a de-facto “[popularity tax,](https://blog.codinghorror.com/the-popularity-tax/)” and that’s like a giant wet blanket over content creators. Cheaper bandwidth is a net public good: it leads directly to more content, and higher quality content, for everyone.

[networking](https://blog.codinghorror.com/tag/networking/)
[bandwidth economics](https://blog.codinghorror.com/tag/bandwidth-economics/)
[data transfer](https://blog.codinghorror.com/tag/data-transfer/)
[computer architecture](https://blog.codinghorror.com/tag/computer-architecture/)
[storage solutions](https://blog.codinghorror.com/tag/storage-solutions/)
