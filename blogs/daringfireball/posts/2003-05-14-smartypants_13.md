---
title: "SmartyPants 1.3"
date: 2003-05-14
url: https://daringfireball.net/2003/05/smartypants_13
slug: smartypants_13
word_count: 435
---


[SmartyPants 1.3 is out.](https://daringfireball.net/projects/smartypants/) See the project page for the download link and full details.


It’s mostly bug fixes pertaining to edge conditions where SmartyPants was curling quote characters the wrong way. I’ve fixed every reported case, so if you encounter any mis-curled quotes with SmartyPants 1.3, please let me know.


## Nerdy Details


One bug in particular had been vexing me ever since SmartyPants 1.0. The main trick with educating quotes in HTML markup is that you need to take care not to touch the quotes *inside* tags — the quotes surrounding HTML attribute values need to remain plain ASCII straight quotes.


So what SmartyPants does is *tokenize* the input text. Each piece of text is split into tokens, where a token is either a tag (and thus ignored) or a run of text between tags (and thus filtered). For example, this text:


```

"You said <em>what</em>?"

```


would be split into five tokens:



| Token | Type |
| `"You said ` | text |
| `<em>` | tag |
| `what` | text |
| `</em>` | tag |
| `?"` | text |



SmartyPants filters each token independently. So, in the above example, it will filter the first token (curling the opening double-quote), skip the next token because it’s a tag, filter the third token (but not actually do anything since there’s no punctuation), skip the next, then filter the last token (curling the closing double-quote).


Simple enough.


The problem arises with input like this:


```

<p>"<i>Tricky!</i>"</p>

```


which splits into the following seven tokens:



| Token | Type |
| `<p>` | tag |
| `"` | text |
| `<i>` | tag |
| `Tricky!` | text |
| `</i>` | tag |
| `"` | text |
| `</p>` | tag |



The problem is that the quote characters end up getting split into single-character tokens, all by themselves. With no preceding or succeeding characters to provide context, SmartyPants has no hint which way the quote should be curled.


Even a two-character token usually provides enough context to make an accurate guess as to whether a quote is opening or closing. But it’s just not possible with only one character.


The solution seems so obvious, I’m embarrassed not to have thought of it months ago. What SmartyPants now does is cheat by remembering the last character of the previous text token. Then, whenever it encounters a single-character quote token, it uses that character as context to guess which way to curl the quote.


Duh.



| **Previous:** | [Safari’s Unscriptable Tabs](https://daringfireball.net/2003/05/safaris_unscriptable_tabs) |
| **Next:** | [Zeldman Reloaded](https://daringfireball.net/2003/05/zeldman_reloaded) |


PreviousNext