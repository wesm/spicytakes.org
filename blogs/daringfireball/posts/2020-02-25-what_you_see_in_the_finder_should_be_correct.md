---
title: "What You See in the Finder Should Always Be Correct"
date: 2020-02-25
url: https://daringfireball.net/2020/02/what_you_see_in_the_finder_should_be_correct
slug: what_you_see_in_the_finder_should_be_correct
word_count: 786
---


Last week Marco Arment [tweeted this screenshot of a glitch/bug in the Finder on Catalina](https://twitter.com/marcoarment/status/1229892483812921344): he selected a folder full of multi-hundred megabyte files and the Inspector panel showed the folder size as “Zero KB”.1


Clearly that’s wrong. I know from talking to Arment privately that about 30 seconds after he took the screenshot, the Inspector updated to show the actual folder size. But that’s still *very* wrong. The Finder should *never* show inaccurate information regarding the state of the file system. Never.


This is the sort of problem in recent versions of MacOS that clearly isn’t getting enough attention within Apple. John Moltz and I discussed this on [yesterday’s episode of my podcast](https://daringfireball.net/thetalkshow/2020/02/24/ep-277), and Moltz mentioned a similar problem I’ve seen too: you put some large files in the Trash, then empty the Trash, and the available space shown in Finder windows (View → Show Status Bar) *doesn’t change at all* for an indeterminate amount of time.


This is terribly wrong. Everything the Finder displays should be correct all the time. If, for some technical reason, it doesn’t know the size of something and needs to wait, it should show a spinner or some other indicator that you, the user, need to wait to get the information. The actual file size of a folder is what you want to see, and ideally you should see it as soon as you ask for it. But a spinner, if the system needs time to calculate the size, is still *correct* — it’s correctly showing you that you need to wait. But the Finder should *never* show the wrong number for a file or folder size.


Obviously, the actual integrity of the file system is the most important factor here. It’s reasonable to say that the integrity of the file system is the single most important responsibility of any operating system. *Do not corrupt or lose data.* And by all evidence, the [APFS file system](https://developer.apple.com/documentation/foundation/file_system/about_apple_file_system) is exemplary in that regard. Apple treats the actual integrity of the file system with the utmost attention that it deserves.


But the visual representation of the file system in the user interface should be treated with almost the same amount of attention. This is how users *see* the file system. Showing “Zero KB” for a folder full of large files, or having the available disk space not change at all after emptying the Trash when it was full of very large files, is profoundly wrong. It creates mistrust in an aspect of the system that the user should, ideally, trust completely.


Consider your bank account. The most important job of your bank is to maintain the integrity of the actual amount of money in your account. But if you log into your account and it shows a balance of “Zero dollars” for 30 seconds before updating to show your actual balance — or, say, if you make a large withdrawal (like emptying the Trash) and the “available balance” doesn’t change — well, you’re probably going to start looking for a new bank. Even if your bank hasn’t *actually* misplaced a single penny, it’s a real problem if it *looks* like they have.


The Finder should treat every bit of information it displays as though it’s as important as your bank account balance.2


---

1. Here’s a fun tip you might not know. The Finder has a File → Get Info menu command with default shortcut ⌘I. This opens a regular window displaying information about the currently selected item(s). But if you hold down the Option key, File → Get Info changes to Show Inspector (and the shortcut, of course, is ⌘⌥I). The Inspector is very similar to the Get Info window, but it’s a floating palette window, and instead of statically showing info for whatever was selected when you invoked it (which is how the standard Get Info window works), the Inspector dynamically changes as you select different items in the Finder. ↩︎
2. It used to, for decades. I can’t recall the classic Mac OS Finder *ever* showing incorrect file sizes. You did have to wait sometimes — often quite a while, because spinning disks were slow (especially floppies, if you want to go back that far) and HFS wasn’t efficient for computing folder sizes. But while waiting for a folder size to compute, you’d see a spinner, and in list view with folder sizes turned off, you’d see “--” as the folder size, not “0”. I don’t recall Finder info ever being incorrect in the early years of Mac OS X either.
Something went awry in this regard in recent years. ↩︎︎



| **Previous:** | [Locations of Media Files in MacOS 10.15 Catalina](https://daringfireball.net/2020/02/catalina_media_file_locations) |
| **Next:** | [Tot](https://daringfireball.net/2020/02/tot) |


PreviousNext