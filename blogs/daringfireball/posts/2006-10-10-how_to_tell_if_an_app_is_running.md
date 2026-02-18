---
title: "How to Determine if a Certain App Is Running Using AppleScript and Perl"
date: 2006-10-10
url: https://daringfireball.net/2006/10/how_to_tell_if_an_app_is_running
slug: how_to_tell_if_an_app_is_running
word_count: 1357
---


[BBColors](http://daringfireball.net/projects/bbcolors/) does its thing by reading and writing to BBEdit’s preferences using the `defaults` system. The `defaults` man page says:


> Since applications do access the defaults system while they’re
> running, you shouldn’t modify the defaults of a running
> application. If you change a default in a domain that belongs to a
> running application, the application won’t see the change and
> might even overwrite the default.


So, as a precaution, the `bbcolors` tool won’t load a new color scheme if BBEdit (or TextWrangler, if that’s your bag) is currently running. But so how do you test if an application is currently running?


BBColors is written in Perl, but the simplest good way I know of to test if an app is running is this bit of AppleScript:


```
tell application "System Events"
    count (every process whose creator type is "R*ch")
end tell

```


Where “R*ch” is BBEdit’s four-character creator type.


If BBEdit isn’t running, it returns 0; if it is running, it returns 1 (or a larger integer, if, for whatever reason, you’re running more than one copy of BBEdit).


Using the creator type is a bit geeky — plus, some processes don’t have creator types (most such apps are background “helper” apps, but even some normal apps, Console for example, don’t have creator types). So, you can also just ask for the name:


```
tell application "System Events"
    count (every process whose name is "BBEdit")
end tell

```


and you should get the same results, with the added benefit of being able to identify any process — not every process has a creator type, but they all have names.


There’s also the `displayed name` property, which is different than the just plain `name`:


```
tell application "System Events"
    count (every process whose displayed name is "BBEdit")
end tell

```


That *might* work, but it won’t if you have the Finder’s preference to always display file extensions turned on (as I do). In that case, an application’s `displayed name` contains the “.app” extension, so you’d have to write:


```
tell application "System Events"
    count (every process whose displayed name is "BBEdit.app")
end tell

```


“`Names`” and “`displayed names`” can differ in other ways, as well. You can determine if Quicksilver is running using its `name`:


```
tell application "System Events"
    count (every process whose name is "Quicksilver")
end tell

```


And because the string comparison is case-insensitive, you can mis-capitalize it “QuickSilver” or “quicksilver” or “QUICKSILVER” and it’ll still work. But if you want to identify it by `displayed name`, you’ve got to use the clever Unicode-laden spelling that you see atop its application menu:


```
tell application "System Events"
    count (every process whose displayed name is "Quıcĸsıɩⅴεʀᵦ₄₉.app")
end tell

```


So in a nut: the `creator type` and `name` properties are good bets; the `displayed name` property is not, because it changes depending on the user’s Finder preference for displaying file extensions.


## Doing It From Perl and the Shell


Now as I wrote earlier, BBColors is written in Perl, not AppleScript. I suppose what most Unixheads would do is pipe the results of `ps -aux` through `grep`, but it’s easy to call AppleScript from Perl, or any other shell scripting language: just use the `osascript` command-line tool. From the Terminal, you could type:


```
osascript -e 'tell app "System Events" to count processes whose name is "Finder"'

```


Here’s a Perl subroutine that takes a creator type as a parameter, and returns the result of our AppleScript (i.e. the number of processes running with that creator):


```
sub is_app_running {
    my $creator = shift;

    my $applescript = qq{ 'tell application "System Events" to count } . 
            qq{ (every process whose creator type is "$creator")' };
    my $result = qx( osascript -e $applescript );
    chomp $result;

    return $result;
}

```


Except this code has a few subtle bugs: it won’t work if it’s passed a creator type string containing either a literal double-quote or a backslash character. I’m not aware of any creator type codes that use these characters, but they’re legal.


So here’s a fixed version that backslash escapes single quotes, double quotes, and literal backslashes. We need one level of backslashing for Perl, and another level for the shell when we call the `osascript` tool:


```
sub is_app_running {
    my $creator = shift;
    $creator =~ s{\\}{\\\\}g;
    $creator =~ s{"}{\\"}g;
    $creator =~ s{'}{'\\''}g;

    my $applescript = qq{ 'tell application "System Events" to count } . 
            qq{ (every process whose creator type is "$creator")' };
    my $result = qx( osascript -e $applescript );
    print "result: $result\n";
    chomp $result;

    return $result;
}

```


Starting with Mac OS X 10.4, the system’s default Perl installation includes a Perl module called `MacPerl` (which started life way back in the classic Mac OS era). `MacPerl` contains a routine called `DoAppleScript()`, which does what you think it does; it takes as input a string containing AppleScript code, runs the script, and returns the result as a string. We can use this instead of calling out to the `osascript` shell tool, like this:


```
use MacPerl 'DoAppleScript';

sub is_app_running {
    my $creator = shift;
    $creator =~ s{\\}{\\\\}g;
    $creator =~ s{"}{\\"}g;

    my $applescript = qq{ tell application "System Events" to count } .
            qq{ (every process whose creator type is "$creator") };
    my $running = DoAppleScript($applescript);
    chomp $running;

    return $running;
}

```


The only real advantage to this technique is that you don’t have to worry about escaping single quotes — just double quotes and literal backslashes. `DoAppleScript` is also a little bit faster than shelling out to `osascript`, but both techniques are pretty fast.


You can also use the `Mac::Processes` module, which is part of the `Mac::Carbon` bundle of modules, and is also included by default in Mac OS X 10.4’s default Perl installation. We could rewrite our `is_app_running()` subroutine to use `Mac::Processes` like so:


```
use Mac::Processes;

sub is_app_running {
    my $creator = shift;
    my $running = 0;

    PROCESS_LIST:
    while ( my ($psn, $psi) = each(%Process) ) {
        if ($psi->processSignature eq $creator) {
            $running = 1;
            last PROCESS_LIST;
        }
    }

    return $running;
}

```


We can also identify apps by name using `Mac::Processes`, by using the `processName` property instead of `processSignature`; these names are the same as those returned by the `name` property in our AppleScript examples (i.e. not `displayed name`).


The advantage to using `Mac::Processes` is that you don’t have to mix any AppleScript into your Perl. The disadvantage, though, is that the version of the `Mac::Carbon` modules that ships by default with Intel-based Macs contains a bunch of endian-related bugs. One such bug is that the creator types returned by the `processSignature` property appear backwards: instead of “R*ch” for BBEdit, you get “hc*R”; instead of “MACS” for the Finder, you get “SCAM”.1


That might strike you as a really weird bug. The short explanation is that creator types aren’t really four-character *strings*; they’re four-byte integers, and treating each of the bytes as a MacRoman-encoded character is just a shortcut that makes them more readable and memorable. (Such four-byte “OSTypes” are used throughout Carbon.) The problem is that the PowerPC and 680 × 0 architectures are [big endian](http://en.wikipedia.org/wiki/Endianness), and the x86 (a.k.a. “Intel”) architecture is little endian, which means the bytes comprising an integer appear in the reverse order on Intel.


[Chris Nandor](http://pudge.net/) — who maintains the entire `Mac::Carbon` suite of modules — [fixed these Intel compatibility bugs](http://use.perl.org/~pudge/journal/29967) back in June, but, alas, the fixed versions don’t yet ship with the OS. So if you’re writing a script for your own use and have upgraded to the latest version of `Mac::Carbon` from [CPAN](http://search.cpan.org/), you have no worries. But, if you’re hoping to distribute your script to other Mac users who probably have the default (buggy on Intel) version of `Mac::Carbon` installed, as I was with BBColors, you’re stuck dealing with the buggy version. The best way to do that is to identify apps by name — which works with the default version of `Mac::Processes` on all Macs running 10.4 — rather than by creator type.


---

1. Insert your own joke here. ↩︎



| **Previous:** | [BBColors 1.0](https://daringfireball.net/2006/10/bbcolors_1-0) |
| **Next:** | [Processing Processes](https://daringfireball.net/2006/10/processing_processes) |


PreviousNext