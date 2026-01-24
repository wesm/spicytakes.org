---
title: "Managed HTML rendering"
date: 2004-10-15
url: https://blog.codinghorror.com/managed-html-rendering/
slug: managed-html-rendering
word_count: 533
---

At some point in any WinForms project, you’re bound to need either:

1. WYSIWYG text entry areas with text formatting
2. Quick and dirty printed report generation


The obvious choice for both of these things is HTML. No problem! I’ll just drag my **HtmlTextBox **on the form, set a few properties, and... sadly, no. That control doesn’t exist.* Instead, Microsoft helpfully provides... the**RtfTextBox**. What year is it again? 2004?


Although I am ambivalent towards HTML, there’s no question that it is a far, far better solution than the nasty, crusty old Rich Text Format. **RTF is HTML gone stupid**. If you’re ever bored and want to take on a brain-meltingly difficult project, just try writing a **RTF to HTML converter**. Oh sure, it *seems* easy enough... but I don’t think anyone can appreciate how profoundly irrational RTF is until they actually sit down and work with it in detail. Ugly doesn’t begin to cover it. Based on [my limited research](http://en.wikipedia.org/wiki/RTF), RTF seems to have evolved as the de facto document storage format for early versions of Microsoft Word, apparently based on the whims of whatever development team was working on Word that week.


To be fair, the RtfTextBox actually isn’t that bad. It’s effectively “free” as far as distribution footprint, and it will work for most basic formatting scenarios including URL and mailto: hyperlinks. In fact, Craig Andera just released a serviceable enhanced RichTextBox. The only problem is that it’s, well, RTF. Just try inserting bulleted text to see what I mean. If you’re dead set on a control that renders HTML, there’s only one solution I’m aware of in .NET: IE interop. Lots of people are doing it:

- [The HtmlEditor - a C# control that wraps MSHTML](http://www.itwriting.com/htmleditor/index.php)
- [Lutz Roeder’s HTML Writer](https://web.archive.org/web/20051101060424/http://www.gotdotnet.com/Workspaces/Workspace.aspx?id=ee974084-d5c2-44d5-a11b-b2efb96074f8)
- [HOW TO: Automate Internet Explorer Within a Contained Visual Basic .NET UserControl](https://web.archive.org/web/20041212085221/http://support.microsoft.com/?kbid=311295)
- [Windows Forms FAQ - Web Browser section](http://www.syncfusion.com/FAQ/WinForms/FAQ_c100c.asp)


And it works. Sort of. Like all **heavy duty .NET COM interop**, you can’t escape the feeling that you’re building a giant house of cards, prone to catastrophic failure at the first gentle breeze. There’s also the matter of our little friend Microsoft.mshtml.dll, a primary interop assembly weighing in at 7.8 megabytes. And god help you if a user doesn’t have IE installed on their system. Inconceivable!


While I’m not against interop per se, it seems like overkill to harness the entire bulk of IE to render a little HTML. What’s really depressing is that there are precious few options, interop or otherwise, for getting proper HTML into a WinForms app. **What I’d really like to see is a completely managed, lightweight HTML rendering control written entirely in .NET.** In other words, something with the basic features of the RtfTextBox, but using standard HTML conventions. I realize HTML rendering is not exactly trivial, but I think a smallish subset of standard HTML would meet my needs just fine.


*Well, not in this version of .NET. The WebBrowser control will be available out of the box in VS.NET 2005, but it’s the same exact hunk o’ IE interop – but this time, with a pretty Microsoft ribbon on the top.

[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[winforms](https://blog.codinghorror.com/tag/winforms/)
[html rendering](https://blog.codinghorror.com/tag/html-rendering/)
[rich text format](https://blog.codinghorror.com/tag/rich-text-format/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
