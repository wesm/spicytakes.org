---
title: "Metamorphic Testing"
date: 2019-03-25
url: https://www.hillelwayne.com/post/metamorphic-testing/
slug: metamorphic-testing
word_count: 1697
---

Confession: I read the [ACM Magazine](https://queue.acm.org/). This makes me a dweeb even in programming circles. One of the things I found in it is “Metamorphic Testing”. I’ve never heard of it, and nobody I knew heard about it either. But the academic literature was shockingly impressive: many incredibly successful case studies in wildly different fields. So why haven’t we heard of it before? There’s only [one](https://medium.com/trustableai/testing-ai-with-metamorphic-testing-61d690001f5c) article anywhere targeted at people outside academia. Let’s make it two.


## Background


Most written tests use **oracles**. That’s where you know the answer and are explicitly checking that the computation gives you the answer.


```
def test_dist():
    p1 = (0, 3)
    p2 = (4, 0)
    assert dist(p1, p2) == 5

```


In addition to being an oracle test, it’s also a manual test. Somebody sat down and decided specific inputs and specific outputs. As systems get more complex, bespoke manual tests become less and less useful. Each one only hits a single point in a larger state space, and we want something that covers the state space.


This gives us **generative testing**: writing tests that hit a random set of the statespace. The most popular style of generative testing is **property based testing**, or PBT. We find a “property” of the function and then generate inputs and see if the outputs match that property.


```
def test_dist():
    p1 = random_point()
    p2 = random_point()
    assert dist(p1, p2) >= 0

```


The advantage of PBT is that it gives more coverage. The downside is that we’ve lost specificity. This is *not* an oracle test anymore! We don’t know what the answer should be, and the function might be broken in a way that has the same property. We rely on heuristics here.


One big problem with PBT is finding good properties. Most functions have simple, general properties and complex, specific properties. [General properties](https://fsharpforfunandprofit.com/posts/property-based-testing-2/) can be applied to a wider variety of functions but don’t give us much information. More specific properties give more information, but are harder to find and only apply to specific problem domains. If you had a function that determined whether or not a graph is acyclic, what property tests would you write? Would they give you confidence your function is right?


## Motivation


Now take a more complex problem. Imagine we’re trying to write an English speech-to-text (STT) processor. It takes a sound file and outputs the text. How would you test it?


The simplest way is with a manual oracle. Read out a sentence and confirm it gives you that sentence. But this isn’t nearly enough! The range of human speech is *enormous*. It’d be better if we could instead test 1,000 or 10,000 different sound files. Manually transcribing oracles is going to be way too expensive. This means we have to use property-based testing instead.


But how do we generate the inputs? One way would be to create random strings, then run them through a text-to-speech processor (TTS), and then check our STT gives the same text. But, once again, this gives us a very limited range of human speech. Will our TTS give us changes in tone, slurred words, strong accents? If we don’t handle those, is our STT actually that useful? We’re better off sweeping for “wild” text, such as from radio, podcasts, online videos.


Now we have a new problem. Using a TTS meant we started with the transcription. We don’t have that with “wild” text, and we still don’t want to transcribe it ourselves. We’re restricted to using properties instead. So what properties should we test? Some simple ones might be “it doesn’t crash on any input” (good) or “It doesn’t turn acoustic music into words” (maybe?). These properties don’t really cover the “intent” of the program, and don’t increase confidence all that much.


So we have two problems. One, we need a wide variety of speech inputs. Two, we need a way to make them into useful tests without spending hours manually transcribing the speech into oracles.


## Metamorphic Testing


That all treats the output in isolation. What if we embed it in a broader context? For example, if a given soundclip transcibes to output `out`, then we should *still* get output `out` if we:

- Double the volume, or
- Raise the pitch, or
- Increase the tempo, or
- Add some background static, or
- Add some traffic noises, or
- Do any combination of the above.


All of these are “straightforward” transformations we can easily test. For example, for the “traffic noises” test, we can take 10 traffic samples, overlay them on a soundclip, and see that all 11 versions match. We can double or half the volume to turn 11 versions into 33 versions, and double the tempo to get 66 versions. Then we can then scale this up to every soundclip in our database, which helps augment the space of our inputs.


Having 66 versions to compare is useful enough. However, there’s something else here: we don’t need to know what the output is. If all 66 transformations return `out`, the test passes, and if any return something different, the test fails. At no point do we need to check what `out` is. This is really, really big. It dramatically increases the range we can test with very little human effort. We could, for example, download an episode of *This American Life*, run the transformations, and see if they all match.1 We have useful tests *without listening to the voice clip.* We can now generate complex, deep tests without the use of an oracle!


The two inputs, along with their outputs, are all connected to each other. This kind of property spanning multiple inputs/outputs is called a **metamorphic relation**.2 Testing that leverages this is called **metamorphic testing**. For complex systems, it can be easier to find interesting metamorphic relations than interesting single input/output properties.


To be a bit more formal: if we have `x` and `f(x)`, we can make some transformation on `x` to get `x2` and `f(x2)`. In the STT case, we just checked `f(x) = f(x2)`, but we can use whatever relations we want between the two. You could also have MRs like `f(x2) > f(x)` or “`f(x2)/f(x)` is an integer”. Similarly, we can also span more than two inputs, using `f(x)` and `f(x3)`. One example of this might be comparing search engine results with no filters to engine results with one filter and two filters. Most of the case studies I read only use two inputs, because even that is enough to find crazy bugs.


## The Case Studies


Speaking of case studies: How effective is MT in practice? It’s one thing to talk about a technique in abstract, or provide toy examples. Reading case studies is useful for three reasons. First, it shows whether or not this actually works. Next, it shares some potential gotchas if we try to use MT. Finally, it gives us ideas on *how* we can use it. Any MR a case study uses is something we might be able to adapt for our own purposes.


[“Metamorphic Testing: A Review of Challenges and Opportunities”](http://www.cs.hku.hk/research/techreps/document/TR-2017-04.pdf) lists a lot of studies, but they’re all academic papers. Here are a few of the most interesting ones. Articles marked `(pdf)` are, unsurprisingly, PDFs.


## The Problem


Huh, they’re all PDFs.


Finding all of those took several hours. And that ties into the biggest drag on MT adoption: All of the above are **preprints**, or first drafts of eventual academic papers. When I dig into obscure techniques, I always ask “why is it obscure?” Sometimes there’s an obvious reason, sometimes it’s a complex set of subtle reasons, sometimes it’s just bad luck.


In the case of MT the problem is obvious. **Almost all of the info is behind academic paywalls.** If you want to learn about MT, you either need journal access or spend hours hunting down preprints.3


## Learning More


The inventor of MT is [TY Chen](https://www.swinburne.edu.au/science-engineering-technology/staff/profile/index.php?id=tychen). He’s also the driver of a lot of the research. Other names are [Zhi Quan Zhou](https://www.uow.edu.au/~zhiquan/) and [Sergio Segura](http://personal.us.es/sergiosegura/publications/), both of whom have put all of their preprints online. Most of the research is by one of those.


The best starting resource are probably [Metamorphic Testing: A Review of Challenges and Opportunities](http://www.cs.hku.hk/research/techreps/document/TR-2017-04.pdf) and [A Survey on Metamorphic Testing](http://www.lsi.us.es/~segura/files/papers/segura16-tse.pdf). While this article was about Metamorphic *Testing*, researchers have also been applying Metamorphic Relationships in general to a wide variety of other disciplines, such as formal verification and debugging. I have not researched those other uses in depth, but they’re probs also worth looking into.


In terms of application, it should be theoretically possible to adapt most PBT libraries to check metamorphic properties. In fact the first example in the [Quickcheck](https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf) tests a MR, and [this](https://hypothesis.works/articles/testing-optimizers-with-hypothesis/) essay on PBT implicitly uses an MR. *In general* it seems to me that most PBT research focuses on how we effectively generate and shrink inputs, while MT research is more focused on determining what we actually want to test. As such they are probably complementary techniques.


*Thanks to [Brian Ng](https://twitter.com/sindarknave) for help researching this.*


### PS: Request


It’s not actually that surprising that I never heard of this before. There’s a lot of really interesting, useful techniques that never leave their tiny bubble. Learning about MT was more luck than any action on my part.


If you know of anything you think deserves wider use, please [email](mailto:h@hillelwayne.com) me.


---

1. Okay, there’s obvious problems here, because the podcast might have music, samples in other languages, etc. But the theory is sound: given we have a way of acquiring speech samples, we can use it as part of tests without having to manually label it first.
 [return]
2. The corresponding idea in specifications is **hyperproperties**, properties on sets of behaviors instead of individual behaviors. Most HP research is concerned with security hyperproperties. As I understand it HPs are a superset of MRs.
 [return]
3. I had a second, refuted hypothesis: since a lot of the major researchers are from China and Hong Kong, maybe the technique was more well-known in Mandarin-language programming communities than English-language ones. [Brian Ng](https://twitter.com/sindarknave) was kind enough to check for me and didn’t find significant use.
 [return]
