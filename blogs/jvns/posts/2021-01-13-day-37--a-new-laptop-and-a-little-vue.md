---
title: "Day 37: A new laptop and a little Vue"
date: 2021-01-13
url: https://jvns.ca/blog/2021/01/13/day-37--a-new-laptop-and-a-little-vue/
slug: day-37--a-new-laptop-and-a-little-vue
word_count: 850
---


Hello! Tuesday was mostly consumed by setting up a new laptop so I’ll keep this pretty short.


Things in this post:

- setting up the new laptop (very boring honestly but I seem to have written a lot about it anyway)
- switching to vue.js
- a problem I’m having with my setup for proxying SSH connection


### a new laptop arrived!


I bought a new laptop (a thinkpad t14s, the AMD one) and it arrived so of
course I got super distracted and had to set it up immediately. It’s quite a
bit faster than the old computer (a thinkpad x250) which is fun. I’m a bit mad
that it has soldered RAM and that in general it’s harder to service myself but
I went with it anyway.


### how I set up a new computer


Here’s how I set up a new computer and how I do OS upgrades. I’ve done this 3-4
times in the last 3 years and it works pretty well. The main things are:

- I copy my entire home directory to the new computer, which is kind of a
magical thing because it means all my settings are right there when I’m done
- I never upgrade Ubuntu, I always reinstall from scratch. (I tried breaking
this rule and upgrading Ubuntu this year and it failed very spectacularly so
I’m even more personally committed to this rule :) )

1. Go find my 1TB external drive in a box downstairs
2. Find a USB key and put the latest Ubuntu LTS installer on it


On the old computer: (or before rebooting, in the case of an upgrade)

1. Back up my home directory with `cd /home; sudo tar -cf - bork | pv | /media/the_drive/homedir.tar`. The `pv` is important to me because it takes a long time and I get impatient so it’s nice to have a progress indicator.
2. Run `sudo dpkg -l > /media/the_drive/packages`


on the new computer (or after rebooting)

1. Install Ubuntu with disk encryption, don’t bother setting up a partition table, format the whole drive
2. Unpackage my home directory from the external drive and put it back at `/home/bork` (`cat /media/the_drive/homedir.tar | pv | tar -xf -`)
3. Go through the list of packages from `dpkg -l` and manually pick out the ones I want to install and put them in a text file called `to_install` or something (usually there’s a bunch of crap I installed on the previous computer that I don’t necessarily need, so I find sorting through it manually is better)
4. Run `cat to_install | sudo xargs apt install`
5. Over the next few days/weeks, install everything I missed as I notice it


I don’t claim that this is the Best Way to do things, it’s just what I do and
it works ok for me so far. I used to keep my home directory in a separate
partition so I could easily reinstall my OS and leave my home directory alone
but I don’t anymore for some reason that I don’t remember.


### problems I still have with the new laptop


I have a bunch of the usual new computer problems:

- it doesn’t suspend when I close the lid yet
- something is a little wonky with my vim configuration and the top bar looks weird
- I got a new Yubikey Nano and I wanted to set PAM up so that I could `sudo`
without typing in a password, but the instructions on their website aren’t
working for me. I took this as an opportunity to learn a little about PAM so
I bought [Michael Lucas’s Pam Mastery
book](https://mwl.io/nonfiction/tools#pam) because I really like his writing.
It helped me get more debugging information about the issue but I still don’t
know what’s wrong.


### switching to vue.js


I’d been using a tiny bit of stimulus.js for my site. I was dissatisfied with
it because to conditionally show a div depending on the state I needed to add
CSS styles myself to show / hide content, like
`this.pendingDiv.classList.add('hidden')`


So I switched to vue.js which I’ve used for a few small projects before and
like and I like it better.


### a problem with my proxy server


While testing my new vue.js code, I noticed that my Javascript was working fine
but that I was having a problem on the backend.


I use this Go proxy server (`gotty`) to proxy SSH connections to my VMs. The way it works right now is:

- I start `gotty` processes from my Rails app
- each SSH connection gets its own port
- I have another Go proxy (100 lines of Go) that proxies `/proxy/SSH_CONNECTION_ID` to the port of the right backend processes
- the second go proxy find outs port to use by querying an endpoint in the Rails app


I find this whole thing pretty messy and it’s also quite unreliable, the
`gotty` processes sometimes don’t quite start up right and I’m always worried
about them dying and I have no real way to manage them. So I think I’ll work on
that next.
