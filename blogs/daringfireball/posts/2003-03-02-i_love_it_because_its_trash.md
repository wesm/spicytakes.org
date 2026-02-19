---
title: "I Love It Because It’s Trash"
date: 2003-03-02
url: https://daringfireball.net/2003/03/i_love_it_because_its_trash
slug: i_love_it_because_its_trash
word_count: 2237
---


There’s a fascinating argument about the Mac OS X Finder.


It starts at Jonathan ‘Wolf’ [Rentzsch’s sparkling new weblog](https://web.archive.org/web/20030407084645/https://rentzsch.com/bugs/fileFolderOverwriteBug), where he classifies the following Mac OS X Finder behavior as a bug:


> Finder X, unlike Finder 9, allows the user to overwrite a folder
> 	with a file and vice-versa. You can reproduce this: 
> Create a new folder named “test”
> Elsewhere, create a file named “test”
> Drag file “test” over into folder “test”’s container.
> Finder X will warn “A newer item named “test” already exists in this
> 	location. Do you want to replace it with the older one you are moving?”
> 	with [Stop] [Replace] buttons.
> Finder 9 correctly would not allow the action at all. That is, it would
> 	put up a “stop” alert with one unconditional button: [OK]. 
> I accidentally deleted a folder filled with configuration files due to
> 	this bug, that **couldn’t occur under Mac OS 9**. The folder was called
> 	“EOGenerator”, and I was attempting to put the binary, “eogenerator”, next
> 	to its configuration folder. I became momentarily confused at the warning
> 	dialog, but reacted just in time to realize the mistake I had made.
> 	Fortunately, I have backups...


[Bill Bumgarner volleys back](http://radio.weblogs.com/0100490/2003/02/28.html#a415):


> I don’t get it.  Why is this a bug?   You wanted to stick something into a container where that container already contained something of the same name.   Why should it treat replacing a folder with a file of the same name (or vice-versa) any differently than replacing a folder with a folder or a file with a file?


To which Rentzsch responds, in depth, as an update at the bottom of his [original post](http://rentzsch.com/bugs/fileFolderOverwriteBug). It’s well-worth reading in its entirety, but too long to excerpt here. The gist of Rentzsch’s argument is this:

- The classic Mac OS Finder wouldn’t allow you to replace a same-named file with a folder, or vice-versa; it only allowed you to replace files with files, and folders with folders.
- With a basic understanding of Mac OS file system programming, it is easy to see that this was not a technical shortcoming of the old Finder, but instead a very deliberate design decision; the Finder had to go out of its way to prevent these actions.
- Since the old Finder’s restrictions were deliberate, there can only be two explanations:
  1. there were good UI-design reasons for these restrictions; or
  2. the designers of the old Finder were foolish, over-protective, or both.


Rentzsch votes for “a”. Bumgarner’s comments indicate he votes for “b”.


I see both sides. At the very least, I have to agree with Bumgarner that “bug” is not an accurate word to describe the problem. Both Finders are behaving exactly as designed. “Bug”, to me, implies a mistake.


But I agree with Rentzsch as well, that the restriction on replacing a file with a folder (or vice-versa) in the old Finder was a good decision.


I believe the reason the old Finder forbids these replacements is that there is a very high likelihood that such actions are mistakes. I’ve spent a lot of hours in front a computer, and I’ve moved and copied very many files over the years. But I can’t remember a single incident when I wanted to replace a same-named folder with a file, or vice-versa. Perhaps I have, and I’ve forgotten the circumstances, but at the very least it’s something that is done very rarely. Thus, because it’s rarely done, it’s not a significant annoyance that the old Finder requires you to perform both steps manually: trashing (or moving) the original item, then moving the item which you want to replace the original.


(My guess is that this is done so rarely that most of you never noticed it.)


The fact that the Finder allows you to replace same-named files with files, or folders with folders, is a shortcut. The idea is that this is something people need to do on a regular basis, and that it would be convenient to perform both steps (getting rid of the original, and moving the replacement item) in a single action.


If you really do want to replace a folder with a file, it’s not unreasonable to feel that the old Finder’s restriction is wasting a small amount of your time — that you know what you’re doing, and you want the same shortcut the Finder allows for replacing files with files. Thus Bumgarner’s opinion that the OS X Finder is correct to allow this.


The problem, as I see it, is that if such an action is a mistake (as was the case when Rentzsch encountered it), it is *catastrophic*. Yes, you get warned and need to explicitly allow the replacement by clicking a “Replace” button; but after you permit the Finder to replace the original item, it is *gone* — not moved to the Trash, but irrevocably deleted.


If you invoke Undo, the Finder will move the replacement item back to its previous location, but *it will not bring back the item that was deleted*. (Admittedly, that Undo works at all in the OS X Finder is a huge improvement over the old Finder, but it won’t help you here.)


So my argument is that no matter how much aggregate time you might save over the course of a lifetime by the current OS X Finder’s permission of such folder-for-file-or-vice-versa replacements, it will *never* add up to the time you will lose if you get screwed by inadvertently allowing it just once.


If you buy my argument, however, it leads to another conclusion: that the old Finder was wrong even to allow replacement of files with files, or folders with folders. Even though such actions are much more common than replacing files with folders, or folders with files, the destructive consequences of the action are too severe to permit.


Rentzsch comes to a similar conclusion (disproving the fallacious theory that those of us who believe the OS X Finder is seriously flawed always want it to behave exactly like the old Finder):


> Let me take it up a notch. **I think replacing a folder with a folder and a file with a file — *allowed in Finder 9* — shouldn’t be allowed as well**. Like [typing replaces selection](http://rentzsch.com/suck/typingReplacesSelection), it’s a **very dangerous convenience**. I believe the user should be forced to explicitly trash the original and put the replacement in the original’s previous location.


## Good Old Oscar


While the logic behind Rentzsch’s suggestion seems reasonable, I can’t quite bring myself to endorse it — mainly because I frequently use the Finder’s “replace a file with a same-named file” shortcut, and I’d miss it if it were gone.


I’ve decided not that both Rentzsch and Bumgarner are wrong, but that they’re *both right*. Bumgarner is right that the OS X Finder is correct to treat all “dragging one item to replace another same-named item” actions the same way; the old Finder’s behavior was inconsistent (albeit well-intentioned). Rentzsch is right that the Finder should not allow you to destroy an item simply by replacing it.


I believe there is a solution which should make everyone, Rentzsch and Bumgarner alike, very happy: *the Finder should move the replaced items to the Trash.*


The Trash was one of the biggest and best ideas in the original Macintosh. The concept of the Trash is simple, powerful, and obvious. Yes, the actual deletion of a file became a multi-step process, much to the derision of twitchy-fingered DOS and Unix command-line jockeys. But nearly 20 years later, all computers now ship with a Trash-like interface for file deletion. Why? Because the time lost by having to first move files to the Trash (or Recycling Bin, or what-have-you) and then invoke a separate “Empty Trash” command — as opposed to the way commands like `rm` and `del` nuke files instantly — is insignificant compared to how much time you will lose if you delete something important accidentally.


The Macintosh Trash almost completely solved the problem of people accidentally erasing files, a problem which, if you’re old enough to remember, was rampant on systems that lacked a Trash metaphor.


But the Finder doesn’t use the Trash when you *replace* a file, and never has. After permitting the replacement in the confirmation dialog, the original item is gone, deleted, nuked. What the Finder ought to do instead is move the original item to the Trash, then move the replacement to the new location. The confirmation dialog should be worded to indicate exactly what will happen if you click the Replace button. (The dialog should also be smart enough to use the words “file” and “folder”, when appropriate, instead of the lazy catch-all “item”; e.g. “An older *file* named ‘test’ already exists in this location...”, instead of “An older *item* named ‘test’...”.)


This solution solves both problems. It preserves the ability to replace one item with another in one action. But it doesn’t result in a file’s irrevocable deletion. With the original sitting in the Trash, it should be relatively easy for the Finder to make this a completely undo-able action.


## The Alias Problem


The only complication I can think of that would result from my proposal is alias resolution. Mac OS aliases are very clever — their primary means of tracking the item to which they point is by unique file reference IDs, not by hard-coded path. This means if you create an alias that points to a file named “test”, and then you move the original file to a different folder on the same volume, the alias still points to that file. However, if an alias can’t be resolved this way (such as if the original file no longer exists), the [Alias Manager](https://web.archive.org/web/20040407033156/http://developer.apple.com/documentation/Carbon/Reference/Alias_Manager/index.html) will then use a path to try to find another item of the same name in the same location.


So, as it stands today in both the OS 9 and OS X Finders, if you replace a file named “test” with another file named “test”, an alias that used to point to the original will now point to the replacement, because after the Alias Manager fails to find the original by file reference, it will find the new replacement by path name.


With my suggestion that replaced items be moved to the Trash instead of deleted, this poses a problem. Aliases pointing to the original item will resolve to point to the original item in the Trash, not the replacement in the original location. If you empty the Trash first, there won’t be a problem, but the whole point of the Trash is that you’re allowed to keep items sitting inside it. I think this might be solvable by adding some smarts to the Alias Manager, such that if an alias’s target is in the Trash *and* there is a newer item in the original location, it could reassign the alias to the new item.


Also, after writing the above, it occurs to me that the rules of alias resolution could be used to call into question the OS X Finder’s allowance of folder-for-file replacement. To wit:

1. Create a file named “test”. Let’s say it’s a GIF file owned by Preview.
2. Create an alias that points to “test”. The alias’s icon looks like a Preview GIF file.
3. Drag a folder named “test” to the same location as the original “test” file. Tell the Finder it’s OK to replace it.
4. Note that the alias created in step 2 still looks like a Preview document. But if you open it, you will see that it now points to the folder named “test” which replaced the file named “test”.


This is clearly wrong. At the very least, you’d have to consider this a cosmetic bug, in that the alias’s icon doesn’t change to represent its new target. But it could also be argued that it’s an indication the OS X Finder engineers didn’t thoroughly consider the ramification of allowing a file to be replaced by a folder.


## Why Not?


Alias resolution hiccups notwithstanding, it seems to me this is an obvious solution to the problem. So obvious that it made me wonder why the Finder hasn’t always worked like this.


One reason could be that I’m missing some obvious reason why my suggestion is in fact unworkable. Wouldn’t be the first time.


The only other reason I can think of, however, is that until recently, disk space was a scarce commodity. The original Macintosh was *floppy-based*, so each byte on a disk was precious real estate. Disk space was so scarce until the mid-90’s that it wasn’t unusual for many disks to be filled to near-capacity. Thus, there often wasn’t room to replace one file with another without deleting the original. If the Finder would have tried moving the original to the Trash first, in many cases you would have had to empty the Trash immediately just to make room for the replacement, which would have defeated the whole point of my suggestion, not to mention deleting any other files which happened to be sitting in the Trash at the time.


This is not a problem today. Most people have plenty of disk space to spare. I think we can use some of this disk space to make file replacement non-destructive.



| **Previous:** | [Not Dead Yet](https://daringfireball.net/2003/03/not_dead_yet) |
| **Next:** | [Aliasing](https://daringfireball.net/2003/03/aliasing) |


PreviousNext