---
title: "Cleaning Word’s Nasty HTML"
date: 2006-01-09
url: https://blog.codinghorror.com/cleaning-words-nasty-html/
slug: cleaning-words-nasty-html
word_count: 452
---

I recently wrote a Word 2003 document that I later turned into a [blog post](https://web.archive.org/web/20060115032619/http://blogs.vertigosoftware.com/jatwood/archive/2006/01/06/Guidelines_and_Tips_for_Pure_CSS_Layouts.aspx). The transition between Word doc and HTML presented some problems. Word offers two HTML options in its save dialog: “Save as HTML” and “Save as Filtered HTML.” In practice, that means **you get to choose between totally nasty HTML and slightly less nasty HTML.**


I searched around for any existing Word cleanup solutions and found the [Textism Word HTML Cleaner](http://textism.com/wordcleaner/), and Tim Mackey’s [set of regular expressions](https://web.archive.org/web/20060128210548/http://tim.mackey.ie/CleanWordHTMLUsingRegularExpressions.aspx). The Textism solution is great, but requires a subscription for files over 20kb. And I wasn’t quite happy with Tim’s regular expressions, either. So I created my own Word HTML cleanup solution.


This c# 2.0 code removes all unnecessary cruft from Word documents saved as HTML, stripping the HTML down to the bare-bones basics:

kg-card-begin: html

```

static void Main(string[] args)
{
if (args.Length == 0 || String.IsNullOrEmpty(args[0]))
{
Console.WriteLine("No filename provided.");
return;
}
string filepath = args[0];
if (Path.GetFileName(filepath) == args[0])
{
filepath = Path.Combine(Environment.CurrentDirectory, filepath);
}
if (!File.Exists(args[0]))
{
Console.WriteLine("File doesn't exist.");
}
string html = File.ReadAllText(filepath);
Console.WriteLine("input html is " + html.Length + " chars");
html = CleanWordHtml(html);
html = FixEntities(html);
filepath = Path.GetFileNameWithoutExtension(filepath) + ".modified.htm";
File.WriteAllText(filepath, html);
Console.WriteLine("cleaned html is " + html.Length + " chars");
}
static string CleanWordHtml(string html)
{
StringCollection sc = new StringCollection();
// get rid of unnecessary tag spans (comments and title)
sc.Add(@"<!--(w|W)+?-->");
sc.Add(@"<title>(w|W)+?</title>");
// Get rid of classes and styles
sc.Add(@"s?class=w+");
sc.Add(@"s+style='[^']+'");
// Get rid of unnecessary tags
sc.Add(
@"<(meta|link|/?o:|/?style|/?div|/?std|/?head|/?html|body|/?body|/?span|![)[^>]*?>");
// Get rid of empty paragraph tags
sc.Add(@"(<[^>]+>)+&nbsp;(</w+>)+");
// remove bizarre v: element attached to <img> tag
sc.Add(@"s+v:w+=""[^""]+""");
// remove extra lines
sc.Add(@"(nr){2,}");
foreach (string s in sc)
{
html = Regex.Replace(html, s, "", RegexOptions.IgnoreCase);
}
return html;
}
static string FixEntities(string html)
{
NameValueCollection nvc = new NameValueCollection();
nvc.Add(""", "&ldquo;");
nvc.Add(""", "&rdquo;");
nvc.Add("Ã¢â‚¬â€œ", "&mdash;");
foreach (string key in nvc.Keys)
{
html = html.Replace(key, nvc[key]);
}
return html;
}

```

kg-card-end: html

Some caveats:

1. I haven’t tested this with anything but Word 2003 documents saved as HTML. No guarantees on Word 97, Word 2000, Word XP, etcetera.
2. Tables, basic formatting, and images are preserved as simple HTML. I have only tested it with a handful of Word 2003 docs saved as HTML, but it has worked fine on the few I tried.
3. This requires .NET 2.0; I used .NET 2.0 because it’s less code.


If you’re feeling frisky, you can cut and paste the code above to build it yourself. Or you can just download it, lazyweb style:

- [Download the VS.NET 2005 solution](https://web.archive.org/web/20061023020415/http://www.codinghorror.com/blog/files/WordHtmlCleaner-vsnet2005-solution.zip) (3kb)
- [Download the CleanWordHtml console application](https://web.archive.org/web/20071020003015/http://www.codinghorror.com/blog/files/WordHtmlCleaner-executable.zip) (3kb, requires [.NET 2.0 runtime](https://web.archive.org/web/20060202111246/http://www.microsoft.com/downloads/details.aspx?FamilyID=0856EACB-4362-4B0D-8EDD-AAB15C5E04F5&displaylang=en))

[html cleaning](https://blog.codinghorror.com/tag/html-cleaning/)
[word to html](https://blog.codinghorror.com/tag/word-to-html/)
[word html cleanup](https://blog.codinghorror.com/tag/word-html-cleanup/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
