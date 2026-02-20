---
title: "Inno Setup + Excelsior JET = Slice MBs Off Download"
date: 2009-01-23
url: https://www.kalzumeus.com/2009/01/23/inno-setup-excelsior-jet-slice-mbs-off-download/
slug: inno-setup-excelsior-jet-slice-mbs-off-download
word_count: 635
---


If you’ve been following the blog recently you know I’m running a split test on a self-contained executable (made with [Excelsior JET](http://www.excelsior-usa.com/)) versus my standard wrapped JAR (made with [Launch4j](http://launch4j.sourceforge.net/), requires Java installed).  The idea is to see whether the tradeoff of vastly increased download size of the native version makes up for eliminating the Java dependency.  Launch4j will prompt people to download Java if they don’t have a sufficient version installed, but that is one of those decision points where people might stop using the app.


Previously, the approximate size difference was 13 MB versus about 1 MB.  However, with a little help from Dmitry over at Excelsior, I was able to shave 4.5 MB off of the installer for the native version.  Here’s what I did:


1)  Used the detached package option, described at “Java Runtime Slim-Down” in the User’s Guide.


2)  I removed all of the packages which were given the green light to remove — this included Cobra, Management, XML, and all that enterprise-y cruft for my application.  Packages which get the green light are always safe to nix.


3)  Then I made a judgement call about packages which got the red light.  Red light means they’re referenced in some code included in your program but, importantly, if they’re never actually loaded you’re in the clear.  I was pretty sure I could nix the JSound and RMI packages, as I don’t use either and I have a very good idea of what my 3rd party libraries needed (certainly not access to the sound card).


The JET packager thing gives you a test option so that you can actually run through your program and see if you end up needing the detached packages.  If you do, they’re downloaded at need from your website (you get to upload them yourself).  I would strongly prefer avoiding that, so I stepped through all my functionality to make sure it didn’t fire a download.


4)  I used the “deploy as a self-contained folder” option, which let me copy/paste BingoCardCreator.exe and the rt/ folder produced by JET and move them into my folder for InnoSetup to take a stab at.


5)  I used the same InnoSetup script I use for the regular (Java-using version), making sure to modify it so that the rt/ directory was included in the installer and removed by the uninstaller.  This worked fine, functionally, but 13 MBs is a lot.


6)  Dmitry got in touch with me and told me that they have a tool which compresses a particular JAR file that the JET deployment comes with, much much more efficiently than the ZIP algorithm can compress it.  So if you fire that tool once on your system, and then once at install time (to uncompress it), you can save quite a bit of space.  So I packed up the JAR on my system, and then edited my InnoSetup script to call the unpacker right before exiting setup.  Easy peasy.  I can barely tell the difference in install times, but slimming the download 4 MB is easily worth it.


**How To Pack The Jar (assuming you detached packages): **


cd C:\some\path\to\distribution\directory\rt\lib


c:\jet\directory\goes\here\profile{use tab complete}\jre\bin\pack200 -g rt-0.jar.pack rt-0.jar


As long as we’re at it, you can take a gander at my [Inno Setup script](http://pastie.org/368973) if you want.  It is no great shakes but it might help you if you want an example of the whole picture at once.  Feel free to create derivatives from it if that saves you time.  (You’ll note that it is optimized largely to remove as many screens from the installer as I possibly can — no asking where to install, no asking whether to deposit shortcuts or not, etc.  I have non-technical users and don’t want to fatigue them with decisions that they’re largely not qualified to make anyway.)
