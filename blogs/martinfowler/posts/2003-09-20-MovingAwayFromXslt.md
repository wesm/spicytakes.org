---
title: "Moving Away From Xslt"
description: "All of this site is written in simple XML documents and   transformed to HTML. I find this works really well, and means I   never have to worry about dealing with HTML formats. (Not that fancy   layou"
date: 2003-09-20T00:00:00
tags: ["writing"]
url: https://martinfowler.com/bliki/MovingAwayFromXslt.html
slug: MovingAwayFromXslt
word_count: 558
---


All of this site is written in simple XML documents and
  transformed to HTML. I find this works really well, and means I
  never have to worry about dealing with HTML formats. (Not that fancy
  layout is my style, as you can tell.) I've even written [a whole book
  that way](../articles/writingInXml.html).


For most of this time I've used XSLT as my transformation
  language. I've got pretty good with slinging XSLT around and getting
  it to do what I want.


But no more.


When I wrote the software for this Bliki (on a long flight) I did
  it in Ruby.Prior to that I used Ruby to do a new version of my home
  page. My conclusion from this exercise was that using Ruby for XML
  transforms was much easier than using XSLT.

- XML makes a lousy syntax for a programming language. There's
    way too much noise in there and as a result you can't see the program.
- XSLT makes calling subroutines so painful that you are
    seriously discouraged from using them, which encourages duplicate code.
- XSLT handles simple tasks well, but is baroque when it comes
    to more complicated things. Indeed some are impossible and you
    have to jump out into another language anyway.
- Ruby gives me a clean, OO language with clear syntax and a
    [kick-ass
    XML library](http://www.germane-software.com/software/rexml/).(Python may well be just as good, I haven't tried
    it.)
- I can mix template style code with transformer style code.


The design of XSLT does influence the way I use the program. My
  basic transform tasks are handled using recursive apply functions
  just like XSLT's apply-template command. In this case I use ruby's
  reflection to make it work well. The guts of the transformer is


```
class ElementHandler

  def apply anElement
    anElement.each {|e| handle(e)} if anElement
  end

  def handle aNode
    if aNode.kind_of? REXML::Text
      handleTextNode(aNode) 
    elsif aNode.kind_of? REXML::Element
      handle_element aNode  
    else
      return #ignore comments and processing instructions
    end
  end
  def handle_element anElement
    handler_method = âhandle_â + anElement.name.tr(â-â,â_â)
    if self.respond_to? handler_method
      self.send(handler_method, anElement)
    else
      default_handler(anElement)  
    end
  end
...

```


Essentially the `handle_element` method uses
  reflection to invoke a properly named function in the handler
  object. I subclass the ElementHandler for specific kinds of
  page. So I have a question tag for the questions that appear on
  certain pages. For this I write a short transformation routine.


```

  def handle_question anElement
    @html.p {@html.element('b'){apply anElement}}
  end

```


The `@html.element` method pumps out b tags into the output. Inside
those b tags are the result of executing the block of code` {apply
anElement}` which continues the recursion. Here ruby's blocks come in
very useful.


There are probably tons of ways to improve on this, but I haven't
  needed to touch the code much since I made the bliki live. Where I
  have I've found it much easier to deal with than the XSLT.


I think this may raise some real questions about XSLT. There's
  still much I like about the power of XSLT, but I hate the syntax and
  the walls you keep running into. I'm not going to convert my whole
  site over to Ruby tomorrow - most of the XSLT works fine - but I
  can certainly see my way to doing that at some point in the
  future. But the bigger question is whether you're better off with
  scripting language for this kind of task than XSLT.
