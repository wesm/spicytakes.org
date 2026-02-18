---
title: "Networking tool comics!"
date: 2019-02-10
url: https://jvns.ca/blog/2019/02/10/a-few-networking-tool-comics/
slug: a-few-networking-tool-comics
word_count: 402
---


Hello! I haven’t been blogging too much recently because I’m working on a new [zine](https://wizardzines.com) project: Linux
networking tools!


I’m pretty excited about this one – I LOVE computer networking (it’s what I spent a big chunk of
the last few years at work doing), but getting started with all the tools was originally a little
tricky! For example – what if you have the IP address of a server and you want to make a https
connection to it and check that it has a valid certificate? But you haven’t changed DNS to resolve
to that server yet (because you don’t know if it works!) so you need to use the IP address? If you do
`curl https://1.2.3.4/`, curl will tell you that the certificate isn’t valid (because it’s not valid
for 1.2.3.4). So you need to know to do `curl https://jvns.ca --resolve jvns.ca:443:104.198.14.52`.


I know how to use `curl --resolve` because my coworker told me how. And I learned that to find out
when a cert expires you can do `openssl x509 -in YOURCERT.pem  -text -noout` the same way. So the
goal with this zine is basically to be “your very helpful coworker who gives you tips about how to
use networking tools” in case you don’t have that person.


And as we know, a lot of these tools have VERY LONG man pages and you only usually need to know
like 5 command line options to do 90% of what you want to do. For example I only ever do maybe 4
things with openssl even though the openssl man pages together have more than 60,000 words.


There are a few things I’m also adding (like ethtool and nmap and tc) which I don’t personally use
super often but I think are super useful to people with different jobs than me. And I’m a big fan of
mixing more advanced things (like tc) with basic things (like ssh) because then even if you’re
learning the basic things for the first time, you can learn that the advanced thing exists!


Here’s some work in progress:


![](https://jvns.ca/images/curl.jpeg)


![](https://jvns.ca/images/ssh.jpeg)


![](https://jvns.ca/images/netcat.jpeg)


![](https://jvns.ca/images/nmap.jpeg)


![](https://jvns.ca/images/openssl.jpeg)


![](https://jvns.ca/images/ethtool.jpeg)


It’s been super fun to draw these: I didn’t know about `ssh-copy-id` or `~.` before I made that ssh
comic and I really wish I’d known about them earlier!


As usual I’ll announce the zine when it comes out here, or you can sign up for announcements at
[https://wizardzines.com/mailing-list/](https://wizardzines.com/mailing-list/).
