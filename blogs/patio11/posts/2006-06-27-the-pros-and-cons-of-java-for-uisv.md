---
title: "The Pros and Cons of Java for uISV"
date: 2006-06-27
url: https://www.kalzumeus.com/2006/06/27/the-pros-and-cons-of-java-for-uisv/
slug: the-pros-and-cons-of-java-for-uisv
word_count: 630
---


My application is developed in Java, a decision I made with some trepidation.  Lets start with the reasons people generally give to be afraid:

- Java requires a seperate runtime from the application itself.  Most of the Internet does not have a JRE installed, and roughly half of the installed JRE base is the ancient MS 1.1 which is a pain to code for.
- Java is *slow*.
- Java applications are ungainly, ugly monsters.  Especially the Swing apps.


Here are the counterbalancing points in Java’s favor:

- Despite the flaws in “write once, debug everywhere”, Java is still one of the easiest ways to quickly port a desktop application.
- Java can quickly deliver a professional looking GUI.
- Java’s best IDEs are free, along with everything else you need to get your application running.


First, I am not sure whether “users don’t, in general, have the JRE installed” is accurate.  Mac OS X, a major market for me, ships with it installed.  Java has some nice viral characteristics (after you decide to install it on your computer once it persists for years), and with the increasing uptake of broadband I don’t think the 18MB JRE (or the 7 MB mini-install) are the gigantic stumbling block they were back in, say, 2001 when all the “Java will never work on the desktop” articles were published.  Getting accurate statistics on Internet users is like herding cats, but www.thecounter.com registered 89 million hits this month and some 95% of them had a version of Java installed (I’m guessing a large number are MS Java 1.1, which is less than helpful to me, but there you go).


Then there is the work around to not having a JRE installed: I am creating two seperate distributions of my program.  The Mac version is, at the moment, just an executable jar file.  The PC version is wrapped in [Launch4j](http://launch4j.sf.net), an open source native Windows executable which, for the price 21kB, wraps your JAR in an .exe, allows you to display a BMP splash screen while the JRE is loading, and (perhaps most importantly) will handhold your customer through a JRE install if the minimum JRE requirements are not met.  Granted, the JRE install is not for the most casual users.  It weighs in at 18 MB, which is more than a coffee break.  However, with their web install version you can cut that down to 7MB and about ~4 mouse clicks.  Which is certainly more than zero, but doable even on dialup (~20 minutes on 56k).  It thankfully does not require a restart anymore.


With regards to speed: Java is just not slow at what I am doing if you are using a computer which is anything close to recent.  Starting up the JRE takes a few seconds which I can handily cover with a splash screen, and then I display another splash screen for 5 seconds offering them the opportunity to upgrade to the full version before dumping them into the main window.   On my PCs at work and home the entire process takes about 10 seconds, and all of it is hopefully at least minimally engaging to the user.


Anyhow, on development environments: Visual Studio .NET would also let me build a compelling graphical application in a reasonable amount of time, but while I’ve got a legal license at work I don’t at home.  I’m just not enough of an expert with the Windows APIs to do a GUI in a reasonable amount of time without the .NET safety-net under me, and I don’t know of any free alternatives which can touch the combination of Netbeans or Eclipse plus the Java libraries (ugly, ungainly beasts though they are, I’ve cut my teeth on most of the ones in the critical path already).
