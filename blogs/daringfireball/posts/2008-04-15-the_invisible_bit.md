---
title: "The Invisible Bit"
date: 2008-04-15
url: https://daringfireball.net/2008/04/the_invisible_bit
slug: the_invisible_bit
word_count: 753
---


I helped a friend today with a seemingly baffling problem: he could see the files and folders on his desktop (i.e. the icons you see when all windows are closed or hidden), but he couldn’t see the “Desktop” folder itself in his home folder. Ends up, somehow, the folder had been made invisible.


There are a two supported ways1 to mark files as “invisible” on the Mac:

- Start the file or folder name with a dot (e.g. “.like_this”). This is a Unix convention.
- Toggle the HFS+ invisible bit for the file or folder. This is the Mac convention.


The invisible bit is metadata. In the same way that every file and folder has metadata such as created and modified dates, it has a boolean “invisible” bit. Files marked invisible are still readable and writable, they just don’t show up in the Finder or in Open and Save dialogs. Invisibility is not inherited by the contents of an invisible folder, which explains why my friend could see the files on his desktop, but couldn’t see the “Desktop” folder itself in his home folder.


One place where the HFS+ invisible bit is not honored is the terminal — the `ls` command lists files and folders regardless of the state of their invisible bits. (The `ls` command *does* honor the Unix dot-file convention, though; such files are suppressed unless you use the -a or -A options.)


I’m not aware of any software that ships by default with Mac OS X that lets you see or set the HFS+ invisible bit. [See update below.] If you install the (free) developer tools, though, you can use the `GetFileInfo` and `SetFile` utilities.


For example, to check your Desktop folder:


```
$ GetFileInfo ~/Desktop
directory: "/Users/gruber/Desktop"
attributes: avbstclinmedz
created: 03/30/2008 18:25:34
modified: 04/15/2008 18:55:14

```


(The first line is what you type at the command line in Terminal; the next four lines are the results.) The [`GetFileInfo` man page](http://devworld.apple.com/DOCUMENTATION/Darwin/Reference/ManPages/man1/GetFileInfo.1.html) explains the “attributes” line: each letter represents an HFS+ metadata attribute. A lowercase letter means the attribute is off/false, an uppercase letter means the attribute is on/true. “V” is the letter for the invisible bit, so, because it’s lowercase in the example output, we can see that the “Desktop” folder is not invisible.


To make the file invisible:


```
$ SetFile -a "V" Desktop/

```


Then:


```
$ GetFileInfo ~/Desktop
directory: "/Users/gruber/Desktop"
attributes: aVbstclinmedz
created: 03/30/2008 18:25:34
modified: 04/15/2008 18:55:14

```


Note that toggling the invisible bit does not change the folder’s modified date.


Better, for most users, is to use a good file info utility such as [Bare Bones Software’s Super Get Info](http://www.barebones.com/products/super/). Just drag a file or folder onto Super Get Info’s icon and you get a nice window showing most of the metadata associated with the item. Invisibility is indicated with a checkbox. Invisible items pose an obvious problem, of course, in that if you can’t see them, you can’t drag them. Super Get Info solves this with its File → Open Hidden command, which brings up an Open dialog box that lists every item in the file system.


---


**Update:** Starting with Leopard, the [`chflags` command](http://www.devworld.apple.com/DOCUMENTATION/Darwin/Reference/ManPages/man1/chflags.1.html) now supports “hidden” and “nohidden” options to toggle invisibility:


```
$ chflags hidden ~/Desktop

```


On HFS+ volumes, this toggles the invisible bit, just like with `SetFile`.2  Also, you can use the “-lO” (lowercase *L* and capital *O*) options with the `ls` command to include file flags in the output; invisible files will be marked as “hidden”.


---

1. There’s also a third way, which is now deprecated. Prior to Mac OS X 10.4, there was a file named “.hidden” (which, because of the leading dot, was itself invisible) at the root level of the boot volume. This file contained a list of files and folders that were to be considered invisible. By default, it included the underpinnings of the OS, like the kernel (*/mach_kernel*) and the BSD Unix-y directories such as */bin*, */usr*, etc. Starting with 10.4, these files and folders are instead marked as invisible using the HFS+ invisible bit. But [according to this](https://web.archive.org/web/20080829201004/http://www.westwind.com/reference/OS-X/invisibles.html), a */.hidden* file, if present, is still honored. ↩︎
2. One difference between `SetFile` and `chflags` is that on *non*-HFS+ volumes, `SetFile` will create a ._*filename* file to contain the metadata; `chflags` won’t. This means `SetFile` can mark files as invisible even on non-HFS+ volumes. ↩︎



| **Previous:** | [How Much Money Does Apple Get From Google?](https://daringfireball.net/2008/04/apple_google_money) |
| **Next:** | [The Unsatisfying State of Twitter Web Clients for the iPhone](https://daringfireball.net/2008/04/twitter_web_clients_for_the_iphone) |


PreviousNext