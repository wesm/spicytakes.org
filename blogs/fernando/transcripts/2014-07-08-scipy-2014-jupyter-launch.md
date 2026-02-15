---
title: "Project Jupyter Launch Talk"
date: 2014-07-08
event: "SciPy 2014"
video_type: "Talk"
video_url: "https://www.youtube.com/watch?v=JDrhn0-r9Eg"
transcribed: 2026-02-15
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

This is an introduction to Project Jupyter. Project Jupyter is a project that evolved from IPython. IPython, as some of you may have seen a little tweet, is something that brought me to this community 11 years ago. And it has been evolving. And over time, we've been getting tired as the project grew in many directions of answering the question, "well, what about R, or Go, or any of the other 15 languages that now operate in our architecture?"

So we kind of took a long look at what is IPython. And very briefly, these are some of the pieces that make this weirdly scoped project that we call IPython. It is an interactive Python shell at the terminal, and it continues doing that. That shell, those ideas have been abstracted into a network protocol for interactive computing. And Lorena made a number of really amazing points this morning about what interactive computing is, and those hit close to the heart, obviously, for us.

It provides a kernel that speaks that protocol. It provides clients for that protocol based on the terminal, based on a Qt console developed by Evan Patterson, the notebook that has seen a lot of press in this audience. We've developed a file format and machinery around the idea of these notebooks, web services like the Notebook Viewer.

And everything on the left is really, really specific to the Python programming language. But everything on the column on the right is completely agnostic of the language that you're using. And ultimately, we're a project that wants to think about science, about communicating computational knowledge. The fact that people from our community like Chris and Jake Vanderplas are engaging with what was traditionally in our world, the fact that we've had tutorials about Julia here, matters a lot.

And so we're sort of moving in this direction of growing the project into this new project called Jupyter, which is inspired by what I think are the three open languages of science, which are Julia, Python, and R. It's not an acronym. As I said, it's inspired by these. But we're defining protocols and machinery to make all programming languages equal class citizens in the architecture.

We want to acknowledge the long history that astronomy has played in our community, from the work of the Hubble Space Telescope and the original funding for the Chaco project all the way to the continued maintainership of Matplotlib. And we also want to pay homage to Galileo, whose notebooks were the first open science papers.

There's a great blog post that I encourage you to read from Authorea about how science was always meant to be open, that looks at Galileo. These are Galileo's original notes of his observations of the moons of Jupiter, which when he published the Sidereus Nuncius in 1610, he actually published his observations with code and data. And they included -- it was a log of the dates and the state of the night. So there was data, there was metadata, and there was a narrative. So the first notebook was about the moons of Jupiter in 1610. And we're sort of trying to continue that tradition.

Who's doing this? Obviously, the existing IPython team and the existing IPython community. But we've already had wonderful participation of folks from the Julia team in a lot of this effort, from teams at Google and YT that you'll hear about soon. But more importantly, from those of you who care about growing open computational science in other directions.

So the next things that we're doing -- some of it is grunt work. We're moving anything that's language-agnostic to the Jupyter organization. We're going to have a lot of technical work to do splitting up the monstrosity of our main repos into independent components. And that's going to be hard. It's not going to happen overnight.

But more importantly, we want to build a community across languages of protocols. Protocols for computation across networks -- that's kind of the heart of what we've really imagined in the last few years. An architecture of clients and servers that speak these protocols. Open formats for communication and publication in whatever ways, whether it's books or scholarly communication or presentations. And tools for collaboration and education -- tools like the multi-user IPython notebook that many of you have asked us about and that we are working on. And the Collaboratory, which is the next talk.

Thank you.
