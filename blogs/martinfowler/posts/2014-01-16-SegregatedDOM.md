---
title: "Segregated DOM"
description: "Single-page web applications often turn into jQuery soup, where   application logic,DOMmanipulation, and server access are all mixed   together. This mixing of concerns makes such applications harder "
date: 2014-01-16T00:00:00
tags: ["web development"]
url: https://martinfowler.com/bliki/SegregatedDOM.html
slug: SegregatedDOM
word_count: 660
---


Single-page web applications often turn into jQuery soup, where
  application logic, [DOM](https://developer.mozilla.org/en-US/docs/DOM) manipulation, and server access are all mixed
  together. This mixing of concerns makes such applications harder to
  understand and test than they ought to be. Segregated DOM is a modularization
  tactic that separates all manipulation of the DOM into dedicated
  JavaScript objects.


For an example, consider the recent [filter catalog page I
  developed to discuss my favorite eurogames](https://martinfowler.com/articles/eurogames/). A key behavior of
  this page is your ability to click on the filter panel on the left
  side to filter which games display in the entry list panel. All this
  is done via JavaScript. I have JavaScript classes for the
  filter panel and the entry list, each of which encapsulates the DOM
  access for that part of the page. The logic of deciding which games
  to show is kept in a controller class which talks to the DOM
  manipulation classes using an interface that is independent of
  the DOM. The controller class doesn't make any use of jQuery.


![](images/segregatedDom/sketch.png)


During initialization the controller passes its update function
  to the Filter DOM to be called whenever a box in the filter changes
  state, the Filter DOM sets this function to the click events of the
  check boxes. So when anything changes in the filter display this
  update function in the controller asks the Filter DOM class for its
  active filters ➊. The Filter DOM class responds to this call by
  using jQuery to find the appropriate HTML elements ➋, filtering out
  those boxes that are checked, and responding to the controller with a
  simple data structure that indicates which boxes in each group are
  checked ➌.


The controller uses this information about the filter state to
  decide which games should now be visible, divides them into the left
  and right columns, and calls the Entry List DOM with the details of
  which element ids should be displayed in the list ➍. The Entry List
  DOM uses jQuery to shuffle the HTML items into the right divs to do
  the job ➎.


The principal benefit of doing this is to make it easier to
  reason about each class by keeping it focused on a single task. When
  I'm working on the Filter DOM class, I concentrate on how to do the
  DOM manipulations on the HTML elements. When I work on the
  controller I can ignore the details of the HTML structure, css class
  names, and the like.


In more abstract pattern terms, these DOM objects act as
  [Gateways](https://martinfowler.com/eaaCatalog/gateway.html), a passage between two [BoundedContexts](https://martinfowler.com/bliki/BoundedContext.html) (the application
  and the HTML DOM). Like any gateway the DOM object has an interface
  that speaks the vocabulary of its client (the application) and an
  implementation that translates this into the barbaric (HTML DOM) land
  beyond. 1


1: 
      You can use a similar separation for server access - this is the
      classic application of [Gateway](https://martinfowler.com/eaaCatalog/gateway.html).


A good modular design tends to correlate to testability. Each
  class can be tested in relative isolation. A particular advantage
  with a Segregated DOM is that I can test the controller without
  using a browser or mock browser such as PhantomJS. Since I don't
  need a DOM to test the controller, I can test it in node and just
  supply some simple test doubles for the DOM gateways. This makes it
  quicker and easier to modify the controller. By shifting as much
  logic out of the DOM gateway as possible, I can increase how much
  testing I can do without resorting to PhantomJS and the like (an
  application of the [Humble Object](http://xunitpatterns.com/Humble%20Object.html)
  pattern).


## Further Reading


Pete Hodgson was a valuable source for ideas for this article.
    Coincidentally, [his
    own article on using Segregated DOM](http://programming.oreilly.com/2014/01/keeping-jquery-in-check.html) was published the same
    day. It has more details and a short example.


## Acknowledgements

Pete Hodgson gave me some useful ideas for improving this article.

## Notes


1: 
      You can use a similar separation for server access - this is the
      classic application of [Gateway](https://martinfowler.com/eaaCatalog/gateway.html).
