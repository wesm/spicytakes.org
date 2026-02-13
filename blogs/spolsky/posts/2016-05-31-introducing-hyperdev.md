---
title: "Introducing HyperDev"
date: 2016-05-31
url: https://www.joelonsoftware.com/2016/05/31/introducing-hyperdev/
word_count: 1441
---


One more thing…


It’s been awhile since we launched a whole new product at Fog Creek Software (the last one was [Trello](https://trello.com/), and that’s [doing pretty well](http://www.forbes.com/sites/alexkonrad/2016/05/23/trello-get-serious-about-big-businesses-as-it-passes-1-1-million-daily-users-and-triples-sales/#fed92956ce27)). Today we’re announcing the public beta of [HyperDev](https://hyperdev.com/), a developer playground for building full-stack web-apps fast.


HyperDev is going to be the fastest way to bang out code and get it running on the internet. We want to eliminate 100% of the complicated administrative details around getting code up and running on a website. The best way to explain that is with a little tour.


Step one. You go to hyperdev.com.


Boom. Your new website is already running. You have your own private virtual machine (well, really it’s a container but you don’t have to care about that or know what that means) running on the internet at its own, custom URL which you can already give people and they can already go to it and see the simple code we started you out with.


All that happened just because you went to hyperdev.com.


Notice what you DIDN’T do.

- You didn’t make an account.
- You didn’t use Git. Or any version control, really.
- You didn’t deal with name servers.
- You didn’t sign up with a hosting provider.
- You didn’t provision a server.
- You didn’t install an operating system or a LAMP stack or Node or operating systems or anything.
- You didn’t configure the server.
- You didn’t figure out how to integrate and deploy your code.


You just went to hyperdev.com. Try it now!


What do you see in your browser?


Well, you’re seeing a basic IDE. There’s a little button that says SHOW and when you click on that, another browser window opens up showing you your website as it appears to the world. Notice that we invented a unique name for you.


Over there in the IDE, in the bottom left, you see some client side files. One of them is called index.html. You know what to do, right? Click on index.html and make a couple of changes to the text.


Now here’s something that is already a little bit magic… As you type changes into the IDE, without saving, those changes are deploying to your new web server and we’re refreshing the web browser for you, so those changes are appearing almost instantly, both in your browser and for anyone else on the internet visiting your URL.


Again, notice what you DIDN’T do:

- You didn’t hit a “save” button.
- You didn’t commit to Git.
- You didn’t push.
- You didn’t run a deployment script.
- You didn’t restart the web server.
- You didn’t refresh the page on your web browser.


You just typed some changes and BOOM they appeared.


OK, so far so good. That’s a little bit like jsFiddle or Stack Overflow snippets, right? NBD.


But let’s look around the IDE some more. In the top left, you see some server side files. These are actual code that actually runs on the actual (virtual) server that we’re running for you. It’s running node. If you go into the server.js file you see a bunch of JavaScript. Now change something there, and watch your window over on the right.


Magic again… the changes you are making to the server-side Javascript code are already deployed and they’re already showing up live in the web browser you’re pointing at your URL.


Literally every change you make is instantly saved, uploaded to the server, the server is restarted with the new code, and your browser is refreshed, all within half a second. So now your server-side code changes are instantly deployed, and once again, notice that you didn’t:

- Save
- Do Git incantations
- Deploy
- Buy and configure a continuous integration solution
- Restart anything
- Send any SIGHUPs


You just changed the code and it was already reflected on the live server.


Now you’re starting to get the idea of HyperDev. It’s just a SUPER FAST way to get running code up on the internet without dealing with any administrative headaches that are not related to your code.


Ok, now I think I know the next question you’re going to ask me.


“Wait a minute,” you’re going to ask. “If I’m not using Git, is this a single-developer solution?”


No. There’s an Invite button in the top left. You can use that to get a link that you give your friends. When they go to that link, they’ll be editing, live, with you, in the same documents. It’s a magical kind of team programming where everything shows up instantly, like Trello, or Google Docs. It is a magical thing to collaborate with a team of two or three or four people banging away on different parts of the code at the same time without a source control system. It’s remarkably productive; you can dive in and help each other or you can each work on different parts of the code.


“This doesn’t make sense. How is the code not permanently broken? You can’t just sync all our changes continuously!”


You’d be surprised just how well it does work, for most small teams and most simple programming projects. Listen, this is not the future of all software development. Professional software development teams will continue to use professional, robust tools like Git and that’s great. But it’s surprising how just having continuous merging and reliable Undo solves the “version control” problem for all kinds of simple coding problems. And it really does create an insanely addictive form of collaboration that supercharges your team productivity.


“What if I literally type ‘DELETE * FROM USERS’ on my way to typing ‘WHERE id=9283’, do I lose all my user data?”


Erm… yes. Don’t do that. This doesn’t come up that often, to be honest, and we’re going to add the world’s simplest “branch” feature so that optionally you can have a “dev” and “live” branch, but for now, yeah, you’d be surprised at how well this works in practice even though in theory it sounds terrifying.


“Does it have to be JavaScript?”


Right now the server we gave you is running Node so today it has to be JavaScript. We’ll add other languages soon.


“What can I do with my server?”


Anything you can do in Node. You can add any package you want just by editing package.json. So literally any working JavaScript you want to cut and paste from Stack Overflow is going to work fine.


“Is my server always up?”


If you don’t use it for a while, we’ll put your server to sleep, but it will never take more than a few seconds to restart. But yes for all intents and purposes, you can treat it like a reasonably reliably, 24/7 web server. This is still a beta so don’t ask me how many 9’s. You can have all the 8’s you want.


“Why would I trust my website to you? What if you go out of business?”


There’s nothing special about the container we gave you; it’s a generic VM running Node. There’s nothing special about the way we told you to write code; we do not give you special frameworks or libraries that will lock you in. Download your source code and host it anywhere and you’re back in business.


“How are you going to make money off of this?”


Aaaaaah! why do you care!


But seriously, the current plan is to have a free version for public / open source code you don’t mind sharing with the world. If you want private code, much like private repos, there will eventually be paid plans, and we’ll have corporate and enterprise versions. For now it’s all just a beta so don’t worry too much about that!


“What is the point of this Joel?”


As developers we have fantastic sets of amazing tools for building, creating, managing, testing, and deploying our source code. They’re powerful and can do anything you might need. But they’re usually too complex and too complicated for very simple projects. Useful little bits of code never get written because you dread the administration of setting up a new dev environment, source code repo, and server. New programmers and students are overwhelmed by the complexity of distributed version control when they’re still learning to write a while loop. Apps that might solve real problems never get written because of the friction of getting started.


Our theory here is that HyperDev can remove all the barriers to getting started and building useful things, and more great things will get built.


“What now?”


Really? Just go to [HyperDev](https://hyperdev.com/) and start playing!
