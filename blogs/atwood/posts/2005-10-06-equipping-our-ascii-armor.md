---
title: "Equipping our ASCII Armor"
date: 2005-10-06
url: https://blog.codinghorror.com/equipping-our-ascii-armor/
slug: equipping-our-ascii-armor
word_count: 486
---

On one of our e-commerce web sites, we needed a unique transaction ID to pass to a third party reporting tool on the checkout pages. We already had a GUID on the page for internal use. And you know [how much we love GUIDs](https://blog.codinghorror.com/mastering-guids-with-occams-razor/)!

kg-card-begin: html

```
22da5537-de54-459d-9b33-f40f2101143b
```

kg-card-end: html

A GUID is 128 bits, or 16 bytes. And the third party can accept 20 bytes.


This seems workable until you realize that those 20 bytes have to be represented as a plain text string to be transmitted via HTTP in a form post or querystring.


So the question is, **how do we represent a 128-bit integer in a plain text string that fits in 20 characters?** In other words, we need to equip our [ASCII Armor](http://en.wikipedia.org/wiki/ASCII_Armor).


There’s a **Guid.ToByteArray()** method which returns an array of 16 bytes (0-255). So we could just use ASCII values 0-255 to represent each byte, right? But wait a minute. ASCII 13 is carriage return! And good luck sending ASCII 0 (aka null) to anyone. Hmm.


We’re forced to use only [printable ASCII characters](https://web.archive.org/web/20051028015550/http://web.cs.mun.ca/~michael/c/ascii-table.html). Which means we’ll have to use more bytes to represent the same data; it’s unavoidable. Let’s experiment with a few forms of ASCII armor and see how close we can get.


A **Hex encoded** GUID...

kg-card-begin: html

```
Dim g As Guid = Guid.NewGuid
Dim sb As New Text.StringBuilder
For Each b As Byte In g.ToByteArray
sb.Append(String.Format("{0:X2}", b))
Next
Console.WriteLine(sb.ToString)

```

kg-card-end: html

... uses ASCII values 0-9, A-F and results in a **32 byte** string:

kg-card-begin: html

```
EBB7EF914C29A6459A34EDCB61EB8C8F
```

kg-card-end: html

A [**UUEncoded**](https://web.archive.org/web/20050911173045/http://www.codeproject.com:80/dotnet/TextCoDec.asp) GUID...

kg-card-begin: html

```
Dim u As New UUEncode
Dim g As Guid = Guid.NewGuid
Dim s As String
s = u.Encode(g.ToByteArray)
Console.WriteLine(s)

```

kg-card-end: html

... uses ASCII values 32-95 (decimal) and results in a **25 byte** string:

kg-card-begin: html

```
0@-_;,9X-@D2BTV!0V$/TP``
```

kg-card-end: html

A [**Base64 encoded**](http://en.wikipedia.org/wiki/Base64) GUID...

kg-card-begin: html

```
Dim g As Guid = Guid.NewGuid
Dim s As String
s = Convert.ToBase64String(g.ToByteArray)
Console.WriteLine(s)

```

kg-card-end: html

... uses ASCII values a-z, A-Z, 0-9 and results in a **22 byte*** string:

kg-card-begin: html

```
7v26IM9P2kmVepd7ZxuXyQ==
```

kg-card-end: html

An [**ASCII85 encoded**](http://en.wikipedia.org/wiki/Ascii85) GUID...

kg-card-begin: html

```
Dim a As New Ascii85
Dim g As Guid = Guid.NewGuid
Dim s As String
s = a.Encode(g.ToByteArray)
Console.WriteLine(s)

```

kg-card-end: html

... uses ASCII values 33-118 (decimal) and results in a **20 byte** string:

kg-card-begin: html

```
[Rb*hlkkXVW+q4s(YSF0
```

kg-card-end: html

So it is possible to fit a complete GUID in 20 printable ASCII characters using the latest and greatest ASCII Armor. But just barely!


In the process of writing this entry, I couldn’t find any C# or VB.NET implementations of ASCII85, so I wrote one. I’ll have source code up for that shortly.


*The trailing “==” in Base64 is an end of line marker and should not count towards the character total.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[security](https://blog.codinghorror.com/tag/security/)
[encoding](https://blog.codinghorror.com/tag/encoding/)
[ascii](https://blog.codinghorror.com/tag/ascii/)
