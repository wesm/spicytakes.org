---
title: "Life, liberty, and the pursuit of privacy"
date: 2016-06-29
url: https://drewdevault.com/2016/06/29/Privacy-as-a-hobby.html
slug: Privacy-as-a-hobby
word_count: 1428
---

Privacy is my hobby, and should be a hobby of every technically competent
American. Within the eyes of the law I have a right to secure the privacy of my
information. At least that’s the current law - many officials are  [trying to
subvert that right](http://www.apple.com/customer-letter/) . I figure that we’d
better exercise that right while we have it, so that we know how to keep
exercising it once it’s illegal and all the information about it dries up.

One particularly annoying coworker often brings up, “what do you have to hide?”
Though it would defeat the purpose to explain what I’m hiding, let’s assume that
what I’m hiding is benign, at least legally speaking. I’m sure you can
understand why I don’t want  `~/Porn`  to be public information should my
equipment be seized after I publish this blog post and an incompetent (or angry)
investigator leaks it. Building secure facilities for housing secrets is fun!
That’s true even if there aren’t a lot of interesting secrets to hide there.

But the porn folder brings up an interesting point. I’m not ashamed to admit I
have one, but I would be uncomfortable with everyone being able to see it. Or
maybe I’m having an affair (a scandalous proposition for a single guy, I know)
and there are relevant texts are on my cell phone. Perhaps I suck at managing my
finances and the spreadsheets in my documents would tell you so. Maybe I have
embarrassing home videos of bedroom activities on my hard drive 1 . Maybe
there’s evidence that I’m a recovering alcoholic in my files. Maybe I’m a
closeted homosexual and my files prove it, and 10 years from now the homophobes
win and suddenly the country is more hostile to that. Maybe all of this is true
at once!

Keeping these things secret is an important right, and one I intend to exercise.
I don’t want to be accused of some crime and have my equipment seized and then
mishandled by incompetent officials and made public. I don’t want a jury chosen
to decide if I really stole that pack of gum when I was 8 and then have
unfavorable secrets leaked. Human nature might lead them to look on my case
unfavorably if they found out about all the tentacle porn or erotic Harry
Potter fanfics I’ve been secretly writing. Maybe an investigator finds something
they don’t understand, like a private key, and it ends up being exposed through
the proceedings. Maybe this private key proves that I’m Satoshi Nakamoto 2  and
my life is threatened when the case is closed because of it.

To the government:  **stay the fuck out of my right to encrypt** , or, as I
like to think of it, my right to use math. They will try, again and again, to
take it from us. They must never win.

The second act of this blog post is advice on how to go about securing your
privacy. The crucial bit of advice is that you must strive to understand the
systems you use for privacy and security. Look for their weak spots and be aware
of them. Don’t deceive yourself about how secure your systems are.

I try to identify pain points in my security model. Some of them will be hard
to swallow. The first one was Facebook - delete your account 3   4 . I did
this years ago. The second one was harder still - Google. I use an Android
phone running CyanogenMod without Google Play Services. I also don’t use GMail
or any Google services (I search with DuckDuckGo and add !sp to use StartPage if
necessary). Another one was not using Windows or OS X. This is easy for me but a
lot of people will bitch and moan about it. A valid privacy & security model
does not include Windows. OS X is an improvement but you’d be better off on
Linux. Even your non-technical family can surely figure out how to use Xubuntu
to surf the web.

I also use browser extensions to subvert tracking and ads. Ad networks have
severely fucked themselves by this point - I absolutely never trust any ads on
the web, and never will, period. Use software like
 [uBlock](https://github.com/gorhill/uBlock)  to get rid of trackers (and speed
up the web, bonus!). I also block lots of trackers in my /etc/hosts file -
 [check this out](https://github.com/StevenBlack/hosts) . Also check out
 [AdAway](https://free-software-for-android.github.io/AdAway/)  for Android.

These changes help to remove your need to trust that corporate interests will
be good stewards of your private information. This is very important - no amount
of encryption will help you if you give Google a GPS map of your every move 5 
and your search history 6  and information about basically every page on the
internet you visit 7 . And all of your emails and contacts and appointments on
your calendar. Google can be subpoenaed or subverted 8  and many other
companies won’t even try 9  to keep your data secret even when they aren’t
legally compelled to. I like this image from Maciej Cegłowski’s excellent
talk 10  on website obesity about the state of most websites:

When you give all of this information to Google, Facebook, and others, you’re
basically waiving your fifth amendment 11  rights.

Once you do have control of your information, there are steps you should take to
keep it secure. The answer is encryption. I use
 [dm-crypt](https://wiki.archlinux.org/index.php/Dm-crypt)  which allows me to
encrypt my entire hard drive on Linux. I’m prompted for a password on boot and
then everything proceeds (and I’ve never noticed any performance issues, for the
record).

I also do most of my mobile computing on a laptop running libreboot 12  with
100% open source software. The weak point here is that if your hardware is
compromised and you don’t know it, they could steal your password. One possible
solution is keeping your boot partition and perhaps another key on a flash
drive, but this doesn’t fully solve the problem. I suggest looking into things
like case intrusion detection and working on being aware of it when your
hardware is messed with.

I mentioned earlier that my phone is running CyanogenMod without any of the
Google apps. The weak point here is the radio, which is very insecure and likely
riddled with vulnerabilities. I intend to build my own phone soon with a
Raspberry Pi, where I can have more control over this - things like being able
to disconnect power to the radio or disconnect the microphone when not in use
will help.

I also self host my email, which was a huge pain in the ass to set up, but is
lovely now that I have it. At some point I intend to write a better mail server
to make this easier. I use opportunistic PGP encryption for my emails, but I
send depressingly few encrypted emails like this due to poor adoption (follow me
on  [keybase](https://keybase.io/sircmpwn) ? I’ll give you an invitation if you
send me an encrypted email asking for one!)

If you have any questions about how to implement any of this, help identifying
the weaknesses in your setup, or anything else, please feel free to reach out to
me via email ( [sir@cmpwn.com](mailto:sir@cmpwn.com) + [F4EA1B88](/publickey.txt) )
or  [Twitter](https://twitter.com/sircmpwn)  or whatever. Good luck sticking it to
the man!

1. [ICloud leaks of celebrity photos](https://en.wikipedia.org/wiki/ICloud_leaks_of_celebrity_photos) ↩︎
2. The secretive inventor of Bitcoin. I’m not Satoshi, if you were wondering. ↩︎
3. [Click this](https://www.facebook.com/help/delete_account?rdrhc) to do so ↩︎
4. “But I liiiiike Facebook and it let’s me keep up with my frieeeends…” There’s no privacy model that includes Facebook and works. Give up. [Read this](https://stallman.org/facebook.html) and try to ignore the childish language and see the tangible evidence instead. ↩︎
5. If you have location services enabled on your phone, [here’s a map of everywhere you’ve been](https://maps.google.com/locationhistory/). Enjoy! ↩︎
6. [Here’s all of your searches](https://myactivity.google.com/myactivity). You can delete the history here, supposedly. I bet it doesn’t unfeed that history to your personal advertising neural network at Google. ↩︎
7. Google Adsense and Google Analytics are present on basically every website. I’m positive they’re writing it down somewhere when you hit a page with those on it. Facebook certainly is, too. ↩︎
8. Remember [PRISM](https://en.wikipedia.org/wiki/PRISM)? ↩︎
9. [Like AT&T, for example](http://www.pbs.org/newshour/rundown/report-att-cooperated-extensively-nsa-sharing-billions-phone-email-records/) ↩︎
10. [The Website Obesity Crisis](http://idlewords.com/talks/website_obesity.htm) ↩︎
11. That’s the right to remain silent. Come on, you should know this. ↩︎
12. [libreboot](https://libreboot.org/) is an open source BIOS. I got my laptop from [minifree](https://minifree.org/), which directly supports the libreboot project with their profits. ↩︎
