---
title: "Making the web better. With blocks!"
date: 2022-01-27
url: https://www.joelonsoftware.com/2022/01/27/making-the-web-better-with-blocks/
word_count: 867
---


You’ve probably seen web editors based on the idea of *blocks*. I’m typing this in WordPress, which has a little + button that brings up a long list of potential blocks that you can insert into this page:


![](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2022/01/wordpressblocks.png?resize=260%2C573&ssl=1)


This kind of “insert block” user interface concept is showing up in almost every blogging tool, web editor, note-taking app, and content management system. People like it and it makes sense.


We have seem to have standardized on one thing: the **/** key to insert a new block. Everything else, though, is completely proprietary and non-standard.


I thought, wouldn’t it be cool if blocks were interchangeable and reusable across the web?


Until now, every app that wants blocks has to implement them from scratch. Want a calendar block? Some kind of fancy Kanban board? Something to embed image galleries? Code it up yourself, buddy.


As a result of the non-standardization of blocks, our end-users suffer. If someone is using my blog engine, they can only use those blocks that I had time to implement. Those blocks may be pretty basic or incomplete. Users might want to use a fancier block that they saw in WordPress or Medium or Notion, but my editor doesn’t have it. Blocks can’t be shared or moved around very easily, and our users are limited to the features and capabilities that we had time to re-implement.


To fix this, we’re going to create a protocol called the [Block Protocol](https://blockprotocol.org).


It’s open, free, non-proprietary, we want it to be everywhere on the web.


It’s just a protocol that embedding applications can use to embed blocks. Any block can be used in any embedding application if they all follow the protocol.


Our hope is that this will make life much easier for app developers to support a huge variety of block types. At the same time, anyone can develop a block once and have it work in any blog platform, note-taking app, or content management system. It is all 100% free, open, and any sample code we develop showing how to use the protocol will be open-source.


We’ve released a very early draft of the Block Protocol, and we’ve started building some very simple blocks and a simple editor that can host them.


![](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2022/02/bp_illustration_1-v2.png?resize=730%2C485&ssl=1)


We’re hoping to foster an open source community that creates a huge open source library of amazing blocks:


![](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2022/02/bp_illustration_2-v2.png?resize=730%2C333&ssl=1)


What can be a block?

- Anything that makes sense in a document: a paragraph, list, table, diagram, or a kanban board.
- Anything that makes sense on the web: an order form, a calendar, a video.
- Anything that lets you interact with structured or typed data: I’ll get to that in a minute.


If you work on any kind of editor—be it a blogging tool, a note-taking app, a content management system, or anything like that—you should allow your users to embed blocks that conform to the Block Protocol. This way you can write the embedding code once and immediately make your editor able to embed a rich variety of block types with no extra work on your part.


If you work on any kind of custom data type that might make sense to embed in web pages, you should support the Block Protocol. That way anybody with a hosting application that supports the protocol can embed your custom data type.


Because it’s all 100% open, we hope that the Block Protocol will become a web standard and commonly used across the Internet.


That will mean that common block types, from paragraphs and lists to images and videos, will get better and better. But it will also mean that some esoteric block types will be embeddable anywhere. Want to create a block that shows the Great Circle routing for a flight between two airports? Write the code for the block once and it can be embedded anywhere.


Oh, and **one more thing**. Blocks can be highly structured, that is, they can have types. That means that they magically become machine-readable without screen scraping. For example, if you want to create an event block to represent an event on a calendar, you will be able to specify a *schema* that describes the event data type in a standard way. That way tools like calendars can instantly parse and understand web pages that contain your event block, reliably.


Over time, it will mean that anyone can easy publish complex, typed data sets on the web that are automatically machine-readable without extra work. (Have you ever seen one of those websites where there’s a link to “download the data set in .XLS format”? Yeah, say goodbye to that.)


**We’re going public with this very early in the development process** because we need a lot of help!


Everything we have so far is version 0.1. It’s simple and not very good yet and going to need some iteration before it has the hope of truly being a useful web protocol.


This is an open protocol, free and non-proprietary, and it’s going to make the open web much better if widely adopted, so we need to start getting people involved early, giving us feedback, and building new things!


[Go read more about the Block Protocol now!](https://blockprotocol.org)
