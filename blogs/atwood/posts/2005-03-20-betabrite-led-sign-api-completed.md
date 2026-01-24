---
title: "BetaBrite LED Sign API completed"
date: 2005-03-20
url: https://blog.codinghorror.com/betabrite-led-sign-api-completed/
slug: betabrite-led-sign-api-completed
word_count: 174
---

As I mentioned in [Automated Continuous Integration and the BetaBrite LED Sign](https://blog.codinghorror.com/automated-continuous-integration-and-the-betabrite-led-sign/):


> *I’m currently working on some .NET classes that wrap a BetaBrite-specific subset of the *[*Alpha Sign Communications Protocol*](https://web.archive.org/web/20050404030338/http://www.ams-i.com/Pages/97088061.htm)*. This requires serial communication via a 25 or 50 foot RS-232 serial to RJ-12 cable, so you’ll need a physical PC with either a serial port or a USB-to-Serial adapter to get this working.*


This is now ready for public consumption. I posted it as a new article on CodeProject, [BetaBrite LED Sign API](https://web.archive.org/web/20050401015310/http://www.codeproject.com/useritems/BetaBriteAPI.asp) - A simple API for controlling a BetaBrite LED sign via RS-232 serial commands.


Here’s a sample:

kg-card-begin: html

```
Dim bb As New BetaBrite.Sign(1)
With bb
.Open()
.UseMemoryText("D"c, 128)
.UseMemoryText("E"c, 128)
.UseMemoryText("F"c, 128)
.AllocateMemory()
.SetText("D"c, _
"This is file D", _
Transition.Rotate)
.SetText("E"c, _
"This is file E", _
Transition.WipeLeft)
SetText("F"c, _
"time is ", _
Transition.RollDown)
.SetRunSequence("EDF")
.Close()
End With
```

kg-card-end: html

It really came out nicely. Now go get you some of that sweet, hot LED sign action!

[.net](https://blog.codinghorror.com/tag/net/)
[api](https://blog.codinghorror.com/tag/api/)
[serial communication](https://blog.codinghorror.com/tag/serial-communication/)
[betabrite](https://blog.codinghorror.com/tag/betabrite/)
[led sign](https://blog.codinghorror.com/tag/led-sign/)
