---
title: "Compiler, It Hurts When I Do This"
date: 2006-07-26
url: https://blog.codinghorror.com/compiler-it-hurts-when-i-do-this/
slug: compiler-it-hurts-when-i-do-this
word_count: 284
---

Here’s a question that recently came up on an internal mailing list: **how do I create an enum with a name that happens to be a c# keyword?**


I immediately knew the answer for VB.net; you use brackets to delimit the word.

kg-card-begin: html

Public Enum test
[Public]
[Private]
End Enum
Sub Main()
Dim e As test = test.Private
End Sub


kg-card-end: html
A little internet searching revealed that such things are called **escaped identifiers**, and the equivalent in c# is the @ character.
kg-card-begin: html


public enum test
{
@public,
@private
}
static void main()
{
test e = test.@private;
}


kg-card-end: html
They do work the same, but they don’t look the same. In c#, you have to type the unwanted escaped identifier every time you use the enum, and the enum even shows up with the @ prefix in intellisense. However, if you echo back the enum value, it will be “private,” and not “@private,” as expected.However, after spending 30 minutes researching the answer and playing with the results, I began to wonder if the real answer to this question should be another question: **why do you need to do this?** At some point it all becomes a little ridiculous. What’s next – an enum named “enum?” A variable named “variable?”Stop me if you’ve heard this one before:A man goes to a doctor’s office. He says, “Doctor, it hurts when I raise my arm over my head.”

The doctor replies, “Then don’t raise your arm over your head.”If the compiler is telling you it hurts when you do something, maybe you should stop doing it. Just something to consider before merrily swimming your way upstream.

[c#](https://blog.codinghorror.com/tag/c-2/)
[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[compiler](https://blog.codinghorror.com/tag/compiler/)
[enum](https://blog.codinghorror.com/tag/enum/)
[escaped identifiers](https://blog.codinghorror.com/tag/escaped-identifiers/)
