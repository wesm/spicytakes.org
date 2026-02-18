---
title: "C:\ONGRTLNS.OSX"
date: 2009-10-07
url: https://daringfireball.net/2009/10/congrtlns-osx
slug: congrtlns-osx
word_count: 1812
---


## Or: There Is No Replacement for Creator Codes in Snow Leopard


Ignore, for the moment, the specific technical details of how creator codes work (or, perhaps better put, *worked*). What matters is the behavior they enabled, which was the ability for documents of the same type to open in different applications *by default*. A very common case: HTML files. For things like readmes and other files downloaded from the web intended to be *read* as rendered HTML content, yes, I want them to open in my web browser by default. But for “.html” files I’ve created myself, I want them to open in my text editor by default. That used to work; now, in Snow Leopard, it does not.


Launch Services is the subsystem of Mac OS X that determines which application will open a file by default. What I mean by “by default” is that you, the user, indicate that you want to open a file, without directly specifying which app you want it to open in. Most commonly, double-clicking a file in the Finder opens the document in its default handler.


Starting in Snow Leopard, these default file bindings are determined entirely by file name extensions; HFS+ creator codes, if present, are now ignored. The only way in Snow Leopard to set a document to open with an app other than the one that claims ownership of that document’s file name extension is to use the Finder’s Get Info window to make the assignment manually. Behind the scenes, this adds a “usro” resource to the document’s resource fork, the contents of which resource are *not* the app’s bundle identifier (e.g. “com.apple.TextEdit”) but rather a hard-coded string with the path to the app itself (e.g. “/Applications/TextEdit.app”).


That’s it — file name extensions and these “usro” resources are the only remaining ways to bind a file to an application. And, as [Chris Suter documents in this piece on his weblog](http://sutes.co.uk/2009/09/creator-codes-are-not-replaced.html), the only way to add such a resource to a file is by way of a *private* Launch Services API. Users can do it manually using the Finder’s Get Info window, but there is no supported public API developers can use to do this in third-party software (cf. [this thread on Apple’s Cocoa-Dev mailing list](http://lists.apple.com/archives/cocoa-dev/2009/Sep/msg01720.html) from two weeks ago).


Now, as for the actual technical details of type and creator codes, there’s no question that they’re dated. (Not as dated as file name extensions, though.) They date all the way back to the original Macintosh in 1984, a machine with 128 kilobytes of RAM which used 400 kilobyte floppy disks for storage. Every byte was precious, so type and creator codes (along with numerous other aspects of the original Mac OS) were implemented with concise but cryptic four-byte codes (“OSTypes”). As an aid to human readability, the four-byte codes were typically rendered as four-character MacRoman-encoded strings. Many of these strings are naturally mnemonic: The type code for a plain text file is “TEXT”, the type code for an application is “APPL”. I’ll bet you can guess the type code for JPEG files. Application creator codes were often cute: the Finder’s creator code is “MACS”; BBEdit, created by Rich Siegel, has the creator code “R*ch”.


But there’s only so much you can do with four bytes. There’s no good reason today to cram everything into four-byte codes (nor any good reason to use a single-byte text encoding for strings). Mac OS X 10.0 introduced a superior way to uniquely identify applications: bundle identifiers. Bundle identifiers like “com.apple.Safari” and “com.apple.iTunes” are more expressive, informative, and obvious than creator codes like “sfri” and “hook”.


So as John Siracusa pointed out in [his “Metadata Madness” piece](http://arstechnica.com/staff/fatbits/2009/09/metadata-madness.ars), there is no need for a new “replacement” for creator codes. The replacement is the bundle identifier, and it has been here since 2001. Every Mac app already has a unique bundle identifier. What is missing, though, is any supported way to associate a bundle identifier with an individual file to indicate which app created the file.


In the old type/creator code system, files were assigned to applications on an individual basis. In Snow Leopard, Launch Services only considers the file’s type, the type comes from the file name extension, and default bindings can only be managed between types and apps, rather than individual files and apps.


Snow Leopard, effectively, gives us the file-to-application binding policy of Windows 3.0.


## Interpolation Regarding Uniform Type Identifiers and Purported Claims That They ‘Fix’ Creator Codes


Each time I’ve linked to coverage elsewhere regarding Snow Leopard’s disavowal of creator codes, a few readers have kindly emailed me links to Daniel Eran Dilger’s piece on the topic, entitled “[Inside Snow Leopard’s UTI: Apple fixes the Creator Code](http://forums.appleinsider.com/showthread.php?s=&threadid=103219)”, assuming that the article proves what it claims. It does not. I off-handedly [referred to it as “blathering”](http://daringfireball.net/linked/2009/10/01/hosey-utis) last week, prompting several readers to ask why I’d say such a thing.


So, OK, I’ll bite.


The title of the piece claims “Apple fixes the Creator Code”. Then in the first paragraph:


> Instead, Apple has invented a superior alternative for the old
> Creator Code in order to support a variety of new features.
> Here’s why, and what the new Uniform Type Identifiers offer.


That sounds interesting, especially since [my understanding of UTIs](http://devworld.apple.com/mac/library/documentation/Carbon/Conceptual/understanding_utis/understand_utis_conc/understand_utis_conc.html) was that they do not in any way replace the functionality of creator codes.


Then come 2,900 words, none of which explain what was promised in the headline and first paragraph.


Then comes the penultimate paragraph, where Dilger writes:


> Users who miss being able to automatically open a file using the
> app that originally created it can pester their app’s developer to
> get on the ball with UTI. Any application that has been updated
> since 2005’s Tiger, but which does not yet support UTI, has opted
> not to support an important feature of the Mac platform.


This is simply flat-out wrong. There is nothing any developer can do, with UTIs or with any other supported technology, to restore the functionality of creator codes in Snow Leopard. It’s just wrong. UTIs indicate a file’s type, not the application in which it should open by default. Furthermore, developers can’t even directly assign UTIs to files. UTIs are derived from file name extensions.


And then we come to the very last paragraph:


> Everyone else, including many of us who didn’t ever understand why
> the system launched files using a specific app rather than the one
> we had defined for that given file type, can continue using the
> Finder’s Open With menu, drag and drop app launching, or set a
> permanent per-item default “creator” app for opening a selection
> of documents by using the Get Info panel.


So, after claiming at the outset that Apple has “fixed” creator codes by “inventing a superior alternative”, followed by 3,000 words of muddled technical information regarding a technology that is unrelated to binding files to applications, Dilger admits that there is no replacement for creator codes in Snow Leopard, but it’s good news anyway because he never liked the previous behavior in the first place. His closing paragraph is technically accurate, but is completely at odds with the article’s title and opening premise — unless he meant that Apple has “fixed” creator codes in the same sense that one “fixes” a dog.


People want to believe that Apple wouldn’t take out a popular feature and replace it with nothing, but that’s the plain truth.


## End of Interpolation, Back to the Main Point, Which, as a Gentle Post-Interpolation Reminder, Left Off With a Snide Remark About Snow Leopard’s File-to-Application Binding Policy Being Effectively the Same as That of Windows 3.0


Take a step back and consider that the term *creator code* itself shows just how different things are today. When the Mac was created, nearly all documents were proprietary binary file formats. The only app that could read MacWrite files was MacWrite, etc. Even when apps could read other apps’ file formats, they typically did so only through an import/export process. You could, say, import a Word document into ClarisWorks, but not by opening the file directly and writing back to it.


Today, on the other hand, many of the files we work with use common, open file formats: text files, JPEG and PNG graphics, MP3 audio, MP4 video, etc. When you double-clicked a MacPaint file in 1985, there was no question which app you wanted to open it: MacPaint. Today, though, there might be a dozen apps on your system that can open a JavaScript source code text file or an MP3 audio file. “The app that created it” can no longer be assumed to be the answer to the question “Which app would you prefer to open this file with by default?”


The situation is therefore far more complex today. One way Apple has dealt with this complexity is with the fairly-recent addition of the “Open With…” contextual menu in the Finder, which shows a list of apps that claim to be able to open files of the selected item’s type. And there’s always drag-and-drop.


The creator code long ago stopped meaning “the app that created the file”, and instead meant “the app this file should open with by default”. What matters is that the feature is now gone, not what it was called or what a hypothetical actual replacement in the future would be called.


And to be clear, the new binding policy in Snow Leopard is popular with many users. If you really want all files of the same type to open in the same app by default, then a system based exclusively on file name extensions works. Apple could have replaced creator codes with something superior, based on bundle identifiers, but they did not. And even if they plan to do so in the future,1 there is no good reason for dropping creator code support from Launch Services *now*, before the replacement arrives. The simple truth is that many people — including, obviously, at Apple — prefer binding files to applications exclusively through file name extensions.


“Make it a preference” is often (if not usually) the wrong way to solve a problem, but a case like this, where many people prefer/expect it one way and many prefer/expect it the other, is exactly the sort of situation that calls for a preference setting.


I could go on and rant about the inherent inelegance of storing two essential pieces of a file’s metadata, name and type, in a single field — shackling what Apple [proclaims](http://www.apple.com/macosx/) to be “the world’s most advanced operating system” to a metadata limitation of MS-DOS from 1981 — but there’s no use crying over spilled milk.


---

1. Don’t hold your breath. ↩︎



| **Previous:** | [Snow Leopard Adoption Rate](https://daringfireball.net/2009/09/snow_leopard_adoption_rate) |
| **Next:** | [Microsoft’s Competition for Windows 7](https://daringfireball.net/2009/10/microsofts_competition_for_windows_7) |


PreviousNext