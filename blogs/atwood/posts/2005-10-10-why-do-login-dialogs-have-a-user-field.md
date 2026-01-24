---
title: "Why Do Login Dialogs Have a “User” Field?"
date: 2005-10-10
url: https://blog.codinghorror.com/why-do-login-dialogs-have-a-user-field/
slug: why-do-login-dialogs-have-a-user-field
word_count: 314
---

In [The Humane Interface](http://www.amazon.com/exec/obidos/ASIN/0201379376), the late [Jef Raskin](http://en.wikipedia.org/wiki/Jef_Raskin) asks an intriguing question: **why do login dialogs have a “User” field?**


Shouldn’t login dialogs look more like this?


![](https://blog.codinghorror.com/content/images/2025/03/image-305.png)


And you know what? He’s right. **Your password alone should be enough information for the computer to know who you are.**


As software developers, we constantly worry about edge conditions. So let’s put our thinking caps on. Why *can’t* this work?

- **The username adds security.** We broadcast our username in every email we send. There’s no security in a username. It’s public information.
- **No two users could have the same password.** Do we really want two users to have the same password? Doesn’t that imply that the password is already fatally flawed? Enforcing password uniqueness seems like a net benefit for everyone involved.
- **Users can’t choose simple passwords.** Users should never be allowed to choose a simple password. Simple passwords aren’t secure, even with a username/password combo. If we required users to create [pass-phrases instead of single passwords](https://blog.codinghorror.com/passwords-vs-pass-phrases/), they’d be plenty unique, easier to remember, and more secure. Using password alone would encourage the choice of far better passwords than we could ever hope to get with a traditional username/password combination.


The more I think about this, the more I think username/password is simply a bad convention that nobody has sufficiently questioned. As Jef states:


> *When the idea of improving the interface to a website or a computer system by simplifying the sign-on process to require only a password is suggested, it is usually rejected on one of two grounds. Either the programmers say that’s just not the way it’s done, or they say that they have no control over the sign-on procedure. But someone, of course, does have that control.*


It’s time to take control by [evangelizing pass-phrases](https://blog.codinghorror.com/passphrase-evangelism/) and **pushing to remove the user field from login forms**.

[security](https://blog.codinghorror.com/tag/security/)
[user-experience](https://blog.codinghorror.com/tag/user-experience-2/)
[software-development-concepts](https://blog.codinghorror.com/tag/software-development-concepts-2/)
