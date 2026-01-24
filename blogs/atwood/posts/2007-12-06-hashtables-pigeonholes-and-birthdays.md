---
title: "Hashtables, Pigeonholes, and Birthdays"
date: 2007-12-06
url: https://blog.codinghorror.com/hashtables-pigeonholes-and-birthdays/
slug: hashtables-pigeonholes-and-birthdays
word_count: 960
---

One of the most beloved of all data structures in computer science is the [hash table](http://en.wikipedia.org/wiki/Hash_table).


> A hash table is a data structure that associates keys with values. The primary operation it supports efficiently is a lookup: given a key (e.g. a person’s name), find the corresponding value (e.g. that person’s telephone number). It works by transforming the key using a hash function into a hash, a number that is used to index into an array to locate the desired location (“bucket”) where the values should be.


Key-value pairs are quite common in real world data, and hashtables are both reasonably efficient in storage and quite fast at lookups, offering O(1) performance in most cases. That’s why hashtables are the go-to data structure for many programmers. It may not be the optimal choice, but unlike so many things in computer science, it’s rarely a *bad* choice.


But hash tables do have one crucial weakness: **they are only as good as the hash function driving them**. As we add each new item to the hash table, we compute a hash value from the key for that item, and drop the item in the bucket represented by that hash value. So how many buckets do we need? Let’s consider the extremes:

- If we had **one giant bucket**, everything would get piled in together. We’d have to look at each and every item in our one bucket to find the one we want, which reduces us to worst-case performance: an O(n) linear search.
- If we had **exactly the same number of buckets as items**, each item is placed in its own unique, individual bucket. We know each bucket will contain one, and *only* one, item. That’s a perfect hash function, delivering best-case performance: an O(1) lookup.


Reality, of course, lies somewhere in between these two extremes. The choice of hash function is critical, so you don’t end up with a bucket shortage. As you place more and more items in each bucket (i.e., "collisions") you edge closer to the slow O(n) end of the performance spectrum.


There’s something magical about these hash functions that drive the hash table. The idea of the hash as a [unique digital fingerprint](http://haacked.com/archive/2007/01/22/Identicons_as_Visual_Fingerprints.aspx) for every chunk of data in the entire world is a fascinating one. It’s a fingerprint that cleverly fits into a mere 32 bits of storage, yet is somehow able to uniquely identify any set of data ever created.


Of course, **this is a lie**, for several reasons. Let’s start with the most obvious one. Consider all possible values of a 32-bit hash function:


232 ~= 4.3 billion


The current population of the earth is about 6.6 billion people. If we were to apply a *perfect* 32-bit hash function to the DNA of every man, woman, and child on the planet, we could not guarantee uniqueness – **we simply don’t have enough possible hash values to represent them all!**


This is known as the [pigeonhole principle](http://en.wikipedia.org/wiki/Pigeonhole_principle). It’s not complicated. If you try to put 6 pigeons in 5 holes, one will inevitably be left out in the cold.


![](https://blog.codinghorror.com/content/images/2025/07/packages-in-postage-slots-beamish-open-air-museum-county-durham-england.jpg)


You’ll definitely want to **use a large enough hash value** so you can avoid the pigeonhole principle. How much you care about this depends on how many things you’re planning to store in your hashtable, naturally.


The other reason hashes can fail as digital fingerprints is because **collisions are a lot more likely than most people realize**. The [birthday paradox](http://en.wikipedia.org/wiki/Birthday_paradox) illustrates how quickly you can run into collision problems for small hash values. I distinctly remember the birthday paradox from [my college](http://www.virginia.edu/) calculus class, and I’ll pose you the same question our TA asked us:


> In a typical classroom of 30 students, what are the odds that two of the students will have the same birthday?


Don’t read any further until you’ve taken a guess. What’s your answer?


![2007 chinese calendar](https://blog.codinghorror.com/content/images/uploads/2007/12/6a0120a85dcdae970b0120a86da9db970b-pi.png)


Everyone has completely unique DNA, but shares one of 365* possible birthdays with the rest of us. **Birthdays are effectively a tiny 365 value hash function.** Using such a small hash value, there’s a 50% chance of two people sharing the same birthday after a mere *23 people*. With the 30 students in our hypothetical classroom, the odds of two students having a shared birthday rise to 70%. The statistics don’t lie: when the question was posed in that classroom so many years ago, there were in fact two students who shared the same birthday.


A rule of thumb for estimating the number of values you need to enter in a hashtable before you have a 50 percent chance of an existing collision is to take the square root of 1.4 times the number of possible hash values.

kg-card-begin: html

```

SQRT(1.4 * 365) = 23
SQRT(1.4 * 232) = 77,543

```

kg-card-end: html

When using a 32-bit hash value, we have a 50% chance that a collision exists after about 77 thousand entries – a pretty far cry from the 4 billion possible values we could store in that 32-bit value. This is not a big deal for a hashtable; so what if a few of our buckets have more than one item? But it’s a huge problem if you’re relying on the hash as a unique digital fingerprint.


The hashing functions behind our precious hashtables may be a lie. **But they’re a *convenient* lie.** They work. Just keep the pigeonhole principle and the birthday paradox in mind as you’re using them, and you’ll do fine.


*No, let’s forget leap years for now. And other variables like birth patterns. Yes, I know this is how programmers think. Imagine how much it would suck to have one birthday every four years, though. Ouch.

[data structures](https://blog.codinghorror.com/tag/data-structures/)
[hash table](https://blog.codinghorror.com/tag/hash-table/)
[hash function](https://blog.codinghorror.com/tag/hash-function/)
[efficiency](https://blog.codinghorror.com/tag/efficiency/)
[performance](https://blog.codinghorror.com/tag/performance/)
