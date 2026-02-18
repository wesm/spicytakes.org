---
title: "How does IRC's federation model compare to ActivityPub?"
date: 2021-07-03
url: https://drewdevault.com/2021/07/03/How-does-IRC-federate.html
slug: How-does-IRC-federate
word_count: 723
---

Today’s federated revolution is led by ActivityPub, leading to the rise of
services like Mastodon, PeerTube, PixelFed, and more. These new technologies
have a particular approach to federation, which is coloring perceptions on what
it actually means for a system to be federated at all. Today’s post will explain
how  [Internet Relay Chat](https://en.wikipedia.org/wiki/Internet_Relay_Chat) 
(IRC), a technology first introduced in the late 1980’s, does federation
differently, and why.

As IRC has aged, many users today have only ever used a few networks, such as
Liberachat (or Freenode, up until several weeks ago), which use a particular IRC
model which does not, at first glance, appear to utilize federation. After all,
everyone types “irc.libera.chat” into their client and they all end up on the
same network and in the same namespace. However, this domain name is backed by a
round-robin resolver which will connect you to any of  [several dozen
servers](https://netsplit.de/servers/?net=Libera.Chat) , which are connected to each other 1  and exchange messages on
behalf of the users who reside on each. This is why we call them IRC  *networks* 
— each is composed of a network of servers that work together.

But why can’t I send messages to users on  [OFTC](https://www.oftc.net)  from my Libera Chat session?
Well, IRC networks are federated, but they are typically a  *closed*  federation,
such that each network forms a discrete graph of servers, not interconnected
with any of the others. In ActivityPub terms, imagine a version of Mastodon
where, instead of automatically federating with new instances, server operators
whitelisted each one, forming a closed graph of connected instances. Organize
these servers under a single named entity (“Mastonet” or something), and the
result is an “ActivityPub network” which operates in the same sense as a typical
“IRC network”.

In contrast to Mastodon’s open federation, allowing any server to peer with any
others without prior agreement between their operators, most IRC networks are
closed. The network’s servers may have independent operators, but they operate
together under a common agreement, rather than the laissez-faire approach
typical of 2  ActivityPub servers. The exact organizational and governance
models vary, but many of these networks have discrete teams of staff which
serve as moderators 3 , often unrelated to the people responsible for the
servers. The social system can be designed independently of the technology.

Among IRC networks, there are degrees of openness. Libera Chat, the largest
network, is run by a single governing organization, using servers donated by
(and in the possession of) independent sponsors. Many smaller networks are
run on as few as one server, and some larger networks (particularly older ones)
are run by many independent operators acting like more of a cooperative.
 [EFnet](http://efnet.org) , the oldest network, is run in this manner — you
can even  [apply to become an operator](http://www.efnet.org/?module=docs&doc=16)  yourself.

We can see from this that the idea of federation is flexible, allowing us to
build a variety of social and operational structures. There’s no single right
answer — approaches like IRC are able to balance many different benefits
and drawbacks of their approach, such as balancing a reduced level of user
mobility with a stronger approach to moderation and abuse reduction, while
simultaneously enjoying the cost and scalability benefits of a federated design.
Other federations, like Matrix, email, and Usenet, have their own set of
tradeoffs. What unifies them is the ability to scale to a large size without
expensive infrastructure, under the social models which best suit their users'
needs, without a centralizing capital motive.

1. Each server is not necessarily connected to each other server, by the way.  Messages can be relayed from one server to another repeatedly to reach the intended destination. This provides IRC with a greater degree of scalability when compared to ActivityPub, where each server must communicate directly with the servers whose users it needs to reach. It also makes IRC more vulnerable to outages partitioning the network; we call these incidents “netsplits”. ↩︎
2. Typical, but not universal. ↩︎
3. There are two classes of moderators on IRC: oppers and ops. The former is responsible for the network, and mainly concerns themselves with matters of spam, user registration, settling disputes, and supporting ops. The ops are responsible for specific channels (spaces for discussion) and can define and enforce further rules at their discretion, within any limits imposed by the host network. ↩︎
