---
title: "‘Restart Apache’ AppleScript"
date: 2005-11-30
url: https://daringfireball.net/2005/11/restart_apache_applescript
slug: restart_apache_applescript
word_count: 299
---


Here’s a quick tip for those of you developing web sites on your Mac.


When you make changes to Apache’s configuration file
(`/etc/httpd/httpd.conf`), you need to restart Apache to get the
changes to take effect. My most frequent need for this is when I set
up new staging servers using virtual hosting, but it’s the case for
any change you make to httpd.conf.


Apple’s built-in way to restart Apache is the use the Personal Web
Sharing section of the Sharing panel in System Preferences. Just click
Stop and then click Start. Easy — but it’s only really convenient if
you’ve already got the Sharing prefs panel open.


From the terminal, you can restart Apache using the `apachectl
graceful` command, which requires administrator privileges, which means
you’d typically invoke it as `sudo apachectl graceful`. That’s easy
too, but, again, is only convenient if you’ve already got a terminal
window open and can remember the exact spelling of ‘apachectl’.


So because I’m really lazy, I made an AppleScript that does this. It’s
just one single line:


```
do shell script "apachectl graceful" with administrator privileges

```


I saved it as a compiled script named “Restart Apache” in the
`/Library/Scripts` folder in my home folder, which puts it in my
system-wide Scripts menu. (You can turn the system-wide Scripts menu
on using the AppleScript Utility app in your
`/Applications/AppleScript` folder.)


So it’s as simple as this: when I need to restart Apache, I choose
“Restart Apache” from my system-wide Scripts menu, the script prompts
me to authenticate with admin credentials, and that’s it.


**Update:** [Shane Becker shows how to add a keyboard shortcut](http://theresistancearmy.com/blog/?p=202) to
the ‘Restart Apache’ script menu item.



| **Previous:** | [Full Metal Jacket Addenda](https://daringfireball.net/2005/11/fmj_addenda) |
| **Next:** | [A Public Service Announcement Regarding ‘callto:’ URIs and Safari](https://daringfireball.net/2005/12/callto_uris_safari) |


PreviousNext