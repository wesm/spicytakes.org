---
title: "Getting MarkDown and SmartyPants working with EditPad Pro"
date: 2006-09-19
url: https://www.joelonsoftware.com/2006/09/19/getting-markdown-and-smartypants-working-with-editpad-pro/
word_count: 283
---


[MarkDown](http://daringfireball.net/projects/markdown/) is a simple processor that converts text to HTML. For example, it converts *text surrounded by asterisks* to *italics*.


[SmartyPants](http://daringfireball.net/projects/smartypants/) replaces “straight quotes” with “curly quotes” and makes a few other typographic improvements.


[EditPad Pro](http://www.editpadpro.com/) is a very respectable text editor for Windows. It’s fast and contains scrillions of useful features. It’s not the fanciest thing in the world, but if you’re still using Notepad for the occasional bits of text, it’s a fine drop-in replacement.


Here’s what it takes to get them all working together on a typical Windows setup:

- Install Perl, if you don’t already have it. For Windows, the easiest way to do this is from [ActiveState’s download page](http://www.activestate.com/store/activeperl/download/). Just download the Windows MSI package and run it. Make sure to choose the option to associate .pl files with Perl.
- Go into c:\Perl and make a directory called **markdown**.
- Download [Markdown](http://daringfireball.net/projects/downloads/Markdown_1.0.1.zip) and [SmartyPants](http://daringfireball.net/projects/downloads/SmartyPants_1.5.1.zip). Open the ZIP files and put **Markdown.pl** and **SmartyPants.pl** in the directory you just made, **c:\perl\Markdown**.
- Also in that directory, make a little batch file named **md.bat**:


`@echo off  c:\perl\markdown\Markdown.pl %1 > "%~dpn1.tmp" c:\perl\markdown\SmartyPants.pl "%~dpn1.tmp" > "%~dpn1.html"  del "%~dpn1.tmp" start "" "%~dpn1.html"`

- In EditPad Pro, choose Tools | Configure Tools. Click New. Set the Caption to “MarkDown”, and set the Command Line to `c:\perl\markdown\md.bat "%FILE%"`. You may want to check the box in the Files tab that says “Save the current file if it has unsaved changes.”
- Now you have a menu item Tools|Markdown which will save the file you’re working on and generate an HTML version of it (replacing the extension you used with .html), then it pops it up in a web browser so you can check it.
