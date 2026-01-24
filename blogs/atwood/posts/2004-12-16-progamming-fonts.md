---
title: "Programming Fonts"
date: 2004-12-16
url: https://blog.codinghorror.com/progamming-fonts/
slug: progamming-fonts
word_count: 347
---

Mike Gunderloy’s book, [Coder to Developer](http://www.amazon.com/exec/obidos/ASIN/078214327X/), suggests, as part of configuring your IDE, that you explore programming specific fonts. I was intrigued, because I hadn’t ever considered that. I’ve been using **Courier New 9** for years. A little searching turned up a few links:

- This [programming font geek thread](https://web.archive.org/web/20041228064204/http://typographi.com/000744.php#000744)
- A wiki entry on [programming fonts](https://web.archive.org/web/20060313054618/http://keithdevens.com/wiki/ProgrammerFonts)
- A comprehensive ClearType-enabled monochrome [programming font comparison](http://www.lowing.org/fonts/)


Lists of fonts are all well and good, but a picture is worth a thousand words. Here are code snippets in each font, [without ClearType](https://blog.codinghorror.com/consolas-and-cleartype/):


[Andale Mono](http://sourceforge.net/project/showfiles.php?group_id=34153) 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-88.png)


[Anonymous](http://www.ms-studio.com/FontSales/anonymous.html) 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-89.png)


**Courier New** 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-90.png)


**Lucida Console** 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-91.png)


[Lucida Typewriter](https://web.archive.org/web/20060901084554/http://www.codinghorror.com/blog/files/LucidaTypewriter.zip) 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-92.png)


[Monaco](https://web.archive.org/web/20041217003051/http://www.pa.msu.edu/ftp/pub/misc/tek-phaser/ttfonts/MONACO.TTF) 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-94.png)


[Pragmata](http://www.fsd.it/fonts/pragma.htm) 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-95.png)


[ProFont](https://web.archive.org/web/20041230190554/http://www.tobias-jung.de/seekingprofont/#upd) (fixed size bitmap)


![](https://blog.codinghorror.com/content/images/2025/06/image-96.png)


[Proggy Clean](https://web.archive.org/web/20140517174555/http://www.proggyfonts.net/) (fixed size bitmap)


![](https://blog.codinghorror.com/content/images/2025/06/image-97.png)


[Vera Sans Mono](https://web.archive.org/web/20041230152757/http://www.gnome.org/fonts/) 9 point


![](https://blog.codinghorror.com/content/images/2025/06/image-99.png)


I’m sure I missed some, but these seem to be the most popular ones. I am not listing a few I tested here and found so heinously bad in these conditions (9pt sans ClearType) that they didn’t deserve any consideration.


I learned a few things in this experiment:

1. I definitely have to have monospace fonts in my IDE. All of the above fonts are monospace.
2. I don’t care for anti-aliasing of any kind on a programming font. That goes for ClearType and plain old AA. **Note that some fonts decide to anti-alias themselves even at 9 point!**
3. Bitmap fonts, such as Proggy, are very precise but don’t scale. At all. So if you’re programming on a large 1600x1200 or higher screen, that may be a factor. And the scalable fonts can look quite different at larger sizes!
4. **Proggy** is my top choice for programming font, but it’s fixed size and thus doesn’t always work if I’m coding on a 1920x1440 display. If I need a scalable font, I like **Lucida Typewriter** and **Pragmata**.
5. I don’t recommend using Comic Sans as your programming font. Nor do I recommend dreaming up all new programming characters.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[development tools](https://blog.codinghorror.com/tag/development-tools/)
[typography](https://blog.codinghorror.com/tag/typography/)
