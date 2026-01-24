---
title: "Department of Declaration Redundancy Department"
date: 2008-06-19
url: https://blog.codinghorror.com/department-of-declaration-redundancy-department/
slug: department-of-declaration-redundancy-department
word_count: 404
---

I sometimes (often, actually) regress a few years mentally and forget to take advantage of new features afforded by the tools I’m using. In this case, we’re using the latest and greatest version of C#, which offers [implicitly typed local variables](http://msdn.microsoft.com/en-us/library/bb308966.aspx#csharp3.0overview_topic2). While [working on Stack Overflow](http://blog.stackoverflow.com/2008/06/gravatars-identicons-and-you/), I was absolutely thrilled to be able to refactor this code:

kg-card-begin: html

```

StringBuilder sb = new StringBuilder(256);
UTF8Encoding e = new UTF8Encoding();
MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

```

kg-card-end: html

Into this:

kg-card-begin: html

```

var sb = new StringBuilder(256);
var e = new UTF8Encoding();
var md5 = new MD5CryptoServiceProvider();

```

kg-card-end: html

It’s not dynamic typing, per se; C# is still very much a statically typed language. It’s more of a compiler trick, a baby step toward a world of [Static Typing Where Possible, Dynamic Typing When Needed](http://lambda-the-ultimate.org/node/834).


This may be a cheap parlor compiler trick, but it’s a welcome one. While writing C# code, I sometimes felt like I had entered the **Department of Redundancy Department**.


![](https://blog.codinghorror.com/content/images/2025/04/image-153.png)


Sure, there are times when failing to explicitly declare the type of an object can [hurt the readability and maintainability](http://www.25hoursaday.com/weblog/2008/05/21/C30ImplicitTypeDeclarationsToVarOrNotToVar.aspx) of your code. But having the option to implicitly declare type can be a huge quality of life improvement for everyday coding, too.


There’s always a [tradeoff between verbosity and conciseness](https://blog.codinghorror.com/in-defense-of-verbosity/), but I have an awfully hard time defending the unnecessarily verbose way objects were typically declared in C# and Java.

kg-card-begin: html

```

BufferedReader br = new BufferedReader (new FileReader(name));

```

kg-card-end: html

Who came up with this stuff?


Is there *really* any doubt what type of the variable br is? Does it help anyone, ever, to require another `BufferedReader` on the front of that line? This has bothered me for years, but it was an itch I just couldn’t scratch. Until now.


If that makes sense to you, why not infer more fundamental data types, too?

kg-card-begin: html

```

var url = “http://tinyurl.com/5pfvvy”;
var maxentries = 5;
var pi = 3.14159;
var n = new int[] {1, 2, 3};

```

kg-card-end: html

I use implicit variable typing whenever and wherever it makes my code more concise. Anything that **removes redundancy from our code** should be aggressively pursued – up to and including switching languages.


You might even say implicit variable typing is a gateway drug to more dynamically typed languages. And that’s a good thing.

[c#](https://blog.codinghorror.com/tag/c-2/)
[implicit typing](https://blog.codinghorror.com/tag/implicit-typing/)
[compiler trick](https://blog.codinghorror.com/tag/compiler-trick/)
[statically typed language](https://blog.codinghorror.com/tag/statically-typed-language/)
[programming trends](https://blog.codinghorror.com/tag/programming-trends/)
