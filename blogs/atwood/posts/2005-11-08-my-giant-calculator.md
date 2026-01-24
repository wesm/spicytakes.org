---
title: "My Giant Calculator"
date: 2005-11-08
url: https://blog.codinghorror.com/my-giant-calculator/
slug: my-giant-calculator
word_count: 599
---

Have you ever noticed how many people **keep a physical calculator next to their computer?** The irony is almost palpable. My favorite is the [calculator mousepad](http://www.google.com/search?q=calculator+mousepad).


![](https://blog.codinghorror.com/content/images/2025/03/image-350.png)


Jef Raskin, in [The Humane Interface](http://www.amazon.com/exec/obidos/ASIN/0201379376), defends the practice of keeping a pocket calculator next to your PC:


> It’s true. Many of us keep a calculator beside our computers. Why do you need this simple-minded device when you have a whole computer in front of you? You need it because you have to go through contortions worthy of a circus sideshow in order to do simple arithmetic with the computer. There you are, tapping away at your word processor when you want to do a division: 375 packages of Phumuxx cost $248.93; what is the price for one package? On my computer, I have to open up a calculator window. To do this, I move my hand from the keyboard to the mouse, which I use to do a click-and-drag to open the calculator. Transferring my hands back to the keyboard, I type in the numbers I need or tediously cut and paste them from my document. Then I have to press a few more keys and finally copy the results into my document. Sometimes, the calendar window opens right on top of the very numbers I need, just to add insult to injury. In that case, I must use the mouse to move the calculator window out of the way before proceeding. **It is much faster to grab a pocket calculator.**


So what’s wrong with [good old calc.exe?](https://web.archive.org/web/20051225085427/http://blogs.msdn.com/shawnfa/archive/2004/10/06/238923.aspx) Raskin ran a little experiment:


> Using an experienced computer and calculator operator as my test subject, with his word processing program open before him, I measured the total time it took for him to pick up a calculator, turn it on, do a simple addition, and return his hands to the keyboard to resume typing. **It took about 7 seconds.** I then measured the time it took for him to use the built-in calculator. He had to move the cursor to the menu bar at the top of the screen, find the calculator program, open the calculator, enter the sum, and then click back in the word processor so he could resume typing. **This took about 16 seconds.**


I’m not sure why Raskin is so hell-bent on using the mouse to launch the calculator.


![](https://blog.codinghorror.com/content/images/2025/05/image-144.png)


Even on the Mac (where I assume this test was performed), there have to be keyboard shortcuts. On Windows, we’d need the following keystrokes to find the sum of 13 and 14 and paste the result in our word processor:


![](https://blog.codinghorror.com/content/images/2025/05/image-145.png)


It’s certainly possible to perform calculations without ever moving your hand from the keyboard. Many keyboards now have calculator buttons which would reduce the number of keypresses even further. **I guarantee I could beat that 7 second time quoted for the physical calculator.** But it’s not exactly *simple*, is it?


Instead of keyboard acrobatics, Raskin proposes a simpler “do it anywhere” facility. Something built into the OS that obviates the need to spawn a separate window for these kinds of helper functions:

kg-card-begin: html
kg-card-end: html

I agree that the OS should be providing this kind of non-modal (non-window, even) functionality. The run menu is a [(very) limited form of this](https://blog.codinghorror.com/a-celebration-of-the-windows-key/), while [SlickRun](http://www.bayden.com/SlickRun/) and [ActiveWords](http://www.activewords.com/) go even further.


**Users with calculator mousepads are no laughing matter.** Whenever I see users like this, I’m reminded of how far we have to go in GUI design when the simple act of adding numbers together is so complicated.

[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[human-computer interaction](https://blog.codinghorror.com/tag/human-computer-interaction/)
[computing devices](https://blog.codinghorror.com/tag/computing-devices/)
