---
title: "Formatting HTML code snippets with Ten Ton Wrecking Balls"
date: 2005-06-14
url: https://blog.codinghorror.com/formatting-html-code-snippets-with-ten-ton-wrecking-balls/
slug: formatting-html-code-snippets-with-ten-ton-wrecking-balls
word_count: 854
---

If you’ve ever tried to cut and paste code from the VS.NET IDE, you may have noticed that the code generally comes across looking like crap. The root of this problem is that VS.NET copies code into your clipboard in the [accursed Rich Text Format](https://blog.codinghorror.com/managed-html-rendering/). If you were expecting something like standard HTML, *think again, bucko!*


Brad Abrams posted a quick and dirty workaround to convert the [clipboard to HTML using Word](https://web.archive.org/web/20051212012212/http://blogs.msdn.com/brada/archive/2004/10/05/238427.aspx). Cory Smith took that workaround and turned it into a [VS.NET Macro](http://addressof.com/blog/archive/2004/10/06/966.aspx). It works fairly well, but...

- Using Word automation to color-code a code snippet in your clipboard is... not exactly lightweight. But my motto is, **why use a hammer when you can use a frickin’ ten ton wrecking ball?!**
- Word doesn’t seem to pick up background colors, only foreground colors. That’s kind of a bummer.
- The resulting HTML is kinda nasty, even though we are specifically asking for Word’s simplified “filtered” HTML. But it does work in Firefox and IE just fine.


I experimented with Cory’s macro, simplifying it slightly, and forcing a standard font. (I normally use a [custom font for programming](https://blog.codinghorror.com/progamming-fonts/), but not everyone will have that font installed.)


I knew Word’s HTML wasn’t going to be optimal, but after taking a closer look at it, I was profoundly unhappy with it. The fact that copying and pasting it back into VS.NET resulted in extra line breaks was kind of a showstopper, too. Here’s a little taste:

kg-card-begin: html

```
<P class=MsoNormal style="MARGIN: 0in 0in 0pt">
<SPAN style="FONT-SIZE: 9pt; FONT-FAMILY: 'Courier New';
mso-bidi-font-size: 12.0pt">&nbsp;<o:p></o:p>
```

kg-card-end: html

If this is Word’s idea of “filtered” HTML, I’d hate to see the unfiltered version. And what’s up with those empty <o:p> tags all over the place? After I figured out the threading issue preventing me from accessing the clipboard in a macro, I added some code to postfix Word’s crazy HTML into something resembling standard, basic HTML. This worked OK.


But then I wondered – **why not convert the native RTF on the clipboard to HTML myself and cut out the middleman?** I’m all for using ten ton wrecking balls, but not when they er... wreck stuff! Fortunately, I’ve written RTF to HTML converters before, and even more fortunately, VS.NET only uses a tiny subset of RTF to place colored code on the clipboard. Here’s the main conversion function:

kg-card-begin: html

```
<Private Function RtfToHtml(ByVal rtf As String) As String>
<Const tabSpaces As String = "&nbsp;&nbsp;&nbsp;&nbsp;">
<!-- remove line breaks -->
rtf = Regex.Replace(rtf, "[nrf]", "")
<!-- parse RTF color table -->
Dim colorTable As New Collections.Hashtable
Dim i As Integer = 1
For Each m As Match In Regex.Matches(rtf, _
"red(?<red>\d+)green(?<green>\d+)blue(?<blue>\d+);")
colorTable.Add(i, HtmlColor(m))
i += 1
Next
<!-- remove header and footer RTF tags -->
rtf = Regex.Replace(rtf, "{rtf1[^\s]+\s", "")
rtf = Regex.Replace(rtf, "}$", "")
rtf = Regex.Replace(rtf, "deff0{fonttbl{fd+\[^}]+}}", "")
rtf = Regex.Replace(rtf, "{colortbl;(red\d+green\d+blue\d+;)+}", "")
<!-- fix escaped C# brackets -->
rtf = Regex.Replace(rtf, "{", "{")
rtf = Regex.Replace(rtf, "}", "}")
<!-- replace any HTML-specific characters -->
rtf = Web.HttpUtility.HtmlEncode(rtf)
<!-- convert RTF tags to HTML tags -->
rtf = Regex.Replace(rtf, "tabs", tabSpaces)
rtf = Regex.Replace(rtf, "pars", "<br/>" & Environment.NewLine)
<!-- remove unmapped RTF tags -->
rtf = Regex.Replace(rtf, "fs(?<size>\d+)\s", "")
rtf = Regex.Replace(rtf, "cbd+highlightd+\s", "")
<!-- map foreground color RTF tags using <font> tag -->
rtf = Regex.Replace(rtf, "cf0\s", "</span><span style='color:black'>")
For Each m As Match In Regex.Matches(rtf, "cf(?<num>\d+)\s")
i = Convert.ToInt32(m.Groups("num").Value)
rtf = Regex.Replace(rtf, "cf" & i & "\s", _
"</span><span style='color:" & colorTable.Item(i) & "'>")
Next
<!-- fix up orphaned spans at start and end -->
rtf = Regex.Replace(rtf, "(^.*?)</span>", "$1")
rtf = rtf & "</span>"
<!-- convert remaining spaces to HTML spaces -->
rtf = Regex.Replace(rtf, "  ", "&nbsp;&nbsp;")
<!-- add wrapping div -->
rtf = "<div style='font-family:" & CodeFontName & _
"; font-size: " & CodeFontSize & "pt;'>" & _
rtf & "</div>"
Return rtf
<End Function>
```

kg-card-end: html

All this RTF spelunking revealed an interesting fact. I’ve always been disappointed that none of the copied code had background color highlighting. Well, that’s because **the RTF on the clipboard doesn’t contain any of the background colors!** The actual background formatting codes are there, but there are absolutely no entries in the RTF color table for them. Weird.

kg-card-begin: html
**Update 4/2006:**
I have a
[much improved RTF conversion macro](https://blog.codinghorror.com/copying-visual-studio-code-snippets-to-the-clipboard-as-html/)
. This macro is only interesting for historical reasons, or if you need the Word interop conversion.
kg-card-end: html

Anyway, here’s the full FormatToHtml macro (zip). It contains the direct RTF clipboard to HTML conversion, as well as the RTF clipboard to Word clipboard to HTML conversion. To get started:

1. go to Tools - Macros - IDE
2. create a new Module named “FormatToHtml” under “MyMacros”
3. paste the downloaded code into the module
4. add references to System.Drawing, System.Web, and System.Windows.Forms via the Add Reference menu
5. save and close the macro IDE window
6. go to Tools - Macros - Macro Explorer
7. two new macros named “UsingWord” and “UsingRtfConversion” will be under “FormatToHtml:”


![](https://blog.codinghorror.com/content/images/2025/05/image-149.png)


Double-click to run the macro, then paste away...

[html](https://blog.codinghorror.com/tag/html/)
[vs.net](https://blog.codinghorror.com/tag/vs-net/)
[ide](https://blog.codinghorror.com/tag/ide/)
[clipboard](https://blog.codinghorror.com/tag/clipboard/)
[code snippets](https://blog.codinghorror.com/tag/code-snippets/)
