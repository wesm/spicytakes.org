---
title: "Net.WebClient and Deflate"
date: 2005-01-12
url: https://blog.codinghorror.com/net-webclient-and-deflate/
slug: net-webclient-and-deflate
word_count: 392
---

In a previous entry, [Net.WebClient and Gzip](https://blog.codinghorror.com/netwebclient-and-gzip/), I posted a code snippet that enables the missing HTTP compression in Net.WebClient, using the always handy [SharpZipLib](http://www.icsharpcode.net/OpenSource/SharpZipLib/Default.aspx).


This code eventually made it into one of my CodeProject articles. An eagle-eyed CodeProject reader noted that, while my code worked for **gzip** compression, it failed miserably for websites that use **deflate** compression. This is case of **be careful what you ask for**:

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

99% of the time, you’ll get a gzipped array of bytes back from that request. For whatever reason, **deflate compression is extremely rare on the open internet**. The same reader also helpfully provided a URL that uses deflate: Redline Networks. So that was my test case. Although SharpZipLib supports deflate compression, I had difficulty getting this to work using provided the inflator stream class. And since it’s such a rare case, I couldn’t find any working code samples.


In desperation – my [OCD](http://www.ocfoundation.org) prohibits me from letting that last 1% case go – I turned to the [only relevant Google result](https://web.archive.org/web/20050113191959/http://www.icsharpcode.net/opensource/sd/Forum/topic.asp?TOPIC_ID=893) I could find, which happens to be on the SharpZipLib community forum. Jfreilly quickly provided an answer within a day! Problem solved. He also maintains a very nice [SharpZip Library FAQ](https://web.archive.org/web/20050619233307/http://wiki.sharpdevelop.net/default.aspx/SharpZipLib.FrequentlyAskedQuestions). Kudos to you, sir.

kg-card-begin: html

```
<!-- Summary -->
<summary>
Decompresses a compressed array of bytes
via the specified HTTP compression type
</summary>
Private Function Decompress(ByVal b() As Byte, _
ByVal CompressionType As HttpContentEncoding) As Byte()
Dim s As Stream
Select Case CompressionType
Case HttpContentEncoding.Deflate
s = New Zip.Compression.Streams.InflaterInputStream( _
New MemoryStream(b), _
New Zip.Compression.Inflater(True))
Case HttpContentEncoding.Gzip
s = New GZip.GZipInputStream(New MemoryStream(b))
Case Else
Return b
End Select
Dim ms As New MemoryStream
Const intChunkSize As Integer = 2048
Dim intSizeRead As Integer
Dim unzipBytes(intChunkSize) As Byte
While True
intSizeRead = s.Read(unzipBytes, 0, intChunkSize)
If intSizeRead > 0 Then
ms.Write(unzipBytes, 0, intSizeRead)
Else
Exit While
End If
End While
s.Close()
Return ms.ToArray
End Function
```

kg-card-end: html

There is also a mysterious, [third kind of HTTP compression](http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.5), **compress**. Ok, it’s not all that mysterious, but nobody seems to use it. What’s up with that?

[.net](https://blog.codinghorror.com/tag/net/)
[webclient](https://blog.codinghorror.com/tag/webclient/)
[deflate](https://blog.codinghorror.com/tag/deflate/)
[gzip](https://blog.codinghorror.com/tag/gzip/)
