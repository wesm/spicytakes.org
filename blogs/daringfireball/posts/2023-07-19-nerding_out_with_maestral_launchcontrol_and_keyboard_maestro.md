---
title: "Nerding Out With Maestral, LaunchControl, and Keyboard Maestro"
date: 2023-07-19
url: https://daringfireball.net/2023/07/nerding_out_with_maestral_launchcontrol_and_keyboard_maestro
slug: nerding_out_with_maestral_launchcontrol_and_keyboard_maestro
word_count: 1280
---


*Item 1:* [Dropbox](https://www.dropbox.com/products?source=plans) remains an excellent service, seemingly utterly reliable, with fair pricing.


*Item 2:* Dropbox’s official Mac client has been a confusing, ugly, resource-heavy mess for years, and is only getting worse.


*Item 3:* [Maestral](https://maestral.app/) is an open source Dropbox client for MacOS and Linux, developed by Sam Schott. It provides exactly what I want in a Mac Dropbox client, and [what the official Dropbox app once was](https://daringfireball.net/linked/2019/06/13/dropbox-sucks), long ago: a folder that syncs, with a minimal user interface that lives in a menu bar app. It [uses far less memory](https://maestral.app/about/) than Dropbox’s official client and offers a much simpler interface.


I switched from Dropbox’s official Mac client to Maestral last August. Overall I’ve been very happy with the move. But Maestral is not for everyone. [From Maestral’s website, under “Limitations”](https://maestral.app/about/):


> Currently, Maestral does not support Dropbox Paper, the management
> of Dropbox teams and the management of shared folder settings. If
> you need any of this functionality, please use the Dropbox website
> or the official client.
> Maestral uses the public Dropbox API which, unlike the official
> client, does not support transferring only those parts of a file
> which changed (“binary diff”). Maestral may therefore use more
> bandwidth that the official client. However, it will avoid
> uploading or downloading a file if it already exists with the same
> content locally or in the cloud.


I don’t use Dropbox Paper, don’t have a Dropbox “team”, and I’m fine going to the Dropbox website to manage shared folder settings. The only thing I miss from the official Dropbox client is the Finder contextual menu item to copy a sharing link to an item — but I need that seldom enough that I don’t much mind doing that on the Dropbox website too.


Another big difference: [the official Dropbox client is transitioning](https://help.dropbox.com/installs/dropbox-for-macos-support) to MacOS’s relatively new [File Provider APIs](https://developer.apple.com/documentation/fileprovider). These are the APIs that allow cloud-based storage providers to keep certain files online-only, downloading the file locally only when you need it. I don’t need or want that. I just want my entire Dropbox folder’s contents to sync entirely. (Maestral does support Dropbox’s “selective sync” to omit specified folders and files, but those omitted files don’t show up at all in your local folder.) If you keep your Dropbox folder on an external hard drive, you might *need* to switch to Maestral, because Apple’s File Provider APIs require folders to be stored in *~/Library/CloudStorage/*. With Maestral, your local Dropbox folder can be anywhere.


Bottom line: 11 months in, and I’m a very happy Maestral user.


But. For the last month or so, I’ve noticed that whenever I wake my Mac (an M1 MacBook Pro running MacOS Ventura 13.4.1), Maestral (version 1.7.3) is no longer running. It crashes silently in the background while my Mac is sleeping (or when waking up?). [Here’s an issue filed for the bug on GitHub](https://github.com/samschott/maestral/issues/939), dittoed by half a dozen users. The obvious band-aid solution is to manually relaunch Maestral each time I wake my Mac, but that’s annoying and easy to forget. The whole point of Dropbox is that it just works in the background, automatically.


While waiting for a fix in Maestral itself, here are two workarounds. They should be applicable in any situation where you want to automatically relaunch an app that is periodically crashing in the background.


## Workaround 1: LaunchControl and launchd


[`launchd`](https://www.launchd.info/) is Apple’s longstanding (dating back to Mac OS X 10.4) system for running background processes, either on a schedule or triggered by events. The built-in way to manage `launchd` jobs is the `launchctl` command-line utility.1 `launchd` is very nerdy and [has a ton of features](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html).


Enter Robby Pählig’s [LaunchControl](https://www.soma-zone.com/LaunchControl/): “a fully-featured `launchd` GUI allowing you to create, manage and debug system and user services on your Mac.” It costs $21 for a personal license and is worth every cent. LaunchControl is well-designed, comprehensive, and extensively-documented.


In my case, I wanted to create a new `launchd` job that will keep Maestral running at all times. When it crashes while my Mac is sleeping, I just want it to silently relaunch. Creating such a job using LaunchControl is trivial.


First, drag and drop the Maestral app onto the LaunchControl app icon. This will show a dialog box like this:


Click “For current user”.2


That’s it. This does exactly what we want by default: it creates a new user-only `launchd` job that keeps Maestral alive no matter what. If it crashes, it’ll be relaunched. If we quit Maestral manually, it’ll be relaunched.


One bit of manual fiddling I suggest is giving the job a descriptive name. By default, LaunchControl just names it “local.job”. I renamed mine “local.Maestral.keepalive”:


[
](https://daringfireball.net/misc/2023/07/launchcontrol-renaming-agent.png)


The file for this job (after renaming) lives at *~/Library/LaunchAgents/local.Maestral.keepalive.plist*. But you never really need to deal with that file if you’re using LaunchControl. If you ever want to trash it (e.g. after a version of Maestral ships with a fix for this bug), you can do so within LaunchControl itself.


## Workaround 2: Keyboard Maestro and AppleScript


For anyone else out there running into this bug with Maestral 1.7.3, the LaunchControl/`launchd` solution described above is all you need for a workaround. But the nerd in me wanted to know *how often* Maestral was crashing in the background. When Maestral crashes while my Mac is sleeping, it doesn’t seem to leave any sort of log describing what happened or when.


So here’s another workaround, this time using [Keyboard Maestro](https://www.keyboardmaestro.com/) and a tiny AppleScript. First, create a new global macro in Keyboard Maestro. I named mine “Maestral: Keep Alive”. Set it up like this:


[
](https://daringfireball.net/misc/2023/07/keyboard-maestro-maestro-keepalive.png)


The trigger is “Periodically while logged in”, running once a minute, all day, every day of the week. The action is this simple AppleScript:


```
if application "Maestral" is not running then
    display notification (current date) as string ¬
        with title "Maestral was not running"
    do shell script "/usr/bin/open /Applications/Maestral.app"
end if

```


If Maestral is running when this script runs, nothing happens. If it isn’t, the script [displays a notification](https://daringfireball.net/misc/2023/07/keyboard-maestro-maestro-keepalive-notification.png) with the current date and time, and then launches Maestral. Sometimes I notice the notification appear after I wake my Mac, sometimes I don’t. But I can go to Notification Center and see the whole stack of them to see how often it’s occurring. (Turns out it gets triggered a dozen or so times overnight, every day.)


Astute scripters might wonder why I’m using `do shell script "/usr/bin/open /Applications/Maestral.app"` to launch Maestral, instead of the idiomatic `tell application "Maestral" to launch`. Good question. The answer is that each time Keyboard Maestro runs this AppleScript, it needs to be compiled. And whenever an AppleScript is compiled, any applications targeted by `tell` blocks will be launched if they aren’t already running. That’s just a quirk of how AppleScript works, but in this particular case, it would defeat the entire purpose of the script, because when the script runs, Maestral would always be running, because if it weren’t already running before the macro started executing, it would get launched when Keyboard Maestro compiled the script, which happens right before the script is actually run. So we relaunch Maestral with a one-line shell script instead.


---

1. The standard POSIX `cron` utility is still supported on MacOS, but is deprecated in favor of `launchd`. ↩︎
2. Which, to be a HIG pedant, [ought to be title-cased](https://developer.apple.com/design/human-interface-guidelines/buttons): “For Current User”. ↩︎︎



| **Previous:** | [Now Apollo Faces the Cliff](https://daringfireball.net/2023/07/now_apollo_faces_the_cliff) |
| **Next:** | [Of Course Apple Has an LLM AI in the Works, and of Course the Bloomberg Report Revealing Its Code Name Mentions How the Story Moved the Company’s Stock Price](https://daringfireball.net/2023/07/apple_gpt_bloomberg) |


PreviousNext