---
title: "Awesome NLP tutorials by Allison Parrish"
date: 2017-06-17
url: https://jvns.ca/blog/2017/06/17/allison-parrish/
slug: allison-parrish
word_count: 648
---


I love fun programming tutorials, and I love the Jupyter notebook for showing how to do cool Python stuff. So I was
really happy this morning when I saw [Allison Parrish](http://www.decontextualize.com/) (who makes a lot of delightful
computer-generated language art) post these tutorials she’s written (which mostly use the Jupyter notebook) about how to parse and generate English text this morning!


First, some links to cool stuff Allison has done:

- [her awesome website with a billion cool links](http://www.decontextualize.com/)
- Her !!Con talk [lossy text compression, for some reason?!?!](https://youtu.be/meovx9OqWJc) (which is basically about using JPEG compression to compress text, with weird and wonderful results. It’s 10 minutes, watch it, really)
- [The Ephemerides](https://twitter.com/the_ephemerides) is a lovely Twitter bot that posts computer-generated poems and pictures from space
- [everyword](https://twitter.com/everyword) tweeted every word in the English language
- [awesome transcript of “Exploring (Semantic) Space With (Literal) Robots”](http://opentranscripts.org/transcript/semantic-space-literal-robots/), a talk by her about computer-generated poetry.
- A game called [rewordable](http://rewordable.com/) that I want to buy


And now the tutorials! To start, there’s this a  basic intro to [working with CSV files in Python](https://gist.github.com/aparrish/f8e7eab47542678a39a39dddbca4ec2f) (which is extremely useful, but I know that.


Here are the links to the 4 tutorials I was really excited about if you just want the links and don’t care what I have to say about them :)

- [Tracery tutorial](http://air.decontextualize.com/tracery/)
- [Working with Tracery in Python](https://gist.github.com/aparrish/73c19a36b9cdcf604d04e95020418cd4)
- [NLP concepts with spaCy](https://gist.github.com/aparrish/f21f6abbf2367e8eb23438558207e1c3)
- [Understanding word vectors](https://gist.github.com/aparrish/2f562e3737544cf29aaf1af30362f469)


### Text generation


First! Suppose you want to generate random text, like “I’m a banana, not a cucumber”. You could do this by writing like `"I'm a %s, not a %s" % ("banana", "cucumber")`, but you’ll run into problems fast because it’s “I’m *an* apple”, not “I’m a apple”.


It turns out that there’s a cool library called Tracery to help you with text generation. Allison has 2 cool tutorials about Tracery:

- [Tracery tutorial](http://air.decontextualize.com/tracery/)
- [Working with Tracery in Python](https://gist.github.com/aparrish/73c19a36b9cdcf604d04e95020418cd4)


### Parsing text with spaCy


The next tutorial is [NLP concepts with spaCy](https://gist.github.com/aparrish/f21f6abbf2367e8eb23438558207e1c3). Basically you can take a sentence or paragraph and parse it to figure out what it means! Some example of stuff she explains how to figure out:


Where the sentences are
Whether a word is a verb or a noun or what
Identify more complicated grammar constructs like the “prepositional phrases”  (‘with reason and conscience’, ’towards one another’)


She linked to some [examples](https://github.com/aparrish/rwet-examples/tree/master/spacy) of how to use spacy. I ran the “what they’re doing” example on Pride and Prejudice and it wrote out:


```
Hurst is returning
Bingley is blaming
Collins is coming
Darcy is viewing
Bingley is providing
Wickham is caring
Darcy is viewing
Lady is remaining
Hill is coming

```


So it seems to have done a good job of identifying the characters in Pride and
Prejudice! Neat!


Previously the NLP library I’d heard about was NLTK, and she has this very
useful note in the tutorial:


> (Traditionally, most NLP work in Python was done with a library called NLTK.
> NLTK is a fantastic library, but it’s also a writhing behemoth: large and
> slippery and difficult to understand. Also, much of the code in NLTK is decades
> out of date with contemporary practices in NLP.)


### Understanding word vectors


Ok, the next tutorial is [Understanding word vectors](https://gist.github.com/aparrish/2f562e3737544cf29aaf1af30362f469)


The cool thing I learned from this is that you can programmatically “average”
words like ‘day’ and ’night’ to end up with ’evening’! You can also figure out
which animals are similar and all kinds of really cool stuff. I didn’t know
that you could do this, if you want to know more you should read the excellent
tutorial.


### Fun building blocks for doing text experiments!


I think these 3 things (tracery for generating sentences, spacy for parsing
text, and spacy (again) for seeing which words are similar to each other) seem
like a super awesome way to get started with playing with text!
