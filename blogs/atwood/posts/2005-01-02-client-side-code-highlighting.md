---
title: "Client-Side code highlighting"
date: 2005-01-02
url: https://blog.codinghorror.com/client-side-code-highlighting/
slug: client-side-code-highlighting
word_count: 212
---

When I visited [Alex Gorbatchev’s blog](https://web.archive.org/web/20051210160512/http://blog.dreamprojections.com/), I noticed he had a unique client-side code highlighting solution in place, one I hadn’t seen anywhere else. That’s something I’ve wanted on my blog for a while; the vanilla <PRE> sections I’ve been using are serviceable, but primitive. Although [I loves me some Regex](https://blog.codinghorror.com/my-buddy-regex/), I don’t know squat about PERL so I’ve been hesitant to hack anything fancier into my Movable Type install.


After I asked Alex about his solution, he was nice enough to package up his [JavaScript syntax highlighter as dp.SyntaxHighlighter](https://web.archive.org/web/20051122165346/http://blog.dreamprojections.com/archive/2005/01/01/461.aspx). It’s really quite slick, and it works with all kinds of code: C#, VB.NET, JavaScript, PHP, SQL, and XML. Here’s a VB.NET sample:

kg-card-begin: html

```
Public Function GetGoogleWordFrequency(ByVal strWord As String) As Integer
Dim strUrl As String = "http://www.google.com/search?num=1&q=" & _
Web.HttpUtility.UrlEncode(strWord)
Dim wc As New WebClientGzip
Dim strPageContents As String = wc.DownloadDataGzip(strUrl)
Dim m As Match
m = Regex.Match(strPageContents, _
"results.*?d+.*?d+.*?of about.*?(?[d,]+)", _
RegexOptions.IgnoreCase)
If Not m Is Nothing Then
Dim strResults As String = m.Groups("TotalResults").ToString
If strResults.Length > 0 Then
Return Convert.ToInt32(strResults.Replace(",", ""))
End If
End If
Return -1
End Function
```

kg-card-end: html

Alex tested this JavaScript on FireFox and IE6, and is looking for compatibility feedback on other browsers.

[javascript](https://blog.codinghorror.com/tag/javascript/)
[syntax highlighting](https://blog.codinghorror.com/tag/syntax-highlighting/)
[code highlighter](https://blog.codinghorror.com/tag/code-highlighter/)
[client-side](https://blog.codinghorror.com/tag/client-side/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
