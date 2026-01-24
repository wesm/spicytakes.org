---
title: "Shortening Long File Paths"
date: 2006-08-02
url: https://blog.codinghorror.com/shortening-long-file-paths/
slug: shortening-long-file-paths
word_count: 331
---

We’re working on a little shell utility that displays paths in a menu. Some of these paths can get rather long, so I cooked up this little regular expression to shorten them. It’s a replacement, so you call it like this:

kg-card-begin: html

static string PathShortener(string path)

{

    const string pattern = @"^(w+:|)([^]+[^]+).*([^]+[^]+)$";

    const string replacement = "$1$2...$3";

    if (Regex.IsMatch(path, pattern))

    {

        return Regex.Replace(path, pattern, replacement);

    }

    else

    {

        return path;

    }          

}


kg-card-end: html
So, for these paths:
kg-card-begin: html


C:Documents and SettingsjatwoodMy DocumentsVisual Studio
 2005SimpleEncryptionUnitTestsUnitTests.vb
wumpuspublicHilo DeliverablesHilo
 FinalIntroductionCodeIntroApp_Themescellphonephoto-small.jpg


kg-card-end: html
The result is:
kg-card-begin: html


C:Documents and Settingsjatwood...UnitTestsUnitTests.vb
wumpuspublic...cellphonephoto-small.jpg


kg-card-end: html
The general strategy is to **keep the first two folders at the beginning, replace the middle with an ellipsis, and leave the final folder and filename on the end.**After spending an hour dinking around with this and testing it on a bunch of paths, a colleague pointed me to the Windows API call [PathCompactPathEx](http://www.pinvoke.net/default.aspx/shlwapi/PathCompactPathEx.html), which (almost) does the same thing. Doh!
kg-card-begin: html


[DllImport("shlwapi.dll", CharSet = CharSet.Auto)]

static extern bool PathCompactPathEx([Out] StringBuilder pszOut, string szPath, int cchMax, int dwFlags);


static string PathShortener(string path, int length)

{

    StringBuilder sb = new StringBuilder();

    PathCompactPathEx(sb, path, length, 0);

    return sb.ToString();

}




kg-card-end: html
As you can see from the [API definition for PathCompactPathEx](https://web.archive.org/web/20070315042539/http://msdn.microsoft.com/library/en-us/shellcc/platform/shell/reference/shlwapi/path/pathcompactpathex.asp), this works a little differently. It lets you set an absolute length for the path, and displays as many characters as it can with a “best fit” placement of the ellipsis. Here’s the output for our two paths:
kg-card-begin: html


C:Documents and Settingsjatwood...UnitTests.vb
wumpuspublicHilo Deliverab...photo-small.jpg


kg-card-end: html
So, which to choose? **CompactPathEx guarantees that the paths will always be exactly (x) characters while displaying as much as it can, but it may not be able to split cleanly. **My regex always splits cleanly, but makes no guarantees on length.And obviously, if you’re not running Windows, or if you don’t care for p/invoke, the API call is clearly out.

[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[file paths](https://blog.codinghorror.com/tag/file-paths/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[shell utility](https://blog.codinghorror.com/tag/shell-utility/)
[path shortening](https://blog.codinghorror.com/tag/path-shortening/)
