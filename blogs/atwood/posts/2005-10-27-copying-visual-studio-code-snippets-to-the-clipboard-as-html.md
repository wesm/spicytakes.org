---
title: "Copying Visual Studio Code Snippets to the Clipboard as HTML"
date: 2005-10-27
url: https://blog.codinghorror.com/copying-visual-studio-code-snippets-to-the-clipboard-as-html/
slug: copying-visual-studio-code-snippets-to-the-clipboard-as-html
word_count: 419
---

As I mentioned in [Formatting HTML code snippets with Ten Ton Wrecking Balls](https://blog.codinghorror.com/formatting-html-code-snippets-with-ten-ton-wrecking-balls/), **copying code to your clipboard in Visual Studio is often an exercise in futility if you want anything more than plain vanilla text.** VS copies code to the clipboard with bizarro-world RTF formatting instead of the sane, simple HTML markup you might expect. This is true even of the brand spanking new VS.NET 2005.


I previously developed a macro that converted highlighted code to simple HTML on the clipboard using two different methods. I’ve since removed the [Word interop method](http://addressof.com/blog/archive/2004/10/06/966.aspx) entirely because it’s clunky. And **I have improved the RTF-to-HTML conversion method substantially**. Take this code, for example:


![](https://blog.codinghorror.com/content/images/2025/03/image-339.png)


Let’s highlight the code execute the [FormatToHtml.Modern macro](https://web.archive.org/web/20060901084706/http://www.codinghorror.com/blog/files/FormatToHtml-042006.zip), and then paste the contents of the clipboard into something like [FreeTextBox](http://www.freetextbox.com/):

kg-card-begin: html

namespace TotallyUnnecessaryNamespace

{

    /// <summary>

    /// I heart GUIDs

    /// </summary>

    public class MyClass

    {

        public void test()

        {

            string s = “test”;

            int i = 1234;

        }

    }

}

kg-card-end: html

That’s extra clean, well-formatted <span> colored HTML wrapped in a simple <div>. It preserves the color scheme and indentation from your IDE exactly,* although it does substitute a standard monospace IDE font. View source on this post to see the raw markup.


Now compare this with the craptacular results you’ll get when you do a traditional copy and paste! This is how VS.NET 2005’s CTRL+C copy functionality should behave. You could even map the CTRL+C shortcut to the macro if you like.


My favorite new feature, however, is that **the macro now dynamically removes excessive indenting from copied code**. That makes it a lot cleaner when copying code snippets [from the TotallyUnnecessaryNamespace namespace](https://blog.codinghorror.com/a-modest-namespace-proposal/). As Cartman would say, *super sweet.* And it works in Visual Studio 2002, 2003, and 2005. Try it yourself!

kg-card-begin: html

[Download the FormatToHtml macro](https://web.archive.org/web/20060901084706/http://www.codinghorror.com/blog/files/FormatToHtml-042006.zip) (5kb) Updated 4/2006

kg-card-end: html

Here’s how to get started with this macro

1. go to Tools - Macros - IDE
2. create a new Module named “FormatToHtml” under “MyMacros”
3. paste the downloaded code into the module
4. add references to System.Drawing and System.Web via the Add Reference menu
5. save and close the macro IDE window
6. go to Tools - Macros - Macro Explorer
7. Four new macros will be under “FormatToHtml”; double-click to run the macro, then paste away...


*Background colors are lost, but that’s because the RTF markup VS.NET places in the clipboard doesn’t contain the background colors, either. Total bummer.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[visual studio code](https://blog.codinghorror.com/tag/visual-studio-code/)
[html](https://blog.codinghorror.com/tag/html/)
[clipboard](https://blog.codinghorror.com/tag/clipboard/)
[code snippets](https://blog.codinghorror.com/tag/code-snippets/)
