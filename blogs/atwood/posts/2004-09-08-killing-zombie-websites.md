---
title: "Killing Zombie Websites"
date: 2004-09-08
url: https://blog.codinghorror.com/killing-zombie-websites/
slug: killing-zombie-websites
word_count: 181
---

Isn’t it annoying how **deleting a folder from your wwwroot$ doesn’t automatically remove the corresponding website in IIS**? You have to go into IIS and delete the website. If you’re lazy like me, you probably have about a dozen left-over zombie websites waiting to be deleted (or eat some brains).


Well, there is a better way. Remember those hoary old [FrontPage extensions](https://web.archive.org/web/20041025015831/http://www.iisfaq.com/Default.aspx?tabid=2447)? The Microsoft proprietary version of [WebDAV](http://www.webdav.org/)? Well, they’re still around. At some point in 2002 the FrontPage extensions were brought under the [SharePoint](http://www.microsoft.com/sharepoint/) umbrella. I still don’t fully understand the nature of this relationship, but you may see it referred to by either name.


There’s a handy [Check Server Health](https://web.archive.org/web/20050610074631/http://www.microsoft.com/resources/documentation/sts/2001/all/proddocs/en-us/admindoc/owsi02.mspx) page in the FrontPage Site Administration tool that lets you auto-repair all webs.


Select **Repair** and **Detect** for **Verify existence of webs**, then click OK. This removes all orphaned websites at once. Easy! One caveat: if you are running a real non-crippled IIS, the FrontPage/Sharepoint extensions will show up as another website on an alternate port, instead of as a subfolder.

[iis](https://blog.codinghorror.com/tag/iis/)
[frontpage extensions](https://blog.codinghorror.com/tag/frontpage-extensions/)
[sharepoint](https://blog.codinghorror.com/tag/sharepoint/)
[website management](https://blog.codinghorror.com/tag/website-management/)
[server health.](https://blog.codinghorror.com/tag/server-health/)
