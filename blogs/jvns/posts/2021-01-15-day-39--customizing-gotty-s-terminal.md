---
title: "Day 39: Customizing gotty's terminal"
date: 2021-01-15
url: https://jvns.ca/blog/2021/01/15/day-39--customizing-gotty-s-terminal/
slug: day-39--customizing-gotty-s-terminal
word_count: 507
---


Yesterday I spent some time customizing gotty’s terminal from its default white
on black. I couldn’t find any explanation on the internet of how to do this, so
here’s what I did.


### step 1: find one of Blink Shell’s themes


I knew that gotty used HTerm, so I googled “HTerm themes” and found [this list of Blink Shell’s themes](https://github.com/blinksh/themes).


Blink Shell is an open source iPad SSH app (which I actually use sometimes on
my iPad!). It works great, but the important point here is that they apparently
use HTerm as their terminal and so they have a bunch of HTerm themes on GitHub.


For example, here’s the code for the Solarized theme:


```
t.prefs_.set('color-palette-overrides',["#002831", "#d11c24", "#738a05", "#a57706", "#2176c7", "#c61c6f", "#259286", "#eae3cb", "#001e27", "#bd3613", "#475b62", "#536870", "#708284", "#5956ba", "#819090", "#fcf4dc"]);
t.prefs_.set('foreground-color', "#536870");
t.prefs_.set('background-color', "#fcf4dc");
t.prefs_.set('cursor-color', 'rgba(83,104,112,0.5)');

```


### step 2: integrate  it into gotty


At first I tried just including that Javascript in my HTML file. But it said `t` was an undefined variable, so that didn’t work.


So instead I modified `gotty.js` to add these 3 lines:


```
if (setPrefs) { // julia: added this to set terminal colors
    setPrefs(term)
}

```


and put the theme code inside a `setPrefs` function:


```
function setPrefs(t) {
t.prefs_.set('color-palette-overrides',["#002831", "#d11c24", "#738a05", "#a57706", "#2176c7", "#c61c6f", "#259286", "#eae3cb", "#001e27", "#bd3613", "#475b62", "#536870", "#708284", "#5956ba", "#819090", "#fcf4dc"]);
t.prefs_.set('foreground-color', "#536870");
t.prefs_.set('background-color', "#fcf4dc");
t.prefs_.set('cursor-color', 'rgba(83,104,112,0.5)');
}

```


here are the two files I used:

- [https://gist.github.com/jvns/159d1e6415a756da634b298cbc6867e0#file-gotty-js-L22-L24](https://gist.github.com/jvns/159d1e6415a756da634b298cbc6867e0#file-gotty-js-L22-L24)
- [https://gist.github.com/jvns/b25bdfe7508b3d0782b800e5e4e80c47](https://gist.github.com/jvns/b25bdfe7508b3d0782b800e5e4e80c47)


### it still doesn’t look as good as I’d like


I’m not sure why, but even though the background color is right, it doesn’t look as good as the
Solarized theme I have in my terminal on my laptop.


Here’s my laptop’s terminal:


![](https://jvns.ca/images/shell-laptop.png)


and here’s the VM terminal via `gotty`:


![](https://jvns.ca/images/gotty-solarized.png)


I think some of the differences are because I’m using fish on my laptop and
bash on the VM, but the gray directories really seem wrong to me.


I’ve never really understand shell colors so maybe this will be the reason I finally learn.


### also started pushing images to github’s container registry


I also improved my deployment a bit yesterday by pushing Docker images to a registry instead of building them on my server.


This was important because the server is pretty slow, so it would use 100% of the CPU for like
5 minutes on building the images when I deployed and make the server super slow.


So now when I deploy, instead of running this on the server:


```
docker-compose build; docker-compose up

```


I run


```
docker-compose pull; docker-compose up

```


It’s way faster and also feels like it’s going to be more reliable. I
also wasted a bunch of hours trying to build the images in CI but in the end I
decided to just build them om my laptop because I couldn’t get Docker image caching to work with github actions.


This took a long time like things like this always do but it was pretty boring
so I don’t have much more to say about it.
