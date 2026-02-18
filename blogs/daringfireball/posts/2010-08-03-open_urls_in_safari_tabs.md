---
title: "Service: Open URLs in Safari Tabs"
date: 2010-08-03
url: https://daringfireball.net/2010/08/open_urls_in_safari_tabs
slug: open_urls_in_safari_tabs
word_count: 584
---


I’ve [mentioned before](http://daringfireball.net/linked/2009/08/27/macosx-automation) that one of my favorite improvements to Snow Leopard was the overhaul of the system-wide Services menu. Service menu items are more easily accessed (including via the system-wide contextual menu), keyboard shortcuts are now easily configurable, and, best of all, you can easily create your own services using Automator and scripting languages like AppleScript, Perl, Ruby, and Python. [Here’s a good overview of Snow Leopard services](http://www.macosxautomation.com/services/index.html) from Sal Soghoian.


I’ve written a bunch that I use personally. One of my most-used is called “Open URLs in Safari Tabs”. Here’s how it works:

1. Select some text in any application.
2. Invoke the Open URLs in Safari Tabs service. (I usually do this via the control-click contextual menu.)
3. The service passes the selected text to a script I wrote. The script finds all the URLs in the selected text, opens a new Safari window, and creates a tab in that new window for each of the URLs.


The most common app from which I use it is Mail. Say someone sends me an email with three URLs, and I want to open all three of them. The typical way is to click one, which opens it in Safari and brings Safari to the front, then switch back to Mail and click the next one (which again brings Safari front), then switch back to Mail again and click the last one.1


With this service, I just select a range of text in the message that includes all three URLs, control-click on the selection, and select “Open URLs in Safari Tabs”.


URLs are identified using [the regex pattern I posted last week](http://daringfireball.net/2010/07/improved_regex_for_matching_urls).


I wrote the script so that Safari doesn’t come to the front when the service is invoked — the new window and tabs are created in the background. (If you’d rather have Safari come to the front, there’s a line in the script you can uncomment.)


[Here’s a demo movie showing the service in action](http://daringfireball.net/projects/services/Open_URLs_Service_Demo.m4v).


## Download and Installation

1. [Download the Open URLs in Safari Tabs workflow](http://daringfireball.net/projects/services/Open_URLs_in_Safari_Tabs.workflow.zip).
2. Unzip the file. (This may happen automatically, depending upon your browser preferences.)
3. Move the file named “Open URLs in Safari Tabs.workflow” to the *~/Library/Services/* folder in your home folder. (If there is no “Services” folder in your Library folder, create it.)


The service should now be available system-wide, both via the contextual menu and the Services sub-menu in the Application menu, when the current selection is a range of text. You can set a keyboard shortcut for any service in the Keyboard panel of System Preferences. If you wish to examine how it works or change its behavior, open it using Automator.


## Caveats


The service only works with Safari (and [WebKit nightlies](http://nightly.webkit.org/)); it doesn’t work with other browsers such as Firefox or Chrome. The version I’ve made available for download requires Mac OS X 10.6 (Snow Leopard) or later; if you’re using 10.4 or 10.5, you can create a service based on the below-linked Perl script using [Jesper’s free ThisService utility](http://wafflesoftware.net/thisservice/).


## Source Code and License


[Here’s a link to the source code](http://gist.github.com/507356) of the Perl script (which in turn executes an AppleScript) that drives the service. [MIT-licensed](http://www.opensource.org/licenses/mit-license.php) open source.


---

1. Mac OS X Mail supports a shortcut for opening links in the background: Command-clicking; if you know this, you can save a few steps. ↩︎



| **Previous:** | [An Improved Liberal, Accurate Regex Pattern for Matching URLs](https://daringfireball.net/2010/07/improved_regex_for_matching_urls) |
| **Next:** | [Papermaster and That Damn Antenna](https://daringfireball.net/2010/08/papermaster_damn_antenna) |


PreviousNext