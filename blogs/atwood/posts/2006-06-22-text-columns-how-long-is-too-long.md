---
title: "Text Columns: How Long is Too Long?"
date: 2006-06-22
url: https://blog.codinghorror.com/text-columns-how-long-is-too-long/
slug: text-columns-how-long-is-too-long
word_count: 1804
---

Ian Griffiths recently wrote a [proof of concept WPF browser](http://www.interact-sw.co.uk/iangblog/2006/06/21/wpfmsdn) for the MSDN online help. One of the improvements cited is multi-column text:


> This is why WPF offers a column-based reading experience. **We know from experience in the print world that breaking text into columns can make it much easier to read. **Indeed, once you’ve got used to reading in columns, going back to the long unbroken lines offered by the standard SDK viewer feels like punishment!


Code is a highly specialized form of writing, but the same sort of questions always come up. Should we use short lines or long lines? A recent comment from Buggy Fun Bunny* describes this conundrum well:


> What I’ve found amusing for the last 20 years is this insistence, by people who should know better, on 80 column (or less) line limits. That was invented by COBOL (which only has ~66 characters available after you subtract the line number from 73) around 1960. It’s just silly. I remember how wonderful it was when the VT-220 came along and I could use 132 character lines. If nothing else, formatting a report both in code and as output was a piece of cake.
> Beyond the character world, we have wide screen taking over, and folks still think that 80 columns is King. There’s more horizontal real estate, and always was. Use it well.
> And as to scanning narrow: not everybody does; I’ve had the Great Books set and can’t read them because those narrow double columns drive my eyes over the edge.


Hey, I’m a [Great Books](http://www.greatbooks.org/) fan from way back in the day. Nothing blows a seventh grader’s mind quite like reading Graham Greene’s *The Destructors*, or Carson McCuller’s *Sucker*. No wonder people want to burn books. They’re subversive.


So what’s the best way to structure columns of text on a computer screen? How long is too long? Luckily, the Software Usability Research Laboratory at Wichita State has already [researched](https://web.archive.org/web/20060707171441/http://psychology.wichita.edu/surl/usabilitynews/72/columns.htm) – and answered – this question.


But before I reveal the answer, what do you think? Which of these passages is easier to read and comprehend?


### Single column, left aligned

kg-card-begin: html

Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice, “without pictures or conversations?”


So she was considering, in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.


There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself “Oh dear! Oh dear! I shall be too late!” (when she thought it over afterwards it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but, when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge.

kg-card-end: html

### Single column, justified

kg-card-begin: html

Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice, “without pictures or conversations?”


So she was considering, in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.


There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself “Oh dear! Oh dear! I shall be too late!” (when she thought it over afterwards it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but, when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge.

kg-card-end: html

### Double column, left aligned

kg-card-begin: html


| Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice, “without pictures or conversations?”
So she was considering, in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. | There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself “Oh dear! Oh dear! I shall be too late!” (when she thought it over afterwards it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but, when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge. |


kg-card-end: html

### Double column, justified

kg-card-begin: html


| Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice, “without pictures or conversations?”
So she was considering, in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. | There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself “Oh dear! Oh dear! I shall be too late!” (when she thought it over afterwards it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but, when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge. |


kg-card-end: html

The answer is more complex than you might think. The SURL paper first summarizes **past findings of previous research**:

- Longer line lengths generally facilitate faster reading speeds.
- Shorter line lengths result in increased comprehension.
- The optimal number of characters per line is between 45 and 65.
- Paging through online text generally results in better comprehension than scrolling.
- Reading speed is faster for both single and multiple columns, but preference is for multiple short columns.
- Left-justified text is read faster than full-justified text.


And here’s what they found in their study:


![](https://blog.codinghorror.com/content/images/2025/05/image-322.png)


> The results of this study suggest that there is not one best way to present text online. Although **fast readers performed best at the two-column full-justified condition, slow readers benefited from a single column non-justified layout**.


Personally, I was surprised that **justification had such a strong influence on the results. **Simply breaking up text into columns actually *hurts* reading speed noticeably for both slow and fast readers. However, if you fully justify the columns, then – and only then – reading speed increases dramatically for everyone. And clearly, three column layouts aren’t worth it, no matter how you align the text.


So what conclusion can we draw for coders? Probably not much. Code is always left aligned, and in a single column. A related SURL study examines the [effect of line length alone](https://web.archive.org/web/20060711202025/http://psychology.wichita.edu/surl/usabilitynews/72/LineLength.htm) which might be more relevant:


> This study examined the effects of line length on reading performance. **Reading rates were found to be fastest at 95 cpl.** Readers reported either liking or disliking the extreme line lengths (35 cpl, 95 cpl). Those that liked the 35 cpl indicated that the short line length facilitated "faster" reading and was easier because it required less eye movement. Those that liked the 95 cpl stated that they liked having more information on a page at one time. **Although some participants reported that they felt like they were reading faster at 35 cpl, this condition actually resulted in the slowest reading speed.**


Furthermore, line length had no effect on comprehension. Although I’m hesitant to draw broad parallels between source code and a news article, perhaps arbitrarily short lines aren’t *always* necessary in source code to achieve good readability and comprehension.


*I just write this stuff down. I don’t make it up.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[text formatting](https://blog.codinghorror.com/tag/text-formatting/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
