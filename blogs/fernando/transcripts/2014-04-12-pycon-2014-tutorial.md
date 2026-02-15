---
title: "IPython in Depth: High Productivity Interactive and Parallel Python"
date: 2014-04-12
event: "PyCon US 2014"
video_type: "Tutorial"
video_url: "https://www.youtube.com/watch?v=XFw1JVXKJss"
transcribed: 2026-02-15
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

Okay, so it's officially 9.00, so I'm going to sort of get going for real. I think we're going to start recording. Are you guys recording already?

Okay, so good morning, everyone. Welcome to the IPython in-depth tutorial for PyCon 2014. My name is Fernando Perez. IPython was my afternoon hack 12 years ago and still going, but now it's the work of a large team of developers who do a lot of the hard work. I want to introduce you guys to Matthias Bussonnier, who's in the room.

Matthias is a core IPython developer, and he'll be helping us as a floating TA. So if you have any questions, you're always welcome to interrupt me, raise your hand. This is very interactive, so just raise your hand and interrupt me.

But if you do have a question that you'd like hands-on help at the keyboard, just flag Matthias, and he'll come over to your chair and try to help you. If you want to have a quick question where you don't want to break up the flow of the conversation, but you're always welcome to raise your hand, and I will try to answer any questions that come up. Okay, so we have a lot of ground to cover, so I'm going to get started right away. The first thing, I have a few minutes reserved for installation checks to make sure that everyone is going to be okay for the next three hours. I don't want people just watching.

I want you guys to be following along. It's meant to be a hands-on tutorial so that you actually develop some muscle memory when you do things yourselves, but for that I need you guys to have everything on your own machines and up and running smoothly. So if you installed IPython with either Anaconda or Enthought Canopy, I do need you guys to update to IPython 2.0. And I failed. I just realized just now that the instructions I originally gave didn't include this bit of information.

So I want you guys to make sure that if you open IPython in a terminal, you should see 2 point something. I don't care what comes after the 2, but 2 point something. As long as you have IPython 2 point something, you're good to go.

Okay, in terms of the version. If you don't, if you see IPython 1 point something, then you need to run this command if you're on Conda, this command if you're on Canopy. These are from the IPython website from the installation page.

So if you need, you can go to IPython.org and simply click on install and you will see these commands right there. Let me scroll so that you see. You'll see these commands right there. And on Linux, you can pip install. I have, if anyone needs a Windows or a Mac copy of the Anaconda installers, that's a big download.

We have copies on USB stick here. So if you do, raise your hand and we'll pass you the USB stick. The tutorial itself is on GitHub. I gave you guys the URL for that.

If you don't have it, you can go to GitHub and download it. That's a small, like a 3-meg download for the zip file. But I also have copies of that zip file here if you want to grab it from a USB stick. My last update to the materials on the tutorial was about 48 hours ago.

So if you pulled yesterday, you're good to go. Otherwise, you can do a Git pull or just grab it from here. Yes, the IPython in-depth link. You can click on the download zip file or you can Git clone it. It's up to you.

I will not be doing real-time updates to the tutorial. So if you don't have a Git clone, it doesn't matter. It's okay if you just have a zip file.

Okay, so quick show of hands. I want everyone to basically follow with me and do IPython at your terminal. And does this work for you? And if it doesn't work for someone, please let me know. The first few minutes were scheduled for this, so we will come and help you.

You should see 2, IPython 2. This is the first sanity check. Yes. Just the tutorial? Yeah, okay.

So the blue USB sticks don't have anaconda. The black USB sticks that are floating around have anaconda. If somebody needs anaconda, you need a black USB stick.

Okay, was someone raising your hand over here on this side of the room? No? Okay.

So everyone okay with this? Okay, step number 2 of the sanity check. Run import matplotlib. I don't care what version. As long as that works, you're good to go.

And if you don't have matplotlib, it's not a huge deal. We're not going to stop for this. It would be good if you have package manager and you can get it installed.

If you have trouble with this one, I don't want to stumble too much because we only need matplotlib for a tiny, tiny handful of things. And you can live without it. You'll just miss a couple of things and you can watch me do it on the screen.

So it's not a huge deal. But it would be good if you have it. Okay.

And the last sanity check is if anyone is on Windows and has Sophos antivirus running, you may have problems with not seeing output on the IPython notebook. And if that's the case, raise your hand and we will tell you what to do. We've figured out what the solution is. Well, Stack Overflow has it figured out.

But there is a way to solve the problem. But Sophos antivirus kills the web traffic that the notebook system relies on. So you will not see any output by default.

And there's a workaround. It's easy enough to do. So it's not a problem.

But I don't want you guys to freak out if you're on Windows and you have an antivirus. I don't know if Sophos is antivirus or firewall or both. But both.

Okay. So anyway, that thing basically kills the traffic that we need. If you have it and you're having trouble, don't worry. Just raise your hand. We'll help you.

So any questions with installation at this point? I want to make sure. Yes.

For only a tiny, tiny thing. And if you don't have it, it's not a big deal. You can use a print statement and you'll be fine. Yeah. Don't worry about it too much.

Do you have NumPy at least? Okay. It's not a big deal. I mean, I do need NumPy for a couple of things.

But it's also small. And Matplotlib really for order epsilon. So it's not a huge deal if you don't have it.

Any other installation questions? Yes. I don't exactly remember. Why don't you just grab it? I have it here on zip file where you can click on the GitHub URL, whatever you prefer.

If you don't have a Git clone, then it's better if you just copy it. I did update it, I think, last night, two nights ago, but late at night. So it might be better if you have an updated copy.

If you're on Git, just do a Git pull. Okay. Any other installation questions?

All right. So let's get started. So where I want you to be, just so that we're all on the same file system paths, is to open a terminal and go to wherever you put the tutorial material, wherever on your computer you downloaded or unpacked the zip file or cloned it. You should see something like that minus that file, that markdown file, that PyCon file is just my personal notes.

But you should see notebooks, tools, and the readme file. So while you're there, I want you to run IPython notebook. And you should see something like this come up.

Okay. You should see something that basically prints some stuff. That terminal is a terminal that you're going to leave alone.

And then we're going to go to a web browser. And most likely on your systems, the web browser may have actually popped up to the front of your screen because that's the default behavior. I have that disabled.

But that's the default behavior that it will actually open things. And we're going to do pretty much everything from the comfort of a web browser. And you should see something like this. Just that.

So I'm going to leave it. I actually have the notebook server already running, so I can leave that right there. For those of you on Windows, with the Sophos thing, the trick is to say apparently that does it.

So this is just for those of you on Windows. If you type IPython notebook dash dash IP equals localhost, apparently that, yes. Go figure. That port.

Okay. So it may be that that's sufficient for Sophos to leave you alone and let the traffic go through to have, even though 127.0.0.1 and localhost are the same thing, apparently Sophos filters on numeric addresses, but it doesn't filter on the name localhost. Go figure.

But this is just the workaround that we found on Stack Overflow for the specific combination of Windows and Sophos, which obviously I don't have that thing, so I don't test that regularly. But once you have the notebook running, you should see this. Okay.

So this is the application of the IPython notebook, and we're going to, this is all the materials are presented in this form. And the reason why I want you guys to be on 2.0 is because 2.0 lets us navigate the file system. Oh, actually, when you started, I'm sorry, when you started, this is what you should see, because I had already, I had that open yesterday, so my directory was one level down.

So this is what you should see, and everything that we need, all of the notebooks are in the notebooks subdirectory, which is right here. And if you see at the top, there's a notebook called index. So the index notebook has, let me close it here, the index notebook looks like this.

So now I want a check from the people in the back of the room on my font size level, and this is a 1024 resolution screen, so I'm a little limited in what I can do, but any wider? Bigger. Even bigger than this? Is that, no, I'm playing a balance. That's why I asked for the back of the room.

That's good, I need people to be able to see, but I'm constrained by the fact that this is a 1024 resolution screen. Is that big enough? And there are actually a couple of chairs available further up front if somebody would like to move further, but I do want to make sure that the people in the back of the room, and also the folks on video, because this is being recorded, I want to know if this is okay for the video recording font size-wise, if you think it's going to be readable. It's kind of annoying to watch a three-hour tutorial where you can't read anything on the screen.

Okay, so this is... So the first thing that was in the agenda, on the index right here, was a quick installation check, which is what we're doing for the first few minutes. Oh, actually, once I zoom this thing out, I don't see my watch. I'm going to put it right here so I can see it always.

So quick installation check. It seems like we're good. Any last questions on that? Everyone is actually running the notebook?

Okay. So, I'm sorry? Yes? Huh. You have the same problem?

That is really weird. Matias, could you have a quick look? Okay, I've never seen that before, but these are the joys of having 50 live people in a room. We find out about new things. Yes, question?

Excuse me? Are you connected to the internet? You shouldn't need to install MathJax. It'll pull it live from a CDN.

So as long as you're online, you shouldn't need it. Yeah, make sure that you actually are. Yeah. Yes, basically hit Google. Go to Google and make sure, because you may have a, I mean, the Wi-Fi is open in the sense that you get an IP address, but you don't get a routing IP address.

You can't get outside. So you have to go to the login page and type PyCon 2014 in the little field to actually, so make sure that, basically make sure you can hit Google. If you can't get out, then you're good to go. And Matthias is going to look into that weird non-clickable link problem. I have no idea what's going on.

It may be a bug. It may be a real bug of ours. I would try to hit just a page refresh to be sure, just do a page reload. And if that doesn't work, one last try while Matthias looks back there. Open the same URL that you had opened.

Open it in a private or incognito window of your browser. The thing is, it may be cached JavaScript, old, stale, cached JavaScript, and JavaScript caching in the browser is very pernicious and really tricky to get out of. And so, was it just refresh?

Okay, it seems like it's just a stale JavaScript issue. So either hit page refresh, and if that doesn't do it, open an incognito window, which begins completely without history and without a cache, and then it's good, and then you should be okay. Okay, just refresh was enough.

But if you ever see some bizarre misbehavior with the notebook, and especially if later on you start using IPython from Git, and you pull from what we've done recently, you may hit these issues where you have weird misbehavior because of stale JavaScript caches. Before you waste any time, the first sanity check that we've learned is reopen whatever you were trying to do in an incognito window. Those windows are born without history. They're born without cache.

So they don't inherit anything that you had before, and they're the first way to check whether, I mean it could really be a bug, but it's the first sanity check before wasting any time. Okay? All right.

So I am going to give you guys a very quick overview of sort of the key points of IPython in terms of what the project has on the website and a couple of links and resources for you guys, and then we'll dive into the material. So this is the IPython.org website. And we have lots of materials there. In particular, the links at the top are obviously valuable ones, the installation link that we just saw. We have links to our documentation.

This is the docs page, and the documentation always has a copy to the current stable version of the docs, which right now is the 2.x series, as well as the current in development. Basically, we do regular builds of the docs, whatever the current version of the docs in development. And we also have videos, if you're interested. We have talks and tutorials such as this one.

But in particular, I want to point you to the right, the right-hand side of the website, and there's a couple of links in there that are important. The first one is the help chat room. So the help chat room, if I open it, takes me here.

This is a hip chat room where the IPython developers and community members hang out. You can log in without an account. You just type your name or nickname or whatever, and you will be logged in if I type in here.

So this is me, and Matthias and I will both be logged in. And obviously, I will be able to be less responsive because I'll be speaking here, but that's another channel with which you can ask Matthias questions or you can ask each other, and there may be somebody else in the room who can help you. So it's useful to have this as a back channel for now, but this is always open, by the way. That link is always there.

So if you ever have a question about IPython, you can hop onto that help room. We're not guaranteed to be there, but if we are there, we'll try to help you, okay? So there is an IPython channel on Freenode. It still exists. We tend to hang out there less.

The reason we switched from IRC to HipChat was a lot of the support for things like automatic emailing, automatic integration with GitHub, GitHub issues get notified us right on HipChat, comments on GitHub, and you can spend time basically botting the hell out of an IRC server to get all those features, or you can pay a dollar a month. And so we went for the pay a dollar a month option. So IRC, the channel exists, but most of the core developers have switched to using the HipChat room. You're welcome to go to the IRC channel, and I think Min still is there sometimes, but we tend to use it less. It was just a matter of features and convenience with HipChat.

We have been looking. There's a new service that provides sort of HipChat-like functionality that is free called Gitter, G-I-T-T-E-R. We've been kind of exploring using it, but we haven't, we're still using HipChat.

So there's also links to Stack Overflow questions tagged with IPython. It's a useful place to post questions. There's a big community on Stack Overflow, as you all know. You can find help there. You can also post questions on our mailing list.

That mailing list, I'm going to close this window right here. That's, the mailing list is called IPython Dev, but we actually have consolidated our mailing lists into one. We used to have a users and developers list, but IPython really is very, first of all, it's a tool for development of software.

So we, it kind of made sense to have one. And second, we were trying to encourage the idea that our users can be our developers at any time. Anyone who's using IPython should be able to contribute to its development.

And so we wanted to encourage the notion of having a unified community, and we don't have so much traffic that we really, really need to segregate into user and developers. So the user list exists, but we typically, whenever anybody asks a question there, we ask that you post it over here, because we're mostly just monitoring this mailing list. It's useful for large-scale discussions. We also have, there's a wiki that has some useful information that is updated a little bit more frequently than the website. It's a standard GitHub wiki.

There's an IPython subreddit on Reddit, and the community posts their interesting stuff about IPython, questions, et cetera. And finally, and very importantly, you can always file bug reports about IPython on GitHub, as always. So if you spot anything that's a problem, let us know. And we do have way more open bugs than we would like. We have 700 open bugs, but we do have a decent track record of actually closing bugs.

We're close to 5,000 closed bugs. So we actually do close bugs. But obviously, I don't think any project keeps up with its bug list. And we're fairly aggressive at triaging. Truth in advertising, I'm going to be very, very honest with you.

We do look at bug reports, but unless it's a flagrant, really problematic bug, we tend, the reality is we tend to act a lot less on bug reports than we act on pull requests. And the reason is that we have a really small team, and the influx of pull requests is already... large enough to keep us pretty much at maximum bandwidth. So obviously, if a major bug is reported without a contribution as a pull request, yeah, we'll do something about it.

But in reality, bugs that come just with a request for, I would like this to be different or to be better or whatever, without an accompanying pull request, they just naturally get triaged. The reason is limited bandwidth and we really try to make sure that when people contribute code, we don't just drop them on the floor. We try to engage the contribution from the community as much as we can.

So if you simply report something that is not quite the way you like it, consider that mostly a post it for your own personal future to do, to come back and contribute it as a pull request in the future, if you really want something done about it, okay? And so, these are the community resources. I'm going to close things here.

So now, let me start with a very, very basic introduction to using the notebook. And for that, I am going to first, we have, the next part is an introductory notebook where we actually do have material. But let me go to the file menu and click new right here. Or if you were in this interface, you can click new notebook right here.

So I want everyone to do this. You should end up with a page that looks like this. And for now, all I want you guys to know is, type any code you want in there and hit shift enter. And you should see something like that. By the way, I'm using Python 2 by default.

IPython runs on Python 3 just fine. And so, if you have a Python 3 workflow, you can run IPython 3 notebook and it runs. If you installed everything on Python 3, it runs fine. It's completely Python 3 compliant. We actually run on a single source code base.

We don't even run Python 2 to 3. So, you can run from git master with a setup py develop or symlink package directories and it will run fine. So, did everyone get output? Or rather, because obviously I don't expect everyone answering yes all the time. Did anyone not get a bit of output?

One of the symptoms of the Sophos antivirus issue is that you can get everything to work but you don't see any output here. If anyone has that problem, raise your hand because from now on, now this really checks the full chain of the tools. Everything has to be working for this hello world to come back.

Okay. It seems we're good. So, the IPython notebook at its most basic is just a Python shell.

But it's a Python shell where I can go back into here and edit, and edit and hit shift enter again and re-execute. So, think of it as a Python shell but where each of these areas that we call cells is its own text area. And furthermore, you can edit multi-line code, which is annoying to do at the terminal, either in the default Python shell or in the IPython shell. And here, you can edit multiple lines of code.

So, think of these as little embedded text editors, which is really what they are. What we're using this gray area is actually an embedded code mirror instance. It's a JavaScript text editor.

So, it has full syntax highlighting, type completion, everything. It's an embedded entire text editor in that area where you can type arbitrary Python code and you can execute it. And shift enter executes the code.

Okay. So, that's, for now, all I needed to be able to do. And so, let's go back to the index.

So, I'm switching tabs in the browser here. So, let's go back to the index and click on the notebook basics notebook. Okay.

So, now, the entire tutorial is basically going to be you guys following together with me working through these notebooks. And when you open the notebook, what you get are basically two things. You get a dashboard page and you get the index.

So, let's look at these notebook pages. The dashboard page is this page right here, which has a listing of the current directory where you're sitting, right? And the listing of the current directory shows sub-directories and notebook files. It doesn't show every file in there because we don't know what to do with a JPEG or a Word document or an Excel spreadsheet.

So, we don't list every file. We only list files with an IPyNB extension. And we special case one thing.

If you have a file called index, it's always at the top. The idea being an index file lets you organize the content of that directory, kind of like the index.html file on a web server, so you can organize in there the contents of the directory to have links rather than forcing people to wade through the listing of the notebooks. And that's how this particular tutorial is organized. In fact, what you will see is I'm opening things from the index. There's actually more files in the directory than I have links in the index.

The reason is the tutorial really has material for additional things. And in three hours, I can only fit a certain part of it. So, I only linked for today to the part that I think we can reasonably cover, but all of the other notebooks are there.

And so, when you simply open, when you click on one of these, it opens that file. If I click on index, it will open it in the new tab. This is the index file that I've had open. The dashboard shows you, obviously, you can navigate down into subdirectories.

So here, if I go to figs, it says the notebooks list is empty. That directory actually has files, but they're not notebooks. It has figures. It also shows you a tab called running.

So if you click on the running tab, what this shows you are the notebooks that are currently active. The reason why we have that is because you can navigate your file system and start opening notebooks all over the place. Every time you open a new notebook, you spin up a new Python process, right? And you can end up with Python processes all over the place, and you may not remember where you started them all.

So this gives you a way of seeing where are all of your active notebooks. And you can click on shut down to stop the notebook process for any one of them. So if I shut this down, that notebook is gone. It didn't delete the file. It just stops the process, okay?

It simply stopped the process. This list can grow arbitrarily long. One recommendation that I have for you guys now that you're seeing this is I actually don't start the notebook server on a normal terminal. I go into a terminal, and I always open something like screen or tmux, and that's where I open the notebook. I don't know how to give this hint to Windows users because I don't know if there is an equivalent of screen or tmux for Windows.

Maybe there is. I don't know. But on Macs or on Linux, I strongly recommend that you run the notebook server inside of a screen or a tmux session.

The reason is because that way, that process is protected from you accidentally killing the terminal. It's protected from even you logging out of the graphical user interface environment or logging back in. The only thing that will kill the screen or tmux session is if you reboot your computer.

So short of rebooting the computer, you can keep that notebook server process there for a long time, navigate your file system, and just always know that if you go to 127.0.0.1.8.8.8.8, it's there, and it's available, and you can reopen it. If your browser crashes, nothing happens. If your terminal crashes, nothing happens.

So it's a useful thing. And I've had that happen a couple of times. When I've prepared a talk, I have many notebooks ready. And when connecting to the projector, something goes crazy with X11, and I have to log out and log back in again to make it work. Well, no big deal. tmux has everything ready.

The state is in the server. All I have to do is reopen the tabs on the browser, and I'm good to go in 30 seconds. So it's a tip on how to run it. There may be an equivalent Windows solution to have a terminal that protects its processes. I don't know.

Maybe Screen or tmux themselves have a Windows port. I simply don't know. Maybe under Seguin.

Okay. So the, in the notebook itself, so this, we already saw what the dashboard did and what it meant. And in the dashboard, by the way, you saw, for notebooks that are not active, you can delete them from here.

If you want, if you click on delete, if you click on delete, it will ask you if you actually want to delete the notebook. But you can't delete by default a running notebook. You first have to shut it down, okay?

So the notebook itself has, when you're in a notebook, what you have is an area here that is basically like a text editor. This is, I mean, the user interface should be fairly familiar to anyone who has used a text editor, because the first way to think about the notebook is basically like a text editor, but it can execute code as well. I mean, you're typing code, but you can type arbitrary text, but you can also execute code in here.

In addition to that, there's a menu bar, and there's a toolbar for common actions, and there's a title bar at the top. You can always toggle on and off the visibility of the header area if you don't need it, and I'm probably going to do that most of the time. If you end up using the notebook to give talks and presentations, I strongly recommend toggling both the header and the toolbar off and just leaving the menu bar. Everything you can do with both the header and the toolbar, you can do from the menu bar, and it gives you extra vertical space, which is always at a premium when giving a presentation. The menu, I'm not going to go into everything in the menu.

You guys can navigate there, ask me questions. It's fairly self-explanatory. What I do want to go over, let me toggle the toolbar again. The most frequent actions are the ones that I will highlight here in the toolbar.

So this is a save button. The notebook automatically saves every hundred, by default, every 120 seconds. It saves automatically your work, but you can save manually. There's a difference when you hit save manually. Look at what it said.

Watch this part for a second right here on the top right, what happens when I click save. It says, checkpoint created. So the autosave is running on a timer, but if you hit save, in addition, it gives you a checkpoint, and you can go back to that checkpoint if you want.

So it's basically like depth one version control. It's very silly, it's very simple. There's a hidden directory called .ipynb checkpoints, where it just dumps a copy. It's basically a way of giving you an alternative to say, I want to make sure that this is it, in case the autosave saves something while you're in the middle of it and you didn't want it. It gives you the option of having a quick way to go back.

We're not going to reinvent Git here, so we're not going to add branching and whatnot to this. This is just one simple way to checkpoint your work in addition to the autosave feature, because autosave sometimes is not what you want. We did add autosave because it was overwhelmingly requested by the community, but we added this as a way of giving you guys manual control.

So these are commands to insert new cells. So this will insert a new cell below the cell that you had highlighted. These are commands to do cut, copy, and paste, but at the cell level.

So the notebook document is structured as a sequence of cells. In this way, it's different from a word processor. A word processor is a linear sheet, and you don't have any particular demarcation of areas. You can have paragraphs, but those are just extra carriage returns in the middle of text. In the notebook, it's a little different.

As you see, whenever you click on an area, you see an outline. That's because the notebook is structured as a sequence of things that we call cells. These operations, like cut and copy and paste, operate at the whole cell level.

So we give you a way of selecting the entire cell and cutting it all in one shot, or pasting it. So this is when I do page reload, precisely so that I recover what I had. I recover this cell, so I can copy this cell or paste it and it's operating at the whole cell level. Right now, we don't yet have support for highlighting a group of cells together. That is really annoying, we know.

We are the ones who suffer the most from that limitation, but you don't have to report it because we're fully aware of it and we will fix it eventually. But right now, there is no way to do operations on a group of cells together. We only have cut, copy, paste at the single cell level.

So if you ever want to move like 20 cells from one part to the other of a notebook, good luck. It's a pain in the neck. The only way to do that is basically by operating on the underlying JSON data file by hand.

So make sure that you save a copy of the file before you do that. Yes. So you cannot copy and paste whole cells. We haven't implemented correctly support for cross, for entire data structures. You can copy and paste the content of the cells.

So we'll see in a minute when we edit, you can highlight what's on the inside, make a new cell and copy the content. But unfortunately, you can't copy the cell as a data structure or groups of cells. It's something that is definitely in the books for us to do.

So the question for the video recording was whether there was a way to copy and paste cells across notebooks. And so in addition to my answer, what Matias said was that somebody has written a Chrome-specific extension that will let you kind of hack that support in. So cut, copy and paste operate at the cell level. These buttons allow you to move, walk a cell up or down, so they let you reorder things. Because you can't highlight a group, doing this for more than two or three cells, if you need to move a section and it's made up of more than two or three cells, it becomes a little unwieldy because you have to move them one at a time.

And doing that with one or two is okay. Doing that with ten will drive you crazy. This is a command to run a cell. It's basically the same thing as doing shift enter. It simply runs a cell.

The reason we have a button for it is it works on iPad. So we don't have a mobile interface for IPython, a dedicated native mobile UI. But you can sort of get by. I probably wouldn't try to use it on a phone much.

But on a larger tablet, you can get by if you can type. And since, especially on Android, you can install keyboards that have composite events, like shift enter and control enter and things like that. On iPads, you can't replace the keyboard, the system keyboard, so we can't have composite events.

But you can click that little button and actually run cells. So in a pinch, you can actually edit these things and run them on an iPad. This command interrupts the kernel. This button interrupts the kernel, which means it's the equivalent of hitting control C at the terminal.

So we actually send an event all the way back to the kernel to try to interrupt it. And this command restarts the kernel. So when you restart a kernel, what it does is it kills the underlying Python process that you were running and creates a new one. It does not in any way refresh the page or change your document.

So what is happening here is you have your document with your code on the web browser and the actual Python process that's executing that code in the back, and you can decouple the two, which means you can, after you've done all the editing, you can kill the kernel process, get a fresh one, and run again. Question? No. The kernel state does not save the checkpoint.

So the question was, does the checkpoint operation save the kernel state? And the answer is no. The checkpoint operation checkpoints the notebook file only. We do not do anything about the kernel state. Yes, question in the back?

Do you mean that I want to interrupt or that I want to restart? To interrupt? Oh, I have a for loop, and it's doing something, and it's taking a while, and I realize that I don't want it, so I just hit control C. At the terminal, I would hit control C. Control C and here is copy.

I mean, in here, the key bindings are very much text editor, word processor-like. So if I want to stop that for loop, it's calculating something, and it's going to take a half hour, and I realize I don't want it, I can stop it with the interrupt command. Any more questions? I'm sorry? Undo, so that's a really good question, isn't it?

Is there any way to undo? No, unfortunately, we don't have undo support. The only undo that you have is if you cut the cell, it's in the clipboard, so you can paste it back, but it means it's pretty dangerous.

If you cut twice, that's it, right? So that's partly why we have autosave. That's partly why we have checkpointing. Implementing all these things in the web browser takes some work, and we don't have the Google Docs engineering team or the entire Microsoft Live Office engineering team. There's just a handful of us.

So, but pull requests, welcome. Remember, this is an open source project. You can make it better. Yes, question?

If you saved, yeah, that's why I reloaded right there, because I made a mistake, and I deleted, I cut a cell, and instead of, I was going to show pasting it back, but I clicked on copy instead of paste, and so it meant I just, first I cut a cell, and then I copied over that, so my clipboard was gone, and so I hit reload to refresh it quickly from the disk copy. I mean, this is inversion control, so I could, I mean, if anything went wrong, I could have gotten it from version control, but yes, question? So the question is, if you edit the JSON file by hand, are there any pitfalls?

And the pitfall is one missing comma. A single, a single syntactic mistake in the JSON that damages the structure of the JSON file will be enough for you to have a file that can't be opened as a notebook anymore. No, it's a flat, we'll look at the files later. They're flat JSON files on disk.

So if you're going to go do surgery on it, what I recommend is have a copy of it, right, and edit it, and make sure that it loads okay in the notebook again, and if it doesn't load, unfortunately, we don't provide a lot of detail, so if you're doing that and it doesn't load, one thing you can do is open it with, just do JSON.load S, JSON.load, and try to read it because the low level, it is a JSON file, so the low level JSON reader may give you information about where the corruption is, and you may be able to realize, oh, shoot, I missed a comma here, and go back with a text editor, but it's low level surgery that is really unpleasant. We are working on tools to make that better, but right now, it is what it is, okay? So the user interface of IPython.

So, oh, and then here, what we have is a selector for the type of a cell. Cells have types. And the type of a cell indicates how does IPython interpret what's inside the cell.

So by default, all cells are created as code cells. So when you saw me start and we typed print hello world, IPython assumed there's Python code in here, I'm gonna run it, okay? But cells can also contain markdown. They can contain raw content for conversion where we don't assume, we just leave it alone. You type whatever is in there is left alone.

And the idea is when you're putting in their content because you're at some point going to convert this notebook to some other form of output, and you will manage that output in the conversion pipeline downstream. So you know what to do with it and you just want it not to try to be rendered in any way, shape, or form. So we leave it as plain text.

And then we have six heading levels. Now, when you put text in the notebook and we'll have a closer look at putting markdown, you obviously can use heading levels in markdown. Markdown lets you put heading levels. Why did we add our own heading levels? We render heading levels in markdown, but if we put heading levels and you highlight them as this is heading one, this is heading two, we can analyze that notebook and know what the structure of the notebook is.

So for example, there's an extension to automatically create a table of contents for the notebook. Any heading gets an actual anchor. So we automatically put HTML anchors on headings, which means you can refer from one notebook to another notebook with relative URLs and the heading anchors, so that when you create cross-link tutorials and documentations and reading materials, you can refer to specific locations by anchors, whereas we do not do that if it's just markup inside of the markdown cells. And eventually, we hope to also provide things like an outline navigator or the ability to move whole sections, but for that, we need to know structural information about the file.

So we recommend that when you want to provide headings, you don't simply put pound pound for markdown, but you actually use our heading levels because we can help you. If you tell us what the structure of the file is, we can do more intelligent things. Okay? And finally, the cell toolbar, this lets you, it turns out that each of these cells has not only content, it also has metadata.

So you can actually switch and have each cell show you its metadata. So the metadata is a JSON data structure that you can edit arbitrarily. So think of metadata like function annotations for Python 3. It's metadata that we have no semantics pre-assumed upon. We simply allow you to edit the metadata.

It's a JSON dict, it's key value pairs, and you can put whatever you want in there. What we're doing with this is creating slots to annotate every part of a document so that you can tag every piece of it and then do interesting things with it. So for example, we have an extension, Matthias wrote an extension that lets you tag cells as slides and sub-slides and transitions in between slides, and we can generate a slide show out of a notebook automatically by interpreting that metadata. And you can add your own metadata and write filters that interpret the metadata in your own way.

So for example, for education, we're thinking of ways of having metadata tagged to create, say, a student version of a problem set and the instructor's version of a problem set by tagging cells as problem and solution, right? There's many ways that could be done, and this gives you a way to edit it, and it's pure JSON. I have installed Matthias' extension that basically gives me a way to mark cells as slides or sub-slides or fragments of slides, which are basically pre-cooked ways of inserting specific fields into the metadata. He wrote a little bit of JavaScript for that.

So you guys don't have that by default. That's an extension, but you would have the basic one that lets you do the editing of the metadata. And this button, you don't have it.

This is part of Matthias' slide show extension. So this is the toolbar. The header, the only thing that matters in the header really functionally is that you can rename the notebook by clicking on its name, but you can also get that from the file rename menu item.

And so now, one important point about the notebook is that as of 2.0, the user interface is modal. And it's modal, if anyone here uses VI, it has a VI flavor to it. It's not exactly VI, but it has a VI flavor. I'm an Emacs person, but I actually like it.

The reason why we did this is because we're trying to create something that works across all browsers, but we also want it to be very keyboard friendly. And it turns out that creating keyboard shortcuts that operate across browsers and operating systems in all combinations is effectively impossible because every combination of browser and operating system has some combination of meta keys and modifier keys already chosen. So our solution for that was to split the operation of the notebook into two modes, what we call edit mode and what we call command mode. Command mode is the mode where your actions operate at, let me toggle, get back to no, we don't need that.

So command mode is this mode where when I move up and down, I'm moving over cells, and the highlight is operating on entire cells. And edit mode, and edit mode is the mode that I get when I'm editing a cell, and it's indicated by the cell having instead of green highlight around it. So in here, I'm in edit mode, and this cell, and I can edit the content of the cell. When I render that cell, when I do shift enter, I get back and I'm back out into the next cell.

This is now in command mode, which has a gray outline, and the difference in color is a little faint. We're still fine tuning this. We may end up making those borders a little bit thicker. Yes, question?

So to go from command mode, which is this one, into edit, I hit enter into a cell. When I hit enter, I can edit the cell. Now, if I want to execute the cell, if it's a code cell, or I want to render the cell, if it's a text cell, I do shift enter, but you're running two computers. Question, yes, back here. I'll be happy to come over.

Yes, question? Yes, it is, it is. We can, it's all JavaScript. I don't remember how fully customizable, yes, they are, yes, yes. Yeah, with the new code, with the new code, it is possible.

There's a JavaScript table of functions that you can use to modify them and make your own. Yeah, and inside of the cells, you can toggle. CodeMirror has a Vim mode for inside of the, so if you want the editing part to be very Vim-like, you can configure CodeMirror itself to be in Vim mode, and for that one, what's that? Yeah, yeah, but the key map already exists. I mean, yeah, CodeMirror has it.

It's just toggling it on. I don't remember how, but if you ask on the, Matias may remember, but if not, we do have a dedicated Vim developer, and one of the guys in my team is a Vim guy, and I'm sure he knows how to toggle the key map to be a Vim key map. Matias might know, actually, off the top of his head. Yes, you have a question. Oh, just zoom in your browser.

Yeah, like the heading is like this, and here. Oh, so the heading level, so. Yeah, these are the. Yes, so go back to the one you were trying to show me.

So click there, and make it a heading, and now, yes, so that's a heading, so now you have to render it, so if you do Shift-Enter, it renders, okay? Anyone else needs a hand locally? I'm happy to come. Yes? You're going to render your whole document, or do you have to do it some other way?

So, I mean, I'd render it by itself. No, we don't have, we have a way to execute all the code in a notebook, but if you've left a bunch of un-rendered cells, I think we don't have a way to say, go and render all of them. Let me try one thing. It may be that if you reload the page, it does that, but this is a little bit of a hack. Yes, so, because when we load a page, we assume that markdown cells are rendered, if you've left like 50 un-rendered markdown cells, if you save them, you make sure that you hit Save to be fully checkpointed, if you reload it, then they'll all reopen in rendered mode.

Yes, question? Yes? There's an API, there's better than a schema, we have a formal API, you can use our API, and our API, that way you're not operating on raw JSON, you're saying new notebook, new cell, new section, new subsection, and so we provide a Python API for that, yeah.

Okay, so let's continue. Yes, you had a question? If you really need very real time output, you always have to call flush, but that's true even at the terminal, but yes, basically we try to capture output from, we try to flush the output buffers as fast as we can from the kernel, and send them in real time over WebSockets.

So, now, it's still true that sometimes if you really want real time output, you have to call sys.standardout.flush even at the console, right, because Python itself buffers output to some extent. What's that? Yeah, so you may still have to do that, but to the extent that that works in the terminal, we also, and our networking code flushes those buffers very often.

Okay, so let's continue. Are there any questions from this little sort of playing around exercise? Okay.

If you want, so shift-m merges one cell with the next cell below it, and control-shift-splits a cell wherever you happen to be. So, this is useful when, for example, I split more than I merge. I split very often cells when I copy a bunch of Python code, like from a script, or from some example online, and now I want to break it into chunks, right, so I often go in cutting.

But I also, yes, sometimes I merge, and we only have a shortcut for merging below, but you can also, from the menu, you can merge with the cell above. So you can also merge above from the menu. We only have a shortcut for merging with the next cell, kind of swallowing cells in sequence. True, the problem with that is that once you merge them, they're assumed to be of the same type.

So if you want to copy and paste a heading and a markdown in a block of code, we really need to have a way of copying a group of cells of different types and moving them around intelligently. We don't have that. No, it'll merge, but it'll swallow them.

Okay, so let's scroll down a little bit and have a very quick look at what the notebook files are so that you guys get a flavor for them. So, and this will actually show you also, I could just look at one of these notebook files with a text editor, but I wanna show it to you with our API so that you also get a sense for what our API looks like. So here, I'm gonna run this cell of code. And now, so this cell right here says, from IPython NB format import current. Current is the current version of the notebook format.

Whatever the current notebook you're using, that's what you get if you do import current. We also have, we archive previous versions so that it can load programmatically old notebooks if our format ever changes. But this allows you to import current.

Now I open the file, and I can read, I can read that notebook in pure JSON format, and what I get is a data structure. And a notebook has a worksheets data structure inside of it. One notebook can actually contain multiple sheets. We don't wanna emphasize this fact because this is probably gonna change, and we're most likely going to make a notebook have a single sheet for reasons that I don't wanna get into here.

But by now, you always access the first worksheet because there's only one. And then, you can say, show me the first five cells. So these are the first five cells that exist in the notebook, and as you can see here, each cell is a JSON data structure that has a cell type. In this case, it's a heading, so headings have a level. It has this metadata that I was talking about, and it has the actual source that's contained in it.

So the title of this particular notebook was IPython Notebook Basics, and so there it is. The second one is also a heading. The third one, this is the second one. The third one is markdown, and it has all of this markdown source, et cetera, et cetera.

So this API that lets you read notebooks also lets you create notebooks. So somebody in the back was asking me, can I do these things programmatically? And the answer is yes. You can auto-generate notebooks programmatically. We have examples on how to do that.

It's just using that nbformat API, which means somebody asked us a question recently on the main one and said, I wanna create a notebook where I actually emit code automatically. I wanna run certain analyses, but I know in advance most of what I wanna do, so I wanna pre-populate a notebook with blocks of text and blocks of code. And so you can emit a notebook that has all that.

If you can generate the source code, you can auto-generate them, and you can even execute a notebook at the command line. So you can actually pre-populate, pre-create notebooks, pre-execute them, and they will be filled in, and then you can open them later to view them and work on them further, but you can do all that as part of an automated test system, as part of an automated systems interaction with hardware, whatever. Okay, so I'm gonna close this notebook, and we're gonna go to the next one, which is called Beyond Plain Python, IPython Beyond Plain Python.

So we've already seen how to run code. Now what I'm going to talk about is in what ways is IPython at the code level, at the code execution level, in what ways is IPython more than the interactive Python prompt, okay? Because it turns out that what IPython does is it creates a superset of the Python interactive prompt experience. Everything that's valid Python is also valid in IPython.

So anything that you ever do at a Python prompt, you should be able to do in IPython. But you can do a lot more in IPython that's not valid in Python. We've taken liberty.

So running code, we've already seen how that works. But how about getting help? In IPython, if you simply hit question mark, we will open this part of the browser, we will open it with a pager. And it's a pager that you can resize if you drag it. You can make it go away if you click on its divider.

And that pager gives you help and information. So the basic help is basic help about IPython itself. So if you ask question mark, IPython will tell you a little bit about itself, okay? And this help, by the way, also works at the terminal.

So if I say help here, I also get a terminal pager. The same information works at the terminal as it works in the notebook. Now, question mark is everywhere in IPython.

So if I do import collections, which is part of the standard library, and I hit collections name tuple question mark, what I get down here is information about the name tuple object, okay? So we tell you what it is, where does it come from, what file does it come from on the file system, what is its definition, and what is its docstring. The standard library tends to have fairly limited docstrings when it has any at all.

So question mark on the standard library is not often very useful. Question mark on the scientific ecosystem tools tends to be very useful because in the scientific NumPy, SciPy, MatplotLib, all of the data analysis machinery, we've been very diligent in writing extensive docstrings with examples and lots of documentation. So if you type question mark on code from IPython itself or any of the scientific tools, you tend to get a lot of information. From the standard library, eh, it's gonna hit or miss.

Now, one question mark gives you some information. Two question marks try to give you more. Emphasis on try. We may not always find more, but what we do is we use the inspect module of the standard library about as aggressively as we can, and we try to dig into the object as deep as we can, and if we find the source code for it, we will highlight the source code for that object. And you can do this with any object.

In this case, I called onCounter, but you can call it, let's say that I wanna find out about the most common method. If instead I say most common, we will find the code for that method alone. So question mark and double question mark are very useful ways of digging into things in Python live all the time.

This is stuff that is in the Python standard library. We're just reusing the standard library, but we're reusing it very aggressively and making it just a simple character. You probably don't know all of the various parts of the inspect API that you have to use to do this, but you can remember, hey, one question mark tells me stuff, two tell me more. That seems easy enough.

And there's one final use of the question mark, which is what about if you don't quite know what it is that? you're looking for. But you have a vague idea that you may be looking for things that have the word int in them, but you're not sure if it's integer or it begins with int or ends in int. You can use ? with wildcards. In this case, I'm putting two wildcards, one at the beginning and one at the end. You can use only one of them.

And in that case, what ? does is it searches. It doesn't dig into any one object because you don't know the name, but it gives you things that match that pattern in your current namespace. And you can do that with top level names or you can do that with, or you can do that with dotted names, whatever if you're trying.

So we find this combination of things very useful to navigate code bases. Between finding out by doing this kind of search and then doing ? and ? to dig into objects, there's a surprising amount you can learn about libraries you're not familiar with and get moving with your work without even having to go and read documentation, especially with libraries that have good doc strings. Yes?

So everything I'm showing in this section called IPython beyond plain Python is actually part of the core of IPython and it will work in any IPython environment, terminal, QT console or web notebook. So this is part of the core code that runs inside of IPython. There's nothing specific about... There it is, all the same. The only difference is that in the notebook, the pager is this little pane that down here.

In the terminal, we use the system pager, that's all. And in here, you can dismiss it with Q. You can dismiss the notebook pager with Q just like you can dismiss the system pager with Q in a...at least on Unix systems.

So we have a command called %quickref that will give you a quick reference card. So we have a cheat sheet for all these things that I'm telling you. If you type %quickref, you will see this cheat sheet that summarizes the things that I've been saying just now.

Now, the next thing that is useful to know about IPython is path completion. So we have very aggressive code to do deep introspection of objects and path completion. And the path completion machinery in IPython is actually fully customizable. We path complete on file names. We path complete on objects.

We path complete on as much as we can. And you can write custom path completers that introspect your own objects. We've had people write path completers for IPython consoles that are connected to instruments. And when they path complete on the console, they send requests over the network to introspect hardware and actually retrieve real time data from hardware from instruments.

So you can do stuff like that if you really want to, okay? And path completion in the notebook will give you this. And as usual, if you start typing, it starts filtering the list like any completer, okay?

So interactively, it's just like a Python shell. It remembers the previous output with underscore. Underscore is always the value of the previous output.

But there is one difference, which is that in IPython, you can suppress the generation of output if you put a semicolon at the end of the last line. And this is actually useful many times, especially when plotting. Plotting libraries, you normally want to see the figure.

But many plotting libraries, in addition to creating a figure, they return internal output that you don't always need to see. So if you don't want that junk kind of in, and often the plot command is at the end of a bunch of work. And so if you put a semicolon, we suppress the generation of output. The code still executes, we just don't show any output, okay?

Now, underscore gives you the last output, but we also store these input and output prompts out here are not cosmetic, okay? What happens is any time there's an output with a number, we actually generate a variable called underscore and that number for you. These are auto-generated.

So in addition to the single underscore that the Python shell has, we have these underscore and every number that you've created. And there's also two global variables, one called in and one called out that you can. So the underscore 10 is actually stored also as out 10.

So you can access, well, I didn't, I guess I didn't, oh, I didn't generate a 10, but I do have an 11. So let's, for example, check this. For 11, is out 11, it's the same thing. You can, in addition to single underscore, we have two and three underscores for the last three. We don't try to do 10 underscores, that would be kind of silly, but we generally keep up to three underscores.

And similar to out, there's an in data structure, an underscore I with the last three and underscore I in numbers. So we actually keep the input and output history for you. And there's a command called %history that will print your own history. %history and the notebook is not so useful because you have your own code. It's very useful when you're working at a terminal and you want to see, oh, you know what?

What I was just doing, I want that bit of stuff and I want to put it in a file and I just want to copy paste it. So you can type, give me the last five lines of my history, give me all of my history, give me, give it to me with or without line numbers. So %history gives you your history with all kinds of options. In this case, what you're saying is, I want lines one through five of my history with line numbers. That's what the dash end does.

If I do this, you get it without line numbers. Okay? Question in the back? No. Well, you can put print statements, but we do not return each line of code.

We execute the code. You should think of a block of code as a Python script, right? In a script, when you run a Python script that has a bunch of statements, you don't see output from each line of code as it's produced unless you put an explicit print statement. You should think of each cell as a mini script with the catch that the very last expression, we do provide the result so that we thought a lot about this. The question, I'm sorry for the recording, the question was, can I see the output automatically of every line in a multiline block?

And so my answer is, think of it like a script. We thought a lot about how to best go about this. And so what we do is we actually compile, we compile the block of code, we divide it into self-contained expressions. It's not just the last line, it's the last expression.

So if it's a multiline block, it's the last executable block. But for that, we actually return the output only for the last one. And we felt it was the best compromise between giving for small one-line expressions and interactive feel, but also providing kind of scripting-like block behavior.

Okay? So, let me skip that short exercise for now because we have a fair amount of material that I still want to cover and I don't want to fall too far behind. Yes, question back there. Collapse? No, we don't have ways of collapsing code blocks yet.

We're probably going to add that for the published versions of the notebook online so that you can have a little way of basically toggle code in the published view. In the interactive session, we don't have that. One way to do that is to put it on a script and call %run on it. We'll see that command in a moment that lets you run an external script.

So sometimes I do that. If I have a bunch of comments set up, I put it on a PY file on disk that I edit with a text editor. And then I do %run in it or whatever, and then that gets executed.

Okay. So, now, if you start a line with exclamation, that line is not executed by IPython as Python code. It goes to the underlying operating system. Straight on modified OS.system, we send it to the operating system.

And so that lets you type shell-like commands right away, but we actually have a few tricks up our sleeve. And this is where we're beginning to diverge from the Python system. Look at that block of code. Files equals exclamation ls. We capture that into a variable.

So it lets, we let you capture. So now, we're starting to basically let you do kind of bash-like scripting but with Python, with civilized Python syntax instead of having to remember kind of the godforsaken bash syntax for loops and conditionals and all that. So you can say, files equals exclamation. And now, you have, and I can do here, ls. There is no file that starts with ab.

These are the files that have a in them. These are the files that have x in them. Okay. Yes, question in the front. ls minus what?

So what we get, what you get is a list. So we break down, we break down the output on list. We try to take, basically, what does Unix do with standard out? Standard out is accessed as a stream of lines. That's kind of the default mentality of Unix pipes.

So we tried to take that idea. And so we give you a list of lines. Now, in reality, it's a little bit more complicated than that. It's actually not a normal list. It's a special object that we call an SList.

So it looks like a list, but it actually has a few additional. You can access it as paths. So it actually has a few attributes. .l gives you a plain Python list. .s gives you the total string as a single block of text. And .p, I thought this gave you, oh, this one, this one is not, is not made of. If it's made of just pure paths, .p gives you a list of path objects.

So we try to do kind of useful things for scripting like, for Unix scripting like stuff with it. So it looks like a list, but it's exactly a list with a few tricks up its sleeve, okay? Now, when you send commands to the system, we actually let you expand Python variables.

So this, so if you put a dollar sign, we will actually expand the Python variable back before we send it to the shell. So now you start to see how you can basically do logic in Python and then send commands to the underlying operating system without having to do the logic in the shell. You can do the, you can basically mix and match, mix and match things.

So $files is actually expanding the value of the files variable as a string and then echoing that in the shell. Files is a Python variable, not a shell variable right now. So it's a little bit mind bending and I know it feels a little dirty, but it's surprisingly useful. And not only can you expand with $ just variables, but if you expand, I see you have a question.

Let me finish this one, I'll get to you. If you do braces, you can put arbitrary Python expressions in there before you do, we do the shell expansion. So here, I can echo the first file and call upper on it, right, and then echo that with an echo command at the shell. Yes, question in the back. Standard out.

Yeah, it's get output, commands.get output. The question was, sorry for the video, am I capturing standard out and standard error or just standard out, and the answer is standard out. Yes. Excuse me? There's no out.

This is standard out. This was, this was echo. Echo doesn't return a value. Echo prints the standard out.

So this is an important question. The question was, this is not out 37. And as you see, there is no red out 37. There's a distinction in Python between printing something and returning something. That distinction, this is a very important question, so that distinction is, if I type 1 plus 2, this returns the value 3.

If I type print 1 plus 2, this prints the value 3, but doesn't return anything. There is no out, right? And we make that distinction. Out is actually triggering on sys.displayhook.

So it's actually triggering on the internal behavior of the compiler that calls sys.displayhook, okay? So now, this is where it really gets dirty. So let's imagine that you want to do something a little bit more complicated like look at all the files that end with ipynb. I want to see which files in this directory are notebooks and which ones are something else.

So I am doing logic in Python and then I'm doing echo with Python expressions to create the numbering that I want. I have no idea how to do that in the shell, but I can, and obviously echo is a command, a print would do just as well, right? But the point is you can do any Unix command or any system command in this way.

So you can mix and match logic in Python, even complicated logic in Python with inter-sphere system commands. You obviously can do all this in Python itself. If I'm writing production code, I would do it with Python calls, but for quick and dirty work, this is very, very handy especially at the terminal. I can never remember how to do complicated logic in the shell.

So I just do it in this way, but I have access to the most common things, okay? So let's take a quick break because we're at a good point. We're going to start talking about magic functions, but I think the coffee break is on right now. I was told to take a break at 10.15. We're a couple of minutes late.

Let's be back in maybe 15 minutes. Is the mic, am I on, on the recording? Okay, good.

So you've seen me type a couple of times things that begin with percent, like percent quick ref. What's that business? So percent is another bit of special syntax that we have in IPython called magic functions.

So it's again what magic function, if you type, simply type percent magic, surprise, we give you information about the magic system. I'm not going to read it. It pops up on the page or you can read it at your own leisure. The idea behind percent is to provide a syntax for commands to control the environment and to do things that are orthogonal to the default language syntax so that we can do things that are more shell-like at the command line without interfering with variables and code that you may have.

So we created syntax which was deliberately invalid. In fact, the syntax used to be at instead of percent, and then Python 2.4 came out about 10 years ago, and we had to go through a process of switching, and then we made a decision to pick an operator that was in the language as a binary operator so that when it was at the beginning of a line, it would make no sense, and therefore we would be, we'd steer clear of the Python syntax without creating, and it would be future proof for a conflict because Python can't read, well, I guess they could make it a unary operator now, but hopefully they won't. And because it already had a meaning as a binary operator, there was a lot less chance of creating a conflict.

And so the idea for Magix is they're commands that don't take parentheses, you don't have to quote, you just type them kind of shell-style spaces and dashes, but they let you do things like control IPython itself and other things. So, for example, the timeit module is a very useful module in the Python standard library, but it's kind of funky to use, and using it interactively isn't very easy, so we have percent timeit that will call timeit and report for you and will do all of the necessary invocations under the hood so that timeit works and reports. Now, in addition to 1%, you can put 2%.

So the difference between 1% and 2% is 1% is called a line magic, it operates at the level of that one line of code. 2% is only valid at the very beginning of a cell, and it operates on the entire cell. And it simply says, this command applies to the cell, whereas this command only applies to that line, okay? So if I do double percent timeit, I will time the whole block of code under the control of the timeit module, okay? And again, you can mix and match, you can put percents inside of codes of blocks of code.

So just like we did logic with exclamation, you can do a loop and then inside the loop put percent timeit to time a given expression inside of a loop. And by the way, while this is running, look at the top level of the notebook here. This is your indicator that the kernel is busy, that the interpreter is running. When it's not running, that's an empty circle.

So we tried to make it very unobtrusive because if we make it like change colors or whatnot, every time you're running code, you'd have something flashing in the periphery of your visual field, and that drives me absolutely nuts. So it's very subtle, deliberately, but it's there. It's there if you need to know whether your kernel is busy or not. You can highlight that and it, if you hover over it, it tells you and it's just the changes from an empty to a full circle, okay?

So now, what can double percent magics do? You can do things like double percent bash, okay? So this is a shell. Double percent bash goes into the full. Double percent bash actually, I'm sorry, where did I go?

Double percent bash goes into bash and runs the whole block of code. And in double percent bash, we don't do any of the funky interpolation that we do with exclamation. The reason is that the idea for double percent bash is to copy bash scripts and you may be copying a shell script from somewhere that has, and dollar has a very special meaning, so we don't want to mess with it.

So the funny stuff that we do is just with exclamation. Double percent bash means give this thing to bash and run it unmodified. There's a useful magic which is called write file, which writes the contents of the cell to the file that you name. And it's always destructive, right? The idea is if you're logged into a remote notebook server and you don't want to SSH in to open a file with a text editor, you can fake that by saying, write file, put a file name, and type the code in there.

And whenever you run it, it'll write that output into the file system for as that file. And you can make a PY file, you can make whatever you want, okay? So here, there it is. And if I change the file, you can see right there that you're writing the file to disk and then you can read it back from disk, okay?

So there's lots of magics. You can type lsmagic and see the list of magics, okay? You can see what magics are available. These are the line magics that exist. These are the cell magics.

As always, you can find out with... question mark, what a given magic does. So the question mark is consistent and it operates also on magics. It recognizes magics and it'll tell you, magics are just Python functions. It'll tell you what any given magic is, okay?

So when you run Python code, you can actually, so this is also be, again, anything that's valid Python, I'm not gonna explain because it already works. This is beyond Python code, you can type code with Python prompts and we will actually parse that out for you and run it correctly. So that if you're pasting stuff from tutorials or mailing list discussions or whatever, that people copied from the Python prompt and you wanna work with it, you don't have to go and manually highlight the first four characters and delete them every, you can just copy and paste it and we'll run it correctly for you, okay?

And the same thing if the prompts are IPython prompts from the command line, we will also strip that out. So we try to make it really easy to run code that comes from anywhere, okay? Now code produces errors.

So let me here write a little file mod.py, right? Let me import it and this file gives me an error. It's a zero division error. It's a very simple two function calls that have, that produce an error.

So this is an exception. This is what a traceback looks like in IPython. A traceback in IPython is actually a little bit fancier than a traceback in Python. We show more of the stack, we show each frame of the stack with context information. We syntax highlight the code.

We show which line is the offending line and we give you a little bit more information in the, at the top level about the traceback. Now you can control the amount of detail with a magic. So the magic X mode lets you change that.

So if you change the exception mode to plain, then plain looks a lot like a Python traceback. This is about as close to a Python traceback as it is. We just color it, but it looks very similar so that you can paste it into things like doc tests or if you just want it to feel like a Python, a standard Python traceback, you can say X mode plain. And we also have what's called a verbose exception mode. The verbose mode actually analyzes the stack and gives you values of functions at any, both at the offending lines.

It gives you all the values of the locals and at the call frames, at the entry points of each frame in the stack, we actually expand that out. This verbose mode is not the default because it can get huge, right? If you have very large variables in there, it can get absolutely huge so we don't make it the default. The default is the intermediate one. It's not plain, it's not verbose, it's the middle one.

But you can toggle either more or less by changing and you can always configure these things to be persistent, okay? So we really try to make it, so the default is what we call context, which gives you context information but it's not super verbose, okay? So the double percent lets you call not just Bash but actually other languages.

So yeah, we're Python people, we know we're better but still it's nice every now and then people want to run Perl code, there you go. You can run Perl code, okay? You can run Ruby code.

So I want you guys to take a second to write, to do a little exercise which is write a cell that executes in Bash and prints your current working directory and the date. Just take two seconds to do that and run it. Make a cell that in Bash, and if you guys are on Windows, unfortunately I didn't have time to boot a VM to test how to do this on command.exe. I don't know how that would work.

So if you're on Windows, check your email for one minute. I'm sorry. And there may be a way to do this on Windows, I just don't know. Question? Yeah?

Is there a documentation on how to extend the magic to write your own magic system? How about you wait five minutes? All right. Yes, question? No, this is assuming there's a Ruby interpreter installed.

Oh, if you don't have one, then that won't work for you. What's that? Mac OS 10 chips with Ruby. Yes, question? Yes?

Well, what it does is it configures matplotlib to behave in a certain way. So it's not so much that it affects the notebook, it affects the state of the matplotlib library. It initializes a matplotlib backend, and it registers a callback to send plot information back.

So it really has a stateful effect on the kernel, more so than the notebook. Yes? I'm sorry, the question was, does things like the %matplotlib inline, which is a line magic, why does it seem to have a global effect on the whole notebook? It's not that there's anything special about the document. It's that it's a command that modifies the state of the kernel, really.

Okay, has anyone finished the little two-liner in Bash? Okay, a few of you have, since we're running tight on time and we have a lot to cover. I am going to show you how to do it by running this command, %load. %load is a useful magic that loads a path on the file system into the next file, okay?

So it's very handy, and this is what, so what I did was I read that script, which is in the solutions directory, and loaded it into the next cell, and that's the solution. Now, %load is a very useful magic in that it lets you load not only local scripts, but also remote files. So if you ever find a URL with a file name that you're interested in playing with, yes, you can copy and paste, and you can highlight and whatnot, or you can say %load and the URL, and it'll fetch it for you and put it right there, okay?

So let me illustrate that very quickly. Let's go to the Matplotlib gallery. Yes, question. Yes, when we show, so the question was, can you use it as a scraper and parse whatever you fetch? Load by itself doesn't do any parsing, but I'll show you, we're gonna see how to write your own magic that does whatever you want.

So in this case, let's imagine that I wanted simply this script. Yes, I could copy and paste all this, but here's the source code. I can just copy this URL. Where was I? And I can say, load that, and there it is, and when I run it, there it is.

So it's a very handy way of grabbing stuff that could be anywhere online and using it right away, and start learning, start playing, if I now wanna play with Matplotlib and see how to change that. So let me show you how to do that. So let's say I want to load this URL, if I now wanna play with Matplotlib and see how to change that.

So let me close this down here and get back to full screen. So what about debugging? We saw exception reporting. We saw, oh, I can load a remote script and run it. Well, what if it produces an error?

So let's go back to our little division by zero. What if I wanna debug this? Well, Python has actually a pretty nice debugger. I like the Python debugger, PDB. I think it's pretty good, and I actually use it a lot, especially because it can do a very interesting thing, which is to do post-mortem debugging.

You get an exception trace back, and you can go and inspect the stack live. It's one of the most useful ways of debugging code. In 12 years of using Python extensively, I've used a graphical debugger once in my life, in 12 years, in 14 years of using Python. Everything else, I've been able to get by with PDB and the IPython enhancements, because digging into the live stack is so useful that I can typically figure out what's going on, and in the notebook, you can do that. You can do, you can, after there's been an exception, if you type %debug, you will be dropped into PDB, and you can start doing things like, oh, show me the stack.

Okay, this is where I am. Show me x. X is one. Go up one frame in the stack. Show me y.

Okay. Go back down one frame in the stack. This is PDB embedded into the notebook, and what's happening is this little box right here is forwarding standard input all the way from the PDB prompt and the kernel over web, over ZRMQ, over web sockets into the JavaScript and sending it back.

So yes, it's a little bit of a complicated dance, but the point is, as far as you're concerned, it works. You get a command line interactive debugger. You get the power of PDB with the IPython enhancements in terms of color highlighting and whatnot in your web browser, so that you can interactively debug and use all of the control of PDB from the web browser.

Okay, and when you quit, I'm not gonna teach you how to use PDB, that's kind of outside of the scope, but that's just standard Python PDB. You type question mark, it'll tell you all of the commands that it has. Yes, question in the front. Yes. Yes.

Yes, it's the last exception. Whenever an exception is produced, Python saves the traceback and the stack. There's a sys.lastException, I've forgotten. We wrote this code 10 years ago.

But Python itself stores the state of the stack in the last exception, and so you can type percent debug. It doesn't have to be immediately. You can type it later, as long as no, it only works on the last traceback.

Okay? Now, this is because raw input works. So if I type raw input, I get a text block, and no, it's terrible. And when raw input comes back, it gets the value.

So notice that whenever you call raw input, notice what's happening up here. The kernel is blocking, right? The kernel is blocking because it's waiting for your input, right?

So you have to type, you have to get out of there in order for the kernel to unblock, because the kernel is waiting for your input. So for plotting, if you don't have matplotlib installed, as I said, it's not a big deal. You can just watch me do this for a second. Not everyone needs plotting, but at least, because it is very common to need to visualize data, I wanted to show you guys the very basics of how it works.

If you type percent matplotlib inline, you configure matplotlib so that it knows, instead of trying to pop up Windows, it knows to send all of its figure output over the notebook into the document. So once you've done that, you can do your normal imports any way you want. Matplotlib inline doesn't import anything. It doesn't, I mean, it does imports, but it doesn't populate your namespace. It doesn't change.

You still have to be explicit about your imports. It only configures things under the hood. And then you type a little bit of code, and there you go. Matplotlib figures come up here. You can configure it to produce SVG instead of PNG by default.

The default is PNG. I don't want to go into the reasons why. I can tell you offline why, but the default is PNG for good reasons.

But you can configure it to send SVG by default if you prefer. And notice here that I grabbed the figure object. I'll come back to that.

So as I said, we're not going to do a full tutorial. This is just to show you that you can visualize data inline. And the only thing other than normal Python code is to put matplotlib inline once to configure matplotlib to send its plots inline.

So how is all of this working? We have the web browser here, and somewhere there's a Python process executing. How are these things talking? There's JSON data that is being exchanged back and forth. And IPython will print you, will tell you, what the connection data for the current session is.

If you type %connectinfo, it will give you that information. And it prints it to the standard output. This data can be useful to have this JSON data. And it also tells you how to start an IPython client that connects to that kernel. Because what's happening is we have the Python browser here, and the Python kernel is executing.

And these two things are talking, but the kernel isn't exclusive to this client. You can connect to that same kernel via another mechanism and use it simultaneously. That connection data is encoded in this path right here.

So you can connect another IPython application to the same kernel. So for example, if I type qt console, we actually open a qt console, which is this GUI terminal that is connected. Look, I was at prompt 84.

Now I'm at prompt 85. It's a new graphical console that is connected to the exact same prompt. And if we look at that figure that I saw earlier, it's right here.

This is the figure that I had created earlier. I can view that figure right here. This is another client that is connected to the same process because we have a full protocol. Yes, question? The state of the kernel is the same, but only the client that requests an output gets it.

And part of the reason why that's the case is because I can actually open a terminal console connected to the same thing. For reasons that don't matter, the very first time it has to guess the prompt, so this one didn't know that it was at prompt 85. What happens if I try to view the figure at the terminal? Well, at the terminal, a figure can't be displayed as a plot because a terminal, a command line terminal, doesn't know what to do with a PNG image.

So it shows you the basic text representation of the object. So now we have a text terminal, a graphical qt terminal, and the web notebook, all three speaking to the same kernel process simultaneously. So that shows us that we really have a client server protocol for executing arbitrary code. And that protocol is implemented by these three separate clients.

So the question is, is the kernel single-threaded? Yes, the kernel is single-threaded, and code executes on the main thread. So you can obviously run your own import threading and run your own threaded code yourself, but we don't try to add any threading at all to the kernel precisely to keep things simple and to give you full control over threading behavior if you want, which is why the kernel blocks on all code execution. Question back.

So the question is, is there a way to share the notebook live? And the answer is yes, with some limitations. You can run a notebook on a public IP with SSL, update your certificates, but with SSL and password protection. And if you give someone else a password and it's listening on a public IP address, you can connect simultaneously more than one person.

Now, what you don't get is you don't get real-time synchronization of the window view. It's not real-time Google Docs. There's a startup at the University of Washington called Cloud.SageMath that offers that. It's a service that hosts notebooks and offers real-time synchronization. They've added a layer with node.js on top to synchronize the state of the notebooks.

We've talked with them. We're good friends with William Stein, the author of it, and we will eventually add some of that machinery back. But for us, the node.js hack that they're using doesn't quite work for us.

So it'll take a while. So for now, if you want to do that, the solution is basically to one person executes something, saves, the other person has to hit reload. So it's a little clunky, but it can be done if need be. Yes, question? Excuse me?

All the cells in Python code, what's the scope of each of the cells? Is there one big file that you can access? So there is no file scope. You're operating on a live Python interpreter.

So the scope is the namespace of that interpreter. All of these cells are updating a namespace. It's a Python dictionary that we're basically under the hood. All Python, at the end of the day, all we're doing is doing exec on that block of code in a dict. IPython is 100,000 lines of code wrapped around exec code in dict.

That's it. Does that answer your question? All right, so let's go to the next notebook.

So this one is going to be very quick. This one is basically a mini tutorial about markdown. And I'm really going to skip rather rapidly on it because it's markdown syntax.

If you know it already, you already know it. And if you don't, learning markdown syntax is best done as an exercise on your own. All I want to show is that you can do arbitrary markdown. You edit a cell by going into edit mode, and you Shift-Enter to render it. Markdown lets you do italics, bold, lists, numbered lists, et cetera.

And as I said before, you can do headings with markdown style. With pounds, you can do headings. But we recommend, as I said earlier, that you don't do that, that instead you use our syntax because that gives you structural control over the markdown. You can do embedded code.

One thing we do in addition to markdown is mathematics. So this one I want to stop in for a second because this is different from default markdown. We actually let you put single dollar signs to embed LATIC mathematics. And we will render it with MathJax, or double dollar signs, to do displayed equations. The difference is that in LATIC, what are called inline equations are rendered inline, and displayed equations are rendered by themselves in a separate line, and they're centered.

So if you're not into math, this is not a big deal. But for anyone doing very technical content, education, science, et cetera, this is actually kind of a big deal. OK? And we also support GitHub flavor markdown, which means you can put triple back quotes and the name of the syntax that you want of the language, and then we'll render it correctly for you. OK?

Now the other thing that's important to know is that we render local files for you. So in this case, the notebook directory has a subdirectory called figs, and that subdirectory has an SVG file with a Python logo and a little MP4 animation. And so with HTML5 video, you can say, I want that source file as a video, and I want an image with that. And we render the image, and we also render embedded video. Right?

So if you have notebooks that have local content, you can display, whether it's an image, pretty much any HTML. Markdown is a subset of HTML. You can always escape out to arbitrary HTML with arbitrary tags.

So this lets you create documents that have embedded images, embedded code, embedded video, embedded audio. If it's valid HTML and your browser can do it, you can do it. OK?

So security-wise, let's skip this short exercise. I'm a little worried about time, and I know there's some other stuff that's coming up later where I do want to give you time for exercises. So the important point about security is that.

But the notebook is a web server, so it will travel down your file system, but not back up. So where does security matter? If you're running a notebook, not on your laptop, but you're in a shared server, you want to worry about where you run it, right? And you may want to password protect it, even if it's a shared server that's not listening on the public internet, but if there's other users, because it's serving your content over the, it's serving your content on that port and it's accessing files below it.

So it can be hijacked to read your file system, basically, and to execute code for you. If you run a public server, I recommend that you don't run it at the very base of your home directory, even though we do things like, we don't serve .ssh, and we do a few sanity checks, but it's still a good idea not to run, I mean, obviously, if you're going to run a public server, you encrypt it, you password protect it, but I still wouldn't run a persistent public server on my generic home directory, I just don't think it's a good idea. We don't, but like a web server, we don't travel up. We travel down, we don't travel up, right?

So we don't work our way back up the file system. If anyone is really interested in security about IPython, you can think of IPython as weaponized, weapons-grade JavaScript. We have JavaScript code that is connected all the way back to a remote execution engine, so we really are, we really are kind of a weapon waiting to go off. And if anyone cares about web security and is interested, we have a private security mailing list, talk to us, we're happy to discuss this. And we're not security experts, but we're learning, and we have people who care about security who are engaging us.

So we welcome anyone who's a security expert and who's interested in this in talking to us. And there are people in industry who are interested in using this in secure environments, and we're not claiming to be, to know all. We do know that there's problems, we've tried to make improvements to security, but we're happy to talk to any of you if you're interested. And we have private repositories for fixing security problems and working on them before we release them in a responsible manner, so, okay?

So let's go, let's close this one, and let's continue with some other things that IPython goes beyond, where IPython goes beyond plain Python that are very valuable and powerful. Earlier we saw things that operated at the kernel level on all clients, things like the question mark and the percent and the exclamation, all of that is the core of IPython execution. That stuff's been there for about 10 years, okay? This stuff is much newer, and even though technically it happens at the kernel, it really makes sense 95% of the time in the notebook, because it's really about creating rich representations of objects and displaying objects, taking full advantage of what a web browser can do.

And so, for example, when you saw that figure displayed as a PNG in the Qt console and the notebook and as a text file, and just with a standard Python representation in the terminal, that was taking advantage of the fact that we actually provide for objects multiple representations, and we try to have a client give you the richest and the most powerful ones. So objects in Python, you can define what's called the wrapper of an object, the double under wrapper or dunder, that's a special method that lets any Python object define how it wants to be rendered as a string, well, as a representation, because you also have dunder SDR. And what we've done is we've created under wrapper HTML under, under wrapper JSON under, under wrapper PNG under, a complete collection, and objects can render themselves in multiple ways. And when an object is rendered, we actually collect those representations into a MIME-type key dictionary and send that back, so clients actually have access to all the representations and they can show you the best one they can. And that data is encoded and stored in the notebook and saved, which means if an object, for example, if a figure has both a PNG and SVG representation, we may render the PNG in the notebook, but we may take the SVG and render that one to export to PDF, for example, because that dictionary of outputs is stored in, in the notebook.

So for this reason, we've created something called display, which is the equivalent of print, but for this rich representation. So if you want to call, if you call print on something in Python, what you do, what Python does is it computes the string representation of the object and prints that. It calls dunder SDR dunder.

If you call display on that object, IPython calls all of these special methods, collects them into a MIME-type dict, and sends it back to the client, and the client will look at them and say, what can I do? The terminal typically says, I can only show text, and it'll grab the text field and show that. But the notebook saves all of them and shows the richest one it can and has a priority order, okay?

Now you can also display specifically one of them if you want. So you can say display JPEG or display one of them. So let's have a quick look at what this, how this behaves. And here, I've loaded, I also called, so IPython.display is one of the modules that has all of the machinery for rich displays, and it has things like an image object, which knows how to display images.

So an image object, I create an image object from a file, call it I. This is an object which when I compute it, its representation is the PNG, is the actual rendering of the image, because it has an image representation. I can also call display on it, and it will be, notice the difference between calling, returning it and calling display, just like earlier, the difference between print.

So think of display as print, basically rich print, right? When I return it, I get an output value. When I display it, there's no output, it just gets sent as a side effect, right? It's the equivalent of a rich print statement, okay? You can call an image from a remote URL as well, and so the image object can be called.

Now, when it's called in this way, the image is not embedded. It's actually, what we do is we, the HTML that's returned has the remote image URI, and it gets fetched by the browser. You could, we can embed the data if you want.

If you say embed equals true, then we actually save the embedded output image in the notebook, which means this would, if I had loaded this notebook without a network connection, this one would not have worked because it was really fetching it live, whereas this one would load because it would have been embedded as a data URI in the local notebook, okay? We have an SVG object. Let's see. How are we doing on time? I want to give you guys a minute, at least, find an image online, try to do a quick exercise for a couple of minutes of any image, a logo, whatever, Google image, and try to do both embedding it and displaying it locally by file name.

Matias, question? Erlang. Wow.

Okay. Okay. Okay.

Okay. Okay. Okay.

Okay. Very cool. Okay.

Okay. Has anyone got the image to work? Okay.

So several of you are raising your hands. I'm going to move forward because we are a little pressed for time. So videos, in addition to embedded videos, well, there's this thing called YouTube out there. You may have heard of it.

And so we actually provide a default YouTube video object. You can pass it, you simply pass it the hash of the video and you can render and we will embed it and it will actually play. So this is a video from a hackathon at the White House that they had last year. We're about a minute into it. They were demoing, somebody was demoing, a journalist was demoing the IPython notebook and doing some graph analysis at the White House hackathon with IPython.

So we thought it was cool. She's actually here at PyCon. I think she's arriving later today.

So I'm going to meet her later. But we thought it was pretty cool. But this lets you embed arbitrary YouTube videos and you can actually provide width, height, and other, and arbitrary keyword arguments that go to the request.

So if you want to provide things like a start time, a time offset into the video, since the YouTube API supports a start time, I can't remember what the name is, you can pass that to it. How did I get that to pop up, that little pop-up window? Well, whenever you open a function call, if you want to see the signature right there, you can hit shift tab. It's not tab because we had too many events conflicting on tab completion, so we separated.

So tab is tab completion. And for querying and function calls, it's shift tab. It pops up a little pop-up window. You can expand it to see more information.

So here we show how to do, for example, if you want to control the start time here, it's start. And if you click, and you can collapse it back or send it to the pager if you really want to keep it out for reference. And by the way, the pager can always be sent to another tab.

So if you click on this, you can open the pager in a separate tab if you want to keep it for reference. Okay. So if you want to keep a few pages open, this works much better obviously on like a large monitor. You can keep reference tabs open and keep working on your main one.

Okay. So we do have an HTML object. So if you have a piece of source code of source HTML, you can display it. It's called HTML, oddly enough. Though we do provide a double percent HTML cell type.

So if you just want a block of HTML to be rendered as output, we do that. So obviously, if you type HTML in a markdown cell, that will be rendered in place. But if for some reason you want to highlight, say you're taking an HTML tutorial, so you really want to show this is the input and this is the output, well, this is one way to do it.

So if you're teaching HTML, you can do this. If you're teaching JavaScript, you can do it. So here's an example copied from, so there's a JavaScript object and it will return JavaScript. And here's an example copied verbatim and we also have a double percent JavaScript that will return its output as JavaScript.

So this is an example copied verbatim from the D3 gallery. So we just fetch, we fetch with the JavaScript command. We fetch the actual D3, the D3 URL from the CDN for where D3 hosts its content. We provide a little bit of CSS styling and then a block of JavaScript that actually returns as its output a D3 example.

So this protocol lets you, you can define for your own objects all of these representations. And we have in our documentation, we have an extensive tutorial on how to write custom display methods. The way, for example, many of the libraries in Python like Pandas can display themselves in a nice way is by providing these special display methods for their own objects.

So for example, if I load, so this is a simple CSV file, right, that I'm going to save as data.csv. It's basically stock prices. If I load that into Pandas, if I load that file into a data frame, when I display the data frame, Pandas provides HTML wrappers for its objects.

So when I display that, instead of seeing a bunch of text, I see a nicely formatted HTML table from that CSV file. So here, all I did was load, load that data CSV file into a data frame object and it will be nicely displayed. Similarly, for example, the SymPy library, which is to do algebra, symbolic computing and sort of high school style symbolic algebra, lets you compute and tell it to return logic representations. And because we know how to render math, not only if you type it in between dollar signs like I showed you earlier, but if you return object, then you can actually see your expressions formatted in proper mathematical notation as output. Yes, question in the back.

So, yes, you can have interactive representations. What happens though is we actually, when we load a new notebook that we haven't, that you haven't seen before and that was not created by you, for security reasons, it won't render the interactive content. You'll have to re-execute it for that.

What we do, and this is going back to the security issues, we actually generate a private key for you and we sign your own notebooks with your own key so that you know what content you created. And if it's content that doesn't seem to come from you on first render, we don't render the JavaScript because the reason is that that JavaScript could, in principle, use the notebook API to call back into the kernel and execute code. So we'd be in a situation very much like the famous Microsoft word viruses where when you open a document, that document on opening it would execute code arbitrarily. And we want people to understand that running code in a notebook is running code.

So at that point, I mean, you have to trust what code you're executing. But it really felt like it was too much for people to say that when they're simply viewing something that looks like a document, that that could execute arbitrary code. So for that reason, we don't execute dynamic content on load.

But it's there and you can execute it if you rerun the cells, okay? We also have an iframe object. Oh, I'm sorry. I keep forgetting. The question was whether HTML output for the recording, whether HTML output could also return dynamic JavaScript.

And that was my answer. So there's an iframe object as well. The PyCon website is a little bit slow.

Let me make it a little narrower here maybe for this screen. So this is the, oh, I'm fairly zoomed out. So this is the PyCon website loaded in an iframe.

So you can return arbitrary URLs and embed them into the notebook. And let's see. Let's maybe skip this exercise for the, because I really want to give you guys time to cover, to do exercises on the next section. And finally, there's examples on how to render math.

This is what the SymPy code uses under the hood. This is mostly of interest for people who do very mathematical work, but the point is you can return LATIC objects. And we actually provide a raw LATIC one for basically complex LATIC constructs and a simple math one that assumes it's a single equation. And basically, we do the dollar signs for you.

But back to the beginning to summarize, these are all of the representations that you can provide. And so the methods are called repper underscore that, JSON, LATIC, HTML, SVG, et cetera. And your object can provide whichever ones of these methods you want. Pandas is a library that makes very good use of this, but people are bundling this into many systems. In our documentation, there's examples on how to add this because sometimes you may want to add fancy representations to objects from libraries you don't control and where you can't add the methods.

There's a second mechanism. You can add a special method if you're writing the code yourself or you can actually register special renders so that when an object of a certain type comes back, we call back a special render on it. So if you want to add fancy representations to objects that are coming from a library that you don't want to modify or you can't modify, you can register your own renders so that when those objects come back, you get a pretty representation even if the library doesn't provide it. Somebody was going to try to ask a question in the front. Was it you?

Yes. So, yes, the PNG representations can return. If you have the data in memory, you can send it, and that's how the Matplotlib rendering works that way.

So I can show you in detail in the code how it's done. In Matplotlib, which gives us access to getting the rendering data in memory, we never write anything to disk. The way those images are coming back is purely done in memory. When we do the plotting in Matplotlib, we create the PNG data, we base64 encode it, and we put it in the data field of the dict and send it over.

So it has to be base64 encoded because it has to come back as JSON, but it doesn't have to be written to disk. For the PNG field, for the SVG field, we only have those representation types. We could define others. Those are the ones that we have to consider. Sorry.

The question was whether there's ways of sending this data purely in memory, and so I was trying to answer that. Does that answer the question? So what specifically? I mean, PIL, what? No.

Yeah. I mean, it has to be in a browser. It wouldn't know what PIL is. It has to be in a browser. It wouldn't know what SVG is.

It has to be in a browser. No. Yeah. I mean, it has to be in a browser. A browser wouldn't know what to do.

A raw array of pixels, a browser wouldn't know what to do with it. So you sort of have to encode. You can keep that in the kernel, but when you're going to send it for representation, it has to be in a format that a browser has some idea of what to do with.

So a raw block of pixels doesn't really mean anything to a browser unless it's encoded in a specific image format. Okay? So now let's go to the next block. We still have 40 minutes, which is...

This is something new. So if anyone ended up not upgrading to IPython 2.0, you're going to have to watch for the next 15 minutes because this only runs on 2.0. So this was the reason why. Everything else that we've done up until now was okay on 1.x, but this only runs on 2.0.

Okay? So... I'm sorry? 12.20. Oh, okay, good. I thought it was until 12.

Oh, good, good. I misjudged. read the schedule? Okay, good. I still have to give you guys 10 minutes for the survey, so I have until, I guess, 12.10, but that's good because it means I don't have to rush over the stuff in the end. And I also want to leave a little bit of a slush at the end for open questions because there's a lot more material in here.

So let me first give you an example and then we'll do an exercise. So we're going to take this one from the kind of demo inwards. So what we've done in IPython 2.0 is provide APIs that let you, up until now, we've been using rich features of browsers to display output, right?

But it's been a one-way thing. We've been saying, here's stuff that happens in my Python process. Let me send it over and make it look nice on the notebook.

Let me show an image, a video, whatever. How about if I want to use the browser itself to control what's happening in the kernel, right? So in IPython 2.0, we defined an API to do precisely that, to connect interactive controls in the browser with execution in the kernel, right, and to let you actually wire the two together.

So you guys should be able to run this and follow along with me on your system as long as you have NumPy and matplotlib. If you have NumPy but not matplotlib, you can replace the plot in show command with a print and you'll just print an array. It won't look as pretty, but for the sake of the exercise, it'll work fine. I tested it and it does the job for what I mostly intend to show. It won't look as pretty, but it'll do the job, okay?

So I'm plotting, I'm loading an array of numbers. This is a raw array of numbers of the kind you were asking about, a NumPy array, but I'm interpreting it as an image. So it's an N by P by three channel red, green, blue array, okay? It's an image that comes and that is ships in the scikit-image library as one of the default test images. It's a coffee cup, but I saved it as a pure NumPy array so we wouldn't depend on scikit-image or even on a PNG reader.

Let's imagine that I wanted to do a little exercise and this was a tutorial and I was teaching about images. So I wanted to show how to change the red, green, and blue channels of an image, right? So, and I wanted to show you guys how to change the color levels of an image independently and what happens there.

So I write my little edit image function. It takes an image and it has a multiplying factor for red, green, and blue and it makes a copy of the input image so it doesn't damage the input array and it multiplies the red, green, and blue channels by R, G, and B, right? Simple enough. You can, and you can multiply by less than one or by more than one if you want to basically.

This is the kind of stuff that you do in an editor in Photoshop with the channel sliders, right? And you plot it and you also return the, you return the output as a new image. So if I write that and I want to show you guys, well, what happens if I amplify the red channel over one, I start saturating on red. If I set it at zero, I remove all the red, right?

So, yes, I could play a lot with this re-executing the cell over and over with parameters and illustrate my point. But wouldn't it be nice if I had sliders for red, green, and blue and can show you that? The problem with that is that I'm a command line guy. I don't like to write GUI code and I don't know how to write GUI code and I'm old enough that I'm going to die without writing GUI code.

So, but every now and then, I would like to have a little bit of a GUI for this kind of work and so we figured out how to do that. So, if you import from my Python HTML widgets, the interact function and the fixed function and you say, I want to interact with my image editor, with my image as a fixed parameter, this image I of my coffee cup as a fixed parameter, but I want R, G, and B to vary between zero and three, right? That much I can write. I don't know how to write GUI code, but that I can say. And if I do this, this is what happens.

I get three sliders that now control my red, green, and blue channels and let me slide them. And what's happening here is, as I slide my interactive controls, every time an event fires in the browser, we're sending back to Python code to say, call that function again with these values of, with the current values of the parameters, execute the code again, and send it back to me. So, every time you move those sliders, the code is going to Python, the kernel is executing, and it's sending you the output back.

So, you can basically create self-contained little graphical interfaces, simple ones. You're not going to write Adobe Photoshop or Microsoft Word with this, right? It's for simple stuff, but for simple parameter exploration with one line of code that even I can write, you can get interactive control and parameter exploration for your code. And we think this is very, very useful.

Any questions? Yes. So, does interact return the values that we selected?

So, let me do here. I assigned, I hadn't assigned it to anything. Let me, I assigned it to the variable called ii.

So, this is a function. Interact returns a function. No. This one, where are those values? Matias, weren't they in widget?

I thought they were in widget.values. Widget.keys has some other widget keys. Okay.

Let me look at that and get back to you because I, they're in there somewhere, but I forgot exactly where they are. Sorry. So, how does interact know what kinds of sliders, what kind of widgets to create and how did it know that we should put sliders in there?

What we do is we try to do effectively type introspection based on the values and guess what would be the most sensible widget to give you for the given kind of parameter that you're providing. And this plays very nicely with Python's dynamic typing behavior where if you have, imagine a function that works on pretty much any input, a function that simply prints, right? Print x, a function that just prints its output, and we call interact with x equals true. Well, that's a Boolean, so the widget that makes sense for a Boolean is a checkbox, right? Because that's kind of the only sensible thing to do with a Boolean in terms of graphic or GUI representation is a checkbox.

If you pass a slider, if you pass a range from zero to ten in steps of two, which is the range syntax, well, the thing that makes sense is to create a slider that goes from zero to ten in steps of two, right? So that's exactly what we do, an integer slider that goes zero, two, four, six, eight, ten. The only difference is that in this case, we actually include the endpoint.

So we're not honoring exactly the range syntax. Yes, question in the back. Yes.

So I'm only showing you guys the high level API. So the question was, is there a way to override this? So the answer is yes. The low level API that I'll open a link to the documentation and show you in a minute, gives you control over how to create your own widgets. And all of these are, we're really under the hood doing type checking and creating instances of a bunch of widgets that are fully typed.

So you can say, I need a float slider, I want a menu, I want, and we have a fairly large collection of widget types. So interact is the highest level, most concise entry point for quick and dirty stuff. The underlying widget API is more of a standard GUI sounding library API that gives you all of the standard widget types. Does that answer your question?

Okay. So if you give it a string, you get a text box. And as you see, it updates as I type because every time an event fires, we send it.

So we keep calling the function. Now, we do throttle that queue because obviously, imagine you're moving a slider quickly and it's a complicated computation that takes 30 seconds and it's a floating point slider. So as you drag it, it fires 150 events. You don't want to now have to wait for two hours for the thing to finish rendering.

So what we do is we keep that queue very shallow. And so we only, I think we keep it at depth three. So we only, we start dropping events and we queue up only the last three events.

So that if you do that, then you'll see the beginning of the behavior because the first event goes out. Then as you drag it, most of them get dropped and the last two are going to be queued up. And then you'll see the beginning and the end of your action, but most of the intermediate events will get dropped. It's a solution basically for, because this could be running also on a high latency link. You could be running on your browser and the server could be running remotely on a high latency link.

You don't want this dragging to basically, to pay the price of communication overhead for no good reason. If you pass it a dict, well, a dict is a key value pair. So here you can, you see we generate a menu. And in this case, look, the keys of the dict are strings.

So they can be shown in the menu. The values are only going to exist kernel side. So it doesn't matter that these values aren't representable in JavaScript, right? We have to send JSON over.

But as long as we, as the kernel can send some string representation, your values can be anything that exists kernel side. So we give you a complete coupling between the JavaScript that can exist in the browser and the code that executes in your kernel, okay? Any questions on that?

Now there's also a decorator form of this called interactive. And the interactive decorator is basically a way of getting really, really quick and dirty. I have this block of code and I want to just make it interactive for a second.

So what you get is an object which when you display it, behaves interactively like that. So interact operates on an existing function. You call interact and you pass it parameters and you get the interactive behavior. The interactive decorator decorates a function and turns it automatically into a function that has, that when you call it, behaves as a widget. And I can't find, I'll need to look at where those values are because I know they're there, I just can't remember exactly where in the API they are.

What's that? No, I don't have a widget. We'll look at that in a second.

So I want you guys to do, practice a little bit this and write a function, use interact to write a function that takes a string as its input and reverses it and sorts its input and prints its input sorted and optionally reverses it. So either does a forward sort or reverse sort as you work with it. So this will force you guys to actually, I mean, so the underlying function call in the standard library that you want to use is sorted.

So sorted will give you, will give you a sorted list and you can use question mark to query how exactly to pass the reverse key, but it's a one liner. And in the meantime, I'm going to cheat and try to answer this question that you were asking because I know that's not what I was looking for. Ah, okay. Thank you. That's what I was looking for.

So back to your question about where that value was stored, Matias helped me find it. So the function object has its widget. So the widget is this thing.

So whenever we return from interact to function object, the widget object is the widget that does the interactivity and that widget has a children and the first children, the first, so these are the children, the three float sliders in this case. And so if I want the value of the first one, it's that. The value of the second one, it's that.

So the widget.children is a list of your widgets and for each of them, .value is the value. And this is where I got confused. Widget, we have widget and widgets and I got, I tripped on that.

So widgets, widget, no, it's widget. You can tell that this is still new API. That is not fully in my brain yet.

But widget has your children and for each one of them, .value is the value attribute. So you can always get to it programmatically. Okay.

So, did anyone write something roughly like this? So you sort the string, you pass the reverse argument and then as you type, you see it update and then if you reverse, this is the action. I'm going to scroll up a little bit for the people in the back. I see them straining their necks.

So, I've said I want an interactive function. I call it sorter. It takes a string as an input and reverse is an optional flag and then all it does is it prints the sorted string with the optional reverse flag and I print it as a string.

So I remember sorted returns a list and so I called join on it to make it back a string. And the only reason why I'm calling strip is because otherwise any whitespace in between words goes in the front. If you don't do this, then whitespace will pull up in the front and as you put whitespace, it goes in the front.

But very, very simple. But it shows you how if you're teaching, for example, how an API works to someone, this is a very nice way to illustrate what the sorted API looks like because we kind of, we can see here the various aspects of what it does, how it behaves, how strings and lists behave, all of that condensed into a one liner that anyone can remember. Yes, question? Well, if I'm using the quick and dirty interactive decorator, they do because we need to guess these things.

But if I had a function that didn't have default values, okay, then this would be just a normal function. I can say, ah, I have an existing function from another library, for example, that wasn't created, but I want to interact with it. I want to interact with sorter. Here, because we have to create the widgets, you have to give us some information.

But I can say, I want the default string to be empty. Oops. And I want reverse to be true by default, and there you go. You have default is, it's true by default and there's no string at the beginning, but as you type, it's there.

So this lets me work on an existing function. I mean, in this case, I just wrote it, but it could be taken from a library. And you want to take a function from a library and play with it interactively, that lets you do it.

So it doesn't have to be written. It's only in the case where you're going to use the really quick, I mean, basically, the interactive decorator is there just so that you can grab a block of code and make it interactive right away because Python doesn't have blocks. If this was done in Ruby, people can implement this and they will probably implement it with a block syntax where they simply take a block and pass arguments to the block because in Ruby, blocks are first class objects. In Python, they're not. We have lambdas and functions, right?

So we have to do it via the function API rather than the block because Python doesn't have the concept of first code. Code, standalone code is not a first class object in Python. So we have to encode it into a function. I'm sure the Ruby, and I mentioned Ruby because it's a good example of another language whose syntactic behavior regarding this kind of problem is different. The API for JavaScript communication and all that is completely language independent.

So a Ruby kernel can implement all of this stuff, but their syntactic representation of it can be different. And they can still reuse our JavaScript widgets and everything and they can save Ruby notebooks with widgets, but you will express that in the syntax of their language and it will probably look a little different. Does that make sense?

Any other questions? Okay. So did that exercise work for people?

Okay. So there is a link here to our example collection and our example collection contains lots of in-depth details about how to use the widget system, okay? Lots of them.

And so you can see a lot more. So I want you guys to click on that link because I want to take a minute to show you what this is. It's a good time. I'm not going to go in detail on all of these. I mean the whole point of just getting you started is so that you can then continue learning on your own.

But now is a good time now that you've been seeing these notebooks to click on the home icon and see what am I pointing at. Well, this is a website called nbviewer.ipython.org. Let me show the URL. It's called nbviewer.ipython.org. This was Matias' weekend hack that has grown legs of its own and it's graciously hosted by the kind folks at Rackspace.

And what nbviewer provides is a service to share notebooks. So you write a notebook and you want to show it to your colleague who doesn't have IPython installed and you don't want your colleague to have to install IPython because they may say, that's annoying and I don't like it and I don't want to deal with it, but I just want to see what you did. So as long as you're willing to put that notebook somewhere on the public internet, somewhere, anywhere, it could be a temporary URL hidden on your website, as long as it's findable on the public internet, you can give your colleague the URL and that URL, so I clicked on that.

Let me, it's annoying that I can't show paths. So what you get when you click, when you paste the URL to an existing notebook, that's what happens. You see a URL that says nbviewer.ipython.org and then the original path to the notebook. If it's on GitHub, we know where they are, but this URL could be anywhere.

This is an example of a URL at MIT and so you see here a completely nbviewer.ipython.org slash URL slash the original path to that notebook, but what we do is we take that notebook, convert it to HTML and render it as a standard webpage. So your colleague can read what you did and view it as a normal webpage with just a web browser and we see a ton of traffic these days on Twitter where people post what they did on, by posting nbviewer URLs and they share content in this way. Now, obviously this is static.

This is a webpage. I can't execute anything. This is just a static webpage. nbviewer is a really simple service. It doesn't run. We didn't have to worry about Heartbleed because it doesn't run on HTTPS.

There's no authentication. It's just static. Take the notebook, convert it to HTML, render it for you. That's all we do, okay?

But it's a very convenient way of sharing content with your colleague. This is also an example that shows a notebook that was written in a different language. So this language is called Julia. It's a dynamic language for numerical computing out of MIT. We've been collaborating with those guys a lot.

They're great. And so this is a notebook that shows how to execute pure Julia code instead of Python code. So this isn't doing percent anything. There's a native Julia kernel that is behind this and you can run pure Julia code. We have new kernels being written for other languages.

We had an R kernel developed last week. So my postdoc at Berkeley spent about a week working on it and now there's a native R kernel. The Julia one was written in collaboration with the Julia team last summer. Matias just showed me a minute ago somebody wrote an Erlang kernel. There's an F sharp one.

There's a Ruby one. We're now up to about 15 kernels maybe in different languages. Someone had a question. No, no. It's pure.

The HTML, what we're doing is we're running a command called NB. Let me close this. So let's say that I would like to show you this notebook basics. Notebook has an HTML file. I can run IPython, NB convert to HTML, notebook.

I don't know why tab completion isn't working on my shell now. This is bash, not IPy and B. And so I set NB convert to HTML and the name of the file. And what that did is it produced notebook basics.html, which I can now open in Chrome and I see the HTML version of that notebook we were seeing earlier.

So we're doing this for you as a service so that you don't have to do the conversion, attach the file, email it to your colleagues, so on and so forth. So as long as it's on the public internet, we will do that conversion to HTML for you. Yes, because the notebook, when you run code, this output is written into the notebook file.

So we can do the conversion without having to execute any code whatsoever, which is why we can convert notebooks on a service that is converting notebooks written in Julia or Erlang or R or any language and we don't care because we're just converting a JSON data structure into HTML that we assume is made of markdown blocks and text blocks and graphics and MIME type codes, MIME typed tagged output blocks. Yes, question. So the question is, do the widgets work in these static conversions and we can check that. We can check that by going to this interactive widgets and let's look at, for example, Lawrence Differential Equations, which is a notebook widget that provides an interactive call here and there's nothing below it. The answer is no, not yet.

Now, we are thinking of a way, we're planning on a way of recording statically. Obviously, they won't work live because to drag a slider that makes an actual call to the kernel requires a running kernel. But obviously, you can imagine saying, well, what if I record those outputs and cache them and then have a cache of values so that I can drag the sliders and at least see the previous values. Maybe not if there's a text field where I can type new input, but at least for things that had a prerecorded value, we're going to do that.

But that's in the plans. Jake VanderPlas at UWashington who's here, he was teaching a machine learning workshop yesterday. He wrote a version of a library called IP Widgets that does that. It doesn't do it exactly the way we're planning on doing it as a more permanent solution because he embeds all of that output in the notebook itself so the notebooks get rather large, but it works today. You can view on his blog posts little widgets that actually work interactively.

Our long-term plan is to build that as a way of basically caching those controls, the actual messages that go back to the controls, but simply replacing the execution with a read from a static cache. Does that answer your question? Okay.

All right. So, NBViewer is an extremely useful service and whenever you're on NBViewer and you're viewing one of these notebooks, so this, for example, these are the notebooks for a workshop that was taught yesterday from a book, an O'Reilly book called Mining the Social Web. And this O'Reilly book written by Matthew Russell provides a collection of notebooks for all the examples in the book. There's a collection of notebooks and you can browse.

If you provide a URL to a single notebook, we render it. If it's a URL to a directory of notebooks, we show you the notebook directory kind of like in the local dash browser so that you can click and view any of them. And whenever you see one of these notebooks, you can always click here on download and download the actual notebook file.

So, now, that means if you actually want to execute that notebook, that's what you want to do, right? If your colleague can view it via NBViewer, if they actually want to modify it, then all they have to do is click on download. Now, at that point, they may have dependencies, there may be data that they don't have. Obviously, we're not trying to solve that entire problem, but at least the part of giving you the notebook for execution, it's one click away, okay?

Now, this, our NBViewer service requires that the notebook is accessible on the public Internet, right? We have to, you have to give us here a URL of somewhere online that we can go fetch or we special case gist. If you have a GitHub gist, you can just put the gist number. You don't have to provide the full URL and we know how to navigate the GitHub file, the GitHub paths and fetch the actual notebook just by gist ID, so it's very convenient.

But what if you want to share with a colleague a notebook which isn't on the public Internet, maybe inside your company or an environment where you can share public stuff? You can run NBViewer internally. Just run NBViewer in your Internet. NBViewer is just another repository on the project. Matias does the bulk of the work on NBViewer.

And you'd run it and deploy it locally inside your firewall and then you share your stuff internally. We know a lot of organizations that are doing that for sharing work that they don't want on the public Internet. Any questions? Yes? Yeah.

Because when I saved those notebooks, I had run them and the output was there. So when I hit save, we write to disk the file with everything that's on the screen. So now I can choose, that's a good question, I can choose, let's say that I have this notebook and it has all these things and I want to save it without all of that, I can say, all output clear. And if I do that, the notebook is completely cleaned up of all output. Actually, I just realized we don't clear widgets.

We should. That's a mistake. But those don't get saved anyway, so it doesn't matter.

But this notebook gives you a clean notebook with zero output. If you want to give to someone a notebook just to get started with or you don't want images saved in version control, for example, you can say clear all output. You can also say run all and then that executes a whole notebook.

So for example, one thing that you may want to do and that we do often in research is say, let me view my toolbar again. Restart the kernel. I've done a bunch of work. I've been working for three hours on a data problem. I've gone back and forth.

I'm a little lost. I want to check before I send this to my colleague that this whole thing actually works. So, restart the kernel. I lose my state. I cleared all output and then I say, run all.

And this basically runs through the whole notebook top to bottom and executes the entire thing in one long shot. So, it gives me a chance of kind of creating a clean notebook where the prompts are numbered back from one, two, three, four and kind of having and checking that the whole thing actually run because I've been working on it for four hours and I'm tired and I don't remember if I did things in the wrong order. And before I send it to someone, I want to make sure that what's on my screen really works if they start from scratch.

So, you can say, restart kernel, clear all output, run all. And if it works, you save it and you send it, okay? So, now, let's switch for the next 20 minutes into some slightly sort of less flashy and exciting topics but very important ones about using IPython as a system which is, how do you customize this thing? IPython is a pretty complex architecture by now and there's some concepts in here that are really important.

So, when you run IPython at the command line, if you say, IPython dash H, we try to give you help. We try to give you a lot of help. This looks funny, funnily rendered because of font sizes but it actually, on a terminal, it's not that bad.

But I'm going to zoom back up so that even though it looks ugly, the people in the back can actually see something. So, IPython dot H gives you help. IPython has a lot of commands, IPython notebook, IPython QT console, IPython console and they all have lots of flags. How do you find about all these flags?

If you say, help all and you grep on a given pattern, right, you can find out what is the command line flag for whatever because what I, the way IPython was written, actually every property of every object that makes any of the IPython applications can be set at the command line. So, not only can you configure it by having things in config files which we'll see in a minute, you can change flags at the command line which means you can either do them as one-off things or you can have aliases for a few things that you'd like to do. But there's a million flags because literally every property of every object that makes the IPython system can be configured at the command line.

And so, a common one is, I don't want the IPython terminal to ask me whether I want to exit all the time or not. How would I find out about exit? If you say, help all, then help all, help all will actually print every flag that IPython has. And obviously, that's pages and pages. You grep for the word exit.

And so, here you see that, oh, you can force a direct exit without confirmation by typing, no confirm exit. Or you can set the flag by saying, terminal.interactive shell.confirm exit equals false. So, what you'll see is a lot of flags have this format, dash, dash, Python expression equals Python value. That's because all of the values in the configuration files that are Python object properties can be set at the command line with their fully qualified name. And we have a pretty elaborate system that basically reads this command line flags and applies them at initialization time as object properties.

The config part of IPython is actually kind of a project in and of itself. It's one of the most complex pieces of the project. So, the principles of configuring IPython are that configuration is always done using these class attributes that describe all of the objects that make the machinery. And yes, it is complex, but it gives you a lot of freedom to create effectively custom applications for your own purposes. We have a parent abstract class called the configurable that defines the pieces of the applications that are configurable.

And you can set flags on them by giving the class name and the attribute name equals value. And if you do it at the command line, it's dash, dash, attribute name equals value. If you do it in the config files, our config files are just Python scripts.

And these Python scripts are stored in what are called profiles. So, what IPython does is it lets you not only configure these things at the command line, but you can store configurations in groups of related stuff. So, IPython lets you define as many profiles as you want. There's always a default profile, which is called, oddly enough, profile default.

But you can create profiles with any name that you want. And the idea of creating profiles is, let's say that I want to start an IPython session and I want to preload these libraries for connecting to this database and I want my notebook server on this port and I want the kernel to be started with this flag. But I have some other thing where I have a completely different set of things, right? Python lets you configure the default shell in a very primitive way. You can define the $python startup environment variable.

It's one variable and it can point to one file that gets executed at startup time. Obviously, that's nowhere near enough. I mean, that's okay for the Python shell, the idea of the Python shell. It's a lightweight and quick system.

For the amount of stuff that we do in IPython, that's nowhere near sufficient. So, we created the concept of profiles that has existed for since the beginning of IPython. And a profile gives you a way of containing and naming an entire set of related configuration things.

So, let me create a new profile. So, this is how you create a profile in IPython. You say, IPython create and you give it a name. I called it new profile in this case. You can find where it is.

So, IPython, if you run IPython locate profile instead of create profile, it tells you where it put it. And, well, in fact, when you create it, it also prints where it put it. It's just that I had already run this so it already existed. It didn't make a new one.

But in here, it says, in my home directory, .ipython, the default profile is profile underscore default. The new profile is profile underscore new profile. They're always named in that way. Profile underscore, they are directories. You can find out where the current profile you're running under is by calling get IPython which is a globally defined name that gets you the current version of the kernel.

It's the kernel object itself. And then calling, finding the location of the profile directory. In this case, I'm running with a default profile. Let's see what's in there.

Let me call this with dash L. It may be a little bit easier to read. So, this is what is stored in there. We have a security directory where connection data is stored securely. It has read-only permissions for you kind of like .ssh.

It has a static directory where you can store custom static data for the notebook, custom JavaScript, custom CSS, all kinds of stuff like that. Some logging stuff, your history, your history, all of your inputs are stored in an SQLite database. So, anything you've ever entered is stored and you can actually grep and you can open that SQLite database and mine it for data if you need.

And there is, and the config files themselves are there. So, the config files, this is what the actual IPython config file looks like. So, this is where you can put code and flags to configure IPython itself.

So, I actually have some stuff that I load. If I'm running on, okay, this is old stuff. I can, I want certain flags changed from their default values.

So, these config files are put there and by default, they're all commented out. But you can put, you can change, these are these flags that I was talking about that you can change at the command line as one of things. You can also change them here permanently. And this, and these files, even though they are, they're meant for configuration, they are Python scripts, which means you can do things like check your operating system name and make decisions depending on what OS you're running on or the time of day or the username you're under if you want to share a profile, but in different systems, you have different usernames. Whatever you want to do, you have the full power of Python to execute.

Everything you do is assigning attributes on this C object, which you get at the beginning by calling get config. It's this object which acts like a dotted dictionary to start appending values into it. And so, what we do is we create these trees of objects and we ship those at initialization time to the objects to initialize themselves and get started.

So, I'm explaining this to you guys, not expecting you to be able to do anything too complicated right now, but so that you know where the bodies are buried because this is a question that comes up fairly often is, how do I configure this thing? And there's a lot of power available to you in there to create. The nice thing about profiles is that you can make them completely self-contained and then you can share them. And we see projects that share profiles under version control. Say, if you want to run for this thing, just install this profile.

And then you start IPython with that profile. And you have everything you need preloaded for what we're going to do. You can include JavaScript extensions in your profiles. You can have preloaded startup files.

So the startup directory is a simple directory that contains files, Python scripts. And they will get run at runtime, at initialization, in the order that they're named. So kind of standard Unix style. You name them if you care about the order. Just name them with numbers so that we execute them in that order.

If you don't care, name them whatever you want, if it doesn't matter. So if you want a bunch of code always run at startup, you just put a script in the startup directory, and it'll get executed at startup time. So let's skip on, the little exercise there isn't really super important. And I want to have time for the last piece and a couple of questions.

But there is an exercise that I do want to do, because this comes back to a question that a couple people asked me earlier. And I said five minutes. I thought it was later in that notebook. I'd forgotten that it was in this other notebook. That actually came an hour later.

But both of you guys asked me about that. Which is how do I define my own magic? So we saw earlier how to use magics, right? We had line magics and cell magics. Well, what if you want to write your own magics?

Well, it's actually pretty easy. We actually define an API that lets you decorate a Python function and turn it into either a line magic or a cell magic. So you import these decorators, register line or cell or line and cell magic, because you can actually write a function that can be called as either 1% or 2%.

So remember, line magic is 1%. Cell magic is 2%. And this is a line magic that all it does is sleep for the amount of time.

So I'm going to have a percent sleep. What it does is it takes that, turns it into a float, because the time.sleep command expects a number. And remember, the line gets it as a string.

And then we sleep for that. So here, I'm sleeping for two seconds. And you see, we're back.

Let me sleep for five seconds. And you'll see up at the top, this is busy for five seconds. The kernel is sleeping, so it's busy.

And then it's, and if I ask question mark, you get question mark on it. If I ask two question marks, you get the source code for it, like always. So it actually hooks it into the running IPython system at runtime.

If you want a few magics persistently defined, you do that in your startup script, and then you're done. You have your own magics for whatever, and you can define magics for your own profiles. Cell magics take two commands, because a cell magic also sees the rest of the line where it's declared, right?

So what that does is it gives you the ability to have a cell magic that takes parameters. So a line magic is a function that takes one argument, the body of the, just the rest of the line. A cell magic is a function that takes two arguments. The rest of the line, and the body of the cell.

So this is a cell magic called dummy. And if I call dummy, and this is what I put on the line, and this is what I put on the cell, and it prints them, this is what it does. So with this, you see that because the lines, as you see here, I'm just calling print. The input to magics, both line magics and cell magics, is just the text, right? That's why magics can do whatever they want.

That's why they can say this is Bash code, not Python code. That's why they can say this is Perl, or Ruby, or whatever. Because the magic itself gets called with that as a block of text. And it can interpret that text in any way you want. It can say this is Python code that I'm gonna run under the control of the profiler.

This is Bash code that I'm gonna save to a script and execute separately. This is text that I'm gonna write to the file system. It can do whatever you want, right?

So you have arbitrary control. You get both the line and the output, and you can do whatever you want with it. This is the highest level API for simple magics. We have very complex magics written. I put a link in there to the documentation that shows you how to define more complex magics.

So we actually have a class that you can use called the magics class. You can inherit from it, and then you can define methods on that object that behave as magic functions. What that allows you to do is to have magics that are stateful.

So for example, we have a magic called the R magic that lets us execute blocks of code under the control of the R interpreter, but we have to keep that interpreter alive in between executions because it's like, just like you have the Python kernel, now we have the second thing running there that's alive and persistent. So we have an object, in this case a simple line, just a function isn't enough. We really need a persistent stateful object that has things like what password it started with and temporary files open, all kinds of crap that has to happen under the hood. That guy is an object that has methods that all act on the same state of the same R interpreter, but it actually exposes not just one magic, but multiple magics are coming from the same object.

So the object-oriented API really gives you kind of full control, but for simple things that you just want to do one thing, you can register them as line magics. And one important point about the value of being able to define your magics is the following. Let me, I have this dummy magic here, right? I have dummy here. And this just prints the input.

What if I say dummy equals 100, right? Dummy is 100, but double percent dummy still works. That's the value of this funky syntax that creates an orthogonal namespace.

So when we look these things up, we know that the percent things refer to a namespace which is separate from the variable namespace of the language and so that you can have names and it doesn't matter what you're doing with your code. You never clobber the control layer of your commands, of your magic commands by creating variables that may collide in names because those guys are always escaped with the percent names. It's actually a separate table of names that we look, where we look that stuff up. You have a question? You have to share the profile.

You have to share the profile. Or you could put the magics, you could put the magics at the top or you could put them in a script and run that script and share the notebook, share kind of a project. That's up to you, yes, yes. No, the notebook. No, we don't have any, I mean, that's kind of an open-ended problem because you could be, those magics could be imported from other libraries.

Anyone can define a magic. So in fact, there are packages that define magics. Some of our magics, we're actually starting to ship them out to their own projects.

So right, we have a Cython magic that lets you put inline blocks of Cython and we automatically compile it and load it. That magic is being removed from my Python now that we kind of know what it needs to do. We're shipping it to the Cython project.

So that magic has to be imported from Cython. So we can't package a notebook that can potentially pull in half the operating system with it, right? So the problem of dependencies is not a problem that is within, the problem of dependencies and the problem of Python packaging is beyond scope, as we say. It's in scope for the gentleman in the back. Question.

Yes, those variables are, in the namespace. So if you say ip equals get ipython, you get the ipython object. I'm not gonna print all of it, but, ipython.userns is the user namespace. That's your namespace. ipython, the question for the recording is, could a magic refer to variables that were declared elsewhere?

So the kernel doesn't see the notebook document, it sees its namespace, right? So when you run code, you're running code in the Python process. What namespace does it see? It sees this dictionary. It's called userns, it's the user namespace.

The reason we do that is because we have to execute our own code for ipython itself to operate. So we execute your code in this special dict called userns. And that code has all of your variables defined in it.

So if I say, these are the first 10 in whatever order they're coming out printed from the keys, these are the first, from everything we've been doing for a while, right? So you can, in a magic, it's arbitrary Python code. And whenever ipython is running, this get ipython is one of the few things that we do to pollute the global namespace. We shove this thing into the built-ins, I think, so that it's always there.

And so you can get a hold of the running ipython and operate on that dictionary and do whatever. You can modify it if you want. You can trace things, you can do whatever you want with it. Does that answer your question?

Any other questions? Okay. So, last, I wanna talk about running a public notebook server, right?

So this is a very quick tutorial. So what, by default, I've been running, as you've seen, whoops, my notebook is running on, and yours are running on 127.0.0.1 on port 8888, HTTP, not HTTPS. If we want to run a public notebook server, we can.

And the way to run a public notebook server is to turn on SSL and password protect it, okay? So if I, and the way you have to save the password for the notebook is you have to save it salted and encrypted. We don't store plaintext passwords. And we created a function to make it a little bit easier for you, which is called password. And that function, running it this way is a bad idea because I'm actually typing the password in here, but this was for illustration purposes.

But you can run that at a terminal. You can run this block of code at a terminal, and we'll do the salting and encoding for you in a Python terminal that you quit, and you don't save that anywhere. And I would recommend running that in a normal Python terminal, not in an IPython one, so it doesn't even go into your SQLite history database or anywhere. And once you have a password, you create, it's a good idea to not run this on a standalone profile because you want to configure it a little bit differently.

So let's create a profile called notebook SSL. And we can set our password in there. So I've created, as you see, we randomized the salt.

So we encrypted with SHA1, here's the salt, and here's the encrypted password. We can add this flag to the notebook in the config file. In that profile, we add this now to the password field of the server. And second, we create a certificate as well. In this case, well, in this case, I am creating a certificate.

If you're in an organization that actually has proper certificates, I would recommend that you use a real, properly signed certificate. But in this case, if you just want to do it for personal usage, you can create your own certificate. If you have OpenSSL installed, if you have a currently patched version of OpenSSL that's immune to hard bleed, you do this.

If you don't, don't. You create, you can create a self-signed certificate, and then you give it where to store that certificate, as well as the key file, and you also want to run it on your public IP address, not on local host, unless you're gonna tunnel traffic over SSH by hand, but I'm assuming that you want kind of a simple setup where you actually can find that machine on the public internet. So you tell it, instead of running on local host, to listen on all IP addresses. And you probably want to also tell it not to try to open a web browser at startup, because this is really gonna be a server.

So once you do that, then you can say, notebook dash dash profile, the profile name. So this is the beauty of having this concept of profiles, where you can isolate complex and related sets of configuration options for doing different things. You can have your default notebook running locally, and this configuration, I actually use this as a backup option when I'm giving talks and tutorials. I have a notebook running back at Berkeley in my office that has the same stuff that I have here, and so if my laptop dies, if something funky happens, I can borrow someone's laptop, connect to that, type in my password, and I'm off to the races again. It's running the exact same code, it has the exact same thing, and I actually don't leave it running forever.

I just turn it on before the talk and turn it off afterwards. Still, it's still an open, keep in mind, you're running a server that has access as your user to the entire, I mean, you're basically giving yourself, anyone with that password has effectively as good as SSH access to your machine, right? So this is really, really potentially dangerous, but also very useful if you know what you're doing.

So you type that, and that is running. Again, I run it on a tmox session so that it's persistent, and I log out of that server, and I leave it overnight, and the next day I know that I have a plan B running in my office, and it has saved my butt a couple of times, okay? Any other questions? It's, I, Nick, the question is, has anyone tried to do this with a sandboxed Python? Nick should correct me if I'm saying something wrong, but my impression is that the core Python team has pretty much settled on the fact that there is no such thing as a sandbox Python.

That, I mean, if you're thinking about a restricted Python, you can obviously run this in a VM, or in a Docker container, or an LXC container, or something where you use OS-level jailing and containerization technology to protect that process. That's the way to do it. The notion of sandboxing the Python language has been proven over and over and over to be a figment of the imagination of people who think they can do it, but every time somebody has tried to sandbox the language, they realize that you can sandbox it if you cripple it to the point of doing nothing more than one plus one, but that having any sense of a usable Python will give you hooks back into arbitrary execution, and people have found all kinds of creative ways of doing that, so if you really want to containerize something, you should containerize it at the operating system level, and especially because in IPython, we do so many weird things that I promise you any version of restricted or sandboxed Python that somebody might think is useful will not run IPython. We do, we use every piece of the standard library. We use private methods.

We use sys.underscore getframe everywhere. We do lots of nasty things with the heart of the interpreter. Any of these sandboxed Pythons will have closed most of that off, and IPython won't even start. I promise you that. Question?

So, if we're using this, users can overwrite each other. So, the question is, if we're using this, users can overwrite each other. The answer is yes, because there is no concept of users. You're locked, there's a password field. There's no user field.

It's you. Now, the concept of a multi-user IPython notebook is coming, so one of the grants that funds our work from the Alfred P. Sloan Foundation is supporting that, and that, we just released 2.0 four days ago, or five days ago, and we're going to be five days ago, and now we're starting to work on 3.0, where we will write the first prototype of that, so that then you will be able to deploy, as a daemon, a proper server that will authenticate with your local Unix accounts, or with maybe your organization's authentication system, and then it will give people a login, and they'll get their own personal notebook server, but that doesn't exist yet. In the meantime, people have written ways to basically have a little mini load balancer sitting in front, and spin up Docker containers for people.

So there's a project called IPyDRA, yes, I was going to, Hydra is the old Stanford one that started it from friends at Stanford, but it was kind of rewritten into a cleaner version called IPyDRA, I-P-Y-D-R-A on GitHub. And IPyDRA basically lets you start easily, kind of notebook servers, one per user, and there's also one called Jiffy Lab that does similar things using Docker, to basically create Docker containers for each user. So these are kind of solutions that exist right now, we're gonna build a full multi-user server in the next few months. And now I'm basically in open questions for a few minutes, and then I have to give you guys a few minutes to do the survey, thank you, the survey.

But yeah, I'm basically done with the material, so. Yeah, and it seems like you're done with the material, so I'll go ahead and ask a few more questions. I'm just wondering, like, you know, what are the main reasons you use IPyDRA on a notebook or IPyDRA on a server? It depends on what you're doing, I use both. I use all three, in fact.

I use the Qt console, the notebook, and the REPL all the time. Sometimes I'll have a notebook, and a Qt console open on the same kernel, basically the Qt console is like my scratch area, code that I don't wanna save, I just type it in the Qt console, because it's nice and it can get plots, and I can get multi-line editing, and then the notebook for stuff that I'm saving, think of it like writing in clean and having a piece of scratch paper for something quick and dirty here. I use the terminal all the time because it starts quicker, the REPL starts much quicker. If I'm SSHing into a remote machine and I just wanna do something in Python quickly, I use the IPython REPL.

But the REPL is limited to what read-line can do, so multi-line editing is absolutely miserable in a REPL. You really don't wanna type more than two or three lines of multi-line code. I mean, we do an auto-indent for you, and we try to make it nice, but it's really, I mean, a terminal is not the place to edit complex multi-line code.

So they all three have value, and they all three have kind of their role to play. One point, one important point about running code is the %run magic lets you run a script. I have a script that produces an error deliberately, but the point is %run is one command that I didn't mention much because in the notebook, it's kind of superseded because in a notebook, you tend to type yourselves, and if you have a little script-like blocks, you put them in cells. In the terminal, well, you don't have much of that, so the workflow if you're working in a terminal is more edit a script with a text editor, and you wanna execute it.

But if you wanna keep executing scripts that update your local namespace, or maybe pop up figures, and you keep working, %run lets you do that. %run is basically exec file on steroids. It runs a script, updates your local namespace, and lets you keep on working. I still use that in the notebook if I wanna move a bunch of common code out into, basically, I have a bunch of code that I wanna execute in three related notebooks, and I wanna load them. I don't want to copy-paste it into cells of all of them. I put it in a PY file and I put %run at the top of the notebook, run and load it and then I can have five notebooks that load a bunch of common stuff in that directory without like having a profile or anything.

So %run still has its value and I should have mentioned it earlier. Yeah. But the REPL is still very useful. I mean, the REPL is valuable. Sometimes you're just SSH-ing into a remote machine.

As I said, it starts up much quicker so it still has value. Questions? Let me check on the time. Oh, it's 12.20.

So I think I should stop now and give you guys a few minutes to answer the survey. If you go into the dashboard, there is there a PyCon 2014 Logistics Notebook that has the links to the notebook. I mean, you don't have to read them from me. You can click on your own or you can read them from here. And those are links to the survey and I'm going to give you guys, I should have given you probably more time.

I'm sorry. I thought we had five more minutes. But I'm happy to continue talking. I'm going to be here for the rest of the conference.

So if you have any other questions, please come and ask me. Otherwise, thanks for your attention. Thank you, Matias, for helping. And take a few minutes to answer the survey, please. I do want to honor that part of our commitment to the conference organizers.

The feedback helps them basically know how to make the tutorials better. Thank you.

