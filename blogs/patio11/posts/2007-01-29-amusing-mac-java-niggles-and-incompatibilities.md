---
title: "Amusing Mac Java Niggles and Incompatibilities"
date: 2007-01-29
url: https://www.kalzumeus.com/2007/01/30/amusing-mac-java-niggles-and-incompatibilities/
slug: amusing-mac-java-niggles-and-incompatibilities
word_count: 395
---


Three things to not do the next time you release Java software on a Mac:

1. Use ./ to refer to the current directory. On Windows, this will refer to the current directory the JAR is on. On Mac, it will refer to a directory internal to the JAR. Since you can’t actually access that, it appears to default to system root. (!?) If, on the other hand, you refer to the directory as . you introduce other problems which I can’t quite recall at the moment (memo to self: “//don’t use . here, causes problems” is not a maximally useful comment).
2. Exercise caution with using javax.print.PrintServiceLookup. On a Windows machine, you are guaranteed that the default printer will be equivalent (.equals) to one of the printers returned on that list. This might lead you to write code which, for example, pre-selected the default printer from a drop-down list of printers. On a Mac, you are not guaranteed that the default printer will be equivalent to one of the printers on the available printer list. Which means, if you were careless like me and assumed that the default printer was on that list if the default printer wasn’t null, you will have your GUI thread choke and die with an index out of bounds error thrown by the list component. I’m going to recode my default printer selection logic to use least-distance string comparison to get around this little feature.
3. Fail to test code known to be good. This burned me badly. In a Java application, as opposed to a trivial Hello World program or CS assignment, you’re going to be heavily reliant on the Java libraries working as advertised. As you can see from above, sometimes they have quirks in them. Seemingly innocuous changes to one part of your code can have a ripple effect causing the libraries to break assumptions you have made in other parts of your code, resulting in potential showstoppers. Example: I changed *nothing* about the internal printing logic in 1.05, and just changed the printer used from hardcoding it as the default printer to giving users a choice of other printers as well. Swing is a known good component, the default printer is a known good component, and the printer enumeration methods are known good… but the combination of the three introduced a showstopper on the Mac.
