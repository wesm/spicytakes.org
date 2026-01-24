---
title: "Is Your IDE Hot or Not?"
date: 2006-09-14
url: https://blog.codinghorror.com/is-your-ide-hot-or-not/
slug: is-your-ide-hot-or-not
word_count: 475
---

Scott Hanselman recently brought up the topic of [IDE font and color schemes](https://web.archive.org/web/20061107042100/http://www.hanselman.com/blog/CommentView.aspx?guid=038f7325-ba8e-46d1-a1ad-ecc186167de8) again. I’ve been in search of the [ideal programming font](https://blog.codinghorror.com/progamming-fonts/) and the [ideal syntax colorization scheme](https://blog.codinghorror.com/pimp-my-ide/) for a while now. Here’s my current take on it.


![](https://blog.codinghorror.com/content/images/2025/05/image-360.png)


As you can see, I’ve finally given in to [the inevitability of ClearType](https://blog.codinghorror.com/my-lovehate-relationship-with-cleartype/). Someone pointed out the [zenburn vim color scheme](http://www.vim.org/scripts/script.php?script_id=415) in the comments. I think it’s a nice dark background yin to my light background yang. So I set it up as an alternative for the dark background enthusiasts.


![](https://blog.codinghorror.com/content/images/2025/05/image-361.png)


Try these IDE color schemes yourself. Download the exported Visual Studio 2005 Fonts and Colors settings files:

- [Download Jeff’s scheme](https://github.com/coding-horror/ide-hot-or-not/raw/master/exported-font-and-colors-for-jeff-atwood-sept-19.zip) (2kb)
- [Download “Zenburn” scheme](https://github.com/coding-horror/ide-hot-or-not/raw/master/exported-font-and-colors-zenburn.zip) (2kb) (now with HTML, XML, and CSS properties by Geraldo Medrano)
- Download more schemes, and contribute your own, at the [Studio Styles](https://studiostyl.es/) site.


To import, use the **Tools | Import and Export Settings** menu in Visual Studio 2005. But be sure you have the necessary fonts installed first – [Consolas](https://web.archive.org/web/20070224212834/http://www.microsoft.com/downloads/details.aspx?familyid=22e69ae4-7e40-4807-8a86-b3d36fab68d3&displaylang=en) for the main font and [Dina](http://www.donationcoder.com/Software/Jibz/Dina/) for the output console font.


Here’s how to export your own IDE font and color settings:

- Tools | Import and Export Settings...
- Select Export
- Click the All Settings node to unselect everything in the tree
- Expand the tree to “All Settings, Options , Environment”
- Click the “Fonts and Colors” node
- Click next, name the file appropriately, and Finish.

kg-card-begin: html

What we really need is for **some enterprising coder to create a “Hot or Not” site for IDE color schemes**, where we can post screenshots and downloadable *.settings files for our preferred IDE color and font schemes. Update: Someone set up Studio Styles.

kg-card-end: html

If we’re posting comparative screenshots, it might be a good idea to use the same code sample in each one. Here’s the code sample I used in the above screenshot, which highlights some potential programming-specific font legibility issues (O vs. 0, I vs. l, etcetera).

kg-card-begin: html

```

#region codinghorror.com
class Program : Object
{
  static int _I = 1;
  /// <summary>
  /// The quick brown fox jumps over the lazy dog
  /// THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
  /// </summary>
  static void Main(string[] args)
  {
    Uri Illegal1Uri = new Uri("http://packmyboxwith/jugs.html?q=five-dozen&t=liquor");
    Regex OperatorRegex = new Regex(@"S#$", RegexOptions.IgnorePatternWhitespace);
    for (int O = 0; O < 123456789; O++)
    {
      _I += (O % 3) * ((O / 1) ^ 2) - 5;
      if (!OperatorRegex.IsMatch(Illegal1Uri.ToString()))
      {
        Console.WriteLine(Illegal1Uri);
      }
    }
  }
}
#endregion

```

kg-card-end: html

If you’re formulating your own ideal font and color scheme, the only specific advice I have for you is to [avoid too much contrast](https://blog.codinghorror.com/code-colorizing-and-readability/) – don’t use pure white on pure black, or vice versa. That’s why my background is a light grey and not white.

[font settings](https://blog.codinghorror.com/tag/font-settings/)
[color schemes](https://blog.codinghorror.com/tag/color-schemes/)
[ide](https://blog.codinghorror.com/tag/ide/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[syntax colorization](https://blog.codinghorror.com/tag/syntax-colorization/)
