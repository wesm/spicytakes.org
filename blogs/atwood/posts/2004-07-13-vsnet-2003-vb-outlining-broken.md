---
title: "VS.NET 2003 VB outlining broken"
date: 2004-07-13
url: https://blog.codinghorror.com/vsnet-2003-vb-outlining-broken/
slug: vsnet-2003-vb-outlining-broken
word_count: 611
---

Evidently the [VB code outlining support](https://web.archive.org/web/20050306135017/http://searchvb.techtarget.com/vsnetATEAnswers/0,293820,sid8_gci954119_tax293475,00.html\) is completely broken in VS.NET 2003. Why hasn’t this gotten more publicity?


We used the code outlining features all the time at work in 2002, and they worked great. But after switching to VS.NET 2003 we noticed that selecting Edit, Outlining, Toggle All Outlining does **nothing** in VS.NET 2003 for VB code. Not only that, but turning off Tools, Options, Text Editor, Basic, VB Specific, “Enter outlining mode when files off” doesn’t work either. Doh! I can’t believe this hasn’t been fixed yet in a patch for VS.NET 2003, because it makes working with #Region – which we use a lot – pretty much impossible.


I searched around for a bit and found this [blog entry by Roland Weigelt](http://weblogs.asp.net/rweigelt/archive/2003/07/06/9741.aspx). While it’s not a fix, per se, it does add support for #Region outlining at the very least. I was not able to get the code he posted to work, rather, I used the code posted in the comments by Andrew Eno:

kg-card-begin: html

```
Imports EnvDTE
Imports System.Diagnostics
' Macros for improving keyboard support for "#region ... #endregion"
Public Module RegionTools
' Expands all regions in the current document
Sub ExpandAllRegions()
Dim objSelection As TextSelection ' Our selection object
DTE.SuppressUI = True ' Disable UI while we do this
objSelection = DTE.ActiveDocument.Selection() ' Hook up to the ActiveDocument's selection
objSelection.StartOfDocument() ' Shoot to the start of the document
' Loop through the document finding all instances of #region. This action has the side benefit
' of actually zooming us to the text in question when it is found and ALSO expanding it since it
' is an outline.
Do While objSelection.FindText("#region", vsFindOptions.vsFindOptionsMatchInHiddenText)
' This next command would be what we would normally do *IF* the find operation didn't do it for us.
'DTE.ExecuteCommand("Edit.ToggleOutliningExpansion")
Loop
objSelection.StartOfDocument() ' Shoot us back to the start of the document
DTE.SuppressUI = False ' Reenable the UI
objSelection = Nothing ' Release our object
End Sub
' Collapses all regions in the current document
Sub CollapseAllRegions()
Dim objSelection As TextSelection ' Our selection object
ExpandAllRegions() ' Force the expansion of all regions
DTE.SuppressUI = True ' Disable UI while we do this
objSelection = DTE.ActiveDocument.Selection() ' Hook up to the ActiveDocument's selection
objSelection.EndOfDocument() ' Shoot to the end of the document
' Find the first occurence of #region from the end of the document to the start of the document. Note:
' Note: Once a #region is "collapsed" .FindText only sees it's "textual descriptor" unless
' vsFindOptions.vsFindOptionsMatchInHiddenText is specified. So when a #region "My Class" is collapsed,
' .FindText would subsequently see the text 'My Class' instead of '#region "My Class"' for the subsequent
' passes and skip any regions already collapsed.
Do While (objSelection.FindText("#region", vsFindOptions.vsFindOptionsBackwards))
DTE.ExecuteCommand("Edit.ToggleOutliningExpansion") ' Collapse this #region
objSelection.EndOfDocument() ' Shoot back to the end of the document for
' another pass.
Loop
objSelection.StartOfDocument() ' All done, head back to the start of the doc
DTE.SuppressUI = False ' Reenable the UI
objSelection = Nothing ' Release our object
End Sub
End Module
```

kg-card-end: html

To install, use the steps Roland outlined:

- Open the Macros IDE (Tools - Macros - Macros IDE)
- Create a new module “RegionTools,” replace the code in the created file with the posted source code, save file.
- Assign keys in VS.Net (Tools - Options - Environment - Keyboard).


As he mentions, type “Region” in the “show commands containing” section of the keyboard mapper to filter the commands to the ones in RegionTools. I used CTRL+SHIFT+Left and CTRL+SHIFT+Right, bound only to the Text Editor (not Global).


Thanks Roland and Andrew for your tips!

[outlining](https://blog.codinghorror.com/tag/outlining/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[vb](https://blog.codinghorror.com/tag/vb/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[bug-fix](https://blog.codinghorror.com/tag/bug-fix/)
