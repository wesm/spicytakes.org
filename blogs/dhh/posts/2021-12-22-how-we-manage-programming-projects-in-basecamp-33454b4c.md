---
title: "How we manage programming projects in Basecamp"
date: 2021-12-22
url: https://world.hey.com/dhh/how-we-manage-programming-projects-in-basecamp-33454b4c
slug: how-we-manage-programming-projects-in-basecamp-33454b4c
word_count: 751
---

That we manage all our programming projects in
[Basecamp](https://basecamp.com)
is perhaps an obvious admission since its our own product. But it's less obvious to some how that's possible, given the apparent lack of affordances to tie todos, messages, or check-ins together with code commits automatically. Some teams who are Basecamp curious can't seem get over this conceptual hump: How can we organize the programming work, if everything isn't tied together?
The simple answer is: don't. You don't need to string every todo to every commit. Micromanaging that level of detail has the appeal of superficial neatness, but without much if any payoff in additional ease or insight in practical terms. Modern programming projects are already packaged for easy reference and review through the magic of the
[pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
. That's all the pointer you need.
The vast majority of all feature development at Basecamp has a 1-1 relationship between a project and a pull request. This relationship provides all the tie-in necessary to match the work with the planning, at a coarse level that doesn't rely on micro linking every individual piece together. (I'll write another post about why I don't fancy breaking up the work into multiple small pull requests per project.)
The entire story is told in two parts: The Basecamp project that sets the scope, manages the outstanding work, documents the trade-offs and the considerations. The GitHub repository that holds the code, the per-line review notes, and the results of continuous integration testing.
Let's take
[the Out of Office feature](https://twitter.com/jasonfried/status/1472986193398697987?s=20)
we just launched for Basecamp. We ran the project in Basecamp as
*Cycle 6: BC4 Out of Office*
, and did the nitty-gritty design of How Should It Work in a series of todo threads, like this:

![bc3 todo of a feature.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc3NDE2LCJwdXIiOiJibG9iX2lkIn19--0b0d2b5ecda154da9dd4806b60651ceb474aef8af859b5535cf5cac04ebada01/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/bc3%20todo%20of%20a%20feature.png)

The entire feature was tracked as three major todo lists: A list for the epicenter (we could just have shipped this alone), a list for the stretch version (we ended up doing this as well), and a list for the integration with the mobile apps. The progress story was told through a simple
[hill chart](https://basecamp.com/features/hill-charts)
plotting these three scopes moving over the hill:

![three todolists moving over the hill chart.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc3NjI4LCJwdXIiOiJibG9iX2lkIn19--7f27686f3e41210e10bf01be7efe93f337d0a7b658ce870619fb2b7471626d6e/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/three%20todolists%20moving%20over%20the%20hill%20chart.png)

Along side this work of the work, we also used the Basecamp project to have discussions about leaving the campsite better than we found it. Could we move our avatar code in Basecamp to use Active Storage, a recent framework added to Rails?

![discussing moving avatars to active storage.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc3NzkwLCJwdXIiOiJibG9iX2lkIn19--e553a2f2fdff1cee5fb97f0ce7fcb387e22385a45d5919cd9cf32eb1b82f4f63/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/discussing%20moving%20avatars%20to%20active%20storage.png)

Occasionally we'd settle quick questions via Campfire that needn't be presented as a big argument:

![campfire settles quick questions.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc3OTgxLCJwdXIiOiJibG9iX2lkIn19--6cdbaeeb321a83f61e80056cac3c3326833ffcbca4557779b08783bfbed71b5d/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/campfire%20settles%20quick%20questions.png)

Then in the GitHub repository, we'd do code reviews, and handle the discussion of the implementation there:

![code review comment 1.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc4MjczLCJwdXIiOiJibG9iX2lkIn19--0f78511aee31012e440355ea718756ab9315ae70482ad2362f0883c2a2804470/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/code%20review%20comment%201.png)


![code review comment 2.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc4Mjc0LCJwdXIiOiJibG9iX2lkIn19--3555ae2a31b59944671bb5320b2ae2824c71f3f52bd9a828dc1a9ac99fddf6f6/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/code%20review%20comment%202.png)

And as you can see on this chop of the commits happening on the repository, none of these commits would have brought additional clarity to the project by being tied to a specific todo or update. And, if one commit really did stand out as being worthy of such a tie-in, you'd just copy and paste the URL to make the connection.

![list of commits.png](https://world.hey.com/dhh/33454b4c/representations/eyJfcmFpbHMiOnsiZGF0YSI6NjUxNjc4NjI1LCJwdXIiOiJibG9iX2lkIn19--53f6dbcd959245275e9e3f6de7410b909fa9c29df7484da6229f8bbc3cee1f7b/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/list%20of%20commits.png)

Programmers are trained in consistency and coherence. They're key properties of writing good code. But sometimes chasing those properties outside the code just don't offset the cost of doing so. Managing projects, be they code or otherwise, is mostly about communication. Making decisions about how things should work, doing the trade-offs to ship within the time allotted. That's the kind of work that benefits from narratives, selective highlighting, and human context far more than it does from some procedural idea of Tying It All Together.
I get that this might feel somewhat alien if you're working at a feature factory pulling tickets from a Jira backlog. That's a very different environment to the one we're cultivating at Basecamp through
[Shape Up](https://basecamp.com/shapeup)
. And as long as you're stuck in that assembly-line mindset, I do think Basecamp probably does seem incompatible. But that's why we're so keen to share the fully integrated story about how we work. From
[REWORK](https://basecamp.com/books/rework)
to
[It Doesn't Have To Be Crazy At Work](https://basecamp.com/books/calm)
to
[Ruby on Rails](https://rubyonrails.org)
to Shape Up to managing all of it in
[Basecamp](https://basecamp.com)
. We're here to help people set their sights on the right motivations, give them organizational ideas to visualize such a pursuit, gift the technical tools to implement it all, and manage everything through a system built around all these concepts.
It's all in and from Basecamp.
