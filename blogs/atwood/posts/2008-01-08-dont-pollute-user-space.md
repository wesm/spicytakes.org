---
title: "Don’t Pollute User Space"
date: 2008-01-08
url: https://blog.codinghorror.com/dont-pollute-user-space/
slug: dont-pollute-user-space
word_count: 617
---

What is user space? User space is the location in the filesystem where users put their personal files – their “stuff.” Here’s the user space folder structure in the **Windows XP** operating system:

kg-card-begin: html

```

Documents and SettingsUser
Application Data
Cookies
Desktop
Favorites
Local Settings
My Documents
My Music
My Pictures
My Recent Documents
NetHood
PrintHood
SendTo
Start Menu

```

kg-card-end: html

And here’s the user space folder structure in the **Windows Vista** operating system:

kg-card-begin: html

```

UsersUser
AppData
Local
Roaming
Contacts
Desktop
Documents
Downloads
Favorites
Links
Music
Pictures
Saved Games
Searches
Videos

```

kg-card-end: html

This new [Vista user space folder structure](https://web.archive.org/web/20080517012558/http://www.shahine.com/omar/MyDocumentsInVista.aspx) may seem oddly familiar to people using operating systems based on Unix. It gives new life to the [famous quote](https://web.archive.org/web/20080513143742/http://mailman.postel.org/pipermail/internet-history/2001-November/000068.html) “Those who do not understand Unix are condemned to reinvent it, poorly.” Regardless, I’m glad we no longer have to deal with a [scarily long default user path](https://blog.codinghorror.com/filesystem-paths-how-long-is-too-long/) – with aggravating embedded spaces, even – to our personal stuff. If a user is keeping notes in a text file, we can reasonably expect to find those notes at the following path:

kg-card-begin: html

```

Documents and SettingsUserMy Documentsnotes.txt
UsersUserDocumentsnotes.txt

```

kg-card-end: html

Now that we’ve established what and where user space is, I have a message for all the programmers reading this – including myself. **Keep your dirty, filthy paws out of my personal user space!**


Take a look in your `Documents` folder right now. Go ahead. Look. Do you see any files or folders in there that you personally did not create? If so, you’ve been victimized. Applications should never create or modify anything in *your* documents folder without *your* permission. And yet, sadly, it happens all the time. Applications, and more specifically, the programmers who wrote those applications, think it’s perfectly A-OK to carpet bomb your personal user space with their junk.


Well, it isn’t.


As Omar Shahine [originally pointed out](https://web.archive.org/web/20080413072955/http://www.shahine.com/omar/MyDocuments.aspx) almost two years ago, we should be mad as hell, and we shouldn’t take it any more. If applications need to store shared files, that’s what the `AppData` and `Application Data` folders are for. In OS X, which inherits a lot of filesystem conventions from BSD Unix, Apple has a great set of guidance appropriately titled [Don’t Pollute User Space](https://web.archive.org/web/20080724113840/http://developer.apple.com/documentation/MacOSX/Conceptual/BPFileSystem/Articles/WhereToPutFiles.html):


> It is important to remember that the user domain (`/Users`) is intended for files created by the user. With the exception of the `~/Library` directory, your application should never install files into the user’s home directory. In particular, you should never install files into a user’s `Documents` directory or into the `/Users/Shared` directory. **These directories should only be modified by the user.**
> Even if your application provides clip art or sample files that the user would normally manipulate, you should place those files in either the local or user’s  `Library/Application` Support directory by default. The user can  move or copy files from this directory as desired. If you are concerned about the user finding these files, you should include a way for the user to browse or access them directly from your application’s user interface.


Discovering this made me realize how much I missed the good old days of strict operating system and GUI conventions. Granted, Apple is cheating quite a bit by inheriting the well-worn conventions of classic Unix operating systems. But so much of Windows seems dangerously ad-hoc in comparison.


At any rate, it is our obligation as programmers to let the user’s folders belong to the user. Do the responsible thing and store your application files in an appropriate location, not as virtual litter amongst the user’s other files. Please **don’t pollute user space**.

[file management](https://blog.codinghorror.com/tag/file-management/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
