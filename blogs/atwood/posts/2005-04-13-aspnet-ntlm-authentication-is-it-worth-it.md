---
title: "ASP.NET NTLM Authentication - is it worth it?"
date: 2005-04-13
url: https://blog.codinghorror.com/aspnet-ntlm-authentication-is-it-worth-it/
slug: aspnet-ntlm-authentication-is-it-worth-it
word_count: 736
---

At work, we have the luxury of assuming that everyone’s on an intranet. So when it comes to identity management on our ASP.NET websites, [NTLM authentication](https://web.archive.org/web/20050930202957/http://dotnetjunkies.com/Article/6B31D299-347C-4B85-82C5-954546165C80.dcik) is the go-to solution. Why trouble the user with Yet Another Login Dialog when you can leverage the built in NTLM functionality of IIS and Internet Explorer? Just reach in and grab one of these `Request.ServerVariables` passed in through the HTTP headers:

kg-card-begin: html

```
LOGON_USER  = HOMESERVERJeff
AUTH_USER   = HOMESERVERJeff
REMOTE_USER = HOMESERVERJeff
```

kg-card-end: html

I don’t pretend to understand the subtle difference between these three fields; [this CodeProject article](https://web.archive.org/web/20050723003554/http://www.codeproject.com/asp/request_server_variables.asp) has some hints. At any rate, at least one of them will contain the domainusername of the user accessing our web page. And it’s free – as long as you define “free” as **three browser round trips**:

kg-card-begin: html

GET /WebApplication1/WebForm2.aspx HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)
Host: homeserver
Connection: Keep-Alive
HTTP/1.1 401 Unauthorized
Content-Length: 1656
Content-Type: text/html
Server: Microsoft-IIS/6.0
WWW-Authenticate: NTLM
WWW-Authenticate: Basic realm="homeserver"
Date: Thu, 14 Apr 2005 02:59:26 GMT
GET /WebApplication1/WebForm2.aspx HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)
Host: homeserver
Connection: Keep-Alive
Authorization: NTLM
TlRMTVNTUAABAAAAB7IIogQABAAwAAAACAAIACgAAAAFASgKAAAAD1dVTVBVUzY0SE9NRQ=
=
HTTP/1.1 401 Unauthorized
Content-Length: 1539
Content-Type: text/html
Server: Microsoft-IIS/6.0
WWW-Authenticate: NTLM 
TlRMTVNTUAACAAAAFAAUADgAAAAFgoqiMixeuxRDQq8AAAAAAAAAAKgAqABMAAAABQLO
DgAAAA9IAE8ATQBFAFMARQBSAFYARQBSAAIAFABIAE8ATQBFAFMARQBSAFYARQBSAAEAFABIAE8ATQ
BFAFMARQBSAFY
ARQBSAAQANgBoAG8AbQBlAHMAZQByAHYAZQByAC4AYwBvAGQAaQBuAGcAaABvAHIAcgBvAHIALgBjA
G8AbQADADYAaA
BvAG0AZQBzAGUAcgB2AGUAcgAuAGMAbwBkAGkAbgBnAGgAbwByAHIAbwByAC4AYwBvAG0AAAAAAA==
Date: Thu, 14 Apr 2005 02:59:26 GMT
GET /WebApplication1/WebForm2.aspx HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)
Host: homeserver
Authorization: NTLM 
TlRMTVNTUAADAAAAGAAYAGwAAAAYABgAhAAAAAwADABIAAAACAAIAFQAAAAQABAAXAAAAAA
AAACcAAAABYKIogUBKAoAAAAPVwBVAE0AUABVAFMASgBlAGYAZgBXAFUATQBQAFUAUwA2ADQAhUEDu
dJHhNcAAAAAAA
AAAAAAAAAAAAAA74hHe6W7Di69Hgo553hEc7OZLaIizpzh
HTTP/1.1 200 OK
Cache-Control: private
Date: Thu, 14 Apr 2005 02:59:26 GMT
Content-Type: text/html; charset=utf-8
Server: Microsoft-IIS/6.0
Set-Cookie: ASP.NET_SessionId=0nispyqogdrmpjyxnzxe2b55; path=/
Content-Encoding: gzip
Vary: Accept-Encoding
Transfer-Encoding: chunked

kg-card-end: html

This is the classic challenge-response handshaking sequence that Eric Lippert described in his recent entry, [You Want Salt With That? Part Four](https://web.archive.org/web/20051124011600/http://blogs.msdn.com/ericlippert/archive/2005/02/07/368569.aspx): Challenge-Response. And it really does work; no passwords are ever transmitted, and yet we know exactly who the user is.


Although it is delightfully easy to implement, NTLM authentication carries a **hefty performance cost**. How hefty? The last time I benchmarked it, almost 1000ms per request, compared to under 20ms for anonymous requests. And there are a lot of other caveats, too:

- IE will only send NTLM credentials *automatically* to sites it deems [in the “Intranet Zone”](https://web.archive.org/web/20051202014615/http://cyberforge.com/weblog/aniltj/archive/2004/10/25/705.aspx). Websites in any other security zone will pop up a login prompt.
- NTLM credentials typically don’t make it [through a proxy](https://web.archive.org/web/20220712055448/https://groups.google.com/g/microsoft.public.isa/c/uj_76Gcqu-c), so you must enable Basic authentication in addition to NTLM, otherwise you risk permanently blocking a chunk of your userbase from your application. And Basic authentication is, uh, unsecure. Like “barely better than plain text” unsecure.
- If you have users coming in from multiple domains, you must set authentication to use “all domains” via [the backslash trick](https://web.archive.org/web/20060216160540/http://support.microsoft.com/?id=827991). This leads to another problem: if users have accounts with the same name in other domains, those accounts will take priority.
- All new folders in IIS default to Integrated and Anonymous authentication. This seems contradictory; will NTLM be used, or will everyone map to the anonymous account? The Windows Server 2003 Directory Security dialog clarifies this at long last: anonymous will be used unless NTFS access control lists are specified on that folder. And how do we know that, exactly?
- It’s also possible to control authentication via ASP.NET’s <authorization> Web.config section. But this *only* works if the IIS Directory Security settings are left at their default of Integrated and Anonymous. IIS settings will overrule whatever you specify in Web.config.
- Integrated authentication checks the user’s Windows account at the time they access your website. If there is any problem with a given user’s Windows account, they won’t be able to access your website. Is that user temporarily locked out? Password expired? Must change password at next logon? Are there network problems preventing your webserver from communicating with other domains? This inevitably results in a lot of user complaints that “I can’t get to your intranet site, but all the others work – what’s wrong with your site?” Those other sites don’t use NTLM. And I am put in the uncomfortable position of troubleshooting people’s Windows accounts so they can get to our website.


I used to be a big believer in NTLM authentication in ASP.NET. However, after living with it for the last two years, I’m starting to wonder if we wouldn’t all be better off with Yet Another Login Dialog.

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[ntlm authentication](https://blog.codinghorror.com/tag/ntlm-authentication/)
[iis](https://blog.codinghorror.com/tag/iis/)
[http headers](https://blog.codinghorror.com/tag/http-headers/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
