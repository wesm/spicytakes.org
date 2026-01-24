---
title: "Logging TraceListener Improved"
date: 2005-03-11
url: https://blog.codinghorror.com/logging-tracelistener-improved/
slug: logging-tracelistener-improved
word_count: 256
---

I made a few improvements to the [Logging TraceListener](https://blog.codinghorror.com/logging-tracelistener/):

- Files can now be aged by date as well as size
- Filename is now completely templated using a single FileNameTemplate property, which supports standard `String.Format` codes for file number and date
- Added separate properties to specify units of scale for age and size (kb, month, gb, week)
- Default limit changed to 1mb maximum size, no age limit, no file count limit


Here’s how the new options look when set it up via the .config file:

kg-card-begin: html

```
<!-- this enables IIS-style logging of console output -->  
<system.diagnostics>  
<trace autoflush="true" indentsize="4">  
<listeners>  
<add name="CyclicLog"  
type="ConsoleApp.CyclicLogTraceListener,ConsoleApp"  
initializeData="fileCountThreshold=10, fileSizeThreshold=512,  
fileSizeUnit=kilobytes, fileAgeThreshold=1, fileAgeUnit=months,  
fileNameTemplate='console-{1:MMM-yy}-{0:0000}.log'" />  
</listeners>  
</trace>  
</system.diagnostics>
```

kg-card-end: html

And here’s how it looks when created manually:

kg-card-begin: html

```
_HtmlLogger = New CyclicLogTraceListener
With _HtmlLogger
.TimeStampFormat = ""
.FileNameTemplate = "html-{1:MMM-yy}-{0:0000}.log"
.FileAgeThreshold = 1
.FileAgeUnit = CyclicLogTraceListener.AgeUnit.Months
.FileCountThreshold = 3
End With
```

kg-card-end: html

I did this to get a separate, private log file for the large amounts of HTML I wanted to trace. Including them with the regular console output is way too noisy. I combined age, number, and size limits, so I end up with something like this:

kg-card-begin: html

```
html-Feb-05-0000.log        (1mb)
html-Feb-05-0001.log        (1mb)
html-Mar-05-0000.log        (1mb)
console-Feb-05-0000.log   (512kb)
console-Mar-05-0000.log   (512kb)
```

kg-card-end: html

With the configuration specified above, no more than 3 logs will ever exist, and no more than 3 per month, and never more than 512kb or 1mb in size.

[c#](https://blog.codinghorror.com/tag/c-2/)
[logging](https://blog.codinghorror.com/tag/logging/)
[tracelistener](https://blog.codinghorror.com/tag/tracelistener/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[configuration management](https://blog.codinghorror.com/tag/configuration-management/)
