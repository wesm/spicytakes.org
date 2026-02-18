---
title: "A Public Service Announcement Regarding ‘callto:’ URIs and Safari"
date: 2005-12-16
url: https://daringfireball.net/2005/12/callto_uris_safari
slug: callto_uris_safari
word_count: 316
---


[Skype](http://skype.com/) — the high-fidelity voice over IP chat/phone service —
supports the “callto:” URI scheme. What this means is that in the same
way a “mailto:” link can be used to initiate a new email message from
a web page:


```
<a href="mailto:[email protected]">Send me an email</a>

```


you can use a “callto:” URI to initiate a Skype call. To send a
message to someone with the Skype username “example”:


```
<a href="callto://example">Call me on Skype</a>

```


Using the “SkypeOut” feature, you can use Skype to make phone calls,
which for international calls can be remarkably cheaper than direct
phone-to-phone connections. Just use the phone number in place of the
Skype username, prefixed by an international calling code (“+1”
within the U.S.):


```
<a href="callto://+12125551234">Call my phone from Skype.</a>

```


Except that last example won’t work from Safari: “callto://*username*”
URIs work just fine; “callto://*phonenumber* URIs don’t work at all.
You click them and nothing happens.


The solution is not to use the slashes after the “callto:” scheme:


```
<a href="callto:+15558675309">Jenny, you got my number.</a>

```


and they’ll work just fine. I have no idea which format is “correct”,
but given that “mailto:” URIs have never used slashes, my money is on
the no-slash format being canonical. The most authoritative source I
could find is [this MSDN “CallTo URL” developer documentation](http://msdn.microsoft.com/library/default.asp?url=/library/EN-US/netmeet/nm3_1l4o.asp),
which indicates the slashes should not be included.


Firefox (and other Mozilla-derived browsers, such as Camino) work just
fine with “callto:” URIs with or without the “//”; Safari allows for
the “//” if the recipient is a Skype username, but *not* if it’s a
phone number.


So if you’re working on Skype integration — or, as [we](http://joyent.com/) call it in the
Web 2.0 world, a “Skype mash-up” — don’t use slashes in your
“callto:” URIs if you want them to work in Safari.



| **Previous:** | [‘Restart Apache’ AppleScript](https://daringfireball.net/2005/11/restart_apache_applescript) |
| **Next:** | [Merry](https://daringfireball.net/2005/12/merry) |


PreviousNext