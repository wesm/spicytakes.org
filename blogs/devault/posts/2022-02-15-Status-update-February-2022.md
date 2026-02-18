---
title: "Status update, February 2022"
date: 2022-02-15
url: https://drewdevault.com/2022/02/15/Status-update-February-2022.html
slug: Status-update-February-2022
word_count: 357
---

Hello once again! Another month of free software development goes by with lots
of progress in all respects.

I will open with some news about  [godocs.io](https://godocs.io) : version 1.0 of  [our fork of gddo](https://sr.ht/~sircmpwn/godocs.io) 
has been released! Big thanks to Adnan Maolood for his work on this. I’m very
pleased that, following our fork, we were not only able to provide continuity
for godoc.org, but also to simplify, refactor, and improve the underlying
software considerably. Check out  [Adnan’s blog post](https://adnano.co/2022/02/10/godocs.io-one-year-later/)  for more details.

In programming language news, we have had substantial progress in many respects.
One interesting project I’ve started is a Redis protocol implementation:

```
const conn = redis::connect()!;
defer redis::close(&conn);

fmt::println("=> SET foo bar EX 10")!;
redis::set(&conn, "foo", "bar", 10: redis::ex)!;
```

Another contributor has been working on expanding our graphics support,
including developing a backend for  [glad](https://github.com/Dav1dde/glad)  to generate OpenGL bindings, and a
linear algebra library ala  [glm](https://glm.g-truc.net/)  for stuff like vector and matrix manipulation.
Other new modules include a  [MIME database](https://drewdevault.com/2022/01/28/Implementing-mime-in-xxxx.html)  and encoding::base32. Cryptography
progress continued with the introduction of XTS mode for AES, which is useful
for full disk encryption implementations, but has slowed while we develop bigint
support for future algorithms like RSA. I have also been rewriting the language
introduction tutorial with a greater emphasis on practical usage.

Before we move on from the language project: I need your help! I am looking for
someone to help develop terminal support. This is fairly straightforward, though
laborsome: it involves developing libraries in our language which provide the
equivalents of something like ncurses (or, better,  [libtickit](http://www.leonerd.org.uk/code/libtickit/) ), as well as the
other end like  [libvterm](http://www.leonerd.org.uk/code/libvterm/)  offers. Please  [email me](mailto:sir@cmpwn.com)  if you want to help.

In SourceHut news, we have  [hired](https://sourcehut.org/blog/2022-02-02-welcome-conrad/)  our third full-time engineer: Conrad
Hoffmann! Check out the blog post for details. The first major effort from
Adnan’s NLnet-sponsored SourceHut work also landed yesterday, introducing
GraphQL-native webhooks to git.sr.ht alongside a slew of other improvements.
pages.sr.ht also saw some improvements that allow users to configure their
site’s behavior more closely. Check out the “What’s cooking” post later today
for all of the SourceHut news.

That’s all for today, thanks for reading!
