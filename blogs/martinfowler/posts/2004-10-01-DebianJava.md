---
title: "Debian Java"
description: "Installing most things on Debian is sinfully easy:apt-get 	install package-name. Sadly Java is an exception since it's 	not in the basic debian system. I recently downloaded and installed 	java 1.5 (o"
date: 2004-10-01T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/DebianJava.html
slug: DebianJava
word_count: 469
---


Installing most things on Debian is sinfully easy: `apt-get
	install package-name`. Sadly Java is an exception since it's
	not in the basic debian system. I recently downloaded and installed
	java 1.5 (or 5, or whatever they're calling it these days) on my
	Debian Sid desktop. In brief
	the procedure is.


```

# apt-get install java-package
download the sun jdk from java.sun.com
# make-jpkg jdk-1_5_0-linux-i586.bin
# dpkg -i sun-j2sdk1.5_1.5.0_i386.deb
# apt-get install sun-j2sdk1.5debian
# update-alternatives --config java

```


(This is what I did. It worked for me, but it may not be the best
	way or work for you.)


Now the gory details. To make a java install into a debian
		package you need a tool that will debianize the sun install
		program. There's a few scripts out there that will do this and
		I've had the devil of a time finding out which one is the right
		one to use (I've done the install several times with different
		ones). It seems like the best choice is probably java-package
		which is available in Sid. (An alternative was j2se-package, but this [is now obsolete](http://www.z42.de/debian/).


Download the installer from Sun, you need the one that ends in
	â.binâ - don't use the RPM.


Once you have the binary you can now debianize it with the
	make-jpkg commands on the binary
	file.


When I did this (with all three scripts) I got a problem because
		the scripts aren't currently set to recognize the file name of the
		java 1.5 binary from sun (this may well be fixed by the time you
		read this.) To fix it I edited
		/usr/share/java-package/sun-j2sdk.sh. (If you can't see how,  wait
		until it gets updated.) After the edit the deb package built with
		no problem.


With the package built I moved it to where I keep my custom
		packages (/root/debs) and ran dpkg to install it. It gave an error
		saying it failed to install due to a dependency on
		sun-j2sdk1.5debian. However don't panic - if you then install
		sun-j2sdk1.5debian with apt-get everything installs properly. You
		can't do this the other way around because sun-j2sdk1.5debian is
		dependent on sun-j2sdk1.5.


If you had java installed like this before, typing 'java' at the
	command line just gives you the old VM. To get the new one use
	update-alternatives (or you can just make your own link).


My thanks to Michael
		Schuerig for letting me know about newer packaging
		scripts. I recently found this [description of the install process](http://serios.net/content/debian/java.php) which looks much better than what I have here.


Dirk Estievenart told me about a few things that were out of date. Here is his install procedure:


```

//download bin jdk from Sun
#apt-get install java-package
//exit root and login with normal user:
#fakeroot make-jpkg jdk-1_5_0_06-linux-i586.bin
//su again:
#dpkg -i sun-j2sdk1.5_1.5.0+update06_i386.deb
#update-alternatives --config java
# java -version
//The latter just to check

```
