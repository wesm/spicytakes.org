---
title: "What’s Wrong With Turkey?"
date: 2008-03-13
url: https://blog.codinghorror.com/whats-wrong-with-turkey/
slug: whats-wrong-with-turkey
word_count: 884
---

Software internationalization is [is difficult](https://blog.codinghorror.com/software-internationalization-sims-style/) under the best of circumstances, but it always amazed me how often one *particular* country came up in discussions of internationalization problems: **Turkey**.


![turkish flag](https://blog.codinghorror.com/content/images/uploads/2008/03/6a0120a85dcdae970b012877703853970c-pi.png)


For example, [this Rick Strahl post](http://www.west-wind.com/weblog/posts/2204.aspx) from mid-2005 is one of many examples I’ve encountered:


> I’ve been tracking a really funky bug in my West Wind Web Store application that seems to crop up only very infrequently in my error logs. In a previous post I mentioned that I had instituted some additional logging features, specifically making sure that I would also log the locale of the user accessing the application.
> Well, three bug reports later I noticed that all errors occurred with a Turkish (tr) browser. So I changed my browser’s default language to Turkish and sure enough I could see the error occur.


Or, say, this 2005 [post from Scott Hanselman](http://www.hanselman.com/blog/UpdateOnTheDasBlogTurkishIBugAndAReminderToMeOnGlobalization.aspx):


> I had blogged earlier about a bug in dasBlog that affected Turkish users. When a Turkish browser reported an HTTP Accept-Language header indicating Turkish as the preferred language, no blog posts would show up. As fix, I suggested that users change their blog templates, but I knew that wasn’t an appropriate fix.


I understand that [Turkish prisons](http://en.wikipedia.org/wiki/Midnight_Express_(film)) are not to be trifled with, but the question remains: why do Turkish people take such cruel and perverse delight in breaking our fine software? **What’s wrong with Turkey?**


As with so many other problems in software development, the question shouldn’t be what’s wrong with Turkey, but rather, **what the hell is wrong with *software developers?*** Some of this is sort of obvious if you have any cultural awareness whatsoever.

- In the United States, we would typically format today’s date as **3/14/2008**. In Turkey, they format it as **14.3.2008**.
- In the United States, we use commas to group digits, like so: **32,768**. In Turkey, they group digits using a period, so the same number would be entered as **32.768**.


These minor formatting differences are usually not a big deal for output and display purposes, but it’s a whole different ballgame when you’re parsing input. You'd naturally expect people to input dates and numbers in the format they're used to. If your code assumes that input will be in typical American English format, there will be… trouble.


Most languages have this covered; there are functions that allow you to read or write dates and numbers appropriately for various cultures. In .NET, for example, it’s the difference between these two calls:

kg-card-begin: html

```
int.Parse(“32.768”);
int.Parse(“32,768”, System.Globalization.NumberFormatInfo.InvariantInfo);

```

kg-card-end: html

Because no culture is specified, the first call will parse the number according to the rules of the default culture that code is running under. Let’s hope it’s running under a Turkish version of Windows, so it can parse the number correctly. The second call, however, explicitly specifies a culture. The “invariant” culture is every American programmer’s secret dream realized: we merely close our eyes and wish away all those confusing languages and cultures and their crazy, bug-inducing date and number formatting schemes in favor of our own. A nice enough dream while it lasts, but instead of rudely asking your users to “speak American” through the invariant culture, **you could politely ask them to enter data in ISO international standard format instead.**


Anyway, point being, this kind of culture support is baked into most modern programming languages, so all you need to do is make sure your developers are aware of it – and more importantly, that they’re thinking about situations when they might *need* to use it.


But all that date and time formatting stuff is easy. Or about as easy as i18n ever gets, anyway. Strings are where it *really* starts to get hairy. Guess where this code fails?

kg-card-begin: html

```
switch (myType.ToLower())
{
case “integer” : ;
}

```

kg-card-end: html

If you guessed Turkey, you’re wrong! Just kidding. Of course it fails in Turkey. When we convert the string “integer” to upper and lower case in the Turkish locale, we get some strange characters back:

kg-card-begin: html

```
“INTEGER”.ToLower() = “ınteger”
“integer”.ToUpper() = “İNTEGER”

```

kg-card-end: html

It’s sort of hard to see the subtle differences here unless we ratchet up the font size:

kg-card-begin: html


| I → lowercase → ı |
| i → uppercase → İ |


kg-card-end: html

There’s obviously no way these strings are going to match “integer” or “INTEGER” respectively. This is known as [the Turkish I problem](https://web.archive.org/web/20080404230022/http://msdn2.microsoft.com/en-us/library/ms973919.aspx#stringsinnet20_topic5), and the solution should feel awfully familiar by now:

kg-card-begin: html

```
“INTEGER”.ToLower(System.Globalization.CultureInfo.InvariantCulture)

```

kg-card-end: html

That will produce the expected output, or at least, the output that matches the comparison in the original code snippet.


This is, of course, only the tip of the iceberg when it comes to internationalization. We haven’t even touched on the truly difficult locales like Hebrew and Arabic. But I do agree with Jeff Moser – if your code can [pass the Turkey test](http://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html), you’re doing quite well. Certainly better than most.


![](https://blog.codinghorror.com/content/images/2025/04/image-24.png)


If you care a whit about localization or internationalization, **force your code to run under the Turkish locale as soon as reasonably possible**. It’s a strong bellwether for your code running in most – but by no means all – cultures and locales.

[internationalization](https://blog.codinghorror.com/tag/internationalization/)
[bug tracking](https://blog.codinghorror.com/tag/bug-tracking/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[browser languages](https://blog.codinghorror.com/tag/browser-languages/)
