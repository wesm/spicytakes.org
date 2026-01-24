---
title: "Of Spaces, Underscores and Dashes"
date: 2006-04-26
url: https://blog.codinghorror.com/of-spaces-underscores-and-dashes/
slug: of-spaces-underscores-and-dashes
word_count: 256
---

I try to avoid using spaces in filenames and URLs. They’re great for human readability, but they’re remarkably inconvenient in computer resource locators:


Any spaces in URLs are converted to the encoded space character by the web browser:

kg-card-begin: html

```
XCOPY "c:\test files\reference data.doc" d:
XCOPY c:\test-files\reference-data.doc d:

```

kg-card-end: html

A filename with spaces has to be surrounded by quotes when referenced at the command line:

kg-card-begin: html

```
http://domain.com/test%20files/reference%20data.html
http://domain.com/test-files/reference-data.html

```

kg-card-end: html

So it behooves us to **use something other than a space in file and folder names**. Historically, I’ve used underscore, but I recently discovered that **the correct character to substitute for space is the dash**. Why?


The short answer is, [that’s what Google expects](http://weblog.philringnalda.com/2004/04/22/underscores-are-bad-mmkay):


> If you use an underscore ‘_’ character, then Google will combine the two words on either side into one word. So `bla.com/kw1_kw2.html` wouldn’t show up by itself for kw1 or kw2. You’d have to search for `kw1_kw2` as a query term to bring up that page.


The slightly longer answer is, the underscore is traditionally [considered a word character](http://www.regular-expressions.info/charclass.html) by the w regex operator.


Here’s [RegexBuddy](http://www.regexbuddy.com) **matching the w operator against multiple ASCII character sets**:


![](https://blog.codinghorror.com/content/images/2025/05/image-274.png)


As you can see, the dash is not matched, but underscore is. **`This_is_a_single_word`, but `this-is-multiple-words`**.


Like NutraSweet and Splenda, neither is really an *acceptable* substitute for a space, but we might as well follow the established convention instead of inventing our own. That’s how we ended up with the backslash as a path separator.

[spaces](https://blog.codinghorror.com/tag/spaces/)
[underscores](https://blog.codinghorror.com/tag/underscores/)
[dashes](https://blog.codinghorror.com/tag/dashes/)
[filenames](https://blog.codinghorror.com/tag/filenames/)
[urls](https://blog.codinghorror.com/tag/urls/)
