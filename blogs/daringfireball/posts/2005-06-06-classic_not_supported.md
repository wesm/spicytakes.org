---
title: "Classic Not Supported on Intel-Based Macs"
date: 2005-06-06
url: https://daringfireball.net/2005/06/classic_not_supported
slug: classic_not_supported
word_count: 188
---


I haven’t seen this reported elsewhere, and there hasn’t been any official announcement from Apple, but page 67 of Apple’s [Universal Binary Programming Guidelines](http://developer.apple.com/documentation/MacOSX/Conceptual/universal_binary/universal_binary.pdf) PDF explicitly states that Classic apps are not supported in the Rosetta emulator that runs PowerPC apps on Intel-powered Macs (emphasis mine):


> Rosetta is designed to translate currently shipping applications that
> run on a PowerPC with a G3 processor and that are built for Mac OS X. 
> Rosetta does not run the following: 
> **Applications built for Mac OS 8 or 9**
> Code written specifically for AltiVec 
> Code that inserts preferences in the System Preferences pane 
> Applications that require a G4 or G5 processor 
> Applications that depend on one or more kernel extensions 
> Kernel extensions 
> Bundled Java applications or Java applications with JNI libraries
> that can’t be translated


I don’t think this is surprising, but it’s certainly the end of the Classic Mac era.


**Update:** I have confirmed that Apple has no plans for Classic support on Intel-based Macs.



| **Previous:** | [Intel-Apple Odds and Ends](https://daringfireball.net/2005/06/intel_apple_odds_and_ends) |
| **Next:** | [Bombs Away](https://daringfireball.net/2005/06/bombs_away) |


PreviousNext