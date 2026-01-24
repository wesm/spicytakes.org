---
title: "Setting up Subversion on Windows"
date: 2008-04-05
url: https://blog.codinghorror.com/setting-up-subversion-on-windows/
slug: setting-up-subversion-on-windows
word_count: 1429
---

When it comes to readily available, free source control, I don’t think you can do better than [Subversion](https://web.archive.org/web/20080312035657/http://subversion.tigris.org/) at the moment. I’m not necessarily *advocating* Subversion; there are plenty of other great source control systems out there – but few can match the ubiquity and relative simplicity of Subversion. Beyond that, source control is source control, as long as you’re [not using Visual SourceSafe](https://blog.codinghorror.com/source-control-anything-but-sourcesafe/). And did I mention that Subversion is... free?


Allow me to illustrate how straightforward it is to **get a small Subversion server and client going on Windows**. It’ll take all of 30 minutes, tops, I promise. And that’s assuming you read slowly.


The first thing we’ll do is download the [latest Subversion Windows binary installer](https://web.archive.org/web/20080312035657/http://subversion.tigris.org/). At the time of writing, that’s 1.46. I recommend overriding the default install path and going with something shorter:

kg-card-begin: html

```

c:svn

```

kg-card-end: html

Note that the installer adds `c:svnbin` to your path, so you can launch a command prompt and start working with it immediately. Let’s create our first source repository, which is effectively a system path.

kg-card-begin: html

```

svnadmin create “c:svnrepository”

```

kg-card-end: html

Within that newly created folder, uncomment the following lines in the **conf/svnserve.conf** file by removing the pound character from the start of each line:

kg-card-begin: html

```

anon-access = none
auth-access = write
password-db = passwd

```

kg-card-end: html

Next, add some users to the **conf/passwd** file. You can uncomment the default harry and sally users to play with, or add your own:

kg-card-begin: html

```

harry = harryssecret
sally = sallyssecret

```

kg-card-end: html

As of Subversion 1.4, you can easily **install Subversion as a Windows service**, so it’s always available. Just issue the following command:

kg-card-begin: html

```

sc create svnserver binpath= “c:svnbinsvnserve.exe –service -r c:svnrepository”
displayname= “Subversion” depend= Tcpip start= auto

```

kg-card-end: html

It’s set to auto-start so it will start up automatically when the server is rebooted, but it’s not running yet. Let’s fix that:

kg-card-begin: html

```

net start svnserver

```

kg-card-end: html

Note that the service is running under the **Local System account**. Normally, this is OK, but if you plan to implement any Subversion hook scripts later, you may want to switch the service identity to an Administrator account with more permissions. This is easy enough to do through the traditional Windows services GUI.


![](https://blog.codinghorror.com/content/images/2025/04/image-56.png)


Now let’s verify that things are working locally by adding a root-level folder in source control for our new project, aptly named **myproject**.

kg-card-begin: html

```

set SVN_EDITOR=c:windowssystem32notepad.exe
svn mkdir svn://localhost/myproject

```

kg-card-end: html

It’s a little weird when running locally on the server, as Subversion will pop up a copy of Notepad with a place for us to enter commit comments. Every good programmer *always* comments their source control actions, right?


![](https://blog.codinghorror.com/content/images/2025/04/image-55.png)


Enter whatever comment you like, then save and close Notepad. You’ll be prompted for credentials at this point; ignore the prompt for Administrator credentials and press enter. Use the credentials you set up earlier in the `conf/passwd` file. If everything goes to plan, you should be rewarded with a “committed revision 1” message.

kg-card-begin: html

```

svn mkdir svn://localhost/myproject
Authentication realm: <svn://localhost:3690>
Password for ‘Administrator’: [enter]
Authentication realm: <svn://localhost:3690>
Username: sally
Password for ‘sally’: ************
Committed revision 1.

```

kg-card-end: html

Congratulations! You just checked your first change into source control!


We specified `svn://` as the prefix to our source control path, which means we’re using the native Subversion protocol. The **Subversion protocol operates on TCP port 3690**, so be sure to poke an appropriate hole in your server’s firewall, otherwise clients won’t be able to connect.


Now that the server’s good to go, let’s **turn our attention to the client**. Most people use [TortoiseSVN](http://tortoisesvn.net/) to interact with Subversion. Download the latest [32-bit or 64-bit Windows client](https://tortoisesvn.net/downloads.html) (1.4.8.12137 as of this writing) and install it. The installer will tell you to reboot, but you don’t have to.


Now create a project folder somewhere on your drive. I used `c:myproject`. Tortoise isn’t a program so much as a shell extension. To interact with it, you right click in Explorer. Once you’ve created the project folder, right click in it and select “SVN Checkout...”


![](https://blog.codinghorror.com/content/images/2025/04/image-54.png)


Type `svn://servername/myproject/` for the repository URL and click OK.


![](https://blog.codinghorror.com/content/images/2025/04/image-53.png)


Tortoise now associates the `c:myproject` folder with the  `svn://servername/myproject` path in source control. Anything you do on your local filesystem path (well, most things – there are some edge conditions that can get weird) can be checked back in to source control.


There’s a standard convention in Subversion to start with the “TTB folders” at the [root of any project](http://svnbook.red-bean.com/en/1.4/svn.reposadmin.planning.html):


> Because Subversion uses regular directory copies for branching and tagging (see [Chapter 4, Branching and Merging](http://svnbook.red-bean.com/en/1.4/svn.branchmerge.html)), the Subversion community recommends that you choose a repository location for each project root – the “top-most” directory which contains data related to that project – and then create three subdirectories beneath that root: **trunk**, meaning the directory under which the main project development occurs; **branches**, which is a directory in which to create various named branches of the main development line; **tags**, which is a collection of tree snapshots that are created, and perhaps destroyed, but never changed.


Of course, none of this means your developers will actually *understand* [branching and merging](https://blog.codinghorror.com/software-branching-and-parallel-universes/), but as responsible Subversion users, let’s dutifully add the TTB folders to our project. Note that we can batch up as many changes as we want and check them all in atomically as one unit. Once we’re done, right click the folder and select “SVN Commit...”


![](https://blog.codinghorror.com/content/images/2025/04/image-52.png)


In the commit dialog, indicate that yes, we do want to check in these files, and we *always* enter a check in comment – right? right?


![](https://blog.codinghorror.com/content/images/2025/04/image-51.png)


You’ll have to enter your server credentials here, but Tortoise will offer to conveniently cache them for you. Once the commit completes, note that the files show up in the shell with source control icon overlays:


![](https://blog.codinghorror.com/content/images/2025/04/image-50.png)


And now we’re done. Well, almost. There are a few settings in Tortoise you need to pay special attention to. Right click and select “TortoiseSVN, Settings.”

1. See that hidden “.svn” folder? These folders are where Subversion puts its hidden metadata schmutz so it can keep track of what you’re doing in the local filesystem and resolve those changes with the server. The default naming convention of these folders unfortunately conflicts with some fundamental ASP.NET assumptions. If you’re an ASP.NET 1.x developer, you need to switch the hidden folders from **“.svn” to “_svn” format**, which is on the General options page. This hack is [no longer necessary](http://blog.dotsmart.net/2008/02/19/moving-on-from-svn_asp_dot_net_hack/) in ASP.NET 2.0 or newer.
2. I’ll never understand why, but by default, Tortoise tries to **apply source control overlays across every single folder and drive on your system**. This can lead to some odd, frustrating file locking problems. Much better to let Tortoise know that it should *only* work its shell magic on specific folders. Set this via “Icon Overlays”; look for the exclude and include paths. I set the exclude path to everything, and the include path to only my project folder(s).


![](https://blog.codinghorror.com/content/images/2025/04/image-49.png)


Unfortunately, since Tortoise is a shell extension, setting changes may mean you need to reboot. You can try terminating and restarting explorer.exe, but I’ve had mixed results with that.


And with that, we’re done. **You’ve successfully set up a Subversion server and client**. A modern client-server source control system inside 30 minutes – not bad at all. As usual, this is only intended as the gentlest of introductions; I encourage you to check out the [excellent Subversion documentation](http://svnbook.red-bean.com/) for more depth.


I find Subversion to be an excellent, modern source control system. Any minor deficiencies it has (and there are a few, to be clear) are more than made up by its ubiquity, relative simplicity, and robust community support. In the interests of equal time, however, I should mention that some influential developers – most notably [Linus Torvalds](http://www.youtube.com/watch?v=4XpnKHJAok8) – ***hate* Subversion and view it as an actual evil**. There’s an emerging class of [distributed revision control](http://en.wikipedia.org/wiki/Distributed_revision_control) that could eventually supersede existing all the centralized source control systems like Subversion, Vault, Team System, and Perforce.


I’m skeptical. I’ve met precious few developers that really understood the versioning concepts in the simple centralized source control model. I have only the vaguest of hopes that these developers will be able to wrap their brains around the *vastly* more complicated and powerful model of distributed source control. It took [fifteen years](https://blog.codinghorror.com/fifty-years-of-software-development/) for centralized source control usage to become mainstream, so a little patience is always advisable.

[version control](https://blog.codinghorror.com/tag/version-control/)
[subversion](https://blog.codinghorror.com/tag/subversion/)
[windows](https://blog.codinghorror.com/tag/windows/)
[source control](https://blog.codinghorror.com/tag/source-control/)
[setup](https://blog.codinghorror.com/tag/setup/)
