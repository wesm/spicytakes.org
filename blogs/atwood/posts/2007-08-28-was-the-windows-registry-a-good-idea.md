---
title: "Was The Windows Registry a Good Idea?"
date: 2007-08-28
url: https://blog.codinghorror.com/was-the-windows-registry-a-good-idea/
slug: was-the-windows-registry-a-good-idea
word_count: 783
---

One of the hot new features introduced with Windows 95 was the [Windows Registry](http://en.wikipedia.org/wiki/Windows_Registry). The Windows Registry offered a centralized database-like location to store application and system settings. No more plain text .INI files splattered all over your system. Instead, issue a few easy API calls and your application settings are safely nestled away deep inside the registry hive.


But after living with the Windows Registry for more than a decade, **I’m starting to wonder if we were better off with those .INI files**.


![Windows Registry Editor, [X]](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b012877700d3d970c-pi.png)


I understand the need to store truly system-wide settings in one place. Let the operating system store settings however it deems fit. The real problem with the registry is that it was exposed to the outside world. Instead of being a secure, central hive for only the most essential and global settings, over time the registry has slowly become **a trash heap of miscellaneous junk settings for every rinky-dink application on the planet**.


Woe to the poor computer user who naively attempts to manipulate the filesystem without first supplicating to the Registry Gods. Manipulating the filesystem is utterly obvious, completely intuitive, and unfortunately also the fastest way to break an application in Windows. You have to reconcile almost everything you do in the filesystem with that opaque, unforgiving binary blob of data known as the Windows Registry.


For instance, when I upgrade and reinstall Windows, most of the games I have installed on my secondary drive are instantly broken because they store cd-key and (redundant) path information in the registry. The game vendors’ support teams will tell you to reinstall all your games and patches. Personally, I’d rather search forums and spelunk through the registry to manually recreate the two or three registry keys the game is looking for.


My life would be a heck of a lot easier if per-application settings were stored in a place I could easily see them, manipulate them, and back them up. Like, say... in INI files.


There is an alternative, though. If Windows applications weren’t so busy mindlessly piling all their settings on the registry garbage dump with everyone else, they *could* elect to follow the new, much saner Windows Vista conventions for storing application-specific data:

kg-card-begin: html

```
/Users/Jeff/AppData/Local
/Users/Jeff/AppData/LocalLow
/Users/Jeff/AppData/Roaming

```

kg-card-end: html

**Local** and **LocalLow** are for bits of application data that are truly machine-specific. **Roaming** is for non-machine specific settings that will follow the user. That’s where the lion’s share of the application settings will be. It’s all explained in the [Roaming User Data Deployment Guide](https://web.archive.org/web/20081027080705/http://download.microsoft.com/download/3/b/a/3ba6d659-6e39-4cd7-b3a2-9c96482f5353/Managing%20Roaming%20User%20Data%20Deployment%20Guide.doc) (Word doc). However, these are still user-specific settings, obviously, as they’re under the `/Users` folder. I can’t find any new Windows filesystem convention for system level, non-user-specific settings. I suppose that’s still Ye Olde Registry by default.


It is possible to write Windows applications that don’t use the registry in any way. These are some of my favorite applications. But they’re also the most rare and precious of all applications in the Windows software ecosystem.


Over time, it’s fair to say that **I’ve grown to hate the Windows Registry**. How do I hate it? [Let me count the ways](http://en.wikipedia.org/wiki/Windows_Registry#Disadvantages):

- The registry is a **single point of failure**. That’s why every single registry editing tip you’ll ever find starts with a big fat screaming disclaimer about how you can break your computer with regedit.
- The registry is **opaque and binary**. As much as I dislike [the angle bracket tax](https://blog.codinghorror.com/are-you-an-xml-bozo/), at least XML config files are reasonably human-readable, and they allow as many comments as you see fit.
- The registry has to be **in sync with the filesystem**. Delete an application without “uninstalling” it and you’re left with stale registry cruft. Or if an app has a poorly written uninstaller. The filesystem is no longer the statement of record – it has to be kept in sync with the registry somehow. It’s a total violation of [the DRY principle](https://blog.codinghorror.com/curlys-law-do-one-thing/).
- The registry is **monolithic**. Let’s say you wanted to move an application to a different path on your machine, or even to a different machine altogether. Good luck extracting the relevant settings for that one particular application from the giant registry [tarball](https://blog.codinghorror.com/customization-the-software-tar-baby/). A given application typically has dozens of settings strewn all over the registry.


What’s depressing about all of this is how prescient the UNIX conventions are in retrospect. How many billions of man-hours could we have saved by now if some early Windows NT 3.0 or 3.5 developers had decided to turn off public access to the registry, and transparently redirected the public registry API calls so they followed simpler, UNIX-like filesystem storage conventions instead?

[windows registry](https://blog.codinghorror.com/tag/windows-registry/)
[system settings](https://blog.codinghorror.com/tag/system-settings/)
[api calls](https://blog.codinghorror.com/tag/api-calls/)
[.ini files](https://blog.codinghorror.com/tag/ini-files/)
[application settings](https://blog.codinghorror.com/tag/application-settings/)
