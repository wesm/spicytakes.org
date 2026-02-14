---
title: "Back to windows after twenty years"
date: 2019-11-04
url: https://signalvnoise.com/svn3/back-to-windows-after-twenty-years/
slug: back-to-windows-after-twenty-years
word_count: 1201
---


Apple’s stubborn four-year refusal to fix the [terminally broken butterfly keyboard design](https://signalvnoise.com/svn3/the-macbook-keyboard-fiasco-is-surely-worse-than-apple-thinks/) led me to a crazy experiment last week: Giving Windows a try for the first time in twenty years.


Not really because I suddenly had some great curiosity about Windows, but because Apple’s infuriating failure to sell a reliable laptop reluctantly put me back in the market. So when I saw [the praise heaped](https://www.theverge.com/2019/10/28/20932406/microsoft-surface-laptop-3-13-5-inch-review-test-price-specs-features) upon the Surface Laptop 3, and particularly its keyboard, I thought, fuck it, let’s give it a try!


![](https://signalvnoise.com/assets/svn3/images/2019/11/IMG_3873.jpeg?fit=640%2C480&ssl=1)

*Looks good, doesn’t it?*


The buying experience was great. There was nobody in the store, so with four sales people just standing around, I got immediate attention, and typed away a few quick sentences on the keyboard. It felt good. Nice travel, slim chassis, sleek design. SOLD!


The initial setup experience was another pleasant surprise. The Cortana-narrated process felt like someone from the Xbox team had done the design. Fresh, modern, fun, and reassuring. Apple could take some notes on that.


But ultimately we got to the meat of this experience, and unfortunately the first bite didn’t quite match the sizzle. The font rendering in Windows remains excruciatingly poor to my eyes. It just looks bad. It reminded me of my number one grief with Android back in the 5.0 or whenever days, before someone at Google decided to do font rendering right (these days it’s great!). Ugh.


I accept that this is a personal failure of sorts. The Windows font rendering does not prevent you from using the device. It’s not like you can’t read the text. It’s just that I don’t enjoy it, and I don’t want to. So that was strike one.


But hey, I didn’t pluck down close to $1800 (with taxes) for a Windows laptop just to be scared off by poor font rendering, right? No. So I persevered and started setting up my development environment.


See, the whole reason I thought Windows might be a suitable alternative for me was all the enthusiasm around Windows Linux Subsystem (WSL). Basically putting all the *nix tooling at your fingertips, like it is on OSX, in a way that doesn’t require crazy hoops.


But it’s just not there. The first version of WSL is marred with terrible file-system performance, and I got to feel that right away, when I spent eons checking out a git repository via GitHub for Windows. A 10-second operation on OSX took 5-6 minutes on Windows.


I initially thought that I had installed WSL2, which promises to be better in some ways (though worse in others), but to do so required me to essentially run an alpha version of Windows 10. Okay, that’s a little adventurous, but hey, whatever, this was an experiment after all. (Unfortunately WSL2 doesn’t do anything to speed up work happening across the Windows/Linux boundary, in fact, it just makes it worse! So you kinda have to stick with Linux tooling inside of Linux, Windows outside. Defeating much of the point for me!).


So anyway, here I am, hours into trying to setup this laptop to run *nix tooling with Windows applications, running on the bleeding edge of Windows, digging through all sorts of write-ups and tutorials, and I finally, sorta, kinda get it going. But it’s neither fast nor pleasant nor intuitive in any way. And it feels like my toes are so stubbed and bloody by the end of the walk that I almost forgot why I started on this journey in the first place.


I mean, one thing is the alpha-level of the software required to even pursue this. Something else is the bizarre gates that Microsoft erects along the way. Want to run Docker for Windows on your brand new Surface Laptop 3? Sorry, can’t do that without buying an upgrade to Windows Pro (the $1800 Surface Laptop 3 apparently wasn’t expensive enough to warrant that designation, so it ships with the Home edition. Okay, sheesh).


The default Edge browser that ships with Windows 10 is also just kinda terrible. I clocked a 38 on the Speedometer 2.0 test, compared to the 125 that my MacBook Pro 13 ran with Safari. (But hey, there’s another beta version of Edge, the one that now uses the Chrominum rendering engine, and that got it to a more respectable 68.)


Anyway, I started this experiment on a Monday. I kept going all the way through Friday. Using the laptop as I would any other computer for the internet, and my new hobby of dealing with the stubbed toes of setting up a *nix development environment, but when I got to Saturday I just… gave up. It’s clearly not that this couldn’t be done. You can absolutely setup a new Windows laptop today to do *nix style development. You can get your VS Code going, install a bunch of alpha software, and eventually you’ll get there.


But for me, this just wasn’t worth it. I kept looking for things I liked about Windows, and I kept realizing that I just fell back on rationalizations like “I guess this isn’t SO bad?”. The only thing I really liked was the hardware, and really, the key (ha!) thing there was that the keyboard just worked. It’s a good keyboard, but I don’t know if I’d go as far as “great”. (I still prefer travel, control, and feel of the freestanding Apple Magic Keyboard 2).


What this experiment taught me, though, was just how much I actually like OSX. How much satisfaction I derive from its font rendering. How lovely my code looks in TextMate 2. How easy it is to live that *nix developer life, while still using a computer where everything (well, except that fucking keyboard!) mostly just works.


So the Surface Laptop 3 is going back to Microsoft. Kudos to them for the 30-day no questions return policy, and double kudos for making it so easy to wipe the machine for return (again, another area where Apple could learn!).


Windows still clearly isn’t for me. And I wouldn’t recommend it to any of our developers at Basecamp. But I kinda do wish that more people actually do make the switch. Apple needs the competition. We need to feel like there are real alternatives that not only are technically possible, but a joy to use. We need Microsoft to keep improving, and having more frustrated Apple users cross over, point out the flaws, and iron out the kinks, well, that’s only going to help.


I would absolutely give Windows another try in a few years, but for now, I’m just feeling #blessed that 90% of my work happens on an iMac with that lovely scissor-keyed Magic Keyboard 2. It’s not a real solution for lots of people who work on the go, but if you do most of your development at a desk, I’d check it out. Or be brave, go with Windows, make it better, you pioneer, you. You’ll have my utter admiration!


Also, Apple, please just fix those fucking keyboards. Provide proper restitution for the people who bought your broken shit. Stop gaslighting us all with your nonsense that this is only affecting extremely few people. It’s not. The situation is an unmitigated disaster.

