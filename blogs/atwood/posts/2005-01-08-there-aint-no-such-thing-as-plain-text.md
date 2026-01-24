---
title: "There Ain’t No Such Thing as Plain Text"
date: 2005-01-08
url: https://blog.codinghorror.com/there-aint-no-such-thing-as-plain-text/
slug: there-aint-no-such-thing-as-plain-text
word_count: 764
---

Over the last few months, I’ve come to realize that **I had an ugly American view of strings**. I always wondered what those crazy foreigners were complaining about in their comments on my CodeProject articles, and now I know: there ain’t no such [thing as plain text:](http://www.joelonsoftware.com/articles/Unicode.html)


> *If you have a string, in memory, in a file, or in an email message, you have to know what encoding it is in or you cannot interpret it or display it to users correctly. Almost every stupid “my website looks like gibberish” or “she can’t read my emails when I use accents” problem comes down to one naive programmer who didn’t understand the simple fact that if you don’t tell me whether a particular string is encoded using UTF-8 or ASCII or ISO 8859-1 (Latin 1) or Windows 1252 (Western European), you simply cannot display it correctly or even figure out where it ends. There are over a hundred encodings and above code point 127, all bets are off.
> How do we preserve this information about what encoding a string uses? Well, there are standard ways to do this. For an email message, you are expected to have a string in the header of the form*
> `Content-Type: text/plain; charset="UTF-8"`
> *For a web page, the original idea was that the web server would return a similar Content-Type http header along with the web page itself -- not in the HTML itself, but as one of the response headers that are sent before the HTML page.
> This causes problems. Suppose you have a big web server with lots of sites and hundreds of pages contributed by lots of people in lots of different languages and all using whatever encoding their copy of Microsoft FrontPage saw fit to generate. The web server itself wouldn’t really know what encoding each file was written in, so it couldn’t send the Content-Type header.
> It would be convenient if you could put the Content-Type of the HTML file right in the HTML file itself, using some kind of special tag. Of course this drove purists crazy... how can you read the HTML file until you know what encoding it’s in?! Luckily, almost every encoding in common use does the same thing with characters between 32 and 127, so you can always get that far on the HTML page without starting to use funny letters.*


In my case, this applies absolutely. **I was doing a naïve, blanket UTF-8 conversion of this byte data**, assuming I got back something of type “text/*”:

kg-card-begin: html

```
        Dim wc As New Net.WebClient
wc.Headers.Add("User-Agent", _strHttpUserAgent)
wc.Headers.Add("Accept-Encoding", _strAcceptedEncodings)
Dim b() As Byte = wc.DownloadData(strUrl)
```

kg-card-end: html

Clearly this isn’t right. It is right *most of the time*, which can lull you into a false sense of correctness. A lot of things are like that in software; you think you have it right, but you just haven’t hit the edge conditions yet. I found [a code sample](https://web.archive.org/web/20040617041905/http://weblogs.asp.net/feroze_daud/archive/2004/03/30/104440.aspx) on Feroze Daud’s blog that demonstrates how to semi-correctly detect the HTML encoding, as described by Joel. I thought it could be further improved.


Here’s my take:

kg-card-begin: html

```
<!-- Summary -->
<summary>
Attempt to convert this charset string into a named .NET text encoding
</summary>
Private Function CharsetToEncoding(ByVal Charset As String) _
As System.Text.Encoding
If Charset = "" Then Return Nothing
Try
Return System.Text.Encoding.GetEncoding(Charset)
Catch ex As System.ArgumentException
Return Nothing
End Try
End Function
<!-- Summary -->
<summary>
Given the Content-Type header, try to determine string encoding
using header and raw content bytes
"Content-Type: text/html; charset=us-ascii"
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</summary>
Private Function GetEncoding(ByVal ContentTypeHeader As String, _
ByVal ResponseBytes() As Byte) As System.Text.Encoding
If Not _blnDetectEncoding Then
Return _DefaultEncoding
End If
Dim strCharset As String
Dim encoding As System.Text.Encoding
'-- first try the header
strCharset = Regex.Match(ContentTypeHeader, "charset=([^;\\"'/>]+)", _
RegexOptions.IgnoreCase).Groups(1).ToString.ToLower
encoding = CharsetToEncoding(strCharset)
'-- if we can't get it from header, try the body bytes
If encoding Is Nothing Then
strCharset = Regex.Match( _
System.Text.Encoding.ASCII.GetString(ResponseBytes), _
"]+content-type[^>]+charset=([^;\\"'/>]+)", _
RegexOptions.IgnoreCase).Groups(1).ToString.ToLower
encoding = CharsetToEncoding(strCharset)
If encoding Is Nothing Then
Return _DefaultEncoding
End If
End If
Return encoding
End Function
```

kg-card-end: html

Between the raw bytes from the HTTP response, and the Content-Type HTTP header, we should be able to get something reasonable. I use UTF-8 as my default if no encoding can be determined, which as near as I can tell is a best practice with strings in .NET. **I apologize to all the non-English speaking users of my CodeProject articles **–** **I’m fixing it!

[unicode](https://blog.codinghorror.com/tag/unicode/)
[encoding](https://blog.codinghorror.com/tag/encoding/)
[plain text](https://blog.codinghorror.com/tag/plain-text/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[character encoding](https://blog.codinghorror.com/tag/character-encoding/)
