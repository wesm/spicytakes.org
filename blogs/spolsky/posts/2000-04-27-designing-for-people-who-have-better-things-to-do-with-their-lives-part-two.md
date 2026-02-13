---
title: "Designing for People Who Have Better Things To Do With Their Lives, Part Two"
date: 2000-04-27
url: https://www.joelonsoftware.com/2000/04/27/designing-for-people-who-have-better-things-to-do-with-their-lives-part-two/
word_count: 2098
---


When the Macintosh was new, [Bruce “Tog” Tognazzini](http://www.asktog.com/) wrote a column in Apple’s developer magazine on UI. In his column, people wrote in with lots of interesting UI design problems, which he discussed. These columns continue to this day on his web site. They’ve also been collected and embellished in a couple of great books, like [Tog on Software Design](http://www.amazon.com/exec/obidos/ASIN/0201489171/ref=nosim/joelonsoftware/), which is a lot of fun and a great introduction to UI design. (Tog on Interface was even better, but it’s out of print.)


Tog invented the concept of the *mile high menu bar* to explain why the menu bar on the Macintosh, which is always glued to the top of the physical screen, is so much easier to use than menu bars on Windows, which appear *inside *each application window. When you want to point to the File menu on Windows, you have a *target* about half an inch wide and a quarter of an inch high to acquire. You must move and position the mouse fairly precisely in both the vertical and the horizontal dimensions.


But on a Macintosh, you can slam the mouse up to the top of the screen, without regard to how high you slam it, and it will stop at the physical edge of the screen – the correct vertical position for using the menu. So, effectively, you have a target that is still half an inch wide, but a mile high. Now you only need to worry about positioning the cursor horizontally, not vertically, so the task of clicking on a menu item is that much easier.


Based on this principle, Tog has a pop quiz: what are the five spots on the screen that are easiest to acquire (point to) with the mouse? The answer: all four corners of the screen (where you can literally slam the mouse over there in one fell swoop without any pointing at all), plus, the current position of the mouse, because it’s already there.


The principle of the mile-high menu bar is fairly well known, but it must not be entirely obvious, because the Windows 95 team missed the point *completely* with the Start push button, sitting *almost* in the bottom left corner of the screen, but not *exactly*. In fact, it’s about 2 pixels away from the bottom and 2 pixels from the left of the screen. So, for the sake of a couple of pixels, Microsoft literally* “snatches defeat from the jaws of victory”*, Tog writes, and makes it that much harder to acquire the start button. It could have been a mile square, absolutely trivial to hit with the mouse. For the sake of something, I don’t know what, it’s not. God help us.


In the previous chapter, we talked about how users hate reading, and will avoid it unless they absolutely cannot accomplish their task. Similarly:


> **Users can’t control the mouse very well.  **


I don’t mean this literally. What I mean is, you should design your program so that it does not require a tremendous amount of mouse-agility to use it right. Top six reasons:

1. Sometimes people are using sub-optimal pointing devices, like trackballs, trackpads, and the little red thingy on a ThinkPad, which are harder to control than true mice.
2. Sometimes people are using mice under bad conditions: a crowded desk; a dirty trackball making the mouse skip; or the mouse itself is a $5 clone which just doesn’t track right.
3. Some people are new to computers and have not yet developed the motor skills to use mice accurately.
4. Some people literally will never have the motor skills to use mice precisely, and never will. They may have arthritis, tremors, carpal tunnel; they may be very young or very old; or any other number of disabilities.
5. Many people find that it is extremely difficult to double-click without slightly moving the mouse. As a result they often drag things around on their screen when they mean to be launching applications. You can tell these people because their desktops are a mess because half the time they try to launch something, they wind up moving it instead.
6. Even in the best of situations, using the mouse a lot *feels slow* to people. If you force people to perform a multi-step operation using the mouse, they may feel like they are being stalled which in turn makes the UI feel unresponsive, which, as you should know by now, makes them unhappy.


In ye olden days when I worked on Excel, laptops didn’t come with pointing devices built in, so Microsoft made a clip-on trackball that clipped to the side of the keyboard. Now, a mouse is controlled with the wrist and most of the fingers. This is much like writing, and you probably developed very accurate motor skills for writing in elementary school. But a trackball is controlled entirely with the thumb. As a result, it’s much harder to control a trackball to the same degree of accuracy as a mouse. Most people find that they can control a mouse to within one or two pixels, but can only control a trackball to within 3 or 4 pixels. On the Excel team, I always urged people to try out their new UIs with the trackball, instead of only with a mouse, to see how it would feel to people who are not able to get the mouse to go exactly where they want it.


One of the UI elements which bothers me the most is the dropdown combo list box. That’s the one that looks like this:


When you click on the down arrow, it expands:


Think about how many detailed mouse clicks it’s going to take to choose, say, Times New Roman. First, you have to click on the down arrow. Then, using the scroll bar, you have to carefully scroll until Times New Roman is in view. Many of these dropdowns are carelessly designed to show only two or three items at a time, so this scrolling is none too easy, especially if you have a lot of fonts. It involves either carefully dragging the thumb (with such a small range of movement, it’s probably unlikely that this will work), or clicking repeatedly on the second down arrow, or trying to click in the area between the thumb and the down area — which will eventually stop working when the thumb gets low enough, annoying you even further. Finally, if you do manage to get Times New Roman into view, you have to click on it. If you miss, you get to start all over again. Now multiply by 10, if, say, you want to use a fancy font for the first letter in each of your chapters, and you’re *really *unhappy.


The poxy combo dropdown control is even more annoying because there’s such an easy solution: just make the dropdown long enough to contain all of the options. 90% of the combo boxes out there don’t even use all available space to drop down, which is a *sin*. If there is not enough room between the main edit box and the bottom of the screen, the dropdown should grow *up* until it fits all the items, even if it has to go all the way from the top of the physical screen to the bottom of the physical screen. And then, if there are still more items than fit, let the combo scroll automatically as the mouse approaches the edge, rather than requiring the poor user to mess with a teensy weensy scrollbar.


Furthermore, don’t make me click on the little tiny arrow to the right of the edit box before you pop up the combo: let me click *anywhere* on the combo box. This expands the click target about tenfold and makes it that much easier to acquire the target with the mouse pointer.


Let’s look at another problem with mousing: edit boxes. You may have noticed that almost every edit box on the Macintosh uses a `fat, wide, bold font` called Chicago which looks kind of ugly and distresses graphic designers to no end. Graphic designers (unlike UI designers) have been taught that thin, variable spaced fonts are more gracious, look better, and are easier to read. All this is true. But graphic designers learned their skills on *paper*, not on the screen. When you need to *edit* text, monospace has a major advantage over variable spaced fonts: it’s easier to see and select narrow letters like “l” and “i”. I learned this lesson after watching a sixty year old man in a usability test painfully trying to edit the name of his street, which was something like Fillmore Street. We were using 8 point Arial, so the edit box looked like this:


Notice that the I and the Ls are literally *one pixel wide*. The difference between a lower case I and a lower case L is literally *one pixel.* (Similarly, it is almost impossible to see the difference between “RN” and “M” in lower case, so this edit box might actually say Fillrnore.)


There are very few people who would notice if they mistyped Flilmore or Fiilmore or Fillrnore, and even if they did, they would have a *heck* of a time trying to use the mouse to select the offending letter and correct it. In fact, they would even have a hard time using the blinking cursor, which is two pixels wide, to select a single letter. Look how much easier it would have been if we had used a fat font (shown here with Courier Bold)


Fine, OK, so it takes up more space and doesn’t look as cool to your graphic designers. Deal with it! It’s much easier to use; it even *feels *better to use because as the user types, they get sharp, clear text, and it’s so much easier to edit.


---


Here’s a common programmer thought pattern: there are only three numbers: 0, 1, and *n*. If *n* is allowed, all *n*‘s are equally likely. This thought pattern comes from the belief (probably true) that you shouldn’t have any numeric constants in your code except for 0 and 1. (Constants other than 0 and 1 are referred to as “magic numbers”. I don’t even want to go into the gestalt of *that*.)


Thus, for example, programmers tend to think that if your program allows you to open multiple documents, it must allow you to open *infinitely* many documents (as memory allows), or at least 2^32, the only magic number programmers concede. A programmer would tend to look with disdain on a program which limited you to 20 open documents. What’s 20? Why 20? It’s not even a power of 2!


Another implication of *all n’s are equally likely* is that programmers have tended to think that if users are allowed to resize and move windows, they should have *complete* flexibility over where these windows go, right down to the last pixel. After all, positioning a window 2 pixels from the top of the screen is “equally likely” as positioning a window *exactly* at the top of the screen.


But it’s not true. As it turns out, there are lots of good reasons why you might want a window exactly at the top of the screen (it maximizes screen real estate), but there aren’t any reasons to leave 2 pixels between the top of the screen and the top of the window. So, in reality, 0 is much more likely than 2.


The programmers over at Nullsoft, creators of [WinAmp](http://www.nullsoft.com/), managed somehow to avoid the programmer-think that has imprisoned the rest of us for a decade. WinAmp has a great feature. When you start to drag the window *near* the edge of the screen, coming within a few pixels, it automatically *snaps* to the edge of the screen perfectly. Which is probably exactly what you wanted, since 0 is so much more likely than 2. (The Juno main window has a similar feature: it’s the only application I’ve ever seen that is “locked in a box” on the screen and cannot be dragged beyond the edge.)


You lose a little bit of flexibility, but in exchange, you get a user interface that recognizes that controlling the mouse precisely is hard, so why should you have to? This innovation (which every program could use) eases the burden of window management in an intelligent way. Look closely at your user interface, and give us all a break. Pretend that we are gorillas, or maybe smart orangutans, and we really have trouble with the mouse.
