---
title: "What are SSL ciphers & session keys?"
date: 2016-05-06
url: https://jvns.ca/blog/2016/05/06/what-are-ssl-ciphers-and-session-keys/
slug: what-are-ssl-ciphers-and-session-keys
word_count: 495
---


This morning I gave a lightning talk at work (about what I learned about CDNs last week). Lightning talks at work are super fun and great. I like hearing about what my coworkers are working on & thinking about a lot, and they’re pretty lightweight to prepare.


During that talk, I made some offhand remark like “I know basically nothing
about security”, which is true. Then at lunch [Cory](https://twitter.com/gphat)
was like “hey, you said you knew nothing about security! I have some facts for
you!” and proceeded to tell me a very useful thing I did not know!!


So. I knew about public key cryptography, and that people use
[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) to do encryption. I
mostly know how RSA works because I took a number theory class in undergrad and
thought I understood what RSA was for – you encrypt messages with it, right?


It turns out that no, you do not use RSA to encrypt messages in practice, which is what Cory told me and what surprised me so much.


The Wikipedia article says:


> RSA is a relatively slow algorithm, and because of this it is less commonly
> used to directly encrypt user data. More often, RSA passes encrypted shared
> keys for symmetric key cryptography which in turn can perform bulk encryption-
> decryption operations at much higher speed.


So. If you’re developing the SSL protocol, you want encryption to be pretty fast. RSA is super secure but not very fast. So what do you do? Maybe what that Wikipedia paragraph says!

- choose a fast symmetric cipher (like AES). This is called, well, the **cipher**.
- choose a random key for that cipher. This is called the **session key**.
- Encrypt that key using RSA (public key crypto) and send it to the person you’re communicating with
- Then you both have the same AES key, and can encrypt all your communications back and forth after that


I then went and read Karla Burnett’s great article [SSL: It’s hard to do right](https://recompilermag.com/issues/issue-1/ssl-its-hard-to-do-right/), which says


> For example, if a client negotiated the Diffie-Hellman protocol (DH) for key exchange, with RSA for authentication, `AES_256_CBC` as a cipher, and SHA-256 as a hash, the connection would have a ciphersuite of `DH_RSA_WITH_AES_256_CBC_SHA256`.


which suggests that you don’t actually encrypt keys with RSA, but instead you agree on a key using Diffie-Hellman. But in any case you **definitely** don’t encrypt your messages with RSA.


Now all the conversations people have about insecure SSL/TLS ciphers make so much more sense to me!! Like, if your server chooses a bad cipher to communicate with, it doesn’t matter that the way you decided on that key is really good and totally secure! They can just break the cipher and read your SSL traffic.


If you’re interested in SSL you should read Karla’s article! It’s super good and explains a lot of recent SSL exploits quite clearly, and really motivates me to keep my TLS up to date :).
