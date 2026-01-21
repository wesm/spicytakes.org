---
title: "Talk: Introducing Ghostty and Some Useful Zig Patterns"
date: 2023-09-12
url: https://mitchellh.com/writing/ghostty-and-useful-zig-patterns
word_count: 3552
---


This is the text format of a talk I did for [Zig Showtime](https://zig.show).
If you'd rather watch the video, you can find it on YouTube:
[Zig Showtime: Ghostty](https://youtu.be/l_qY2p0OH9A?t=331).
The video also includes a Q&A session at the end which I did not include
in this post.


![Slide 1](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-1.png&w=3840&q=75)


Hello! I'm excited to talk today about Ghostty. Ghostty is a brand new terminal emulator written from scratch in Zig.


Note: at the time of writing this, Ghostty is still not publicly available.
I make note of this multiple times in this talk but I wanted to mention this
up front so no one gets the wrong idea right away. The plan is for Ghostty
to be free and open source and released sometime in 2024. We're currently
running a closed beta program (with source access). I talk about this
at various points in the talk.


---


![Slide 2](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-2.png&w=3840&q=75)


My name is Mitchell! I'm one of those people that just loves, loves, loves to code.


I've started some popular software projects in the past, maybe you've heard of them maybe not: Vagrant, Terraform, Vault, etc. I haven't worked on any of those projects in many years, though.


I'm also one of those people that has *always* had a side project going on. Always. I wrote a Hearthstone log analyzer and replay software around a decade ago and sold that to a pro esports team. I wrote my own mail server from scratch a few years ago and use that to run mail on some of my domains. And now, well now I have a terminal emulator.


I built this slide around dinner time and I'm really hungry so I decided to just use a bunch of pictures of me eating. I'm not particularly passionate about food or anything like that. I'm just hungry like... right at this moment. And I like a thematic element that really ties the room together.


---


![Slide 3](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-3.png&w=3840&q=75)


But this talk is about Ghostty! The terminal emulator!


So before going further, here is what Ghostty looks like! In this one screenshot you can see that Ghostty is quite full featured!


Ghostty is a native app on macOS and Linux. It has splits, supports true color, runs vim just fine, has multiple font styles (bold, italic, etc.), supports the Kitty graphics protocol, and more. That's just what you can see *in this screenshot!*


---


![Slide 4](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-4.png&w=3840&q=75)


In case you don't know what a terminal emulator is, you've probably used one, here are a few. There are dozens, hundreds more.


---


![Slide 5](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-5.png&w=3840&q=75)


If there are so many, why create another one?


---


![Slide 6](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-6.png&w=3840&q=75)


At a fundamental level, this is the state of terminal emulators today as I saw it. You have fast terminals, feature rich terminals, and native terminals. You can pick at most two properties to have.


---


![Slide 7](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-7.png&w=3840&q=75)


Ghostty aims for -- and in my opinion already achieves -- all properties.


---


![Slide 8](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-8.png&w=3840&q=75)


Fast, features, native feel is *not mutually exclusive*.


I think Ghostty does well enough *today* to deserve a green checkmark, and there is still a lot we can do better at.


Also, calling out the warning signs, my bar for a native platform experience is that the app feels and acts like a purpose-built native app. I don't think this bar is unreasonable. For example, I don't think it's unreasonable to say that Alacritty is kind of not native because new windows create new processes. Or that Kitty is kind of not native because tabs use a non-native widget. And so on (there are many more examples for each).


---


![Slide 9](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-9.png&w=3840&q=75)


So at a "foundational" level, I'm trying to do this: the speed of Alacritty, the feature richness of Kitty, the level of native integration as iTerm (for macOS), etc.


---


![Slide 10](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-10.png&w=3840&q=75)


But I want to go further. I want the terminal to be a modern platform for text application development, analogous to the browser being a modern platform for GUI application development (for better or worse).


Browsers ship *dozens* (hundreds?) of new features per year. They innovate fast and excite application developers. This may be a bit much, but I think terminals can innovate faster than they are.


Some examples are listed here:

- Progress bars! Why are we redrawing progress bars (poorly, most of the time) every single time?
- Drag and drop so editors and other applications can act more natively.
- Tab/split control so multiplexers can take advantage of modern terminal emulator performance and features.
- Mouse gestures so TUIs can react to flicks, multi-touch, momentum, and more.
- Security features: terminal escape sequences are a scary place today. More on this another time. We can do better.
- And more!


---


![Slide 11](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-11.png&w=3840&q=75)


Is Ghostty fast? How do we know? There are many ways to benchmark a terminal emulator, and I don't want to dedicate a significant portion of this talk to that. The point I want to make is Ghostty is "fast." I'm not going to claim it is the "fastest."


Here I show Ghostty running a DOOM fire animation that records the FPS. This is a good stress test because it modifies so many cells and also is performing scroll back.


You can see Ghostty maintains around 480 to 500 FPS and the animation is
very, very smooth. By comparison, the official macOS Terminal.app (so I don't
pick on any awesome community project) is extremely choppy at less than 10 FPS.
If you use a "fast" terminal emulator like Alacritty or Kitty you'll see
similar numbers to Ghostty.


The point is: I'm not trying to say Ghostty
is the fastest, but it is *in the category of "fast"*, so I think
the green checkmark in my table is warranted.


Try this with your own terminal and see how it goes: [https://github.com/const-void/DOOM-fire-zig/](https://github.com/const-void/DOOM-fire-zig/)


Note for the text format: the slide image is an image so it won't show
the video. Ghostty runs the linked program at roughly 480 to 500 FPS.


---


![Slide 12](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-12.png&w=3840&q=75)


Is Ghostty feature-rich? I don't know how to quantify this, but here is a qualitative list of features we support, many that are relatively rare.


---


![Slide 15](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-15.png&w=3840&q=75)


On macOS, the main GUI experience is written in Swift using AppKit and
SwiftUI. The tabs are native tabs, the splits are native UI components,
multi-window works as you'd expect, etc. On Linux, the GUI experience is GTK
using real GTK windows and other widgets.


Features such as error messages are not implemented with a specialized terminal
view, we actually use real native UI components. The point is, while the
terminal surface and core logic is cross-platform, the user interaction is
all purpose-built for each operating system for a true native experience.


---


![Slide 16](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-16.png&w=3840&q=75)


Let's get a real quick overview of the tech stack and the project itself.


First, the project. The project is currently in a closed beta phase with source access. The reason we're doing a closed beta is because this is a **personal project** and I don't want to overwhelm myself. A closed beta lets me slowly invite people, fix their issues, and repeat.


When the project is ultimately released, it will be free and open source licensed most likely under the GPL license. I say "most likely" because testers are welcome to voice their input. An active area of discussion currently is perhaps choosing a more permissive license such as MIT.


There is a public discord you can join today. I source beta testers from that Discord. And I write a devlog every so often on my personal blog.


On the tech side, I will be going into detail about most of these in this talk so I won't spend too much time here. Just know that it's written in Zig, the native bits are truly native (i.e. AppKit on macOS), and we've written a lot of our own dependencies such as an event loop.


---


![Slide 17](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-17.png&w=3840&q=75)


Okay, so let's start out with the obvious question: why zig?


---


![Slide 18](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-18.png&w=3840&q=75)


Simply put: I like the community, language, and build system. I think the features of the language and build system are really well suited to this terminal project and this talk is dedicated to highlighting that.


---


![Slide 19](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-19.png&w=3840&q=75)


Speculate all you want, I don't care for this question and I don't care to answer it. I chose Zig, I like Zig, let's move on.


---


![Slide 20](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-20.png&w=3840&q=75)


Here is an overview of the code architecture by subsystem. These are the major subsystems within Ghostty along with their description. I'll show a visual diagram in the next slide...


---


![Slide 21](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-21.png&w=3840&q=75)


Here is the runtime architecture putting that together. Everything in this diagram is 100% Zig except for "apprt" on macOS, which is partially Swift.


The basic idea here:

1. The app is launched and the entry point is in "apprt."
2. Apprt is responsible for creating one or more "surfaces". A surface is anything that represents a single interactive terminal. Apprt can choose to put this in a window, tab, split, whatever. It doesn't matter to the core!
3. Each surface launches an IO thread and a renderer thread.
4. The IO thread creates the pty file description and runs the configured command (usually a shell). The IO thread is responsible for reading/writing the pty, handling terminal events such as escape sequences, etc.
5. The renderer thread converts the terminal state and draws pixels at some regular framerate. The renderer is also responsible for font shaping and rendering.


---


![Slide 22](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-22.png&w=3840&q=75)


As excited as I am about terminal emulators, this is Zig Showtime, so the focus of this talk is going to move to being about the Zig patterns I use in Ghostty.


These aren't in any particular order.


Note for online readers: Most of this section I tabbed over and showcased these patterns in the actual Ghostty source code (within a Ghostty terminal, naturally). If you fast forward the
[video](https://youtu.be/l_qY2p0OH9A?t=331) to these slides, you can watch.


---


![Slide 23](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-23.png&w=3840&q=75)


First up, comptime interfaces!


---


![Slide 24](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-24.png&w=3840&q=75)


A comptime interface is a value with an implementation that changes depending on some compile-time-known information.


The source code here are real examples extracted directly from Ghostty. The example shown here is the definition of a "font face" that depends on some build option. You can see that for some build-time setting we use CoreText, others FreeType, and we also support a web-based Canvas implementation!


The bottom pane shows the interface in use. Code using these interfaces doesn't care *how* things work, there is some defined interface and it calls it or uses it.


---


![Slide 25](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-25.png&w=3840&q=75)


Comptime interfaces are the primary way Ghostty implements platform-specific functionality and is used for fonts, renderers, app runtimes, and more.


The main benefit is for implementations that *never* change at runtime you can swap out implementations with zero runtime overhead. All of the field access and function dispatch is determined at compile-time.


---


![Slide 26](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-26.png&w=3840&q=75)


A feature of the Zig compiler is that it only analyzes code that is actually referenced. This is a feature, not a bug, because it enables situational code to exist without nasty `#ifdef`-style guards to make it invisible.


The downside is for comptime interfaces, you must ensure you test all build options otherwise it is very easy to introduce build failures.


Ghostty runs through all build options in CI.


---


![Slide 27](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-27.png&w=3840&q=75)


This is the same slide I showed earlier. I want to show this again to showcase what all of these features and patterns enable.


---


![Slide 28](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-28.png&w=3840&q=75)


Here are those same subsystems, the implementations that exist today, and the implementations that are possible in the future. Almost of all these alternate implementations are comptime interfaces.


---


![Slide 29](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-29.png&w=3840&q=75)


Next up, some more comptime, but this time data tables.


---


![Slide 30](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-30.png&w=3840&q=75)


This is an example of a table of data. In this case, we're looking at some input encoding information for the Kitty Keyboard Protocol.


The `RawEntry` tuple form is not very nice for real usage, but it is very convenient for easily building up a table.
Notice neither of these are `pub` -- they aren't meant to be used outside of this file.


With these non-pub entries, we then process them...


---


![Slide 31](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-31.png&w=3840&q=75)


Using comptime, we can process the raw entries. In this case, we're taking the raw entry tuples and converting them to more runtime-friendly structs.


The conversion process happens all at compile-time, so there is no runtime cost. Further, since the raw entries aren't ever used in runtime code, they don't take up any binary space in your final build.


In this case, the conversion is mostly a straightforward data transformation, but we can do cooler things...


---


![Slide 32](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-32.png&w=3840&q=75)


Here is an example from the table of platform-specific key codes. Our raw data contains the key codes for each platform (Mac, Windows, Linux via xkb, even USB codes). But for runtime we turn it into `entries` which contains only the platform we're building for.


This way, our struct is tighter, our final binary is smaller, and we don't need to do this conditional lookup at runtime.


---


![Slide 33](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-33.png&w=3840&q=75)


We can take that even further. Here is an example from the data table that defines what escape sequence a terminal should send to a running program for a given key input in a given mode.


A lot of these follow a distinct, repetitive pattern. Instead of just manually typing it all out, we can write a function we execute at comptime to programmatically build the data.


Many projects often have shell, Python, or other scripts to do data generation. With Zig, you can do it all in comptime.


Note: the `comptime {}` wrapper around our function body in `pcStyle` is a trick to ensure that this function can never be called at runtime.


---


![Slide 34](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-34.png&w=3840&q=75)


Next we'll talk build on comptime data tables and talk about comptime type generation.


---


![Slide 35](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-35.png&w=3840&q=75)


Let's start with a 30-second tutorial on the `@Type` builtin. A lot of people don't know this exists. The `@Type` builtin lets you create types at comptime. It is *ridiculously powerful* but also *ridiculously scary*.


---


![Slide 36](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-36.png&w=3840&q=75)


Be careful! This is something you want to limit use of to situations where it makes sense. You need to be careful to not go "full metaprogramming" because it harms readability and slows down compilation.


---


![Slide 37](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-37.png&w=3840&q=75)


This example shows how Ghostty defines the various "modes" it supports. A mode is a terminal mode that a running program can query and set that changes the behavior of the terminal emulator. There are hundreds of modes.


In this example, we have our standard pattern of an unexported `entries` data table. One of the ways we process this table is to turn all the keys into an exhaustive enum using the `@Type` builtin.


The reason I don't define the enum up front is because there is additional data associated with each entry that I want to keep packed for easy editing and reference. In this case, each mode has a value.


---


![Slide 38](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-38.png&w=3840&q=75)


This shows the creation of the `FontIndex` structure. This structure is used in Ghostty to reference a specific font. We use the high-bits to represent the style (regular, bold, italic, etc.) and the low-bits to represent an index into an array.


We can determine the exact number of bits we need for the index by determining the number of bits required for the style.


If we add more styles which add more bits, it'll limit the number of fonts we can represent with the index.


Note: this is paired with tests to ensure we have a specific size available so that if we do ever increase the bitsize of Style, we are doing it very consciously.


---


![Slide 39](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-39.png&w=3840&q=75)


Next we talk about how Ghostty integrated with Swift. The reality is this is a more general solution to *any* language that can call a C API, not just Swift.


---


![Slide 40](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-40.png&w=3840&q=75)


The problem we faced is that modern macOS development effectively requires Swift. Yes, you can build decent applications with Objective-C, but all the new fancy functionality and frameworks Apple is shipping is Swift-only, and the writing is on the wall for ObjC.


---


![Slide 41](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-41.png&w=3840&q=75)


On Linux, Zig just uses the GTK C API. Zig's ability to call C APIs is well known. The problem is Swift (for Mac apps) can't export a C API, macOS applications expect to own `main`.


But... Swift can call C. And Zig can export a C API.


---


![Slide 42](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-42.png&w=3840&q=75)


So I ended up also packaging up Ghostty as an embedded C API. I compile this into a static library that my Swift-based macOS app depends on, and Swift then calls the library.


---


![Slide 43](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-43.png&w=3840&q=75)


And here is Swift initializing the Ghostty configuration, for example.


---


![Slide 44](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-44.png&w=3840&q=75)


We can have an extremely native macOS experience this way without sacrificing portability with Linux or other future platforms.


But what's *extra* cool is how easy Zig made it (the Zig build system in particular) to write a program that can compile as both an exe and a lib.


---


![Slide 45](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-45.png&w=3840&q=75)


In the future, I plan on supporting the C lib artifact as an official artifact that could enable anyone to embed a fully functional, full featured, fast, modern terminal in their applications.


But for now, this is unpublished and used only for the macOS application.


---


![Slide 46](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-46.png&w=3840&q=75)


That's a tour of the major patterns we use in Ghostty. There is a lot more but I think that's good for one talk. Some of those patterns can probably be full talks on their own...


Let's finish this talk by talking a little bit more about Ghostty!


---


![Slide 47](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-47.png&w=3840&q=75)


So what's next for the project?


The terminal emulation capabilities are reasonably complete. It is extremely rare to find programs that don't work with Ghostty, render incorrectly, etc. These are top priority bugs when they're found. Dozens of testers are using Ghostty all day for their professional work, and it is reliable.


The focus now is mostly on native platform experiences and making the apps feel more and more purpose-built for that platform. For example, on macOS we're working on a GUI settings window instead of just file-based settings. We're also doing stuff like iCloud configuration syncing between Apple devices (own your own data).


And more...


---


![Slide 48](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-48.png&w=3840&q=75)


Ghostty is fast, but there is still a ton of room for improvement. There
are still a lot of low-hanging performance wins that we know about, which is
exciting since Ghostty is already quite fast.


Additionally, we'd like to fuzz our VT stream parser and handlers. We did
some fuzzing and found a few bugs so I'm sure there are plenty more lurking
around.


There are a variety of performance areas we've never measured at all
such as startup time, input latency, etc. We've tried to avoid pessimizing
these code paths but by measuring them I'm sure we'll find some big wins.


Ghostty's memory usage right now isn't great. It isn't *terrible*, but
it isn't great. I spent a lot of time and effort ensuring CPU and renderer
performance was great, but was a little lax on memory usage. There are some
easy wins here, for example we currently preallocate the entire scrollback
buffer which is a few megabytes. It'd be pretty easy to make that dynamically
allocate.


---


![Slide 49](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-49.png&w=3840&q=75)


We're running an active beta program. To be part of the program you must join Discord.


Our process is based around stability: we invite some number of testers and do not invite another wave until all of the outstanding issues are resolved. When I say "issues" I mean bugs or major missing functionality. We don't build every feature request.


---


![Slide 50](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-50.png&w=3840&q=75)


Ghostty will be publicly released next year (2024) sometime. I intend to continue to expand the beta program to potentially hundreds of people before then.


The first released version will be version 1.0 or at worst a 1.0 release candidate. The goal of this heavy testing program is that we can launch out of the gate with a stable, feature rich project.


I stated this earlier, but Ghostty will be FOSS and the license will likely be GPL. I say "likely" because testers still have input, but the current plan is GPL. Many other terminals are GPL. There are some concerns specifically about `libghostty` and GPL, so that is an active area of discussion.


In addition to wanting to have stable software, part of the delay is that I'm weeks away from having a baby **I have a newborn baby** and I know I'm going to be very very busy so I don't want to put undue pressure on myself by trying to also cultivate and launch a full blown OSS community.


Some parents have asked how I possibly had time to write a new talk,
deliver it, and create this post with a newborn baby at home. I
wrote the talk and this post (with the exception of some notes like this one)
prior to my baby's arrival. Delivering the talk itself was not too hard
to fit in between feedings. And yes, I'm tired. 😊


---


![Slide 51](https://mitchellh.com/_next/image?url=https%3A%2F%2Fstatic.mitchellh.com%2Fghostty%2Fzig-showtime%2Fslide-51.png&w=3840&q=75)


❤️

- [https://discord.gg/ghostty](https://discord.gg/ghostty)
- [https://mitchellh.com/ghostty](https://mitchellh.com/ghostty)
