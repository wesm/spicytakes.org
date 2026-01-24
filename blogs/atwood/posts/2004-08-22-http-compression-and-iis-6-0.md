---
title: "HTTP Compression and IIS 6.0"
date: 2004-08-22
url: https://blog.codinghorror.com/http-compression-and-iis-6-0/
slug: http-compression-and-iis-6-0
word_count: 698
---

[HTTP compression](https://web.archive.org/web/20040707011055/http://webreference.com/internet/software/servers/http/compression/) is the **ultimate no-brainer**. The network is really slow, and CPU time is effectively free and getting faster and, uh, “free-er” every day. Compression typically reduces plaintext size by 75 percent: that quadruples your throughput! **Every website should be serving up HTTP compressed pages to clients that can accept it.** The client indicates ability to accept compressed contents in the request headers:

kg-card-begin: html

```

GET /blog/index.xml HTTP/1.1
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*
Accept-Language: en-us
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)
Host: www.codinghorror.com
Connection: Keep-Alive

```

kg-card-end: html

HTTP compression was available in IIS 5.0, but it was also horribly broken. I know that’s a link from a vendor selling a competing product, but I can personally vouch for this – it sucked. Don’t enable compression in IIS 5.0. It’s not worth the pain it will inevitably cause you. Fortunately, there is an alternative – the free [FlatCompression ISAPI filter](https://web.archive.org/web/20040831041843/http://www.flatcompression.org/). It’s not very sophisticated. All outgoing content of the specified mime type(s) is blindly compressed in real time with no caching, so it’s ideal for sites with mostly dynamic content. Most importantly: it actually works, unlike the built in IIS 5.0 compression, and it’s free open source. If you control an IIS 5.0 server, you should have the FlatCompression ISAPI filter installed.


One of the things I was looking forward to in IIS 6.0 was a **HTTP compression layer that actually worked.** I *thought* I had HTTP compression enabled correctly in IIS 6.0 in the Properties, Service tab, but after looking at some sniffer traces.. not quite. I followed a few walkthroughs, such as the excellent [Enabling HTTP Compression in IIS 6.0](https://web.archive.org/web/20051030012929/http://www.dotnetjunkies.com/HowTo/16267D49-4C6E-4063-AB12-853761D31E66.dcik), and I was still getting spotty results. A few observations on my troubleshooting:

- Adding the IIS compression filter .dll to the extension manager made absolutely no difference on my server. I’m not sure why people think they need to do that; It has no effect for me, and I tried it both ways a few times.
- Despite what the MS documentation says, **the metabase filename extension lists are not space delimited!** They are cr/lf delimited.
- You must restart IIS to get it to reload any changes you’ve made to the metabase.
- There appear to be some non-obvious metabase entries that will prevent compression of script output.
- Setting the file extensions to “blank” does not cause IIS to compress all content as specified in the documentation.


Getting a variety of static content extensions to compress was easy, but I had an absolute rip of a time getting dynamic script output to compress. You know, .cgi (perl), .aspx, .asmx, etc. I followed every suggestion out there with no joy – the sniffer kept showing uncompressed dynamic output coming back, but all the static files I tried came back compressed just fine. I’m still not sure which metabase setings I changed to get it to work, so I will post the current working version of the relevant IIS metabase sections in their entirety:

kg-card-begin: html

```

<IIsCompressionScheme	Location ="/LM/W3SVC/Filters/Compression/deflate"
HcCompressionDll="%windir%system32inetsrvgzip.dll"
HcCreateFlags="0"
HcDoDynamicCompression="TRUE"
HcDoOnDemandCompression="TRUE"
HcDoStaticCompression="TRUE"
HcDynamicCompressionLevel="10"
HcFileExtensions="htm
html
xml
css
txt
rdf
js"
HcOnDemandCompLevel="10"
HcPriority="1"
HcScriptFileExtensions="asp
cgi
exe
dll
aspx
asmx"
>
</IIsCompressionScheme>
<IIsCompressionScheme	Location ="/LM/W3SVC/Filters/Compression/gzip"
HcCompressionDll="%windir%system32inetsrvgzip.dll"
HcCreateFlags="1"
HcDoDynamicCompression="TRUE"
HcDoOnDemandCompression="TRUE"
HcDoStaticCompression="TRUE"
HcDynamicCompressionLevel="10"
HcFileExtensions="htm
html
xml
css
txt
rdf
js"
HcOnDemandCompLevel="10"
HcPriority="1"
HcScriptFileExtensions="asp
cgi
exe
dll
aspx
asmx"
>
</IIsCompressionScheme>
<IIsCompressionSchemes	Location ="/LM/W3SVC/Filters/Compression/Parameters"
HcCacheControlHeader="max-age=86400"
HcCompressionBufferSize="8192"
HcCompressionDirectory="%windir%IIS Temporary Compressed Files"
HcDoDiskSpaceLimiting="FALSE"
HcDoDynamicCompression="TRUE"
HcDoOnDemandCompression="TRUE"
HcDoStaticCompression="TRUE"
HcExpiresHeader="Wed, 01 Jan 1997 12:00:00 GMT"
HcFilesDeletedPerDiskFree="256"
HcIoBufferSize="8192"
HcMaxDiskSpaceUsage="99614720"
HcMaxQueueLength="1000"
HcMinFileSizeForComp="1"
HcNoCompressionForHttp10="FALSE"
HcNoCompressionForProxies="FALSE"
HcNoCompressionForRange="FALSE"
HcSendCacheHeaders="FALSE"
>
</IIsCompressionSchemes>

```

kg-card-end: html

The last things I tried were modifying the HcNoCompression* settings, and turning HcDoStaticCompression on for gzip. It’s likely one of those.


I enabled HTTP compression for the .cgi script filetype, which covers the PERL scripts that Movable Type uses, and the interface was just blasting on the screen after I did that. **It’s truly amazing how much faster pages appear to load, even over a 100baseT local network, with HTTP compression enabled. **It is dramatic. I can only imagine how much snappier pages load over a remote network.

[http compression](https://blog.codinghorror.com/tag/http-compression/)
[iis 6.0](https://blog.codinghorror.com/tag/iis-6-0/)
[networking](https://blog.codinghorror.com/tag/networking/)
[website performance](https://blog.codinghorror.com/tag/website-performance/)
[compression techniques](https://blog.codinghorror.com/tag/compression-techniques/)
