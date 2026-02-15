---
title: "Interactive Parallel Computing with IPython"
summary: "Tutorial at SciPy 2014"
date: 2014-07-09T00:00:00
tags: ["tutorial", "transcript"]
slug: 2014-07-09-scipy-2014-tutorial
word_count: 9642
source_file: transcripts/2014-07-09-scipy-2014-tutorial.md
content_type: transcript
event: "SciPy 2014"
video_url: "https://www.youtube.com/watch?v=y4hgalfhc1Y"
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

I think we can get started if people are finishing their lunches, a few of them. So I don't know if anybody's supposed to tell me to start if I just go. I'm going to assume I just go. All right, I have been told to go.

All right, so I'm Min Reagan Kelly. I'm a core dev on IPython. I've been working on IPython for a long time. One of my main contributions in IPython is IPython's interactive parallel computing facilities. And so I'm going to give a tutorial on how to use IPython for some interactive parallel computing, which IPython has a slightly different model from most parallel computing tools since it has this emphasis on interactivity. So there will be some interesting things.

And to help me out in here, we've got one over here and some IPython-associated people like Fernando and John and Kyle in the back. So I don't know if Aaron Amadia is... He's getting Post-its. So when Aaron brings you a Post-it note, you can put that on your laptop and that will tell these folks that you need a hand so you don't have to sit there with your hand in the air. Yeah, and there's the SciPy Etherpad for... The people will be lurking there if you want to ask questions.

All right. So getting started, this tutorial will be from this repository on GitHub. It's IPython Notebooks, as one might expect from a tutorial about IPython. So just clone that repo and you should be just about good to go.

And the dependencies are the basic dependencies of IPython. We'll just do some basic plotting. So numpy, scipy, matplotlib. There will be some demonstration with MPI and scikit-image, but you don't necessarily need to be... If you have trouble installing those, then you should be able to follow along without executing through everything. If you have Anaconda or Canopy, that's everything you need except probably MPI. If you use Anaconda, you can just install MPI for Py and it will almost work depending on what machine you're on. There's some help on that in the Etherpad. And if you prefer pip, there's a list that doesn't render right, so I'll just make it literal. Just a few simple packages that I'll use. I'll use NetworkX for some graphing examples.

All right, so let me gauge the room a little bit. This is the advanced tutorial, so I'm going to assume everybody is familiar with IPython. Is that true? Yes? Raise your hand if you are familiar with IPython that way. All right, okay. And let's keep them up. How about if you've used the IPython notebook before, like this morning? Okay. And how about if you've used IPython Parallel before? All right, okay. More than usual.

Okay, so I'm going to give just a little bit of background. Everybody is familiar with IPython. I'm going to give a little bit of background on IPython from the perspective and how it works to kind of describe the motivation for why IPython Parallel exists and also the reasoning behind how it works.

So as everybody is very familiar with, at the most basic level, IPython is just Interactive Python. That's what the I stands for, and that's why you always capitalize it. But if it's all lowercase, that's fine. Don't capitalize the P and not the I. That's all we ask.

All right, so I've got basic interactivity. As I print things, they come out. I can run this C call that will segfault. So my kernel died, but the notebook noticed because the notebook is a different process. The kernel died. I've restarted it for you. So I'm all okay.

At the basic level, IPython is Interactive Python. At a second level, we've got tab completion. We've got introspection. We've got shortcuts for doing shell commands. You can assign things from shell commands. We've got magics that let you do some things that might be verbose in Python. Right in a kind of a shell style that can be a bit more convenient to type. That was an unreasonable item to choose.

We've also got some basic... This is just a simple thing that raises an error. We've got basic debugging facilities. So there's my debugger. Debugger, and there's a bunch of magics. That was debug. Percent debug. Percent debug opens an interactive debugger session. So if you don't exit out of the debug session, you will still be in the debug session. Yes, I think so. You can... Let's find out. Yep.

There is one thing you need to be careful with the debugger that you can lose the interactive element in the debugger, and then you won't be able to get back to the regular IPython session. Anyway. There's a bunch of magics. So IPython does lots of things, as many people have realized. It does usually more things that at least I know how to do.

And then the next level from a bit more than interactive Python is a bit more than plain terminal REPL. So, you know, I can plot. I can get figures. I can display LaTeX equations. I can do SymPy things. I can interact with SymPy things. I can display images. I can display YouTube videos. So at this level, you know, IPython is a bit more than just executing Python and text output. It can have rich output.

And once you've got this rich output and input, you can have these notebook documents, like I'm presenting with, which save my input and my output and can have math, code, LaTeX, markdown, you know, all kinds of stuff. So we can peek at a notebook. A notebook's just a JSON document. And we can do things with those notebooks, like convert them to HTML.

So I just ran the nbconvert command in IPython, which generated this HTML file, which looks very similar to the one you're using, but it's not interactive. This is just a static HTML file. You can see it's HTML instead of IPython.

So from a technical standpoint, we've talked about what kind of functional the IPython is, but from a technical standpoint, IPython really, at this point, is a protocol. It's a message protocol over WebSockets and 0MQ for doing remote execution. So when I hit Shift-Enter, the JavaScript builds a JSON message called an execute request and sends that to the notebook server. The notebook server relays that to the kernel where the code's executing. That executes some code, and then that builds messages, builds an execute reply that tells you whether an error was raised or whether it succeeded and what the prompt number is.

And display data can have side effects, like when you do plot commands and things. These are also messages that can have MIME-type keyed data that comes along as messages from the kernel.

And then a very simple example that belies how complex what's going on here. So I just did double percent JavaScript and then wrote some JavaScript code, and that JavaScript code executed some Python code. So what I just did was I sent a string from JavaScript to the Python kernel. The Python kernel interpreted that, and it found this JavaScript magic. So IPython found the magic to call a function, and that function took the rest of the cell as text, which is JavaScript, and then published that JavaScript as a display data message with the JavaScript MIME-type.

And then the JavaScript received that message, says, ah, this is JavaScript. I'm going to execute it. And then that executed, which called an IPython API in JavaScript, which then called execute, which executed an assignment in Python which sent another execute request back down to the kernel and executed it. And now I have this one, just to verify that I'm actually doing this.

So that's what IPython is at a technical standpoint. It's a message protocol. So we've got clients, and we've got kernels, and the protocol is publicly documented. It's probably the best part of our docs. Our docs, the rate of development of IPython has resulted in our docs somewhat suffering in terms of not keeping up with the changes in IPython APIs.

One of the things that we are relatively good at is maintaining this message spec document. So we've got a big document that describes all the network connections. You can have multiple front ends connected to one kernel. And then it describes all the messages in the specification, the wire protocol that's sent over 0MQ.

And the reason we have this is, as Brian and John talked about this morning, you can actually write a kernel. This REPL code is text, MIME type output. There's nothing Python about it. So you can write kernels in any language, and you can back the notebook by any language. At least any language that has 0MQ bindings, which at this point is about 40 languages.

So to summarize that, what's IPython? In general, what the goal of the project is is tools for interactive computing. You've got code, you want to run it, you want to interact with it, you want to introspect it, you want to tab complete, you want to debug, you want to save your sessions, share them, you want rich output, that kind of stuff. And it's implemented by a message protocol. So we've basically implemented remote execution.

And so how does this become IPython parallel? I'm going to start with a demo to motivate what you can do with IPython parallel, and then I'll go through how it actually works. So I don't necessarily expect you to follow along this one, but I'm just going to show you this in action.

So I just start a cluster. You won't have as many profiles as I do. Oh, and this notebook, there's a notebook in there that will download images from Wikimedia Commons. You can just run all in the images notebook. It will download images, and there's also a link to an image zip which is the result of me running that script if for some reason it doesn't behave.

So I load plotting, load basic scikit-images. So I write a function to find the contours in an image file with scikit-image. Plot those contours with matplotlib. This is just a function that given a... basically call both of those functions and return png data. This just gives me a list of picture files anywhere on your computer. If you've got pngs and jpegs, it'll work. Just any path to pictures.

So I just test my function. And it just draws red lines on the low boundary and then blue lines on the high boundary. So just little drawing lines around the bright parts and the dark parts.

So I do that in parallel. I connect to iFiles in parallel, create a couple of what are called views. And then I do some boilerplate to get my engines all set up. And then I just call this map function with my Python, with my git contours, the function I want to call. I want to call this on all my pictures.

And I'm just going to map async the function on the pictures and then iterate through the results and display it. So this is just doing the function I called and doing some random image analysis on a few pictures. I'm just doing the exact same thing, but I'm doing it remotely. So these are sending off the image file names and the function, evaluating the function remotely, and then asynchronously iterating through the results as they arrive to display the images.

And I'll just keep on going. I'll just keep on going for kind of a while. In fact, the performance limit of this function is matplotlib drawing the contours because there's a bunch of them. So I'm actually calling matplotlib remotely on the engines and generating just PNG data. These are not downloading. The downloading is done in a different notebook. There is a version of this notebook that makes the download part of the operation on the engines. You can do that simply enough, but not in this particular case.

All right, so that's kind of the gist of I can write a function, I can build some arguments that I want to call it with, and then I can test it remotely once I've got it, or test it locally once I've got it running. I just pass the function and the arguments I want to call it with, and then I can run it in parallel on.

Yeah. So I can talk about, there's a way around that. Python 3.4 broke something. So you can use dill. Dill is a tool that is based, it's pickle, but more. And IPython can, there's a function in IPython that's, you just use dill. It just says stop. So IPython adds a tiny bit to pickle to allow it to send functions. But it doesn't, we don't implement our own serialization. People call it pickle and dill have already done that. And so you just say, tell IPython to turn off its special handling and use dill instead, and then it'll just work. There are still, there still exist some things that dill can't pickle, but that set is much smaller than what IPython can. Yeah.

All right, let's stop that guy, get back to zero. All right. So now we're going to be talking about this in an overview of the IPython architecture.

So in regular IPython, you have a client, you have a front end, say the notebook, and then you have a kernel where code executes, and they communicate with messages. Once you have remote execution, it's actually not a great leap to have, okay, I've got one remote kernel, why don't I have three of them and just use them all together? And that's the kind of, the design principle of IPython parallel is taking the existing message spec that IPython already has for doing remote execution, and then just saying, all right, I've got n remote engines, let me, and then adding abstractions for how to deal with multiple remote namespaces in which to execute.

And the way this is accomplished is that rather than having clients connect directly to kernels, as in the notebook, you have an intermediary of a hub and four or five schedulers that collectively refer to as the controller. And these processes listen on a bunch of sockets, and then clients connect to the controller, and engines connect to the controller, and then clients essentially talk directly to engines, and then the messages are relayed via 0MQ in the schedulers.

So the client just says, all right, let me tell, I want to tell kernel 0 to, I want to send an execute request to kernel 0, I want to send, and then kernel 0 sends his reply back up.

And so the design principles are, we really want the parallel IPython is designed to be just like regular IPython, but in parallel. So it's a full IPython namespace, there's magics, there's everything, there's rich display. Everything you get from IPython, it's just, you have more than one of it.

And we don't want IPython to reinvent or compete with MPI. We want you to be able, with things like MPI and other parallel computing tools, we want you to just be able to, if you want to use MPI, you just use MPI. You can start the engines with MPI and use MPI broadcasts and everything and it will be exactly as fast as it would be without IPython because you're just using MPI. There's not abstraction layers or anything, it's just all we have is an event loop. That's all IPython is.

So the engine is just, so an IPython kernel normally listens for connections. So you start a kernel and it basically, it's like a server and then you can create multiple clients and execute code and get results and kill the clients and then bring up new clients and run new code. And the only difference between an engine and a kernel, it's the exact same code, the only difference between, the only thing the engine does is it connects instead of listens. And because of some of the magic of 0MQ, it doesn't actually matter. None of the code needs to change depending on your connection direction. This is one example of the reasons why we use here.

And then the different schedulers expose different execution models. So standard ways of running code or, you know, you want to do explicitly, all right, engine 0 do this, engine 1 do this, engine 3 do that. Or you can load balance like, I don't care where this happens, I just want it to happen at some point and assign it to idle engines when they're read. And IPython handles both of those by using different schedulers for the different patterns.

And the hub is basically just a big fat logger that, so the schedulers are actually pure C functions that are just an inner loop of, I got a message, forward it on, and then I got a message, send it back. And the hub, every message that the scheduler gets, it also forwards on a side channel to the hub. And the hub sees, all right, everything is happening. I see this person or this client requested this execution, save that in the database. This result came back, save that in the database.

And because of that, you can, after submitting a bunch of code, you can come back and say, hey hub, what was the result of this execution? Without keeping your client and waiting for the reply, you can say, I know I submitted this work. Is it done yet? How far has it gone? What was the result? And the hub, being this big database thing, is slow.

And the important thing is the fact that the hub is slow doesn't matter because the hub is not involved in execution at all. So the hub can be slowly pushing things to databases and things, and that actually doesn't interfere with execution because execution happens, the relaying of execution messages from the clients to the kernels is relayed purely through these schedulers, which are separate processes. They can be threads, but normally separate processes that have little to no logic.

And the way you use IPython is you create a client, and this is the low-level object that builds messages and handles replies and everything, and that has 0mq sockets to connect to the controller. And then once you have the client that's got all your connections set up, then you build views, and the views are really the APIs for different execution models.

So just to get started with the MapPython cluster, you start with this terminal command, ip cluster start, that starts a cluster, and then dash n, the default number will be the number of CPUs on your machine. You can specify any number that you want. This will spin up, this will start a controller, and then start an engine.

And you can also do this by visiting the clusters tab, and then just starting. And an IP cluster is basically a wrapper for starting processes. So an IPython cluster is just starting a script IP controller, and then n times starting a script IP engine.

And then the IP cluster wrapper script exposes some ways to start processes in a common environment. So it can start your engines with SGE, with PBS, with Torque, with Condor, with MPI, with SSH, with LSF. I think WinHPC still works. Probably. And you can actually write your own custom launchers that are in my special environment. This is how engines should start. And then you can just do IP cluster start, and it will start the engines in the appropriate way.

Yeah? Not any of it at all. Yeah, no, there are logical ideas. I have never used MATLAB. If anything, some of it is inspired by the multiprocessing library. So most of the API in IPython at the client level where you do advanced things is basically a superset of functionality on the async result object that is in multiprocessing.pool, and is really superseded by futures, but this was before futures. So I have in a branch whatever pep number it is, an async IO compatible version of async execution. Not MATLAB inspired.

So we've started a cluster. Who has started a cluster? All right. Who tried and failed to start a cluster? I'll let Aaron. You can help someone before you help John. All right. So we've got a couple. I think there's... So I'll keep on going.

So at the very basic level, once you've got the cluster going, you create a parallel client object, and a client is this object that wraps the connections to the cluster. And the client has IDs. These are the engine IDs of my engine. So I see I have four engines.

You can, in fact, add engines as a function of time if I can... So if I did... I just type, type the engine, and I've got another engine. So you can add engines, you can remove engines as a function of time. Sure. So they write connection files that are used for engines and clients to know what the port numbers and authentication keys and everything are for a cluster. And if you want multiple clusters on the same profile, then you need to add a cluster ID argument that just adds a suffix to the file so they don't collaborate with each other. But yeah, you can have 100 clusters on the same machine.

Yeah, so let's see if we can make any sense of this log output. Yeah, so it found my default profile, and then it loaded the connection file. And then it, from that connection file, figured out where the controller was, it sent a registration request, and then initialized the interactive Python, the IPython session, the kernel. And then at some time later, at some time 150 milliseconds later, the controller replied, hey, I know you're there. Now you're part of the cluster, and you're ready to go.

And those events, the client doesn't have to actively poll for cluster updates, it doesn't need to ask the hub what the structure of the cluster is. When engines register with the hub, the hub publishes a message to all clients, and says, hey, I just got a new engine. And so clients are always up to date with the current, so I can actually, let me, so I just started an engine, I interrupted it, and now I'm back down to four engines.

Yeah? I have a number of GPUs. I need like my, my process, to use each process. Is there any use case that you can provide to use it? You mean how to get IDs of GPUs, or, right, so each engine... Like, like, I have like four machines, each has four GPUs, and I, I, I would send, you know, a, a job to one of those processes, so I, I, I know that the process is two, and if it's three, you always need to be on one.

Yeah. Are you asking how do you, from Python, pin to a GPU? There was a, you know, it is, it's related to, I think, to ID, so I don't know.

Yeah, so, so the, the process is, so these, these IDs are just, this is just an integer counter, and then you can, I'll, in actually a couple of seconds, I'll show, I'll get some information about that process, and you can use that information to say whatever, whatever API you have for, pin this, this process to like, you know, OpenCL, set, select compute device, or whatever the API is, you just say what you would do is, from the client level, you say, give me all the machine, give me all the engines on this machine, and then give me all the available GPUs on that machine, and then say, this engine, execute whatever Python code that says, hook me up to GPU number one, hook me up to GPU number, number two, and then you can, so you can directly execute, you can execute code that queries the information, and then based on that information, you can coordinate, all right, this guy should get GPU one, this guy should get GPU two, this guy should get GPU three, and then you execute different code that says, all right, actually perform that association, whatever the appropriate API call is. Right.

So another important, yeah, another important feature of IPython parallel that is inherited from the, the fact that it's IPython, is that it's fundamental, the engines are fundamentally stateful. So if you, and I'll get to this in a second, if you execute code, A equals five, and the kind of code is text part of the API, if you execute A equals five, that's the same as if, if I had a notebook, and I just typed A equals five in an input cell, that A is available for the rest of the future until I, yeah, every engine is its own isolated process. So it's like having multiple notebooks. It's just all my notebooks are this Python client object.

So I've got each, each kernel is a separate process and can be on any machine. I will do a demo later with a remote cluster, probably. We'll, we're going to see some, some logic based on the host name of the, of, of the engine. And they're all, they're all just like, it's like you started a terminal IPython session and every engine is a separate IPython session. So if you do A equals five in this one, A equals ten in this one, this guy's got ten, this guy's got five.

Yep. One of the reason I, I was told that actually when you're, like, when you're launching the system, like, and one of the processes is not, when you're using the API, you're basically, you're releasing the system, like, and I was told that, actually, IPython, it's not a problem.

Well, it depends on the nature of your, IPython doesn't die. It's true that, hmm. So if you know how to recover, so this is kind of getting ahead of, ahead of myself, but yeah, there are various, an engine dying is just an event in the IPython structure. And so any tasks, any work that's currently happening on that engine will fail. So with a special exception, as far as your client is concerned, it looks like it'll raise, like, an engine died exception.

And the, depending on how you're using IPython, you can either have logic to handle that at the client level, you can just ignore it, depending on, right, there's a lot of different appropriate actions to take when an engine dies and the work it was doing is lost. One is to just safely ignore it. One is to try to do it somewhere else. One is to stop everything, nothing makes sense if that guy died. And IPython doesn't, IPython will do one of those for you, but the main thing it does is let you propagate the fact that that event happened to you and then provide you enough hooks that you can actually decide what action to take.

So in the load balance case, you can say, sometimes this thing dies because maybe it's, I've got code with, it's not thread safe and it just segfaults one in ten times or something. And you can say, when you submit things to the load balance scheduler, you can say, this thing might fail, or maybe there's some random number seeding, you get edge cases, and it might fail, but I don't, just, the right thing to do if it fails is just to try again. And so you can specify a number of retries to a task. The default is zero because the default of an exception is it's unrecoverable. But you can say, this might fail, if it fails, just do it again. And then, as far as the client is concerned, it'll look like it's still running, it just happened to switch where it's running from one engine to another. And that, that lets you recover from, recover from engine death.

But it depends on the nature of your ensemble of tasks, how much work it is to recover from an engine death. If it's, if, if you've got nothing but atomic tasks, then it's easy. But if you've got nothing but atomic tasks, almost everything is easy.

All right. I'm just going to define a couple of simple functions. Something that multiplies two numbers. Something that summarizes information about my current process. The relevant one is probably going to be the process ID.

Now, the, the basic API for remote execution in IPython is this view.apply. So I create a view, and then instead of calling the function locally, I pass the function and its arguments. So instead of mall56, I call apply mall56. Same thing happened. I call apply summary, same thing happened. Same thing happened. Except, the PID when the function was called was actually a different one. So this function, the summary function was actually called on the remote engine. So it, IPython packed up the function, packed up the arguments, sent them over to the engine, engine said, all right, I'm going to call that function with arguments, and then here's the return value, send it back.

So this is, this is not a representation of a Python dictionary, it's actually a dictionary. Unlike in the notebook, say what? Right here. Yeah, create a client. So in the notebook, generally what you do is you send, you execute, you execute code as text, and then you get back all these representations. You can have MIME type data, that can be HTML, PNG, all kinds of stuff. But what you don't get is actually the code object itself, because JavaScript doesn't understand what Python objects are.

And so with, I mean, it would, with JSON you could send integers and simple dictionaries of strings, but an important difference of the IPython parallel client, when using this apply functionality, is that instead of talking code and code as text and representations of output, it's talking actual Python functions and Python objects as arguments, and then it returns actual Python objects as the result of the computation.

And so we've done a basic, basic execution remotely, and basic execution, what's, what does a parallel call look like? The only difference between remote execution and parallel, parallel remote execution, is what kind of view you create, so that the API is the same, you call apply with multiply and five and six, but instead of slicing with engine zero, I sliced everything. So just give me all my engines, and call apply. And what do I get? I get a list that is the same shape as my engines.

Yeah? I'm having a little trouble finding that. I'll go into more detail on how to create views and everything. I'm just showing that once it's in parallel, I created a different view, called the same function, and I got, I got parallel, I got multiple results because I called it multiple times. But I'll go, I'll go into how to create views and what kind of views you might want to create in the next section.

So I got a direct view with zero. I got a direct view with range four. Or list range four, if you're in Python 3. All right, so I got PIDs. I can extract PIDs with, if you want to dramatically increase the readability of your already dense line with the list comprehension, I can get the PID of all my engines.

Python, the Python language, has a built-in function for mapping. You just call map with a function, and then iterators of arguments. So views, also, views have a map method. And this map method behaves exactly the same as the map function with some slight differences on infinite iterables. And we've got a couple parallel magics. All this stuff I'll go into a bit more detail in the next.

Right. So all my engines are on the same host and they each have a different PID. This shows I can do print statements.

So now we're going to talk about the basics of doing things remotely and ultimately asynchronously. I'm going to start by creating a single view with block equals true, so synchronous view on engine zero. And the API really is, it's all about this apply. I build, I define functions, I get arguments, and I just call those functions. And so locally I just call the functions and then to do it remotely I just pass it to apply.

So here's a function that just gives me a collection of norms of an array as dictionary. So I created my array. I called my function. I have an empty markdown cell.

So to do the same thing remotely I just called my function, but I raised a name error. Raised a name error on numpy because numpy in this function is resolved to globals, which works fine in my interactive session, but numpy when it resolves to globals in my remote session, it didn't find it because numpy is not imported in the interactive session. So I need to import numpy on the road.

This is a common issue with people getting started with IPython Parallel, and that's that if you define functions interactively, any globals they refer to refer to globals in the interactive namespace. And if you call them remotely, then those globals will resolve to the interactive namespace in the remote environment. And this can be annoying for things like imports of numpy, but it can also be useful for operating on data that I can define variables in my interact on my engines, and I can just refer to them as globals in my local functions. And when I call them, it will get the data out of the global namespace.

What? Am I adding an import hook in this context manager? Yes. Right, because I don't want it to happen all the time. Yes, so this is a context manager that, if you, one of the goals of the rewrite of IPython Parallel from the olden days is adding, we didn't used to be able to do anything other than code as text, and so adding things where you don't have to type code as text is something that we worked on, and one of those things is being able to import numpy in a context manager. Yes.

So I sent the function itself. But the, so when I call apply, I call apply with get norms. So I'm actually, when I do that, I'm actually sending the function object to the engine, and that function object, the internal code of that function object refers to, when it says numpy in here, that means whatever the hell global numpy is. So once I, yes.

It will send a new copy of the function, if, so there are things I'll get to later about if, if there are things that are expensive to send, there are ways to send them only once. Well, also, if you, so if you send, if you send a function that's a module function, so if I look at, oh, what's the, so get norms won't be too tiny, but if I look at pickle, so if you pickle a function that's a module function, the pickle representation of that function is just basically, it's where it is. So that's, that's something that's not really worth being efficient about, because if I were to encode any, anything more abstract, as like a cache reference, it would be hard to get more compact than that.

But yeah, the, so the first thing would be, if, if a function is big and complicated, make it a module function. And actually, the global namespace resolution also changes. So modules, so the reason interactively defined modules, their module is main. So when they refer to globals, they refer to globals, which is, they refer to the interactive namespace. That's not true of module functions, right? When you define a function in the module, and you did import numpy at the top of the module, then you can use numpy in the function. That doesn't break in IPython, because it, it, it unpick, unpacks it back where it was, so the globals still resolve.

It's just the, the issue is that the main module, which is the interactive namespace, is different for my client interactive session than it is for my engine interactive session. It's one of those things that is straightforward once you know all of how I, how, all of how Python namespaces and modules work, particularly in interactive sessions, but that is not, but it is far from clear just looking at things.

It's why, so often people will, they'll work stuff out in a notebook, and then they'll take that stuff and they'll move it to, like a utility module just right next to it, and they'll import from there, and then the behavior will totally change, and that's because things in main behave differently from things not in main in, in terms of how they relate to the outer namespace, and people get confused both by relying on globals referring to main and by, wanting that to not happen. They get confused by both.

Okay. So now I can call that function, I did import NumPy, now I can call the same function, and it will work from now on because NumPy is imported.

So the simple, just like we've got magic run in IPython, I have a script that just does, defines a function, defines a variable, does a couple imports. I can call run with a path, and that sends the content of that file and runs it on my engine. I can execute code as text, assign a new variable to the result of a function call, I can get the results, A is 5, B is 25.

Now we already saw the fact that globals refer to the surrounding namespace being a problem when I hadn't imported NumPy yet. Now this is where it's a feature, and that's that I can update A in my namespace by just declaring it as a global. So I can increment A, this finds A in the global namespace of the engine, and then adds a value to it. So I'm just calling engine.apply increment A 5. So 5 plus 5 is 10, call it again, 10 plus 5 is 15. So I'm loading A from the globals on the engine, and then I'm writing back to it.

And again, referring to the global namespace, if you've got a name that's undefined, it will fall back on the global namespace, say, okay, A, I got it from main, A is 20 at this point, I can multiply numbers by A without doing any shenanigans. If I just assume it, treat A as a global in my function, it will get it from the interactive namespace. So this lets you separately push data and then just use it by its name.

And then the last bit is identity, is that sometimes you want to push data only once, but then you want to call apply with that data that's on your engine as an argument. You don't have to send it every time. So when I call apply with the function and arguments, it sends the function and the arguments and then gets back the result. But if one of those arguments is a two gigabyte array, and I want to call 10 functions on it, I don't want to send it every time. So what you do is you send it once, and then what you pass to the argument of apply is a parallel reference. And this is a special object that when you give it as an argument to apply, when it's deserialized on the engine, it actually gets the object in the interactive namespace referred to by that string.

Yes, so I've already sent A, and this just says give me A. I get a name error if I ask for a variable. It's just like if I had called that function with doesn't exist, I would get a name error on doesn't exist because it's not there.

So parallel reference is... So what apply does is it takes the function and the arguments and then it, to first order, pickles them, and then sends them over to the engine, and then that unpickles them. And a reference object is a special object that when it's unpickled, instead of unpickling as a reference object, it unpickles as like main.name. It's ever so slightly more complicated than that, but that's the gist of it.

And you can actually use references, you can have a reference to a callable as the function in apply. So I can do... A equals five. What's a method on a number? A.bitLength, that sounds interesting. So if I... I still have... I'm pretty sure this is going to work. Yeah. So what this did was it resolved, the reference resolved to the method A.bitLength and then called it. It was confused by the method. It was confused by that. The A is different.

So if I, or what was five? All right. So I got basics of execution. You might want to actually get some data from your client to your engine.

So the gist is you've got push. Push sends data, takes a dictionary, and then updates the interactive namespace. So one of the important pieces of IPython, important pieces that is, it is important to get comfortable. One of the pieces of Python is important to be comfortable with when working with IPython if you want to really kind of get the most out of it. It's that in Python, you've got modules. Modules have a namespace, and a namespace is just a dictionary. In IPython Parallel, you're just doing remote execution. You've just got remote namespaces. And a remote namespace just means a remote dictionary.

Yes, well, yes and no. You can do that. You will pretty much guaranteed get pickling failures, because you will try to send things that won't pickle. But if there were no unpickleable things, then yes, that would work. It's actually backwards. So the reference, so I create a reference on my client session. So if I do a reference on A, that means that when this code executes on my kernel, the kernel, it gets A from its own interactive namespace.

Let's do an example. If you want to pass it. Yeah, yeah. So passing is a reference. Passing is a reference, basically, yeah. So it's splitting up the, when you call a function with arguments, you're sending the function and the arguments. If you want to break that up, so you do push for the arguments, and then from then on, you use references.

Yeah. It's just pickle. We do, so we do, pickle refuses to serialize some things that it can actually serialize just fine. And one of those things is functions. So that is the extent, well, so the main thing that we add to pickle, or we do a pass to wrap objects in other things that are pickleable. And the main thing we do there is take function objects and say, this is actually a function object. Or we take a function object and then store its attributes, and then tell pickle, hey, this isn't a function object at all. You can pickle this just fine. And then it unpickles it. And then we do basically what pickle should do. We don't do anything, things like Cloud Pickle from PyCloud and DIL do all kinds of crazy stuff. And they can get to the point of pickling the interpreter.

And basically, all we did was add, we need to send functions, because otherwise we can't use functions as our main API. And that's all we added. The other thing we added was efficient. We do not pickle NumPy arrays. We wrap NumPy arrays in a special object, then actually send them with zero copy, with zero MQ. So there are zero in-memory copies of a NumPy array when you send it. It gets copied over the network. So you're not offloading a copy, you're actually making a copy of it?

No, because it's still a TCP connection. So there is a copy. The engine will have a copy, unless you use memmap. The engine will have a copy, but you won't. The engine, if you did a naive thing with pickle, when you send it, you would have two copies. Because a pickle representation of a NumPy array is a little bit of metadata, and then a copy of the whole thing. And then the engine would get a copy as the pickle, and then unpickle it, and then have two copies. So if you're running up against memory limits, and push results in what would be like seven copies of your array in memory, you can, that can be annoying and have performance consequences.

Yeah? How do you keep these examples available when you can't run it in Python? Oh yes, yes, yeah, yeah. Yeah, the IPython parallel is just a library. You don't need to use IPython for any part of it. Take all the examples I have, with the exception of a couple that display things. They run as a plain script. Yes, yeah. And that's how, in most real production use, if you're doing, you often won't be doing an interactive session, you'll be, spin up engines, submit a bunch of work, maybe shut down that client, write down what work you submitted, and then sometime later, open another client and say, give me the results. It's all offline, you don't have to do anything interactive.

Yeah? Yeah. All right, so, moving along. So, we've got, yeah. So, pandas, yeah. Yeah. I won't come back to that today. Yeah, you can.

So, we, NumPy arrays are easy, because they're a tiny bit of metadata, and then a blob of memory. Pandas are less easy, because they're basically, I mean, they're basically slightly more metadata. So, we could handle them cleverly, but we don't. Just because, if it's big, then, if it's a big data frame, then you're probably loading it from a file anyway.

Yeah, and then basically what you would do is, you would distribute the file data. So, if you're using the efficient, so pandas can efficiently load large data frames from disk, using memory mapping and all that stuff. So, what, if your data frame is large, is I would distribute it so that it's accessible via the file system, and you do that out of band. You don't do that with, you can do it with IPython if you want, but there's not a big reason to. And you send it, you send the file to every physical machine, and then you load it in the, kind of, memory map lazily evaluated from disk mode.

So, you don't, rather than loading the data frame on the client and sending it, you send the code to load the data frame to the engines and then the engine is loaded directly. That's true of pretty much all data. If you can load the data on the engine, it will be better to load it than to send it.

Yeah? Right. Yeah. If you've got a NumPy array that's an attribute of an object that enable, we won't do anything special. Yeah. Yeah. It's only if it is an argument to the function. I think we might walk like one level deep, so if you pass an argument that is a tuple of NumPy arrays, we may catch that, but nothing more elaborate than that. And I'm not sure if we used to do that. I'm not sure if we do that anymore. Yeah.

So sending data, you do that with push. Getting data, you do that with pull, logically enough. Pull can take a name. Push takes a dictionary. Pull takes one or either one name or a tuple of or one key or a tuple of keys. And we've got, again, since, as I talked about, a remote namespace is really just a dictionary. So if you've got an API around a remote namespace, that API might as well implement at least some subset of dictionary methods. So you can do a dictionary assignment.

You can execute. So I assign A as range five, B is A backwards. I can pull B and I get range five backwards. So that's the simple way of moving data around. It's just, it's a remote. Think of it as a remote dictionary. You can write to that dictionary. You can read from that dictionary. It just happens that it might take a while if you're asking for a couple of gigs.

I want that so badly but context managers do not give you access to the code block. Yeah, we want that but we can't. Context managers don't give you enough access to do that. Yeah, it's sad. Yeah, time for a pep. That's actually a good idea. It is a good idea for context managers that actually have access to the code object without it being, yeah, the AST or something, without it being executed. That would be, that would make this, that would, right, because execute, one of our goals was to get rid of code as text.

But, and the, if you could do it from looking at code, yeah, with, you know, the, what we really want is things like, you know, exec code in something like that or with E0, right, that would be awesome. And, but context managers don't give you the context you need. But if someone writes an IPEP to actually add that, then we would use it immediately.

So here's an exercise to do if you're up and running. So I've got a matrix, A. I'm wondering if you, for an exercise, can you call these functions remotely. So let's do A0.execute.

So the engine has a different value of A. Now I just want to call these functions, get the eigenvalues and get the norm of A, but actually execute that function on the engine. Does that make sense? Yeah. So I've got a couple of functions. I've got an array and I want to do, I want to basically make these same local calls but I want to make those calls actually execute on the remote namespace. And then, yes, I would like the results.

Yeah. There's the hint so far. It's a zero dot. Second hint, zero dot apply. Because I'm passing it in module function, yes. If I wrote a function, if I wrote my norm, return NumPy. If I wrote that, I would need to import NumPy. But if I pass it the function itself, I don't need to. But also if you've been shift entering along, then NumPy has been imported on the engine anyway, so. Not as NP, no. But that still the error.

Yes. So you'll get, if you've got no, you'll get, if you've got no, if you've got no, yeah, you'll get weird errors if there's no connection file. So there's no connection file, it'll do that. If there is a connection file but there's no cluster, you'll get a timeout after 10 seconds, I think.

Yes. Yes, but I've got a default profile, so it's, oh. Oh, that, you're looking at that, IO error? That's the one, yes. Sorry, the profile didn't exist when I called it that. Yes. So if you get that, that means there isn't a cluster running. I will, I will open a pull request soon, let's say. But does everyone understand how to start and stop the cluster from the graphical interface? So at least now if you recognize that error, now you know what to do?

Yes. Yes. Click the big logo, which won't look like that, but it will say those words, then click clusters, and then click start. Or in a terminal, do IP cluster start. Yes.

Yes, I'll, I'll, I'll, I'll do one now, one second. What are you doing after this? Where did I go?

So there we've got our solution, as I call the module function, I'm going to pass it a reference to A. And the difference to that is if I just pass it A, I'm going to take A from my local namespace, send it, and then call the function with my local A and then get the result back. Which is kind of silly because I could just call it remotely if I'm going to send the argument, if I'm going to send the argument and send the function.

And it doesn't take very long. No, I think it might be using eval. High tech. Right here. So this is the, the startup is, I've got A, it's over there. Assuming you have A. Just to, just so that you can tell that I'm doing a different thing.

Yeah, this, this is a shortcut for push. Yeah. And then I can call it, I add two as the extra argument for norm. And now the gist of IPython's API where you can get more, yeah. No, it's star args, double star keyword args. So forget what the name of the argument is. That's, that is in fact one of the differences between apply and between IPython apply and built-in apply, is that instead of passing a tuple and a dict, you just call it like, basically you take the parentheses and you move it over. So instead of, instead of foo A B equals five, you just do apply foo A B equals five.

Which adds some complexity to IPython, to the client implementation. But I, is a, I think a nicer interface than having to turn everything into a tuple. Turn it into a tuple work? Was it a link, did you just put parentheses or did you have commas? You did that with parentheses. Fascinating. That gave me a different result. But it did eval, it called norm with that, I don't know what that does. So that resulted in this call. Which I don't even know what that means. I, that, yeah. Right?

So a lot of the powerful stuff you can do with IPython is, so we're sending a message and then we're going to get a message back. It's kind of silly to wait for it. If you want to, you know, assign a bunch of work and then wait for, you want to wait for the results when you actually need them. So IPython's interface is fundamentally asynchronous.

So I just said block is false, which is the default behavior, but I said block equals true at the beginning for simplicity. Let's do this, step through this faster.

So I'm just calling a function that takes ten seconds. I ask if it's ready, it's not ready. I get with a timeout, this is another thing inherited from the async result from multiprocessing. I get a timeout error, it's not ready. But then if I call get with no arguments, it defaults to waiting up to forever.

And so apply, the default behavior of apply is governed by the block attribute. But you can always, regardless of the block attribute, you can always explicitly do it synchronous or asynchronous execution by using underscore sync and async. If you call get with no arguments, so get takes a timeout and the default timeout is forever. So we'll block up to that timeout and if it's not ready after that time, it'll raise a timeout error. And the default behavior is infinity. But if you don't want to wait at all, you can do get zero and that'll raise a timeout error that's, there's not a big reason to use get zero instead of if ready. Ready is asking the same question.

There's also a, so get returns the value, there's also a wait that is like get but instead of returning the results, it just returns none. This is, it returns none on success and timeout error otherwise. That's just wait, wait and get are inherited from multiprocessing.pool and they behave exactly the same.

Something we have in addition to multiprocessing.pool is metadata about the execution. And this is where a lot of the fancy stuff in terms of diagnosing and instrumenting and monitoring happens. So there's metadata about the execution which includes the engine where it ran, information about the messages. If there's code, you can get the code that ran, tracebacks.

This object would contain rich metadata, rich MIME type metadata. So if I did plots remotely, this object would contain those plots and timestamps for when the message left the client, arrived at the engine, left the engine and arrived at the client. And also the standard error, standard out of the, of the execution.