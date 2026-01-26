---
title: "Don't put data science notebooks into production"
description: "We've come across many clients who are interested in taking the computational notebooks     developed by their data scientists, and putting them directly into the codebase of     production applicatio"
date: 2020-11-18T00:00:00
tags: ["data analytics"]
url: https://martinfowler.com/articles/productize-data-sci-notebooks.html
slug: productize-data-sci-notebooks
word_count: 1362
---


First, let’s describe what computational notebooks are. Notebooks originated with the
    Wolfram Mathematica language and the idea is now quite popular in the data
    science community, particularly with Python and R users. Basically, it's a
    combination of a script consisting of commands integrated with some
    visualization and documentation. You see the code that has been run and the
    result, whether it is just text, a nicely formatted table or a graphical
    figure. The documentation can explain what is happening, making them useful
    for tutorials. Notebooks are
    essentially a nicer interactive shell, where commands can be stored and
    easily rerun with changes. The graphics or outputs are right there in one
    window rather than saved elsewhere in files or popped up in other windows.
    The interactive session can be saved in one file and shared so that
    anyone else (under certain conditions) can run it with the same results.


Notebooks are essentially good at two things. They make a nice
    interactive shell for data scientists doing interactive, exploratory work.
    They are also good for demos. They are not crucial tools for doing
    data science and many data scientists do not use them at all.


Notebooks share a lot of characteristics of spreadsheets and have a lot
    of the same strengths and weaknesses. First, the strengths. They allow
    people without much in the way of programming skills to do useful
    quantitative work. Notebooks are essentially scripts and scripting is the
    first step in general programming. Excel, for example, allows for scripting
    as well, such as using formulas. And one can actually do a whole lot of
    useful work with drag and drop operations as well. They both are tools that
    combine the concerns of storage (both code and data), visualization, and
    bussiness logic into one application.


Having one tool being the one-stop-shop for several concerns has both
    advantages and disadvantages. The advantage is simplicity for simple things.
    Why would I use a database, a Java application and Javascript frontend just
    to do some simple operations to calculate the payroll for the dozen
    employees that I employ at my startup? That’s what spreadsheets are great
    at. But that doesn’t mean a spreadsheet should be used to handle payroll for
    a major international bank. And they are not used for that, for good
    reasons. Those situations are more complex. There are many more variables.
    They have auditing requirements. The data may be quite large, etc.


Teams of people can succeed at building large applications to solve
    complex problems but only if they can control that complexity. And we have
    very few tools to do that. The most important of all is to break it into
    many smaller, less coupled problems. That’s why in the
    [Presentation Domain Data Layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) pattern, we
    separate UI, domain logic, and storage. We can focus on how a calculation is
    performed without being distracted by how it will be displayed or how data
    is accessed.


Putting a notebook into a production pipeline effectively puts all the
    experimental code into the production code base. Much of that code isn't
    relevant to the production behavior, and thus will confuse people making
    modifications in the future. A notebook is also a fully powered shell, which
    is dangerous to include inside a production system. Safe operations require
    reproducibility and auditability and generally eschews manual tinkering in
    the production environment. Even well intentioned people can make a mistake
    and cause unintended harm.


What we need to put into production is the concluding domain logic and
    (sometimes) visualizations. In most cases, this isn't difficult since most notebooks
    aren't that complex. They only encourage linear scripting, which is usually
    small and easy to extract and put into a full codebase. If it's more
    complex, how do we even know that it works? These scripts are fine for a few
    lines of code but not for dozens. You’ll generally want to break that up
    into smaller, modular and testable pieces so that you can be sure that it
    actually works and, perhaps later, reuse code for other purposes without
    duplication.


So we’ve argued that having notebooks running directly in production
    usually isn’t that helpful or safe. It’s also not hard to incorporate into a
    structured code base. So why is anyone even talking about how to
    productionize notebooks? **The essence of the problem is that data scientists
    and software developers do not always communicate very well or understand
    what the other needs to do.** Many data scientists do not really understand
    the concerns of professional software developers such as automated,
    reproducible, and auditable builds, or the need and process of thorough
    testing, or the importance of good design in making codebases supportable
    and flexible. In turn, many software developers do not really understand
    what data scientists are doing.


While two types of people can often work well together without
    understanding the details of what the other has to do, this is generally not
    one of those situations. There are tremendous advantages to be had when data
    scientists and developers can share knowledge and learn a little more about
    what the other has to do and why they do things the way they do. **This is to
    say that data scientists should strive to learn software development and work fully
    embedded in the delivery team responsible for delivery of production
    software**. They don't need to reach full capacity in this regard but they
    should fully understand the basics and continue to learn in the areas most relevant
    to their work on the team.


They’ll find that using many of the techniques of software
    development actually makes them more productive as data scientists. They’ll
    find they can handle more complex tasks and spend far less time debugging
    when they structure code properly. Developers will find that they can make
    much better use of data science models and methods when they take the time
    to understand a little more about what is actually going on. Neither needs
    to become fully skilled in the other field but they should at least be competent
    in its basics.


Notebooks are useful tools for interactive data exploration which is the
    dominant activity of a data scientist working on the early phase of a new
    project or exploring a new technique. But once an approach has been settled
    on, the focus needs to shift to building a structured codebase around this
    approach while retaining some ability to experiment. The key is to build the
    ability to experiment into the pipeline itself. An example would be
    including a machine learning model registry which allows one to modify
    parameters at either run-time or build-time and stores results such as
    performance metrics in a data store. This has the advantage that experiments
    are always repeatable as they run with versioned code and their results are
    retained for purposes of comparison, and also as demonstrable markers of
    progress. This ensures that any difference in effect can be demonstrated to
    come from an intended cause which is the hallmark of any good experiment.
    The goal, after all, is to learn what changes to production software will
    create more business value. The smaller the gap between the environment of
    the experiment and the actual implementation, the more we can be confident
    that the change really creates value. Another key idea is to build data
    science pipelines so that they can run in multiple environments, e.g., on
    production servers, on the build server and in local environments such as
    your laptop. That enables even more possibilities of experimentation without
    disrupting anything happening in production.


To conclude, we believe the discussion of how to productionize data
    science notebooks is missing the point. The goal should be to empower data
    scientists and their entire delivery teams to come together and build
    software that delivers the required business functionality while still
    retaining the ability to experiment and improve. This requires moving out of
    notebook style development after the initial exploratory phase rather than
    making it a continuing pattern of work requiring constant integration
    support. This way of working not only empowers data scientists to continue
    to improve the working software, it includes them in the responsibility of
    delivering working software and actual value to their business
    stakeholders.


---
