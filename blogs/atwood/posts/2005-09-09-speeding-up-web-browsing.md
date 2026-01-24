---
title: "Speeding up web browsing"
date: 2005-09-09
url: https://blog.codinghorror.com/speeding-up-web-browsing/
slug: speeding-up-web-browsing
word_count: 544
---

In order to speed up my web browsing experience, **I disable Flash in Internet Explorer**. I’ve got nothing personal against Flash, mind you, but it’s generally chrome. It’s visually (and sometimes audibly) distracting, and it adds download time to each page view.


![](https://blog.codinghorror.com/content/images/2025/05/image-137.png)


An image is worth a thousand words, but for completeness, here’s the step-by-step:

1. Select the Tools, Manage Add-Ons menu
2. The dialog defaults to add-ons currently loaded. Look for “Shockwave Flash object” and “Shockwave ActiveX Control” from publisher “Macromedia, Inc.” If these aren’t visible, choose “Add-ons that have been used by Internet Explorer” from the dropdown menu. Sort the list by Publisher and look for Macromedia.
3. Click each add-on, then click the Disable option button.
4. Click the OK button. Upon exiting the dialog, it will warn you that you need to restart IE, but this isn’t the case. The current page will simply refresh and the flash movies will be either gone entirely or replaced with GIFs.


Flash is also the source of a [giant memory leak in Firefox](https://web.archive.org/web/20051001064510/http://fusion94.org/archives/2005/07/firefox_memory.html), so it’s probably a good thing to disable there as well. **I rarely need to see Flash movies as part of my normal web browsing**, but if I do, I just reverse the above steps. I’m sure there’s some fancy Firefox conditional display mod (e.g., click to display the flash movie) out there, too. Some quick Google searching confirms that [indeed there is](https://web.archive.org/web/20050922235456/http://flashblock.mozdev.org/). Go figure.


I’m also experimenting with using a custom HOSTS file that [blocks ad domains](http://www.mvps.org/winhelp2002/hosts.htm). I’m not anti advertising so much as I am pro speed. And the fastest downloads of all are the ones you don’t have to do!


So [what’s the HOSTS file](http://en.wikipedia.org/wiki/Hosts_file)?


> *In computing, a host file, stored on the computer’s filesystem, is used to look up the Internet Protocol address of a device connected to a computer network. The host file describes a many-to-one mapping of device names to IP addresses. When accessing a device by name, the networking system will attempt to locate the name within the host file if it exists. Typically, **this is used as a first means of locating the address of a system, before accessing the Internet domain name system**. The reason for this is that the host file is stored on the computer itself and does not require any network access to be used, whereas DNS requires access to an external system, which is typically slower.*


What we’re doing is redirecting a bunch of ad-specific domain names to the loopback 127.0.0.1 IP. That way, when your browser tries to download an advertising image from, say, m.doubleclick.net, it returns in under a millisecond with a 404 “file not found” error. Compare that to the time it would take to perform an actual download of a 20-50kb flash or GIF advertising file from a remote website. It’s a substantial speed boost!


I’m not aware of any negative effects of blocking ad domains this way, but I encourage you to visit the hosting page for [details](http://www.mvps.org/winhelp2002/hosts.htm). For convenience’s sake, here’s a direct link to the [zipped HOSTS file](https://web.archive.org/web/20051029032008/http://www.mvps.org/winhelp2002/hosts.zip) from the mvps site. Make a backup of your c:windowssystem32driversetchosts file, then overwrite it with the ad-blocking version contained in that zip file.

[security](https://blog.codinghorror.com/tag/security/)
[browser settings](https://blog.codinghorror.com/tag/browser-settings/)
[web performance](https://blog.codinghorror.com/tag/web-performance/)
[flash](https://blog.codinghorror.com/tag/flash/)
[add-ons](https://blog.codinghorror.com/tag/add-ons/)
