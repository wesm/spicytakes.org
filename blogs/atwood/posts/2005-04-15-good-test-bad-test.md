---
title: "Good Test / Bad Test"
date: 2005-04-15
url: https://blog.codinghorror.com/good-test-bad-test/
slug: good-test-bad-test
word_count: 528
---

After years of building ad-hoc test harnesses, I finally adopted formal unit testing on a recent project of mine using [NUnit](http://www.nunit.org/) and [TestRunner](https://web.archive.org/web/20050418202914/http://www.mailframe.net/Products/TestRunner/). It was gratifyingly simple to get my first unit tests up and running:

kg-card-begin: html

```
<TestFixture()> _  
Public Class UnitTests  
Private _TargetString As String  
Private _TargetData As Encryption.Data  
<TestFixtureSetUp()> _  
Public Sub Setup()  
_TargetString = "an enigma wrapped in a mystery slathered in secret sauce"  
_TargetData = New Encryption.Data(_TargetString)  
End Sub  
<Test(), Category("Symmetric")> _  
Public Sub MyTest()  
Dim s As New Encryption.Symmetric(Encryption.Symmetric.Providers.DES)  
Dim encryptedData As Encryption.Data  
Dim decryptedData As Encryption.Data  
encryptedData = s.Encrypt(_TargetData)  
decryptedData = s.Decrypt(encryptedData)  
Assert.AreEqual(_TargetString, decryptedData.ToString)  
End Sub  
End Class 
```

kg-card-end: html

It’s a great system because I can tell what it does and how it works just by looking at it. You can’t knock simplicity. The problem with unit testing, then, is not the implementation. It’s determining what to test. And how to test it. Or, more philosophically, **what makes a good test?**


You’ll get no argument from me on the fundamental value of unit testing. Even the most trivially basic unit test, as shown in the code sample above, is a huge step up from the testing most developers perform – which is to say, **most developers don’t test at all!** They key in a few values at random and click a few buttons. If they don’t get any unhandled exceptions, that code is ready for QA!


The real value of unit testing is that **it forces you to stop and think about testing**. Instead of a willy-nilly ad-hoc process, it becomes a series of hard, unavoidable questions about the code you’ve just written:

- How do I test this?
- What kinds of tests should I run?
- What is the common, expected case?
- What are some possible unusual cases?
- How many external dependencies do I have?
- What system failures could I reasonably encounter here?


Unit tests don’t guarantee correct functioning of a program. I think it’s unreasonable to expect them to. But writing unit tests *does* guarantee that the developer has considered, however briefly, these truly difficult testing questions. And that’s clearly a step in the right direction.


One of the other things that struck me about unit testing was the challenge of balancing unit testing with the massive refactoring all of my projects tend to go through in their early stages of development. And, [as Unicode Andy points out](https://web.archive.org/web/20050427203647/http://www.twelve71.org/blogs/andy/000694.html), I’m not the only developer with this concern:


> *My main problem at the moment with unit tests is when I change a design I get a stack of failing tests. This means **I’m either going to write less tests or make fewer big design changes**. Both of which are bad things.*


To avoid this problem, I’m tempted to take the old-school position that tests should be coded later rather than sooner, which runs counter to the hippest theories of [test-first development](https://web.archive.org/web/20050529075802/http://www.xprogramming.com/xpmag/testFirstGuidelines.htm). How do you balance the need to write unit tests with the need to aggressively refactor your code? Does test-first reduce the refactoring burden, or do you add unit tests after your design has solidified?

[nunit](https://blog.codinghorror.com/tag/nunit/)
[testrunner](https://blog.codinghorror.com/tag/testrunner/)
[unit testing](https://blog.codinghorror.com/tag/unit-testing/)
[encryption](https://blog.codinghorror.com/tag/encryption/)
[symmetric encryption](https://blog.codinghorror.com/tag/symmetric-encryption/)
