---
title: "Understanding Model-View-Controller"
date: 2008-05-05
url: https://blog.codinghorror.com/understanding-model-view-controller/
slug: understanding-model-view-controller
word_count: 1190
---

Like everything else in software engineering, it seems, the concept of [Model-View-Controller](http://en.wikipedia.org/wiki/Model-view-controller) was originally invented by [Smalltalk](http://en.wikipedia.org/wiki/Smalltalk) programmers.


More specifically, it was invented by one Smalltalk programmer, Trygve Reenskaug. Trygve maintains a page that [explains the history of MVC](http://heim.ifi.uio.no/~trygver/themes/mvc/mvc-index.html) in his own words. He arrives at these definitions in a paper he published on December 10th, 1979:

1. **Models**
Models represent knowledge. A model could be a single object (rather uninteresting), or it could be some structure of objects.
There should be a one-to-one correspondence between the model and its parts on the one hand, and the represented world as perceived by the owner of the model on the other hand.
2. **Views**
A view is a (visual) representation of its model. It would ordinarily highlight certain attributes of the model and suppress others. It is thus acting as a *presentation filter*.
A view is attached to its model (or model part) and gets the data necessary for the presentation from the model by asking questions. It may also update the model by sending appropriate messages. All these questions and messages have to be in the terminology of the model, the view will therefore have to know the semantics of the attributes of the model it represents.
3. **Controllers**
A controller is the link between a user and the system. It provides the user with input by arranging for relevant views to present themselves in appropriate places on the screen. It provides means for user output by presenting the user with menus or other means of giving commands and data. The controller receives such user output, translates it into the appropriate messages and pass these messages on to one or more of the views.


It may seem like we’re deep in [Architecture Astronaut territory](https://blog.codinghorror.com/it-came-from-planet-architecture/) now, but bear with me. The MVC concepts are a little abstract, it’s true, but it’s an incredibly common pattern. It is literally all around you. In fact, let me bring it back down to Earth this way: you’re looking at MVC *right now*.

kg-card-begin: html


| **Model** = HTML | **View** = CSS | **Controller** = Browser |
|  |  |  |


kg-card-end: html

This ubiquitous trifecta represents MVC almost perfectly.

1. Model
The HTML is the “skeleton” of bedrock content. Text that communicates information to the reader.
2. View
The CSS adds visual style to the content. It is the “skin” that we use to flesh out our skeleton and give it a particular look. We can swap in different skins via CSS without altering the original content in any way. They are relatively, but not completely, independent.
3. Controller
The browser is responsible for combining and rendering the CSS and HTML into a set of final, manipulatable pixels on the screen. It gathers input from the user and marshals it to any JavaScript code necessary for the page to function. But here, too, we have flexibility: we can plug in a different brower and get comparable results. Some browsers might render it faster, or with more fidelity, or with more bells and whistles.


So if you believe the web has been at all successful – most signs I’ve seen point to *yes* – then you also have to acknowledge **the incredible power of Model-View-Controller.**


It’s no coincidence that many of the most popular web programming frameworks also encapsulate MVC principles: Django, Ruby on Rails, CakePHP, Struts, and so forth. It’s also officially creeping into ASP.NET under the fledgling [ASP.NET MVC project](http://www.asp.net/mvc/).


Just take a gander at the project layout in a **sample ASP.NET MVC project**:


![](https://blog.codinghorror.com/content/images/2025/04/image-107.png)


It’s *almost* self-explanatory, if you’ve ever built an application of any kind:

1. Model
The classes which are used to store and manipulate state, typically in a database of some kind.
2. View
The user interface bits (in this case, HTML) necessary to render the model to the user.
3. Controller
The brains of the application. The controller decides what the user’s input was, how the model needs to change as a result of that input, and which resulting view should be used.


It’s beautiful in its simplicity, [as Terence Parr notes](http://www.artima.com/lejava/articles/stringtemplate.html):


> For the “MVC” of a web app, I make a direct analogy with the Smalltalk notion of MVC. The model is any of the logic or the database or any of the data itself. The view is simply how you lay the data out, how it is displayed. If you want a subset of some data, for example, my opinion is that is a responsibility of the model. The model knows how to make a subset. You should not be asking your graphics designer to filter a list according to age or some other criteria.
> The controller in a web app is a bit more complicated, because it has two parts. The first part is the web server (such as a servlet container) that maps incoming HTTP URL requests to a particular handler for that request. The second part is those handlers themselves, which are in fact often called “controllers.” So the C in a web app MVC includes both the web server “overlord” that routes requests to handlers and the logic of those handlers themselves, which pull the data from the database and push it into the template. This controller also receives HTTP POST requests and processes these, sometimes updating the database.
> I look at a website as nothing but a graph with edges with POSTs and GETs that routes pages.


Here’s one quick way to test if your application has properly segregated itself between the Model, View, and Controller roles: **is your app skinnable?**


> My experience is that designers don’t understand loops or any kind of state. They do understand templates with holes in them. Everybody understands mail merge. And if you say, “Apply the bold template to this hole,” they kind of get that, too. So separating model and view addresses this very important practical problem of how to have designers work with coders.
> The other problem is there is no way to do multiple site skins properly if you don’t have proper separation of concerns. If you are doing code generation or sites with different skins on them, there is no way to properly make a new skin by simply copying and pasting the old skin and changing it. If you have the view and the logic together, when you make a copy of the view you copy the logic as well. That breaks one of our primary rules as developers: have only one place to change anything.


**Skinnability cuts to the very heart of the MVC pattern.** If your app *isn’t* “skinnable,” that means you’ve probably gotten your model’s chocolate in your view’s peanut butter, quite by accident. You should refactor your code so that only the controller is responsible for poking the model data through the relatively static templates represented by the view.


The power and simplicity of properly implemented MVC is undeniable. But the first step to harnessing MVC is to understand *why* it works, both on the web, and also within your own applications.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[model-view-controller](https://blog.codinghorror.com/tag/model-view-controller/)
[mvc](https://blog.codinghorror.com/tag/mvc/)
[smalltalk](https://blog.codinghorror.com/tag/smalltalk/)
