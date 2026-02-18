---
title: "‘Do Shell Script’ and Premature Optimization"
date: 2009-02-05
url: https://daringfireball.net/2009/02/do_shell_script_premature_optimization
slug: do_shell_script_premature_optimization
word_count: 316
---


After last week’s [piece](http://daringfireball.net/2009/01/applescripts_targetting_safari_or_webkit) on how to write AppleScripts that dynamically target either Safari or WebKit, a few readers asked about the following subroutine, which returns the name of your default web browser:


```
on GetDefaultWebBrowser()
    set _scpt to "export VERSIONER_PERL_PREFER_32_BIT=yes; " & ¬
        "perl -MMac::InternetConfig -le " & ¬
        "'print +(GetICHelper \"http\")[1]'"
    return do shell script _scpt
end GetDefaultWebBrowser

```


The question, more or less, is why call out to the shell to use Perl rather than figuring out a way to do it in pure AppleScript? It costs memory and time to call out to the shell and launch an instance of the Perl interpreter.


My answer is that this Perl routine is plenty fast enough, and when the script is finished the memory used by the Perl interpreter is released. I wrote a simple script that does nothing other than call this routine one time; [Script Debugger](http://www.latenightsw.com/sd4/index.html) reports that it typically takes less than 0.1 seconds to run. If this were something that I were calling repeatedly, hundreds or thousands of times in a tight loop, sure, I’d consider writing the fastest possible version. But I only call this routine one time. Perl, and the Mac::InternetConfig library that the snippet uses to get the default handler for the “http” URL scheme, are installed with Mac OS X by default.


This strikes me as a perfect example of [Donald Knuth’s famous axiom](http://en.wikipedia.org/wiki/Optimization_(computer_science)): “We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.” There are a slew of cases where the easiest solution to doing something in AppleScript is to use `do shell script` to do it from a shell scripting language. I think it’s the best thing that ever happened to AppleScript.



| **Previous:** | [Writing AppleScripts That Dynamically Target Either Safari or WebKit](https://daringfireball.net/2009/01/applescripts_targetting_safari_or_webkit) |
| **Next:** | [Apple, Google, and Palm](https://daringfireball.net/2009/02/apple_google_palm) |


PreviousNext