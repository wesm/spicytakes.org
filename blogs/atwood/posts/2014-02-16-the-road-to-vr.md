---
title: "The Road to VR"
date: 2014-02-16
url: https://blog.codinghorror.com/the-road-to-vr/
slug: the-road-to-vr
word_count: 1287
---

A month after I [wrote about](https://blog.codinghorror.com/you-dont-need-millions-of-dollars/) John Carmack, [he left id Software](https://web.archive.org/web/20131204170859/http://www.gamasutra.com/view/news/205539/John_Carmack_officially_leaves_id_Software.php) to become the CTO of Oculus. This was big news for two reasons:

1. Carmack *founded* id in the early 90s. An id Software without Carmack is like an Apple without Woz and Jobs. You wouldn’t leave the prestigious company you founded unless you had some pretty compelling new dreams to pursue.
2. [Oculus](http://www.oculusvr.com/) (update: now Meta) is the company many are betting will break VR headsets into the mainstream. And even if they don’t manage to pull that off, they are now the most credible contender to make serious headway towards consumer VR the industry has ever seen.


Virtual reality is the stuff of programmer legend. Every software engineer that’s ever read [Snow Crash](http://www.amazon.com/dp/B000FBJCJE/) (or more recently, the excellent [Ready Player One](http://www.amazon.com/dp/0307887448/)) has dreamed of jacking into the metaverse. But why *now?* Well, if you think of it in very coarse terms as strapping two smartphones on your face and writing clever glue software, modern consumer VR is a natural outcome of what Chris Anderson calls the “peace dividend of the smartphone wars” in [this article](http://www.foreignpolicy.com/articles/2013/04/29/epiphanies_from_chris_anderson):


> It’s hard to argue that we’re not in an exponential period of technological innovation. The personal drone is basically **the peace dividend of the smartphone wars, which is to say that the components in a smartphone – the sensors, the GPS, the camera, the ARM core processors, the wireless, the memory, the battery – all that stuff, which is being driven by the incredible economies of scale and innovation machines at Apple, Google, and others, is available for a few dollars.** They were essentially “unobtainium” 10 years ago. This is stuff that used to be military industrial technology; you can buy it at RadioShack now. I’ve never seen technology move faster than it’s moving right now, and that’s because of the supercomputer in your pocket.


It’s no coincidence that another [programming legend](https://blog.codinghorror.com/i-happen-to-like-heroic-coding/), Michael Abrash, is also head over heels in love with VR. He worked with Carmack on Quake, and joined Valve software in 2011. His recent treatises on VR are practically religious tomes – “excited” doesn’t even begin to cover it:

- [Why Virtual Reality Is Hard, and Where it Might be Going](http://media.steampowered.com/apps/valve/2013/MAbrashGDC2013.pdf) (2013, pdf)
- [What VR Could, Should, and Almost Certainly Will Be Within Two Years](http://media.steampowered.com/apps/abrashblog/Abrash%20Dev%20Days%202014.pdf) (2014, pdf)


I apologize that these are both PDFs, but like everything else Abrash writes, they are amazing. **You should read them. Closely.** I don’t call him [one of the best technical writers](https://blog.codinghorror.com/there-aint-no-such-thing-as-the-fastest-code/) I’ve ever encountered for nothing. If you find these interesting – and if you don’t, I will personally drive to your house and pull your damn geek card myself – you should also dip into his blog, which drills into the specific challenges VR presents.


I thought VR would be at best a novelty in my lifetime. I remember playing Dactyl Nightmare at a storefront in Boulder, Colorado in the mid 90s.


If nothing else, it is abundantly clear that even after all these years, VR presents deep, hairy technical challenges even on today’s insanely fast, crazily powerful hardware. That’s exactly the sort of problem suited to the off-the-charts skill level of legendary programmers like Abrash and Carmack. Having both of these guys working on the newest Oculus Rift prototype with an enthusiasm I haven’t felt since the early 90s means **we could be on the verge of a Doom or Quake style killer app breakthrough in VR.**


![](https://blog.codinghorror.com/content/images/2025/02/image-155.png)


There’s no shortage of breathless previews, such as [this one at Gizmodo](http://gizmodo.com/i-wore-the-new-oculus-rift-and-i-never-want-to-look-at-1496569598), which ends with:


> But if the original Oculus was a proof of concept, this model is proof that the concept is genius. There’s zero doubt in my mind that when the final version of this device comes out it is going to change the world. For me, today, already has.


I’m optimistic about the next generation of Oculus Rift. But cautiously so.


Thanks to a friend, I had an opportunity to borrow the older Oculus Rift developer kit. And to be honest… I wasn’t that impressed.

- It’s a big commitment to strap a giant, heavy device on your face with 3+ cables to your PC. You don’t just casually fire up a VR experience. It takes substantial setup and configuration to get it ready. And even after configuring it, entering and exiting that VR experience is a far cry from quickly sitting down in front of a TV and grabbing that extra controller, or turning on a tablet.
- Demos are great, but there aren’t many games in the Steam Store that support VR today, and the ones that do support VR can feel like artificially tacked on novelty experiences. I did try [Surgeon Simulator](http://www.surgeonsimulator2013.com/) 2013 which was satisfyingly hilarious.
- Having your eyes so close to the screens means the display is effectively very low resolution. And I mean *extremely* low resolution; I’m talking literally 320x200 type stuff. Everyone talks about the “screen door effect” which is the actual matrix of pixels. I personally found it very distracting, probably the number one thing that bothered me about the experience. Any kind of text was basically unreadable. The prototype is only 720p though, whereas the newer models will be 1080p. That will help, but the resolution problem was so severe to me that I’m not sure it’ll be enough.
- VR is a surprisingly anti-social hobby, even by gamer standards, which are, uh… low. Let me tell you, nothing is quite as boring as watching another person sit down, strap on a headset, and have an extended VR “experience.” I’m stifling a yawn just thinking about it. I suppose games could present a friendlier set of data on the screen for others to spectate while sending a different set of data to the VR headset, but most of the games we played showed the actual VR screen, which is extreme distort-o-vision to the naked eye. Not really something you can watch or enjoy.
- Wearing a good VR headset makes you suddenly realize how many other systems you need to add to the mix to get a truly *great* VR experience: headphones and awesome positional audio, some way of tracking your hand positions, perhaps an omnidirectional treadmill, and as we see with the Crystal Cove prototype, an external Kinect style camera to track your head position at absolute minimum. Eventually maybe even wear a suit to track your whole body. Notice how quickly we get into geez-this-is-a-lot-of-equipment territory.


The Oculus Rift prototype was an excellent and interesting and worthwhile experience, don’t get me wrong, but it was more of a tech demo than anything else. It felt a long way from something that I’d be comfortable donning on a regular basis.


I’ll leave you with Michael Abrash’s summary:

kg-card-begin: html

> Compelling consumer-priced VR hardware is coming, probably within two years
> It’s for real this time – we’ve built prototypes, and it’s pretty incredible
> Our technology should work for consumer products
> VR will be best and will evolve most rapidly on the PC
> Steam will support it well
> And we think it’s possible that it could transform the entire entertainment industry

kg-card-end: html

But that hardly does it justice; read the entire presentation (linked above).


If you want some of the hardest practical problems in computer science to work on, bringing VR to the world is as ambitious (and fun!) a goal in software and hardware engineering I can think of. So like any proper card-carrying geek, I’ll certainly be ordering the new Crystal Cove model of Oculus Rift as soon as it’s available.


It’s a start. Maybe a big one.

[virtual reality](https://blog.codinghorror.com/tag/virtual-reality/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
