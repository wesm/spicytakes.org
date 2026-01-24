---
title: "VS.NET and Code Regions"
date: 2005-07-04
url: https://blog.codinghorror.com/vsnet-and-code-regions/
slug: vsnet-and-code-regions
word_count: 245
---

I’m currently working on a project where almost every function has its own region. At first I found this convention onerous, but as I used it, I saw why it was necessary. **The default Visual Studio .NET outlining support leaves a lot to be desired.** Take your typical commented Page_Load method:

kg-card-begin: html

```

/// <summary>
/// This method is called when the Page’s Load event has been fired.
/// </summary>
/// <param name=“sender”>The <see cref=“object”/> that fired the event.</param>
/// <param name=“e”>The <see cref=“EventArgs”/> of the event.</param>
private void Page_Load(object sender, System.EventArgs e)
{
if (!Page.IsPostBack)
{
// do stuff
}
}

```

kg-card-end: html

That function will outline in two blocks: one for the XML comments, and another for the actual code itself:


![](https://blog.codinghorror.com/content/images/2025/05/image-111.png)


It’s aggravating that there is no built in support for **outlining the entire function and the comments.** Hence, the need for a simple region around the comments and the function, which provides the outlining support you might expect in the first place:


![](https://blog.codinghorror.com/content/images/2025/05/image-112.png)


I just checked, and VS.NET 2005 (aka Whidbey) has this same bad behavior. What a bummer. I am working on a macro that Region-izes all the functions in a file, but in the meantime you might want to check out the [Documentator macros on CodeProject](https://web.archive.org/web/20050802074604/http://www.codeproject.com/csharp/DocumentatorMacros.asp). They combine commenting and region-izing into one function, which isn’t always what I want, but it’s close enough to start.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[code organization](https://blog.codinghorror.com/tag/code-organization/)
[code structuring](https://blog.codinghorror.com/tag/code-structuring/)
