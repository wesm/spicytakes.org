---
title: "The Inverse Web"
date: 2013-08-28
url: https://blog.mempko.com/the-inverse-web/
slug: the-inverse-web
word_count: 574
tags: ['firestr', '#wordpress', '#Import 2024-11-03 23:36']
---



**I would like to propose a thought experiment about what the inverse of the Web would look like.**


The Web conjures the idea that we are all interconnected. But somewhere at the end of the nineties the spiders grew bigger. In reality, all the services we use in day to day communication on the Web are configured in a star network. A star network is where all nodes meet in the center like spokes in a bicycle wheel.


The backbone of the Web is the Internet, based on TCP/IP and DNS. TCP/IP by design is a decentralized technology, providing a fundamental base to build upon. The Web is built on the internet using the HTTP protocol, which is designed to be a client/server architecture.


The Dot Com bubble brought major investment into HTTP and the browser. This investment has influenced our use of the internet to this day, where companies stand in the middle of our communication through the web. Instead of my client accessing your server and yours accessing mine, our clients access Google, or Yahoo, or Microsoft who manage the communication for us.


They stand in the middle of you and me. This position has allowed greater power and control of our communications and abuse by these companies. Star networks allow centralized storage and control of all communication in a network, which makes accessing things like your email and chats easy for both the companies that administer them, and malicious organizations.

****


**Great power plus great incompetency leads to great abuse.**


I got tired of this. Not only because programming for the Web is a convoluted mess, but also because it can be dangerous to our social future as demonstrated by the recent NSA conspiracy with corporate America.


So it got me thinking about what the Inverse Web would look like. I came up with the following criteria.


All communication would be…

1. Peer-to-peer instead client/server.
2. With people you know instead of anonymous servers.
3. State-full instead of stateless.
4. Encrypted by default instead of plain-text.


Instead of browsers downloading software from anonymous servers, software is uploaded to people you know. Instead of the code behind the software you connect to being proprietary and out of control of the clients, the software is open source and free to share and modify.


What would such software look like? The idea of the Inverse Web inspired me to start a project called Firestr (pronounced Fire Star) to figure this out.

- [Firestr Github Page](http://www.github.com/mempko/firestr?ref=blog.mempko.com)
- [Firestr Introduction](https://blog.mempko.com/2013/03/02/firestr-v0-1/)
- [Distributed Whiteboard ](https://blog.mempko.com/2013/03/23/write-a-distributed-white-board-app-using-firestr/)
- [Many Connections Demo](https://blog.mempko.com/2013/04/29/draw/)
- [Timer Demo](https://blog.mempko.com/2013/04/30/firestr-timer-demo/)


Firestr is currently very far along. Previously, the software satisfied all criteria except the last one. As of today, I have reached an important milestone where all P2P communication is now encrypted. The encryption scheme is simple at the moment but is a good foundation to build upon. Public key cryptography is used for the greeting messages and Diffie-Hellman-Merkle key exchange with AES for actual data communication.


In light of the recent historical events involving our privacy and corruption that star networks allow, I think we need to turn the web upside down and build new computational and communication systems on top of the internet. It probably won’t be [Firestr](http://www.github.com/mempko/firestr?ref=blog.mempko.com), but we as a society can choose to put capital in making better software. We don’t have to rely on the VCs and Valley to fund it. We can start another experiment in political economy.

