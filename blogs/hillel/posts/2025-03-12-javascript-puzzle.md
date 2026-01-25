---
title: "A Perplexing Javascript Parsing Puzzle"
date: 2025-03-12
url: https://www.hillelwayne.com/post/javascript-puzzle/
slug: javascript-puzzle
word_count: 356
---

What does this print?


```
x
= 1
x
--> 0 

```


Think it through, then try it in a browser console! Answer and explanation in the dropdown.


Show answer
  
It prints `1`.
wait wtf
At the beginning of a line (and **only** at the beginning of a line), `-->` starts a comment. The JavaScript is parsed as
`x = 1;
x; // 0 
`
The browser then displays the value of the last expression, which of course is 1.
but why
It’s a legacy hack.
Netscape Navigator 2 introduced both JavaScript and the `<script>` tag. Older browsers in common use (like Navigator 1) had no idea that `<script>` content was anything special and wrote it as regular text on the page.  To ensure graceful degradation, webdevs would wrap their scripts in [html comment blocks](http://www.javascripter.net/faq/hidingjs.htm):
`<script>
<!--
console.log("hello world!")
-->
</script>
`
Old browsers would parse the content as an HTML comment and ignore it, new browsers would parse the content as JavaScript and execute it. I’m not quite sure why `<!--` and `-->` weren’t syntax errors; presumably there was special code in the js engines to handle them, but I can’t figure it out [where](https://github.com/zii/netscape/tree/master).
All modern browsers at least recognize `<script>`.1 But since some old websites still have the hack and the standardization committee will never, *ever* break the web, they added `<!--` and `-->` as legal comment tokens to the [2015 standard](https://ecma-international.org/wp-content/uploads/ECMA-262_6th_edition_june_2015.pdf).

`<!--` and `-->` both act like `//`, i.e. starting line comments. `-->` is only valid at the start of a line (to avoid ambiguity with a postfix decrement followed by a greater than operator), while `<!--` can occur anywhere in the line. — [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#html_comments)

[Web browsers are required to support this syntax](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html), while other engines are not. Node and Electron both support it, though, as they share Chromium’s v8 engine.



Text-only browsers like Lynx recognize the tag, they just choose to ignore the contents.
 [return]



show all


*If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*


*I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/).*
