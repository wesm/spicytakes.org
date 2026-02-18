---
title: "Getting the Size of Your Display With AppleScript, the Lazy Way"
date: 2006-12-16
url: https://daringfireball.net/2006/12/display_size_applescript_the_lazy_way
slug: display_size_applescript_the_lazy_way
word_count: 579
---


So I had this idea for an AppleScript to neatly resize and arrange all my open web browser windows. I want each window sized to 1024 pixels wide, and to the full height of my display, with the first window positioned near the left edge of the screen, and each subsequent window stacked about 20 pixels to the right of the previous one. Here’s a [screenshot of my desktop](http://flickr.com/photos/gruber/323448584/) showing what I mean.


The tricky part in writing a script to do this is determining the height of the screen. (Or the width, for that matter, if I wanted to do something to make sure all the windows fit on screen, no matter how many there are.) I wasn’t aware of any way to obtain the size of the screen using AppleScript. I could hard code a size into the script, but the main reason I wanted to write the script in the first place is that I switch between my 20-inch Cinema Display and the built-in display of my 15-inch PowerBook, which (the switching) can leave browser windows in weird sizes. I want the same script to work with both displays.


My friend [Craig Hockenberry](http://iconfactory.com/home/staff) — crackerjack programmer at The Iconfactory — had a solution:


```
tell application "Finder"
    get bounds of window of desktop
end tell

```


This returns a list of four integers: the x and y coordinates of the top left and bottom right corners of the desktop. E.g. with my Cinema Display, it returns:


```
{0, 0, 1680, 1050}

```


So to get the width and height of the display:


```
tell application "Finder"
    set _b to bounds of window of desktop
    set _width to item 3 of _b
    set _height to item 4 of _b
end tell

```


(The leading underscores are something I’ve started using in my AppleScript variable names to make them easily distinguishable from terms in scripting dictionaries; think of them sort of like Perl’s [sigils](http://en.wikipedia.org/wiki/Sigil_(computer_programming)).)


The problem with this technique is that if you’re using multiple displays, it still just returns four coordinates. The “desktop” is conceptually one big rectangle encompassing all active displays. For example, if I enable both my Cinema Display (1680⁠ ⁠×⁠ ⁠1050) and my PowerBook display (1440⁠ ⁠×⁠ ⁠960), and arrange them (in the Displays panel of System Prefs) like this:


then the rectangle returned by the script is:


```
{0, 0, 3120, 1050}

```


With this arrangement:


you get:


```
{-1440, 0, 1680, 1050}

```


The first number is negative because the origin (0, 0) of the coordinate system is the top left corner of the main display — the one with the menu bar. Which means that with the secondary screen on the left, the top left corner of the desktop is at (-1440, 0).


And if you arrange your displays like this:


you get the seemingly enormous:


```
{0, 0, 3120, 2010}

```


So, in short, asking the Finder for the `bounds of window of desktop` works great if there’s just one display. If you need information about the dimensions of each display in a multiple display setup, you’ll need to find another technique.


**Update, 22 April 2012:** Shane Stanley’s free [ASObjC Runner](http://www.macosxautomation.com/applescript/apps/runner_vanilla.html) makes it even easier to get the display dimensions from AppleScript, and, even better, offers full support for multiple display setups.



| **Previous:** | [The Iniquities of the Selfish](https://daringfireball.net/2006/12/iniquities_of_the_selfish) |
| **Next:** | [I Sold My App Through MacHeist and All I Got Was This Lousy T-Shirt](https://daringfireball.net/2006/12/macheist_lousy_tshirt) |


PreviousNext