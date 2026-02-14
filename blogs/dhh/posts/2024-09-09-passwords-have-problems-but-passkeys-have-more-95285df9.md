---
title: "Passwords have problems, but passkeys have more"
date: 2024-09-09
url: https://world.hey.com/dhh/passwords-have-problems-but-passkeys-have-more-95285df9
slug: passwords-have-problems-but-passkeys-have-more-95285df9
word_count: 588
---

We had originally planned to go all-in on passkeys for
[ONCE/Campfire](https://once.com/campfire)
, and we built the early authentication system entirely around that. It was not a simple setup! Handling passkeys properly is surprisingly complicated on the backend, but we got it done. Unfortunately, the user experience kinda sucked, so we ended up ripping it all out again.
The problem with passkeys is that they're essentially a halfway house to a password manager, but tied to a specific platform in ways that aren't obvious to a user at all, and liable to easily leave them unable to access of their accounts. Much the same way that two-factor authentication can do, but worse, since you're not even aware of it.
Let's take a simple example. You have an iPhone and a Windows computer. Chrome on Windows stores your passkeys in Windows Hello, so if you sign up for a service on Windows, and you then want to access it on iPhone, you're going to be stuck (unless you're so forward thinking as to add a second passkey, somehow, from the iPhone will on the Windows computer!). The passkey lives on the wrong device, if you're away from the computer and want to login, and it's not at all obvious to most users how they might fix that.
Even in the best case scenario, where you're using an iPhone and a Mac that are synced with Keychain Access via iCloud, you're still going to be stuck, if you need to access a service on a friend's computer in a pinch. Or if you're not using Keychain Access at all. There are plenty of pitfalls all over the flow. And the solutions, like scanning a QR code with a separate device, are cumbersome and alien to most users.
If you're going to teach someone how to deal with all of this, and all the potential pitfalls that might lock them out of your service, you almost might as well teach them how to use a cross-platform password manager like 1password.
Yes, passwords have problems. If you're using them without a password manager, you're likely to reuse them across multiple services, and if you do, all it takes is one service with awful password practices (like storing them in plain text rather than hashing them with something like bcrypt), and a breach will mean hackers might get access to all your other services.
But just because we have a real problem doesn't mean that all proposed solutions are actually going to be better. And at the moment, I don't see how passkeys are actually better, and, worse still, can become better. Unless you accept the idea that all your passwords should be tied to one computing ecosystem, and thus make it hard to use alternative computers.
A decent alternative to passkeys, if you need the extra layer of security, is to lean on email for the first login from a new device. Treating email as a second factor, but only on the first login from that device. Everyone has email, everyone understands email. (Just don't force us all to go through magic links exclusively, as that's a pain too for those who've actually adopted a password manager!).
Bottom line, I'm disappointed to report that passkeys don't appear worth the complexity of implementation (which is substantial!) nor the complexity and gotchas of the user experience. So we're sticking to passwords and emails. Encouraging opt-in 2FA and password managers, but not requiring them.
Passkeys seemed promising, but not all good intentions result in good solutions.
