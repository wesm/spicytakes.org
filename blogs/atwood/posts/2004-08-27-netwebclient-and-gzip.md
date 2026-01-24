---
title: "Net.WebClient and GZip"
date: 2004-08-27
url: https://blog.codinghorror.com/netwebclient-and-gzip/
slug: netwebclient-and-gzip
word_count: 204
---

The Net.WebClient class doesn’t support HTTP compression, e.g., when you add the **Accept-Encoding: gzip,deflate** header to your request:

kg-card-begin: html

```
Dim wc As New Net.WebClient
'-- google will not gzip the content if the User-Agent header is missing!
wc.Headers.Add("User-Agent", strHttpUserAgent)
wc.Headers.Add("Accept-Encoding", "gzip,deflate")
'-- download the target URL into a byte array
Dim b() As Byte = wc.DownloadData(strUrl)
```

kg-card-end: html

What you get is a gzipped array of bytes. It’s pretty easy to add the missing gzip support, though. First, download the [SharpZipLib](http://www.icsharpcode.net/OpenSource/SharpZipLib/Default.aspx%22?ref=blog.codinghorror.com) and add a reference to **ICSharpCode.SharpZipLib** to your project. Then it’s only a few more lines of code...

kg-card-begin: html

```
Dim gz As New GZip.GZipInputStream(New MemoryStream(b))
Dim intSizeRead As Integer
Dim unzipBytes(intChunkSize) As Byte
Dim OutputStream As New MemoryStream
While True
'-- this decompresses a chunk
'-- remember the output will be larger than the input (one would hope)
intSizeRead = gz.Read(unzipBytes, 0, intChunkSize)
If intSizeRead > 0 Then
OutputStream.Write(unzipBytes, 0, intSizeRead)
Else
Exit While
End If
End While
'-- convert our decompressed bytestream into a UTF-8 string
Return System.Text.Encoding.UTF8.GetString(OutputStream.ToArray)
```

kg-card-end: html

And voila, the bandwidth, you have saved eet! How do I know this actually works? Using my network sniffer of course...

[c#](https://blog.codinghorror.com/tag/c-2/)
[.net](https://blog.codinghorror.com/tag/net/)
[gzip](https://blog.codinghorror.com/tag/gzip/)
[webclient](https://blog.codinghorror.com/tag/webclient/)
[sharpziplib](https://blog.codinghorror.com/tag/sharpziplib/)
