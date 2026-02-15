---
title: "IPython In-Depth: Interactive Tools for Scientific Computing"
summary: "Tutorial at SciPy 2012"
date: 2012-07-17T00:00:00
tags: ["tutorial", "transcript"]
slug: 2012-07-17-scipy-2012-tutorial
word_count: 20196
source_file: transcripts/2012-07-17-scipy-2012-tutorial.md
content_type: transcript
event: "SciPy 2012"
video_url: "https://www.youtube.com/watch?v=AvknbGH01FE"
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

in parallel. What PyPub lets you do is take your function, take your data, send it out to Amazon's S3, EC2, Alexa Compute, Cluster, Cloud, whatever it's called, you know each that's chunked up into different parts, several nodes, they're all computed, the results are collected and brought back to you. So in the background you've set up some EC2 instance for this? I don't have to set up anything at all.

So PyPub is a service for you. You get 23 hours to start with and once you go beyond that then there's a fee per transportation hour, very low, depends on what resources you want to use. So I'm still well within my 23 hours here.

So let's see, let's get some data here that we want to compute. So let's say, data equals range, 1000, and let's say it wants to do the equivalent of, so f of x is going to be returning x to the x, okay? So we can do map, f, data, and we get this list of results back, okay?

Now let's say, for whatever reason that it wants to compute this on the cloud, using PyPub. So what I'm going to do is I already imported cloud, so import cloud, and then you would say cloud.map, f, data, and you get this weird x-ray and you just name it back. It's obviously not the same result, right? What that is, is a list of keys in two dots on PyPub, and then what you can say is cloud.result, underscore, so just the previous value, right?

So I'm going to do that, it's going to, basically now it's going to go to PyPub and say, give me all those results back, and you may think, wow, this is taking a really long time, and it is just because this is mostly just network communication that's going on. The jobs themselves take almost no time at all. So the point here is that you want to make sure that the work you're doing, when you're doing cloud computing, the work load is really big, because there can be a lot of overhead in communication.

So we sit here and we wait, and one thing you can do is you can look at PyPub, it has this nice interface. And if you look here, so these are all the jobs that are running in PyPub, and this top one here are the jobs that are running currently. And you see the status here is about half of them have completed and have returned. You refresh the page, you see the number is going up eventually.

So it's time to collect all this stuff back. How many instances have you got? I don't know.

This is launching 1,000 jobs, I don't know. So yeah, it may be launching 1,000 jobs, and each one is running on different clusters, so there's a lot of overhead. I'm sure there's control for tweaking that to be able to chunk it up into different sizes, but I can see, I mean, since there are so many virtual cores on each EC2 instance, and you just have one large or something, I can see it not being that many instances, actually.

So the thing you're charged for is the run time, and look at it, it only, there we go, let's go back here, you see that it finally returned and gave us back the result. So that's PyPub in five minutes, and there's a lot of other functionality, the main interface is the map, as you recall, so it's the same kind of thing that we've seen before. Thank you, thank you everybody.

We have three of the core i5 developers here with us today, Ming-Reng and Kelly, who many of you already know, and Mathias Bussonnier, who is a new member of the team. Mathias started contributing a lot to the project to the point where we realized it would be much better to bring him in rather than trying to keep up with his pull requests. So I think this is going to be helping us floating around the room if any of you have any issues, so obviously you're welcome to stop us any time with any questions, but if you get stuck on something, perhaps a little bit of vocal help can get you unstuck, just raise your hand and Mathias will try to come over and see if he can give you a quick help on the go. In scenarios of tutorials of this kind, we've found in general that that works really well, and it helps keep things going along.

So, did everyone get the installation instructions, and does anyone have any installed problems now that perhaps Mathias, because we're hoping that most of you will basically follow along with what we're doing, little exercises, we don't have a big, long, 4-hour PowerPoint presentation for you, but we have a lot of hands-on work. So, Mathias, will you come in to give me a hand? I just wanted to say thank you to the others for effecting this on my Mac, I basically can't do anything that relies on the Mac.

Okay, so the QT stuff is going to be absolutely minimal, because we knew that the installation of that could be tricky, so we deliberately are keeping that to an absolute minimum. So, I will simply show something in QT, and that's about it. So you can see how it works, and later you can go ahead and fight with the QT installation. We knew that one would be potentially tricky, so if you don't have the QT stuff working, don't worry about it, you won't miss anything, you can just watch what I'll do in five minutes. The IPython 0.8 is important to have, right? 0.13.

Okay, 0.13. 0.13, ideally, yes. 0.4, yes, yes. But we're not going to be using anything special that isn't in there. Oh, there it is. What happened? Three.

Better? Okay. How do we put this on this one? You've got it.

We've got to figure out what's going on. Alright, so who has IPython 0.12 instead? Okay, so we do have a few with 0.12. Do you want to upload the v2 version somewhere in Dropbox? Do you want it in the URL?

This one? So, for those of you, because we are going to be doing a lot of things with the notebook, for those of you who are on 0.12, we don't want to burn time right now trying to do an upgrade of multiple IPython 0.13. So we've created 0.12 compatible versions of all the notebook files. And they are here in Dropbox, in that cardboard.

So you can go ahead and grab it. And the way to find it is twitter.com slash minark. And the top tweet has the link. Does everyone from 0.12 have this information?

So I can switch to 0.13. So for those of you on 0.13, all of the tutorial materials are in this repository on GitHub. So you can go ahead and either clone it if you want, clone it locally, or you can always click here and get a zip download of the repository as a single zip file, in a directory. We only have a handful of slides. And no, they're not there, but I can make them available later.

Because we only have a very few slides. So yes, I can put the PDF up later. Okay, so we're going to give you, while everyone downloads and whatnot these things, we're going to give you a very short overview of the project.

And then we'll switch to hands-on work. Was that something for me? No, no, we're good.

So why was iPython created, and a reason other than me not doing my thesis? Basically, the I is for interactivity. And the reason is that scientific computing, which is the reason why we're all here, is inherently an exploratory problem, where typically we don't know what we're doing in the sense that we have ideas, we have certain tools, we possibly have data, but we're looking for understanding for a problem. It's very rare in scientific computing we write code against a well-defined spec, where somebody tells us this is what you have to write. Other than in somewhat artificial homework settings, that is not the reality.

So having a way to work in an exploratory way is really important. And it's no surprise that MATLAB and IDL and Mathematica and Maple and just about every scientific computing environment has some kind of interactive system, because it's just a necessity. And Python could be a decent interactive system. The operative working could, because the default interactive shell that ships with Python is pretty lousy. If you try to type something like, oh, I want to look at my files, you get an error.

You try to find information about something, you get an error. You pass it a path in an intuitive way, you get an error. When you actually manage to run a file, the tracebacks are not the most important.

This is what a typical session in Python looks like. And so we think we can do better, and we started writing initially, because this was kind of an afternoon hack, to make something where you could combine the kinds of things that you need to do in everyday scientific computing work, which is to mix the language with your environment. To access data, to access files, to run code, to understand the problem, to visualize data.

So in Python, if you type ls, you get your files. If you pass an object and ask with the question mark for information about it, it will give you all of the internals of the object, including its source code syntax highlighted. If you run a script, there's a run command, which you can give a path in a syntax that is familiar to you with path completion.

And then if you get an error, you get a traceback that goes like that. So this is exactly the same error that Python would give you this bit of information for. We give you something like that, with multiple levels of the tracebacks, and color highlighting, and you can even have variable values at that point. And in everyday work, it saves a lot of time. Cognitively, to see information like that, it makes it just far easier to quickly pinpoint exactly what's going on.

You don't have to spend so much time debugging, but actually running code. Then we think it is important to provide tools that make this process easy. So this was sort of the beginning of Python. A console that would be better than the default Python one. And we ended up having support for plotting, and you'll hear a lot more about that in the map of the talk that John will give later.

So it was basically an environment that would give you a MATLAB or IBM-like old-style shell, and you could do code, and you could have plots, and multiple plots would not block the execution of code. This is what we had for a while. But over time, we developed this into a fairly rich architecture that also allows other things, such as the Qt console, which I will briefly demo, but those of you who don't have Qt installed right now don't have to worry about it. It's something that feels like a text console, so it has the very same library feel of a terminal, but it actually lets you include inline figures, it lets you do multiline blocks of code, and edit multiline blocks with syntax highlighting and graphical tooltips.

So it's basically a blend of elements from a graphical user interface and elements from a text terminal design for scientific computing. And yet, it supports the same syntax and the same features of a basic Python service, based on the same exact architecture. Based on that protocol, Microsoft developed a plugin for Visual Studio that uses the exact same protocol and plugs into Visual Studio so that you can use Visual Studio for Python development and have an embedded Python console. And based on the same architecture, later we developed what we will be using today for most of the work, which is the web-based notebook, which is something that we had wanted to have for a very long time, for many reasons.

This is the kind of environment that is inspired by a system like Mathematica, and maybe especially Mathematica. Both Brian, me, and myself are all physicists, and at least Brian and I have used Mathematica extensively, and we love it. And we had always wanted something like this for our Python workflow, so we finally have it now.

Additionally, iPython provides a fairly powerful library for parallel computing that is a very high-level system that allows you to have not only one iPython, but N iPythons, all of them controlled by a single object called the iPython controller. To which you can connect and disconnect, you can send it commands, you can send it data to scatter around in your engine, you can send it jobs to be executed. These connections can come and go, which means that this entire cluster can be active and running in a system to which you connect, check for something, disconnect, and let it continue running. Multiple of these connections can happen at the same time, which means multiple people can be logged in and looking at the same data for collaborative work, and we will see more of this later on today. A very quick history of the project.

It started, as I said, as a quick afternoon hack. Initially, it was just a configuration file. But eventually, I realized that I wanted to do a few more things with it, and I discovered two other projects that were related to my little hack.

One was called iDP, and one was called lazyPython. I contacted both authors, and they both graciously said, go ahead, use the code, I'm doing the thing, I'm doing something else. So, having the thesis to write, I dove into that, merged the three, and thus, iDPython was born. In 2002, I actually did have to graduate, so when John Hunter contacted me with some patches for plotting support, I told him, no, right now, I'm really not messing around with iDPython, I really have to finish my thesis, and the rest is mathematical history, which you'll hear about tomorrow. In 2004, we joined forces with Brian, who was a classmate of mine in physics at CU Boulder, and Min was, at the time, an undergrad student of his, and Min's senior thesis project was the first prototype of the parallel computing machine.

So, in fact, what you will be using today is a complete second implementation after years of experience with the first prototype, which was based on a library called Twisted, and the new system, we think, is a lot better, but benefits from the hindsight obtained during that period. We had a few kind of slow years of slow and incremental updates, a few important features were added, but no major changes. And finally, around 2009, we were able to refactor the internals of the project in a major way if needed. It had become basically a big, very dense, very monolithic, and very difficult to improve code base, and we were able, with some NIH funding, to support Brian to spend a summer basically disentangling that mess and setting up a cleaner architecture. And that brought us to 2010, where we discovered a networking library called 0MQ, which is kind of the secret sauce that underlies all of the communication that we use, both for interacting and for parallel work.

And Enthought supported the idea of building on top of 0MQ this famous QT console that we've talked about. And what we did was we built the QT console between ourselves and Enthought, but at the same end of the process, we left in place an architecture that would then allow us to build parallel computing and the web notebook and everything else and do the same thing. So, that was a very successful effort. At the same time, we got a Python 3 port.

And then, based on that machinery, in 2001, the web-based notebook was developed. Now, at this point, we have about 110,000 lines of code. It's a large project.

We have over 130 committers. This is a very complete credit list. The people in bold are the people who are committers to the project. And those in blue are simply those who are active physically here in the room.

So, there's three in addition to myself. Mia and Matias are here. But we have a very active project. All of you are obviously welcome to use the project, but our hope is that some or many of you will actually become contributors eventually. And GitHub makes that very easy.

IPython has become a fairly widely used project. These are not just people who use it, but rather projects that build upon IPython as a tool. It's widely used both in scientific and non-scientific projects, and we're happy for that. Even though our interest is scientific, IPython itself doesn't have dependencies on NumPy or Matplotlib or any scientific tool. IPython by itself runs only using the standard library.

So, people outside of the technical computing world find it useful as well. So, to wrap up this very brief world-wide introduction, we have to thank the people who have supported us. Anthos, as I mentioned, since the very beginning, they hosted our mailing list. Eric contacted me, I don't know, I think it was probably two, and offered to host CDS back then on the mailing list. And over the years, they've supported us in many ways.

And Microsoft, over the years, has also supported us on a number of interesting key points. In particular, now we've been making it easier to put IPython on Azure, because they basically relaunched their Azure platform, and we have an ongoing collaboration with them about that. We haven't had dedicated federal funding from the NIH or the NSF, but we've been able to piggyback on some support. And we do have, thanks to Chris Keyes, who may or may not be in the room, in collaboration with them, we do have some dedicated DOD support for it through the rest of this year.

So, to wrap it up, so that you can have an idea of what you're getting yourselves into, IPython started as a better package shell, but it really has become a pretty rich toolkit for interactive work with some very flexible components, and a high-level and fast and interactive parallel computing API that doesn't preclude using MPI, as we will see later, for those of you who live in the MPI world. And it actually lets you do certain rather neat things that are a complete pain in the neck to do with MPI. So, that's the URL for our website, and probably the second URL is the most important one, which is where to find us on GitHub, so that we can continue and improve the product.

So, let me stop here with the PowerPoint. This is the only slide deck that you'll see for the next four hours. The rest, hopefully, will be hands-on work for all of you. Any questions at this point?

Okay. So let me ask you, who in the room has never used IPython? Don't be afraid, don't be shy.

OK, we do have a few hands. Who has used it lightly? Quite a few of you. And I'm going to assume the rest of you are sort of people who dedicate.

OK, this tutorial was labeled, it was kind of a weird name, interactive slash beginner slash advanced. Because we have a spread of topics, right? And we are going to try to be useful to everyone.

So I'm going to start with a very brief introduction to the basic usage of IPython, sort of the classic usage of IPython. For the next 10 to 15 minutes, much of this may be old news to you, but it will be useful for those of you who are new to the system. And we will gradually kind of crank up the volume in terms of the specification of the tools that we're using. Is anyone having problems with the download of the zip file or the git repository that we gave before? We want to make sure that everyone does have those files unzipped somewhere in a directory, because you will be working there soon.

No? OK, well, that's not very good. OK. Right away, I'm going to change this a little bit more. I want to know from the people in the back whether this font size is enough.

It was more readable dark. A 50-pattern. And how does this work on a video? I'm happy to use it here. It doesn't matter.

Up another notch would be good. But which, with a black background, or what do you want? You had a black. Black. Leave it like that?

OK. And one more font size? Yeah. Is that good enough? Yeah.

OK. So if you simply run the command IPython, this is what you should get. And as I said, some of you are going to have 0.12 or 0.1 here. Hopefully, most of you have 0.13. And those of you running from Gitmaster have 0.13 there. 0.13 is new, and it's recent enough that the difference is between what I have here and 0.13 or not.

We don't see anything in any way. So this is what IPython looks like at this part. And you should, at the very least, heed the first piece of information that it shows you. OK? It says the question mark.

So I'll give you an introduction. %QuickRef will give you a quick reference, a cheat sheet of the main features. Help will call the Python built-in help system. Python has its own help system, which can be accessed with the help command. And for any object, using question mark will give you details about it. And double question mark will give you additional details.

So at the end, we try to put that up front so that at least everyone sees it at the beginning. And let's see what happens. If you do a question mark, this is what you get. You get a little text introduction about what IPython is. Most people never read this.

I would recommend that you spend maybe not necessarily now. But at some point, three minutes reading it, it's only, that's it. It's less than 200 lines. It's a very quick read. It'll save you a bunch of time.

You'll learn a bunch of little tricks about the things that IPython can do, even though I am going to demonstrate some of those right now. For those of you not used to a Unix environment, what happens here is it opens the system pager, which you exit with the Q character to get out of it. And it also said that if you type percent, wait for everything. And by the way, I would hope that you guys are following along with me. Type.

Type as I go. Try to build muscle memory. And everything that we'll do in the notebooks, try to follow along. Try to open them with us.

Because you learn these things by making your fingers do the walking, not by watching. So and if something doesn't work for you, then you can raise your hand and Matias and Mabel will come and help you. And when Mabel's speaking, we'll keep holding. We will always try to come and help out with this stuff.

So what does QuickRef do? QuickRef gives you a cheat sheet. It's a quick reference of the main features that I've described in more detail so that you can remember them quickly.

So these two things are kind of handy to have in there. I typed clear, and it actually cleared the terminal. Why?

Because clear is an alias that we actually add. And I think on Windows, we call it CLS, which is consistent to the system. And this is beginning to show you where I can deviate from the plain Python system, right?

In that if you type in a Python shell, clear, you'll get a name error, actually, because there is nothing called clear built into Python. Whereas we make something called clear. And if you want to know what clear is, what would you do? Exactly.

So if you ask question mark about clear, Python tells you, what is it? It's a system alias. So we have a facility for writing, declaring commands that alias system commands. And clear happens to be one that is predefined. You can define your own system aliases.

And in this case, it's an alias for internal structure. And that's because of how some of the arguments are organized. But it basically is an alias for the system command clear. And that's it. How can you make aliases?

Well, this would be kind of an obvious thing to try. And you can write alias question mark tells me that alias is actually a magic function that defines aliases. So what is a magic function?

This is another part of where Python differs from the plain Python system. And it's a very, very important part of Python A because it's extensively used throughout the system. B, because it's extensible, you can define your own magics to do all kinds of interesting things, which means you can declare those either in your own configuration or you can ship them as part of your projects so that effectively you can define your own control language on top of Python.

So what is the idea behind magics? First of all, how are you getting back to the line command? Q. Q exits the pager, yes.

So whenever the amount of text doesn't fit in the terminal, IPython will invoke the system pager, which is by default less. And to exit the system pager, you hit Q. And on Windows, I think we simply page things one block of text at a time.

But we also honor Q to try to make the experience similar. OK, that makes all the documentation go away. So you can't see, you can't Q and then look up above.

Yes. Yes, that is true. And those are some of the things that get better in the Qt console and the web notebook. A text terminal is a fairly limited environment. There's not a whole lot we can do in a text terminal.

We have no two-dimensional control of the terminal. So some of those things are just inherent limitations of the text terminal, yes. Couldn't you just change your system pager to be more?

So that way you get back what you just. And you can configure your pager. You can configure your pager to whichever one you want.

So you can change that. But some of these suboptimal quirks in the Qt console, for example, or in the web notebook, the help area and the working area are actually separate. And so you can actually keep your system information down here and your work area up here. And they scroll independently.

So up there, we saw something called magic, well, a natural thing to do would be to type magic to see what it is. And magic actually will explain to you what the magic command system is. So I don't expect you guys to read all this, just to know that this exists, because I'm going to explain to you what magic is for. Magic commands are commands that are prepended with a percent sign. I didn't have to prepend a percent when I typed magic, because by default, if there's no ambiguity, we will automatically add the percent for you.

If you type a name which matches the magic, and you didn't put the percent, we will prepend it for you if there's no ambiguity. But in general, if you want to be completely explicit, they always have a percent sign. And what they are, what magics are, are simply commands that take a more command-line-like syntax rather than the Python syntax. And the reason for having this is that the Python syntax, Python is a very nice language, but it's basically a programming language whose syntax requires parentheses and quotes and everything for executing Python code.

But in an interactive environment, it's very useful to have a quick and lightweight way of doing things to the interactive environment that aren't necessarily the code itself. And MATLAB has that. They have commands. IDL has that in the form of the dog commands.

So in Python, we call them magic that was inherited from IDP. And they're prefixed with a percent, which is invalid Python syntax. And magics are called much more like command-line things. They're called with spaces as the interface.

So I can do cd to tmp, and that changes the working directory. This is a lot nicer than having to do it in Python. How would you do this in pure Python? You would have to import os. You would have to do os.chdir, the crime of speaker, not to turn your cell phone off.

Sorry. Excuse me. OK, sorry about that. You would have to do os.chdir slash tmp.

This is how you change directories in Python. So obviously, if you're going to have to change directory all the time as you work, it's a lot nicer to be able to type just cd, whatever it is, than to type all of that. And we've added a long list of magic functions to do common things.

So cd is one of them. And can anyone tell me why cd is a magic and not an alias? Because I said clear was an alias. cd is not an alias. It's a magic. I had to put it in the first place.

It worked with an assumption. Excuse me? Just a command, not a shell command?

Because you need special characters. No. What are you changing? Whose state are you modifying when you do a change of directory like that? Changing your environment.

You're changing the environment of the Python process. But if we make cd an alias, it would do a cd in the subprocess that calls the system command. So you would call a subsystem command, cd on it, and throw it away.

So it wouldn't have any effect. The effect that you're trying to have is change the working directory of the Python process. It's important to understand this distinction because Python gives you such a direct access to the operating system that it's good to have in your head and understand that part of the problem is the Python machinery that you're managing. And you are on top of the operating system. And you can very easily send commands to the underlying OS.

But certain rules still apply. OK? Yes? Can I control the part? Don't I try the part?

Yes, it's completely configurable. Not in the Qt console, but in the terminal console, it's completely configurable. That's it. Excuse me? Just look at the document.

Yes. And we're going to try to leave some time for a Q&A afterwards. And during the conference, you can come to us with questions.

But yes, it's completely configurable with a bash-like syntax. So you can put working directories and time stamps and all that stuff. So another magic that is very useful that many of us use is the timing magic. You want to time how much does executing a Python statement take. You can just type time it.

And Python will actually use a built-in module called the time-it module to very carefully and in a well-calibrated way time the execution of the code and tell you that computing 2 to the 10 takes on this particular lab 58 nanoseconds per execution. OK? So the magic system has a lot of magic. We don't have time in this quick introduction to cover them all.

So how would you find out what all the magics are? We have an LS magic. And the LS magic shows you that these are the available line magics that have a percent. And it also says that there's some available cell magics, which take 2% times. Hold off on those.

They also work in the terminal, but they really shine in the node. So we'll cover them a little bit later. And it also tells you that right now, the magic is on, which means that the percent prefix is not needed if there's no ambiguity.

But if there is ambiguity, you do need the percent, which means that if you declare a variable called cd, which is 10, now cd is 10. But percent cd is still percent cd. So it lets you disambiguate explicitly when you have a question.

Because the overriding rule by Python is that all of these things that I'm showing you are sugar on top of the basic Python interpreter. But IPython goes to extreme lengths to ensure that it reproduces faithfully the behavior of the Python interactive interpreter whenever you feed it Python. So if you type print hello scipy, it will work just like that. If you type hello scipy with a syntax error, it will give you a traceback. Once you do it right, it will give you output.

Notice the difference between print hello scipy and hello scipy. In here, there's an out prompt. Here, there wasn't.

This is something that is also true in the Python prompt, but there is no visual cue about it. There's a difference between returning a value and printing something to standard output. That is also true in the Python prompt, but because there is no visual indication of output in the Python shell, you just don't know about it. In IPython, we make that very explicit and deliberately so because those numbers that are there are not just visual cues. Whenever something produces a result, a variable is automatically created for you with that number, prepended with underscore i.

So for example, if I want the output 15, I can type underscore, whoops, prepended just with an underscore, underscore 10, whoops, 15, and that's the value 10, right? Underscore 19 is the value hello scipy. Why is this useful?

Because if you ran some computation that took 10 minutes and you forgot to assign it to a variable, it's very, very annoying to have to say, shoot, I have to use up arrow and wait for another 10 minutes again. IPython will cache that for you. This is inspired. Mathematica does exactly the same thing. It's that they use instead percent and the prompt number.

That wasn't valid. That's not a valid variable name in Python, so we used underscores. And not only are the outputs, but the inputs are also cached.

So underscore i19, the string that you type as an input is also cached. So you begin to see how, hopefully, kind of the pieces of the puzzle come together to give you an environment where working interactively is easy and fluid. I'm gonna cover two more things, and I think to stay on track, we need to switch gears into the next topic.

The first thing is the most useful key in the entire keyboard in IPython is, probably by space on the keyboard, the key that disproportionately has consumed the most effort in the IPython code base is the tab key. We have literally thousands of lines of code devoted to making the tab key useful in IPython. The i is the input line.

So underscore i19 was the input line 19. And underscore 19 is the output of input 19. And if an input didn't produce an out prompt, there isn't a corresponding, so for example, there is no underscore 10 because the input number 10 didn't produce an out value. It printed something, but it didn't produce a value.

Okay, any other questions? All right, so I was talking about the tab key. Yes, go ahead. Ah, this is Python. Well, I should do another one that's maybe a little bit more, so 17.

And yes, if I do eval, Min is right. Eval, and there we're actually showing you something else. If you see how I typed eval and it rewrote the line and put the parentheses in for me, that's also another little trick that IPython does. If it detects that it's a function call and there are arguments, it will put the parentheses around it for you. And it will rewrite the line.

So we've added lots of little tricks in IPython basically to save you typing because when you're working interactively, finger distances is sort of often the bottleneck. So we wanna minimize that. And I was talking about, yes, question in the back.

Yes. Yes, you can delete that one. And for simply with the underscore I, they're also cached as underscore O.

So you should, if underscore 19 was something that I wanna get rid of, I would say delete underscore 19 and underscore output 19, which are just aliases. Oh, no, they're not, nevermind. No, we never did that, so nevermind. You would just delete underscore 19 and it would be gone. There is a percent reset magic that doesn't kill the current session but flushes all those variables, but all of them.

So percent reset will say, once deleted, all that stuff can't be recovered. You really wanna do it. And then now, none of them, none of them exist anymore.

So you can flush that cache. And the length of that cache is also configurable. How many entries it keeps. Every few, I think, what is it already called, 1,000 or? I think it's 1,000.

So in most cases, before you reach that point, you've already restarted the session at some point in practice. But yes, there is a mechanism to control that. Any other questions?

Okay, so I was talking about the tab key. Let's import numpy. imp tab completes. So the tab key will complete on keywords in the Python language. If I hit num and I hit tab, it takes a few seconds the first time around and it'll give me a message because it's actually, it has to cache what modules can I import.

But once this caching has been done, it's very quick. And now it tells me, these are the three things that can be imported. So I wanna import numpy. And it actually knows how to import, how to read into it. If I wanna import the sub-module, oh, it'll import, I can import numpy.

Okay, let's do the usual thing where we import NumPy as mp, okay, and if I want to explore what does NumPy have, the tab key will show me everything that is in it. So the tab key, it can be used to complete on just about everything. It completes filings, it completes Python keywords, it completes inside function arguments, it completes just about everywhere we can have completion machinery, and you can define your own custom completion for objects.

So it's a very useful way of exploring objects. If you're just learning Python and you want to learn how to make Python strings, the easiest way to do that is make a string and hit the tab key on it and look at these things, oh, I wonder how capitalize works. This is how I basically taught myself Python, by writing this code and actually playing with it. And this is how I explore libraries. I rarely read documentation, I simply import it and start tabbing around and question marking around and very quickly I figure out how things work.

You will notice a strong difference between the quality of the information that you get from doc strings from code in the standard library and from scientific modules. In the scientific community, we've put a lot of effort into writing good doc strings. So if you do np.linspace, this is the doc string that you get. It has parameters, it has examples, it has all kinds of things. And you saw the standard library doc string is two lines long when you get one because you don't always even get one.

That's the way life is. Is it possible to get tab completion on, I guess it's a temporary, so you have an object and you're calling a method and that returns some other object and you want to see what the attributes of that returned object are? No, because if you haven't executed it yet, that object doesn't exist.

We have to inspect something that exists in memory. So that's called reading completion and it's off by default because you can have some unpleasant side effects, but you can turn it on in a config and then it will compel the line and then do completion. But that could be bad. Yeah, it's potential.

So if it's something that you want to only happen once, then you want to make sure that it's off. But for simple dictionaries, that could be fine. Something which is nice about IPython is that, for example, if you see an example when you read the good doc strings that NumPy has and that Matplotlib has, and you see that and you wonder if I can do that example. You can paste it like that. Even with the input prompts.

And it works because IPython will automatically filter out input prompts from either the Python shell or our own in and out with numbers. So it's easy to copy and paste from interactive sessions and we will do the right thing always. So there's a lot more to learn about IPython that we can't sort of... Just about this part that we can't cover right now. I'm only going to mention one last command, which is...

Let me open an editor. Actually, I can do it inside IPython. Depending on how people have it configured. I'm going to... What's that?

That's true. So I'm going to make a small file foo.py, which simply says x equals one, y equals two. And I save it.

So there is foo.py. Okay. I can see the contents of foo.py. Anything that I pass after the exclamation sign is passed straight out to the underlying operating system. Okay?

So if you want to issue a command for which you don't have an alias, just put exclamation and type the command and it will go to the operating system. And then if I run... So let's see if I have a variable called x. I don't have a variable called x.

Let me run foo.py. And I don't even have to type the .py. IPython will assume it.

So this runs that script that declares x as one, y as two, and prints x plus y. And what is x now? x now is one. So what happened there? x wasn't defined. When you type run, IPython executes the script in an empty namespace so that it runs as if it was being run at the command line by itself.

But when the execution finishes, it updates your variable namespace with the contents of the script. The reason for that pattern is that it's a very useful way of writing more complicated code in small scripts rather than... Because the IPython command line is not something where you want to type more than a couple of lines long worth of code.

So you put your real code in scripts, but you do run, and you load your data, maybe you plot something, and you kind of go back and forth. For years, this was the only workflow we had. Now we have other tools, but it's still useful to know this because for simple and quick things, it's still the quickest way to get stuff done.

Basically, you have an editor, you have a shell, you do something quick, you type a few lines in the script, you run it, and then you play with the data. And that back-and-forth workflow can be really, really productive. Do you have a question? Yeah, is there a way to use the run command that doesn't squish the namespace?

So that just overwrote x, right? If I had x equals 3, it's gone. So is there a way to do that so it doesn't... No, no. If I use run method, it's going to send all these variables...

Back into the interactive namespace, yes. There is a way to do the opposite. I know you have a question, I'll be right with you. There is a way to do the opposite.

Let's say that I say print x plus y plus z. If I run foo, that's going to give me an error. But if I have z equals 10, I can... And I run foo, I still get the error because it's running an empty namespace.

But if I say run dash i, run it with my interactive names available, then this works. So you can do the opposite. You can run a snippet as if it was in the interactive namespace.

But what you're asking for, which is the opposite, run the snippet and don't feed it back into the namespace. We've never... I mean, it would be easy to add.

We've never... It's the first time we get a back request in 10 years. It's basically execfile in... Yeah, I guess... If you don't want to get it back, then run isn't really helping you out much.

Yeah, but... You just use the built-in execfile... True.

Yes, if you do this... Huh. Oh, it does it. Oh, yes, you can pass it in namespace, yes. You can pass it in namespace. x is still not there.

So that works. Okay? Question.

So, just curious. If I had written my script in such a way that it does that if underscore name underscore equals main, that sort of idiom that a lot of people use for writing their scripts, how would run behave in that situation? Let me illustrate that, because it's an important question.

So, this pattern is very common in Python scripts. Let me make my font here a little bit bigger so that everyone can see. So, if I now run foo in the normal way, it prints the in main part. If you don't want that to happen, you can pass the dash n, and dash n does not set name to main.

So it'll act like you're just doing an import? Like an import star. It acts like an import... With the difference that it actually does run the code, so it does the effect of an import star with reload, which is impossible to do with import star, because you can't import star with reload unless you do a named import, then a reload, then an import star.

So, run dash n has the effect of not setting name equals main. And you should, if nothing else, read the doc screen for run, because it takes a lot of flags, it has a lot of useful information, it can run code under the control of a debugger or a profiler, it can give you timing information, so you can run a script with dash t, and it'll summarize timing execution times. There's a lot more to explore. We don't have time to stay kind of here, so we're going to switch gears into what's our next part.

Yes, yes. Speaking of reload, stuff that's imported from foo, is that import once and you're stuck with it? Yes, unless you explicitly do a reload, or you put in the script itself a manual reload. We do have an extension called auto-reload that you can look into in the docs, which has been flagged modules for automatic reloading. I've personally not used it, but it was written by Pauli Bertanen, from Sci-Fi fame.

He's really good at it, so I kind of trust that it's good code. But I just don't use it much. So, that's it for the text console.

Let's switch gears into the notebook, so that hopefully all of you can now follow. And what I want you to type is in this godly mess of... I don't know how to change the font size on this thing.

In the directory where you have... Let me do this in this terminal that has the large fonts. This is what you should have downloaded from GitHub, either because you cloned our repo, or because you grabbed the zip file and unpacked it. Or, those of you on 0.12, you grabbed Min's version of the same thing. You should have this.

So, in a terminal, go to the directory called notebooks, which will look like this. And in that directory, we want you to type IPython notebook. And I'm sure we will have one or two people for whom this is going to glitch. Please raise your hand, and Matthias and Min will come and try to help you out if it glitches in any way. The expected behavior...

Matthias, there's one over here as well. Thanks. The expected behavior is this. And by default, it will probably pop up your web browser as well. I have that suppressed.

So, what the IPython notebook server is, is a system that allows you to use all of the same features that you just saw about IPython in the terminal, but through a graphical interface that runs inside of a web browser. And as we mentioned in the instructions, it has to be a modern web browser, which right now means reasonably recent Safari, Firefox, or Chrome, not Internet Explorer. There is no released version of IE that works. Our understanding is that IE 10 will probably work, but we haven't tested it yet. Not even IE 9 works.

So, if you're on Windows, you do need to do this on either Chrome or Firefox. And on the Mac, Safari works as well. I'm running this on Linux.

So, what IPython notebook does by default is this. It opens a web server running on your local computer on port 8888. So, if you go to that URL, you should see something that looks like this. Can everyone see me there? I'm going to try to make...

I think I don't have a lot of wiggle room. Okay, I can crank the size by one, but that's about it. Okay?

Because otherwise I'll begin having to do lateral scrolling. Is this going to be enough for the video? Reasonably enough?

Okay. So, does anyone have problems getting here? This is a good time to do a quick spot check and ensure that from now on we want everyone to be able to follow with us.

So, we're going to... Yes? The Dropbox? The Dropbox, yeah.

Let me go back and show that one. So, rather than copying the Dropbox URL, if you go to twitter.com slash minrk, the first tweet is the one that has the link. This one right here. It may be easier to copy twitter.com slash minrk than to copy that whole Dropbox URL. Anyone else need this information?

Yes? When you have iPython Notebook, is there a parameter you can assign which browser to go to? You can set the $BROWSER environment variable.

So, on all caps, if you set the $BROWSER environment variable... Can you open the browser? Yeah, it will open. It should open the default. Yeah, it just opened default.

I don't know how to open it. I mean, I'm just wondering if there is an option. On platforms that aren't Windows, it's easy. Yeah, if you try just typing capital $BROWSER equals, does that do an executable for another browser? Yeah.

None of the iPython core developers are regular Windows people, so our knowledge and mastery of Windows is suboptimal, to put it diplomatically. So, back here. So, what iPython does is it will show you all of the notebooks that are in the current directory as links, and there's also a tab here called Clusters that we'll come to later. Ignore it for now. Each of these things is an existing notebook.

You can also create a new notebook. So, let's start by creating a new notebook first. So, if we click on this, it makes a new untitled notebook. And one unfortunate limitation of the system as it is right now is that it can only serve one directory at a time.

So, if you want to work on a notebook simultaneously in multiple directories, you have to start it several times. We will add file system navigation to this thing, but it hasn't been done yet. So, for now, you have to start separate ones. They start on increasing ports, 8889, 8898, 8891, et cetera, et cetera, with a caveat that on Windows, because of quirks of the platform, you have to set that port number manually because the automatic port selection doesn't work normally. Does it fix the Infernao matches?

Oh, really? They fixed that in Infernao. Cool.

So, this is what the notebook looks like when you start. It feels, it has a look which is sort of a hybrid between a word processor and a computing system. Those of you who have used Mathematica should feel right at home because it is very much inspired by the design of Mathematica or Maple notebook environments, but with kind of our own sauce.

And here, the difference, though, is that if you hit enter, it doesn't execute because now what you get is cells where you can keep editing multiple lines of code. And you can go up and down, and you can do backspace. And when you actually want to execute that block of code, which we call a cell, you hit shift-enter.

And then when you hit shift-enter, it does execute. So, the model is a little bit different, but it is much easier to build blocks of multiline code. And in addition to code, you can also put text.

So, right here, there's a drop-down menu, and there are key bindings for all of this that lets you change, for example, to Markdown, which is a syntax. It's a markup language that allows you to type simple text and italics and bold and raw HTML and other things. And when you execute this, you get a cell that has that node put in there.

So, you can combine code, results, and text in a single document. And these documents are saved. When you save, this is an actual file that is saved.

So, if now I type ls un, and I execute that, I see there is a file called untitled0.ipynb in the file system. If I type head, and look, the tab completion works in the notebook, too. If I type head untitled0.ipynb, this is the beginning of the file. I'm not going to dump the file for you. It's a JSON format, which is machine readable, and we have utilities to convert it to other formats and whatnot.

So, your session is being written to disk as a file that you can export to HTML, PDF, you can share with colleagues, conversion control, etc., etc. And you can export it to pure PY scripts, as well. So, you can build something coded here, which is then automatically exported into Python scripts if you want to run them normally at the command line.

So, is this basic model working for people? Excuse me? Whenever you execute a cell, it creates a new one below. Oh, shift-enter.

Yes, to actually execute a block. So, when you're inside a block, if you hit shift-enter, it executes that block and puts you in the next one. Sorry, I missed how you got a text block instead of a prompt.

So, when I was here, I went to this menu and I chose, instead of code, which is the default, I chose markdown. You can also choose what we call raw text, which isn't very used yet. It's kind of an experimental feature. Or heading levels, to give the document structure.

Yes, question? Can you get the laptop format? Excuse me? Can you get the laptop format?

Yes, that's coming. Question? You know, you have the five-ended view, etc. I got something on the side of my page where it will cross the top. You got something on the left?

Yes, so you're using version 0.12. Sorry? You are using version 0.12.

This is why we wanted people, if possible, to upgrade to 0.13. The user experience is vastly nicer on 0.13. We rewrote much of the user interface.

So, those on 0.12 have a somewhat clunky looking thing on the left with a few of the menu elements and not everything is available. We'll be happy over the next few days to help you update. But the basic features do work the same.

So, most of the stuff that you'll see here works the same. Okay? Any other questions?

So, as you see, I've been typing LAS. I've been typing exclamation. You can type magics in here. All of the same works. Works here as it works on the basic Python.

So, what happens? Somebody said, how can I see? You asked, Dennis, how can I see the information and still actually keep working, right? Well, let's try that magic with one that popped off the pager, right?

So, if I call that, this is what happens. So, now what you get is a little scroll area at the bottom and the notebook at the top and you can drag this divider. On 0.13, on 0.12, you can't drag it. And to dismiss it, you can just click on it and it goes away. Okay?

And tooltips are much nicer. Excuse me, how did you get it to go away? You click. You just click on the dividing line and it goes away. You click on it.

Oh. So, we also have graphical tool tips for the column with the call signature, which if you tap again, they grow to contain more information, and if you tap again, then they expand into the, into the pager. So, we try to make use of the nice features that the browser provides to make it possible to make, to make, to make things that are impossible at the command line possible in this environment. Okay?

So, this is sort of the basic use of the notebook, but because I don't want to, I want to show you lots of the features available, and I don't want to type them all, what we're going to do next is actually go through a pre-paired notebook that was there, and probably the same, it's a battery-fied or something, which is the one that is called the Quick Tour of the Python Notebook. Sorry, what's a quick way to add a cell? Ah.

So, if you want to add a cell, let me close this, if you want to add a cell either below or above, there are, there are key bindings, but you can either use, this will insert a cell above, and this will insert a cell below, okay? You can also merge cells and split cells, which is very handy as you're doing kind of more editing. You can move them up and down, this, or with the menus, you can move, you can rearrange them, basically walk them up or down. These key, these are cut, copy, paste for a whole cell.

So the normal control C, control X, control V, or command on the Mac work inside for text. If you want to cut, copy, or paste a whole cell, then these will cut, copy, and paste an entire cell. Are the key bindings the same or different? The key bindings are the same, and you can get them here, with keyboard shortcuts. They're kind of funny.

So the key bindings, they all have a prefix, control M, or command M, and then a letter. And the reason for that is that we have to kind of walk the minefield of the interaction between default key bindings on all operating systems and all web browsers. And so the only way to kind of avoid all the possible conflicts was to create a ghetto behind control M, and then make our key bindings there, except for shift enter and control enter. Okay? Yeah, that doesn't work.

Excuse me? My control M is already gone. Huh.

But I haven't... Okay. What is this?

But I haven't... Okay. What is the difference between running a cell and running a cell in place? That if I run a cell with shift enter, the cursor goes to the next cell. If I run it in place, it executes, and the cursor stays here, and highlights the whole thing so that I can immediately type another command.

So it gives me kind of a, if you want to do a few quick things right there and not save them permanently, it's a way of kind of staying in place to get a few sort of console-like commands right there without building that up in the document. Right? Because sometimes you just want to check a few things that you don't really want to save, and that way you don't have to go back and delete those cells afterwards. We used to call that terminal list, but nobody knew what that meant.

Right now you have, you know, is there a quick, easy way to see the history of everything between those two commands besides just history? I guess, or does it... Like that? Yeah, I guess so. Or you can, yes, you can also do, so history, history with numbers.

The input, there is actually a variable called in, so if you want to see... No, because those numbers, this is something which is important. For those of you not used to normal type systems, this is an important kind of mental shift to make, which is that the numbers represent the order in time, in time, as measured by a cloth on the wall or on your wrist, the order in time in which code was executed. Whereas the layout on the page can be whatever you want it to be. You can move cells up or down.

So those numbers are there to remind you in what order did you run stuff. Right? Now, the notebook makes it very easy to restart a fresh kernel, basically kill the process that was running, and open a fresh one. And you obviously lose everything, but when you restart the kernel, now these numbers, which we believe in, have become meaningless.

But you can run the entire notebook in a single command. So if you want to basically make sure that the visual order and the temporal order match after you've been working all afternoon on a problem and you've moved stuff around, the safest thing to do is kill the kernel, do a run all, and then that will run the cells in order from top to bottom, and those numbers will be consecutive. It's an unavoidable kind of complexity, and all notebook systems have it, between the fact that you have a two-dimensional document and you have temporal execution, and those two orders may potentially be different. It takes a little bit to get used to, but that's why we never remove those numbers, because we want them to be there to remind you that this cell may have been actually run after this one, even though it's in the wrong place spatially.

Questions? Okay, so let's go to the quick tour of the notebook. So now, what I'm going to, and I think we're starting to run behind on time already, right?

So I'm going to go quickly. I'm going to toggle the header out and make this full screen so that we have as much space as possible. So some of these things we've already seen.

And here, the play button executes one cell at a time, and the stop button interrupts the kernel from a long-running computation. So, for example, here, this is another feature of Python which is true in the notebook as well, which is that if you have Python variables, when you execute system commands, we expand, if you use a dollar sign, we expand the value of the Python variables into the underlying shell command. That can come in very handy to combine logic between Python logic and system shell.

Now, obviously, all of you here at some point are going to have to plot data. How do you plot in the notebook? When you want to plot in IPython, you use the %PyLab magic, which activates plotting mode. And the most common way to do so in the notebook is by saying, PyLab inline, meaning I want my figures to show up here in line in the notebook. John, tomorrow, is going to talk extensively about Matplotlib, so I'm sure there will be some demos, and you saw also extensive demos of Matplotlib interactivity.

So, Matplotlib can also pop up floating windows. But in the notebook, if you do inline plotting, which is kind of the more common way to work, these plots are non-interactive, but they get saved as part of the document, and they can get exported to PDF and HTML and so on and so forth. So, once you've loaded PyLab, not only do we activate the plot support, but we also import all the non-PyLab and all the Matplotlib names for you.

So, typing something like that will make a plot. As I said before, if you copy and paste blocks straight from an interactive tutorial, you can leave the prompts in. We insert them for you.

So, that's copied from the online tutorial. When you run something, we try to report errors nicely. So, standard error is highlighted differently from standard output. It has a red background. I wish all terminal shells did that.

I don't know why they don't. Python errors are also shown as nice tracebacks with line numbers. One trick to know, which is very useful, Ctrl-M-L toggles line numbers for any given cell.

So, when you're debugging with a traceback on a long cell that has lots of numbers, it becomes very hard to see where it is. So, you may want to toggle line numbers on. We don't keep them on by default because they're kind of annoying in daily work, but they're useful to toggle on when you need to debug something. I already did that. If you run code that generates outputs asynchronously, we capture it in real time.

We've gone to great lengths to capture output from the kernel in real time, and not only at the very end of a process. If you blow up your kernel, so what I did there was using C type, I passed a null pointer to a system library, and that actually set fault in Python. Within a couple of seconds, Python will detect that and will say, should I restart the kernel? If you say yes, you get a fresh kernel. Obviously, the data is lost, but you haven't lost the document you were working on because those two things are separate.

These markdown cells, there's no time here for a markdown tutorial, but markdown cells can be pretty complicated. You can have arbitrary HTML, syntax-highlighted code, and all of it is correctly rendered when you come out of it. How did you do syntax highlighting? Or is it just the text that is Python? If the text is indented four spaces, markdown will indent it.

It's a good idea to do a quick brush up on markdown syntax in one of the online tutorials because it really is a handy format. What's your JavaScript in Python? Are you using page down? We're using page down and we're using pretty Python. Courtesy of Math Jacks, you can also come back to the question that somebody was asking.

If you use single dollar signs, that is inline math. If you use double dollar signs, that is displayed math. When you come out of it, you get a proper map that is rendered properly so that you can save documents with equations.

Now we're in a web browser. Anything a web browser can display, we pretty much can display. Now look at this. Here I have an object whose output, whose Python value is an image.

What we've done, and we'll cover this in more detail later, is we've defined the ability for objects to represent themselves in ways other than plain text. You can have a variable whose representation is an image or is anything that basically a browser can swallow. We have an image object whose representation is a visual image. It can take either local images or remote images. It can take SVG.

It can take PNGs. As we said, it's a browser. You can do YouTube.

We have an object called YouTube video whose representation is an embedded YouTube video frame so that you can put, this is a talk from one of the notebook talks that we did at UWashington last year, so you can imagine building interactive documents or teaching that contain text, math, explanatory videos, code, exercises, etc. Right within one document, and this stuff is safe, can be urgent control, etc. Local HTML5 video kind of, sort of works. This one only works so far in Chrome, and it took Chris Keys, I don't know what he did to encode this MP4 because when I tried to encode something similar, I got an error.

So, this is local video embedded. We're reading the raw video data and creating an HTML element which is a video element, and that gives an actual local video file. I'm sure this will get better as video support in browsers improves.

Right now, it's kind of quirky. You can have local files as well. So, this is a markdown cell that is using HTML to display local files. Using Safari and it worked fine. It did?

Okay, but I know that on Firefox, it didn't work for us, and I'm on a Linux box, so I don't have Safari to test with. So, okay, it's good to know that on Safari and on Chrome, it works. On Firefox, it doesn't.

So, it seems to be getting better. You can embed, as I said, anything a web browser can show. So, that's the actual Wikipedia mobile page for today.

So, if we search for SciPy in Wikipedia, that's the Wikipedia page for SciPy. Okay? So, you can embed pretty much anything that a web browser can show. About the security of local files?

Yes. If I do a cd command and I cd back out, is my file going to be able to see other files? It's just a Tornado plain file server, and the static directory is where the notebooks live.

So, it searched things in that tree, but it can't get out. Okay, so I can cd anywhere below me. Yeah. I can't cd out. No, you can actually cd the Python shell out, but you can't access via HTML files out, because the Tornado server will never walk back up.

Right. But you still can't cd, yes. No, Python doesn't sandbox you at all. It's a real shell. It's an honest-to-God, completely unrestricted system access.

Okay, so that can be a security issue. This is just an arbitrary shell. If you put that publicly without a password on it, then you basically put it at the same level as a bash prompt on the internet. That's why, by default, it only runs on localhost. And in order to run it on a public IP, you have to do that explicitly, you have to enable SSL, and you have to put a password on top.

Because, as Min just said, it's otherwise a shell on the internet. Sorry, yes? Yeah, I'm trying to get use case.

So, I put all this great stuff up there, but mainly only I can see it when I put it up. What is this for, really, in the end? Well, it is for us to do our research work, to collaborate with colleagues. If you put a password-protected notebook, you can...

So, how does the collaboration work? Do you have to go through those steps you mentioned? Yes, yes. If you put a password-protected server, multiple people can log in at the same time and actually work sort of like Google Docs, but with a brain, with execution, not just with editing. It doesn't do real-time synchronization.

You have to do that manually, and multiple people can't yet. Yes, yet. We will have that.

So, in theory, we didn't have to all be using our own versions on our own computers here. We could all be plugged into you. Yes, yes. Doing this.

So, you would all be sharing my session. We will eventually add proper multi-user support so that there's a notion of users, but that hasn't been, that has not been done yet. Okay. But, you can also export these documents statically as HTML or PDF to share with the world.

Okay. Questions? Okay.

So, we have mathematics support. So, one of the most useful things that we have is, many of you have probably seen the Matplotlib gallery, which is a long list, a long list of Matplotlib examples that you can, of thumbnails that you can go, and if you're looking for something that, if you're trying to create a plot, you can kind of browse around here and say, oh, that looks vaguely like what I'm after. So, you click on it, you read, you can copy and paste. We actually make that process a lot easier.

We have a magic called load. Those of you on OO12, it's actually called LoadPy, and if you give it a URL, it will actually fetch that code, put it in the next cell for you, so that you can hit shift enter and run it right there, and start playing with it. So, it makes it very easy, and load can take both remote URLs and local files, and it just slurps them into the next cell. Do you have any way to split the window? Like, let's say, so, for example, in this, the code runs off the screen.

I can't actually see the top of the code, the checkerboard. Is there a way? No. No, not currently.

So, before, we were doing math in the markdown area. We were typing math, but the notion of extended representations of objects, means that you can also have objects, whose representation is mathematics. So, we have a math object, and we have a latex object.

So, these are objects, whose representation is rendered math, and this is put to great use, by integrating with the SymPy library, where if you load a special extension that we provide, called SymPy printing, then we automatically hook into SymPy, so that all results that SymPy produces, are nicely rendered as math. So, now, I'm making SymPy calls, e to the i, e to the i x, with x substituted as pi, and then floating point, that's e to the minus i pi minus 1, e to the i square root of 163, 50 decimal points, but all of these things, are actually being rendered nicely, as latex, if I expand an algebraic expression, if I simplify it, etc., etc. Limits, power series, simple integrals, simple differential equations, and things nicely, are nicely represented, with proper mathematical notation, we have a little, I'm not going to go in detail through this, but we have a little example, combining SymPy and NumPy, to plot Taylor series, where you can compute things symbolically, and then do numerical plotting, and so, with Python, and these tools, now you can have a fairly high-powered, mathematical computing environment, including symbolic, work all of it in the same Python syntax, not with a funny, three-headed, three-headed Hydra, that Matlab gives you, where you have to use the mutepad kernel, bolted on the side, of the Matlab language. I had a little exercise, for you guys to do here, at the end, but in the interest of time, I think we should cut that short, right? Or do you want to give them a...

Okay. Okay, so, why don't you guys try to take, a couple of, well, it's kind of a very, mathematical, quirky exercise, and so I think, the time will be better, you answering other questions, since I know that I slipped, a little bit. Are you next, or? Ah, the cellmatics.

Right? Can I quickly ask, how your equations look so much better, than say, with computing? Mathjax. Mathjax.

Yes, Mathjax. Google Mathjax, the American Mathematical, the AMS, and the AIP, the American Mathematical Society, and the American Institute of Physics, paid people, to develop a proper, decent, honest-to-god, computer, in JavaScript, with the proper, computer modern fonts. It took years, for this to come out. The previous iteration of it, was not as good, it was called JSMath, and Mathjax, is absolutely awesome. It's also way big, Mathjax itself, is way bigger, than Python, than IPython.

Yeah, this was a huge undertaking. So, we actually have a note, in our, right now, you're pulling it online, if you want to work, with Mathjax, say on plane, without, or somewhere we don't, you don't have an internet connection, now you can install it, locally, copy it, locally, so that it's cached, and you can, it will run it, off the internal call. If you don't have it, and you open a notebook, with Mathjax, you'll get an error warning, but you can still use the notebook, just won't render the math.

Okay. This Mathjax, is a beautiful project, and it lets you write, a lot of math, and L, which is, godforsaken abomination. Thank you so much. And the other thing, is that, you can, you can, you can, you can, and I don't know if you mentioned it, but Mathjax will also render, as math ML, what Wikipedia uses, so you can write your, equations and facts, in notebooks, or within Python, and then copy the math ML, and paste it, to update it with PDR. I didn't know that.

Yes. So, if I'm playing around, in this and I've got, all these cells, and I'm interactively, doing this, is there a way, to do that? I don't know. I don't know. I don't know.

I don't know. I don't know. I don't know. I don't know. I don't know.

I don't know. I don't know. I don't know. I don't know. I don't know.

I don't know. I don't know. I don't know. Do I? I don't know.

I don't know. I don't know. I don't know. I don't know. I don't know.

I don't know. I don't know. I don't know. I don't know. I don't know.

I don't know. Yeah? Question, I think you answered it, correct. I don't know. I don't know.

I don't know. I don't know. You don't have the conversion code to do that separately quite ready, but if you start, and right now it's a little funky because, oh no, no, two things, I'm sorry, never mind.

Yes, file, download as, py, there you go. Or if you start the notebook server and you pass it the dash dash script option at the beginning, then automatically every time the IPINB is saved, a py will get written next to it. It will always say, automatically you will have the same, the py that goes with the IPINB and the py only has the inputs. What was the option again? Dash dash?

Script. Script. Or manually you can do it once by downloading it here. I'm wondering if it's not the mat-x-cdn. Blank?

Yeah. It may take a while, and if it doesn't in a few minutes, then we may be hitting, we were hoping that the network would be okay with multiple people hitting the CDN, the mat-x distribution, content distribution network. In that case, sorry, I don't want to mess with doing the local install right now because all those things cost time, so if that's the case, please just watch me. Most likely, if you do it at different points in time, the multiple hits to the CDN won't matter as much. Is that it, Min?

Okay. In the interest of time, I'm going to start kind of walking you guys through this, and if it pops up for someone, let me know, because then it will mean it's the CDN. That's my suspicion, that it's pulling data off the mat-x-cdn, but it could be wrong. Sorry about that.

This is the art of live demos. Something always goes wrong. So, the notion, so cell magics, let me also put this, remove the header, and we'll screen this guy.

So, the cell magics, I said we would hold off on them before, because they really make the most sense in the notebook. This is the LS magic that you guys saw before, and at the bottom it said there are these available cell magics that are compended with two percents. So, cell magics are magic commands that apply to the whole cell. They actually can be used in the terminal. You can basically type double percent and start typing stuff, and the first time you type two blank lines, that signals end of cell in the terminal.

But they sort of, they shine, really, in the notebook. This is a recent extension to IPython that actually opens the door to a lot of interesting things. So, I'm really bummed out that it isn't loading for you guys. But... It's just in the JavaScript, the first cell which calls things that are not garbage.

Oh, it's your secret Java. Oh, I left that in there. Shoot. We left that in there. I'll just...

What's that? I'm sorry. We were testing something yesterday, and I forgot. I was meaning to delete that, and I forgot to delete it. Oh, sorry.

Is it a quick Vim operation? Excuse me? Is it a quick text editing operation? It'll just be the first cell, and just delete it.

Basically, if you click up here, you'll see there's kind of an empty cell. Delete that with the scissors. Save, and reload. And that should do it. It may not be able to do it.

That's true. It's wedged. Let me see if I can do it. Sorry about that. We were doing an experiment yesterday at midnight, and I forgot that it ended up saved in here.

I didn't mean to create this. What it does is it gives me a slideshow mode. It gives me this mode. It's something that Matias wrote, which is kind of neat, to demo notebooks in slideshow mode. Matias did it last night, but obviously we weren't.

We were not trying to force upon you guys code from midnight last night. This really was an accident. So how do the cell magics work?

So the cell magics work. Let me make sure that I have my pilot support. Just like the line magics apply to the rest of the line they take, cell magics are commands that apply not only to the rest of their line, but also to the body of the cell.

So with timeit, for example, if you wanted to know how much is done by day to compute the eigenvalues of a 100x100 matrix, this would be one way to do it. But you're timing everything, the creation of a random matrix and the eigenvalue. Now let's create a variable separately. With cell magic, you can say make this as part of the setup code, which is executed only once and not timed, and then the cell is the stuff below it, and that's what I want timed.

So now you will only be timing the eigenvalue computation and not the setup code. So cell magics are magic commands that apply to the entire body of the cell. And the underlying API is that line magic gets as its argument the text on that line, and it can do whatever it wants with that text. You just write functions that parse it and implement whatever functionality you want. Cell magics get two arguments.

They get the line and the body of the cell, and they can do whatever they want with both of those, which means they can execute it, they can print it, they can call something else with it, and we're going to see all kinds of crazy things that we do with it. So if you just check on the GitHub, the ipython slash ipython intent, the cell magics is now missing the inappropriate cell. Can you just download it again and drop it in there? You can either git pull if you cloned, or you can redownload manually. Sorry about that again.

Apologies. No, my fault. I was the one who committed that mistake.

So what did you say? The time int in a cell will do the last line only? No, time int in a cell will do the whole body. Will do the whole body of the cell, but the first line will not be timed.

So you can put setup code in there, because that's actually how the time int module works. The time int module has the notion of setup code and timed code. So with the cell magic, we can expose both. Whereas with the line magic, there's no easy way of exposing both.

So if you do percent percent, that first line doesn't get timed? No, percent percent declares that cell as a cell magic. And what we do is we call under the hood, we call the function that implements that, and we give that function the line and the cell.

And then that function can do whatever it wants. Now, how would you find out how time int works? Question mark. Two question marks, and you can see the code.

This is how time int works. This is the source code for time int. It's not completely trivial, but you can see it right there.

So whenever you want to learn something in IPython about the internals of some stuff, put a question mark or put two question marks. One gives you basic data, two gives you more in-depth information. So there's a capture magic. If you say capture, and you give it a variable name, it will capture all output from that cell into the variable that you just named.

In this case, cat. And that variable has a standard out and a standard error attribute, and it has a show method that will print both of them. If you don't give it a name, then it simply captures and suppresses all standard out and standard error.

So if for some reason you're going to be calling code that is extremely verbose and you don't want to see it, you can put capture at the top, and then it basically silences it. Or you can capture for reuse. There's a file magic. The file magic simply saves the contents of the cell to a file with that name.

So if I say file foo, it writes that. And now I can run that file with %run. Why is this useful?

Because if you're working only through the notebook into a remote server where you don't have SSH access, you have no way of editing files. So this is kind of a poor man's way of editing files. You put %file, you put your code in there, and you dump things in. You can have a notebook, which is a bunch of file cells, and you dump them into the file system, and then you run the notebook with them as data.

So we don't have a full-blown IDE, but we kind of work around the problem. And it overwrites, and it will tell you if it overwrote the file. So now comes the stuff that starts to get really interesting. The script magic will run the underlying code under some other interpreter.

So you can say script Python and run that code, and it will call the Python interpreter and execute that code. But you can say script Python 3, and it will call Python 3 if that exists on your system. And using the script magic, we created default magics for common interpreters, such as Ruby.

So if you have Ruby on your system, if you type %Ruby and you put code there, that block gets executed by calling Ruby. You can put bash code. So if you want to call bash script, you can just paste straight-up a bash script into a cell, put %bash, and it will be executed by bash on your system.

So are those built-in to Python here, or are they actually calling out to what you have defined as bash on the system? Yes, the latter. Script foo will try to find foo on your system and call it.

Yes, yes. So now this one I do want you guys to do a little exercise. Write out of cell here, so right here, out of cell above this.

So this inserts a cell above. And then here, write a file called lnum.py, such that when you write script lnum.py, it reprints the contents of the script, numbering the lines, and prints n when it's done. So this, I'm going to give you five minutes. If you don't all get it, it doesn't matter. Whatever comes in as a script is something that takes input on standard n.

That's how scripts work. They take input on standard n. So your job, and hint, don't forget about the executable bit, is to write a script called lnum.py. And you can do this from within the notebook. We're going to see this in two minutes, so I'm going to give you five minutes to try to think about it.

See if you can figure out how to create a script that can be used with the script magic to execute and to number the lines of any block that it's given. So I'm going to wait five minutes. Think about it. Give it a try. And in five minutes, we'll post the solution.

This is what you have to do. Double percent file lnum.py. You make it a Python script. I mean, that's one way to do it, because it was a py. You could do this in Bash or anything else.

And you simply read all input, and you enumerate the back printing, and you put a print at the end. So if you do this, now you've written lnum.py. But as you saw already, if you execute it right away... Oh, I had already changed the main executable. If you haven't done the executable, you'll have to do this first.

And then when you run it, it will execute. And here, what it does is it simply numbers whatever it's in. So this shows you how you can put this system to very good use in creative ways.

But now we're going to see things that are actually a little bit more interesting. You can automatically capture output, especially from shell scripts. It's very useful.

So when you run scripts, you can say, I want to capture out into the output variable and center error into the error variable. And so if you run this, then there is no output right there. Instead, that output is captured into Python variables, which can be handy if you want to run shell scripts and then use their output to do post-processing without having to write complicated sub-process module code. You can simply say, output of bash-output to the stereo code, and you're done. You can even run scripts in the background with the dash-dash-pg flag.

That will run things in the background, and instead it will capture the output into a pipe object. So now if you want to read its contents, you simply have to call the read method on it. And it becomes available as the pipe is written to.

So you saw there was a delay in there. There was a sleep one, so not all output was available immediately. So the system is fairly flexible, as always.

Question mark will give you the details. Now on to even more interesting things. So depending on which version of EPD you have installed, you may or may not have Cython available.

So I'm not sure. So some of what follows may not work for all of you, and I didn't want to make everyone try to install Octane R, R, Py, Cython, all of that. So if the following doesn't work for you, just watch that it is possible, and we can look at helping you install these tools later on.

So who here in the room has never heard what Cython is? Okay, a few of you. So Cython, located at Cython.org. Cython is a Python-like language, derived basically from Python, to make it much easier to write extension modules.

So Cython is basically a set of syntactic extensions to the Python syntax that allow the Cython system to automatically generate C code that is compiled by GCC, and because you can have type declaration, you can bypass a lot of the overhead of the Python interpreter and optimize code to run much faster than by default. But normally writing Cython requires that you create separate Cython files, and you put stuff in modules, and you compile it in special ways. We've tried to make that very easy.

We've supplied an extension called Cython Magic, and if you load it with a low-dxt magic, now you can put %cython__piximport, and you give it a module name, and it will automatically create a module with whatever code you put below, call foo, and import everything from it. So if I do this, that code actually has been compiled. Good.

So now it's taking a bit of time because it had to compile. It had to call GCC. My hard disk is spinning. Thanks for catching that. I had a foo.py in there, so it was picking up foo.

So we can deduce that it doesn't overwrite a file if it's already there? Yes, I think that's the case. I say I think because this particular magic, I don't really use it all that much. The plain Cython one is a lot nicer. The plain Cython one does all of the compilation in a hidden cache directory with md5 names for the source code, and simply imports everything from it.

So it lets you put arbitrary Cython code right in there, and then it will compile it for you. If you change the source code, it automatically compiles and reloads. It caches it with an md5 hash of the source, and it does all the import for you.

So in this case, this is the kind of thing that is possible to do in Cython. You can define, and this is not a Cython tutorial, so we don't have time to go into detail, but I'm showing you that you can do things like saying, this is a C function that takes a double and returns a double, and doesn't need to hold the global interpreter lock. This thing is going to run like a bat out of hell compared to a normal Python function. And this is an implementation of Black Scholes model for options pricing that's using this function in C.

So in this loop, there isn't going to be, in this block, the gil isn't going to be held. If you run this in parallel in a thread, it won't be holding the gil, and all you have to do is hit Shift-Enter, let Cython compile it, and call it. And if you time it, it will time it just like anything else, and we could have a comparison in Python, and it would run probably somewhere between 10 and 100 times slower.

But this not being a Cython tutorial, I don't want to dwell on it. The point is that it makes it very easy to use Cython. You can link the libraries, so if you need to link to the math library, you can say "-ln", like you would with GCC. You can pass include pass. By default, the math library is linked, so in reality, "-ln'' isn't necessary.

But if you have some other library, I don't know, GSL or whatever, you can pass "-ln", like you would to a compiler, and it will call the linker at that stage. So this is actually calling the sign function from the system C library and not from the Python library. So this makes it very easy to basically sprinkle Cython into your workflow as you need it.

We also have one to do the same thing with R. For those of you who are heavy into statistical data analysis, you know that R has a number of things that Python doesn't have. And it has some very useful libraries for data analysis. Jonathan Taylor from the stats department at Stanford developed and contributed for the 0.13 release the RMagic extension.

So this is not an 0.12. And what the RMagic does is it lets you call R from within Python. So imagine that you have two arrays. You have a data set that looks like this, and you want to do a linear fit on it. Of course, there are tools to do that in Python.

Right now, there's a stats model tutorial going on that has tools in Python for that. But let's suppose that you want to use R. Well, so you have X and Y arrays of Python data that you want to analyze with R. You can say R push XY, and that will push X and Y to the R interpreter.

And then you can call in R the LN, the linear model function with Y. Just do a simple linear fit of Y with X as a query and print the coefficients. And that will come back as a NumPy array.

So this went out, passed the inputs to R, called the R code, got the output, and gave it back to you as a Python variable. You can pass whatever is the last statement of the R line. With a single percent, it's just a line magic.

So just whatever code you put in that line will get returned as an output. Because line magics can be anywhere in there, you can mix and match. Basically call some code in R, pull it, and then print it in Python.

But more interestingly, you can actually call R plotting. So in this case, this is an R line that actually called a plot and printed it. the summing statistics of that linear fit. So this is printing from R, and this is the R plotting output. And the same extension will load a cell-level magic for R, which allows you to pass inputs, and to say, I want these things as outputs when you're finished.

So what this will do is, it will execute this entire block under R, giving it whatever x and y were in Python as R variables, and grabbing back for Python xy coef when it's finished. And this has a plot, so it does kind of nice. It executes everything, and gives you a plot.

So you have access to all of the fancy R machinery. Identically, and I'm going to go through this one really quickly, with the exact same kind of mental model of the R one, we have an octave one. So if you have MATLAB scripts that are compatible enough to... I have no idea what happened there. Some bizarre interaction between all the things that I've been doing.

So now you can do the same thing. You can call octave, pass it variables around. You can push that into octave, grab outputs from octave. You can call the octave plotting. You can call arbitrary octave code that includes plots, and it will execute.

It will capture output and bring the octave plots. And octave does have some very useful stuff. So their filter design stuff is pretty good. They do have 3D plotting. MATLAB has 3D plotting too.

The point is now, within one environment, we've been using Python, Bash, Ruby, Perl, Cython, Python 2 and Python 3, R, Octave. All of it is staying within one single system. And the cell magic system is completely extensible. Our documentation explains how you can declare your own cell magic and define your own.

So all of this put together gives you access within one single environment to quite a bit of computational power. As I said, by defining your own, you can access your own code in a similar way. We haven't written a double percent Fortran one yet, but it's really easy to write one with F2Py and just run out of time over the release.

So you could put Fortran blocks and have them automatically compile with F2Py. We just didn't get to that. Are there any questions on this? With the percent being out in the middle of the statement, doesn't that get distinguished from doing the modular?

Because it's only valid for assignment. We special case the syntax equals percent, which is not valid Python. So we special case basically calling a magic and assigning its output to a variable. Our parser special cases that. And because that is completely invalid, Python syntax is not valid.

That's all you need to say. Variable equals percent whatever. It's the only thing you can do.

Yes, question over here. Yes. The interaction between Python and R and the object that you just showed can only be done in the notebook in this interactive environment, or you can have... No, no. That's a very good question.

So that actually, I was going to finish here, but that reminds me that there's one more thing I want to show you guys. The whole business about this QT console that we talked about, let me open it up. So this is, what I did was I opened the QT console and look at my prompt number, 10. That prompt number is, if I do up arrow, I get this. If I do up arrow again, I get that.

This is a QT console which is talking to the same kernel as the notebook is talking to. You can open, because the architecture is simply, there's a kernel, it speaks a protocol, and any number of clients can connect to it. So you can hook a QT console or a text console to it, and these calls work there as well.

Now, the plots won't work in a text console, but I think this will work. Let's see. There you go. And in a text console, they also work.

Yes, sir, question. So then presumably all the local variables are common? No, only the ones that you explicitly pass in the I and O flags.

These are two separate namespaces. These are separate processes. The R magic rules have to instantiate the R process separately. It will only pass back and forth variables that we explicitly wrote in the test. And by the way, the R extension depends on the rpy2 library, which, to my knowledge, does not run on Windows.

So the R stuff simply doesn't work on Windows, but that's because the library in the handout simply does not exist, does not operate on Windows. Question. Does the QT console have interactive plots or not? Flowing window plots? No, like...

To be able to drag and move the plots. Yeah, rotating something in 3D. Non-embedded. If you open a flowing map of the windows, they are interactive in the sense that they're their own windows. If you put them inline, they're static windows.

Is it the same as before? If you do pylab without the inline flag, you get flowing windows. Can you disable the floating windows from the test? Toggle? Sorry, can you toggle the inline?

Toggle. We've had code kind of do that, but it has been rotted. I'm trying to convince Ryan May in the next couple of days, one of the Mac OS developers, to kind of pick it back up and finish it.

So I'm not trying to put you on the spot or anything, Ryan. This is your quality of life. No, exactly. It's not hard, and it's a really, really often requested feature, and I have the code. John Hunter and I wrote that code in India a year and a half ago, but we never finished it, and it's just been rotted, and it's just a matter of sitting down for an hour and not really even finishing it up.

You'll have to talk about it. Right. No pressure, Ryan.

So this shows you how the architecture, we sort of think of the notebook as the tip of the spear, because it's a fairly attractive thing. It's extremely useful. It's fantastic. A lot of people are excited about it, but the body of the spear is more of a battering ram. It's the entire architecture of how you can apply it, and you begin seeing that when you realize that, oh, I can hook up a Kinect console to the same thing, and the history is the same, and all of those things come for free.

They simply come because of the fact that the architecture was designed to have clients that are talking over the same protocol to the exact same server, accessing the same service. Okay? Any other questions right now?

Okay, so the last notebook that we're going to see is the one called display control. So here, we're going to go into a little bit more detail into how is it that we made those things where the display could be an image, where the display could be a Python, could be an SVG figure or a PNG figure. So let me execute this.

So the way our display machinery works is, there are two ways to use it. One is you can define custom classes that have special methods called underscore, wrapper, underscore, something, underscore, meaning wrapper PNG, wrapper SVG, wrapper HTML, wrapper Locket. We support all those. The list is... we have them here to do what it is.

So let me show you quickly an example of how this works. I'm making a Gaussian object, which is simply a Gaussian distribution from NumPy. It samples a Gaussian distribution with a given mean and variance and a number of items, but it has a PNG representation, and it has an SVG representation, and it has a histogram property, which represents itself as the histogram plot, okay? And it has a Locket representation.

So all I've done is I do the computation, I store these things, and then if I define a wrapper PNG that returns the PNG data, that's enough for IPython to pick it up and render it as a PNG. If I define a wrapper SVG that computes the SVG data using matplotlib, then that's enough for IPython to pick it up. If I return... define a wrapper Locket that simply returns the proper Locket string for that Gaussian, then that's enough.

And what I've done is I've... we have... all of these representations come back to you when you execute one of these out, and then we made properties that are PNG, SVG, Locket to access each of these, and as I said, a histogram. So when we execute this, if I define X as a Gaussian and I simply view it, this is what comes back out. The highest priority one is Locket.

So simply because it had a Locket representation, IPython will grab it and see it. But let me show you something. Let me open a QT console against this kernel, and let me look at X in here. The QT console doesn't know how to render math, because MathJax doesn't work here.

This is not an HTML browser. This is a QT text browser. So it says, I got the representation. The fanciest one I know how to do, how to represent, is the PNG one.

So it defaults to that one. If we did this with a text console, it would just show the text representation. So you don't get an error. We return a dictionary with all the representations that are available, and each client does the best it can. Okay?

Is this how your dictionaries and your lists and all that look nice, as compared to if I just did a print of it in Python? No. For the basic stuff, it's just because we load it from the standard library, the pretty module, which is built into the standard library. It's called pretty, and it's a pretty printer. And by default, we print using pretty.

It's a completely different mechanism. Yes. It's just because we by default put pretty on everything. You can turn that off with percent pretty, if you want to see plain, normal Python stuff.

This is new, and a separate, dedicated mechanism. So now we have these attributes, so if you want to see the PNG, you can see the PNG. If you want to see the SVG, you can do that. If you want to display, so this shows you the SVG. If you make a second Gaussian with different parameters, now you can display both histograms and see them next to each other.

So you see how you can basically add very rich displays to your own objects. Okay? Now this requires defining custom wrapper methods. How are we doing on time to have an exercise? Should we skip it?

This is... So now, you guys are going to do an exercise, which is, I just showed you, I just gave you an example that has wrapper PNG, wrapper logic, wrapper SVG, lots of fancy stuff. What I want you to do is write a little class right here, whose representation is simply italics HTML. That's it. And as a hint, I should have put a hint in here.

So, hmm, why wasn't it... What's that? There? Ah.

So this is how you, italics in HTML are just between I and angle right. So write a subclass of the built-in string, such that whenever you print it, if you define a string, hello, and it's A, if you hit A, instead of seeing hello, you see hello, you see hello, you see hello, you see hello, you see hello, you see hello, you see hello, you see hello, instead of seeing hello, you will see HTML, italicized hello. All you have, it's a one-liner, and that's, all you have to do is define a method using these special representations.

So here, we did wrapper, wrapper SVG, wrapper PNG, wrapper LaTeX, all you have to do is define wrapper HTML with that syntax, wrapper HTML underscore. So, all you have to do is subclass the built-in Python string, and make it so that it always shows up when you print it. And that's it.

So, subclass the built-in Python string, and make it so that it always shows up as italicized HTML. For example, pandas, for those of you who saw the tutorial, has put this to great use by making pandas data frames show up as nice HTML tables in the node. So, give it a couple minutes, give it a try, and we'll look at a solution in a short question. And we're coming to a break, obviously, I know we've been going pretty much nonstop for almost two hours. I know you guys are tired, so we are going to take a short break.

Coffee, etc. We're coming to the end of this. But this is a short exercise, I'm going to give you guys five minutes. What's that? Yeah, of course.

Do we have autocall? Percent autocall is a flag that toggles between how aggressive the autocall maintenance is. We may have disabled writing quality. I have it on, and you can configure it to be always on if you want. If you type autocall question mark, you'll see the various behaviors it has.

Because of this notion that you can connect a text console, a QT console, or a notebook to the same kernel, the kernel doesn't have a notion of cells. It just has a notion of blocks of code that were executed in time, one after the other. It doesn't know about the state of things. Yeah, we don't have that. That would be a logic that would have to be wired in JavaScript.

Yeah, that's absolutely true. So, version control, we put a fair amount of effort into making the JSON format very version-controlled. So, it says that the keys are sorted. And you can always say, all output clear, and that will delete all output, and it will delete all input prompts as well. Excuse me?

Yes, run all. Run all. No, expand is for expanding long blocks of output. Clear will delete all output, so that if you want to save only the input, which is basically what really changes with version control, if you clear all before saving, then no prompt numbers will be saved, and no output will be saved.

So, it's only the code. And it's basically as diff-friendly as possible. And we break multi-line blocks of code into single lines in the JSON, so that the diffs are a little bit more human-friendly. And do you have any version of interacting with the Wiki system? No.

Some people have been looking into it. There's a fellow who's been doing a lot from CERN, Baltimore Calret, who's been starting to play with Wiki ideas. He's on the dead man list.

So, I'd encourage you to kind of pop your head in there and see what happens on that front. I honestly haven't thought about that particular point yet. And we're trying to leave kind of a slush 20 minutes at the end for sort of open questions and other ideas. Has anyone gotten it to work?

Okay, we have a few winners. Fine, you don't count. So, let me show you guys the solution. That's what will happen.

So, it will show both, and they have different background colors. So, the first one has a green background, because it has been executed, so it knows it's in the kernel namespace. The one that has a bluish background, it's saying, I found this in the local text area. It's not a variable that exists.

So, as I said, there's two ways to do this. One way is what we just did, which is to define special methods, which is great if you're creating new objects. But sometimes, you might want to add the nice notebook behavior to code that someone else wrote, where you're not going to go modifying their library. It's a third-party library.

So, thanks to Robert Kern from mThought, we have a system that allows us to register these special representation methods against existing objects. So, that simply IPython will say, when that object shows up, I will represent it with this thing, without having to change the code for that object. So, let me illustrate that quickly with the NumPy polynomials.

So, this is what a NumPy polynomial object looks like. The point right now is not to go into the details of NumPy. This is just how you make a polynomial in NumPy, and it's just that text. That's how NumPy, by default, will show polynomials. But, you could imagine wanting a nicer representation of that.

So, let's imagine that we write a function called polyLatex that will go and check the size and generate the code for it. It doesn't matter a whole lot. The point is, there's a function that nicely produces, on a given polynomial, a correct Latex string.

So, I've written the code to, given a NumPy polynomial, produce a nice Latex string that will be valid Latex. So, if we call that string as a Latex object, with our display Latex object, that will be rendered. By default, it's a string, but if we call it with a Latex object, it will be rendered.

So, now we have a function that, given a NumPy polynomial, knows how to compute a nice Latex representation and show it. But, how do we make that happen automatically, so that all of my polynomials show up that way? This is how you do it. It's a little convoluted, but there's a method to the madness. You grab the main IPython object.

There's always a getIPython function defined in your namespace. And you register a Latex formatter, which is for type TextLatex. And then you say, this formatter should be used for this type by name. You give it the module, you give it the class, and you give it the function that you want to be called.

So, basically, what IPython does is, whenever it gets an object of this class that comes from this module, just to make sure that there are no classes, with something else, it will call this function to render it. And this is registered and activated internally. So once I've registered this, if I view P again, now P is always rendered in logic mode.

Yes, question? Are any of these registered by default? Excuse me? Are any of these registered by default? None are registered by default.

But for example, the SymPy printing extension, that's what it did. The SymPy printing extension did this trick to register against all SymPy types. And that way, the SymPy results automatically show up in logic mode. Is there any talk about clustering a bunch of these together and having one easy way to just like some set for a bunch of numpy? Yeah, it would be very easy to write an extension that has all of these.

And these low-dxt commands can be put in your startup file. So you could load them automatically in your profile any time. We haven't done that, but that can be your next contribution to iFive.

So now that we've registered this, it will be true for all. All knowing that because it has been registered, it's active from now on. And finally, one very short but useful thing related to the display system, which is that we also have a special command, which is we inject into your namespace, which is called clear output, that allows you to flush the output area, to delete it in the notebook. And that's useful if you want to do sort of animation-like stuff within the notebook.

For example, here's something that writes in place numbers. It calls clear output and rewrites in a number each time, rather than printing the numbers, letting them scroll down. So you can do things like simple animations. It's not perfect. It flickers a little bit, but it's reasonably serviceable to do in-place updates of things.

And using that, for example, you can actually call JavaScript, if you want, and then put a nice animated JavaScript progress bar, for example. Because remember, just like we can represent HTML, you can return JavaScript. If the browser can show it, we can show it. And clear output lets you flush the output area to continue working in place. I think this is what we have in terms of the general introduction to the notebooks.

And now, we're going to switch gears to the advanced parallel machinery, which is also based on the notebook. But I think it's time for a quick break, right? So let's take 10 minutes. Should we take 10? Be back on 15 at 10.