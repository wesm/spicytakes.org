---
title: "The Next Larger Context"
date: 2023-07-27
url: https://www.elidedbranches.com/2023/07/the-next-larger-context.html
word_count: 1736
---


> “Always design a thing by considering it in its next larger context — a chair in a room, a room in a house, a house in an environment, an environment in a city plan” — Eliel Saarinen


Frequently we will be given problems to solve by other people. Early in our career, these problems will usually be well-scoped and specific, eg:

- Add this new data to an interface
- Make an endpoint that returns a certain specific calculation or piece of data.


And as we grow as engineers these tasks become bigger but often the success criteria remains well-defined:

- Write a service to manage the state of a customer.
- Create a new interface that allows developers to manage and track the status of their code change from review to deployment.


There are often plenty of decisions to be made in implementing these designs, but we are not identifying the problem to solve ourselves, just building the system to solve it well.


A major challenge that I see many people hit right around the time they become senior engineers is that they want to progress farther in their career, but they expect that the way they can do that is that they will be given a hard problem to solve that can only be solved by the level of technical skill they’ve gained so far. In fact, they expect that the career path from senior engineer to even loftier heights (depending on your company that might be things like “staff engineer” or “principal engineer”) will go much as it has gone up through to senior: you’re given increasingly harder problems, and you get to use your skills to solve them.


I didn’t write [The Staff Engineer’s Path](https://amzn.to/3MuiUMA) because I’m not qualified to talk about a path I didn’t follow. But what I can tell you based on my years of managing people throughout the stages of their career and watching friends who are on the individual contributor path is this: it is exceedingly rare that the path past senior engineer comes from being handed increasingly hard problems. It’s not that there aren’t hard problems to be solved, for sure, but they are generally being solved by the people who were already around on the team when the problem was discovered. And most of us don’t work in research, so the job of exploring the edges of possibility and discovering completely new things is not part of what we’re expected to do. Instead, at the senior levels, we are expected to identify problems that match business opportunities with something that technology can solve.


The blending of these two things, business opportunities and technology, is where you need to turn your eye, senior engineer. But that doesn’t mean you need to become a product manager, or a manager-manager, or even an expert in the business. Instead you should look at the problems you’ve been solving and that your team is solving, and follow Saarinen’s advice: look at them in the next larger context*. Here are some examples.


### **Current Context: A Bespoke Storage System**


Let’s say that you are on a team that supports a bespoke storage system that has been built up over years for your company. You’ve been something of an expert in the internals of that system, how it works, how it scales, you have added some features to it, and you are capable of teaching other developers how to use it.


The next-biggest context to start to understand here is how this storage system supports the company that is using it. Why do you need a bespoke storage system? What are people putting into it? What are their complaints about the system? What are they using it for that surprises you? You need to understand not only the way the system works itself, but the way the people who are using the system interact with it. This gives you the larger context that it is operating in, and will help you see the next opportunities for this area. Is it time to bring in a new type of storage system, one that fits with some of the data your users are producing that isn’t being served well by the current system? You are supporting a bespoke storage system, in an era where companies are trying to move away from bespoke systems in favor of open source or cloud hosted solutions. What does this mean for the future of your system? How can you get ahead of that trend, either by showing true differentiation between what your company needs vs the external options, or by embracing that trend and drawing down the differences to allow the company to eventually move to one or more of the external options?


The lesson from larger context here is that sometimes the advanced move is not to build a more complex thing, but to enable the company to embrace the broader trends in storage systems. But when the right thing is to build a bespoke solution, you will only do that well if you understand why you need to differentiate and how to make the case for that based on the understanding of the larger context around your system, namely, its users.


### **Current Context: An Inventory Management System**


Now let’s take a very business-focused example. Imagine that you are an engineer on an inventory management system. You have overseen the development of this system to account for the nuances of the company that uses it. You understand very well how the operations team thinks about inventory, how they plan to buy new things when inventory runs low, and the kinds of reports they want to see on a regular basis about all things inventory.


The next-biggest context here could be a few things. It could be the entire context of warehouse management. If your company not only tracks inventory but actually manages the warehouse they use to store inventory, they probably have some warehouse management systems that you have integrated with your inventory management system. How well do you understand that world? How does your inventory management system fit into it? Are there opportunities to build out better integrations that could provide more accurate reports for the operations team forecasting inventory needs?


The other side of this information flow of course is the information that you’re getting from the customers themselves. You’re tracking customer behavior in some way, if you’re working in any sort of modern commerce company. Are you automatically feeding information about customer interest in your products into the inventory management system to improve planning? Or, can you use information about inventory management to show to customers which items are about to be sold out?


These questions may sound like product questions, but in many cases they are all about technical challenges. Integrating all of these disparate systems together in an effective way is challenging. Even if all of these systems were developed in-house, they will have evolved at different rates and in different ways, and feeding new data from one system into another can sometimes require that you rethink the entire way the systems work together. If you built your inventory management system to do batch processing, for example, because you never expected that inventory would change fast enough to need real-time updates, you don’t have an easy way to feed information about low stock dynamically to the website. In fact, may websites fake statistics like the number of users buying a particular item because they have no easy way of feeding this information back and forth.


You need to think about the larger context of your system both to identify business opportunities that it could be filling, but also to predict how the technology you’ve built to support the current needs might fail you if you needed to integrate with a new model.


### **Current Context: A Developer Tools Team**


Our last example puts you in the context of a team that supports the tools and processes other engineers in your company use to develop software. You are the person who supports Jenkins, and all of its various integrations, for doing build and test. You know Jenkins inside and out, and have created an impressive set of automation that makes it easy for you to manage a large number of build and test pipelines for the company. However, this project has only been around for a little while and many teams still don’t have good continuous integration processes.


The next-larger context here is one of education. How are people using your product? How many teams understand the power of the automation that a system like Jenkins can provide? Where are there additional places that can take advantage of this system? What would be the blockers for them taking advantage of the system?


By teaching people how to use the system and getting more users into your system, you will start to understand the patterns of testing and integration more broadly at your company. You may identify pieces of support that are missing that would get more teams to be able to release more frequently, such as a good feature flagging system. You may identify that the artifacts you build are huge and take a long time to create, and this could lead you down a path of figuring out how to make those artifacts smaller or faster to build. You may simply identify the need to set up some kind of classes for new developers about how to write good unit and integration tests, so that they can get value from running their code through your pipelines.


---


What all of these examples show is that, as engineers, when we are looking to do a larger project than the ones we’ve done before, we need to step out of the context that we normally operate in. When you look one context bigger, you will see immediate new opportunities that you can tackle in adjacent areas. So don’t wait for the next project to come to you, seek it out by looking at the slightly bigger picture. That is where you will find your growth.


**You look only one context bigger because it is easy to overdo things and violate our “evolve complex systems from simple systems” principle when you try to go too broad.*


*Enjoy this post? You might like my book, *[*The Manager’s Path*](http://amzn.to/2nw1QN5)*, available on Amazon and Safari Online!*
