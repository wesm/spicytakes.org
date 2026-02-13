---
title: "Figuring Out What They Expected"
date: 2000-04-11
url: https://www.joelonsoftware.com/2000/04/11/figuring-out-what-they-expected/
word_count: 1576
---


When a new user sits down to use a program, they do not come with a completely clean slate. They have some expectations of how they think the program is going to work. If they’ve used similar software before, they will think it’s going to work like that other software. If they’ve used *any* software before, they are going to think that your software conforms to certain common conventions. They may have intelligent guesses about how the UI is going to work. This is called the *user model*: it is their mental understanding of what the program is doing for them.


The program, too, has a “mental model,” only this one is encoded in bits and will be executed faithfully by the CPU. This is called the *program model*, and it is **The Law**.** **As we learned in [Chapter One](https://www.joelonsoftware.com/uibook/chapters/fog0000000057.html), if the program model corresponds to the user model, you have a successful user interface.


Let’s look at one example. In Microsoft Word (and most word processors), when you put a picture in your document, the picture is actually embedded in the same file as the document itself. You can create the picture, drag it into the document, then *delete the original picture file*, but the picture will still remain in the document.


Now, HTML doesn’t let you do this. HTML documents must store their pictures in a separate file. If you take a user who is used to word processors, and doesn’t know anything about HTML, and sit them down in front of a nice WYSIWYG HTML editor like FrontPage, they will almost certainly think that the picture is going to be stored in the file. Call this *user model inertia*, if you will.


So we have an unhappy conflict of user model (the picture will be embedded) versus program model (the picture must be in a separate file), and the UI is bound to cause problems.


If you’re designing a program like FrontPage, you’ve just found your first UI problem. You can’t really change HTML. Something has to give to bring the program model in line with the user model.


You have two choices. You can try to change the user model. This turns out to be remarkably hard. You could explain things in the manual, but everybody knows that users don’t read manuals, and they probably shouldn’t have to. You can pop up a little dialog box explaining that the image file won’t be embedded, but this has* two* problems: it’s annoying to sophisticated users, and users don’t read dialog boxes, either (we’ll take more about this in Chapter Six).


So, if the mountain won’t come to Muhammad … your best choice is almost always going to be to change the program model, not the user model. Perhaps when they insert the picture, you could make a copy of the picture in a subdirectory beneath the document file, so that at least you can match the user’s idea that the picture is copied (and the original can be safely deleted).


### How do I know what the user model is?


This turns out to be relatively easy. Just ask them! Pick five random people in your office, or friends, or family, and tell them what your program does in general terms (“it’s a program for making web pages”). Then describe the situation: “You’ve got a web page that you’re working on, and a picture file named Picture.JPG. You insert the picture in your web page.” Then ask them some questions to try and guess their user model. “Where did the picture go? If you delete Picture.JPG, will the web page still be able to show the picture?”


A friend of mine is working on a photo album application. After you insert your photos, the application shows you a bunch of thumbnails: wee tiny copies of each picture. Now, generating these thumbnails takes a long time, especially if you have a lot of pictures, so he wants to store the thumbnails on the hard drive *somewhere* so that they only have to be generated once. There are a lot of ways he could do this. They could all be stored in one large file called **Thumbnails**. They could all be stored in separate files, in a subdirectory called **Thumbnails**. They might be marked as hidden files in the operating system so that users don’t know about them. My friend chose one way of doing it which he thought was the best tradeoff: he stored the thumbnail of each picture **picture.JPG** in a new file named **picture_t.JPG** in the same directory. If you made an album with 30 pictures, when you were done, there were 60 files in the directory including the thumbnail pictures.


You could argue for weeks about the merits and demerits of various schemes of storing the pictures, but as it turns out, there’s a more scientific way to do it. Just ask a bunch of users where they think the thumbnails are going to be stored. Of course, many of them won’t know or won’t care, or they won’t have thought about this, but if you ask a lot of people, you’ll start to see *some* kind of consensus. The popular choice is the best user model, and it’s up to you to make the program model match it.


Next, you have to test your theories. Build a model or prototype of your user interface and give some people tasks to accomplish. As they work through the tasks, ask them what they think is happening. Your goal is to figure out what they expect. If the task is “insert a picture,” and you see that they are trying to drag the picture into your program, you’ll realize that you better support drag and drop. If they go to the Insert menu, you’ll realize that you better have a Picture choice in the Insert menu. If they go to the Font toolbar and replace the word “Times New Roman” with the words “Insert Picture”, you’ve found a relic who hasn’t been introduced to GUIs yet and is expecting a command line interface.


How many users do you need to test your interface on? Your instinct may be “the more, the better,” which makes sense for scientific experiments. But that instinct is wrong. Almost everybody who does usability testing for a living seems to think that five or six users is enough. After that, you start seeing the same results again and again, and any additional users are just a waste of time.


You don’t need a formal usability lab, and you don’t really need to bring in users “off the street” — you can do “50 cent usability tests” where you simply grab the next person you see and ask them to try a quick usability test. Make sure you don’t spill the beans and tell them how to do things. Ask them to “think out loud” and interview them using open questions to try to discover their mental model.


### If your program model is nontrivial, it’s probably not the user model.


When I was 6 and my dad brought home one of the world’s first pocket calculators, an HP-35, he tried to convince me that it had a *computer* inside it. I thought that was unlikely. All the computers on Star Trek were the size of a room and had big reel-to-reel tape recorders. I thought that there was just a clever correlation between the keys on the keypad and the individual elements of the LED display that happened to produce mathematically correct results. (Hey, I was 6).


An important rule of thumb is that user models aren’t very complex. When people have to guess how a program is going to work, they tend to guess simple things, rather than complicated things.


Sit down at a Macintosh. Open two Excel spreadsheet files and Word document file. Almost any novice user would guess that the windows were independent. They *look* independent:


The user model says that clicking on Spreadsheet 1 would bring that window to the front. What *really* happens is that Spreadsheet **2** comes to the front, a frustrating surprise for almost anybody:


As it turns out, Microsoft Excel’s program model says that “you have these invisible sheets, one for each application, and the windows are ‘glued’ to those invisible sheets. When you bring Excel to the foreground, all other windows from Excel will move forward, too.”


Riiiight. Invisible sheets. What are the chances that the user model included the concept of invisible sheets? Probably about zero. So new users will be surprised by this behavior.


Another example from the world of Microsoft Windows is the Alt+Tab key combination which switches to the “next” window. Most users would probably assume that it simply rotates among all available windows. If you have window A, B, and C, with A active, Alt+Tab should take you to B. Alt+Tab again would take you to C. Actually, what happens is that the second Alt+Tab takes you back to A. The only way to get to C is to *hold down* Alt and press Tab* twice*. It’s a nice way to toggle between two applications, but almost nobody figures it out, because it’s a slightly more complicated model than the rotate-among-available-windows model.


It’s hard enough to make the program model conform to the user model when the models are simple. When the models become complex, it’s even more unlikely. So pick the simplest possible model.
