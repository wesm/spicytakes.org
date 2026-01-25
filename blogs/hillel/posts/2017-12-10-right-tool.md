---
title: "What's the Right Tool for the Job?"
date: 2017-12-10
url: https://www.hillelwayne.com/post/right-tool/
slug: right-tool
word_count: 2137
---

“Use the right tool for the job” is a pretty tired cliche. Mostly it’s used to dismiss overengineering and one-size-fits-all solutions to problems, like using microservices for your 10-user app. It isn’t a bad saying, it’s just tautologically true. I don’t think anybody wants to use the wrong tool for the job, unless they’re trying to sabotage it. “Should I use the right tool for the job?” is a rhetorical question.


“What’s the right tool for the job?” is a much more fun question. Imagine someone says “Which datastore should I use for my startup: Postgres or MongoDB?” I’d probably say Postgres and give a bunch of reasons why. But what if someone else comes in and says “MongoDB”? They could probably give a bunch of good reasons, too. After all, [five years ago](https://www.nemil.com/mongo/1.html) it was The Future of Databases! How can I reasonably claim that Postgres is the right tool? And what about the [300 other database engines](https://db-engines.com/en/ranking)?


To some extent you can satisfice: say Postgres may not be the perfect fit, but it’s good enough. But that doesn’t solve the problem: how do we decide what’s “good enough”? Is MongoDB good enough? Memcache? [TinyDB](http://tinydb.readthedocs.io/en/latest/intro.html)? At some point you need to answer the question.


Here’s some answers I’ve seen and some thoughts on them.1


### Requirements


First things first is the sanity check. Often you can rule out tools (or more rarely, decide on one) solely based on the requirements you have. You are not going to use Mongo for bank accounts, because you need complex transactions. You wouldn’t use Excel or Haskell in embedded hardware. You wouldn’t use regex to parse HTML.


Rarely, you find the right tool with requirements alone. Usually you’ll still have a bunch of candidates. Let’s move on.


### Experience


This is probably the simplest answer: “I have experience with Postgres. I know it works.” It’s a pretty fast heuristic and in many cases works just fine.


On the other hand, can you really trust yourself? You only have a limited frame of reference and all the squishy meat biases that make us believe dumb things. Personal story: I thought PHP was God’s gift to mankind and brushed off all the arguments against it with “I use the right tool for the job”. In retrospect, the reason I thought it was so great was because the only other languages I knew at the time were C++ and Matlab.2 After I learned Python I realized that PHP was actually pretty cruddy.


I know Dunning-Kruger is often overused3 but I think it applies here. We’re bad at objectively judging ourselves. There’s only a weak correlation between how much you believe you understand something and how much you actually do. We need to recognize the limits of our experience, which means finding some other way to decide.


### Authority


Listening to an authority. Also known as “trusting someone else’s experiences”. This is A Bad Idea for all of the same reasons that trusting your own is. If you don’t believe me, here’s Ken Thompson saying [safer languages are dumb](https://twitter.com/danluu/status/885214004649615360) and here’s Guido Van Rossum saying [map and filter are dumb](https://www.artima.com/weblogs/viewpost.jsp?thread=98196).


Most authorities are really, really good at what they do. But they still have the same limits of experiences and biases we do, and we shouldn’t just take them on their word.


### Abstract Arguments


The vast majority of information produced is people using “reason”, aka abstract arguments. From a [pro-Mongo article](https://www.mongodb.com/post/36151042528/post-transactional-future):

- The majority of ‘operational’ data is non-relational
- Schema data is hard to refactor
- You rarely need transactions.


On the other hand, from an [anti-Mongo article](https://www.stavros.io/posts/startup-mistakes-datastore/):

- The majority of ‘business case’ data is relational
- Schemaless data is hard to refactor
- You always need transactions.


Two sets of abstract arguments saying the exact opposite things. Who do you believe? Without any outside information, we tend to agree with who made the better argument. In practice that’s the better writer. If all you’ve got is “reason”, the Right Tool may be “whichever has the best marketing.”


Fortunately, we can do much better than abstract arguments. We can actually support our claims with evidence. Korokithakis brought in a lot more evidence than Asay did. That’s a better path to finding the right tool.


“But how can we trust evidence?” I don’t know, I’m not a philosopher. I guess we could say that knowledge isn’t a “thing” so we can’t play the same languages games with–4


“But how can we trust *this piece* of evidence?” Okay that I can answer. Let’s list some pieces.


### Examples


**Examples** are self-contained demonstrations of a tool. They require minimal contextual knowledge to understand. Most often they are created for the sole purpose of being evidence, unlike f.ex case studies (which often are byproducts of software development). [Kyle Banker](https://web.archive.org/web/20120518223623/http://kylebanker.com/blog/2010/04/30/mongodb-and-ecommerce/) uses one to show how easily Mongo handles shopping carts:


```
{'_id': objectid('4b980a6dea2c3f4579da141e'),
 'user_id': objectid('4b980a6dea2c3f4579a4f54'),
 'state': 'cart',

 'line_items': [
    {'sku': 'jc-432',
     'name': 'John Coltrane: A Love Supreme',
     'retail_price': 1099
    },

    {'sku': 'ly-211',
     'name': 'Larry Young: Unity',
     'retail_price': 1199
    },
  ],

 'shipping_address': {
   'street': '3333 Greene Ave.',
   'city': 'Brooklyn',
   'state': 'NY',
   'zip': '11216'
  },

  'subtotal': 2199
}

```


Here we’ve got some query that, he claims, would require a bunch of nasty joins across multiple SQL tables, while the Mongo shopping cart is a single object. He argues this means Mongo is easier to work with.


I love examples. I spend a lot of time [thinking](https://twitter.com/Hillelogram/status/935944661201510401) about [examples](https://www.hillelwayne.com/post/persuasive-examples). I think a good example is worth a hundred abstract arguments. But examples are contrived. This makes them easily explainable and good for showcasing things, but they don’t completely reflect reality. The writer can choose which parts of the real world they reproduce and this, unconsciously or not, can rig the evidence. If an example would undermine the writer’s point, they can simple *choose not to present it*, or tweak it to look better.


Let’s go back to the Mongo example above. Banker also talks about how easy aggregation is:


```
map = "
  function() {
    emit(this['shipping_address']['zip'], {total: this.total})
  }"

reduce = "
  function(key, values) {
    var sum = 0;
    values.forEach(function(doc) {
      sum += doc.total;
    }

    return {total: sum};
  }"


db.orders.mapReduce(map, reduce, {out: 'order_totals_by_zip'});

```


Is this really better for reporting than `SUM` and `GROUP BY`? What if you needed to add the top three totals for each zip? What if you need to find the best-selling item in each zip, or the item with the highest deviation? By slightly tweaking the example we can make it more pro- or anti-subject.


### Case Studies


**Case studies** are analyses of real-world systems. Sometimes the system was created for the purpose of providing a case study, more often the case study is a happy byproduct. Case studies are some of the strongest evidence that the average person can produce, because they can faithfully represent all of the tradeoffs in a tool. They also (in theory) can’t be ignored: the downsides of an approach can’t be argued away by ‘reason’. Probably the most famous anti-Mongo article is Sarah Mei’s [Diaspora Case Study](http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb/). She identifies the issues they had with MongoDB:

- Most of their data ended up being relational
- Making SQL more performant was easier than making Mongo more constistant
- Their non-relational data *also* turned out to be relational


Score one for Korokithakis! His reasoning is backed by the evidence of reality.


Case studies are great and we should write more. At least, we need to write more *good* case studies, and it’s easy for even an experienced person to write a bad one. Making a good case study is exhausting. You need to first build the system, then analyze it, and then make sure you have as much detail as possible. Often, you can bias a case study by just leaving stuff out. You can also bias it by not exploring the counterfactuals: showing that “A” is not just better than “nothing”, but also better than “B”. You see this a lot with microservices articles. The writer is really enthusiastic about how microservices worked better for them than a monolith… after they invested a ton of time into transitioning to microservices. What if they instead invested that time into redesigning the monolith? I’ve never seen any comparisons of that; if you have any, [send them my way](mailto:h@hillelwayne.com?subject=Your essay is dumb Hillel, why are you so dumb?).


There’s an uglier, more dangerous issue with case studies. Just as you can tweak examples, you can rig case studies. [Business Insider](http://www.businessinsider.com/how-we-use-mongodb-2009-11) has a case study where they found Mongo a great fit. In the full disclosure, though, they mention that Business Insider and 10gen (the creators of Mongo) share a cofounder. Sure, the author says “I [still] believe it’s the best technology for us”, but Mongo was only officially released just nine months before the BI article. According to [Nemil Dalal](https://www.nemil.com/mongo/3.html) 10gen consistently used case studies as a marketing tactic, meaning many pro-Mongo case studies should be treated with caution.


One way to identify biased case studies is to see how “fair” they are. Mei talks about why Mongo was a good idea at first, then what the workarounds to their initial problems were, and then finally what Mongo’s effective use case is. Even though she’s strongly anti-Mongo, she’s willing to talk about the good aspects. On the other hand, BI lists the flaws as “it lacks transactions, so banks shouldn’t use it”, and “it’s not good if your legacy system relies on SQL”. These ‘flaws’ don’t show balance or a well-rounded case study.


The final issue with case studies is they’re pretty hard to find. You ideally want a few so you can see patterns or correct for biases in individual cases, but for niche problems you might only find one or two. I’ve started bookmarking all the good studies I read, regardless of whether it’s actually useful, just in case I ever need it.


### Formal Research


Controlled studies, [obsessive benchmarking](https://www.techempower.com/benchmarks/), experiments on undergrads, all that fun stuff. A full academic study is, *in theory*, the best we can aspire to.


In practice, we’re not quite there yet. First of all, most software engineers don’t really respect research. It’s a common meme that there’s no way to [measure software engineering](https://redfin.engineering/measure-job-satisfaction-instead-of-software-engineering-productivity-418779ce3451). Second, most papers are inconclusive with many factors of error. If a paper sees no difference between bugs in static and dynamic type systems, was it because there is no difference? Small sample size? Wide variations in programmer abilities? The specific type system? The scope of the exercise? Amount of time they had?


Both of these are solvable problems, but they’re both symptoms of the third and biggest problem: software engineering research is hard. Really hard. The [Software Engineering Institute](https://sei.cmu.edu/index.cfm) is one of the biggest institutes in the USA and we pour [300 million](https://www.cmu.edu/news/stories/archives/2015/july/sei-contract-renewed.html) into it every year.5 Sure, they do stuff besides academic research, but still. You have to spend a lot of time and money to get even marginal results.


Formal Research is a definite nice to have, but I wouldn’t count on having it for any given question.


---


So where does that leave us? I’m seeing a tradeoff of ease vs rigour here. For most small decisions you’re fine just using experience. Otherwise, in my experience (ha!) case studies are the gold standard. They’re more informative than everything but conclusive research, which is almost never available. Plus, unlike research, “laypeople” can produce useful case studies: you’re presumably doing something at work, and it’s usually possible to turn “here’s what I did this quarter” into something people can learn from. Note to self: write some case studies.


One other interesting thing: I feel (but am not certain) that while examples are considerably more rigorous than abstract argument, they aren’t much harder to create. So if you’re writing about a tool and are primarily using abstract arguments, back them all up with examples to make your case stronger.


---

1. A lot of these examples are going to involve MongoDB. I don’t have any opinions on it (aside from distaste for the former hype), but it makes a fascinating case study. MongoDB came out in 2009, was the Future of Databases by 2013, and now is a punchline. It’s a very neat timeline. Also, so many ‘primary sources’ are online, unlike earlier computing fads.
 [return]
2. I majored in physics and the lab used C++. Do not make C++ your first language.
 [return]
3. And [misused](https://danluu.com/dunning-kruger/).
 [return]
4. [Witt’s Vipers!](https://en.wikipedia.org/wiki/Philosophical_Investigations)
[return]
5. Actually, I’m not sure if that’s annual or total? Based on [DoD press releases](https://www.defense.gov/News/Contracts/Contract-View/Article/612899/), I think they’re talking about [this](http://government-contracts.insidegov.com/l/11701911/FA870215D0002) contract, but it’s a lump sum for 500 million. Can someone better at this than I am [let me know](mailto:h@hillelwayne.com?subject=Hey idiot you clearly don't know how to read a contract) if I understand correctly? Thanks!
 [return]
