---
title: "If You Like Regular Expressions So Much, Why Don’t You Marry Them?"
date: 2005-03-22
url: https://blog.codinghorror.com/if-you-like-regular-expressions-so-much-why-dont-you-marry-them/
slug: if-you-like-regular-expressions-so-much-why-dont-you-marry-them
word_count: 317
---

All right... *will!*


I’m continually amazed how useful regular expressions are in my daily coding. I’m still working on the MhtBuilder refactoring, and I needed a function to convert all URLs in a page of HTML from relative to absolute:

kg-card-begin: html

```
<summary>
converts all relative url references  
   href="myfolder/mypage.htm"  
into absolute url references  
   href="http://mywebsite/myfolder/mypage.htm"  
</summary>  
Private Function ConvertRelativeToAbsoluteRefs(ByVal html As String) As String  
Dim r As Regex  
Dim urlPattern As String = _  
"(?<attrib>shref|ssrc|sbackground)s*?=s*?" & _  
"(?<delim1>[\"'']{0,2})(?!#|http|ftp|mailto|javascript)" & _  
"/(?<url>[^\"'>]+)(?<delim2>[\"'']{0,2})"  
Dim cssPattern As String = _  
"@imports+?(url)*['\"(]{1,2}" & _  
"(?!http)s*/(?<url>[^\"')]+)['\")]{1,2}"  
'-- href="/anything" to href="http://www.web.com/anything"  
r = New Regex(urlPattern, _  
RegexOptions.IgnoreCase Or RegexOptions.Multiline)  
html = r.Replace(html, "${attrib}=${delim1}" & _HtmlFile.UrlRoot & "/${url}${delim2}")  
'-- href="anything" to href="http://www.web.com/folder/anything"  
r = New Regex(urlPattern.Replace("/", ""), _  
RegexOptions.IgnoreCase Or RegexOptions.Multiline)  
html = r.Replace(html, "${attrib}=${delim1}" & _HtmlFile.UrlFolder & "/${url}${delim2}")  
'-- @import(/anything) to @import url(http://www.web.com/anything)  
r = New Regex(cssPattern, _  
RegexOptions.IgnoreCase Or RegexOptions.Multiline)  
html = r.Replace(html, "@import url(" & _HtmlFile.UrlRoot & "/${url})")  
'-- @import(anything) to @import url(http://www.web.com/folder/anything)  
r = New Regex(cssPattern.Replace("/", ""), _  
RegexOptions.IgnoreCase Or RegexOptions.Multiline)  
html = r.Replace(html, "@import url(" & _HtmlFile.UrlFolder & "/${url})")  
Return html  
End Function
```

kg-card-end: html

Each Regex is repeated because I have to resolve relative URLs starting with forward slashes to the webroot first – and then all remaining relative URLs to the current web folder.


One of the BCL team recently recommended [pretty-printing regular expressions](https://web.archive.org/web/20060618025054/http://blogs.msdn.com/bclteam/archive/2005/03/15/396450.aspx), e.g., using whitespace to make Regexes more readable with **RegexOptions.IgnorePatternWhitespace**. I agree completely. We do this all the time with SQL. I can think of a half-dozen tools that will block of SQL and pretty format it – but I am not aware of any Regex tools that offer this functionality. I guess I’ll email the author of [Regexbuddy](http://www.regexbuddy.com) and see what he has to say.


And here’s an interesting bit of trivia: did you know that the ASP.NET page parser [uses regular expressions](http://weblogs.asp.net/cazzu/archive/2005/01/10/RegexParsing.aspx)?

[regex](https://blog.codinghorror.com/tag/regex/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[.net](https://blog.codinghorror.com/tag/net/)
[coding practices](https://blog.codinghorror.com/tag/coding-practices/)
