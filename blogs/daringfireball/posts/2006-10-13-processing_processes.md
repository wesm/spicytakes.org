---
title: "Processing Processes"
date: 2006-10-13
url: https://daringfireball.net/2006/10/processing_processes
slug: processing_processes
word_count: 1840
---


Lots of great reader feedback regarding Tuesday’s “[How to Determine if a Certain App Is Running Using AppleScript and Perl](http://daringfireball.net/2006/10/how_to_tell_if_an_app_is_running)”. Here are the highlights.


## Bundle Identifiers


[Sven-S. Porst](http://earthlingsoft.net/ssp/blog/) emailed to point out that it’s somewhat curious that you can query System Events for processes by name, displayed name, and by creator type — but *not* by bundle identifier. I.e. you can do this:


```
tell application "System Events"
  count (every process whose creator type is "R*ch")
end tell

```


But you can’t do something like this:


```
tell application "System Events"
  count (every process whose bundle identifier is "com.barebones.bbedit")
end tell

```


Which seems like a strange oversight considering that System Events is new to Mac OS X, and bundle identifiers are the “Mac OS X” way to uniquely identify applications. They’re also certainly much easier to remember, and generally easy to guess.


## Clever Endianness Workaround for `Mac::Processes`


I mentioned Tuesday that the useful `Mac::Processes` Perl module, which ships as part of Mac OS X’s Perl installation, has a few endianness-related bugs in the version that ships with Intel-based Macs. To wit, creator type codes are reversed.


While writing Tuesday’s article, I considered suggesting a workaround that would involve checking creator types both forwards and backwards, and considering it a hit if you got a match in either direction. That’s *likely* to work just fine, but too skanky a hack to endorse.


Reader Patrick McCafferty emailed a much better workaround: look for a process by name that you *know* must be running, like, say, loginwindow, and check its creator type (“lgnw” for loginwindow). If it’s reversed, then you know you’re running on an Intel-based Mac with the older (buggy) version of `Mac::Processes`, and you can work around the bug by reversing all creator types manually.


It’s easier, of course, to just match by process names (which aren’t affected by the endianness bug) instead of creator codes, but McCafferty’s suggestion was just too clever not to pass along.


## p.s. — What about `ps`?


The most common question, though — by far — was, “Why not just use `ps` and `grep`?” I did mention this technique in passing on Tuesday, before getting on to how to execute embedded AppleScript from within Perl, writing:


> I suppose what most Unixheads would do is pipe the results of `ps
> -aux` through `grep`, but it’s easy to call AppleScript from Perl […]


The reason I didn’t cover it in more detail is that it can be a bit tricky to get it right. Nearly everyone who emailed to suggest it, for example, got it wrong, suggesting [something along the lines of](http://www.paulbeard.org/wordpress/index.php/archives/2006/10/11/daring-fireball-how-to-determine-if-a-certain-app-is-running-using-applescript-and-perl/):


```
ps -x | grep -c Safari

```


**Brief explanation for the benefit of readers to whom the above command looks like utter gibberish:** The `ps` command-line tool gives you a list of running processes, one per line. If you just type `ps` with no options, you only get a listing of processes belonging to the current user (which is you) which have a “controlling terminal”, which means, more or less, that they’re processes which were initiated at the command line. Adding the `-x` switch tells the `ps` command to display all processes, including those that are “normal” Mac OS X applications, and that’s what we want.


The `grep` command goes through lines of text one-by-one, applying a regular expression to each line, looking for matches. In the above case, the pattern is the literal string “Safari”. The `-c` option tells `grep` only to count the number of matching lines; without specifying that option, `grep` will print the matching lines in their entirety. The pipe (`|`) character connects the two commands together. So, first, `ps -x` runs and generates a list of running processes, one per line; those lines are *piped into* `grep -c Safari`, which counts how many of those lines match the pattern “Safari”. If Safari isn’t running, the result will be “0”; if it is, the result should be “1”.


In most cases, including the above example where we’re looking to see if Safari is running, this will work. But it won’t work — at least not as expected — in other cases. For example, if you try the same thing to see if iTunes is running:


```
ps -x | grep -c iTunes

```


for most people the result of that command is *always* going to be at least “1”, *even when iTunes isn’t running*. The problem is that there’s an invisible background application called “iTunesHelper”,1 and the grep pattern “iTunes” matches that name as well, and unless you’ve disabled it, iTunesHelper is always running. We need a more precise grep pattern if we want to match process names accurately.


The problem with regular expressions is that it’s often easy to write one that *usually* works, but hard to write one that *always* works. Instead of just trying to match the part of the line that you’re looking for, you should try to match the *entire* line, including both the part you’re looking for and the parts you aren’t otherwise interested in. That way “AppName Helper” won’t get mistaken for “AppName”.


Here’s what a line of output from `ps -x` looks like:


```
696  ??  S    0:01.22 /Applications/TextEdit.app/Contents/MacOS/TextEdit

```


That’s the process ID (a unique number for each process; multiple instances of the same program get their own ID), a couple of columns we don’t care about, and then the full path of the running program. So imagine you were trying to test if a hypothetical app named “Content” were running; if you tried this:


```
ps -x | grep -c Content

```


you’d get a match for every single app with a “Contents” folder inside its application bundle — which pretty much means every single application you use. (When I ran that command just now to test it, the result was “52”.)


One way we can narrow this down is to pass `ps` the `-c` option on the command line; this option tells `ps` only to the list the name of the process, not its full path. A typical line of output from `ps -xc` looks like this:2


```
696  ??  S    0:01.22 TextEdit

```


All we’re interested in is the name of process; for our purposes here, those other columns aren’t interesting. So, one way to match the entire line, looking for TextEdit, would be:


```
ps -xc | egrep -c "^[ ]*[0-9]+[ ]+[^ ]+[ ]+[^ ]+[ ]+[^ ]+[ ]+TextEdit$"

```


Lord knows I loves me the regular expressions,3 but avoiding crafting a pattern like the above is what led me to skip this technique originally.


But it ends up we can make this *a lot* easier. The ugly parts of that pattern are the bits that match the columns of output from `ps` that we aren’t interested in. We could avoid that work if we could just tell `ps` that we aren’t interested in the process names — and thanks to `ps`’s heretofore-unknown-to-me `-o` option, that’s exactly what we *can* do. (Thanks to reader Sam Vaughn for this solution.)


A few typical lines of output from `ps -xc -o command` look like this:


```
iChat
iChatAgent
MarsEdit
Dictionary
Preview
TextEdit

```


That is, just the process names, one per line, no more, no less. Now we can grep for one particular app name with a simple pattern like this:


```
ps -xc -o command | egrep -c "^iTunes$"

```


That’s both clever and robust.


## Benchmarks


So which technique is best? I’m pretty sure they’re all equally reliable. And it ends up they’re all pretty fast.


If you’re writing AppleScript, the answer seems clear: use System Events, and identify apps by either name or creator type. I’ve seen people calling out to `ps` using AppleScript’s `do shell script` command, but I can’t see why unless they’re unaware of how to do it using System Events.


If you’re using Perl, the answer isn’t quite as clear, but it seems to me that the `ps`-and-`egrep` method discussed above is probably best, followed by using `Mac::Processes`. Here’s a version of the `is_app_running()` Perl subroutine that works by calling out to `ps` and `egrep`:


```
sub is_app_running {
    my $app_name = quotemeta shift;
    my $running = qx( ps -xc -o command | egrep -c "^$app_name\$" );
    chomp $running;
    return $running;
}

```


The other options from Perl are `Mac::Processes`, and calling out to System Events via AppleScript using either `osascript` or MacPerl’s `DoAppleScript`.
All seem equally accurate, but the `ps`-and-`grep` technique seems fastest.


My first attempt at benchmarking these four techniques ([see the source here](http://daringfireball.net/misc/2006/10/running-app-test)) was inconclusive. In fact, according to the results of that script, calling out to `ps` and `egrep` was actually slightly *slower* than either of the two techniques for using AppleScript from within Perl.


That didn’t seem right to me — I expected the `ps`-and-`egrep` technique to be at least somewhat faster, if not a lot faster, than either AppleScript calling method. So I plugged it into my working copy of [BBColors](http://daringfireball.net/projects/bbcolors/), and, lo and behold, it felt snappier, and using the `time` tool to measure a single invocation showed that when using `ps`-and-`egrep` to test if BBEdit is running, `bbcolors` ran in a little under half a second every time. Using my previous technique of calling out to AppleScript, it generally took somewhere between 1.5 to 2.5 seconds each time.


In my benchmarking script (the one that showed calling AppleScript from within Perl coming out ahead), I’m testing each routine 1,000 times. I suspect that what’s happening is that there are some serious caching and “*everything is already loaded in memory*” benefits to the repeated calls. But my real world usage doesn’t resemble that benchmarking setup at all — the `bbcolors` tool calls this routine just once, not hundreds of times in quick succession, and when you call it just once, the AppleScript-based methods are slower because they have to compile the embedded AppleScript code and invoke the OSA runtime.


Using `Mac::Processes` also is noticeably faster, in real-world use, than either AppleScript-based technique, but not quite as fast as `ps`-and-`egrep`.


---

1. There’s something funny about iTunesHelper’s name. In most places it shows up as “iTunesHelper”, no space. But in Activity Viewer, it shows up as “iTunes Helper”, with a space. AppleScript seems to know about both spellings, but “iTunesHelper” seems to be the canonical one; if you type `tell app "iTunes Helper" to activate`, after your script editor compiles it, the app name is changed to “iTunesHelper”. My best guess as to why this is: in the *iTunesHelper.app/Contents/Info.plist* file, the value for the CFBundleName key is “iTunes Helper”; but the application binary itself is named “iTunesHelper”. ↩︎
2. With most command-line tools, single-character options can be concatenated together; “`ps -xc`” is equivalent to “`ps -x -c`”. ↩︎
3. Have you looked at the source code to [Markdown](http://daringfireball.net/projects/markdown/)? ↩︎



| **Previous:** | [How to Determine if a Certain App Is Running Using AppleScript and Perl](https://daringfireball.net/2006/10/how_to_tell_if_an_app_is_running) |
| **Next:** | [Using Keyboard Maestro to Intercept Keyboard Shortcuts Usurped by the System](https://daringfireball.net/2006/10/keyboard_maestro) |


PreviousNext