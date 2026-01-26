---
title: "Draft"
description: "I've written quite a few books now, and one questions that I     get from time to time is what tools I use to write them. I've     developed a pretty nifty tool-chain - at least for my purposes -     "
date: 2014-03-14T00:00:00
tags: ["writing"]
url: https://martinfowler.com/articles/bookColophon.html
slug: bookColophon
word_count: 1370
---


I've written quite a few books now, and one questions that I
    get from time to time is what tools I use to write them. I've
    developed a pretty nifty tool-chain - at least for my purposes -
    over the years, so here's my notion of how it all hangs together.


When I started writing, I used word-processing or publishing
    tools. I tried Microsoft Word for a while, but wasn't that keen on
    it. My early books (Analysis Patterns, UML Distilled, Planning
    Extreme Programming, and Refactoring) were all written using
    Framemaker - which is a sophisticated tool for large documents. If
    you like a WISIWIG editing environment, it was pretty good
    (although I haven't used it since around 2000).


With Patterns of Enterprise Application Architecture, I made a
    significant shift in my book writing - moving to a text based
    system. By this I mean keeping the source files from my book in an
    open textual format. This has worked out really well for me. I'm a
    geek after all, and it's easy for me to write tools to process
    text-based files. I can also keep the book with standard version
    control systems - which is useful when working on my own and vital
    for collaborative work for others.


Such a mechanism has its downsides for many people. I no longer
    have WISIWIG - instead I compose my writing in a text editor and
    run a script to generate readable output. This works just fine for
    me, but imagine non-geeks would find it rather primitive.


One particular advantage of this scheme for a technical author
    such as myself is the handling of software code. In my pre-text
    days I would have to write programs, get them working and tested,
    and then copy/paste them into Framemaker. That last step was the
    problem, often I needed to change the program and then had to
    update the code in the book. With manual copy/paste, errors
    happend easily.


Now with my current scheme, all code is automatically imported
    into the book as part of the build process. So if I update my
    code, the book automatically becomes up to date. I would never go
    back to manual copy/paste again.


The one exception to my all-text approach is diagrams. I've
    used a variety of diagram drawing tools, and these are mostly
    WISIWIG style tools. This isn't ideal, but I haven't come across
    a solution that would work better with direct text editing.


## Source Text Format


The key point of my approach is the idea of using an open
      textual format. In my case I use home-grown XML vocabulary. It's
      mostly similar to HTML, but with additional tags I've put in
      that make sense for my books. I've always been a fan of **semantic
      markup** - marking up the text according to its meaning rather
      than it output formatting. For example, one thing I do from time
      to time is bolding a phrase when I define it, as I've done
      above. I like doing this because if a reader is looking for a
      definition of a term, they can find it quickly by scanning the
      page.


However when I do the markup for that I don't use a tag like
      `<b>` or `<bold>`,
      instead I use the semantic tag `<term>`.
      I then decide in my transformation code to turn terms into
      bolded text.


I prefer this because it forces me to focus on semantics
      rather than formatting. It also gives me other useful features
      during the transformation. When I transform terms, not just can
      I make them bold, I can also insert markers for indexing into
      the output.


Many people I know like the idea of text documents, but
      dislike XML. Some people find XML awkward to type, or the tags
      get in the way of reading. A popular alternative choice here is
      markdown, which is deliberately easy to read and write in plain
      text. I prefer XML because it gives me more flexibility in
      markup - I can introduce whatever tags I like, including
      specialist tags for just this book - and flow them smoothly into
      the process.


Another source format I've come across is to use Docbook XML
      vocabulary. Docbook is a standard XML vocabulary for documents,
      particularly long documents. It has some useful advantages, but
      I find its tags to be rather verbose and intrusive. Also
      adopting Docbook would stop me using my own semantic tags.


Another text choice with a long heritage is LaTeX - but I've
      never tried it.


## Transformation Target


To turn my source documents into output I use a
      transformation toolchain that I'll discuss in a moment. The
      immediate target of that toolchain is Docbook. While I don't
      like Docbook as a source document format, it is really good as a
      transformation target. Once you have your text into Docbook,
      then there's a raft of OSS tools that can turn that Docbook into
      lots of formats: HTML, PDF, ePub, etc. I can easily incorporate
      these tools into my overall toolchain so with a single command I
      can generate any combination of these formats.


I typically use the HTML output when working on the book in
      the early days. If I want to share the book with reviewers I can
      generate PDF or ePub as they wish. My publisher (Pearson) takes
      the Docbook files and feeds them into their publication process.


## Transformation Toolchain


The toolchain that generates the Docbook is a series of
      scripts I put together myself in Ruby. They take a series of XML
      files that form the book text, together with reference files for
      things like a bibliography and live code directories, and
      generate the Docbook output.


They are structured as transformation rules, so when the
      transformer sees a âtermâ tag it knows to output the appropriate
      Docbook element (together with index information). If I add new
      tags, I just have to add new handler methods for them and I can
      quickly get them visible in the output. The toolchain is very
      similar to the one I use for my website, the main difference is
      that the website toolchain outputs to HTML rather than
      Docbook


## Editing


The nice thing about this approach is that I can use any text
      editor to write with. My favorite text editor is Emacs, and it's
      particularly helpful that Emacs has a very nice mode (NXML mode)
      for editing XML documents with. A lot of XML editors I've seen
      are intended for XML as a serialization of a hierarchic data
      structure, which isn't suitable for marked-up text. NXML mode is
      very suitable for text markup, so it works well for me. Amongst
      other things it can be set up with a RNC schema file so that the
      editor is schema-aware.


## Code Import


Automatic code import is a very important part of my
      toolchain. I can work with regular program code, organized
      however I like. All I need to do is put markers enclosed as
      comments to indicate regions of the code that I may want to pull
      into the book as code fragments. I then have an XML element that
      names the file and the fragment together with a label. When I
      run the tool chain the code is pulled out of the live file into
      the Docbook output.


## Graphics


Graphics represent the one area where I don't do my editing
      in a text editor. Currently I'm addicted to OmniGraffle for
      doing diagrams (mac only). OmniGraffle will export to various
      formats I need for the book production (png, eps, etc). My
      script tool chain uses Apple's scripting capability to
      automatically re-export files as needed, so I don't have to
      remember to export when I change a diagram.


## Version Control


Like any programmer I value version control highly. When I
      started with P of EAA we used CVS, since then I've used SVN,
      Mercurial, and git. A version control system is particularly
      helpful when collaborating with others as we can use the same
      approach for code to keep our writing in sync.


When the book goes to production, I've arranged with my
      publisher, Pearson, to use copy editors, indexers, and other
      production staff who are comfortable working on the original
      source files in the repository.


---
