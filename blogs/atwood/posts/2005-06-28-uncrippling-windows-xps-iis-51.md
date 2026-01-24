---
title: "Uncrippling Windows XP’s IIS 5.1"
date: 2005-06-28
url: https://blog.codinghorror.com/uncrippling-windows-xps-iis-51/
slug: uncrippling-windows-xps-iis-51
word_count: 400
---

Scott Mitchell says the [best new ASP.NET feature](https://web.archive.org/web/20051217205538/http://scottonwriting.net/sowblog/posts/3447.aspx) in VS.NET 2005 is the integrated webserver. I agree. No more ditzing around with annoying IIS dependencies and install issues: aspnet_regiis, anyone? Tight coupling of VS.NET to IIS is also number three in K Scott Allen’s [worst of the .NET 1.x](http://odetocode.com/Blogs/scott/archive/2005/03/22/1118.aspx) years. Good riddance IIS, hello, [Son of Cassini](https://web.archive.org/web/20051211010245/http://dotnetjunkies.com/WebLog/anoras/archive/2005/01/04/41146.aspx)!


Unfortunately, we’re still stuck with VS.NET 2003 in the meantime, and **Windows XP’s IIS 5.1 is thoroughly crippled out of the box**. It allows only one root website, and a maximum of ten concurrent connections to that website. Microsoft really, really doesn’t want us hosting slashdot.org on our XP Pro box. These limits are so aggressive that they can get in the way of legitimate localhost development. But there are workarounds.

1. **Increase the 10 concurrent connection limit**


Are you getting 403.9 “Access Forbidden: Too many users are connected” errors on an XP Pro website? You’re limited by default to 10 concurrent connections by design, but this can be increased. First, make sure your default windows script host is set to the console (cscript.exe) one.

kg-card-begin: html

```
cscript //h:cscript
```

kg-card-end: html

Next, let’s increase the connection limit to 40.

kg-card-begin: html

```
C:InetpubAdminScriptsadsutil set w3svc/MaxConnections 40
```

kg-card-end: html

Note that this is a hard-coded limit; it can’t be increased any further unless you like patching windows system files. You can, however, make the IIS connection timeout more aggressive so connections don’t last as long.

1. **Run more than one root website**


IIS 5.1 only allows one root website. This is fine if your websites run under subfolders:

kg-card-begin: html

```
http://localhost/MyWebsite1
http://localhost/MyWebsite2
```

kg-card-end: html

But it’s kind of a pain if your websites must run as root, or need to be tested when running as root:

kg-card-begin: html

```
http://MyWebsite1/
http://MyWebsite2/
```

kg-card-end: html

In that case, you’d have to edit your [hosts file](https://web.archive.org/web/20050629080633/http://www.mvps.org/winhelp2002/hosts.htm), and switch the default home directory for the default website. But there’s a better way. You can [hack up multiple websites](http://www.xoc.net/works/tips/multiple-iis-sites-professional.asp) in IIS 5.1 via command line tricks, or you can use this [nifty little GUI utility](https://web.archive.org/web/20050716044327/http://www.firstserved.net/services/iisadmin.php) which automates that for you. It works great – you’ll even see multiple websites show up in the IIS manager. But bear in mind that, unlike the server versions of IIS, only one website can be active at any given time.

[iis](https://blog.codinghorror.com/tag/iis/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[vs.net](https://blog.codinghorror.com/tag/vs-net/)
[localhost development](https://blog.codinghorror.com/tag/localhost-development/)
