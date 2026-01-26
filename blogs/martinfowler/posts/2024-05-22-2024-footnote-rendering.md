---
title: "Using Footnotes"
description: "How I use, and render, footnotes"
date: 2024-05-22T00:00:00
tags: ["writing"]
url: https://martinfowler.com/articles/2024-footnote-rendering.html
slug: 2024-footnote-rendering
word_count: 528
---


Last week I added a small feature to this website, changing the way it
    renders footnotes. That prompted me to write this quick note about how I use
    footnotes, and how that influences the best way to render them.


In my early years of writing, I avoided using footnotes. My general view
    was that if it was important enough to worth writing about, it should make
    its way into the main text, otherwise it should be discarded. That attitude
    saw me through my early books and my articles (including this site) up till
    the late noughties.


But then I was writing [an article](https://martinfowler.com/articles/obamaSoftware.html) about the
    technology work done on Obama's 2008 campaign. I found I wanted to add a
    bunch of details about what was done, but that made the article feel like a
    laundry list, burying any narrative thread. I found that moving a lot of
    details to footnotes allowed the main article to be more coherent, but still
    meant the details were in there for the curious reader. That became the crux
    of my use of footnotes, **they were for details that I wanted to include, but not derail
    the main thrust of the prose**.


My original approach to footnotes was to have a reference as a short link
    [1] to the body of the footnote at the end of the article.
    The reader can click on the link, jump to the footnote body at the end, and
    then use the back button to return to where they were reading. The new
    rendering allows the reader to click the
    reference, as before, but now the footnote opens up under the paragraph, so
    the reader doesn't have to scroll2. I still keep the footnotes section at the
    end of the article, in case the reader prints the article out.


2: The reader may need to scroll if reading it on a
    phone after a long paragraph. But I didn't want to split paragraphs for the
    footnote text.

â
Like this

Another rendering I've seen for footnotes is the **sidenote**, where the
    footnote text is put to one side of the pageâ . The trouble
    with this rendering is that it's too easy for the reader's eye to glance
    over and read the sidenote's text. This then breaks the reader's flow of the
    main text, and thus defeats the purpose of using a footnote. I like the need
    to click on the reference, because then it's easier for the reader to refrain
    from the effort to do it. They then will only click as a deliberate act - and I want
    the decision to follow the footnote to be a conscious choice.3


3: There's also the point that sidenotes don't
    really work on a phone-size display, so will need a different rendering for
    that case. (And I didn't bother with that for this example.)


Since the reader has to click on the footnote reference to reveal the
    text, I don't think a small superscript fits the bill. So instead I've used a
    light grey box, hopefully subtle enough to fade into the background, but
    large enough to invite a reader's finger when using a phone or tablet.


---
