---
title: "PyData NYC (I gave a machine learning talk! yay!)"
date: 2014-11-27
url: https://jvns.ca/blog/2014/11/27/pydata-nyc-i-gave-a-machine-learning-talk-yay/
slug: pydata-nyc-i-gave-a-machine-learning-talk-yay
word_count: 658
---


This past weekend I went to PyData NYC. It was super fun! I got to meet
some people who do machine learning in different fields than me (THE
BEST) and a guy at the bar told me about his classmates’ adventures in
hacking login systems in Novell Netware. (Also the best. It turns out
that one of the nice things about having a blog is that people
occasionally come up to me at conferences and tell me GREAT THINGS).


And I gave my first-ever machine learning talk! I often feel like the
main (only?) thing I’ve learned about machine learning so far is how
important it is to evaluate your models and make sure they’re actually
getting better. So I gave a talk called “Recalling with precision” about
that (a terrible pun courtesy of
[@avibryant](http://twitter.com/avibryant)).


The basic structure:

1. You’re building models, and you do lots of experiments
2. You want to remember all of the results forever, so that you can tell
if you’re improving
3. Some arguments for why it’s important to evaluate whether your models
actually work (for an example of what can go wrong, see [The Value Added Teacher Model Sucks](http://mathbabe.org/2012/03/06/the-value-added-teacher-model-sucks/)).
4. “Just remember everything forever” is much easier said than done
5. So let’s describe a lightweight system to actually remember some
things forever! (basically: store training results in S3 forever;
make a webapp to draw [lots of graphs](https://github.com/stripe/topmodel) using those results)
6. It exists! It’s open source. [http://github.com/stripe/topmodel](http://github.com/stripe/topmodel)


(It’s still pretty new. If you try it and have thoughts,
[let me know?](mailto:julia@stripe.com))


People asked lots of questions, so I think it may have been useful. It’s
hard to tell, with talks :)


Some things I learned at PyData: (links largely taken from
[Michael Becker’s great wrap-up post](https://mdbecker.github.io/blog/2014/11/24/pydata-nyc-the-really-short-version/))


## csvkit is great


[Sasha Laundy](http://blog.sashalaundy.com/) (who is fantastic) gave a
totally wonderful talk called [“How to make your future data scientists
love you”](http://blog.sashalaundy.com/talks/data-audit/). She told some
great data horror stories about missing data, data that you can’t join,
and talked about some basic tools for auditing datasets to make sure
that it’s actually possible to answer questions about data. And she
talked about practical, useful tools like
[csvkit](https://csvkit.readthedocs.org/en/0.9.0/)! I have already
discovered that it includes the amazing `csvlook` which will format your
csv in a human-readable table.


Her talk reminded me of when I used to work for a consulting company and
how hard it is to communicate with clients about what data they need to
provide for you to be able to answer the questions. Communication is
*hard*.


## Automatically training models?


I’m usually pretty skeptical when people talk about automatically
training models. [Dan Blanchard](https://dan-blanchard.github.io/)
described a [framework called SKLL](https://scikit-learn-laboratory.readthedocs.org/en/latest/) for
using scikit-learn a little more easily which seemed plausible to me.
Basically you tell it which models you’re interested in experimenting
with (decision trees? random forests? SVM?), make a config file, and
it’ll train all of them and give you predictions and serialized models.


It has a [well-written tutorial](https://scikit-learn-laboratory.readthedocs.org/en/latest/tutorial.html#titanic-config).
Good documentation makes me so happy.


## Blaze: a different way to run queries


I talked to the folks at Continuum Analytics a little bit about Blaze.


As I understand it, it’s a library that translates pandas-like queries


```
negative_balances = t[t.balance < 0]
negative_balances[['user', 'date', 'balance']]

```


into SQL queries


```
SELECT merchant, date, balance
FROM table
WHERE balance < 0

```


And it supports more than one database backend! Like CSVs, HDF5 files,
and maybe some other weird formats.


I’m still not sure if it’s useful to me and it’s in a pretty early
stage. But, neat!


### Things I missed


A few things I want to remind myself to look at later:

- [Monary: Really fast analysis with MongoDB and NumPy](http://pydata.org/nyc2014/abstracts/#294) (because “really fast analysis” and “MongoDB”? really?)
- [Advanced IPython Notebook widgets](http://pydata.org/nyc2014/abstracts/#316) (because I’ve been trying to learn about these interactive widgets *forever*)
- [On building a data science curriculum](http://pydata.org/nyc2014/abstracts/#331) (in case I ever want to teach a class)
