---
title: "Why Isn’t My Encryption... Encrypting?"
date: 2009-05-17
url: https://blog.codinghorror.com/why-isnt-my-encryption-encrypting/
slug: why-isnt-my-encryption-encrypting
word_count: 853
---

It’s as true in life as it is in client-server programming: the only secret that can’t be compromised is the one you never revealed.


But sometimes, it’s unavoidable. If you *must* send a secret down to the client, you can encrypt it. The most common form of encryption is [symmetric encryption](http://en.wikipedia.org/wiki/Symmetric-key_algorithm), where the same key is used to both encrypt and decrypt. Most languages have relatively easy to use libraries in place for symmetric encryption. Here’s how we were doing it in .NET:

kg-card-begin: html

```

public static string Encrypt(string toEncrypt, string key, bool useHashing)
{
byte[] keyArray = UTF8Encoding.UTF8.GetBytes(key);
byte[] toEncryptArray = UTF8Encoding.UTF8.GetBytes(toEncrypt);
if (useHashing)
keyArray = new MD5CryptoServiceProvider().ComputeHash(keyArray);
var tdes = new TripleDESCryptoServiceProvider()
{ Key = keyArray, Mode = CipherMode.ECB, Padding = PaddingMode.PKCS7 };
ICryptoTransform cTransform = tdes.CreateEncryptor();
byte[] resultArray = cTransform.TransformFinalBlock(
toEncryptArray, 0, toEncryptArray.Length);
return Convert.ToBase64String(resultArray, 0, resultArray.Length);
}

```

kg-card-end: html

This is how our symmetric encryption function works:

1. We start with a secret string we want to protect. Let’s say it is “password123”.
2. We pick a key. Let’s use the key “key-m4st3r”.
3. Before encrypting, we’ll prefix our secret with a salt to [prevent dictionary attacks](https://blog.codinghorror.com/rainbow-hash-cracking/). Let’s call our salt “NaCl”.


We’d call the function like so:

kg-card-begin: html

```

Encrypt(“NaCl” + “password123”, “key-m4ast3r”, true);

```

kg-card-end: html

The output is a base64 encoded string of the [TripleDES encrypted](http://en.wikipedia.org/wiki/Triple_DES) byte data. **This encrypted data can now be sent to the client without any reasonable risk that the secret string will be revealed**. There’s always *unreasonable* risk, of the silent black government helicopter sort, but for all practical purposes there’s no way someone could discover that your password is “password123” unless your key is revealed.


In our case, we were using this `Encrypt()` method to experiment with **storing some state data in web pages related to the login process**. We thought it was secure, because the data was encrypted. Sure it’s encrypted! It says `Encrypt()` right there in the method name, right?


Wrong.


There’s a bug in that code. A bug that makes our encrypted state data vulnerable. Do you see it? My coding mistakes, [let me show you them!](https://web.archive.org/web/20090619183101if_/http://www.pantherkut.com/wp-content/uploads/2007/05/my_pokemons.jpg)

kg-card-begin: html

```

string key = “SuperSecretKey”;
Debug.WriteLine(
Encrypt(“try some different” +
“00000000000000000000000000000000”,
key, true).Base64ToHex());
Debug.WriteLine(
Encrypt(“salts” +
“00000000000000000000000000000000”,
key, true).Base64ToHex());
3908024fc33b55c3
4e885c8946b80735
704cbe2a41d25f21
81bb6d726bd35152
81bb6d726bd35152
81bb6d726bd35152
1367f10f2584ace3
4ae7661295a98e46
81bb6d726bd35152
81bb6d726bd35152
81bb6d726bd35152
4ee5d23b3b5e3eb4

```

kg-card-end: html

(I’m using strings with multiples of 8 here to make the Base64 conversions easier.)


Do you see the mistake now? It’s a short trip from here to unlimited data tampering, particularly since the state data from the login process contained user entered strings. An attacker could simply submit the form as many times as she likes, chop out the encrypted attack values from the middle, and insert them into the next encrypted request – **which will happily decrypt and be processed as if our code had sent it down!**


The culprit is this line of code:

kg-card-begin: html

```

{ Key = keyArray, Mode = CipherMode.ECB, Padding = PaddingMode.PKCS7 }

```

kg-card-end: html

Which, much to our embarrassment, is an *incredibly* [stupid parameter](http://msdn.microsoft.com/en-us/library/system.security.cryptography.ciphermode.aspx) to use in symmetric encryption:


> The Electronic Codebook (ECB) mode encrypts each block individually. This means that any blocks of plain text that are identical and are in the same message, or in a different message encrypted with the same key, will be transformed into identical cipher text blocks. If the plain text to be encrypted contains substantial repetition, it is feasible for the cipher text to be broken one block at a time. Also, it is possible for an active adversary to substitute and exchange individual blocks without detection.


It’s fairly standard for symmetric encryption algorithms to use feedback from the previous block to seed the next block. I honestly did not realize that it was *possible* to pick a cipher mode that did not do some kind of block chaining! `CipherMode.ECB`? More like `CipherMode.Fail`!


So, what have we learned?

1. **If it doesn’t *have* to be sent to the client, then don’t!** Secrets sent to the client can potentially be tampered with and compromised in various ways that aren’t easy to see or even predict. In our case, we can store login state on the server and avoid transmitting any of that state to the client altogether.
2. **It isn’t encryption until you’ve taken the time to fully understand the concepts behind the encryption code**. Specifically, we didn’t notice that our encryption function was using a highly questionable `CipherMode` that allowed block level substitution of the encrypted data.


Luckily, this was a somewhat experimental page on the site, so we were able to revert back to our standard server-side approach rather quickly once the exploit was discovered. I’m no [Bruce Schneier](http://www.schneier.com/), but I have a [reasonable grasp of encryption concepts](http://www.codeproject.com/KB/security/SimpleEncryption.aspx). And I *still* completely missed this problem.


So the next time you sit down to write some encryption code, consider the above two points carefully. Otherwise, like us, you’ll be left wondering **why your encryption isn’t... *encrypting***.


(Thanks to Daniel LeCheminant for his assistance in discovering this issue.)

[encryption](https://blog.codinghorror.com/tag/encryption/)
[security](https://blog.codinghorror.com/tag/security/)
[symmetric encryption](https://blog.codinghorror.com/tag/symmetric-encryption/)
[.net](https://blog.codinghorror.com/tag/net/)
[encryption libraries](https://blog.codinghorror.com/tag/encryption-libraries/)
