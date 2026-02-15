---
title: "DataArray Lightning Talk"
date: 2010-07-01
event: "SciPy 2010"
video_type: "Lightning Talk"
video_url: "https://archive.org/details/Scipy2010-FernandoPerez-Dataarray"
transcribed: 2026-02-15
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

You can think of this as a prelude to the BoF that we'll have later today, for those of you interested, that follows in the discussion of pandas and statsmodels from the data we've already done. To motivate the idea that I have here, the actual code is available on GitHub already. That is the GitHub website, but what I'll be showing you is just the actual build of the documentation.

The motivation is the following. NumPy arrays, that we all love and use, have very rich semantics for handling the internal content of each cell. If I think of a NumPy array as a cube, or a square, or a four-dimensional cube of data, in each of the cells I can describe with lots of flexibility what goes in there. I could either have a number, or I could have several fields with names, or I could have fields that themselves are vectors and matrices. NumPy is very rich in that sense. But it has absolutely no semantics whatsoever for describing the geometry of those dimensions. They're just direction 0, 1, 2, 3, 4, 5.

If you have a four-dimensional array and you want to do some indexing along the third dimension, you have to count commas in your square brackets. If you write complicated code that does a lot of indexing, all of those commas are everywhere. And if halfway through your project you decide that you need to add an extra dimension in the middle, now you have to track everywhere, make sure that all of those operations have been properly updated and offset as you added in the dimension. We have no semantics on those. And this is a problem in practice, just in practice for me.

So what we've been playing with at UC Berkeley was a prototype of what would be the minimal set of ideas that we could add to NumPy to give us enough semantic control over the geometry of the arrays that could be pushed into NumPy itself, something that would be lightweight enough that it would be realistic to push it back into NumPy. So this isn't anywhere nearly as sophisticated as pandas, but hopefully later in the BoF today we'll discuss these ideas to find what of all of this can go eventually into NumPy so that then pandas and statsmodels and whatnot can build the more application-specific objects.

I'm going to quickly show you basically a couple of examples from the documentation. Simply, these are the actual examples. What we have now is a real working prototype, thanks to the fact that at Berkeley a software developer, Mike Trumpy, over the last three or four weeks has worked a lot on actually implementing this. I started this about a year ago. We had a lightning talk. Matthew Brett, Jonathan Taylor, and I had very little time to actually make a few afternoons worth of progress. And then the last few weeks Mike Trumpy at Berkeley has implemented most of it with the help of Stefan last week.

So what we have is this. The idea is we want to be able to name the axes of an array. And if that's all you want, names, this is all you need to do: you simply name your axes. You say, I want my labels to be A, B, and C. You have these labels. And then you can operate on that axis by names, and you can do all of your standard operations by name.

Now, in addition, you can have possibly unnamed axes. This is important so that you can support things like broadcasting. NumPy arrays tend to grow dimensions on the fly when certain operations are done. So axes can be unnamed, and they can be named later. But in addition to simply unnamed axes, your axes can, if you want to, also have data associated with them. So this would be an example of an object that has two axes, capitals and time. We now think of these as ticks along each axis. And the overhead of this object is a little bit higher than the overhead of just having the names, but it's still fairly lightweight.

And if you have a look at the documentation, we've basically implemented most of the normal semantics of slicing, et cetera, of the arrays. And later today in the BoF we'll try to go in detail over these ideas to see what of this we can bake eventually into NumPy. But this should be considered not production code, but a prototype so that we can have a useful discussion. Thanks.
