---
title: "List And Hash"
description: "It's now common in many programming environments to represent data structures as a   composite of lists and hashmaps. Most major languages now provide   standard versions of these data structures, tog"
date: 2015-12-03T00:00:00
tags: ["language feature"]
url: https://martinfowler.com/bliki/ListAndHash.html
slug: ListAndHash
word_count: 748
---


It's now common in many programming environments to represent data structures as a
  composite of lists and hashmaps. Most major languages now provide
  standard versions of these data structures, together with a rich
  range of operations, in particular [Collection Pipelines](https://martinfowler.com/articles/collection-pipeline), to
  manipulate them. These data structures are very flexible, allowing us to represent
  most forms of hierarchy in a manner that's easy to process and
  manipulate. 1


1: 
      I find it awkward that there's no generally accepted,
      cross-language term for this kind of data structure. I could do
      with such a term, hence my desire to make a [Neologism](https://martinfowler.com/bliki/Neologism.html)


![](images/listAndHash/listAndHash-01.png)


The essence of this data structure is that there are (usually) two
  composite data types:

- Hashmaps are a key-value data structure, which may be called
    associative arrays, hashtables, maps, or dictionaries.
- Lists are simple sequences. They're not quite the same as
    traditional arrays as they dynamically resize as you add or remove
    elements (some languages do call them arrays, however). They can
    be indexed by integer keys.


The leaves of the tree can be any other element, commonly the
  basic primitives in the language (such as integers and strings),
  but also any other structure that isn't treatable as a list or
  hash.


In most cases there are separate data types for the list and
  hash, since their access operations differ. However, as any lisper
  can tell you, it's easy to represent a hash as a list of key-value
  pairs. Similarly you can treat a hash with numeric indexes as a list
  (which is what Lua's tables do).


A list 'n' hash structure is by default schemaless, the lists can contain disparate
  elements and the hashes any combination of keys. This allows the data structure to be
  very flexible, but we must remember that [we nearly always have an implicit schema](https://martinfowler.com/articles/schemaless/#implicit-schema)
  when we manipulate a schemaless data structure, in that we expect certain data to be
  represented with certain keys.


A strength of the list and hash structure is that you can
  manipulate it with generic operations which know nothing of the
  actual keys present. These operations can then be parameterized with
  the keys that you wish to manipulate. The generic operations,
  usually arranged into a collection pipeline, provide a lot of
  navigation features to allow you to pluck what you need from the
  data structure without having to manipulate the individual pieces.


Although the usual way is to use flexible hashes for records, you
  can take a structure that uses defined record structures (or objects) and
  manipulate it in the same way as a hash if those record structures provide reflective
  operations. While such a structure will restrict what you can put in
  it (which is often a Good Thing), using generic operations to
  manipulate it can be very useful. But this does require the language
  environment to provide the mechanism to query records as if they are
  hashes.


List and hash structures can easily be serialized,
   commonly into a textual form. JSON is a
  particularly effective form of serialization for such a data
  structure, and is my default choice for this. Often XML is used to
  serialize list 'n' hash structures, it does a serviceable job, but
  is verbose and the distinction between attributes and elements makes
  no sense for these structures (although it makes plenty of sense for
  marking up text).


Despite the fact that list 'n' hashes are very common, there are times I wish I was
  using a thoughtful tree representation. Such a model can provide richer navigation
  operations. When working with the serialized XML structures in [Nokogiri](http://www.rubydoc.info/github/sparklemotion/nokogiri), I find it handy to
  be able to use XPath or CSS selectors to navigate the data structure. Some kind of
  common path specification such as these is handy for larger documents. Another issue is
  that it can be more awkward than it should to find the parent or ancestors of a given
  node in the tree. The presence of rich lists and hashes as standard equipment in modern
  languages has been one of the definite improvements in my programming life since I
  started programming in Fortran IV, but there's no need to stop there.


## Acknowledgements

David Johnston, Marzieh Morovatpasand, Peter Gillard-Moss, Philip Duldig, Rebecca
    Parsons, Ryan Murray, and Steven Lowe

    discussed this post on our internal mailing list.

## Notes


1: 
      I find it awkward that there's no generally accepted,
      cross-language term for this kind of data structure. I could do
      with such a term, hence my desire to make a [Neologism](https://martinfowler.com/bliki/Neologism.html)
