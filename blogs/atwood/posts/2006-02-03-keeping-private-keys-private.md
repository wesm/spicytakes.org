---
title: "Keeping Private Keys Private"
date: 2006-02-03
url: https://blog.codinghorror.com/keeping-private-keys-private/
slug: keeping-private-keys-private
word_count: 610
---

After I posted the CodeProject article .NET Encryption Simplified, a reader asked this question in the comments:


> *I would like to know what your thoughts are on private key storage in applications. I believe the recommended practice is to use the DPAPI, but I have found this to be too cumbersome for practical use. I would like to encrypt certain aspects of my apps and even parts of my database, but without secure key storage it is pointless. Thoughts?*


The class in that article is suitable for most encryption scenarios, but I was using it in a web service. That meant **I had the luxury of keeping my private key on a different physical server**. I had never even considered the problem of private key storage on the same machine!


At the risk of belaboring the obvious, asymmetric encryption hinges on keeping the public key public, and the private key private. This is a snap if you’re doing cross-machine calls. You slap the private key on your server, and freely distribute the public key to clients. The private key is never transmitted over the network, so unless a disgruntled user manages to battle his way into your data center and *physically access your server*, you’re secure. But if all the encryption work you’re doing is on the local machine, then the private key and the public key are both stored somewhere on the local machine. **How in the world do you keep the private key away from the prying eyes of the local user?**


It seems like an insoluble problem to me, since users have complete physical control over their own machines. However, a user named “bigals” posted this helpful response in the comments:

kg-card-begin: html

> *
> First of all, convert your private key to a PKCS12 file, which is a nice little container for private keys. Then you have a few options for **storing the private key**:
> **In your machine's key store.**
> This is not as safe as the user store, as it can be accessed by any user if they have enough permissions.
> **In the current user's key store.**
> This is more secure than the machine store, because it's protected by windows ACL's. But it can play havok on you if passwords and permissions are changed for that particular user.
> **In the registry.**
> You can use ACL's to protect the registry key.
> **On a [smart card](https://web.archive.org/web/20060703220225/http://www.microsoft.com/technet/security/topics/identitymanagement/scard.mspx).**
> The CryptoAPI has native support for this.
> Smart cards can be removed and secured.
> The keys are never stored on the machine, so it is a very secure solution.
> Remember, never store an instance of your keys or passwords in a string!
> The .NET GC does not clear these values very well, and they are visible in the string table memory for anyone to steal! .NET 2.0 has a new object called [SecureString](http://msdn2.microsoft.com/system.security.securestring.aspx), which [keeps strings in encrypted memory](https://web.archive.org/web/20060420163406/http://blogs.msdn.com/shawnfa/archive/2004/05/27/143254.aspx).
> *

kg-card-end: html

This is another reason why the user comments are  [the best part of a blog](https://blog.codinghorror.com/if-youre-reading-this-you-are-a-low-value-demographic/). A two-way dialog between author and reader is often the difference between good content and *great* content.


The only way to keep a private key truly private is to store it on a completely different machine. If you must store the private key on the same machine, some vulnerability is inevitable. You can only make it *inconvenient* for a user to find the private key through software protection. If you want to make it really *difficult*, you have to embed the [private key in specialized hardware](https://web.archive.org/web/20060208040601/http://www.free60.org/wiki/Documentation), like the Xbox 360 does.

[security](https://blog.codinghorror.com/tag/security/)
[encryption](https://blog.codinghorror.com/tag/encryption/)
[key management](https://blog.codinghorror.com/tag/key-management/)
[dpapi](https://blog.codinghorror.com/tag/dpapi/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
