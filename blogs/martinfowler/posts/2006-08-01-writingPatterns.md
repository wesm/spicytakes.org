---
title: "Writing Software Patterns"
description: "I've spent a lot of my writing energy writing   patterns. From time to time I get asked questions about why I do   that and what makes a good pattern. This is a brief article about   how I look at pat"
date: 2006-08-01T00:00:00
tags: ["writing"]
url: https://martinfowler.com/articles/writingPatterns.html
slug: writingPatterns
word_count: 5431
---


When you look at multiple software systems, you often find recognize similarities.
    A set of program elements work together in roughly the same way in lots of
    different places, even if masked by different names and incidental
    variations in behavior. Experienced programmers learn how to solve common
    problem in particular ways, and make rough copies from what they've seen
    before, while adapting these copies to better fit their new home.


If possible, we'd like to capture these common solutions as libraries or
    frameworks. But often the variation is big enough that it's difficult to represent
    it as a single library. Worse still, we may find we wish to copy a solution
    from a system written in an entirely different programming language.


Therefore: in the early 1990's, a bunch of people in the software world
    developed the idea of software patterns to capture these common solutions.
    By writing them down, in a somewhat structured format, we can better share
    this otherwise implicit knowledge. And, in contrast to libraries, this writing can
    also explain when the solution is appropriate and what signs lead to an
    alternative approach


## What is a Pattern


A common definition of a pattern is that it is “a solution to a problem
    in a context”. That’s a definition that’s always struck me as being rather
    unhelpful.


For me a pattern is primarily a way to chunk up advice about a topic.
    Chunking is important because there's such a huge amount of knowledge you
    need to write software. As a result there needs be ways to divide knowledge
    up so you don't need to remember it all - what you need is to be able to get
    at a particular chunk of knowledge when you need it. Only then do you need
    details.


The solution provides a useful focus for the chunking. With
    some young eager programmer asking some grizzly veteran (i.e. anyone over
    thirty) how to deal with a particular situation and hear the veteran say âoh
    - you'll need an *identity map* thereâ. The colleague can then look up
    identity map in some suitable patterns book.


So to make this chunking work each pattern should **name a solution**.
    This solution should be concrete, at least at the level of discussion we are
    talking about. You should be able to go away and use the pattern once you're
    given the reference. If you're successful the name should enter the
    vocabulary of the profession. It can take a while to do this, but when you
    say “proxy” any reasonable professional should know what you mean.


Patterns should have recurrence, which means **the solution must be
    applicable in lots of different situations**. If you are talking about
    something that's a one-off, then it's not worth adding the name to the
    profession's vocabulary.


One of the interesting things here is that a singular solution can often
    lead to a recurrent pattern. This usually crops up when you see two
    different singular solutions which look completely different on the surface,
    yet have a deeper similarity - what Christopher Alexander refers to as the
    “core of solution”.


Let me give an example for this. I was looking at one of our early Java
    web projects. On this project the team wasn't allowed to use JSPs. So they
    wrote a set of Java classes which walked through a structure of domain
    objects, and produced the appropriate HTML for a particular domain object.
    They noticed they were getting duplication in the code for spitting out
    common HTML structures for fields, tables, etc. So they pulled all of the
    HTML spitting code out into a second utility class that had methods like
    `renderField (String label)`. When they did this they noticed
    that they could make drastic changes to the entire web application's
    appearance just by altering code in the utility class.


Later on I saw a different project. They were using XSLT to turn XML into
    HTML pages. But they needed to support multiple organizations who wanted the
    same data displayed in their own format. So they split the transformation
    into two steps, first producing an intermediate XML with elements like field
    and table, with second stage actually producing the HTML. They would have a
    different second stage for each organization.


Although it seems obvious as I write it now, but when I first saw these
    two projects I sensed there was something similar in their approaches.
    However it took me several months to understand the key point - splitting a
    transformation into two steps: logical page and physical (HTML) page. This
    is the “core of the solution” which I wrote up as [Two Step View](https://martinfowler.com/books/eaa.html). One of the great intellectual
    challenges of patterns is finding and isolating this core amongst all the
    surrounding stuff that's needed on real projects.


### Patterns versus Recipes


A popular, and very effective, form of technical writing is the
      cookbook style (eg [The Perl
      Cookbook](https://www.amazon.com/gp/product/0596003137/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0596003137&linkCode=as2&tag=martinfowlerc-20), [Rails Recipes](https://www.amazon.com/gp/product/0977616606/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0977616606&linkCode=as2&tag=martinfowlerc-20)).
      There is a lot of similarity between cookbooks and patterns books. Both
      emphasize a problem-solution style.


I see the big difference between the two in the notion of building a
      vocabulary. Recipes tend to be more particular, usually tied to a
      particular programming language and platform. Even when patterns are tied
      to a platform, they try to describe more general concepts.


As a consequence of this recipes have a stronger problem focus than the
      solution focus in patterns.


Although my writing interest is in patterns, this reflects my interest
      in general design principles rather than a judgment on the relative
      usefulness of the two styles. Both are effective for same basic reason -
      they chunk based on a concrete thing somebody wants to get done today. As
      a result I find both very effective. You can also learn great principles
      from them, but it's the answers to particular questions that bring you to
      the table.


## Why are Patterns important?


One of the quotes that I find particularly appealing when I think about
    the need for patterns that that part of interest in patterns came from
    “...observations that projects fail despite the latest technology for lack
    of ordinary solutions” [[PLoPD 1]](https://www.amazon.com/gp/product/0201607344/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201607344&linkCode=as2&tag=martinfowlerc-20). Patterns provide a way
    to organize and name those ordinary solutions to make it easier for people
    to use them.


Since these solutions are ordinary, it's common that experts in a field
    won't find anything new in a patterns book. For such people the biggest
    value of a patterns book is to help them to pass on the solutions to their
    colleagues.


Despite my liking for patterns, I don't think that
    patterns are the right approach for all situations. Even in my own latest
    [patterns book](https://martinfowler.com/books/eaa.html), I used a mixture of patterns
    and narrative text. I think the patterns helped focus the narrative and
    provided a good way for me to separate the details of the solutions from the
    overview discussion of them. Patterns are a communication medium, and like
    any communication technique there are situations where they work well and
    those where they work badly. Practice and familiarity help you tell the
    difference.


## Important Parts of Patterns


Anyone who takes a look at patterns is usually struck by the fact that
    most patterns are written using a regular form. Once you look at two sets of
    patterns you realize hardly ever do two patterns authors use the same form.
    The different patterns forms all have particular qualities to them, and any
    patterns author will tend to pick a form that works well with their innate
    preferences.


Despite the various forms, most patterns do have common elements. I'll
    talk about the different forms later on, but I think that's easier to do if
    I cover some general principles first.


### Patterns are Solutions


Almost anything written about patterns has a definition that reads
      something like “a pattern is a solution to a problem”. While I don't
      disagree with that statement, I think it does tend to under-emphasize the
      point that patterns are primarily about solutions.


I think it's important to say this, because there is a certain mystique
      that tends to embroil patterns. To cut through that mystique, we must
      never forget that the whole point of writing a pattern is to describe a
      recurring and useful solution. Success is all about doing that in a way
      that others can replicate that solution when it's appropriate. Everything
      else is secondary - which means that however we choose to write the
      pattern, whatever form we take - all has to support this. Too often I've
      seen patterns writers, including myself, get lost in a particular format
      and lose sight of this simple priority. So whenever writing is getting
      difficult, remember it's the solution that counts.


And the problem? Well any solution is a solution to a problem. How
      could you have a solution without a corresponding problem? Understanding
      the problem (or problems, a pattern can solve more than one) is a key part
      of understanding the solution. Thinking about the problem helps you focus
      on the “core of the solution”. It also helps us avoid sliding into too far
      of a tools-oriented discussion. So understanding the problem is important
      - indeed vital. But the solution should remain the focus of the
      pattern.


### An Evocative Name


One of the valuable features of patterns work is that it develops a
      vocabulary with which we can talk about how to do things. By naming
      recurring solutions, we can gradually build a vocabulary of software
      design that goes beyond the usual issues of technology that we normally
      wrestle with. I understand Java's listeners, and .NET's delegates better
      when I know they are part of ways of implementing the Observer pattern.
      The name “observer” gives me a hook that gives me a way into understanding
      new technological concepts - which often have different names in different
      technologies.


Choosing good names is hard, and I've found that I'm constantly
      fiddling with names even very close to deadlines. Since they are going to
      be a vocabulary, it's worth putting a lot of effort into getting good
      names. Just think of what that wrinkled veteran needs to say.


As a result names should be short, but of course it's hard to come with
      tight names. Mine tend to be two or three words - as I feel that most of
      the good one word ones are taken.


If I see patterns that are alternative ways of doing something, then I
      like to use different adjectives that modify a common noun. So Page
      Controller and Front Controller are two different forms of Controller.
      Strictly they are forms of Input Controller in P of EAA, but I only use
      three words if I really have to (as I felt I did with Single Table
      Inheritance and it's alternatives.)


I like to make my pattern names be **noun phrases**. One of
      the valuable qualities of patterns is that they create a vocabulary, and
      that's easier to do with nouns. Verbs require more grammatical variation
      to fit them into prose, which makes it harder to consistently use the
      name. I like to imagine a wizened old developer telling her colleagues:
      “you need to use a *<pattern-name>* here”.


### Why as well as how


When we talk about solutions, it's easy to focus on the solution itself
      and how to apply the solution. It's harder to talk about when the solution
      is appropriate and what conditions are suitable for it, or not. This is
      why patterns writers put emphasis on the problem, because that focuses our
      minds on the trigger for the pattern. It's also why patterns writers talk
      about forces, because forces are a way of exploring the indications and
      contra-indications for the pattern.


Whenever I think I have a pattern, I try to think about when I would
      *not* use the pattern. This often leads me to alternative patterns,
      which is why my patterns often come in groups of alternatives.


I'm particularly suspicious of whole pattern languages that only
      describe one set of alternatives. One of the triggers for [P of EAA](https://martinfowler.com/books/eaa.html) was my annoyance with people who talked about
      The One Architecture to use for J2EE. Software systems, even within a
      particular area such as enterprise applications, live in a diverse world.
      There are lots of ways of doing things, and often most of them are right
      in some given circumstances. So whenever you think âyou should never do
      thatâ, think hard about it. There may be a time, and not just will that
      lead you to another pattern - it will also help you understand your
      primary pattern better.


### Code Examples


Many people worry about examples in patterns, and code examples in
      particular. After all patterns are about deep similarities in solutions
      that look different every time we use them. There is a genuine reason to
      be worried that some readers will take the example as the pattern,
      thinking about patterns as glorified macros.


In my view there are many people that understand things much better by
      example. When given an example, they can then start abstracting for the
      general principle. That's certainly the way I seem to work. So I'd rather
      give an example, and run the risk of lack of abstraction, than avoid the
      example and lose readers completely in the abstraction.


If you are very concerned about a particular interpretation of a
      pattern, then a useful approach is to use multiple examples. The different
      examples of the same pattern can help illustrate common threads. Different
      examples can be different approaches using the same platform, or using
      different platforms.


Of course some people won't look at code examples, since any code
      example contains a lot of details. As a result I try to make my code
      examples skippable - by which I mean that I write the pattern so it's
      understandable without the code example. Code examples are then a
      bonus.


When writing a code example there's a tension in how
      complicated to make it. If I make it too simple, then people
      may dismiss it as not realistic, but if I make it too complex
      then people have to understand a bunch of stuff that's nothing
      to do with the pattern in order to understand the
      pattern. Complicated enough and we get to what Micheal Feathers
      calls the MEGO point (âMy Eyes Glaze Overâ) and I've lost them
      completely. I prefer to err on the side of being too simple. If
      I get the simple stuff clear then I (or others) can add more
      complicated stuff with interactions between patterns later. I'd
      rather people understand a little than fail to understand a
      lot. This desire is reinforced by the chunking that patterns are
      about - a reader should only have to read that one pattern to
      understand the pattern.


## Common Pattern Forms


Every author tends to make his own particular pattern form, but certain
    pattern forms have become more well-known. These are often used exactly by
    new authors, or at least as starting points.


### Alexandrian Form


Many people see Christopher Alexander's [A
      Pattern Language](https://www.amazon.com/gp/product/0195019199/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0195019199&linkCode=as2&tag=martinfowlerc-20) (APL) as an important influence in the patterns
      world. Alexander write about building architecture and was a big influence
      behind some of the early advocates of software patterns. He wrote his
      patterns book in a particular form which is known in the software patterns
      world as Alexandrian form. As well as the patterns in his book, you can
      also find good examples of this form in [Domain-Driven Design](https://www.amazon.com/gp/product/0321125215/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321125215&linkCode=as2&tag=martinfowlerc-20). On the web a good example
      is Josh Kerievsky's [Knowledge
      Hydrant](https://www.industriallogic.com/papers/khdraft.pdf) patterns.


Like many standard forms, we actually see a fair amount of variation of
      the Alexandrian form in practice. I'll describe it by quoting the
      description of the form from APL


> For convenience and clarity, each pattern has the same format. First,
>         there is a picture, which shows an archetypal example of that pattern.
>         Second, after the picture, each pattern has an introductory paragraph,
>         which sets the context for the pattern, by explaining how it helps to
>         complete certain larger patterns. Then there are three diamonds to mark
>         the beginning of the problem. After the diamonds there is a headline, in
>         bold type. This headline gives the essence of the problem in one or two
>         sentences. After the headline comes the body of the problem. This is the
>         longest section. It describes the empirical background of the pattern,
>         the evidence for its validity, the range of different ways the pattern
>         can be manifested in a building, and so on. Then, again in bold type,
>         like the headline, is the solution - the heart of the pattern - which
>         describes the field of physical and social relationships which are
>         required to solve the stated problem, in the stated context. This
>         solution is always stated in the form of an instruction - so that you
>         know exactly what you need to do, to build the pattern. Then, after the
>         solution, there is a diagram, with labels to indicate its main
>         components.
> After the diagram, another three diamonds, to show that the main body
>         of the pattern is finished. And finally, after the diamonds there is a
>         paragraph which ties the pattern to all those smaller patterns in the
>         language, which are needed to complete this pattern, to embellish it, to
>         fill it out.
> -- [[alexander-apl]](https://www.amazon.com/gp/product/0195019199/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0195019199&linkCode=as2&tag=martinfowlerc-20)


The patterns in APL average at half a dozen pages each.


The Alexandrian form is a very narrative form, with relatively few
      headings. As it a result it tends to flow better then most alternatives
      when you read it. The bolded summary sentences of the problem and the
      solution stand out well, and allow you to skip through a large body of
      patterns very quickly.


In software patterns that use the Alexandrian form, a common variation
      (used by [Big Ball of Mud](http://laputan.org/mud/)) is to divide up the
      main section, the body of the problem, into two parts. The first part,
      after the problem headline, expands on the problem and the issues around
      it. The second part is moved to after the solution summary, and describes
      the details of the solution.


I heard Richard Gabriel criticize this, on the grounds that it forces
      you to duplicate much of the discussion of alternatives and trade-offs. I
      didn't think too much about this before, but I find I agree with him.
      Cutting up the body breaks the flow of the pattern and makes it more
      choppy as you worry about whether issues should be discussed in the
      problem half or the solution half.


Most patterns books organize the patterns as relatively self-standing
      sections, like a reference book. [Evans](https://www.amazon.com/gp/product/0321125215/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321125215&linkCode=as2&tag=martinfowlerc-20)
      embeds the patterns into the flow of a general narrative book. The
      Alexandrian form helps him do this, as the flow of patterns is more
      narrative than the more structured pattern forms.


### GOF Form


The GOF form is the form used for the seminal [Gang of
      Four](https://www.amazon.com/gp/product/0201633612/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201633612&linkCode=as2&tag=martinfowlerc-20) book, that really launched patterns into the software world.
      It's a very structured form, breaking up the pattern into many headings:
      Intent, Motivation, Applicability, Structure, Participants,
      Collaborations, Consequences, Implementation, Sample Code, Known Uses, and
      Related Patterns. The GOF pattern are quite large, a dozen pages each.


### Portland Form


The Portland form got its name from the fact that several people, from
      Portland Oregon, at the first patterns conference all used a similar form.
      A good on-line example is [[cunningham-checks]](http://c2.com/ppr/checks.html).


Portland form is entirely textual and very short, usually less than a
      page per pattern. A couple of paragraphs describe the problem, then there
      is the word âthereforeâ emphasized typographically, followed by a couple
      of paragraphs that describe the solution.


### Coplien Form


So called, because it's most identified with Jim Coplien, I've also
      heard it referred to as Canonical Form, although I'm not sure which canon
      such people are referring to. A good on-line example is [[coplien-fault-patterns]](https://sites.google.com/a/gertrudandcope.com/info/Publications/Patterns/PLoP95-telecom)


I see this form varied a good deal. The key elements are headed
      sections for Problem, Context, Forces, and Solution. Most authors will add
      a few extra sections too. Each section is a few paragraphs, with the
      forces section commonly a list of bullet points. Patterns in this form are
      usually fairly short - a couple of pages.


### POSA Form


This form gets its name from the [POSA](https://www.amazon.com/gp/product/0471958697/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0471958697&linkCode=as2&tag=martinfowlerc-20) book.
        Similarly to GOF it is a very structured and quite large form, although
        their headings are different: summary, example, context, problem,
        solution, structure, dynamics, implementation, example resolved,
        variants, known uses, consequences, and see also. The patterns are
        usually just over dozen pages in length. An important part of this form
        is that the patterns are preceded by a narrative chapter that summarizes
        the patterns and describes the overall topic.


### P of EAA Form


I'm being cheeky to call this a standard form, since nobody other than
      me uses it. But I've been writing patterns for a long time, experimenting
      with various styles, and this is the one I've come to prefer. It's fairly
      narrative, with a few sections: how it works, when to use it, and one or
      more examples. The length averages at around eight pages, but it varies
      from one page to well over a dozen. [This](https://martinfowler.com/eaaDev/Notification.html) is a recent example.


## Choosing Your Pattern Form


As you can see by just looking at the list of common forms, there is a
    lot of different ways you can write your patterns, in fact there's much more
    than that. I only mentioned those that are commonly referred to - every book
    typically uses its own and many papers show many further variations. So my
    primary piece of advice is to remember that your pattern form is a personal
    choice. Different forms work for different authors, because different
    writing styles work with different personalities. The most important thing
    is to find a form that works with your style of writing, and for the ideas
    that you want to convey.


A good first step is to begin by reading. Read a lot of different pattern
    books and papers. Concentrate on the content, but ask yourself which forms
    seem the most comfortable to you. To really appreciate this you need to read
    them both in a start-to-end style, but also by looking up and skipping
    through them. You probably have already done this a lot in the course of
    your other work - which patterns did you find work best for you?


Once you've got an idea of what form (or forms) you like, start writing.
    Try to experiment with several different pattern forms. A useful exercise is
    to write the same pattern in a few different forms to see which ones seem to
    work best for you. Get some people to review them and tell you which forms
    seem to read best for them. Don't be afraid to experiment here, it took me
    many years before I found a pattern form that worked for me.


Once you've picked a basic form, don't let the form force its way too
    much over the content. I notice this problem particularly with the very
    structured forms like GOF and POSA - people feel that they have to put
    something in to every heading for every pattern. But not every pattern
    requires the same treatment. You'll find some elements that you want in
    every pattern, but many elements are optional. It's better to leave
    something out than put in a weak placeholder.


A big question is whether you prefer a more narrative style, or a
    structured style with many headings. Often when people start out they like
    the headings because it directs them on how to write. I tend to prefer a
    more narrative style, because it tends to lead to writing that flows
    better.


Patterns vary considerably in their size. Portland form often gets a
    pattern over and done with in a few paragraphs, POSA can go on for a couple
    of dozen pages. Your choice here depends a great deal on how much detail you
    want to go into. If you are going to explore implementation issues and
    provide sample code, you are going to inevitably have longer patterns. In
    this case, more structure is often more useful, although I use just a few
    headings even for long patterns.


## Common Issues


When you sit down and write patterns, many issues come up for lots of
    pattern authors. There's not necessarily a right answer to these questions,
    but at least I can give my perspective on them.


### Arranging Patterns into a Structure


A common problem that people run into is how to structure the
      patterns they are writing. Patterns encourage chunking, and it's
      easy to concentrate on the chunks. But how do you fit these
      chunks into something meaningful? I've seen many people struggle
      with an overall structure to a collection of patterns.


My biggest advice here is âdon't worry about it - I don'tâ. I
      prefer to concentrate on the individual patterns, describing
      the interesting solutions that I come across. Once I begin to
      get a set of patterns together I then think about how they
      should be structured and look for obvious gaps that need more
      patterns that cover them.


In particular, you don't have to spend a lot of time trying to get an
      overall structure right before you dig into the patterns. I find
      I don't really understand the patterns until I dig into the
      details of describing them.


Remember that in the end it's more valuable to have a bunch
      of good patterns, poorly organized than it to have a really good
      structure with weak patterns underneath them.


### Patterns and Pattern Languages


I've often been troubled by a lot of the mystique that people
      summon up around patterns. One of the common areas to kick up
      this kind of dust is in the issue of patterns and pattern
      languages. This is often accompanied by 'this isn't a pattern
      language, it's *merely* a catalog of patterns'.


The idea behind a pattern language comes again from
      Alexander. The idea is that you have a body of patterns with a
      structure that leads you from pattern to pattern. You begin with
      (usually) some very strategic patterns, each pattern leads you
      to a point where you have to decide to apply other patterns. A
      pattern language has a flow that connects the various patterns.


If a pattern language comes easily to you, then well and
      good - but I don't think a book that's just a loose collection
      of patterns is a bad thing. Certainly none of my books have been
      pattern languages, neither is GOF. Pattern languages are also
      very hard to write - and I've seen people get stuck
      trying to put them together. Remember that the value of the
      patterns is the usefulness of what they say, in this sense I
      look at pattern languages as a structuring mechanism - and the
      same comments apply to what I said above.


([Knowledge Hydrant](https://www.industriallogic.com/papers/khdraft.pdf) is a good
      on-line example of a pattern language.)


### Granularity of Patterns


One of the biggest issues I worry about is how conceptually
      big to make my patterns. This isn't about how many pages it
      takes to write them up, but how much conceptual ground is
      covered by a pattern.


As you start delving into patterns you begin to realize that
      you often have choices between turning two related concepts into
      separate patterns, or combining them as variations of a single
      pattern. A good example of this from GOF is the Proxy pattern,
      which describes four variations (remote proxy, virtual proxy,
      protection proxy, and smart pointer). You could write these as
      four separate patterns, or as one pattern with four variations,
      or as one summary pattern with four further patterns for each
      variation.


There's no easy answer to this one, or at least if there is
      I'd love to know what it is. Deciding where to place the
      boundaries between patterns is one of the hardest problems I
      wrestle with.


One thing I do assert is that if you do split them, don't try
      to have an overall pattern too. So when I worked on patterns for
      mapping inheritance in object-relational patterns I picked
      different patterns for Single Table Inheritance, Class Table
      Inheritance, and Concrete Table Inheritance. I didn't try have
      an overall âinheritance mappingâ pattern to tie them
      together. This does mean there's some duplication is the 'when'
      section as I have to discuss the trade-offs between the three in
      each case. I can live with a some of that duplication (just
      don't cut and paste the text, write it differently each
      time). There is a tying together in the narrative - which is
      part of the purpose of the narrative in my style.


### Be Specific


A common question that comes up in reviews of patterns is
      where a pattern that written for one domain seems to also make
      sense in others. Alice writes a pattern about database
      interaction, Bob says that similar advice applies to network
      communications too and suggests making the pattern more general.


In general, I resist such generalizations. The key question
      is the author's experience. If Alice knows about databases but
      not about network programming, then a pattern she writes should
      describe the database situation. The reader may then consider it
      applicable to their area of expertise, but it's up to reader to
      decide if it's applicable. Such a reader is in a better
      situation to make that judgement than the writer.


### Tasks rather than Tools


One of the great plagues of software writing is a focus on
        tools rather than tasks. Tool oriented books say - “here is a
        toolbox and I’ll explain how you use each tool”. Task oriented
        books say “here’s a bunch of tasks you need to do, here’s how
        to do them (showing you the tools in the process)”. Tool
        orientation is easier to write, especially for software
        manuals, because it’s easy to look at a framework (say) and
        identify the tools.


But task orientation is much better. People don’t approach
        a book saying “how do I use this widget”, instead they come
        needing to do some task and trying to find out how to carry
        that out. With a tools book they spend time looking at likely
        tools to see if they can help; this is all well and good, but
        it’s much better if they can find their task right there
        instead. This is why recipe oriented books are so handy - they
        focus on tasks.


Patterns always fall into the danger of being tool oriented
        - after all what we are doing with patterns is trying to
          identify conceptual tools. It's thus very easy to end up
          making a book into a tool-oriented guide to newly named
          tools.


This is the importance of the problem part to
        patterns. Although in the end we are identifying tools, we can
        mitigate the dangers of tool-orientation by putting a lot of
        thought into the problem each pattern (tool) solves. We are
        free to shape the pattern boundaries how we choose, indeed
        this freedom is what makes pattern writing so hard. Trying to
        make the work as task-oriented as we can helps draw those
        boundaries in a useful way.


### Nothing new here


A common complaint about patterns books is that they have
        nothing new to tell experienced developers. Not just is this
        true, but it's the whole point of patterns.


Patterns are there to capture knowledge from the field, not
        to present original ideas. As a result it's inevitable that
        patterns books aren't going to add stunning new ideas to those
        who have been working in a field for a while. But even so I
        think there's an important role for patterns books even to
        those who don't need to learn the ideas. This role is to help
        the experienced people communicate their experience to those
        around them who are less experienced. Few teams consist of
        entirely of seasoned developers. One of the most important
        things an experienced leader can do is pass on her skills.


So if you're evaluating some patterns in a field you're an
        expert in, don't expect to learn new things. Instead evaluate
        them on how they would help you to communicate your knowledge
        to others. Try them out by using them yourself and seeing if
        they help people grasp important concepts.


This is why patterns books should also age well. Many of
        the fundamentals of software design don't change very rapidly,
        even though our technologies do. So don't be concerned too
        much if a pattern book is old.


---
